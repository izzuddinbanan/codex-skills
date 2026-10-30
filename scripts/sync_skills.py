"""Export user skills, record content versions, and optionally commit/push."""
import argparse
from datetime import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

REMOTE = 'https://github.com/izzuddinbanan/codex-skills.git'
EXCLUDED_PARTS = {'.git', '__pycache__', 'node_modules', '.venv', '.system'}
SECRET = re.compile(rb'(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,}|sk-(?:proj-)?[A-Za-z0-9_-]{40,}|-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----)')


def collect(source):
    result = {}
    for skill in sorted(source.iterdir()):
        if not skill.is_dir() or skill.name.startswith('.') or not (skill / 'SKILL.md').is_file():
            continue
        files = {}
        for file in sorted(skill.rglob('*')):
            if file.is_symlink():
                raise ValueError(f'Symlink requires review: {file}')
            if not file.is_file() or any(part in EXCLUDED_PARTS for part in file.relative_to(skill).parts):
                continue
            if file.suffix in {'.pyc', '.bak', '.log'} or file.name == '.DS_Store':
                continue
            if file.name == '.env' or (file.name.startswith('.env.') and file.name != '.env.example'):
                raise ValueError(f'Private environment file requires review: {file}')
            data = file.read_bytes()
            if SECRET.search(data):
                raise ValueError(f'Possible credential detected; export blocked: {file}')
            files[file.relative_to(skill).as_posix()] = data
        result[skill.name] = files
    if not result:
        raise ValueError('No user skills found; refusing an empty export')
    return result


def digest(files):
    hasher = hashlib.sha256()
    for name, data in sorted(files.items()):
        hasher.update(name.encode() + b'\0' + data + b'\0')
    return hasher.hexdigest()


def snapshot(source, repo, reason, evidence, validation):
    # Inspect every candidate before writing any exported skill.
    candidates = collect(source)
    manifest_path = repo / 'versions.json'
    previous = json.loads(manifest_path.read_text(encoding='utf-8')) if manifest_path.exists() else {'skills': {}}
    previous_skills = previous['skills']
    if set(previous_skills) - set(candidates):
        raise ValueError('Installed skills are missing from source; review removal manually')
    current = {'skills': {}}
    changed = []
    for name, files in candidates.items():
        checksum = digest(files)
        old = previous_skills.get(name)
        if old and old['sha256'] == checksum:
            current['skills'][name] = old
        else:
            version = '1.0.0' if not old else '.'.join(old['version'].split('.')[:2] + [str(int(old['version'].split('.')[2]) + 1)])
            current['skills'][name] = {'version': version, 'sha256': checksum}
            changed.append(f'{name} {version}')
        destination = repo / 'skills' / name
        if destination.exists():
            for existing in destination.rglob('*'):
                if existing.is_file() and existing.relative_to(destination).as_posix() not in files:
                    existing.unlink()
        for relative, data in files.items():
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
    if changed:
        manifest_path.write_text(json.dumps(current, indent=2) + '\n', encoding='utf-8')
        log = repo / 'CHANGELOG.md'
        existing = log.read_text(encoding='utf-8') if log.exists() else '# Skill history\n'
        now = datetime.now().astimezone().isoformat(timespec='seconds')
        entry = f'\n## {now}\n\nReason: {reason}\n\nEvidence: {evidence}\n\nValidation: {validation}\n\n' + '\n'.join('- ' + name for name in changed) + '\n'
        log.write_text(existing + entry, encoding='utf-8')
    return current


def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args], text=True).strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex'))) / 'skills')
    parser.add_argument('--reason', required=True)
    parser.add_argument('--evidence', required=True)
    parser.add_argument('--validation', required=True)
    parser.add_argument('--push', action='store_true')
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]
    if args.push:
        if git(repo, 'remote', 'get-url', 'origin') != REMOTE:
            raise ValueError('Unexpected origin; refusing to push')
        if git(repo, 'branch', '--show-current') != 'main':
            raise ValueError('Sync must run on main')
        git(repo, 'fetch', 'origin')
        refs = git(repo, 'for-each-ref', '--format=%(refname)', 'refs/remotes/origin/main')
        if refs and git(repo, 'rev-list', '--count', 'HEAD..origin/main') != '0':
            raise ValueError('Remote has unseen commits; review and integrate them before publishing')
    result = snapshot(args.source.resolve(), repo, args.reason, args.evidence, args.validation)
    print(f'Exported {len(result["skills"])} user skills; content versions recorded.')
    if args.push:
        # Only repository-owned export and support paths are staged.
        git(repo, 'add', '--', 'skills', 'versions.json', 'CHANGELOG.md', 'README.md', 'THIRD_PARTY.md', 'UPSTREAM.json', 'LICENSES', 'scripts', 'tests', 'config', '.gitignore', 'AGENTS.md')
        if git(repo, 'diff', '--cached', '--name-only'):
            message = 'chore(skills): ' + args.reason.replace('\n', ' ')[:100]
            git(repo, 'commit', '-m', message)
        git(repo, 'push', '-u', 'origin', 'main')
        print('Published commit ' + git(repo, 'rev-parse', 'HEAD'))


if __name__ == '__main__':
    main()
