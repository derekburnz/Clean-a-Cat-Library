# Issue #178 four-preset screens, 2026-11-24 (main 55acb70)

The step bar, tool tray and coin counter are NOT in the game code on main yet: src/client/UI/init.luau is still the starter HUD (one Menu button, an example window and toasts). They exist only as mockups (PRs #43, #50, #53). So the HUD the rule is meant for could not be captured. The real in-game screen was captured instead, camera on the tub in plot 2 with a dirty cat in it, via rbx-device-simulator-lua. Every visible button and label in PlayerGui was measured; the top bar inset was 58 px on every preset.

Setup: fresh local place, never saved or published. spaPlot, customers, customerFigures, stations, streetLoadTest, scrubPrototype on.

## Per preset (files on the PC at C:\Users\Derek\Downloads\Clean-a-Cat-captures\issue178-screens\)
- issue178-screen-iphone14.jpg, 750 x 390: Menu button at (16, 140), 120 x 52, text 20 px, clear of the top bar and the thumbstick. Jump button 70 x 70 at (655, 242). Nothing cut off. Menu readable but takes a noticeable bite out of the left edge on this small screen. Tub and cat in view, small.
- issue178-screen-ipad10.jpg, 1180 x 820: Menu at (16, 355), 120 x 52, text 20 px. Jump button 120 x 120. Nothing cut off or overlapping. Readable.
- issue178-screen-xboxone.jpg, 1920 x 1080: Menu at (16, 485), 120 x 52, text 20 px, no touch controls. Nothing cut off, but the Menu text is small for a TV from the couch and it sits only 16 px from the left edge, inside the area TVs often crop. A larger size on console and an inset of about 5 percent would help.
- issue178-screen-pc.jpg, 1366 x 768: Menu at (16, 329), text 20 px. Nothing cut off. Readable.

Pass rule (nothing cut off or under the top bar or thumbstick, text readable): met on every preset except that text is small on Xbox. The screen the rule is meant for can be judged only once the HUD is built; rerun takes a few minutes.

## Copy to the cloud
Not possible: the PC session has no access to the cloud shared folder (/mnt/project-files does not exist on the PC) and no tool that writes to the project's shared Library. The four pictures stay on the PC. Someone with access to the PC (Derek) would need to upload them.

Console: no game errors; usual no-DataStore notices and the three rbxassetid://203785492 lines.
