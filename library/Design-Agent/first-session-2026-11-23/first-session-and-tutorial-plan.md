# Clean a Cat: first session and tutorial plan

Design-Agent, 2026-11-23 ET. Status: plan for the build, based on Planning-Agent's gdd-draft.md. The design itself is not locked until Derek's playtests are in, so any change to the draft's loop or numbers updates this plan. Values marked (draft) come from gdd-draft.md; values marked (proposed) are mine and need Planning-Agent's OK before they go into tuning.md.

## Goals
- The player is scrubbing a cat within 3 seconds of being able to move, before any reading (the name promises it).
- A clean cat, a photo and a cat of their own before 0:45.
- A clear next goal before the 60 second mark and a first build before the 180 second mark (the two Home bounce windows).
- Every step tapped by the player, dim plus one arrow, one instruction of a few words at a time. No window opens by itself. No shop, social or like prompts in the session.

## Switches (LiveFlags, off by default, turned on the hour they publish)
| Switch | What it controls | With it off |
|---|---|---|
| `TutorialFirstSession` | Dim, arrows, the few word instructions and idle hints for steps 1 to 10 | Same spawn (stray in tub, sponge in hand), no dim or arrows, the goal line still shows |
| `TutorialGoalLine` | The one line goal at the top of the screen | No goal line |
| `LongBuildOffer` | The builder kitten's speech bubble offering the first 8 hour build, and the notify bell | The build is still in the builder panel, no bubble, no bell |

Each switch has its own clean day before the next goes on, so Growth can read each one apart.

## Loading (counts as part of the tutorial)
- The player's own spa room, the stray, the tub and the sponge stream in first. Everything else (street, other spas, decor) loads after.
- No loading screen scene, no logo, no intro. Target: can move in under 10 seconds on a mid phone. Funnel step `loaded` fires when the client can move.

## The steps
Time is from `loaded`, on a phone. Each step logs once per save, on the server.

| # | What the player sees | What they tap or do | Target time | Funnel step |
|---|---|---|---|---|
| 1 | Standing at the tub, a muddy stray in it, sponge in hand. Screen dims except the cat. Arrow on the cat: **Scrub!** | Drag a finger over the mud (mouse: hold and move; gamepad: hold A and move the stick cursor) | 0:00 to 0:03 | `first_scrub` |
| 2 | Mud chunks fly, 12 to 20 patches (draft). At 80% clean the rest pops off, the real coat shows and the cat shakes off. Camera stays with the player. 1.5 seconds, no skip | Nothing; it plays out from their scrub | 0:15 | `first_reveal` |
| 3 | Dim plus arrow on the brush in the hotbar: **Brush!** | Tap the brush, then three swipes on the cat | 0:25 | `first_brush` |
| 4 | Three bow buttons rise in the bottom bar. Instruction: **Pick a bow** | Tap one | 0:30 | `first_style` |
| 5 | Arrow on the camera button next to the tub: **Photo!** | Tap it. The before and after card opens (the player opened it) with +10 coins (draft). Coins fly to the counter | 0:40 | `first_photo` |
| 6 | Arrow on the card's X: **Close** | Tap X. The stray hops into the display window, a heart pops: **Your cat!** Cat Index 1 of 10 stamps | 0:45 | `first_resident` |
| 7 | A customer walks in holding a dirty cat. Arrow on the customer: **Take cat** | Tap the customer (or walk up and press the prompt) | 1:00 | `first_customer` |
| 8 | The cat sits in the tub with its need icons. No dim this time, only an arrow on the first needed tool if the player is idle 8 seconds | Clean it with sponge and brush | 1:20 | none (side event) |
| 9 | Arrow on the customer: **Give back** | Tap. Coins, a tip and a star | 1:30 | `first_return` |
| 10 | When coins reach the first tool's price, arrow on the Tools board by the tub: **New soap!** | Tap the board, the Tools window opens with Bubble Soap lit, tap Buy, tap X | 2:00 | `upgrade_1` |
| 11 | When coins reach the Brush Table price, arrow on the builder kitten: **Build!** | Tap the kitten, the Builder window opens, tap Brush Table, tap X. A 10 second countdown shows over the station | 3:00 | `first_build` |

