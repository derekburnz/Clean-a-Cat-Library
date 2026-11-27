# Economy recheck, 2026-11-26 (Design-Agent)

Issue 841, PR 842.

## Result
- First tool after about 3 cats: **holds**. The first tool is bought at about cat 2 to 3.
- Second Tub at about cat 5: **holds** (cat 5, about 4:05).
- First helper after about 15 cats: **broken by today's gifts**. Jo (150) now comes at about cat 6 (4:45) when the like reward lands with the first special visitor, and about cat 10 (7:25) without it.
- Fix: Jo costs 300 behind the new switch `joPrice`, off by default. With it on, he comes at cat 15 (10:45) without the like reward and at cat 10 to 12 (about 7:30) with it.
- Day 2 reasons: **hold**. They are the good crate on check in day 2, the long Third Tub build, the jar and the daily quests. The jar's 30 an hour per helper is capped at 8 hours, so one helper gives 240 coins.
- No runaway in the first hour. Hand washing makes about 1,600 coins an hour, and Sam 1,200, the Third Tub 1,000 and the bows are waiting. With the starter pack (2x Coins and Golden Sponge, 2.4x on hand washes) it is about 3,900 an hour, which is paid power by design.

## Today's changes, one by one
| Change | Effect on pace |
|---|---|
| Counter window: faster to take a cat | Cats per minute go up, about 40 s to 32 s a cat, so purchases come sooner in minutes, not in cats |
| Free Rewards: 150 coins (like) | The big one. It can land at about 4:40, so Jo at 150 is bought at once |
| Free Rewards: crate at 30 min | No coins; pets boost tips and helper pay, within the pet cap |
| Old station refund | Paid once, only on older saves that built those stations; at most 215 coins; no new player gets it |
| Starter pack 199 Robux | Same contents; more buyers, 2.4x hand pay for them |
| Helpers earn while away | Jar: 30 an hour per helper, 8 h cap, Garden 37.5 an hour and 12 h |

## Model
16 coins a cat (+2 after the Second Tub). Cats come at 1:00, 2:00 and 2:45, then every 40 s. The check in pays 50 at 3:45. Quests open at 6:00 (bows 40 after 3 cats, washes 50 after 5). Order of buying: tool 30, Second Tub 60, Jo.

| case | Jo 150 | Jo 300 |
|---|---|---|
| check in and quests, no like | cat 10 (7:25) | cat 15 (10:45) |
| plus the like reward at 4:40 | cat 6 (4:45) | cat 10 (7:25) |
| plus the like reward and 32 s a cat | cat 7 (4:53) | cat 12 (7:33) |

To do on dev: turn `joPrice` on and re-time the first 15 minutes on the iPhone 12.
