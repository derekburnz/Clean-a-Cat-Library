# Wash screen hides world bars (PR 979), 2026-11-27

Local Studio only, unsaved places, iphone_13 frame (749 x 388). Every off-by-default switch was on except toolCursor, streetLoadTest, exampleFeature and openingReplay; washScreen was on. Seeded save with Jo and Sam hired, bench 6, and six customers at the counter with cards and heart bars. The tester name is the only name.
- Before: origin/main 287f995 (no PR 979).
- After: branch claude/project-thread-r0i85j at f557d0b (PR 979).

Studio's screen and video capture never draw BillboardGuis, so red QA boxes mark each enabled on-screen BillboardGui (`*-marked.png`). A script also counted, every 0.1 s, the enabled BillboardGuis, SurfaceGuis on parts, Highlights and Humanoid name tags.

| Step | Result | Numbers |
|---|---|---|
| Before, scrub | shows the bug | 6 CounterCard (heart bar) and 1 VisitorStar over the wash screen, plus the tools board title |
| Before, mid wash (claws) | shows the bug | the same 6 cards and the star, plus the paw ring. There is no rinse shot: the Studio skip hook jumped the foam step |
| After, scrub | PASS | 0 enabled billboards out of 9 to 11 in the game, 0 SurfaceGuis on screen, 0 highlights, 0 name tags; suds show |
| After, rinse (blue spray-off bar) | PASS | 0 billboards, 0 surface guis, 0 tags; suds on the cat |
| After, camera move into the wash | PASS | 12 billboards dropped to 0 at 0.9 s, when the camera turned Scriptable; the camera yaw changed at 1.0 s; no frame with both. The move is a cut behind the bubble wipe, not a pan |
| After, claws: paw marker | PASS | the PH_PawRing highlight is on (yellow outline on the front leg) and is the only one; 0 billboards |
| After the wash ends | PASS | 12 billboards on again: 6 CounterCard, 2 WorkerBar (Jo and Sam), VisitorStar, GiftBeacon, 2 prompt pills; signs and boards back |

Seen, not part of this PR: the cats on the counter (3D models) still show through the wash room's back wall, in both builds.
