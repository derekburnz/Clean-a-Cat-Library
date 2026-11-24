# Issue #122 stink effect captures (phone size), 2026-11-24

Real iPhone 14 emulator, 844 x 390 landscape, touch input, thumbstick and jump button. Fresh local place built from main (1683c79), not Clean-a-Cat-Dev or the published place. In Play, customers, scrubPrototype and stinkEffects were set true from the server; nothing live touched.

Cotton cat: rerolls gave Cotton once but the first scrub went wrong; second run kept giving Inky and Smudge, so the CatReady event was re-sent from the server with kind Cotton. Visuals and wisps are the real ones; the server record still said Inky (matters only for payment).

## Shots (on the PC, C:\Users\Derek\Downloads\Clean-a-Cat-captures\)
- Before: issue122-01a-before-scrub-default-camera-iphone14.jpg, issue122-01c-before-scrub-default-camera-run2-iphone14.jpg, issue122-01b-before-scrub-close-iphone14.jpg (zoomed one step)
- Part way: issue122-02a-mud-14of20-gone-default-camera-iphone14.jpg, issue122-02b-mud-14of20-gone-zoomed-iphone14.jpg. Could not stop at half: one short drag cleared 14 of 20 patches (everything facing the camera), so 70 percent.
- Clean: issue122-03-clean-zoomed-iphone14.jpg. Wisp emitter is removed once clean.

## Notes for Review-QA
- At default camera distance on a phone the cat is about 40 px tall and the wisps are hard to see. They show clearly only zoomed (faint green puff above the head), and on the three customer cats at the door.
- Touch scrubbing works in the emulator: a finger starting on the cat locks the camera until it lifts; a drag starting off the cat turns the camera (the PR #44 checks, now verified in the emulator).
- A scrub starting in the lower-left thumbstick zone also moved the character (touch drove the stick at the same time). Probably should not move the player. Emulated touch; check on a real phone.
- Console: three "ContentId rbxassetid://203785492 failed: Asset type does not match requested type" lines. The id is not in the repo or any texture, image, sound or mesh field in the place, so likely Roblox's own touch controls. No other game errors.
- The 11/23 captures folder was gone when this started; it was recreated.
