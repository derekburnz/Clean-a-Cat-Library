# Clean a Cat  (2026-11-23 ET, Planning-Agent, status: draft, name locked, design not locked until Derek's playtests are in)

Second pass on November 23: prices, tips and build slots were reworked with Design-Agent so the first 5 minutes add up (issue 5 in the game repo), the notification opt-in became a bell button and the design was checked against Roblox's maturity rules.

Slug: `clean-a-cat`. Game repo: `derekburnz/Clean-a-Cat`. The name was locked on November 23, 2026 (Clean a Cat, chosen over Clean the Cat).

This draft follows Derek's loop from November 23: get a dirty cat, clean it in different ways, return it to its owner or put it on display, earn money and fill the index, and upgrade the spa with builds that take longer and longer so players come back. How the name was chosen is in [cat-spa-concepts.md](cat-spa-concepts.md). Games to playtest first are in [playtest-list.md](playtest-list.md).

**Hook (one sentence):** people hand you their filthy cats and you scrub, fluff and style each one by hand while you build the fanciest cat spa on the street.

**Name and first minute:** the name says Clean a Cat, so a new player is cleaning a cat within 3 seconds of spawning and has a clean one by second 15.

**Core loop**
- Every 30 seconds: take a dirty cat, clean it at each station it needs and hand it back for coins and stars, which buy tools, new stations and bigger rooms.
- Every session (10 to 15 min): serve 15 to 25 cats, keep a stray or two for the display window, stamp new pages in the Cat Index and start a long build before leaving.
- Every week: finished builds open new rooms and rarer customers, index sets pay out and Derek's events (for example a Cat Show weekend) bring players back.

**How players get cats** (options and reasons are in cat-spa-concepts.md)
- **Customers bring them.** People queue at the door holding a dirty cat. A board by the door shows which cats can come and the chance of each. Stars earned by good service raise the chance of rarer cats. Nothing paid changes the chances. The first customer is always a common cat and the board lights up from the second customer, so every chance shown is true.
- **Strays turn up.** Now and then a muddy stray waits in a box at the back door. Nobody owns it, so once it is clean it stays as a spa cat. The very first cat of the game is a stray, so every player owns a cat inside the first minute.
- No catching and no searching. Catching did poorly in Derek's last game and it would move the fun away from the spawn.

**Cleaning in different ways:** each cat shows one to four need icons. Mud needs the sponge, tangles need the brush, a wet coat needs the blow dryer, a bad smell needs the bubble bath and long claws need the pawdicure. Each step is one hands-on action of ten seconds or less. Rarer cats have more needs and pay more. A station the player has not built yet shows as a locked icon, which is the reason to build it.

**Return or display**
- **Customer cats** go back to their owner: coins, a tip for a clean job and stars for the spa.
- **Strays** move into the display window at the front. They earn tips over time, also while the player is away up to a cap, and a fuller window draws more customers.
- **Cat Index:** every kind of cat gets a Washed stamp the first time it is cleaned and a Resident stamp when one lives in the window. Finished sets pay a bonus.

**First session** (brand new player, phone)
- 0:00 Spawn inside your own small spa at the tub. A muddy stray is in it and a sponge is in hand. One arrow says Scrub.
- 0:15 The mud is gone, the real coat shows and the cat shakes off.
- 0:25 Three brush swipes fluff it up. Pick one of three bows.
- 0:40 Before and after photo and 10 coins. The stray hops into the display window and is yours.
- 1:00 The first customer walks in with a common cat. Goal shown: Cat Index 1 of 10. The chance board lights up when the second customer arrives.
- 2:00 Buy Bubble Soap (30 coins, instant): a wider scrub.
- 3:00 Build the Brush Table upgrade (40 coins, 10 second build). The builder kitten hammers and a countdown shows.
- 4:00 A customer arrives whose cat needs a blow dry. The icon is locked and the dryer costs 75 coins with a 1 minute build.
- 5:00 Buy the dryer. Cats keep coming while it builds.
- 6:00 The dryer is done and dried cats pay more. The builder kitten shows a big blueprint: the VIP Room, 8 hours, 100 coins, with the line Start it before you go.
- 8:00 Start the VIP Room. It builds on its own slot behind a curtain with a countdown sign, so the kitten is still free for stations.
- 8:00 to 15:00 A purchase about every 90 seconds: a better brush (instant), then the Bubble Bath (10 minute build) near minute 12.
No forced tutorial, pop-ups, shop prompt or like request in this session. Tutorial steps are tapped by the player (dim plus arrow) and ship behind an off switch.

