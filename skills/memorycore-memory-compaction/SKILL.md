---
name: memorycore-memory-compaction
description: "MUST use when user says 'compact memory', 'compact [file]', 'check budgets', 'set budget', 'restore compaction', or before any 'save' whose target memory file exceeds its budget in compaction/compaction-policy.md. Match equivalent Malay requests by intent; no explicit skill invocation required."
---

# MemoryCore: memory-compaction

## Codex integration (takes precedence over the upstream reference)

- Memory root: `C:/Users/izzud/.codex/memorycore`. Resolve upstream memory paths (`main/`, `projects/`, `library/`, `daily-diary/`, `topic-diary/`, `compaction/`, `adventures/`, `media-generation/`, and `master-memory.md`) against this root, never against the current repository. Repository code and its own plans remain in their actual project.
- Use Codex tools available in this session; Claude plugin commands, Claude settings, and Claude hook scripts are reference material, not executable setup instructions for Codex.
- Select this skill by the meaning of the request in Malay or English. No skill-name mention or activation phrase is required from the user. Skip ceremonial activation messages; keep useful progress and required approval messages.
- Preserve existing memory. Store only evidenced preferences and useful task context, with project paths and source dates. Keep each project's session in `projects/sessions/<project-key>.md`; the shared `main/current-session.md` is only a brief index. Never treat a different project's session as this project's state. Never store passwords or API keys.
- Use Asia/Kuala_Lumpur for user-facing timestamps. These files provide continuity only when Codex can read them; they are not a background service.
- Skill selection does not authorize unrelated actions. Commit only changes from the authorized task after reviewing the diff, and preserve unrelated user changes. Push only when requested. A reminder is a stored note, not an OS notification or scheduled job.
- Forge proposals may be drafted automatically; changes to other skills or global rules follow the user's approval requirements in the upstream workflow. Prefer existing specialized skills and tools when they already cover the task.


Read [upstream-skill.md](upstream-skill.md) for the workflow. Supporting templates and documentation are beside this file. Apply the Codex integration above wherever upstream assumes Claude or a project-local memory root.
