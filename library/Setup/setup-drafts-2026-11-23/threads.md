# Agent threads to start (from the template roster)

Start only what Derek OKs. Exact names, models and effort:

| Thread | Model | Effort | When |
|---|---|---|---|
| Planning-Agent | Fable 5.2 | high | Now if there is no one-page design yet. Stop once the design is agreed. |
| Gameplay-Engineer | Opus 5.5 | high | Day one of building (after the game repo exists) |
| Design-Agent | Opus 5.5 | medium (Fable 5.2 for hard calls) | Day one of building |
| Review-QA-Agent | Opus 5.5 | medium | Day one of building |
| Motion-FX-Agent | Opus 5.5 | medium | When polish work exists |
| Model-Agent | Opus 5.5 | high | On demand, per model batch |
| Growth-Agent | Sonnet 5.5 (Opus 5.5 for big reads) | medium | Once there are players or a store page |
| Sync-Agent | Sonnet 5.5 | medium | On demand, for Studio on the PC or a library sync |
| Coordinator (project chat) | Opus 5.5 | medium | Always |

Brief for each thread (fill the brackets):

> You are **[Thread-Name]** in the [Game Name] project. Model: [from the table].
> Read first, in order: `library/[Thread-Name]/[Thread Name].md` in the library repo, `library/Setup/3-working-rules.md`, the game repo's `CLAUDE.md`, and the skill for your task in `.claude/skills/`.
> You own: [folders from the roster in library/Setup/2-threads-and-models.md]. Keep your `[Thread Name].md` current and push it before any reset.
> Check open `claim` issues and open PRs on the game repo before starting. First task: [issue link and the ask].

Planning-Agent has no game repo yet: it reads `Planning-Agent/Planning Agent.md` in the shared files and uses the skills under `starter-game-repo/dot-claude/skills/` in the template repo.

Derek is on the Ultra plan, so no downgrades: every thread runs on the model above.

Order for this project: Planning-Agent first (Derek wants research and brainstorming once setup is done). The day-one build threads start once a design is agreed and the game repo exists.