**Progression and build times**
| Step | Example | Slot | Build time | Reached about |
|---|---|---|---|---|
| Tools | Bubble Soap, better brush | None | Instant | Minute 2 |
| First station upgrade | Brush Table | Station | 10 seconds | Minute 3 |
| Second station | Blow dryer | Station | 1 minute | Minute 5 |
| First room | VIP Room (rarer customers) | Room | 8 hours | Started near minute 8, open on day 2 |
| Third station | Bubble Bath | Station | 10 minutes | Minute 12 |
| Fourth station | Pawdicure | Station | 1 hour | Session 2 |
| Later rooms and floors | Kitten playroom, roof garden | Room | 12 to 24 hours, never longer | Days 2 to 7 |

Rules for builds: there are two build slots. The builder kitten builds one station at a time (seconds up to 1 hour). The building site builds one room at a time (hours). A room build never blocks a station build, the spa stays open while building, a finished build waits for the player and nothing is lost by coming back late. No paid skips at launch.

Why two slots: with one build at a time the 8 hour build sat behind the 10 minute and 1 hour builds, so a first session never reached it, and once it was running nothing else could be built for 8 hours. The day 2 hook only works if most players who stay past minute 8 leave with a long build running.

**Economy**
- Sources: coins and tips per cat served, tips from window cats and index set bonuses.
- Sinks: tools, stations, rooms, window cushions and decor.
- The one pace number: cats served to afford the next purchase. About 3 for Bubble Soap, 3 for the Brush Table, 6 for the dryer and 7 for the VIP Room, then multiply by about 1.6 each step. If pace is too fast, raise the price rather than cut a reward.
- Starting values (agreed with Design-Agent on issue 5, paper numbers until the scrub is timed on a phone): first scrub 8 seconds, a common cat pays 10 coins plus a tip of 2, a window cat tips 1 coin every 10 seconds, the away tip jar holds 1 hour of tips, Bubble Soap 30 coins, Brush Table 40 coins, dryer 75 coins, VIP Room 100 coins.
- Guard rail: the whole display window earns less than about a third of what washing earns at the same stage, so washing stays the main way to earn.
- The numbers move to `docs/design/clean-a-cat/tuning.md` in the game repo, which Design-Agent keeps.
- First chance board: Common 60%, Uncommon 25%, Rare 11%, Epic 3.5%, Legendary 0.5%. Shown chances must match the code.

**Reason to come back tomorrow**
1. A long build finishes while the player is away and opens with a small celebration on return.
2. The tip jar from the window cats is full.
3. The board shows tomorrow's VIP customer as a silhouette.
No streaks and nothing is lost by missing a day.

