# Motion-FX moments and sounds pass on main dc51ecb (includes PR 719), 2026-11-26
Unsaved local place, iPhone 13 frame, real taps. Studio uses the low effects tier. Switches: everything OFF_BY_DEFAULT on except toolCursor, streetLoadTest, exampleFeature, openingReplay, benchGrow, cameraClear (scrubEffects, revealEffects, fluffEffects, dryEffects all on). Draft PR 720 has the results and 7 pictures in docs/vfx/clean-a-cat/fx-pass-dc51ecb (names checked, no assignee or reviewer, not merged).

## NOT (5)
1. buildDone, questDone, checkIn never fire. AudioController listens for Moments.BuildFinished, QuestDone and CheckInClaimed, but Moments has none of those signals. Builds finished and the check-in claim worked, with no cue.
2. #4 foam trail: Effects.stream("foamTrail") is never called while scrubbing.
3. #7 hop to the window: ScrubController fires Moments.CatToWindow, nothing listens to it.
4. Pet reveal pop: no wiggle after it. The pop works: scale 0.04 to 0.78 to 0.70 in 0.45 s, head and tail stay on.
5. #6 flashes: 4 sparkle bursts in 0.36 s when the cat is fluffed, over the limit of 3 a second.

## PLAYS
scrubLoop, bubblePop, mudPlop, revealChime, catShake, stepChime, brushSwish, purr, bowPop, camera, heartLow, catLeave, crateOpen, petReveal, starUp (real Fuse tap), workerDone, visitorChime, glow, bow popIn with 3 hearts, visitor highlight and sparkles, worker take, gift sparkle every 4.5 s.
Walk-off: quarter turn in 0.4 s, then walk at 3.2 studs/s, faded and gone by 2.6 s. Mood: customer at 0.14 heart had head down 6 degrees (foot tap not measured). Garden ambience: 1 petal/s, about 5 on screen, blossom clouds rise and settle 0.12 studs in all. Fur puffs left out on purpose; the brush shine plays instead.
Not measured: the 0.15 s fleck fade and the 0.4 s dirt fade.
Peak particle counts (low tier): 4 mud flecks a patch; at the reveal 6 sparkles, 6 drops and 8 flecks three times; 3 hearts at the bow; about 5 Garden petals.
Every sound loaded; now and then one bubblePop showed as not loaded and the next ones loaded. Volumes all 0.45 or less. Console: only known lines. Play stopped, nothing saved or published.

# Recheck on main 4954d9c (PR 722 merged, PR 719 already in): all four PASS
Correction: Motion-FX's guess was right; the earlier "foamTrail never called" was wrong (the first-call log line had scrolled out of the printed part). This time every foam call was kept: on a slow rub Effects.stream was called 14 times at drag speeds 0.17 to 2.29, raw rate rounded to 0 on 13 of them.
Method: same local place with the 6 files changed since dc51ecb copied in from 4954d9c (EffectsController, Effects/init, Crate, the new Hop, WorkerService, WorkerRules), fresh save with 14 crates, same switches (scrub/reveal/fluff/dry on). iPhone 13 frame, low tier. Wash started with E, later steps with the Studio test step; bow and photo were real taps; crate opened with the RequestOpenCrate remote, not a tap.
1. Foam on a slow rub: PLAYS. With PR 722's floor the rate is 3/s on every call. Fast rub: 1,031 calls at speeds up to 158, rate 3 to 8 (low-tier cap), 3.05 on average.
2. Fluff flashes: PASS. 2 sparkle bursts at the same moment (shake burst plus brush sparkle), then none until the photo 21 s later (was 4 in 0.36 s).
3. Stray hop: PLAYS. 1.6 s after the photo the stray rises 0.60 studs and lands with a dust puff. It hops in place in the tub, then shows on the window seat as a separate copy, so it is not a hop onto the cushion (question for Motion-FX: should it travel?).
4. Pet reveal wiggle: PLAYS. After the pop (0.78 to 0.70) the pet turns side to side between 0.51 and 0.71 s, -4.6 to +7.6 degrees; head and ears stay on the body.
Reveal now shows 1 sparkle burst plus drops and flecks three times. Console: known lines only.
Peak particles (low tier): foam 3/s slow, up to 8 fast; 12 sparkles at the fluff; 5 dust at the hop; 6 sparkles twice at the pet reveal. No FAIL, no new pictures; notes added to draft PR 720. Nothing saved or published.
