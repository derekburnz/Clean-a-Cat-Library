# Policy check of everything sold (issue 531), 2026-11-26

Review-QA-Agent, read from main at e0bfa9e against the `monetization-policy` and `roblox-policy-compliance` skills. Code reading only; the Studio and dev checks are listed at the end.

## Verdict
PASS for the code as built. Nothing can sell yet: every product and pass id is 0 in both dev and live, so all buy buttons stay hidden until Derek creates them.

## What was checked
| Item | Result |
|---|---|
| Robux crates (CrateOne, CrateFive; `crateShop`) | PASS. A bought crate is the earned normal crate with the same list. `CrateRules.odds` gives every pet a percent (normal 25 25 13 13 8 8 6 2, good 15 15 15 15 12 12 12 4, each 100) and `roll` uses that very list. The crate window shows the list on the same screen as the buy rows, before any tap. |
| PolicyService | PASS. Read on join with 3 tries; anything but a clear "not restricted" hides the shop (fail closed). The server checks again on every buy. Earned crates stay for everyone. A Studio attribute plays a restricted player. |
| Coins for Robux | None. No product gives coins, so no currency route turns into a paid random item. |
| Receipts | PASS. One ProcessReceipt owner; PurchaseId saved with the grant; NotProcessedYet until the save holds it; granted even if a switch went off since. |
| Starter pack (199) | PASS. Fixed contents (three passes), real 72 hours from first join kept on the server, never restarts or extends, offered only after the tutorial and only to a player with none of the three, opens only on tap. The saving is computed from Roblox's real pass prices and rounded down (199 of 547 shows 63%). |
| Finish now (5 tiers) | PASS. Waiting is always free, price by time left, no price under the hide limit, a paid skip on a build that finished first is kept as credit. |
| Passes (five) | PASS. Price read from Roblox and shown before the confirm; the shop text says what each gives. |
| Like row, favourite and group gift | Owner decision, recorded. Our house skill says never reward likes or favourites; Derek chose the favourite plus group gate for Starcoat (2026-11-25) and the like row's "A gift either way, 150 coins" (2026-11-26). The like is never checked or faked as checked and the coins come either way. No Roblox rule was found for or against (Growth-Agent's check of 2026-11-25). Not blocking. |
| Like ask (`likeAsk`) | PASS on wording: no reward named, the spec bans coin, gift, free and grow. |

## Before anything sells on live
1. Derek creates the dev products and passes and pastes the ids; Review-QA rechecks the dev set and that every price shows.
2. Derek declares paid random items in the experience questionnaire before `crateShop` goes on anywhere.
3. On dev: a restricted test player sees no crate rows; an allowed one sees the chance list before the buy rows.
4. On promotion: the live ids go in, Review-QA rechecks the live set, and the policy pages linked in `monetization-policy` are read again in case Roblox changed them.
