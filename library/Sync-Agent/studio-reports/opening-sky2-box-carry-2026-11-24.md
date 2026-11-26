# Sky re-measure, first frame, box exit, carry: main 0f020c9 (#354, #351, #352, #355 in), 2026-11-24
Fresh local unsaved builds, nothing pushed. Switches local only: opening-wash dev set plus openingBox, carryHold, skyDraft (flipped off and on via a scratch override in separate Play runs). Earlier part taken on 7b0b690, everything redone on 0f020c9 when the carry item arrived; all numbers are from 0f020c9. R6: default R6 rig as StarterPlayer.StarterCharacter, recoloured (scratch only).

## Sky (OFF -> ON now; ON on 1b77aa9 in brackets), same views and contrast-sample.ps1 as before
Desktop street: pavement L 0.52 -> 0.76 (was 0.97), colour (235,225,213) warm cream, not glare; road L 0.055 -> 0.13 (was 0.29); road against pavement 5.4:1 -> 4.6:1 (was 3.0:1): meets the 4.5:1 aim; blue house wall L 0.23 -> 0.38 (was 0.62).
a06 street: pavement L 0.52 -> 0.76 (was 0.95); road L 0.06 -> 0.14 (was 0.31); road against pavement 5.1:1 -> 4.3:1 (was 2.8:1): just under the 4.5:1 aim.
Desktop spa front: sign panel against wall 1.6:1 -> 1.6:1 (was 1.4:1); panel against pavement 2.2:1 -> 1.8:1 (was 1.4:1); panel L 0.21 -> 0.40; wall L 0.12 -> 0.23; white window wall L 0.33 -> 0.61. Reading: the panel still does not read against the wall; it is 1.6:1 with the sky off too, so this is the panel's own colour, not the sky.
HUD unchanged: Menu text 16.7:1 off and on; coin digits 12.7:1 off and on; coin outline against the sky 6.3:1 -> 5.7:1 (6.2 -> 5.6 on the a06), still readable.

## First frame (desktop; Heartbeat delta, RenderStepped count, truck position/parts, ContentProvider.RequestQueueSize per frame)
hb1 scene 0.024 s dt 77 ms 0 renders truck x -64.50, 91 parts, queue 18
hb2 0.921 s dt 838 ms 0 renders x -64.50 queue 1
hb3 1.357 s dt 473 ms 0 renders x -64.50 queue 0
hb4 1.384 s dt 32 ms 0 renders x -64.50
hb5 1.402 s dt 24 ms 0 renders x -64.50 queue 27
hb6 1.463 s dt 54 ms FIRST RENDER truck x -62.50 y 0.50 queue 91
hb10 1.506 s render 2 x -60.70; hb14 1.534 s render 3 x -59.93
iPhone 13: same shape (600 and 731 ms frames), first render at scene 1.45 s, truck x -62.50.
The stall is two long frames (0.84 and 0.47 s) plus a few short ones, with nothing drawn until 1.46 s. The truck model is loaded throughout (91 parts from the first frame); the asset queue empties during the stall, then refills to about 90 once drawing starts. Thanks to #351 the truck holds at x -64.5 through the stall; it has moved only 2 studs when the first frame is drawn, 52.5 studs up the road from the player (player at x -10). The game's own log: "[Opening] camera back 5.10 s into the scene (shot over)"; the earlier 1.3 to 1.5 s marker was wrong, camera returns at about 5.1 s. [Opening] truck moving 0.11 s after the join.

## Box exit vs truck (iPhone 13; no iPhone 12 preset)
Per-frame geometric overlap test of each box part against every truck part (bounding boxes). Truck parts are only named CleanACat_Prop_DeliveryTruck_Body, _Door or _xx_Wheel, so named by size. Exit from scene 3.81 to 4.15 s, lands about 4.36 s.
- Cargo floor (Body 6.00x0.25x9.20 and 5.48x0.03x8.71): box sits 0.03 to 0.15 studs into the floor the whole time it is inside, up to 4.11 s (sinks rather than rests on top).
- Small Body part 0.52x0.34x0.10 (two; probably a rear light or plate bracket at the back opening): overlapped 0.04 to 0.12 studs from 3.83 to 4.15 s, about 75 frames, as the box slides out over the back edge.
- Back door panel (Door 5.64x5.43x0.16): overlapped 2 frames at 4.364 to 4.368 s as the box drops past, up to 0.26 studs (brief clip through the lower edge).
- Posts (0.20x5.96x0.20), side walls (0.25x5.46x9.18), mud flaps (0.10x1.40x1.60), wheels: no overlap in any frame.

## R6 bug (new, ticket-worthy)
With an R6 avatar PlotService.standAt puts the root only HipHeight + half the root's height above the ground; R6 HipHeight is 0, so the root sits 1 stud up instead of 3. Legs end 2 studs under the street and the avatar falls through: root y -1.71, freefall, invisible; the camera sits low behind a potted plant. FloorTrail already handles R6 (its comment says R6 legs are 2 studs); PlotService does not. (Avatar moved up by script to continue the test.)

## Carry with R6 (#355), relative to the HumanoidRootPart (right, up, forward)
1. Head corner vs chin: PASS. Chin at (0, 1.00, 0), face at F 0.59; nearest point of Suds to the chin (-0.02, 0.94, 0.79): 0.80 studs away, in front of and just under the chin; penetration into head and torso 0.00 (R6 has no neck part). Method: sample points over every visible part of Suds against the head and torso boxes.
2. Tail vs right forearm: FAIL. The tail passes 0.27 studs into the right arm's box. The tail tip clears it by 0.98 studs at (1.04, 1.26, 1.79), so it is the tail base crossing the forearm. Both arms also sit about 0.48 studs into his body (that is the hold).
3. Size pop into the tub: FAIL. Logged scale and bounding box every Heartbeat from the walk to the tub until 3 s after he was in. Held: Loaf scale 1.40, box 1.95x1.71x2.59. During the 0.4 s hop he shrinks smoothly 1.40 to 1.00 (0.1 to 0.5 percent per frame). In one frame at the hand-off he becomes the Sit body under PH_SpaPrototype at scale 1.50, box 2.29x2.82x1.87. Largest frame-to-frame change +56.7 percent in box diagonal (scale 1.00 to 1.50 plus the loaf-to-sit swap). The hop should end at 1.5 (or the tub body should start at the scale the hop ends at).

Console: no new warnings or errors (no-DataStore notes, rbxassetid://203785492 x3, two [Opening] lines).
Shots on the PC: Downloads\Clean-a-Cat-captures\opening-sky2-2026-11-24\ desk-street-sky-OFF/ON (ON: cream pavement, visible road), desk-spa-sky-OFF/ON (ON softer pastel, sign panel still flat against the wall), a06-street-sky-OFF/ON, iphone13-box-exit-1..4 (box tipping out past the open back door over the pothole, to the road), iphone13-box-exit-clip.mp4. Downloads\Clean-a-Cat-captures\suds-carry2-2026-11-24\ 1-carry-R6-default-camera-behind, 2-carry-R6-front (Suds across the chest, head near the avatar's chin, face visible), 3-R6-sunk-under-pavement-after-opening (no avatar visible, camera low behind the plant). No account names.
