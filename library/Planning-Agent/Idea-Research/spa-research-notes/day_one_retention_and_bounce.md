# Day 1 retention and first-minute bounce on Roblox (as of 2026-11-22)

Labels: [official] = Roblox; [dev] = developer-reported; [tracker] = third-party data; [opinion] = blog/agency. Roughly 25 tool calls used. Many DevForum threads redirect to create.roblox.com/maintenance and could not be read. Pages fetched through a summarizing tool, so quotes are as returned by that tool; the studio should re-read key pages directly. Not repeated from earlier notes: the Discovery FAQ ad-exclusion text, the Jun 15 2026 28-day move in outline, Mar 2026 Standout Games.

## 1. Roblox guidance and benchmarks on first-session drop-off, D1 retention, playtime

### Takeaway
Roblox publishes no "good D1" number in its Retention doc. Its benchmarks are relative ("similar games" shown on the analytics page) and explicitly not part of ranking. The only hard D1 numbers found are GameAnalytics 2025 (tracker, by session-length bucket) and a few DevForum posts (dev-reported, old).

### Cited Findings
- [official] Retention doc: "Day 1 retention is the percentage of new users who come back to your game after visiting it for the first time." It gives no benchmark or "good" threshold; it points to three levers: core loop, first-time user experience, performance. For onboarding it says to get players into the game quickly, "ideally in 5 minutes or less after entering your game." Undated page, fetched Nov 2026. — [Retention doc](https://create.roblox.com/docs/en-us/production/analytics/retention.md)
- [official] Benchmarks: "Benchmark metrics are based on a set of similar games shown at the bottom of your analytics page." "Benchmarks and benchmark games do not impact the Recommended for You algorithm in any way." Use as rough guide if the chosen games do not fit. Undated. — [Discovery docs](https://create.roblox.com/docs/en-us/discovery.md)
- [official] Retention doc notes a dip after a big influx of new users is "typical and temporary." — [Retention doc](https://create.roblox.com/docs/en-us/production/analytics/retention.md)
- [official] Onboarding doc: new players decide "within minutes"; track the Player Funnel and A/B test specific tutorial steps with Experiments, push values with Configs; keep early XP thresholds low; give free starter items/soft currency but balance so there is a reason to return; show short-, mid- and long-term goals in highly visible places; end onboarding "with a deliberately designed moment of joy." Undated. — [Onboarding](https://create.roblox.com/docs/production/game-design/onboarding.md)
- [tracker] GameAnalytics 2025 Roblox report (data 2025; page says "Last updated Aug 24, 2026", data window ends July 2025, so over 12 months old): median D1 / D7 by game average session length: 0-3 min 4.31% / 0.41%; 4-6 min 6.20% / 0.88%; 7-12 min 7.91% / 0.90%; 13-18 min 10.24% / 1.20%; 19-24 min 11.46% / 1.61%; 25+ min 10.76% / 1.82%. 95th percentile D1: 10.72%, 13.17%, 13.37%, 15.91%, 23.60%, 24.79%. Platform session length (GameAnalytics-integrated games, about 47% of engagement by their estimate): median 6.62 min mid-2025 (5.98 in 2024, 7.63 in 2023). No genre split in the report. — [GameAnalytics](https://www.gameanalytics.com/cn/reports/2025-roblox-report)
- [dev] Sept 30, 2024 (over 12 months old): a developer with 11% D1 was told by another community member that 11% was "pretty decent" and to aim for 15%+; no staff reply. — [DevForum](https://devforum.roblox.com/t/day-1-retention/3177419)
- [opinion] Rowatcher (earlier note) says D1 above ~30% before running ads; no methodology. Contrast with GameAnalytics 95th percentile of about 25%.

### Inferences
- A D1 of 10-15% sits near or above median in GameAnalytics' data; 24-25% is top 5%. Longer average sessions go with higher D1, so session length and D1 are linked in the data (correlation only).
- The Rowatcher 30% figure looks unrealistic against GameAnalytics percentiles.

### Gaps
- No official D1 benchmark by genre, no cozy/tycoon/simulator numbers found. DevForum cozy/tycoon D1 numbers not found. RDC 2025/2026 talks with benchmark numbers not retrieved.

## 2. Early signals feeding Home (Recommended For You) in 2026

### Takeaway
Official docs list play-through rate, first play bounce (under 60 s and 61-180 s segments), play days per user (Day 1, Day 2-7, Day 8-28) and playtime per user (capped 60 min/user/game/day). Signals come only from organic users.

### Cited Findings
- [official] Discovery doc (undated): "Play through rate" = "The rate at which users play your game after seeing it in the Recommended for you sort" (listed as most important). "First play bounce rate" (negative) = "The rate at which users leave your game after a short play session," with segments "< 60 seconds average rate" and "61-180 seconds average rate." "Play days per user" = "The average number of unique days users engage with your game," segments Day 1, Day 2-7, Day 8-28. "Playtime per user" = "The average amount of time users spend in your game," capped at 60 minutes per user per game per day. — [Discovery](https://create.roblox.com/docs/en-us/discovery.md)
- [official] Jun 15, 2026 newsroom (John Ciancutti): algorithm expanded "from its previous 7-day view to a 28-day view that directly measures long-term retention"; signals cover "day 1, day 2-7, and day 8-28"; the previous qualified play-through signal split "into more granular signals" for play-through behavior, session quality and spend. The article does not mention quick leaves. — [Newsroom](https://about.roblox.com/newsroom/2026/06/optimizing-discovery-great-games-reach-millions-players-roblox)
- [official] DevForum "How we are improving Home this year": Mar 9, 2026 "Deep play through rate" introduced ("identifies the deeper conversion to sustained interest and active participation"); Mar 26, 2026 7-day qualified play sessions per user ("helps capture whether a game retains users after the first session"). The page does not mention first-minute leaves. — [DevForum](https://devforum.roblox.com/t/how-we-are-improving-home-this-year/4502571)
- Earlier note already holds: Aug 6, 2026 post on retention and monetization value; Jul 29 autoplay video on Home (up to 39% playtime increase in tests).

### Inferences
- The two bounce segments (under 60 s, 61-180 s) map directly onto the studio's minute 0-3 goal; D1 is the first play-day segment.

### Gaps
- Roblox's "Recommended For You Algorithm Improvements That Better Value Long-Term Retention" post (4684575) was unreadable (maintenance redirect). I found no official wording naming a "28 day signal" beyond the newsroom text above. The doc page itself is undated, so whether the "<60 s / 61-180 s" wording predates 2026 is unknown.

## 3. Roblox advice on onboarding, loading, mobile, pop-ups

### Takeaway
Official onboarding pages give qualitative advice and no tutorial length or load-time numbers. I could not retrieve Roblox's performance docs on load and low-end devices.

### Cited Findings
- [official] Onboarding techniques (undated): show prominent in-world visuals instead of pop-up text; highlight targets by dimming the screen and outlining a button (Hello Kitty Cafe example); keep hints on screen until the step is done; directional trails; feedback for every action; contextual tutorials triggered by natural play; timed hints based on playtest data (example: in "Plant," most players pressed the seed button within 10 seconds so a highlight at 11 seconds). — [Techniques](https://create.roblox.com/docs/production/game-design/onboarding-techniques.md)
- [official] Same page, "Mistakes to avoid": lengthy prescriptive tutorials ("Players quit when they're bored by them, and they also quit when they don't understand what to do in the first few minutes"); text-heavy instructions; front-loading everything; silent actions; hints too early/late; repeated hints. Focus the first session on essentials and delay non-essential learning. — same page
- [official] Onboarding page (above): reach the game quickly, "ideally in 5 minutes or less."
- [opinion] Rowatcher, Aug 24, 2026: no measured data; claims drop-off is concentrated in the first 90 seconds; names loading-screen monologues, gated first actions, explaining before experiencing, NPC dialogue walls as mistakes; cites Adopt Me (hold a baby at once, no explanation). Promotional tool plug at the end. — [Rowatcher](https://rowatcher.com/news/your-first-90-seconds-are-destroying-roblox-retention)

### Gaps
- No official load-time target, no mobile or low-end device guidance retrieved (create.roblox.com performance page fetch failed). No official pop-up/shop-timing rule found. Several DevForum first-session threads were seen only as titles (e.g. "Players leaving during tutorial", "Why are people spending less than 3 minutes at our game"); not read.

## 4. Day 2 return hooks in the named games

### Takeaway
Evidence retrieved is thin: only a few games had readable, dated guide pages. Confirmed items below; everything else is unverified and should be playtested.

### Cited Findings
- Grow a Garden: [opinion/dev quotes, May 27, 2025, over 12 months old] icon says "Grows Offline"; developer quote that offline growth brings players back to see what they grew; weekly Saturday 7am PST updates with a gift; limited-time events with rare plants and pets; veterans gift fruit to newcomers. Newsletter does not mention restock timers. — [GameDiscover](https://newsletter.gamediscover.co/p/what-grow-a-gardens-89-million-ccu). Naavik (Jul 6, 2025): "gentle first-time user experience", "idle-inspired timers and resource collection", Robux can speed timers; top hits borrow "timers, boosts, gacha, cosmetics, and progression passes" from mobile F2P. — [Naavik](https://naavik.co/digest/predicting-the-next-big-hits-on-roblox/)
- Throw Food For Animals: [guide, updated Nov 1, 2026] "Animals placed at your base keep earning money while you're away from the game." Other hooks (daily reward, timers) not found on that page. Category: offline-earning timer. — [Bloxodes](https://bloxodes.com/articles/throw-food-for-animals-beginners-guide)
- Steal a Brainrot: [guide, Apr 26, 2026] offline income only from Rebirth 5+ ("Below that threshold, cash stops accumulating when you log out entirely"); storage cap stops income until collected; bases can be robbed while you are away; Tier 5 lock costs $250M, stops "roughly 90% of casual thieves." No lock timer mentioned. Social/loss hook (theft). — [RBLXGuide](https://rblxguide.com/games/steal-a-brainrot/updates/steal-a-brainrot-afk-farming-guide-2026)
- Steal An Egg: nothing retrieved.
- Adopt Me, Pet Simulator 99, Bee Swarm, Fisch, Dress To Impress, Brookhaven, Restaurant Tycoon 2, My Restaurant, 99 Nights in the Forest: searches returned only listing pages; the Adopt Me wiki fetch was blocked. I could not verify any hook for these from a source and will not state them from memory.
- Category map for the verified ones: timers that finish while away = Grow a Garden growth, Throw Food offline earnings, Brainrot offline income (gated and capped); scheduled updates/events = Grow a Garden; social = Garden gifting, Brainrot raiding (loss-based).

### Gaps
- Seed shop restock timing, Adopt Me aging/login rewards, Pet Sim 99, Bee Swarm quests, Fisch, DTI, Brookhaven, Restaurant Tycoon 2 / My Restaurant offline earnings, 99 Nights class progress: not found. Needs wiki reads or playtest.

## 5. Fair vs pressure hooks; Roblox policy on streaks, daily rewards, likes

### Takeaway
No Roblox rule banning daily reward streaks was found; Roblox ships a streak daily-reward feature itself. Notifications have explicit anti-pressure rules. Rules on rewarding likes/favorites were not found from staff.

### Cited Findings
- [official] Engagement Rewards feature package: "Daily rewards unlock after a certain number of consecutive daily logins"; `requiredDaysVisitedStreak` = consecutive days to earn; popup on join unless hidden. The page states no policy restrictions. — [Engagement rewards](https://create.roblox.com/docs/resources/feature-packages/engagement-rewards)
- [official] Experience notifications (page updated 2026-11-20): prohibited tactics include "disguised ads, false time pressure, bait-and-switch rewards, and tricking users into purchases"; games cannot require notifications to be enabled to participate or advance. — [Notifications](https://create.roblox.com/docs/production/promotion/experience-notifications.md)
- [official] Rewarded video: "bait" and misleading reward descriptions prohibited; cannot gate progress on an ad. — [Rewarded video](https://create.roblox.com/docs/production/promotion/rewarded-video-ads)
- [dev, Jul 2024, over 12 months old] Rewarding group joins considered safe by one member; favorites detectable by API, likes not; no staff comment. — [DevForum](https://devforum.roblox.com/t/boundaries-of-in-game-rewards/3051700)
- Earlier note: paid random items need odds disclosure and a restricted-region alternative.

### Inferences
- Reward-for-return with no loss when skipped (growth waiting, collection gifts) is consistent with all rules found. Loss streaks and false countdowns clash with the notification "false time pressure" rule, at least for notifications; I found no wider rule.

### Gaps
- Roblox Community Standards and the Creator Rewards (Engagement) policies on streaks, favorites and likes were not read in full. No staff statement on rewarding likes/favorites found.

## 6. Does offline progress measurably help retention?

### Takeaway
No numbers found. Only qualitative claims.

### Cited Findings
- [opinion, 2025] The GameDiscover piece argues offline growth helps retention because players can play other games and return; no data. — [GameDiscover](https://newsletter.gamediscover.co/p/what-grow-a-gardens-89-million-ccu)
- Earlier note: Garden Horizons (Grow a Garden-style) lost about 98% of players in about 2 weeks after a launch peak, linked to dev exits and an exploit. — [allthings.how](https://allthings.how/garden-horizons-player-count-drop-what-happened-and-is-the-game-dead/)

### Gaps
- No D1/D7 numbers from any Grow a Garden analysis, post-mortem, RDC talk or DevForum thread retrieved. A Roonby piece (Jan 13, 2026) on Grow a Garden losing players appeared in search but was not read.

## 7. First-session mistakes that raise bounce

### Takeaway
Roblox and one opinion piece agree: long or text-heavy tutorials, front-loaded information, silent actions and unclear goals. Others on the studio's list (load time, cutscenes, early shop pop-ups, icon mismatch) have no source found.

### Cited Findings
- [official] See section 3 (mistakes list, undated).
- [opinion] Rowatcher Aug 24, 2026: dialogue walls, loading-screen lore, locked first actions. — [Rowatcher](https://rowatcher.com/news/your-first-90-seconds-are-destroying-roblox-retention)
- [dev, Aug 2026, from earlier note] one game's ad traffic: about 45% never pressed the Deploy button, D1 about 3%. Single anecdote. — [DevForum](https://devforum.roblox.com/t/sponsored-ads-traffic-degrades-the-engagement-metrics-used-for-discovery-causing-paid-acquisition-to-harm-organic-ranking/4838351)

### Gaps
- No sourced statement on cutscenes, early shop pop-ups, load time, or icon/first-minute mismatch.

## 8. Features that help return visits and their rules

### Cited Findings
- [official] Experience notifications (updated 2026-11-20): opt-in only; personalized notifications go to opted-in 13+; under-13 opt-ins receive only experience update notifications; opt-in prompt not shown to under-13s, to users who already enabled it, or who saw it in the last 30 days; one notification per user per day per experience plus an unstated aggregate daily cap; 99 character string; launch data 200 bytes; sent from server scripts; game needs 100+ visits, not under moderation; no default string, each created in Creator Dashboard; delivery not guaranteed; stats after 100 impressions. — [Notifications](https://create.roblox.com/docs/production/promotion/experience-notifications.md)
- [official] Rewarded video (undated, 2026 footer): game must be public and unrestricted, no social hangouts with private spaces, approved content questionnaire, 2,000+ monthly unique visitors, publisher 13+ with 2-step and ID verification; user must click to start; reward granted after view, must be a developer product normally sold for Robux, no randomization, no Robux rewards, no progress gating; ads 6-30 s full screen; Join with Reward is closed beta, mobile only. Earlier note: rewarded video in 400+ experiences (Jan 2026). — [Rewarded video](https://create.roblox.com/docs/production/promotion/rewarded-video-ads)
- [official] Mar 26, 2026: 7-day qualified play sessions signal (Home). See section 2.

### Gaps
- Continue row on Home, events (docs), update announcements: not read, no rules retrieved. A very young audience reaches only update notifications, so the opt-in notification route is largely closed for under-13s.

## Source reliability notes
- Official docs fetched are undated; the notifications page is the only one with a date (2026-11-20).
- GameAnalytics data is from 2025; GameDiscover and Naavik pieces are 2025.
