# Opening speed baseline, main e525885 (2026-11-24)
CAVEAT: the device simulator only changes screen size and graphics level. These are this PC's speeds in Studio (capped at 240 fps) and are for comparing builds, not real phone speed; the real check is Derek's iPhone 12 (Studio has no iPhone 12 preset: iPhone 13, 750x390 viewport, 844x390 screen, was used).
Method (METHOD.md on the PC, for an identical second run): fresh local unsaved rojo build; switches on in that place only: sudsWash, openingBox, sudsMascot, carryHold, tutorialTrail, tutorialTip, tutorialDim, spaPlot, scrubPrototype, scrubEffects, revealEffects, fluffEffects, catMotion, stinkEffects, scrubFeel, scrubTurn, customers, gameHud, recapCard, spawnView, washChecklist, plus skyDraft. Steps: tap box, tap Suds, walk to the tub, E for "Wash him" (the tub prompt is off screen on a phone so a tap cannot reach it), then 10 s of scrub drags. Frame times are RunService.Heartbeat deltas from a scratch LocalScript (_QAPerf, not committed). Average = frames / time; 1% low = 1 / 99th-percentile frame time; worst = longest frame. "Default" = Level 21 set explicitly (Studio's Automatic did not stick); Level 1 set from the client and Play restarted each time.

[Opening] lines (all within 0.2 s):
a06 default: truck moving 0.13 s after the join, 0.01 s after the scripts started
a06 Level 1: 0.14 s / 0.02 s
iPhone 13 Level 1: 0.12 s / 0.02 s
iPhone 13 default: 0.12 s / 0.02 s
Scene starts 0.04 to 0.05 s after the client script starts in all four runs.

a06 (706x339):
| Window | Default (Level 21) | Level 1 |
| Scene start + 6 s | 177.1 fps avg, 142.7 1% low, worst 767 ms | 177.5 avg, 141.2 low, worst 859 ms |
| Scene start to camera back | 1.25 s, 2 frames, worst 527 ms | 1.34 s, 3 frames, worst 859 ms |
| Wash view 10 s | 240.0 avg, 166.1 low, worst 7.0 ms | 240.1 avg, 165.9 low, worst 7.0 ms |
| Draw calls / tris mid-scene | 14 / 22,586 | 12 / 22,416 |
| Draw calls / tris mid-wash | 20 / 29,694 | 14 / 28,708 |
| Memory join / scene / wash | 2553 / 2907 / 2922 MB | 2588 / 2922 / 2942 MB |
iPhone 13 (750x390):
| Scene start + 6 s | 178.9 avg, 155.7 low, worst 736 ms | 176.6 avg, 143.9 low, worst 731 ms |
| Scene start to camera back | 1.41 s, 4 frames, worst 736 ms | 1.44 s, 4 frames, worst 731 ms |
| Wash view 10 s | 240.1 avg, 165.7 low, worst 7.0 ms | 240.1 avg, 166.2 low, worst 7.2 ms |
| Draw calls / tris mid-scene | 14 / 22,694 | 10 / 19,948 |
| Draw calls / tris mid-wash | 20 / 29,702 | 14 / 28,828 |
| Memory join / scene / wash | 2672 / 2959 / 2982 MB | 2641 / 2955 / 2989 MB |
Counts (same every run): at join workspace 2512 instances, 2068 parts, Stats.InstanceCount 14,160; mid-scene workspace 2849 / 2105 parts, InstanceCount about 68,970; mid-wash workspace about 3660 / about 2610 parts, InstanceCount about 69,800. Memory is Studio's whole-process total (includes Studio itself); compare between runs only.

Reading: the only stall is at the very start: one 0.5 to 0.86 s frame right after the scene starts plus a few more in the first 1.3 s; InstanceCount jumps 14k to 69k then (assets loading). The "camera handed back" marker fires at 1.3 to 1.5 s, during that stall, earlier than the roughly 5 s settle measured on 6fed572: could be the stall or a real change in #347; worth knowing for the second run. After the stall everything runs at Studio's cap; Level 1 vs 21 makes no fps difference on this PC; Level 1 only cuts draw calls (up to 6) and a few thousand triangles. Studio may not report draw calls fully. Mud did not clear in the wash view (simulator drags are not touch), so the wash window measures the view with a drag held, not real scrubbing.
New warnings/errors: none (no-DataStore notes, rbxassetid://203785492 x3, ProfileStore notice).
Files on the PC: Downloads\Clean-a-Cat-captures\perf-baseline-2026-11-24\ _QAPerf.client.luau (final measuring script) and METHOD.md. Second run: same switches, steps, both sizes, Level 21 then Level 1.
