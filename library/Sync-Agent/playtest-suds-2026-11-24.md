# Playtest report: the Suds opening (#289, #291, #292, #295), 2026-11-24

Build: main 709c279. Local unsaved scratch place; repo untouched; flags workflow not used. Tester: Sync-Agent via Studio on Derek's PC.
Setup: LiveFlags.resolve edited in the scratch copy so sudsWash, openingBox, sudsMascot, recapCard, scrubPrototype, spaPlot, gameHud, customers, tutorialTrail, tutorialTip, onboardingFunnel start on (plus stations, builds, bubbleBath, pawdicure, proBrush for run E). SaveSchema.template edited per run: A fresh desktop; B fresh a06 706x339; C fresh iPhone 13 844x390 (no iPhone 12 preset); D suds = 1 then 2; E stars = 3, Brush Table, Dryer, Bath, Pawdicure built, Pro Brush, Epic cats. Every Play is a brand new local save, so "rejoin" is simulated by starting Play at the saved stage. All switches set back to false from the server at the end.

## Summary
Every numbered item passes or is covered another way. One MAJOR: on phones the box lands hidden behind the player's own avatar from the default camera. The two #292 fixes pass on the a06. No new console errors. Minors listed below. The collar sparkle and the purr sound could not be confirmed.

## Pass / fail
| # | Item | Result |
|---|---|---|
| 1 | Join at SpotOpening facing the street; truck honks, bumps, drops box; camera back ~3.5 s | PASS. Stand at (-10, -37). Truck drives the near lane, bumps, back door opens, box drops at (-10, -40.6), 4.2 studs in front, on the pavement edge. Camera back to Custom ~3 s in. After respawn you land on SpotOpening with the box still waiting. (Run A: camera briefly looked stuck after the respawn; that was the test tool forcing the camera, not the game.) |
| 2 | Tap opens once; peek, shake, hop; kitten in tub ~2 s later with trail and "Wash him" tip | PASS. One tap opened it; a second 0.3 s later did nothing (one stage change). Kitten peeks and shakes 1.5 s; box and box kitten gone at +1.5 s; tub kitten at +2.0 s, never two at once. Floor arrows and "Step 1 of 3: Wash him" tip show and clear on the first scrub. Minor: after the tap the camera still faces the street, the trail starts behind you. |
| 3 | Rejoin before/after tap | PASS by simulation. Fresh: scene plays. suds = 1: no scene, kitten waits in the tub with the 3-step bar. suds = 2: no scene, no kitten, first cat is a Common customer (Muffin), Suds by the door. |
| 4 | Wash bar 1 of 3, 2 of 3, no bow step, camera button after last stroke | PASS. "Step 1 of 3", "2 of 3" with 3 brush strokes, "Step 3 of 3 · Take the photo"; bows stay hidden, camera shows. |
| 5 | Photo: collar and bell, jingle, sparkle, naming card | PASS with notes. Mint collar with gold bell on the clean kitten. collarJingle_1 played but was logged twice at the same moment (possible double play, minor). Collar sparkle NOT confirmed: no particle emitter found on the cat. Card: "Meet Suds!", "3 stars" (no +), "He's your spa cat now!", "Open the spa!"; no coin rows, no rarity chip; coins stayed 0, chance board did not light. Minor: the portrait shows an orange cat plus a dark square (the black-cat emoji splits into two glyphs). |
| 6 | Next cat Common; Suds at his spot, one only; tap purrs and hops, at most once per 0.6 s | PASS. Smudge (desktop) / Muffin (a06), 4-step bar. Suds at SpotMascot (-4.8, -23.4), facing into the room, sensible size, only one Suds. Taps from 6.7 studs (ClickDetector range 24): 4 taps in 1.4 s gave 3 hops at least 0.8 s apart. Purr sound NOT detected in logs. Expected "[MascotService] CleanACat_Prop_SudsBed is missing" appears once. |
| 7 | Rollback | PASS. openingBox off while the box waits: scene clears, kitten in the tub on the 3-step bar. sudsMascot off: Suds leaves; back on: returns, one model. (sudsWash off was not listed in the Review-QA items; not run.) |
| 8 | Existing save with stars never gets box or Suds | PASS (stars = 3 save: no scene, no box, no Suds; ordinary first customer). |
| 9 | Phones: items 1, 2, 5 on a06 and iPhone-size | See below: MAJOR on box visibility. Truck scene plays fully on the a06. Card fits: a06 card 525x187 at (90,71), "Open the spa!" 150x45, touch worked; iPhone 13 card at (112,97), tip line and 3-slot tray fit. |
| 10 | No new console errors | PASS. Only the bed-missing warning, no-DataStore notes, rbxassetid://203785492 warning x3, AnalyticsService lines. |

