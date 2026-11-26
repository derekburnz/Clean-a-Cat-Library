# Remaking all eight threads (Derek, 2026-11-26 ET)

Derek deleted every thread to reset context and image limits. Everything a new thread needs is in this repo and the game repo. Roster, models and effort: `setup-drafts-2026-11-23/threads.md` (Derek is on Ultra, so no downgrades; Design-Agent on Opus 5.5 medium, Fable 5.2 high for hard calls). Brief to paste (fill the name):

> You are **[Thread-Name]** in the Clean a Cat project. Read first, in order: `library/[Thread-Name]/[Thread Name].md` and the handoff file beside it in the library repo (derekburnz/Clean-a-Cat-Library), `library/Setup/3-working-rules.md`, the game repo's `CLAUDE.md` (derekburnz/Clean-a-Cat) and the skill for your task in `.claude/skills/`. Project memory is `memory/project-memory.md` there (topic files beside it). Check open `claim` issues and open PRs before starting. Keep your thread md current and push it before any reset.

Handoff file per thread (read it right after the thread md):
- Planning-Agent: `library/Planning-Agent/handoff.md` (plan page files, Derek's answers, open questions).
- Gameplay-Engineer: `library/Gameplay-Engineer/handoff-2026-11-26.md` (parked patches in `wip-2026-11-26/`).
- Design-Agent: `library/Design-Agent/handoff.md`. Rebuilt by Sync-Agent from GitHub because the thread was deleted before it could hand off; items marked UNCONFIRMED there need a check.
- Review-QA-Agent: `library/Review-QA-Agent/handoff-2026-11-26.md`.
- Motion-FX-Agent: handoff in `library/Motion-FX-Agent/` (Motion FX Agent.md and the handoff note merged in library PR 1).
- Model-Agent: `library/Model-Agent/handoff-2026-11-26.md`.
- Growth-Agent: `library/Growth-Agent/handoff.md`.
- Sync-Agent: `library/Sync-Agent/handoff.md` and `studio-session-handoff.md` (Studio on Derek's PC; the RC session needs a fresh start with `start_remote_control`, the PC is DESKTOP-DFOGFG7, the clone is `C:\Users\Derek\Downloads\games\Clean-a-Cat`).

Things a remade thread must know that are easy to miss:
- Dev first: nothing goes live without Derek's confirmation. Feature switches stay OFF on live.
- Picture PRs (Studio screenshots) stay drafts, no assignee, never merged.
- Only Sync-Agent drives Studio. Test movement only with `_G.qaWalkNamed` (skill `studio-test-movement`).
- Memory topic files and the instructions copy in `memory/` are word for word copies: never edit them by hand, only Sync-Agent copies. `memory/project-instructions.md` was refreshed from the project settings on 2026-11-26.
- GitHub MCP tools and some others come and go between turns; load them again through tool search when missing.
- The shared folder `/mnt/project-files/<Thread>/` mirrors `library/<Thread>/`; Sync-Agent copies newer wins, never shrinking a `.md`.
- Thread ids die with the project: never store them.
