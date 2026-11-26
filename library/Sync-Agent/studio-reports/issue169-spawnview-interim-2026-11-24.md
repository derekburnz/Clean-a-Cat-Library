# Issue #169 spawnView first frame, interim (main 1808a3e, before PR #173), 2026-11-24

Verdict: spawnView fixes the wall view but FAILS on the tub and the cat's face. To be redone after PR #173 (tub turns to face the new spawn).

Setup: fresh local place from 1808a3e, iPhone 14 and Samsung A06 emulators. spaPlot, customerFigures, stations, streetLoadTest and spawnView on from the server; scrubPrototype and customers also on (otherwise no tub or door line in own plot). True first spawn: Players.CharacterAutoLoads off in the unsaved scratch copy, LoadCharacter called once plots were placed, no input. Per shot: 9 x 5 ray grid from the camera for parts nearer than 4 studs, parts touching the character, facing, what is in view, how much of tub and cat the avatar hides.

## spawnView on (same on both devices, fresh Play and respawn)
Pass: no wall, glass or part near the camera (0 of 45 rays under 4 studs); nothing touching the character; character faces the street; window and door line in view.
Fail: the player stands 5 studs straight behind the tub, so the avatar hides 82 to 84 percent of the tub and 100 percent of the cat, and the cat shows its back (its face points to the street, the same way the camera looks).
The very first frame (1a) is taken before the avatar finishes loading and shows the tub clearly; within about half a second the body covers it (1b, 2).
Suggested: #173 should fix the cat's back; moving the spawn a little to one side of the tub would keep the avatar from hiding it.

## Baseline, spawnView off (fresh Play)
Fail: the camera sits outside the glass front looking in; a pink and green wall edge fills about the right fifth of the view; the character faces into the shop, away from the street. The avatar hides 77 percent of the tub, but the cat's face is toward the camera. spawnView is clearly better on walls and facing.

## Two players: not run
Studio's Test > Clients and Servers needs clicks in Studio's window, and the screen-control prompt times out with nobody at the PC. Stand-in: own player given slot 2 and respawned; framing matches plot 1 (no walls, faces the street, window and door line in view, avatar over the tub).
POSSIBLE BUG to check in a real 2-player test: on the first spawn right after the slot changed to 2, the character fell through the floor on both devices (y -33 iPhone, -171 A06); the next respawn was fine. Plot 2 floor is solid at y 0.5 and the spawn spot (44, 0.5, -7) has nothing blocking it. Possibly the load-test plot clearing its stand-ins while the character spawns, so player 2 might drop through on joining. Unconfirmed.

## Console
No game errors. Usual no-DataStore notices and the three rbxassetid://203785492 lines.

## Shots (on the PC, C:\Users\Derek\Downloads\Clean-a-Cat-captures\)
issue169-iphone14-{1a-fresh-play-first-frame, 1b-fresh-play-settled, 2-respawn-first-frame, 3-plot2-single-player-stand-in, 4a-baseline-spawnview-off-first-frame, 4b-baseline-spawnview-off-settled}.jpg and the same six as issue169-a06-*.
