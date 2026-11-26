# Paid skips on build timers: check and proposal (2026-11-25 ET, Growth-Agent)

For Planning-Agent. Derek chose "sell skips at launch" on 2026-11-25. Sources: the Roblox pages read earlier today (monetization foundations "Presenting products", developer products, passes, paid random items) and our monetization-policy skill. OFFICIAL = on a Roblox page, JUDGMENT = my call. No Roblox data exists on skip prices or buying rates.

## Short answer
Allowed. Sell it as a developer product in a few fixed price tiers by time left, button on the builder panel, never as a pop-up, waiting is always free. It does not clash with the Second Builder pass if the tiers are set as below.

## Is it allowed
- Not random, so the paid random item rules do not apply.
- OFFICIAL: players must not be misled, confused or pressured. A countdown must be accurate and must not restart. No false "limited time". Pushy words are out for minors ("Finish now" is fine, "BUY BEFORE IT'S GONE" is not). No page forbids a Robux skip of a timer. Roblox does list "timers that can be removed or brought forward" as unpopular with players, which is a design warning, not a rule.
- OFFICIAL: a thing the player "uses up" is a developer product, not a pass.

## Product type and price rule
- **Developer product**, one per tier (a developer product has one fixed price, so a price that moves with time left cannot be one product).
- **Tiers by time left on that build** (JUDGMENT, numbers to be tested):
  | Time left | Skip price |
  |---|---|
  | under 1 hour | 15 Robux |
  | 1 to 4 hours | 35 Robux |
  | 4 to 12 hours | 75 Robux |
  | 12 to 24 hours | 99 Robux |
  Rounded up to the next tier, shown before the confirm as "Finish now, 35 Robux", and the tier is fixed at the moment the player taps (it does not change while the Roblox confirm is open). Check the builder panel text matches the product price the server reads from the catalog.
- No skip for builds under about 1 hour (they take seconds to minutes by design and a skip there teaches players to pay for nothing).
- **The first long build** (the 8 hour VIP Room offered in session one) has no skip. JUDGMENT: it is the day 2 reason to return, and Derek's goal is a strong day 2. Skips open once the player has come back once or when the second long build starts. Keep this behind a switch so Derek can change it on real numbers.

## Where the button sits and how it stays kind
- On the builder panel next to the build's timer, one small button. Nothing pops up, no banner, no notification mentions a skip.
- Price shown on the button; Roblox's own confirm shows it again. No countdown, no "only today", no crossed out price.
- A no is final for that build and the session: the button stays, but is not highlighted or animated, and no prompt follows a decline.
- The timer text always shows the true time left; waiting is always free and nothing is lost by coming back late.
- Hide the button until the timer is at least an hour long (see above), and for players where PolicyService or parental controls restrict spending if the game uses a spending check later.

## Build notes for Gameplay-Engineer (JUDGMENT, for the issue)
- The server owns the build end time. The skip product handler is idempotent and saves before it returns granted.
- If the build already finished or changed by the time the receipt arrives, keep a "skip credit" for the same tier or lower so the player is never charged for nothing. Log it as a failure case for review.
- Log: `skip_offer_seen` (tier), `skip_bought` (tier), `skip_credit_used`.

## Sitting beside the Second Builder pass
- They fix different things: Second Builder gives a second build slot (more things at once, a permanent upgrade, a game pass); a skip finishes one build now (a one-off purchase).
- To not undercut: price the Second Builder pass so a regular player pays for it with about the cost of three to four skips (suggest 249 to 399 Robux), and keep skips by tier so one skip never costs more than the pass. Do not give the pass a free skip and do not discount skips to pass owners.
- JUDGMENT, honest risk: skips make the long timers less of a reason to return, which was the day 2 hook. Watch day 1 return for skip buyers versus the rest, and tell Derek if day 1 falls after skips go on. A skip switch off is the fast rollback.

## Line for the monetization calls table
| Idea | Type | Policy | Verdict |
|---|---|---|---|
| Skip build, 15 / 35 / 75 / 99 Robux by time left | developer product (4 tiers), not random | accurate timer, price shown before confirm, no pressure wording, no prompt after a no | yes, behind a switch; not on the first long build, not on builds under 1 hour |
| Second Builder, 249 to 399 Robux | game pass | none | yes |

## Open for Derek
1. First long build without a skip (my pick) or with one from the start.
2. Tier numbers: my starting guess, to be tuned from real sales.
3. Whether Second Builder owners get any skip benefit (my pick: no).

## Update 2026-11-25 (latest): Derek: skip any build, the first long one too ("Always can pay for skips for any build")
Derek's call, so it replaces my picks on the first long build and on builds under an hour. My numbers and rules (JUDGMENT, tune from sales):
| Time left | Skip price |
|---|---|
| under 2 minutes | 5 Robux |
| 2 minutes to 1 hour | 15 Robux |
| 1 to 4 hours | 35 Robux |
| 4 to 12 hours | 75 Robux |
| 12 to 24 hours | 99 Robux |
- **Short builds:** the smallest tier is 5 Robux so a child is never asked for 15 Robux to skip 30 seconds. Hide the button when under 15 seconds are left (the wait is shorter than the confirm).
- **Against a mistaken press:** (1) Roblox's own confirm shows the price and needs a second tap, so every skip is already a two step buy; (2) the Finish now button is small and never sits where the Start build button was, so a double tap cannot hit it; (3) ignore taps for a second after the panel opens; (4) if the build finishes before the receipt is processed, keep a skip credit of that tier, never charge for nothing (already in the build notes).
- **First long build now skippable:** this weakens the day 2 reason to return, which was Derek's top goal. Keep it behind its own switch and compare day 1 return between players who skipped the first long build and those who did not. Tell Derek if skippers return clearly less.
- **Waiting cats leaving** (Derek: a cat leaves when its heart bar is empty and the job is lost): fine for a young audience if the heart bar is visible and drains slowly. JUDGMENT rule: never sell a way to keep or bring back a leaving cat, and never flash a price at the moment a cat is about to leave. That would be pressure at the moment of loss.
Table lines: Skip build: developer product, tiers 5 / 15 / 35 / 75 / 99 Robux by time left, any build, behind a switch, no countdown or pressure wording.

## Update 2026-11-26: tiers as built (Gameplay-Engineer, PR 588)
The build uses these tiers instead of my first guess, same price ladder: FinishTier1 5 minutes or less 5 Robux, FinishTier2 30 minutes or less 15, FinishTier3 2 hours or less 35, FinishTier4 8 hours or less 75, FinishTier5 more than 8 hours 99. I accept them; builds never exceed 24 hours, so tier 5 covers the rest. A skip credit is a finish bought for a build that ended on its own before the receipt landed; the next Finish now it covers is free. The button never shows until the five products exist. These replace the tier tables above.
