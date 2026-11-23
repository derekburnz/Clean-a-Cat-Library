# Roblox ads as a demand signal, and the audience for cozy cat / spa games (as of 2026-11-22)

Labels: [official] = Roblox; [dev] = developer-reported; [opinion] = agency/blog/press. Research was capped at ~22 tool calls; devforum.roblox.com threads on Ads Manager recaps redirected to a maintenance page and could not be read (only titles seen in search results).

## 1. How Roblox ads work in 2026 and what Ads Manager reports

### Takeaway
Ads Manager sells sponsored thumbnails on Home and in search, with goals of Plays, Earnings (limited) and Qualify for Kids and Select. Reported metrics are Spent, Impressions, Clicks, Plays, cost per play, Playtime and Earnings/ROAS. Roblox also runs video/brand ad products (rewarded video, homepage feature) but those are for brands and monetization, not a small studio's game promotion.

### Cited Findings
- [official] Sponsored thumbnails appear on Home and in search; up to 10 thumbnails per campaign, rotated evenly; shown 16:9. Goals: Plays, Earnings (Limited), Qualify for Kids and Select. — [Ads Manager docs](https://create.roblox.com/docs/production/promotion/sponsoring-experiences) (undated page, fetched Nov 2026)
- [official] Summary cards: Amount Spent, Impressions, Plays, Playtime. Table: Spent, Impressions, Clicks, Plays, cost per play (CPP), Playtime, Earnings. Earnings campaigns report ROAS (attributed USD earnings / spend; "Estimated ROAS" while attribution is open). Impressions/clicks real time; plays/earnings depend on attribution, can include events up to 30 days after ad served; data can take up to 48 hours. — [Ads Manager docs](https://create.roblox.com/docs/production/promotion/sponsoring-experiences)
- [official] Auto-bidding: set budget and duration, Roblox calculates bid; daily or lifetime budgets. — same page
- [official] Docs do not list a play-through or retention metric for ad-acquired players in the report; ad-acquired retention would have to come from the experience's own Analytics. (Absence on the fetched page; page summary only.) — same page
- [official] "Ad campaigns for games that are not unique can result in no ad spend and no conversions." Ads are moderated before going live. — same page
- [official] Roblox (CES, Jan 2026) says it is scaling its ad platform: Homepage Feature (premium CPM brand unit, closed beta), Rewarded Video (in 400+ experiences, completion above 90%, viewability above 95%), programmatic access via Amazon DSP, Liftoff, Index Exchange, Magnite, Pubmatic plus Google. — [Roblox newsroom, Jan 2026](https://about.roblox.com/newsroom/2026/01/roblox-expands-advertising-platform)
- [dev] Aug 29, 2026 DevForum report claims lower CTR on unchanged creatives since changes announced June 15, 2026 (unverified; relayed from other developers). Staff reply only "assigned to our team for review." — [DevForum](https://devforum.roblox.com/t/sponsored-ads-traffic-degrades-the-engagement-metrics-used-for-discovery-causing-paid-acquisition-to-harm-organic-ranking/4838351)
- [dev] Search-result titles only (content not read): "Ads Manager Updates: Home + Search Combined, New Benchmarks and Sunsetting the Classic Flow" and "Ads Manager RDC Recap: Earnings, ROAS Reporting, & Incrementality" exist on DevForum. — [benchmarks thread](https://devforum.roblox.com/t/ads-manager-updates-home-search-combined-new-benchmarks-and-sunsetting-the-classic-flow/4084863), [RDC recap](https://devforum.roblox.com/t/ads-manager-rdc-recap-earnings-roas-reporting-incrementality/4909790)

### Inferences
- A "cat spa" ad that wins clicks is measured by Clicks and CTR (real time); plays and CPP lag up to 48 hours to 30 days.
- The "New Benchmarks" thread likely contains official benchmark figures and is worth a manual read by the studio.

### Gaps
- Roblox did not appear to have a separately documented search-ads or video-ads format for game promotion in the pages read; the combined Home + Search flow is only known from a thread title.
- Official detail on in-report play-through/retention for ad cohorts not found.

## 2. Benchmarks for CTR and cost per play

### Takeaway
No official benchmark number was retrieved. Developer-reported CTRs span 0.01% to ~2.7% depending on format and creative; one July 2026 thumbnail test hit 2.6-2.7%. Treat all as anecdotal.

### Cited Findings
- [dev] July 27, 2026: one developer's sponsored game thumbnails: Game Icon CTR 2.59%, CPP 1.695 ad credits; custom artwork CTR 2.7%, CPP 0.044 ad credits (figures as posted; the poster's own numbers have minor inconsistencies). — [DevForum](https://devforum.roblox.com/t/need-advice-on-my-games-ad-performance-and-next-steps/4760265)
- [dev] July 13, 2026: sponsored UGC item ads showed CTR 0.01% to 0.09% across 9 items (~2,000 Robux, 1.7M impressions, under 5 attributed purchases). This is UGC item ads, not game ads. — [DevForum](https://devforum.roblox.com/t/bug-sponsored-ads-algorithm-fails-to-target-users-resulting-in-mathematically-broken-ctr-001/4734574)
- [opinion] Rowatcher: realistic CTR 1-2% for sponsored placements; ~5,000 Robux/day "cost floor", 7-day minimum; 7,000-10,000 Robux/day for obby/tycoon genres; implied ~8-17 Robux per visit (the note's own calc); D1 retention above ~30% before running ads. Author estimates, no methodology; page dated 2025-01-16 with modification 2026-06-21 (inconsistent). — [Rowatcher](https://rowatcher.com/news/roblox-ads-in-2026-the-minimum-budget-that-actually-works)
- [dev] Older threads (2022-2024) report CTRs like 0.012%-0.021% on sponsors: possibly outdated, pre-Ads Manager. — [example](https://devforum.roblox.com/t/is-this-game-icon-really-that-bad-game-only-got-0012-sponsoring-ctr/2038721) (search listing only)

### Inferences
- CTR comparisons are only meaningful against the studio's own other creatives run in the same campaign window and audience targeting, since format and targeting vary widely.

### Gaps
- No official 2025/2026 CTR/CPP benchmark text retrieved (benchmark thread unreadable). No format-by-format (video, search, rewarded) benchmarks found.

## 3. What a high click rate predicts; concept testing; advertising something not in the game

### Takeaway
No source found showing a high-CTR creative predicts Home tap rate, retention or success. Evidence points the other way: ad traffic can behave differently from organic. Roblox docs do not endorse fake-door testing; I found no explicit text on it either way.

### Cited Findings
- [dev] Aug 2026: one developer reported ad traffic playtime of 11-12 min vs 28-30 min with ads off, D1 about 3% vs 5-8%, ~45% of new ad players never pressed the Deploy button; single-game anecdote in an extraction-shooter genre. — [DevForum](https://devforum.roblox.com/t/sponsored-ads-traffic-degrades-the-engagement-metrics-used-for-discovery-causing-paid-acquisition-to-harm-organic-ranking/4838351)
- [official] Home ranking's main signal is play-through rate after seeing the game in Recommended for You; first-play bounce is negative; also play days, playtime per user, qualified sessions; based only on organic users. — [Discovery docs](https://create.roblox.com/docs/en-us/discovery.md)
- [official] Ads docs: similar/non-unique games are not prioritized and ad campaigns for them may not spend. — [Ads Manager docs](https://create.roblox.com/docs/production/promotion/sponsoring-experiences)
- [official] The fetched Ads Manager docs do not explicitly require creatives to match the experience, but ads are reviewed against advertising standards. A "New Advertising Policies & Standards" DevForum post exists (2026) but was unreadable. — [DevForum](https://devforum.roblox.com/t/new-advertising-policies-standards/4527365)
- [dev] Rowatcher advice: success signal is concurrents holding 20-30% above pre-campaign baseline two weeks after spend stops. — [Rowatcher](https://rowatcher.com/news/roblox-ads-in-2026-the-minimum-budget-that-actually-works) (opinion, unsourced)

### Inferences
- A click on "cat spa" shows interest in the thumbnail promise; it does not show interest in playing a spa loop. Advertising a game feature that does not exist risks a rejected ad or a misleading-ad policy issue (rules text not read) and bad play-through.
- A safer test: sponsor the existing cat cafe with a spa-themed creative only if the game truly contains a spa element.

### Gaps
- No Roblox guidance on fake-door/concept testing found. No study correlating CTR with later retention found. Advertising-standards text not read.

## 4. Ad-acquired players and Home recommendations

### Takeaway
Official: engagement, retention and monetization of users first acquired through ads are excluded from Home (Recommended for You) ranking signals; ads do not penalize the game.

### Cited Findings
- [official] "Sponsored tiles are served through the ads system and aren't ranked as RFY candidates." — [Discovery FAQ](https://create.roblox.com/docs/en-us/discovery-faq)
- [official] "Engagement, retention, and monetization from users acquired through ads are excluded from RFY ranking signals," including later returns via Home. — same page
- [official] "Ads do not penalize or downrank your game in RFY." Ad-acquired users are considered already acquired, so RFY impressions may dip even as total acquisition rises. — same page
- [official] Signals from sponsored ads, curation, search, charts, friends, teleport, notifications can help a game get considered for organic RFY; each ranking signal is based on organic users from RFY. — [Discovery docs](https://create.roblox.com/docs/en-us/discovery.md)
- [dev] Contrary claim (Aug 2026) that ad traffic harms organic ranking; unverified and conflicts with the official text above. — [DevForum](https://devforum.roblox.com/t/sponsored-ads-traffic-degrades-the-engagement-metrics-used-for-discovery-causing-paid-acquisition-to-harm-organic-ranking/4838351)

### Inferences
- Ads buy players but do not directly build Home ranking; a game needs organic play-through to rank.

### Gaps
- Pages undated.

## 5. Who plays cozy, pet, cat, roleplay, tycoon games

### Takeaway
I did not find official age/gender/device splits for these genres. Only platform-level figures and one tablet/creative note surfaced.

### Cited Findings
- [official, reported via press] Q3 2026 (reported Oct 29, 2026): DAU 138M, down 9% year on year, up 12% quarter on quarter; hours engaged down 15% year on year; players 18+ were 29% of age-checked daily players worldwide (37% US), up 18% year on year; about 64% of daily players age-checked; DAU up 37% in India, 33% in Japan. — [GGRecon, Nov 2, 2026](https://www.ggrecon.com/articles/roblox-daily-players-fall-q3-2026/) (secondary)
- [official] Replay: tablet users most likely to search for creative experiences such as Build a Plane and Dress to Impress. — [Roblox Replay Dec 2025](https://about.roblox.com/newsroom/2025/12/roblox-replay-decoded-search-style)

### Inferences
- An all-ages cozy game sits in a platform whose age-checked audience is shifting older (18+ rising), though the share under 13 was not given.

### Gaps
- No under-13 share, gender split, country or session-pattern data for cozy/pet/cat/tycoon found. Roblox investor deck and RDC talks not accessed. coopboardgames.com listing appeared but not read.

## 6. Roblox Replay and search trends

### Takeaway
The Dec 2025 Replay post does not mention cats, pets, spa, salon, cozy or girls. It stresses roleplay/simulation, broad searches, and avatar self-expression.

### Cited Findings
- [official, Dec 2025 (about 11 months old)] Top 2025 searches: Brookhaven, Grow a Garden, Steal a Brainrot; broad searches like "horror" and "roleplay" popular; roleplay and simulation led the top search list; dance/emote terms took over Marketplace searches in H2 2025; Dress to Impress searched by tablet users; Hello Kitty and Y2K nostalgia noted among millennials; plans for avatar movement and makeup updates in 2026. Survey: 1,600 US Gen Z aged 13-28, 50/50 gender; 68% say branded avatar styles must fit the game theme (56% roleplay, 54% fashion-focused). — [Roblox Replay](https://about.roblox.com/newsroom/2025/12/roblox-replay-decoded-search-style)
- [opinion] A Beauty Matter piece on Roblox year in review exists (not read). — [link](https://beautymatter.com/articles/roblox-year-in-review-what-brands-should-know-for-2026-success)

### Inferences
- Fashion/avatar-styling experiences are a visible demand category (Dress to Impress). That is adjacent to, not proof of, spa/makeover demand.

### Gaps
- No 2026 year-in-review available yet as of Nov 22, 2026. No cat/pet/spa/cozy mention found.

## 7. Rules bounding a young-audience cat spa game

### Takeaway
Content maturity labels gate who can see the game; chat is age-gated; paid random items need odds disclosure; ads docs do not address under-13 ad exposure.

### Cited Findings
- [official] Labels: Minimal/Mild reach Roblox Kids (5-8) and Select (9-15); Moderate reaches Select and 16+; reaching Kids/Select also needs publishing requirements. Unrated experiences are restricted; Kids/Select games without IARC ratings by Jan 26, 2027 may be removed from the Australian Kids and Select catalog. Hangouts with private spaces (bedrooms, bathroom stalls) are 18+ only; hangouts without private spaces 16+; roleplay central to the game is excluded from the hangout question. — [Content maturity](https://create.roblox.com/docs/en-us/production/promotion/content-maturity)
- [official] Age checks required to chat globally from Jan 7, 2026; under 9 need parental consent; 9-12 and 13-15 chat only within own and adjacent age groups; Studio real-time collaboration will require age checks. — [Roblox newsroom, Jan 2026](https://about.roblox.com/newsroom/2026/01/roblox-age-checks-required-to-chat)
- [official] Paid random items: show all outcomes and numerical odds as percentages summing to 100%, including via keys/spin tickets; luck boosts must update odds; check `ArePaidRandomItemsRestricted` via PolicyService, and offer an alternative when true. — [Paid random items](https://create.roblox.com/docs/en-us/production/monetization/paid-random-items)
- [official] Ads Manager: users must be 13+ with verified email; card payments 18+; targeting options reach only players eligible for personalized ads; Kids and Select goal targets age-checked Highly Engaged Players. The docs do not say whether ads can be shown to under-13 players. — [Ads Manager docs](https://create.roblox.com/docs/production/promotion/sponsoring-experiences)

### Inferences
- A spa with "treatment rooms" could be classed under private-space rules only if it is a social hangout; a roleplay/sim framing is treated differently, but the exact classification should be verified in the questionnaire.

### Gaps
- Under-13 ad exposure rules not found. Official 2025/2026 label-change details beyond these pages not read.

## 8. Cross-promotion within a group

### Takeaway
Little retrieved. Teleport is named as a discovery source for organic RFY signals; no rule text or effectiveness evidence was found.

### Cited Findings
- [official] Teleport is listed among sources whose signals can help a game be considered for RFY. — [Discovery docs](https://create.roblox.com/docs/en-us/discovery.md)
- [official, search listing only] Related DevForum posts exist: Direct Joins to Non-Root Places with Teleports, Configure Direct Joins by Place, and "Introducing Two Game Security Settings: Third Party Sales & Cross Game Teleports" (2020, outdated). Content not read. — [Direct joins](https://devforum.roblox.com/t/direct-joins-to-non-root-places-with-teleports/3137041), [Cross game teleports](https://devforum.roblox.com/t/introducing-two-game-security-settings-third-party-sales-cross-game-teleports/674209?page=5)

### Inferences
- Cross-game teleport settings exist and must be enabled by the experience owner (from thread title only; verify).

### Gaps
- No rules, limits, portal/prompt guidance, group page behavior, or efficacy data found. Needs a direct read of create.roblox.com teleport docs.
