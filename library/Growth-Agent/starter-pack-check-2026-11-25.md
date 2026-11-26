# Starter pack check for Clean a Cat (2026-11-25 ET, Growth-Agent)

For Planning-Agent's question `starterpack`. Pack as written: one Spa Starter Pack with fixed visible contents (a look for the tub, a bandana for Suds, one hour of double tips), plain price, no countdown, no stock counter, no crossed out price, shown once, no crate, no coins. Labels: OFFICIAL = Roblox page read 2026-11-25; JUDGMENT = my call, no data.

## Short answer
The pack as written follows Roblox's rules and our monetization-policy skill. Suggested price 99 Robux (judgment). Do not show it at minute 10 of the first session; show it once at the start of the player's next visit. A timed double tips boost is fine as a developer product if the timer is honest.

## 1. Price
- OFFICIAL: Roblox gives no recommended starter pack price, tiers or benchmarks. Developer products can be 1 Robux and up. The Roblox page on starter packs we tried to read does not exist (the link returned the design index).
- Reference we have: Pet Store Tycoon sells 3 random pets, 10,000 cash and an hour of 2x coins for 99 Robux (198 crossed out). Source: Derek's screenshots, 2026-11-24.
- JUDGMENT: 99 Robux. It matches the one price point we have seen for a similar pack, and our pack has no random part and no coins, so it should not be priced higher. A cheaper 49 Robux version is the fall back if the first reads show few buyers. Judge only after several hundred players have seen it (ab-tests.md). Roblox price optimization needs about 60,000 transactions in 30 days, so it is not an option for a long while.
- Show the plain price. No crossed out price: Roblox's test is that a discount must be real and not "always on sale" for the same amount, and a plain price avoids the question.

## 2. When to show it
- OFFICIAL: no rule on when or how often a game may show a purchase prompt.
- Our own rule (gdd-draft.md): no pop-up, shop prompt or like request in the first session, and tutorial steps are tapped by the player. A pop-up at minute 10 of session one breaks that rule and risks the first-minute quit numbers Home reads.
- JUDGMENT: show the pop-up once at the start of the next visit (day 2 or the next time the player joins after a gap), after the player has seen the finished build or the tips jar. Pet Store Tycoon shows its pop-up after in-game day 2, which is close to the same idea. A no is final for that visit, then the pack sits in the shop tab with a plain "View" button. Never show it in the middle of a cat or while a build timer is being chosen.
- Keep a switch for it, off by default, and log the minute it goes on.

## 3. A timed double tips boost as a developer product
- OFFICIAL: Roblox's passes page sends potions, temporary power-ups and currency to developer products (a product can be bought more than once). A passes page rule: something the player "keeps and uses up" is a developer product.
- OFFICIAL, presentation: no timer that is inaccurate or restarts for the same item, no false "limited time", no pressure language for minors (their examples: "View Item", "See Price", "Open Shop" instead of "GET IT NOW").
- Nothing in the boost is random, so the paid random item rules do not apply to it. They would apply if any part of the pack were random: Roblox says a bundle with one random item makes the whole bundle a paid random item.
- JUDGMENT for the build: the pack is one developer product with a server side one time flag (the cosmetics are kept forever, the boost is the used up part). The server owns the boost end time. Say in the pop-up exactly what it gives ("1 hour of double tips"). Decide what a second boost does (adds time) before building. Grant and save before the purchase is marked granted. Check the pass or product ownership on the server, never on the client.

## 4. Does a one time pop-up fit the rules and our skill
- OFFICIAL: no frequency limit, so one pop-up is fine. Roblox says players must not be misled, confused or pressured into a purchase.
- monetization-policy skill: no fake countdown, no "only 2 left", no stock counter, no nagging after a decline, a decline is respected for the session, prices shown in Robux before the confirm, copy says exactly what the item gives, no coins sold. The pack as written matches every line. Also keep: PolicyService is fetched per player, and for players the policy restricts, hide it.
- Watch: the pop-up needs a close button that is easy to hit on a phone and a tap target away from the buy button.

## Also on the plan page (quick notes, JUDGMENT)
- `checkin`, a seven day card counted by days played with no streak: fits our rules. No countdown to "claim before it resets", and missing a day must lose nothing. Rewards must be things the player can see before opening.
- `quests`, a weekly list that gives a crate: fine if the crate is earned only and the odds are shown on the board, as in the design. If a crate can ever be bought with Robux or with a currency Robux can buy, the paid random item rules apply in full.

