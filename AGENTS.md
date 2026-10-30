# Maintaining this repository

This repository publishes personal Codex user skills. Do not include private memory, session history, authentication files, environment credentials, system skills, or plugin caches.

For skill changes, record the concrete evidence and expected improvement. Validate frontmatter, supporting resources, and the relevant behavior. Run exporter tests when changing publication logic. Review the staged diff and publish only to the configured personal repository, without force-pushing. Preserve third-party notices and upstream workflows unless a documented Codex adaptation overrides them.

Use scripts/sync_skills.py to export from installed user skills. A GitHub change is not installed locally until it has been reviewed and copied to the actual skill folder. Avoid blind bidirectional synchronization.