The tutorial ends after step 11. From here only the goal line guides the player, and the arrow only comes back as an idle hint (see below).

### After the tutorial (no dim, no arrows)
- About 4:00: a customer's cat shows a locked blow dry icon. Goal line: **Build the Dryer**. The Builder button shows the dryer's price.
- Dryer built: cats that need a dry pay more. Funnel step `dryer_built`.
- About 6:00 to 8:00 (gdd-draft, two build slots): with `LongBuildOffer` on, the builder kitten shows a speech bubble in the world with the VIP Room blueprint, **Start it before you go**. It is a bubble, not a window. The player taps the kitten to open the Builder window and starts it in the Rooms slot, which never blocks station builds.
- Notifications: the draft says the opt-in is offered right after the first long build starts. To keep "no window opens by itself", the Builder window shows a bell button, **Tell me when it's done**, next to any running build over 1 hour. Only the player's tap calls Roblox's opt-in prompt. Shown only to players who can get personal notifications (13 and over); younger players see a line in the Builder window, **Ready in 8 h. Come back to see it!**

## Rules for every step
- **Idle hints.** No input for 8 seconds on a step: the arrow pulses and grows. 20 seconds: a ghost hand shows the motion once over the target (it never does the step). Log `tutorial_hint` with the step number.
- **Only one thing points.** One arrow, one instruction. Nothing else may show on screen during steps 1 to 6 except the coin counter.
- **One owner for the dim.** A single `TutorialController` on the client owns the dim and arrow. Any other screen that opens during a step must ask it, so nothing clears the dim and leaves the player with no pointer.
- **Resume.** The reached step is saved. A player who leaves at step 4 starts the next visit at step 4 (with a fresh stray if the old one was mid wash). A finished tutorial never repeats.
- **Arrow targets are checked on touch.** Walking into the customer or the board must not open anything by itself; only the tap does.
- **Honest odds.** The first customer is always a fixed common cat for the tutorial, so the chance board at the door lights up from the second customer onward. That keeps every shown chance true. The board never shows during steps 1 to 6.
- **Device checks.** Phone (small and large), tablet, desktop and console. Touch targets at least 44 px; text at least 18 px on a small phone.

## Funnel `onboarding_v1` (for Growth and Gameplay-Engineer)
`joined`, `loaded`, `first_scrub`, `first_reveal`, `first_photo`, `first_customer`, `first_return`, `upgrade_1`, `first_build`, `dryer_built`. Ten steps, logged once per save on the server; a later step does not fill in a missed earlier one.

Side events: `tutorial_hint` (step), `time_to_step` (step, seconds since loaded), `left_at` (last step reached, first session only), `long_build_started`, `notify_opt_in` (shown or accepted). Two fields at most per event.

## Pace check on the draft numbers (needs Planning-Agent)
The draft's 5 minute timeline and its numbers do not agree.
- A window cat tips 1 coin a second (draft). A common cat pays 10 coins for about 30 seconds of work, so the window would pay three times more than washing. Players would earn 30 coins standing still by 1:15 and washing would stop mattering.
- With window tips taken out, a player has served about 5 cats by 3:00. After Bubble Soap (30) they cannot afford the Brush Table (60) at 3:00, and the dryer (150) is out of reach until about 8 minutes, not 5.

Proposed starting values (for tuning.md once Planning-Agent agrees): window tip 0.1 coin a second per cat with a cap of 1 hour of tips, Bubble Soap 30, Brush Table 40 (10 second build), Dryer 75 (1 minute build), common cat 10 coins plus a tip of 2 for a full clean. A quick run of the timeline with these gives soap at about 2:00, the Brush Table at about 2:50 and the dryer done by about 6:00. The pace rule (raise prices, never cut rewards) stays.

## Open points
1. Pace numbers above (Planning-Agent).
2. Is the bow choice kept for every cat, or only the first? Recommended: every cat gets a quick style pick, since it is the creative part players like.
3. Console: confirm the stick cursor for scrubbing feels fine in the first playtest.
