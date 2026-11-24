# Loops that hold players beyond the first five minutes (read 2026-11-24)

Tags: [official] = Roblox docs or talks; [tracker] = player-count site or Roblox search API reading; [opinion] = guide, blog, news or creator write-up. Every page was read through a summarizing fetch tool, so wording is a paraphrase. Roblox search API readings are live snapshots taken 2026-11-24 and were noisy (the same game gave different counts across calls). No Roblox game page, RDC video or YouTube transcript was read. Mechanics only are discussed; no names, characters or art are to be copied.

Games covered: Grow a Garden, Steal a Brainrot, Steal An Egg, Throw Food For Animals, 99 Nights in the Forest, Escape Tsunami For Brainrots, Dig & Clean (counter-example), Garden Horizons (counter-example). Fewer than the 6 to 8 "long holders" asked for have solid numbers; see Gaps.

## 1. The loop at three scales

### Takeaway
The long-holding games share one pattern: a 30-second verb that always pays something, a session goal that is a visible next purchase, and a weekly layer that is content or events, not the verb. Hard numbers for income per second or session length were not found for any game; mostly the multipliers and price steps are public.

### Cited findings
- 30 seconds, Grow a Garden: plant seed, wait, harvest with E, sell to the NPC, buy better seed. Crop value = base value x (weight / base weight)^2 x mutation multiplier. Weather mutations run 2x (Wet, Moonlit) up to 100x (Shocked) and 240x (Cosmic); variants are Silver 5x, Gold 20x, Rainbow 50x. [opinion] [allthings.how, updated 2025-09-29](https://allthings.how/grow-a-garden-mutations-all-types-how-to-get-them-stacking/), [Pocket Tactics, updated 2025-12-04](https://www.pockettactics.com/grow-a-garden-mutations). Shop restocks every 5 minutes on a global clock. [opinion] [gag.gg, 2026-06-22](https://gag.gg/guides/seed-restock-and-values) (from the earlier note).
- 30 seconds, Escape Tsunami For Brainrots: run a wave-dodging course, grab brainrots that produce cash, buy +1/+5/+10 Speed (each step costs more), rebirth at a Speed target. 20 rebirth levels; each needs 10 more Speed (40 up to 230) and adds +0.5x money multiplier (1.5x to 11x); brainrots and mutations are kept, Speed resets. A 89 Robux option skips the Speed reset. [opinion] [allthings.how, updated 2026-01-12](https://allthings.how/how-rebirth-works-in-escape-tsunami-for-brainrots-all-20-levels/).
- 30 seconds, Dig & Clean (a cleaning game): detector finds a spot, tap-dig, spray-clean at a workstation, then display in a museum or sell; museum displays draw tourists who pay income. Six rarity tiers. [opinion] [allthings.how, updated 2026-08-06](https://allthings.how/how-to-play-dig-clean-on-roblox-beginner-s-guide/). No prices or dig times given.
- 30 seconds, Storage Hunters (not on the original list but a care-free "bid, haul, sell" loop): bid on lockers, haul loot to a vehicle, drive to shop, sell. [opinion] [allthings.how, updated 2026-09-04](https://allthings.how/why-storage-hunters-open-world-lost-half-its-roblox-players/).
- Session scale, Steal An Egg: steal an egg, carry it home, hatch a pet that pays per second; nests reset every 5 minutes; biomes unlock by Speed (Lake 900, Desert 10K, Jungle 40K, Snow 170K). [opinion] [bloxodes, 2026-08](https://bloxodes.com/articles/steal-an-egg-beginners-guide) (from earlier notes). Offline: placed eggs earn while away (one guide shows "$16M/Day offline"). [opinion] [allthings.how, 2026-08-27](https://allthings.how/steal-an-egg-how-to-make-eggs-grow-faster-in-roblox/).
- Session scale, Steal a Brainrot: cash storage cap raised $1M to $10M in Update 9 to make room for Mythic and God tiers; Update 26 (late 2025) rebuilt Rebirth with new costs. [opinion] [rblxguide, page dated 2026-04-25](https://rblxguide.com/games/steal-a-brainrot/updates/steal-a-brainrot-update-history-hub-2026).
- Week scale: Steal a Brainrot ran a strict Saturday update (Updates 33 to 64, Jan 10 to Aug 29, 2026); Steal An Egg ran 4 Saturday updates in a row from Aug 22 to Sep 12, 2026. See section 3.
- Roblox says D1 retention is driven by the core loop, first-time experience and performance; D7 by the progression system (short and long goals, content variety, pacing); D30 by an "ending system" for what players do after main goals. [official] [Roblox Creator Docs, retention](https://create.roblox.com/docs/production/analytics/retention), read 2026-11-24.

### Inferences (mine)
- The price steps found in earlier notes (about 5x to 27x per tier) plus Garden's squared weight rule and stacking multipliers mean the number the player sees keeps growing faster than their effort. That is the "weekly" feeling inside a 30-second action.
- A clear 30-second verb plus a visible next price is common to all; none of the sources shows a long-holding game whose verb is purely "scrub, get paid a flat amount".

### Gaps
- Income per second, time between purchases and typical session length were not found for any game. Roblox does not publish genre retention benchmarks.

## 2. Hours 1 to 10: what carries the player

### Takeaway
Across the games read, rarity or mutation multipliers, a collection index, rebirth (or an equivalent reset), and offline or passive income show up in almost all. Trading appears as a later add-on. Leaderboards were found in one game. Treat the frequency as read from guides, not from player data.

### Cited findings
- Mutation or rarity multipliers: Garden (up to 240x, 100+ named mutations) [opinion, Pocket Tactics above]; Brainrot (Gold/Lava/Radioactive early; Cyber 11x; Cursed trade-off 0.5x income, doubles event spawns) [opinion, rblxguide above]; Escape Tsunami (brainrot mutations kept through rebirth) [opinion, allthings.how above]; Dig & Clean (rarity tiers, later Omega, Anomaly, Paradox, PRISTINE condition) [opinion] [Earnaldo update log, read 2026-11-24](https://earnaldo.com/blog/dig-and-clean-update-log).
- Rebirth or reset: Brainrot (rebirth to at least 19 by Aug 15, 2026) [opinion] [eldorado.gg update log](https://www.eldorado.gg/blog/steal-a-brainrot-en/steal-a-brainrot-update-log/); Escape Tsunami (20 levels, table above). Garden: no prestige system on the mutation guide page; not confirmed either way.
- Index or collection: Throw Food For Animals Index pays a cash bonus per completed biome collection [opinion] [Of Zen and Computing, 2026-11-12](https://www.ofzenandcomputing.com/throw-food-for-animals-beginner-guide/) (earlier note); Brainrot Index improvements shipped Jun 13, 2026; Steal An Egg has an Index button (earlier note).
- Offline earning: Throw Food animals earn while offline [opinion, Bloxodes 2026-11-01, earlier note]; Steal An Egg shows daily offline earnings; Garden showed a "Grows Offline" icon in 2025 (earlier note). Dig & Clean added offline earnings only in Update 2 (Aug 16, 2026).
- Trading: Brainrot added a Trade Machine (Feb 21, 2026), then permanent trading and Trade Plaza (Jun 13 and 20) [opinion, eldorado.gg above].
- Base upgrades: Throw Food base size (+2 animal spaces per purchase); Steal An Egg "Bigger Base" upgrade (Sep 12, 2026); Brainrot extra base slot (Aug 15, 2026).
- Events and leaderboards: Brainrot Admin Abuse and weather events; Dig & Clean added two leaderboards (Aug 16, 2026).
- Roblox advice for D30: an ending system, small updates every 2 to 4 weeks, big feature updates every 2 to 3 months, plus trading, guilds, PvP, leaderboards. [official] (Creator Docs link above).

### Inferences (mine)
- Almost every long-holding game has four layers at once: multiplier tiers, a reset or a prestige, a collection index, and passive income. Trading and leaderboards are real but later.
- Garden's own lesson (see section 4) is that layers piling up without space to place them became a complaint, so each layer needs its own room in the world.

### Gaps
- No source ranks these goals by how many players reach them. Roblox analytics for the progression funnel are private to developers.

## 3. Update cadence and events

### Takeaway
The biggest games ship weekly on a fixed day and weekday time. Each drop adds a theme plus new things to collect, usually 3 to 15 items and one new machine, trait or mutation. Slower cadences (two-weekly) exist and were enough for 99 Nights.

### Cited findings
- Steal a Brainrot: Saturday updates, 32 in a row (33 to 64) from 2026-01-10 to 2026-08-29. Typical drop: new brainrots (2 to 13), a machine or mutation (Duels Machine, Trade Machine, Cyber 11x, Crystal 13x), a themed limited event (Valentine's, Easter, Backrooms, Futbol). Update 68 on 2026-09-26 added 11 brainrots and an event. [opinion] [eldorado.gg](https://www.eldorado.gg/blog/steal-a-brainrot-en/steal-a-brainrot-update-log/), read 2026-11-24.
- Steal An Egg: Aug 22 (Cherry Blossom), Aug 29 (Monsters, 8 pets), Sep 5 (Rift event, 15 animals, banners), Sep 12 (Angels vs Demons, 16 pets, permanent biome, Bigger Base). Weekly, Saturdays 15:00 UTC. [opinion] [Earnaldo, read 2026-11-24](https://earnaldo.com/blog/steal-an-egg-update-log). Updates after Sep 12 not found.
- 99 Nights in the Forest: every two weeks on Saturdays since June 2026 (Jun 27 Alien's Revenge, Jul 25 Bee biome, Aug 8 Kids Have Jobs, Aug 22 Biome Refresher, Sep 5 New Classes with daily quests). [opinion] [Earnaldo](https://earnaldo.com/blog/99-nights-in-the-forest-update-log).
- Dig & Clean: Aug 10, 16, 23 and one scheduled Aug 30, 2026, each adding an island, a rarity and 4 to 7 items. [opinion] [Earnaldo](https://earnaldo.com/blog/dig-and-clean-update-log). Later updates not found.
- Grow a Garden: weekly Saturday events through 2025, then the developer said in Aug 2025 that weekly events would be replaced by a feature-driven approach. [opinion] [Roonby, 2025-08-11](https://roonby.com/2025/08/11/grow-a-garden-might-not-be-getting-weekly-updates-anymore/). Players complained in July 2025 of updates "rushed and not very inspired" and the studio created two event teams [opinion] [PC Gamer, 2025-07-09](https://www.pcgamer.com/games/survival-crafting/robloxs-hot-gardening-game-gets-a-crack-squad-dedicated-to-new-events-after-players-kicked-up-over-old-ones-being-rushed-and-not-very-inspired) (earlier note).

### Inferences (mine)
- Weekly cadence plus new "things to chase" each time is the shared factor of the games still near the top. Roblox's own advice (small updates every 2 to 4 weeks) is slower than what the biggest games do.
- Cadence alone did not save Dig & Clean (section 4), so cadence is necessary but not enough.

### Gaps
- Update logs after mid-September 2026 were not found for Egg or Brainrot. Throw Food For Animals update log not found.

## 4. Counter-examples

### Takeaway
Six games from 2025 to 2026 lost most players quickly. Reasons named by sources: one mechanic and clone fatigue, trend expiry, dev departures or slow updates, exploits, monetization, and lag. A cleaning game, Dig & Clean, is the closest and shows a 99.9% fall in about three months despite weekly updates.

### Cited findings
- Dig & Clean (cleaning/dig): peak 270K CCU on 2026-08-16; 235 now; 30-day change -81.5%. [tracker] [RoWatcher, read 2026-11-24](https://rowatcher.com/games/10475794799/dig-clean/dying) (page undated; "99 days ago" implies the read date). Fell about 99.9% in roughly 100 days. Peak coincided with Update 2, which added offline earnings, levels and leaderboards; Update 3 added daily quests. No source gave reasons. The beginner guide (Aug 6, 2026) mentioned neither rebirth nor index. [opinion]
- Garden Horizons: launched 2026-02-22; first update topped 1 million concurrent, about 23,000 in early March 2026. Named reasons: developers left, exploit duplicated seeds and damaged the economy, admin fired, weak second event, lag with 300 plants, late console support, and game passes added in week 1 to 2. [opinion] [allthings.how, updated 2026-03-18](https://allthings.how/garden-horizons-player-count-drop-what-happened-and-is-the-game-dead/) (no tracker named).
- Grow a Garden itself: all-time peak 21.1 million (June 2025) [opinion, Sportskeeda, undated]; Roblox search API shows 17,040 players on 2026-11-24 (original) and 2,223 (Grow a Garden 2) [tracker]. A Sportskeeda page claiming 700,000+ is undated and contradicts this; treated as outdated. Reasons per Roonby (2026-01-13): crowded gardens and lag, pets overshadowing gardening, complexity for new players, team departures (unconfirmed), aggressive monetization. [opinion](https://roonby.com/2026/01/13/grow-a-garden-is-losing-players-is-it-finally-dead/)
- Steal a Brainrot: peaks 5M (Jul 2025), 20M (Aug 2025), 25.8M (Oct 2025), 12.8M (Jan 2026); 215,000 in the RoWatcher article (date not stated), "99.2% decline" [tracker/opinion] [RoWatcher](https://rowatcher.com/news/is-the-brainrot-trend-dying-what-ccu-data-from-three-top-games-reveals). Roblox search API on 2026-11-24 shows 90,630. Still kept a base after 17 months with weekly updates.
- Storage Hunters: peak about 50,000; about 16,600 in Sep 2026. Reason: thinner update communication, unannounced timed events reaching only online players. [opinion] [allthings.how, 2026-09-04](https://allthings.how/why-storage-hunters-open-world-lost-half-its-roblox-players/)
- Other "big then flop" list: The Forge (over 1M to a few thousand; grindy random drops, exploits, private servers cost Robux), Sailor Piece (RNG, bots), Slime RNG (drop within a month; luck-only, little progression), Escape Tsunami and Plants vs Brainrots (trend), Bizarre Lineage (pay walls, long maintenance). [opinion] [Roonby, 2026-07-10](https://roonby.com/2026/07/10/9-roblox-games-that-are-big-and-flop-downfalls-of-the-most-popular-games/). Numbers mostly absent.
- Cleaning clones: the Roblox search API on 2026-11-24 listed 40 "Clean/Wash" titles. Clean The Ballpit! 26,076 players, Clean The Bugs 9,218, Clean Everything 8,658, Clean all the Leaves 3,295; Clean the Kitchen! 347 (RoWatcher peak about 2K on 2026-08-29, 9% of peak). [tracker] Many have under 100.
- Throw Food For Animals reads 159,572 and Steal An Egg 554,565 to 1.24M in separate API calls on 2026-11-24 (noisy). [tracker]
- Escape Tsunami: peak nearly 5M, about 164,000 (date not stated). [opinion/tracker, RoWatcher link above]

### Inferences (mine)
- Most likely drivers, ranked by how many sources point at them: (1) thin or copied loop where updates add more of the same; (2) team or update-quality problems; (3) trend expiry and clone flood; (4) monetization added early; (5) technical load (lag at scale). A care or cleaning game launching into a clone wave should expect the same trend decay unless it has its own depth.
- Dig & Clean having offline earnings, quests and leaderboards by day 14 and still collapsing suggests the retention layers listed in section 2 are not enough alone; the reason is not documented, so this is a hypothesis.

### Gaps
- No tracker gave per-day history for most; Dig & Clean reasons not found; no pet-care game (Adopt Me style) counter-example with numbers found. Adopt Me lost 122K players in one day on 2026-03-31 (519K to 397K), cause unconfirmed [tracker] [RoWatcher](https://rowatcher.com/news/why-roblox-s-adopt-me-lost-122k-players-in-24-hours), but that article's date metadata conflicts.

## 5. Implications for a hands-on washing game

### Takeaway
The hands-on washing act is the 30-second verb. What it lacks on its own is a multiplier layer and a reason to leave and come back. Three structural features would carry players past cat number 20.

### Inferences (mine; from the findings above)
1. A rarity and condition layer on the cat, not just the number of cats. Cats arrive with coat types, dirt types and rare "conditions" (like mutations) that raise payout and appear on weather or events. Basis: multiplier stacks in Garden, Brainrot, Dig & Clean's PRISTINE; the loop is stackable and the washing stays the verb.
2. A collection index plus a place to keep the cats (a spa with rooms, upgraded) that earns while the player is away. Basis: Throw Food and Steal An Egg offline pay, Index bonuses, base upgrades. Keep it care-flavoured: cats rest and the spa pays, no loss for being away.
3. A prestige tier that resets the tools and keeps the collection and a permanent multiplier, with a weekly themed event on a fixed day. Basis: Escape Tsunami rebirth table, Brainrot 32 weekly drops, Roblox advice on an ending system. Limit the number of layers at launch to those that can be explained in under 10 minutes; Garden players complained about complexity.
- Trading is probably not right for a young audience; the reasons are policy and safety, not retention, and were not researched here.

### Gaps
- No source on retention of care or grooming loops specifically; the owner should treat this as a hypothesis and test it with a prototype retention check at D1, D7 and D30 in Roblox analytics.

## Overall gaps
- Fewer long-holding games (3 months or more) than asked were fully evidenced; Brainrot, Garden, Escape Tsunami and 99 Nights are best covered. Throw Food For Animals and Steal An Egg are only a few months old.
- No RDC talks or Roblox game pages were read; the only [official] source is the Creator Docs retention page.
- Player-count readings come from the Roblox search API (noisy), RoWatcher and unnamed trackers in articles. Rolimons, rotrends, rostats, rblxdb, bloxodes, statroblox were not read.
