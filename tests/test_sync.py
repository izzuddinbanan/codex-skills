import importlib.util
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).parents[1] / 'scripts/sync_skills.py'


class SyncTests(unittest.TestCase):
    def test_versions_are_stable_until_content_changes(self):
        spec = importlib.util.spec_from_file_location('sync_skills', SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / 'source'
            skill = source / 'example'
            skill.mkdir(parents=True)
            content = '---\nname: example\ndescription: A useful example skill\n---\n\nDo the task.\n'
            (skill / 'SKILL.md').write_text(content)
            repo = root / 'repo'
            repo.mkdir()
            first = module.snapshot(source, repo, 'Initial', 'Test fixture', 'Fixture check')
            self.assertEqual(first['skills']['example']['version'], '1.0.0')
            second = module.snapshot(source, repo, 'No change', 'Test fixture', 'Fixture check')
            self.assertEqual(first, second)
            (skill / 'SKILL.md').write_text(content + 'An improved step.\n')
            third = module.snapshot(source, repo, 'Improve step', 'Observed gap', 'Fixture check')
            self.assertEqual(third['skills']['example']['version'], '1.0.1')

    def test_secrets_rejected_before_export(self):
        spec = importlib.util.spec_from_file_location('sync_skills', SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / 'source/example'
            source.mkdir(parents=True)
            (source / 'SKILL.md').write_text('---\nname: example\ndescription: Example\n---\n')
            (source / 'credential.txt').write_text('ghp_' + 'A' * 36)
            repo = root / 'repo'
            repo.mkdir()
            with self.assertRaises(ValueError):
                module.snapshot(source.parent, repo, 'Test', 'Test', 'Test')
            self.assertFalse((repo / 'skills/example').exists())


if __name__ == '__main__':
    unittest.main()
