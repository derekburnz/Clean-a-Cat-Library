---
name: studio-test-movement
description: How to move the character in Roblox Studio test runs without walking into walls or getting stuck. Use before any Studio playtest, capture or check that needs the character to go somewhere (tub, door, Garden gate, VIP Room, pads, board).
---

# Studio test movement

Why this exists: Studio runs kept getting stuck (2026-11-26). The map was fine. The way the test character was moved was the cause: the MCP `character_navigation` tool says "Success" even when the character never arrived, held keys follow the camera and not the target, a straight `MoveTo` walks into tubs, pads and customers, and phone auto-jump hops low walls. Walls and the invisible gate slabs work as designed.

## Rules
1. Move the character only with the helper `_G.qaWalkNamed("<Spot>")` or `_G.qaWalk(point)`. The helper file is `qaWalk.luau` (kept in the library repo at `library/Sync-Agent/studio-tools/qaWalk.luau`). It finds a clear stand point next to the target, faces it, turns auto-jump off for the walk, follows a PathfindingService path (AgentRadius 1.6, AgentHeight 5.5, no jumping), checks every 0.5 s for being stuck (under 0.4 studs twice, or a leg over its time), recomputes the path once, then teleports to a checked clear point. It returns reached, method (`path`, `path+retry`, `teleport`) and seconds.
2. Never trust `character_navigation`. Do not use it to move the character. (The third-party `roblox-mobile-playtest` skill lists it; ignore that line.)
3. Never hold W, A, S or D to walk. Keys are for input tests only (Space to jump, E for prompts) after the helper has placed the character.
4. Never drive `Humanoid:Move()` from a script. The ControlModule overwrites it every frame.
5. No straight `Humanoid:MoveTo` across the room. It silently gives up after 8 s, `MoveToFinished` fires about 1 stud short, and on touch auto-jump hops anything under 7.2 studs. For a deliberate collision test use one `MoveTo` leg with a 2 to 4 s limit, read the end position, then cancel with `MoveTo(root.Position)`.
6. Teleport only to a clear stand point: floor below and an empty 2.6 x 5 x 2.6 box. A `PivotTo` that overlaps a part flings the character. Zero the root's velocity after every `PivotTo` and wait until `FloorMaterial` is not Air before walking.
7. Aim at stand points, not object centres. The tub, stray box, pads, board and window seat are solid around their SpaLayout spot.
8. Do not interrupt the game's own walk-ups (Take cat and similar prompts). It leaves states stuck, such as CarryCat at "door".
9. Wait for the plot and the spawn before walking: `ReplicatedStorage` attribute `SpaPlotPlaced` is true and the character is inside Plot1's bounding box (about (-5, 3.5, -7) at spawn). Never run a multi-second `execute_luau` during the opening (it leaves the camera Scriptable); wait outside Studio with a shell until-loop for 25 to 30 s.
10. R6 and R15 both work with the helper. R15 legs do not collide, so a jump clears tops below about y 9.8 and the character can stand on them. Wall and slab tests must include a moving jump (A or D held with Space), not only walking.
11. Report every walk as reached, method and seconds. A tool's "Success" is never proof of arrival.

## Load the helper
1. Start Play. A seeded save skips to the spa; a fresh save has an opening of about 8 s.
2. Wait 25 to 30 s outside Studio. Check in a short Client call: `tostring(game.ReplicatedStorage:GetAttribute("SpaPlotPlaced")) .. " " .. tostring(game.Players.LocalPlayer.Character:GetPivot().Position)` should be `true` and about (-5, 3.5, -7).
3. Paste the whole `qaWalk.luau` as one `execute_luau` on the Client datamodel. It returns "qaWalk ready" and lives in `_G` for that Play session. Paste again after every Stop and Play. A respawn needs no reload.
4. Example: `local r = _G.qaWalkNamed("Tub") return r.target, r.reached, r.method, r.seconds`.

## Named stand points (plot slot 1, pivot (-5, 0, -10), not turned; feet, world)
Positions are read from `SpaLayout.slotSpot(spot, 1)` plus a world offset, so they follow SpaLayout, but the offsets assume slot 1 (always the case in a one-client Studio run; other slots may be turned).
- Spawn (-5, 0.5, -7): SpotSpawn + (-5, 0, 11.5). The real spawn; SpotSpawn alone is (0, 0.5, -18.5).
- Tub (0, 0.5, -16.5): SpotTub + (0, 0, -4.5), room side of the tub.
- DoorLine (-7, 0.5, -23): SpotQueue1 + (3, 0, 0).
- Window (3, 0.5, -20.7): SpotWindow3 + (0, -2.5, 3.5), floor in front of the seat.
- Board (-15.5, 0.5, -24.6): SpotBoard + (3, 0, 0).
- GardenGate (7, 0.5, -2.5): SpotGardenDoor + (0, 0, -3). Frames at x 3.75 and 10.25. GardenInside (7, 0.5, 4.5): + (0, 0, 4).
- VipDoor (-12, 0.5, -2.5): SpotVipDoor + (0, 0, -3). Frames at x -16.25 and -7.75. VipInside (-12, 0.5, 4.5): + (0, 0, 4).
- StrayBox (8.9, 0.5, -2.4): SpotStray + (-2.5, 0, 0). The box is at (11.4, -2.4).
- PadJo (-6, 0.5, -6.5), PadSam (-2, 0.5, -6.5), PadLou (2, 0.5, -6.5): SpotWorker<Name> + (0, 0, -3). The pads are at z -3.5.

## Known blockers (so a stop is not a surprise)
- The back wall is at z 0 to 1. The only ways through are the VIP door and the Garden gate.
- VIP door: frames and open pink leaves (z 1.2 to 5.1) are solid.
- Garden gate: frames and posts at z 1.45 are solid. The pickets do not collide, but an invisible slab runs along each open leaf (12 studs tall after PR 742).
- In the room: the tub (radius about 2.5), the Second Tub pad near (-12, -10), the worker pads, the stray box, customers at x -10 to -12 from z -22 to -31, the window seat at z -24. Jump height is 7.2 studs.

## Results 2026-11-26
114 of 114 test walks reached their spot on main e3ed268, R15 and R6, no teleports: spawn, tub, Garden gate in and out, VIP door in and out, stray box and the three pads, 33 of 33 each way; 8 harder legs (round the tub, between rooms, board to Garden) 24 of 24 on each, three R6 legs needing one recomputed path (no path right after a teleport).