## Sources
Roblox Creator Docs, read 2026-11-25: monetization foundations (Presenting products), developer products, passes, paid random items, price optimization; Roblox Community Standards (Roblox Economy). No page shows an update date. Derek's Pet Store Tycoon screenshots 10, 11 and 13 in Coordinator/references/pet-store-tycoon-2026-11-24/.

## Update 2026-11-25 (later): starter pack from Derek's picture (three cards, struck through total, countdown, bobbing button)
OFFICIAL = Roblox pages read 2026-11-25, JUDGMENT = my call. This replaces the contents of the first pack above; sections 1 to 4 above still hold for the pop-up rules.
Planning's pick: Golden Sponge 99 + second pet slot 149 + 2x Coins 199 = 447, pack price 249, saving 198 = 44% (correct maths).

- **Contents and price: correct.** The three cards are real items with real prices, so the struck through total is true, and nothing in it is random or coins. Restricted players can still see it.
- **Fix needed: players who already own one of the three.** The pack has one fixed price, so for them the "44% saving" is false. JUDGMENT: show the pack only to a player who owns none of the three. Once they buy any single item the pack goes away for them. On the server the pack is one developer product that grants all three rights; ownership checks must accept either route (pack or single pass), and the pack's purchase saves before it returns granted.
- **Call it a bundle, not a sale.** OFFICIAL: a discount is not genuine if an item is "always on sale". A standing bundle price below the sum of real prices is fine, but keep the item prices unchanged while it is shown, and update the total if any price moves. Label "Bundle, save 44%" rather than "SALE".
- **Struck through total:** OFFICIAL: no rule against it beyond the "always on sale" test. Keep.
- **Countdown:** OFFICIAL: not banned if accurate and it never restarts; but Roblox says a deal offered only for a very short time to pressure buyers is not a fair discount, and promotions should suit all audiences by default. Our monetization-policy skill and the project rule are stricter: no countdown pressure for a young audience. Recommendation stays: no countdown. If Derek overrides, the limit must be real: a fixed time from the player's first view, never restarting, and the pack really gone for that player afterwards (the single items stay for sale). Showing the same bundle again later after a "limited time" is a false claim.
- **Bobbing and sparkling button:** the Roblox pages I read say nothing about animating a purchase button, and I found no rule. JUDGMENT for kids: allowed, but keep it gentle: a soft bob for a few seconds when the button first appears, then still; stop it for good after the player has opened the window once or after three visits. A button that keeps sparkling is nagging, which our skill rules out. Tap target on a phone must not sit under the thumb used for the main game action.
- **Window opens by itself once:** conflicts with the project rule that no menu opens by itself (written for tutorial and first session). It is a later visit, so it is not breaking that rule as written, but to stay safe use the button only, or a small note that says "Starter Bundle" on the button and nothing opens. Derek liked Pet Store Tycoon's pop-up, so this is his call. My pick: the button, with the window opening only when the player taps it. If the window opens by itself, once, on the second visit, with an easy close button and no return after a no.
- **Golden Sponge as the lead card:** fine. I withdraw the lean to hold it, since it is felt in the first wash and the pack makes it a good starter. The shop count from shop-weight-and-helper-2026-11-25.md still holds, with Golden Sponge now sold singly and in the bundle.

## Update 2026-11-25 (later): Derek chose a countdown that ends ("countdown but make it end")
Planning's pick: 72 hours of real time from the first time the pack button shows. My check: 72 hours is fine. OFFICIAL: Roblox's complaint is a deal offered "only for a very short time to pressure buyers"; 72 hours is not very short and covers a day 2 and day 3 return and time to ask a parent. Sales sense (JUDGMENT, no data): a longer window loses urgency, a shorter one pushes the young; 72 hours is a fair middle. Read buyers by hour after the clock starts and tell Derek if almost all buys happen in the last hour (that would suggest pressure). Keep 72 hours unless a read says otherwise.

