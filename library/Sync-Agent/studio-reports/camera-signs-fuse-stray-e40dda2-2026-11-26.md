# Camera #670, PR 683 signs, PR 682 Fuse, stray box, 2026-11-26
Main moved during the run: ran on d6fdf1b, ee696a9 and e40dda2. Camera code is the same on all three; only the stray box spot changed after ee696a9. Fresh rojo builds, unsaved local places. Every OFF_BY_DEFAULT key on incl. cameraClear, tubBuilds, pets, petsWindow, crateWindow except toolCursor, streetLoadTest, exampleFeature, openingReplay, benchGrow. Seeded save, iPhone 13 frame unless noted. Pictures: draft PR 687.

## CAMERA (per-frame log, 3 s per spawn)
Joins: PASS on all, no spin. R15 phone 11 of 11 (5 d6fdf1b, 5 ee696a9, 1 e40dda2), R6 phone 2 of 2, desktop R15 1 of 1, R6 1 of 1. Camera already turned on the first logged frame (yaw 50), never changes after. At 2.0 s and 2.5 s at (3.3, 7.9, -0.1), facing the spa.
cameraClear off: the new plate stops the camera at (-5, 6.8, -0.1), 0.1 stud in front of the plate; a grey wedge covers part of the view (picture 04). No longer a full blue screen.
Respawns: FAIL, 1 or 2 in 5. Camera resets about 0.33 s after a respawn. ee696a9: 4 of 5 fine, 1 ended at 2.0 and 2.5 s with the picture right in front (picture 03). d6fdf1b: 1 of 3 logged respawns the same (picture 01).
Wall pieces: no climbing at any of the 8; every jump lands back at y 3.5. Backed into the big picture at (-5, -0.1): camera pulls in to 1.8 studs, spa shows. At (-19.5, -0.1) the camera sits inside the non-colliding picture, grey haze: FAIL (picture 02). Side-wall pieces could not be checked over MCP (camera would not stay pointed from the wall side).
Fresh opening truck shot: PASS, unchanged. Turning in the first 2 s: PASS, no snap back (respawn drag at 0.67 s, smooth to -152).

## PR 683 SIGNS (e40dda2 and ee696a9)
(1) Tapped build: PASS. Real tap on Build Garden gave "Garden / 24h 0m left", board 23:59:58; 75 s later "23h 59m left".
(2) Last minute: FAIL. Seeded VIP Room build with 95 s left read "2m left" and stayed there down to 2 s while the board counted 1:35 to 0:02. At 0 the finished VIP Room replaced the site: PASS.
(3) Rejoin: a real rejoin is not possible on a local place; restarted with the same EndsAt. Garden sign showed the right time ("23h 59m left") but did not count: still "23h 59m left" 65 s later (picture 05). Signs drawn at the join never count down; only a sign from a build started in the session does.

## PR 682 FUSE (real taps, phone; desktop not run)
(1) PASS. Scrubby x4: Fuse made a star-2 Scrubby and left one Scrubby. Pet beside me (Bamboo) stayed.
(2) PASS. Tap on the picture put the pet on me; tap on the name took it off.
(3) PASS. With 6 cards the list scrolls 71.5 px, last row ends exactly at the list's bottom edge.

## STRAY BOX (e40dda2)
Place: PASS. At (11.4, -2.4) (plot spot 16.4, 7.6), 0.1 stud from the side wall, 0.9 from the back wall, 5.2 studs from the Garden gate (picture 06).
Path: PASS. Spawn to Garden gate is clear; path service finds a path.
+10: PASS. First stray's wash took coins 0 to 11.
Prompt: not seen. On this fresh save, after "Open the spa!" the stray went straight to the tub; no prompt showed on the box.
Console: nothing new on any build.
