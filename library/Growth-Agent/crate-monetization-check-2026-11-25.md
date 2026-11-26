# Crate sold for Robux: policy check, price and table line (2026-11-25 ET, Growth-Agent)

Answers Planning-Agent's note of 2026-11-25 (Derek: crates can be earned rarely or sold for Robux; second pet slot is a Robux upgrade). Source: Roblox's paid random items page, read 2026-11-25, no update date shown. OFFICIAL = on that page, JUDGMENT = my call.

## Check of points 1 to 5
1. **A Robux crate is a paid random item: confirmed.** OFFICIAL: bought directly with Robux or with a currency bought with Robux counts. Must show every outcome and the real chance as a percentage before the player spends, adding to exactly 100%. If the list is long it can sit behind a pop-up whose button says a word like "Odds" or "Details" (a bare (i) icon does not count). Rounding is allowed with the disclaimer wording on the page. PolicyService per player: if `ArePaidRandomItemsRestricted` is true, that player must not get the Robux crate. Allowed ways to handle them: an unpaid earnable route, fixed ordered outcomes shown before purchase, direct purchase of a chosen pet priced at the expected value, hiding the crate, or blocking the buy with a message. Our pick (hide it, they keep the earned crates) fits.
2. **Sure new pet rule removed: fine.** Pity systems are not banned. If one is paid for, it is a "probability modifier" and its effect must be shown as a number. We have none.
3. **Earned and bought crate are the same crate with the same chances: allowed.** OFFICIAL: the page is silent on this; free random rewards need no odds list but showing the same list is harmless and builds trust. Our own rule, not Roblox's, and a good one.
4. **Coins do not buy crates, so 2x Coins is outside the question: correct.** Warning: this holds only while no Robux product gives coins. If a pack ever gives coins, then crates bought with coins become paid random items too. The starter pack has no coins, and the double tips boost makes earned tips, not bought currency, so it is fine.
5. **Starter pack stays fixed contents, no crate: correct.** OFFICIAL (Community Standards, via the earlier read): a bundle with a random item in it makes the whole bundle a paid random item. Keep every part of the pack fixed and visible, then restricted players can still see it.

New points found:
- **One of each pet:** OFFICIAL: if a player can only own one of an outcome, the odds shown must update to that player's remaining chances. Decide whether duplicates exist. If a duplicate turns into something (coins, a token), that outcome must be shown in the list too.
- **Trading:** OFFICIAL: for players with `IsPaidItemTradingAllowed` false, pets from paid crates cannot be traded. We have no trading at launch, so nothing to do.
- **The page is silent on:** selling a pack of several crates, bulk discounts, gifting, and age or spending limits. Bulk packs are therefore not forbidden, but the general pressure rules still apply (no fake "best value" claims, a discount must be a real one).
- **Not a Roblox rule but in our monetization-policy skill:** no near miss teasing on a reveal, no spend streaks, prices shown before the confirm, and a decline is respected.

## Price (JUDGMENT, no Roblox guidance or benchmark exists)
- **One crate: 49 Robux.** Pet Store Tycoon sells a pack of 3 random pets plus cash for 99 Robux; one crate at about a third of that keeps a first purchase small for a young audience.
- **Pack of 5 crates: 199 Robux** (about 19% off 245). Say "5 crates" and the price, nothing else; no countdown, no stock counter, no crossed out price.
- Keep the first launch to these two. Read sales from the transactions page with player counts beside every rate, and change one thing at a time (ab-tests.md). Do not trust a read under a few hundred players who saw the shop.
- Option for Derek, not required: a daily limit on Robux crates per player. Roblox's page has no limit, but it protects young players and costs little. Recommended: no limit at launch, review after the first reads.
- Rare pets: the chance list must match the code, and the rarest chance must be shown, not hidden behind the pop-up.

## Line for the game's monetization calls table
| Idea | Type | Policy | Verdict |
|---|---|---|---|
| Crate (one), 49 Robux | developer product, random | odds shown as percentages before purchase, PolicyService, hidden for restricted players, earned crates stay | yes, with the odds list and PolicyService built first |
| Crate pack of 5, 199 Robux | developer product, random | same as above | yes, after the single crate works |
| Second pet slot | game pass | none (player's slot only is the pick) | yes |
| Spa Starter Pack, 99 Robux | developer product, fixed contents | none while every part is fixed; no crate, no coins in it | yes, once per player, shown once on the next visit |
| 2x Coins | game pass | none while no Robux product gives coins | yes |
| Buy coins with Robux | developer product | would make coin bought crates a paid random item | no |

## Open for Derek
Second slot: player's slot only (pick) or workers' too. Whether to sell crates in packs (my pick: yes, a 5 pack) and whether to cap crates per day (my pick: no cap at launch).

## Update 2026-11-25 (later): doubles and fusing (Derek: keep doubles, fuse 3 into a star up)
Source: same Roblox page, read earlier today. OFFICIAL = on the page, JUDGMENT = my call.
- **Doubles need no odds update.** OFFICIAL: the only rule on repeats is that if a player can own just one of an outcome, the shown odds must update to that player's remaining chances. With doubles kept, every pet stays possible every time, so the list stays the same for every player and every crate.
- **The list must say what a double is.** JUDGMENT: add one plain line under the chances, for example "Pets you already own are kept. Three of the same can be fused into a star up." Every outcome in the list is still a pet with its percentage, summing to 100%.
- **Fusing itself.** Roblox lists "combination" and "enhancement" among paid random item types. That applies when Robux pays for it (directly, or through tokens, keys or a currency bought with Robux) and the result is random. Keep it clear of that:
  - Fusing costs pets only. Never sell fuse tokens, fuse boosts or a Robux fuse.
  - Make the star up result fixed (three of one pet always give one star up). A fixed result is not random, so no odds are needed. If a star up ever had a random outcome, show its odds, and it must stay free of Robux.
  - Pets bought in crates can be fused like earned pets. That does not make fusing a paid random item, because the Robux went into the crate, not into the fuse.
- **Pity or luck:** still none planned. If a luck boost is ever sold, its numeric effect must be shown and the odds must update while it is active.
- **Restricted players** (PolicyService) still get no Robux crate but keep earned crates, doubles and fusing.
