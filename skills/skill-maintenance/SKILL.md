---
name: skill-maintenance
description: Maintain and version installed personal Codex skills after evidenced workflow failures, user corrections, recurring manual patterns, or validated skill improvements. Use when synchronizing global skills to the personal GitHub repository or updating their version history, including equivalent Malay requests.
---

# Personal skill maintenance

The user authorized ongoing evidence-based improvements to global user skills and direct publication to `https://github.com/izzuddinbanan/codex-skills` on 2026-10-30. This authorization covers this personal skills repository only. It does not authorize pushing application repositories or publishing private memories.

During active work, notice user corrections, actual skill failures, and recurring manual workflows. Read the affected skill before deciding it needs changing. Distinguish a missing instruction from failure to follow an instruction already present. Do not add universal rules from one ambiguous preference or rewrite skills merely to create activity.

For a supported improvement:

1. Record the observed problem, its source, the smallest intended change, and the behavior that should improve. Keep private examples out of public evidence; summarize the general issue.
2. Make a narrow change to the installed user skill under the current Codex home. Retain upstream references, license notices, and automatic invocation. Use skill-creator for authoring guidance. Do not edit built-in system skills or plugin caches.
3. Validate the skill with the installed skill-creator validator and check the relevant workflow against the previous behavior. On Windows run the validator with `python -X utf8` because some upstream skills contain Unicode that the default code page cannot decode. Use actual task evidence or a small controlled fixture; do not claim behavioral tests that were not run. If no useful change is supported, leave the skill unchanged.
4. Review the diff for secrets, private diaries, session memories, unsupported claims, and unintended behavior changes. A snapshot must contain only shareable skills and repository support files.
5. Publish the validated improvement with:

```powershell
python C:/Users/izzud/.codex/skills-repository/scripts/sync_skills.py --reason "Specific improvement" --evidence "Public-safe observed problem" --validation "Checks actually run" --push
```

The script assigns versions by content and appends the change history. The standing user authorization permits this push without asking again. If authentication fails, remote history has unseen changes, validation fails, or there are conflicting edits, stop publication and report the exact issue; preserve local improvements. Never force-push or auto-resolve conflicting instructions. Inspect and integrate remote changes deliberately before retrying.

Review upstream changes when updating a named source or when an actual incompatibility warrants it. Fetch and inspect the diff, preserve personal adaptations, validate, then publish. Never blindly overwrite working local skills with upstream files.

At task completion, sync only if installed skills actually changed. Save private learning evidence to the local MemoryCore separately from public version history. No background daemon, schedule, or autonomous learning model is implied: this workflow operates while Codex is running and has these instructions available.
