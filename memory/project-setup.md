---
name: project-setup
description: State of the Roblox game template setup (README "setup" flow), Derek's setup answers and what still waits on him
metadata:
  type: project
  modified: 2026-11-24T13:21:01.736Z
---

Setup follows README.md of derekburnz/Roblox-Game-Template ("For Claude, when the person types setup").

- Derek's answers (2026-11-22 ET): GitHub account derekburnz; new game, idea not chosen, research and brainstorm after setup; Eastern time; Ultra plan (no model downgrades); PC DESKTOP-DFOGFG7, Desktop and Downloads folders approved for management.
- Game owner: Roblox group Creampuff Games (already has players from his other game). Uploads go under the group (ROBLOX_GROUP_ID, optional ROBLOX_GROUP_KEY).
- Preference changes from defaults: restarts allowed without asking until public release (ads or real players), then only with his OK; PRs that pass tests always auto-merge (Review-QA pass kept as the gate); silent publishing.
- Final drafts for project instructions, memory and the thread roster: /mnt/project-files/Setup-drafts/ (coordinator applies them and starts threads).
- Agent library folders copied to /mnt/project-files/<Thread>/. Starter dry run: 17 tests and UI gate pass.
- Library repo: derekburnz/roblox-game (copied from the template 2026-11-22 ET, main only, memory/ files written). The template repo can be detached; skills now live in roblox-game/starter-game-repo/dot-claude/skills/
- Next: Planning-Agent (Fable 5.2 high) for ideas, then a one-page design, then the game repo from starter-game-repo/ and the day-one threads.
- Publish setup works since 2026-11-23 ET (game repo PR 110): Derek's Roblox key is the GitHub secret OWNER_KEY (plus ROBLOX_GROUP_KEY for uploads) and AUTO_PUBLISH is true. Workflows fall back to OWNER_KEY and have the public ids built in (universe 10778773655, start place 79301459457383, group 107520049), so no repo variables are needed. First publish run passed. The dev copy place (Clean-a-Cat-Dev) needs no key of its own.
- Ruleset "main" is ACTIVE on the game repo since 2026-11-24 8:20 AM ET (Derek created it from his phone): a pull request is required with 0 approvals, the two checks `Rojo sourcemap, luau-lsp, Selene, StyLua` and `Unit tests, strict types, UI gate` are required (branches need not be up to date), force pushes and deleting main are blocked, no bypass list. Direct pushes to main in the game repo are refused now. Check it from a cloud thread while the repo is public: curl https://api.github.com/repos/derekburnz/Clean-a-Cat/rules/branches/main. GitHub asks Derek for a sign-in code on settings changes; Claude never types codes, so settings changes wait for him.
- Parked by Derek until gameplay is decided: notification message id and the experience secret CleanACat_NotifyKey.
