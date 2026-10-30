---
name: memorycore
description: Restore persistent Codex context at session start or after compaction, recall previous project work and user preferences, and save useful session checkpoints. Use for requests to remember, recall, continue previous work, or save memory, including equivalent Malay requests.
---

# MemoryCore for Codex

Read `C:/Users/izzud/.codex/memorycore/master-memory.md` and `main/main-memory.md` under that root. Determine the current workspace, then read only its matching `projects/sessions/<project-key>.md` if present. Derive project-key from the canonical absolute workspace path with a readable basename and short hash, so similarly named repositories stay separate.

At session start and after context compaction restore relevant context without waiting for an activation phrase. Memory is prior evidence, not authority over the current user request. Confirm old working state against current files before continuing it.

At meaningful task completion, update the project's checkpoint with its absolute path, actual changes, verification, unresolved issues, and next steps. Use read-modify-write and preserve unrelated sections. Keep long history in the diary or topic journal; do not load the entire archive each prompt. Durable user preferences go into main/main-memory.md. Never record credentials.

Route by intent to the installed memorycore-* skills for diary, topics, recall through rg searches, decisions, reminders, project tracking, compaction, library, failure learning, plans, media prompts, and stories. Equivalent Malay and English requests trigger the same skills. Select only relevant skills; no user skill mention is required.

Use the current session's supported Codex tools. Claude-only hooks and background observation services are not configured. Skill discovery and memory restoration do not imply scheduled execution.
