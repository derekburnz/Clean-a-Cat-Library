# Studio test tools (QA only, never shipped in the game)

- `qaWalk.luau`: the path helper for Studio test runs (`_G.qaWalkNamed("Tub")`). Paste it as one `execute_luau` on the Client datamodel after the opening is over. Rules and load steps: `studio-test-movement-SKILL.md` (copy of the game repo skill `.claude/skills/studio-test-movement/SKILL.md`, PR 750, issue 749).
- Result on main e3ed268 (2026-11-26): 114 of 114 test walks reached their spot, R15 and R6, no teleports.
- If the game moves things (SpaLayout spots, doors, tub), update the spot table in both the helper and the skill.
