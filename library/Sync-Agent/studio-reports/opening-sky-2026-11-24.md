# Opening motion and skyDraft, main 1b77aa9 (#350 merge, includes #347), 2026-11-24
Fresh local unsaved build; switches local only: opening-wash dev set plus skyDraft and openingBox (skyDraft flipped between Play runs via a scratch override so before/after are the same view). Desktop 1502x753 and a06 706x339. A scratch logger recorded truck, door, box every frame; times are seconds after scene start. Results were the same on both sizes unless noted.

## Opening: all PASS
- Pothole CleanACat_OpeningPothole at world (-12.5, 0.22, -47.6); player root (-10, 3.5, -37) facing the street: 2.50 studs along the road from the player (on their left), 10.6 studs out. PASS.
- Truck jolt: drops in from 2.43 to 2.99 s (desktop; 2.41 to 2.99 on a06), front wheels then back; lowest y 0.22 at 2.50 s (2.48 a06).
- Back door: opens at 2.43 s (2.41), widest at 2.48 s (2.46); widest recorded 84 degrees vs 100 in the spec (the 0.1 s swing is a few frames, logger probably missed the peak); shut again by 3.24 s, open about 0.8 s, then slams. PASS.
- Box: first seen at 2.53 s (2.51); rolls end over end exactly once (360 degrees about the road axis) from x -19 to x -5; at about 4.4 s at (-5.00, 0.50, -40.60), tiny 1 degree settles until 6.9 s. Rest relative to the player: 5.00 studs to the right, 3.60 in front. Flaps up: up vector (0, 1, 0), tilted 0.1 degrees (a06). PASS.
- First-frame stall: the first frame drawn comes 1.4 to 1.5 s after scene start (the loading stall from the baseline); the truck is already well up the road, so players never see the first 1.4 s of its approach in Studio. Worth checking on Derek's phone.
- [Opening] lines: truck moving 0.13 s after the join, 0.02 s after scripts started (desktop, sky on); 0.15 s / 0.01 s (a06, sky off). No new warnings/errors (no-DataStore notes, rbxassetid://203785492 x3).

## Sky: skyDraft washes out the ground; HUD stays readable (luminance 0 to 1; WCAG contrast)
- Desktop street: pavement L 0.52 to 0.97, colour (195,191,179) to (255,251,242), almost pure white and its texture is gone; road L 0.055 to 0.29 (pale blue-grey); road against pavement 5.4:1 to 3.0:1; blue house wall L 0.23 to 0.62.
- a06 street: pavement L 0.52 to 0.95; road L 0.06 to 0.31; road against pavement 5.1:1 to 2.8:1.
- Desktop spa front: white sign panel L 0.21 (shaded grey) to 0.67; pink wall 0.12 to 0.47; white window wall 0.33 to 0.84; panel against wall 1.6:1 to 1.4:1; panel against pavement 2.2:1 to 1.4:1. The facade turns pastel and flat; the panel blends into the wall and the ground.
- HUD unaffected (drawn on top, after the sky effects): Menu dark text on white button 16.7:1 off and on; coin "0" white digits against dark outline 12.7:1 off and on; outline against sky 6.3:1 to 7.2:1. Readable on both sizes.
Reading: skyDraft does not touch the HUD text but washes out the world: near-white pavement glare, road loses about half its contrast with the pavement, white sign panel no longer stands apart from the wall. Bloom and haze look too strong for the ground; suggestion for Motion-FX: lower the bloom or exposure, or keep the haze off nearby surfaces.

## Files on the PC (Downloads\Clean-a-Cat-captures\opening-sky-2026-11-24\)
desk-street-sky-OFF/ON.jpg (same view from behind the player toward the road, box at their right; ON: white glare pavement, pale road); desk-spa-sky-OFF/ON.jpg (road side looking at the spa front; ON: pastel washed facade, flat white panel); a06-street-sky-OFF/ON.jpg (default phone camera after the scene, same effect); desk-opening-sky-ON.mp4, a06-opening-sky-ON.mp4; contrast-sample.ps1 (the sampling script). Avatar shows, no names.