Countdown rules (OFFICIAL: the clock must be accurate and must not restart for the same item; JUDGMENT for the build):
1. **Accurate clock.** The shown time left equals the server's end time. Show it only on the button and in the window, updated at least once a minute, with days and hours while over an hour.
2. **Server owned end time, per player.** Started the first time the pack button shows for that player, saved with the player's data. A rejoin, a server hop or a client clock change cannot change it.
3. **Never restarts and never extends.** No "last chance" reset, no second window, no event re-run of the same bundle for that player.
4. **Gone for good at zero.** The button and window disappear for that player. The three items stay in the shop at their own prices. A different bundle in a later event is fine; the same bundle again is not (it would make "limited time" false).
5. **A purchase in progress at zero.** If the player opened the Roblox confirm before zero, honour the receipt after zero and grant the pack. Never charge for nothing.
6. **Own one of the three: no pack, no clock** (see the fix above). A player who buys a single item during the window loses the pack and the clock stops showing.
7. **No pressure around it.** No notification, banner or pop-up about the clock running down, no "last hour" nag, no sounds. Wording: "Bundle, ends in 2d 5h", not "HURRY".
8. **Log:** `pack_offer_shown` (clock start), `pack_bought` (hours since start), `pack_expired`.

Line for the monetization calls table:
| Idea | Type | Policy | Verdict |
|---|---|---|---|
| Starter Bundle: Golden Sponge + second pet slot + 2x Coins, 249 Robux (parts 447, save 44%) | developer product, fixed contents, not random | real item prices, accurate server owned 72 hour clock per player, never restarts, gone for good at zero, hidden if the player owns any part, no coins or crates in it | yes, behind a switch, shown once per player |

## Update 2026-11-25 (latest): the 72 hour clock starts at the player's first join (Derek, 3:28 PM ET)
Planning's pick: a small HUD button from the end of the tutorial in session one, true time left on it, no window that opens by itself. Second option: from the second visit with whatever time is left.
- **Roblox pages:** no rule on when a purchase button may appear or how often; the pressure and accuracy rules above apply. A small button that the player taps is not a prompt.
- **Our rules:** gdd-draft.md says no pop-up, shop prompt or like request in the first 5 minutes. A tappable button after the tutorial ends, opened only by the player, keeps that rule if it appears after the tutorial's last tapped step. Project rule 6 (no menu opens by itself) holds because nothing opens on its own.
- **Young audience (JUDGMENT):** a visible clock in the first session is the strongest pressure signal in the game, so keep it small: the HUD button says "Bundle" with the time left in small text, with the gentle bob only for a few seconds. No sound, no sparkle loop, no banner.
- **My pick: agree with Planning's pick** (button after the tutorial). Reason: the clock already runs from first join, so holding the button to the second visit costs a day of the 72 hours and a player who returns after three days never sees it. Ship it behind a switch and read first-minute quits and 1 to 3 minute quits before and after; if early quits rise, move the button to the second visit.
- **Clock details:**
  1. The clock starts at the player's first join, real time, saved on the server. It is only accurate to show once the button shows, so show the true time left (for example 71h 52m) from the first appearance.
  2. Players who first joined before this feature ships: their first join is long gone, so start their clock the first time they join after the feature ships, and do it once.
  3. The rest of the countdown rules above hold: never restarts, gone for good at zero, the three items stay in the shop at their own prices, no pressure notifications.

## Update 2026-11-25 (latest): price change after the second slot became one pass for everyone
Cards: Golden Sponge 99, second pet slot 249, 2x Coins 199 = 547. Bundle price 299 (saving 248 = 45%). Everything else above holds: 72 hours from first join, small button after the tutorial, no auto-open window, hidden once the player owns any part, gone for good at zero. A first session button is within Roblox's pages (no rule on button timing) and our young audience rules if it is small, tap only and gentle; I keep my pick (button after the tutorial) and I would move it to the second visit only if first minute quits rise (see the switch and read above). Derek left the rest to us, so no more asks to him on the pack.

## Update 2026-11-26: Derek set the bundle price to 199 Robux
Parts stay 547 (Golden Sponge 99, second pet slot 249, 2x Coins 199); saving 348 Robux = 63.6%, shown as 63% (round down, computed from live prices). My check finds no policy problem: the comparison is true, nothing is random, and the price is not below any rule. Two notes (JUDGMENT): (1) 199 equals the price of 2x Coins alone, so the bundle is a very strong offer and will take buyers from the singles during the 72 hours; read single sales before and after and tell Derek if single slot sales fall sharply. (2) Players who already own one part still do not see it, so a player who bought 2x Coins at 199 sees no bundle; that is correct and consistent with the rule, but expect a few to ask why. Everything else above holds.
