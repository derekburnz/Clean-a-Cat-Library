---
name: studio-test-movement
description: How Studio test runs move the character without getting stuck on walls (Derek's ask 2026-11-26); path helper, banned methods, where the skill and helper live
metadata:
  type: feedback
---

Derek 2026-11-26 ET: Studio tests keep running into walls and getting stuck; fix it and update the skill and memory. Cause was not the map: the test character was moved badly.

**Rule:** Sync-Agent's Studio session moves the character only with `_G.qaWalkNamed("<Spot>")` (helper `qaWalk.luau`, PathfindingService path with a stuck check, clear stand points, auto-jump off). Never `character_navigation` (answers Success without arriving), never held keys, never `Humanoid:Move` or a straight `MoveTo` across the room, never `PivotTo` into a part. Report each walk as reached, method and seconds. Wall and slab tests need a moving jump (A or D plus Space) too, because R15 legs do not collide and clear tops below about y 9.8.

**Why:** 114 of 114 walks reached their spot with the helper on main e3ed268 (R15 and R6, no teleports); before it, several stuck cases per day (customer in the doorway, Garden gate slab hopped by auto-jump, flung by a teleport).

**How to apply:** skill `studio-test-movement` in the game repo `.claude/skills/` (issue 749, PR 750, draft until Review-QA reviews); helper and spot table in the library repo `library/Sync-Agent/studio-tools/`. Review-QA's playtest steps should use it. RbxSync was vetted 2026-11-26 and NOT installed (proprietary paid licence, runs arbitrary code with loadstring); Roblox Playtest Agent beta is the only other candidate; list in library `Sync-Agent/studio-test-movers-suggestions-2026-11-26.md`. See [[tools-deep-dive]].
