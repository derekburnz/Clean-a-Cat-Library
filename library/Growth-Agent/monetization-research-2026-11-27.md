# Monetization research for Clean a Cat: store, passes, products, offers (Growth-Agent, 2026-11-27 ET)

Derek's ask: good monetization strategies and designs for Roblox games. This file has prices, so it stays in the shared Growth folder and never goes into a public repo. The no-price layout version is already merged: `docs/growth/shop-layout-research.md` (PR 1072, issue 1070).

Labels: OFFICIAL = Roblox page. SEEN = Derek's own playtest screenshots (Coordinator/references/), prices read off phone screenshots so a digit can be off. CLAIM = a third party or forum post, not checked. JUDGMENT = my call. Honest limit: no readable source gives conversion numbers by price or card position, so everything below that is not OFFICIAL or SEEN is a starting guess to be tuned from our own reads (with player counts beside every rate).

## 1. What top games in our genre sell (SEEN, 2026-11-24)
| Game | What is sold | Shape |
|---|---|---|
| My Pet Salon | Starter Pack (one time, limited), a limited seasonal pack, a 30 minute 2x cash boost at a low entry price, deals tab "Picked for you" | Big HUD button for the pack at all times; shop opens on Deals with the biggest card first |
| Barber Simulator | Starter Pack with a visible 48 hour clock, "best deal" ribbon, pet roulette with odds, plus 1 pet slot, infinite pets | Pop up with three picture tiles joined by plus signs, one buy button |
| Clean Everything | Timed helper cards (minutes to forever, five tiers from very cheap to expensive), watch an ad for minutes, carry limit upsell | Row of five equal cards, one start button |
| Pet Store Tycoon | Grand Opening bundle after day 2 (pet pack, cash, 1 hour 2x, struck through price, 50 percent off), Robux shop with Featured, Staff, Boosts, Pet Packs, Cash tabs, gift button beside every price | Day 2 pop up, tabbed shop, helpers sold with "Hired 0 of 5" |
| Restaurant Tycoon 3 (wiki, CLAIM, May 2025) | Passes: sandbox mode, precision build, build collisions, auto money collection, 3x customer luck, 2x item limits; cash and diamond packs | Passes listed first, products second; biggest cash pack gives least cash per Robux |
| Steal a Horse | Trails shop opened by the tutorial with a "Buy to train faster, close X to skip" prompt | Forced buy prompt in minute one |
| Our starter reference (Derek's find) | Starter Pack with three picture tiles, struck through price, 72 percent off tag, countdown | One pop up, one price button |

Pattern: every game puts a one time starter bundle in the first minutes, with 2 to 4 item tiles and one big price button, a struck through regular price and a percent off. Cheap entry items sit around the price of a coffee-sized Robux amount; helper or boost time cards are the reflex buy; the permanent passes are the "considered" buy.

## 2. Roblox's own rules that shape every card (OFFICIAL)
- Discounts must be genuine and fair: an always on "sale" at the same price is not, and a sale that is very short to create pressure is not.
- No countdown that is inaccurate or restarts by itself. No "almost gone" claims unless true.
- Young audience: promotions suitable for all ages, no urgent wording. Roblox's swaps: View Item, See Price, Open Shop.
- Random items bought with Robux: every outcome and its odds, as percentages adding to 100, before the purchase, with a word and not a lone (i); keys and tickets count; PolicyService per player with another path for restricted players.
- A shop should be integrated, contextual (say why the item matters) and inviting. Describe items accurately. A starter pack is an initial offer within the first few minutes.
- Roblox's own Shop (2026): a personalized storefront built from our passes and products, off by default for the global button; no manual card order yet.
- Listed products can appear on Roblox surfaces and need their own 512 by 512 icon.

## 3. Prices (CLAIM and SEEN; Roblox gives none)
- CLAIM (a 2026 blog, commercial): reflex buys 25 to 75, considered 100 to 250, commitment 400 to 1,000 and up. CLAIM (2021 forum): entry 50 to 400, gameplay 400 to 6,000.
- CLAIM (2019 forum): starter packs often priced near 200, shown 10 to 20 minutes in, earnable stuff only, a discount under about 30 percent of content value. Warns that a buy prompt on join is an instant turn off.
- SEEN: starter packs around the 49 to 199 range; helper time cards from about 5 up; 2x boost for 30 minutes at about 19.
- Our current ladder (monetization-calls-2026-11-26.md and Derek's answers) already sits inside this: skips 15 to 99, crates 49 and a pack of 5, passes 99 to 299, starter pack 199 with a true 63 percent saving. JUDGMENT: no price change needed from this research; keep what we have until our own sales reads.

## 4. Where prompts appear (JUDGMENT, from SEEN and the 2019 to 2021 posts)
Good: after a need is felt or a win lands. Ours: the starter button from about 2:45 of play (not on join); a skip offer only when a long build wait is on screen; the crate after a crate is earned; the like ask at a good moment. Bad, seen: a forced buy prompt in the tutorial (Steal a Horse), a pop up on join, stacked pop ups, "Limited, 82 left" counters, ribbons on every card.

## 5. Concrete recommendations for Clean a Cat
1. **Shop at most three tabs**: Boosts and Passes, Crates, New player offer (only while it lasts). Skips stay on the build panel. One card shows at a time per row, three to four cards visible on a phone, one price button per card.
2. **Starter offer first and one picture-tile card**: three item tiles joined by plus signs (matches what players already know from every rival), a "New player offer" chip, the real regular price struck through with the true 63 percent saving, and no clock, as Derek chose. Contents shown with icons before the price.
3. **One reflex-priced entry item on the first screen**: a small cheap card (a boost or a crate single) so the first buy is easy. We already have cheap items; the gap is making one visible without scrolling.
4. **Pass cards state the benefit in numbers** ("2x coins from every cat"), show an Owned state, and each has its own icon through the image gate. Never write free next to a paid item.
5. **Crate card: Chances button in words before the buy button**, percentages adding to 100, hidden for PolicyService restricted players. (Checked in the crate monetization notes; Review-QA re-checks on the live ids.)
6. **Sale display**: strike through only for a real sale with a planned end (launchSale has none yet; Derek said it ends only when he says, so Review-QA is asking him for a date). No ribbons stacked, no stock counters, no restarting timers.
7. **Button words**: View Item, See Price, Open Shop, Collect. Never BUY NOW or LAST CHANCE.
8. **Gift button** only beside the price, off the first card, same purchase flow.
9. **Don't add yet**: a "Featured" tab with nothing real in it, 3x luck style boosts (random odds rules), an auto collect pass if it takes away the scrub that is the fun, a second pop up besides the starter offer.
10. **Measure from day one** with the events already in code: pack_offer_shown, pack_bought, shop_opened (from button or pack_button), purchase_step (prompt, cancelled, granted), skip_offer_seen, skip_bought, crate_opened. Judge buy rate per shop open and per starter pop up, with the player count beside every rate; under a few hundred it is a direction only.

## 6. Hand off
- Design-Agent: the layout parts (items 1, 2, 4, 5, 7, 8) for issue 1030 and the starter pack card. The no-price version is `docs/growth/shop-layout-research.md`; this file is the price-aware one for the design thread only.
- Review-QA: items 5 and 6 go in the policy check before any live flip of crateShop, launchSale and starterPack.
- Derek: needs to pick only the launchSale end date (already raised) and whether to turn on Roblox's own global Shop button (my pick: not at launch).

## Source gaps
- Roblox gives no price points, no card order and no conversion benchmarks. The creation.dev pricing page could not be read. The 2019 and 2021 forum posts are old. The Restaurant Tycoon 3 wiki is a single game and dated May 2025. The 2026 pricing blog is commercial. Treat every number from them as a claim.
- I could not open top simulator games live (Pet Simulator and similar); if Derek wants those compared, he can send screenshots like the ones in Coordinator/references/ and I will add them.
