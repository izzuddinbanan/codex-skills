# Personal Codex skills

Versioned snapshots of installed user skills: Superpowers, MemoryCore Codex adapters, Anti Slop, and personal skill maintenance. Codex system skills, plugin caches, credentials, diaries, session memories, and machine settings are excluded.

## Automatic use and improvement

Codex selects relevant skills by prompt intent in Malay or English. The global instructions in `config/AGENTS.md` load memory and the maintenance skill. The learning loop runs during active Codex tasks: notice an evidenced failure or recurring problem, make a narrow improvement, validate it against the previous behavior, record evidence and validation, then publish it here. This is instruction-based automation, not an unattended background learner. Upstream updates require review before integration; they never overwrite personal improvements automatically.

`versions.json` records each skill's content hash and version. First export starts at 1.0.0; changed skill content increments the patch version. Unchanged content retains its version. `CHANGELOG.md` records the reason, evidence, and validation for each export. Git history preserves prior revisions.

## Publish validated local changes

```powershell
python scripts/sync_skills.py --reason "Describe the improvement" --evidence "Describe the observed problem" --validation "Describe checks actually run" --push
```

Without `--push`, this only exports files and updates versions. Run `python -m unittest discover -s tests` to check the exporter. The publisher checks the destination, rejects recognizable credentials, refuses missing installed skills and unseen remote commits, and never force-pushes. Review changes before publishing. Credential detection is limited and does not replace review.

On the original installation, Git currently authenticates as a different account without repository write access. Codex can publish through the connected GitHub app as the repository owner. The maintenance skill documents that fallback. The command above needs correct Git credentials for unattended CLI publication; no tokens are stored in this repository.

## Restore on another machine

Copy the desired folders from `skills/` into your Codex user skills folder, normally `~/.codex/skills`. Review and merge `config/AGENTS.md` into your global `~/.codex/AGENTS.md`; never overwrite existing instructions blindly. MemoryCore adapters currently contain paths for the original Windows installation. Update those paths to the new user's memory root and initialize empty memory files before use. Do not copy another person's private memory.

See `THIRD_PARTY.md` for upstream attribution. Source licenses remain applicable.
