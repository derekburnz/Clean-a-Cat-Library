# Test plan 2026-11-26: today's dev switches

Written by Review-QA-Agent for Sync-Agent's Studio run. Build: main at e0bfa9e or newer (dev publish run 493 passed). One run covers all nine switches, since they stack on the same counter and HUD.

## Setup
- Fresh unsaved local copy of the place built from main. Never the real place window, never save it, never join live servers.
- Switches on, matching dev: counterLine, counterCards, counterCrate, bigSpa, hudTidy, fewerPills, helperPopups, buildWindow, freeRewards, plus what they need (customers, customerCarry, heartBar, giftStand, pets, smallPrompts). Everything else as dev has it.
- Two saves: a fresh save (opening plays) and a seeded save (about 2,000 coins, one helper hired, no bows bought).
- Device frames: iPhone 14 (844 x 390) for every step, plus one desktop frame per window. Studio cannot fake touch, so tap paths are read from the code or left for Derek's phone.
- Movement: only `_G.qaWalkNamed` or `_G.qaWalk` (skill `studio-test-movement`). Report each walk as reached, method, seconds. bigSpa moves the spots, so use the named spots, never fixed numbers.
- Record the console after every step. Any new error or warning from our scripts is a FAIL for that step.

## Steps and pass rules

### A. bigSpa (the bigger building)
1. Start Play with the fresh save. Pass: the bigger spa and its street load (no small spa), opening plays, no errors.
2. Walk Spawn, Tub, DoorLine, Board, Window, GardenGate, VipDoor, PadJo. Pass: every walk reached by `path` or `path+retry`, none by `teleport`. A teleport names the spot that is blocked.

### B. counterLine, counterCrate, counterCards (the counter window)
3. Seeded save. Wait for three customers. Pass: each walks up with a crate, sets it on the counter, the cat walks out of the crate and sits on a mat (CounterReadyAt about 2.4 s after CounterSetAt). The carrier is empty.
4. Pass: each cat on the counter has a card: a round chip in its owner's shirt colour and its heart bar; neighbouring cards alternate rows and never cover each other; the cards are readable at 844 x 390.
5. Take the second place's cat (not the front). Pass: it is taken from its own mat, no walk to the back of the line; the front customer's cat stays on the counter.
6. Step up (PR 785 retest of FAIL 1): serve the front while a newcomer is still walking in. Log CounterPlace and CounterCrateSpot each frame. Pass: the newcomer's crate lands on their current place's mat, never on the old one, and no two crates share a mat.
7. Let one heart bar run out. Pass: that customer packs the cat back into the crate and leaves; the card goes with it.

### C. hudTidy, fewerPills, helperPopups (the HUD and pop-ups)
8. Pass: the side buttons are a 2 by 2 grid (Shop, Build, Helpers once one is hired, More); More opens a tray with the rest; the coins sit on a solid pill; no waiting faces on the HUD; the starter pack is a side ad showing its struck total and a true saving (199 of 547 shows "save 63%" or less, never more).
9. Stand by the counter with several prompts near. Pass: at most two prompt pills show, the nearest within 10 studs; E still works on each one in turn.
10. Let the hired helper finish a cat. Pass: a popup over their stand, no "+N coins: NAME washed CAT" toast, no per cat toasts; one-off toasts (a first, a level) still show. The stand has no Level up prompt in the world.
11. Note whether the starter side ad covers the counter's right end at 844 x 390 (known from PR 774). Report only.

### D. buildWindow
12. Press Build in the HUD grid away from the board. Pass: "Build and upgrades" opens with every build, its price and time (or countdown, what it waits for, or Built), every tool and the next bow with Buy; it scrolls; nothing clipped at 844 x 390.
13. Buy a tool and start a build from the window while away from the board. Pass: both go through and coins drop by the shown price. Then press Finish now away from the board. Pass: refused until the player is at the board.
14. With too few coins, Buy is grey and does nothing.

### E. freeRewards (the gift card)
15. Open the gift card. Pass: the Free Rewards rows show (like the game, and 30 minutes of play) beside the favourite plus group row.
16. Like row: the Claim appears 10 s after the ask and pays 150 coins once. Claim again or rejoin: no second pay. The wording names no reward for the like itself before the ask (policy: never reward a like is checked on #531; record the exact on-screen words).
17. Play row: set the save's play time near 30 minutes, or wait. Pass: one normal crate, paid once per save.

### F. Abuse pass (server checks)
18. From the Client datamodel fire RequestBuild, RequestBuyTool and RequestBuyBow 50 times in a second with valid and junk arguments, and Finish now from across the map. Pass: no extra spend, no grant, no error spam; Finish now refused away from the board.

## Report
Save it as `library/Sync-Agent/studio-reports/dev-switches-<sha>-2026-11-26.md`, pass or fail per step with console text and walk lines; pictures on a draft picture PR as usual (never merged). Review-QA files each FAIL as an issue.
