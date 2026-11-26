# Clean a Cat: everything sold, with the policy check (2026-11-26 ET, Growth-Agent)

One table for Review-QA's policy check (#531) and Derek's product list. Built from the agreed design (docs/design/clean-a-cat/gdd.md) and the checks of 2026-11-25 in this folder. Rules: OFFICIAL = Roblox page read 2026-11-25, JUDGMENT = my call. Money numbers stay in the library, not the public repo.

## What is sold
| Item | Kind | Robux | Random? | Policy points | Verdict |
|---|---|---|---|---|---|
| 2x Coins | game pass | 199 | no | none while no Robux product gives coins | ok |
| Second Builder | game pass | 299 | no | none | ok |
| Golden Sponge | game pass | 99 | no | none | ok |
| Lou, extra helper with his station | game pass | 249 | no | same output as earned helpers; says exactly what it gives | ok |
| Second pet slot (player and every worker) | game pass | 249 | no | none | ok |
| Crate | developer product | 49 | yes | odds as percentages before buying, summing to 100; PolicyService per player; hidden where restricted; earned crates share the same list | ok once the chance list and PolicyService check are built |
| 5 Crates | developer product | 199 | yes | same as above | ok after the single crate works |
| Finish now, tiers 1 to 5 | developer product | 5, 15, 35, 75, 99 | no | price on the button and Roblox's confirm; accurate timer; no pop up; no prompt after a no; credit if the build already finished | ok |
| Starter Bundle | developer product | 199 | no | real item prices (parts 547, saving 348 = 63%, shown as 63%); accurate server owned 72 hour clock from first join, never restarts, gone for good at zero; hidden if the player owns any part; no coins or crates in it; "Bundle", not "sale" | ok |
| Private server | Roblox setting | 100 per month | no | Plus subscribers get it free from Roblox; price change cancels subs; under 13 may be unable to join | Derek sets it |
| Free pet at the gift stand | in game reward | 0 | no | favourite and group checked, like asked and never shown as checked; no Roblox page allows or bans it; wording honest | small unconfirmed risk, Derek's call |

## Checklist for the policy check (tick each against the build)
1. No Robux product gives coins, and nothing sold is a way to keep or bring back a leaving cat.
2. The crate shows every pet and its percentage before the buy, the numbers sum to 100 and match the code; where a luck boost or pity exists (none planned), its numeric effect is shown.
3. PolicyService is read per player on the server, cached, defaulting to restricted on failure; the Robux crate is hidden or blocked where `ArePaidRandomItemsRestricted` is true; earned crates and fusing still work for those players.
4. Fusing costs pets only and has a fixed result; no fuse token or fuse boost is sold.
5. Prices are shown before every confirm and read from Roblox, not typed in the UI. The pack's "save" figure is computed from live prices.
6. The pack clock is on the server per player, never restarts, and hides the pack for anyone who owns a part; a purchase started before zero is honoured.
7. Finish now: the button hidden under 15 seconds, small, away from the Start build button, taps ignored a second after the panel opens; a skip credit is kept if the build ended first; the receipt saves before it returns granted.
8. No word "free" next to a paid item, no pressure wording ("hurry", "last chance"), no countdown outside the pack, no badge that never clears, at most four items on a shop screen.
9. Every purchase handler is idempotent; every purchase is checked on the server; purchase_step events log prompt, cancelled, granted.
10. Gift stand: card says exactly what is checked; players who cannot favourite or join are not blocked from anything else; the Creampuff Games group wall is off or moderated.
11. Maturity answers match the build (see maturity-questionnaire-answers-2026-11-25.md); re-answer after any new feature.
12. Passes and products are created only after the code that grants them is merged (passes cannot be deleted).

## Order of work
Crate chance list and PolicyService first, then the Robux crate, then the pack's server clock, then skips, then passes in the shop.
