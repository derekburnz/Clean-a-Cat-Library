---
name: derek-money-answers
description: Derek's monetization answers of 2026-11-25 ET - crates sold for Robux, paid skips on any build, five passes incl. Lou the paid helper, second pet slot pass for player and workers, starter pack with a 72 hour countdown
metadata:
  type: project
---

Sources: the plan page database and the project chat, 2026-11-25 ET. Full wording: Planning-Agent/playtest-notes.md. Growth-Agent's checks against Roblox's pages: Growth-Agent/crate-monetization-check, paid-skips-check, shop-weight-and-helper and starter-pack-check files of 2026-11-25. Gameplay answers: [[derek-plan-answers]].

- Prices: all are Growth-Agent's judgment (Roblox gives no guide). Derek on `passes` (pick 0): "do whatever prices for mono for now can tweak later". So prices are ours to set and tune; do not ask him again.
- Crates (`q2-crates` note): "Can also be sold for robux or earned rarely. We can remove the unlucky run one". A Robux crate is a paid random item, so CLAUDE.md rule 9 and the monetization-policy skill apply in full: chances as percentages before purchase, PolicyService check per player, hidden from restricted players. Ours: earned and bought crates are the same crate; coins never buy crates; no Robux product ever gives coins. Price (`crateprice` pick 0): 49 Robux, five for 199, no daily limit.
- Paid skips (`skips` pick 1): "paid skips absolutely need good monotization". `skipprice` pick 1 with "Always can pay for skips for any build": a skip is offered on EVERY build, the first long build and short ones included. Tiers by time left: 5 Robux under 2 minutes, 15 up to 1 hour, then 35, 75, 99. Small button on the builder panel, hidden under 15 seconds left, no pop up.
- Passes (`passes` pick 0): 2x Coins 199, Second Builder 299, Lou the extra helper 249 (`helperpass` pick 0: Jo and Sam for coins, Lou paid, comes with his station, same output), second pet slot 249, Golden Sponge 99.
- Second pet slot (`petpass` pick 1): ONE pass opens a second slot for the player AND every worker (249 Robux). Not our pick; his.
- Starter pack (settled): in the style of a picture he sent (three priced cards, struck through total, bobbing sparkling HUD button). Golden Sponge + second pet slot + 2x Coins, 547 for 199 since 2026-11-26 (was 299; Derek's pick, see [[derek-nov26-answers]]), label "Bundle, save 63%" (computed from live prices; PRICE CHANGED by Derek 2026-11-26 9:50 AM ET, q2-packvalue: 547 for 199, a true 63% saving, he sets the price on Roblox), shown only to players who own none of the three, no crate and no coins in it. "countdown but make it end" and "72h from start I don't care about rest you decide", confirmed 3:58 PM ("starter pack stays for 72h is what i meant"): a real 72 hour clock from first join, kept on the server, never restarts, gone for good at zero. Ours: small button from the end of the tutorial, no window opening by itself.
- Leaving cats: never sell a way to keep or bring back a cat, and never show a price when a cat is about to leave (Growth-Agent's rule, ours).
- He called pets sold only for Robux "kinda scummy" (2026-11-24), so every pet stays earnable without paying.

**How to apply:** these are decided; build behind switches that start off. Anything sold must pass the monetization-policy skill and Roblox's paid random items rules, whatever the pick says.

- 2026-11-26 ET (plan page, q2-wheremake): Derek makes the dev set of passes and products now and the live set when he promotes; Passes.luau and Products.luau key ids per game.GameId. q2-helperxp: no helper XP. q2-notifykey: reuse the group key saved by Derek as experience secret CleanACat_NotifyKey; Gameplay-Engineer checks it can send notifications.
