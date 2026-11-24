# PR #54 effects cost (head 8537bd3), 2026-11-23

Fresh local place on Derek's PC, never saved. PR #54 was already merged, so its head commit was tested. This is a PC baseline, not a phone result: the device emulator needs screen control (that prompt timed out) and only changes screen size and touch anyway.

Method: scrubPrototype on, camera orbiting the tub, drag on the cat about 25 s per run, three scrub, reveal and mud-return cycles. Run A effects off; run B scrubEffects, revealEffects and fluffEffects on.

- Frame time: 4.17 ms average in both (Studio frame cap). 95th percentile 5.31 ms off vs 5.27 ms on. Worst frame 11.2 ms off vs 8.7 ms on.
- Render CPU: 1.28 ms off vs 1.27 ms on (95th 1.66 vs 1.56).
- Render GPU: 0.34 ms off vs 0.35 ms on.
- At most 4 particle emitters and 8 instances at once; cleaned up between cats.
- No game errors in the console.
- fluffEffects never fired: this commit has no brush step yet.

Side finding: with the camera circling the tub, a full scrub to reveal took about 4 s, which supports the PR #56 finding that hidden patches, not tuning, make the first scrub slow.

Needs a real phone or the MicroProfiler on a device to confirm phone frame cost.
Screenshot on the PC: C:\Users\Derek\Downloads\Clean-a-Cat-captures\pr54-01-effects-mid-scrub.jpg