## Phone box visibility (item 9)
- At rest from the default camera the avatar covers the box. iPhone 13: box screen area 44x46 px but only a 41x6 strip shows; a06: 40x41 px with a 38x6 strip. A tap on the avatar's leg in front of the box still opened it (the tap goes through), but players cannot see what to tap.
- The "Open!" prompt bubble (139x72 px) was not visible in any capture; the capture may not show prompt bubbles. Check on a real device.

## #292 fixes on the a06 (run E): both PASS
- bubbleBath off mid-bath: bath goes, suds clear, cat moves to the Pawdicure and the bar shrinks to "Step 3 of 5 · Trim the claws".
- A 0.5 s hold on the cat's HEAD clipped the outlined paw (LegF1, 4 claws gone, outline to LegF2). A second hold finished the step and the cat went back to the tub at "Step 4 of 5 · Pick a bow".
- The bath tray icon is now a soap bar, no longer an empty box.

## Tickets
- MAJOR: on phones the box lands right behind the avatar from the default camera. Drop it to one side or nudge the camera.
- MINOR: Suds's card portrait renders as an orange cat plus a dark square.
- MINOR: the collar jingle seems to play twice.
- MINOR: after the box tap the camera faces the street while the tub is behind you.
- MINOR: queue figures stand on the trail in the doorway.
- NOTE: the collar sparkle and the purr sound could not be confirmed (no emitter found; no sound seen in logs). Worth a check on a real device or by the owner of #293.
- NOTE: the "Open!" prompt could not be seen in captures; check on a real phone.

## Screenshots and clips
On Derek's PC in Downloads\Clean-a-Cat-captures\suds-opening-2026-11-24\ (cannot be copied to the shared folder from the PC). No account names visible.
Clips: clip-4-truck-and-box-a06.mp4 (7.5 s, full scene from truck arriving to camera returning); clip-2-box-tap-and-hop.mp4 (5 s, tap, peek and shake, box gone, tip and tray); clip-3-photo-collar-card.mp4 (4.9 s, photo then Meet Suds card); clip-1 is only 0.6 s (capture cut short).
Frames: 1b truck arriving; 2 bump with back door open; 2b box dropped, truck leaving; 2c camera back, box behind the avatar; 3 box waiting; 4 box opening, kitten peeks; 5 kitten shakes; 6 box gone, "Wash him" tip.
Shots: A1/A2 box waiting at join and after respawn; A3 trail through the door and tip line; A4 card on desktop; A5 collar and bell front view; A6 Suds by the door; B1/B2 a06 box hidden, then seen after stepping aside; B3 a06 card; C1-C3 iPhone 13 box, tip and tray, card; D1 stage-1 save kitten in the tub, no scene; E1/E2 a06 bath before and after bubbleBath off.

## Corrections (2026-11-24, after Planning-Agent's second read)
- Item 1 distance: "4.2 studs" was the 3D distance from the character after the respawn, (-10.19, 3.50, -37.01), to the centre of the box's bounding box, (-10.00, 1.39, -40.60); most of it is the 2.1 stud height difference. On the ground the distance is 3.59 studs, matching the spots: SpotOpening world (-10, 0.5, -37), SpotBox world (-10, 0.5, -40.6) (plot pivot (-5, 0, -10)). The box is 2.50 x 1.78 x 2.51 studs, centred over SpotBox, so its near face is about 2.3 studs from the character. At first join the character stands exactly on SpotOpening; after a respawn it was 0.19 studs off in x.
- Item 6 taps and hops: the original "4 taps in 1.4 s gave 3 hops at least 0.8 s apart" was wrong. Re-measured on main bf28006 (fresh place, stage 2, sudsMascot on): taps at 6.63, 7.03, 7.43 and 8.65 s; hops at 6.75, 7.57 and 8.77 s (each 0.12 to 0.14 s after a tap). Tap 2 (0.40 s after tap 1) did nothing; gaps between counted taps 0.80 and 1.22 s, consistent with a 0.6 s cooldown. He never hopped twice within 0.6 s. Still a PASS.
