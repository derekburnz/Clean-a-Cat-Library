# Dev switches run on main cf33eb4 (2026-11-26, Studio local place, iPhone 13 frame 844x390)
Summary relayed from the RC session; full files on the PC in Clean-a-Cat-captures\qa-cf33eb4-2026-11-26\ (job1 to job4 reports).
- Job 1 counter crate (PR 762 and 785 step-up): PASS. Bea moved place 3 to 2 with 2.8 s left; her crate landed at (1.55,3.44,-26.70), the place 2 mat; newcomer Theo's on the place 3 mat; no shared mats. Settled step-ups and a short-line newcomer land on their own mat. Heart-out packs the cat into the carrier. Bench shows 3 places. No script errors.
- Job 2 counter cards: FAIL. A newcomer's card never appears until its CounterPlace changes (6 of 6, also with counterCrate off; add() is never retried). Filed as issue 853, fix PR 854 (retest queued). Card size PASS 84x26. Starter ad does not cover the counter mats (mats x 176 to 440, ad 559 to 733).
- Job 3 bigSpa and counter window: PASS. 25 walks, all reached, 0 stuck, 2 teleports only from hand picked or just-spawned starts, every named spot reached by path. 240 fps PC cap, 121 to 137 draw calls. Waiting cats visible at the window.
- Job 4 HUD (hudTidy, fewerPills, helperPopups): PASS. Grid is Shop, Build, Helpers, More (not Shop Pets Quests More). More tray: Quests, Gifts, Pets, Index, Settings. Max 2 pills within 10 studs. HelperPaid only, no per cat toasts, Jo's world Level up prompt disabled. Minor: on the iPad frame a toast covers the tray captions; the Helpers window X touches the coin pill.
Not tested: plan steps 12 to 18 (buildWindow, freeRewards, abuse pass) pending extras run; real touch, saves, rejoin, two players.

## Extras (same build cf33eb4)
### A. Review-QA 18 step plan
PASS: 2, 3, 6, 7, 10, 12, 14, 15, 16, 17, 18.
FAIL 4: newcomer cards never appear until CounterPlace changes (issue 853, PR 854).
FAIL 5: after a join with a cat at the door there are no counter Take prompts, only the old SpotQueue1 prompt; CarryController.offerTake never rescans; prompts appear after one serve.
Not tested: 1 (fresh save opening), build start and Finish now (nothing affordable), starter saving text, steps 8 and 9 and 11 covered in jobs 3 and 4 above.
Free rewards: like row wording "A gift either way, 150 coins", paid 150 once; play row gives one crate once. Abuse pass: 250 junk fires, no grant, no errors.
### B. Design pictures (PR 793, 798)
Suds bubble portrait, Helpers icon, Cat Index pictures and recap portrait all draw; all 101 portrait ids fetch. Main now has its own Dirty2 to 4 pictures, so the level 1 fallback in the brief is outdated. Bench card not opened (bench showed 3 places).
### C. Motion-FX
catWalkOut PASS but plays at the photo payout, not at Next cat: hop 2.4 studs, trot to SpotQueue1, fades, gone in 3.2 s; tub empty 28 s after Next. Spa songs: SpaA 83.5 s and SpaB 96.0 s load; Music slider 0 stops the music. Tray and windows: one sound per open or close. Claim: one chime and 3 sparkles plus a crateDrop sound in the same frame. giftClaim, crateDrop, heartLow and spaMusicB are not loaded at first play. Not tested: Reduced Motion, six-customer volumes and frame rate (bench 3).
### D. Model issue 791
Tangles go per stroke but sometimes two at once. Inky stays side-on after scrubTurn through bow and photo. Muffin tail angles out, Rosette fan tail wider than body, nothing pokes through the tub. No fluff puffs on any cat because hideFluff hides them by design since 2026-11-24, which conflicts with 791.
### Quirk
The iphone_13 simulator adds a mirrored second touch on every click; drags were run on the desktop frame. No script errors anywhere. 34 pictures stay on the PC in Clean-a-Cat-captures\qa-cf33eb4-2026-11-26.