**Notifications** (Roblox's experience notifications, rules read November 2026)
- One message at most per player per day, sent when the longest build finishes, for example: Your VIP Room is finished and the cats are waiting.
- Players must opt in. Only players aged 13 and over can get personal messages like this one. Players under 13 only get update notices, so for them the pull is what the game showed before they left.
- The builder window shows a bell button, Tell me when it's done, beside any build over 1 hour. Only a tap on the bell opens Roblox's opt-in prompt, so no window ever opens by itself. Players who cannot get personal messages see Ready in 8 h. Come back to see it! The game never requires the opt-in.
- No fake countdowns or pressure wording. Roblox bans false time pressure.

**Social:** spas sit side by side on one street so players see each other's windows and reveals. Friends can help in your spa, one scrubbing while one brushes. Deliberately not in: stealing, trading, fighting and typed text (cat names come from a preset list). The spa is an open shop floor where only cats are bathed. It has an open front, no doors that close and no rooms or tubs made for player avatars (see the maturity check under Risks).

**Monetization** (follows the monetization-policy skill)
- Game passes only at launch: 2x Coins, Second Builder (a second kitten, so two stations can build at once) and Golden Sponge (a wider scrub with gold bubbles).
- No developer products at launch. Coins cannot be bought, so the random customer never counts as a paid random item. Nothing sold changes the chances.
- PolicyService is fetched per player from day one.

**Prototype scope (vertical slice)**
| System | Smallest version | Size | Owner |
|---|---|---|---|
| Scrub and reveal | 12 to 20 mud patches that vanish under a finger drag or mouse hold | M | Gameplay-Engineer |
| Brush and bow | Three swipes, three bows, before and after photo card | S | Gameplay-Engineer |
| Treatment feel | Bubbles, mud chunks, squeak, sparkle, shake off and purr | S | Motion-FX-Agent |
| Customers and strays | A door queue from a table of ten cats, the chance board and a stray every few customers | M | Gameplay-Engineer |
| Needs and stations | Need icons, sponge and brush at launch of the slice, blow dryer as the first built station | S | Gameplay-Engineer |
| Display window and index | Four cushions, tips while online and away with a cap, Washed and Resident stamps | S | Gameplay-Engineer |
| Builds | Builder kitten for stations and a building site for rooms, one build per slot, timers that run while away, finish celebration | M | Gameplay-Engineer |
| Notification | A bell button on builds over 1 hour and one message when the longest build finishes | S | Gameplay-Engineer |
| Saving | Coins, stars, cats, tools, builds with end times and the index, server authoritative | S | Gameplay-Engineer |
| Cats and spa | One cat body with ten coats, a customer figure, tub, brush table, dryer and one small spa | M | Model-Agent |
| Screens | Coin counter, need icons, photo card, index, builder panel, phone first | M | Design-Agent |
| First minute guide | Three tapped steps with dim plus arrow, behind an off switch | S | Design-Agent |
| Analytics | joined, loaded, first scrub, first reveal, first photo, first customer, first upgrade, first build started, first long build started, returned next day | S | Growth-Agent |
| Checks | Phone playtest, save test on a fresh and a returning player, build timer test across a rejoin | S | Review-QA-Agent |

Build order: scrub and reveal first, on a phone, with one grey cat. If that is not fun, stop and rethink. Then brush and photo, customers, the window, builds and saving.

**Risks**
- Demand: no spa or grooming game has grown large on Roblox. Mitigation: a hands-on loop instead of a slow tycoon, a one week slice and a read of real players before more is built.
- Waiting: timers can feel like a wall. Mitigation: the first builds take seconds, the spa never closes during a build and there is always a cat to wash.
- Fading: well liked cleaning games lost almost all their players in months. Mitigation: builds, the window and the index from the first session, then Derek's events.
- Notifications reach few young players. Mitigation: the reasons to return are shown in the game before the player leaves.
- Technical: many mud patches on cheap phones. Mitigation: cap at 20 patches and run effects on the player's own device.
- Policy: Roblox limits social hangouts to players 16 and over, and hangouts with private spaces (small closed rooms for sleeping, changing or bathing) to verified adults. A random customer can also look like a loot box. Mitigation: the game is about washing cats and not about chatting, the spa has an open front with no closing doors, only cats are bathed, no room is a bathroom or sauna for avatars, chances are on the board and coins cannot be bought. Checked against Roblox's content ratings page on November 23, 2026. The page does not mention spas or pet washing, so this is our reading and not a ruling.
- Reaching young players: a new game is first shown only to age-checked players of 16 and over. To be shown to Roblox Kids (ages 5 to 8) and Roblox Select (ages 9 to 15) the whole maturity questionnaire must be filled in with a Minimal or Mild result, the creator account must be age-checked and verified with 2-step verification, there is a one-time refundable fee per game or an active Plus or Premium subscription, and the game needs 100 unique plays from highly engaged players in 60 days before Roblox evaluates it. Read on Roblox's Kids and Select page on November 23, 2026. Mitigation: Derek does the account steps before the first public test and Growth-Agent plans the first 100 plays.
- Cheating: fake treatment, coin or timer requests. Mitigation: the server owns the cat, the pay and every build end time, and requests are checked and rate limited.

**Out of scope for now:** trading, stealing, fighting, catching cats, paid luck, paid skips, buyable coins, typed cat names, rooms or tubs for player avatars, a booking book with VIP appointments, the bus that drops a crowd of customers, the Cat Show contest, decor sets and any shared characters with Cat Cafe.

**What the playtests should settle before this is locked**
1. Is washing done by hand in the rival games, and does it feel good or like a chore?
2. How do they hand the player a pet, and how long does it take?
3. Do any of them use build timers, and how do the waits feel?
4. What made Derek want to stop playing each one?

**Open questions for the owner**
1. Customers plus strays as the way to get cats? Recommended: yes.
2. Paid skips for build timers? Recommended: not at launch. Sell a Second Builder pass.
3. Longest build time? Recommended: 24 hours at most, with the first 8 hour build on offer in session one.
4. Should the words cat spa also appear in the description and on the icon, since the cat spa ad did well? Recommended: yes, as long as the first minute shows a spa.
5. Two build slots (stations and rooms), so the 8 hour build starts in the first session and never blocks the short builds? Recommended: yes.

**Proposed decision line:** `2026-11-23: Build Clean a Cat as a hands-on wash and style game where customers bring cats and strays stay on display, with timed builds as the reason to return. Why: fastest first fun, a proven come back hook and no catching.`
