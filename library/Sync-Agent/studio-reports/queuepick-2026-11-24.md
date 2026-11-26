# queuePick checks (PR #202, #207; figure step for PR #208 pending), 2026-11-24

Verdict: all three checks behave as intended; #207's rule (no pick before the first customer is paid) works on 592ca9d.

Setup: fresh local places built with Rojo, never saved or published. scrubPrototype, customers and queuePick on from the server in Play, full-size Studio window. Save is a fresh local one: no DataStore, 0 stars.

## 1) Wash next on place 3: PASS (commit 93748d3, PR #202)
- Before: tub Cotton; door line 1 Inky, 2 Smudge, 3 Toffee.
- Walked to the door (place 3's prompt 4.8 studs away), pressed E on "Wash next". Line became 1 Toffee, 2 Inky, 3 Smudge.
- Finished the Cotton visit (scrub, brush, bow, camera). After payment the next cat in the tub was Toffee, the cat that had been at place 3. The line refilled to 1 Inky, 2 Smudge, 3 Toffee (a newly rolled Toffee at the back).
- Shots: queuepick-1a-before-pick-place3.jpg, queuepick-1b-after-pick-place3.jpg, queuepick-1c-next-cat-is-toffee.jpg

## 2a) Fresh save, pick place 2 before serving anyone, BEFORE #207 (93748d3)
- The first cat was already in the tub when the switches came on: Smudge, common, as the first customer always is.
- Door line 1 Muffin, 2 Muffin, 3 Cotton. "Wash next" prompts were already there and pressing E on place 2 was accepted; places 1 and 2 were both Muffin so the line looked the same afterwards.
- So on this commit you can pick before the first payment. The first cat stays common because it is already in the tub before the line is offered.
- Shot: queuepick-2a-fresh-save-pick-place2-93748d3.jpg

## 2b) Same step on main at 592ca9d (PR #207): PASS
- Before the first payment: tub Cotton, line 1 Inky, 2 Patches, 3 Cotton. No "Wash next" prompts at all (QueuePick folder had no prompts, player's ChanceBoardLit not set). Pressing E at place 2 did nothing.
- After finishing the visit the toast said "+12 coins, +1 star". ChanceBoardLit turned true and both prompts (place 2 and 3) appeared straight away, enabled. Next tub cat Inky, line 1 Patches, 2 Cotton, 3 Cotton.
- Shots: queuepick-2b-no-prompts-before-first-pay-592ca9d.jpg, queuepick-2c-prompts-after-first-pay-592ca9d.jpg

## 3) Spamming the prompt: PASS, no console errors (93748d3; same on 592ca9d)
- 12 presses of E, 40 ms apart (about 8 a second), on place 2. The server limits this remote to 1 a second (burst of 2), so most presses were quietly dropped.
- The line ended as it began (1 Muffin, 2 Muffin, 3 Cotton). Each accepted pick swaps the same two Muffins, so the result cannot show how many got through (a limit of this test, not a finding).
- Console: nothing new, only the usual no-DataStore notices and the three rbxassetid://203785492 lines.
- Shot: queuepick-3-after-12-fast-presses-93748d3.jpg

All shots on the PC in C:\Users\Derek\Downloads\Clean-a-Cat-captures\.
