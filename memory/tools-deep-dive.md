---
name: tools-deep-dive
description: Result of the 2026-11-24 deep dive into open source Roblox tools and skills for UI and all-device quality; Derek's picks, the tasks opened (178 to 186) and what is parked
metadata:
  type: project
  modified: 2026-11-24T13:49:57.613Z
---

Derek asked 2026-11-24 ET for a deep dive into open source repos and skills for quality UI and for a game that runs well on phone, tablet, PC and console. Planning-Agent did it. Derek picked the same day and the tasks are open.

- Picks page: https://claude.ai/artifact/UQGWKRdcYzAKcLJJNZUZPC ("Clean a Cat Tool Picks"). His picks save in its database, collection `picks`, doc `s-<id>` with `pick` (0 is our pick) and `note`; `s-skip` holds a note on the skip list. Read with ArtifactData.
- File copy with every id: Planning-Agent/tools-and-skills-deep-dive.md. Research notes: Planning-Agent/Tools-Research/ (4 files). Generator: Planning-Agent/plan-page-source/build_tools.py.

Derek answered all 14 on 2026-11-24 9:29 AM ET (his picks are in the page database and in the file copy). Decision lines: game repo docs/decisions.md (PR 187).
- Yes, tasks opened in the game repo: 178 Roblox's Studio skills for device and speed checks (Sync-Agent confirms on Studio first), 179 roblox-dev-skill 2.23.0, 180 UI and input guides (izzyfrm rules, EL4CTEO roblox-ui and roblox-input), 181 Roblox's text size, see-through, input and safe area settings, 182 speed budget. Derek's weakest test phone is an iPhone 12 (his words 2026-11-24), which is mid range, so cheap Android is covered by Studio presets for layout, lowest graphics setting and a flat memory trend on the iPhone and the crash rate dashboard after the first test.
- Trials that must END WITH AN EXAMPLE DEREK LOOKS AT before anything is kept: 183 spr springs (side by side clip), 185 icon sources (sample sheet), 186 a Roblox style sheet on one screen: DROPPED by Derek 2026-11-24 after the trial (as reported by Design-Agent, his words "drop them we dont need it"; PR 218 removes it). Screens stay in plain code. 184 Trove: keep only if no harm and no extra token use.
- No: Asphalt ("no need since ai does it"). No UI framework for now (Vide is the one to trial later on the Cat Index).
- Left to us, and Derek confirmed 2026-11-24 ("for the two calls go with whats needed", so we may change them when the need shows up): Flipbook not installed for now; tests inside real Roblox from GitHub wait until the style sheet trial is kept or a bug slips past the stand-in, then on merges to main only.
- Parked, Derek unsure: extra skills (lighting, camera, localization, performance, roblox-suite, Chrrxs Studio MCP). Bring back when the spa room is dressed.

Facts worth keeping:
- raw.githubusercontent.com is readable from a cloud thread for any public repo (license files, wally.toml, changelogs). api.github.com and github.com pages are closed for repos outside ours. See [[roblox-research-howto]].
- Roblox gives no phone memory limit and no tap size number. FredokaOne and Nunito are built-in fonts. Fusion on Wally is stuck at 0.3.0 while main is 0.4.0-dev1.
- Skill repos with no license (brockmartin/roblox-game-skill, JustineDevs/roblox-ai-os) cannot be copied. roblox-brain's player psychology skill breaks our young audience rules.

See [[planning-status]].
