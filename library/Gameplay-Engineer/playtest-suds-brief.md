# Playtest brief: the Suds opening (#289, #291, #292, #295)

Use main at or after ed1dde3, on a fresh local place, with every switch set locally and turned off again afterwards. Motion-FX's scene is OpeningScene (#284, #286, #287). The purr, hop and jingle are #293, if it has merged.

## Switches
Under test:
- `sudsWash`: the first cat is the kitten.
- `openingBox`: the truck and the box tap. It needs `sudsWash`.
- `sudsMascot`: Suds on his bed afterwards.

Base they need: `scrubPrototype`, `spaPlot`, `gameHud`, `recapCard`, `customers`, `tutorialTrail`, `tutorialTip`.

Nice to have: `spawnView`, `catMotion`, `scrubEffects`, `revealEffects`, `fluffEffects`, `scrubFeel`, `customerFigures`, `onboardingFunnel` (it logs `box_opened` and `suds_home` in Telemetry.recent).

Set them as ReplicatedStorage attributes `LiveFlag_<name> = true`.

## A brand new save
The kitten only comes to a save with **0 stars, no window cats, and `suds` below 2**. The command bar can't seed (it gets its own module copy), so make the save fresh with a local scratch edit. Don't commit it:
- **Option 1:** in `src/server/Services/DataService.luau`, change `DataService.KEY_PREFIX` to something new, such as add `_t1`, and bump it for each fresh run.
- **Option 2:** your `SaveSchema.template` route, with `stars = 0`, `residents = {}` and `suds = 0`.

To replay from a given stage, set `suds` in the template: 0 means never met, 1 means the box was opened, 2 means he is named.

## The flow, step by step (all switches on)
1. **Spawn and stand.** The player spawns, then is stood on **SpotOpening**: mid-entrance on the near pavement, facing the street. The tub is empty, with no cat.
2. **The scene.** It takes about 3.5 s, and the camera is taken for that time. The truck drives the near lane, hits the bump on SpotBump, the back door opens, and the box arcs out and lands on **SpotBox**, about 3.6 studs in front of the player. Then the camera comes back.
3. **The box waits.** Nothing opens by itself, and the tub stays empty.
4. **The tap.** The player taps the box or uses its Open! prompt. The flaps pop, the muddy black kitten peeks and shakes (about 1.3 s), then hops out toward the spa (about 0.4 s). The box goes.
5. **The kitten in the tub.** About 2 s after the tap, the muddy kitten (the CleanACat_Cat_Suds_Dirty_Sit model) is in the tub. Green floor arrows lead from the player to the tub, and the tip line reads "Step 1 of 3 · Wash him". Both go on the first scrub.
6. **His wash.** The step bar has 3 steps: scrub, brush, camera. There is **no bow step**. Scrub the mud, brush the tangles out in 3 strokes, then the **camera** shows in place of the bows. The photo holds until 15 s after he arrived.
7. **The naming.** The mint collar with its gold bell pops onto him, with a jingle and a sparkle if #293 has merged. The card reads "Meet Suds!", with a black cat portrait stand-in, "3 stars" with no "+", the line "He's your spa cat now!" and the button "Open the spa!". There are no coin rows and no rarity chip. Coins and stars are unchanged.
8. **The first customer.** Tap "Open the spa!". The first customer's cat, a **common**, comes to the tub, and Suds sits at **SpotMascot** by the door. The bed prop CleanACat_Prop_SudsBed is not in the place yet, so he sits on the spot itself, and a single "CleanACat_Prop_SudsBed is missing" warning is expected. Tapping him plays a purr and a hop if #293 has merged.
9. **Rest of the visit.** From here it is a normal first customer: they pay, and the chance board lights.

## Resume checks
- **Leave before the tap**, then rejoin: the scene plays again and the player stands on SpotOpening again.
- **Leave after the tap**, before the photo, then rejoin (`suds = 1`): there is no scene, and the kitten waits in the tub.
- **Leave after the naming**, then rejoin (`suds = 2`): there is no scene and no kitten, the first cat is a customer's, and Suds is by the door.
- **Respawn before the tap:** you land on SpotOpening again.

## Switch-off checks (our rollback)
- **`openingBox` off while the box waits:** the scene clears, and the kitten appears in the tub.
- **`sudsWash` off while the box waits:** the box goes, and the usual first cat comes.
- **`sudsMascot` off:** Suds leaves the plot. Turned back on, he returns.
- **All three off on a fresh save:** the first session is exactly as before, with the usual common customer and the bows.

## Pass criteria
- Every beat above happens in order. Nothing opens or completes without the player's own tap or drag.
- There is never more than one kitten on screen (box plus tub, or tub plus bed).
- The camera is always handed back after the scene, and the player can move.
- He is never stamped in the Cat Index, and coins and stars don't change for him.
- There are no new console errors. Only the bed-missing warning is expected.
- Check the phone profiles (a06, iPhone 14) for the card, the tip line and the 3-step bar.

## Risky, so look closely
- The scene's camera shot and the box landing spot on SpotBox: is the box inside the curb, and can the tap reach it on a phone?
- The 2 s hand-off: does the tub's kitten ever show while the box's kitten is still hopping?
- Whether the collar sits right on the muddy-turned-clean kitten (it is cloned from the clean model with the same offset).
- Suds's scale and facing on SpotMascot without the bed.
- The tip line and floor trail after the hop: do they clear on the first scrub?

## Long waits
There are none to skip. The only wait is the photo, which pays no sooner than 15 s after the cat arrived.

## Screenshots or clip wanted
- The truck and box scene.
- The box waiting, then the tap and the hop.
- The 3-step bar.
- The naming card on a06.
- Suds by the door.
