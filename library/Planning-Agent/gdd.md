# Clean a Cat  (2026-11-25, Planning-Agent, status: agreed, built from the owner's plan answers)

Built from Derek's 65 plan page answers, his chat decisions of 2026-11-22 to 2026-11-25 and nine playtests. His own words are kept in the library repo (`library/Planning-Agent/playtest-notes.md`). Everything goes to the dev place first and nothing reaches the live game until he confirms it. Numbers go in `docs/design/clean-a-cat/tuning.md` (Design-Agent).

**Hook (one sentence):** dirty cats line up at your spa, you pick who is next, scrub each one clean by hand and find out which coat was hiding under the mud.

**Core loop**
- Every minute: pick a cat from the bench, wash it by hand in 3 to 10 short steps and tie its bow. You get coins, a tip and stars, and its coat fills a slot in the Cat Index. Coins buy tools, workers, stations and builds.
- Every session (20 minutes or more): wash about 12 cats, catch a special visitor, tick off daily quests, hire or level a worker and start a build before you leave.
- Every week: finish the weekly quests for a crate, open crates for pets, fuse three of the same pet into a star up and play the owner's events. Christmas is likely the first.

**First session** (targets for a new player on a phone; the full timeline and its rules are Design-Agent's, issue #5)

| Time | What happens |
|---|---|
| 0:00 | The character loads and a truck drops a plain brown box. About 4 seconds to watch, no loading screen. |
| 0:04 | Tap the box. A muddy kitten pops out. Pick him up and carry him to the tub. |
| 0:12 | His wash in the close up view: 3 simple steps. |
| 0:38 | Recap card with 3 stars. He is named Suds and trots to his cushion. |
| 1:00 | The first customer walks in with an easy cat. Wash it for the first coins and the first Cat Index stamp. |
| 1:45 | Suds asks once about notifications. Players under 13 never see it. |
| 2:00 | Two customers wait. The bench opens with a Wash next button. |
| 2:45 | The Index button arrives with a short tip. The tutorial ends. |
| 3:45 | The check in card: what waits on each of the next seven days played. |
| 4:00 | The first special visitor walks in. Only the player can wash their cat, and this first one drops a crate at about 5:00. |
| 6:00 | The Quests button arrives with a tip. |
| 7:00 | The gift stand lights up and Suds makes the like, favourite and group ask once. |
| About 10:00 | The first worker can be hired, station included. |
| About 15:00 | The first long build is offered. |

Rules for the whole session: one ask at a time and at least a minute apart, nothing during a wash or a recap, and menu buttons arrive one by one with a tip. The starter pack button appears after the tutorial and stays still until the second visit. A player who skipped the stand gets one favourite ask on the second visit or after 10 cats. Every first session change ships behind its own switch (rule 16).

**The wash:** always done by hand; no timer ever stands in for it.
- View: placing the cat in the tub opens a close up wash screen. The right tool is in the player's hand for each step. There is no tool menu.
- Steps: every kind of step is in the game from the start. A cat takes 3 to 10 steps by how dirty it is: 3 at dirt level 1, 4 or 5 at level 2, 6 or 7 at level 3 and 8 to 10 at level 4. A step takes about 5 seconds and the same step never comes twice in a row. The tutorial uses only the simple 3 or 4.
- The bar: foam, rinse and trim fill a bar at the top. It is full at about 90%, then the cat shakes off the rest and the next step starts.
- Turning: the cat holds still and turns by itself when a side is done. This is the version to try first.
- Praise: short praise words and a combo that pauses on a slip. Kept light.
- The bow: tying a bow is the easy last step on every cat, one tap that cannot fail. It adds money, and better bows bought with coins add more, so washing by hand stays rewarding next to the workers.
- Recap: the full card after every cat with stars, coins, the tip, each bonus and the coat that was hiding. One tap closes it.
- Dirt: mud that gets darker with the dirt level. No stink wisps.

**The spa**
- The bench: three or four cats wait, each with a card that shows how dirty it is, its steps and its pay. Pick one from the menu or press Wash next. Rarer cats are more often dirty and pay much more.
- Waiting: a waiting cat's heart bar drops and it gets grumpy. When the bar is fully empty the cat leaves and that job is lost. Nothing else is taken. Early bars are long so no cat can leave before about minute 10 of a new player's first session on a phone.
- Workers: human staff. Jo and Sam are hired with coins and Lou is a paid extra. Each comes with their own station in one purchase. A worker takes any cat by the mode the player sets (about to leave, rarest, dirtiest or first in line), is slower on dirtier cats, earns much less than the player and shows a progress bar above the cat. Players can rename their workers and typed names are filtered.
- Suds: the mascot kitten. He walks on four paws, explains new things in a bubble at the bottom of the screen and never washes. He is not a pet and not in the Cat Index.
- Special visitors: they appear now and then and leave after a while. Only the player can wash their cats, which are always very dirty, pay the most and have the coolest designs. Names and designs from Catch a Cat Cafe, the owner's earlier game, may be reused for them. They fill their own page in the Cat Index. After the scripted first one, a crate from a visitor is rare.
- Pets: cats that come from crates. One slot for the player and one for each worker. A pet stays beside the player or beside its worker and a worker's pet raises that worker's money. A pet already owned is kept, and three of the same fuse into a star up with better stats.

**Progression:** tools from about 2:30, the Index at 2:45, Quests at 6:00, the first short station build (15 seconds or less, so no Finish now price shows in the first minutes), the first worker at about minute 10, the first long build at about minute 15 and then more stations up to four tubs. Long builds take hours and never more than 24. A Grand Reopening is not at launch, but the saves are shaped so it can be added.

**Economy**
- Pay for one cat: a base amount, multiplied by speed (stars), by how soon the cat was taken and by how dirty it was (steps), plus the bow bonus and a tip. Taking a cat inside the first 10% of its heart bar gives a big bonus and a normal wait costs nothing.
- Other sources: workers, who earn much less than the player, quests, the check in card and a bonus of about 10% for each friend in the server.
- Sinks: tool tiers, workers with their stations and levels, builds, bows and the first pet slot for each worker.
- The one pace number: cats washed to afford the next purchase. Starting values to test: the first tool after 3 cats, the first station after about 8 and the first worker after about 15.
- Guard rail: workers and pets together always earn less than the player's own washing at the same stage.
- Coins are never sold.

**Reason to come back tomorrow**
- The check in card shows a reward for each of the next seven days played, with a good free crate on day 2. There is no streak and nothing is lost by missing a day.
- A long build started before leaving is finished.
- The tip jar has filled from the workers, up to a cap.
- A couple of daily quests reset each day. A couple of weekly quests give a crate when all are done.
- Empty slots in the Cat Index and a different visitor cat each day.
- Players of 13 and over who said yes get a notification when the jar is full.

**Social**
- Six spas stand side by side on one street, with six players in a server.
- Other players can walk into a spa. This is on from the start and a setting turns it off. A visitor can look and walk around but can never wash, pick, take or block anything.
- Players see each other carry cats and see the clean coats.
- Each friend in the server adds a small bonus, shown on screen.
- The free pet: a gift stand stands in the spa from the start with the pet sitting on it. Its card asks for a like and a favourite together and to join the game's Roblox group. Roblox lets a game check the favourite and the group but not the like, so those two are checked and the pet is then given. No pretend check is shown for the like. The owner is still looking into this.
- Not in: trading, stealing, fighting and friends as customers. The only typed text is a worker's name, and it is filtered.

**Monetization** (follows `monetization-policy`; prices are starting values the owner said to tune later; only the crate is random)

| What | Kind | Robux | Rule |
|---|---|---|---|
| 2x Coins | Game pass | 199 | |
| Second Builder | Game pass | 299 | Two builds at once |
| Golden Sponge | Game pass | 99 | |
| Lou, the extra helper | Game pass | 249 | Comes with his station and works like Jo and Sam |
| Second pet slot | Game pass | 249 | For the player and every worker |
| Crate | Developer product, random | 49, or 5 for 199 | The chance of every pet shows as a percentage before buying. PolicyService is read per player and the Robux crate is hidden where paid random items are restricted. The same crate can be earned. |
| Finish now on any build | Developer product | 5, 15, 35, 75 or 99 by time left | The price is on the button, no pop up, waiting is always free |
| Starter pack | Developer product, fixed | 299 | Golden Sponge, second pet slot and 2x Coins, worth 547. A real countdown of 72 hours from first join, kept on the server, then gone for good. |
| Private server | Roblox setting | 100, or free with Roblox Plus | The owner sets it on the game's page. What the setting allows is being checked. |

Rules that hold everywhere: no Robux product gives coins. Fusing pets is free with a fixed result. Nothing is ever sold to keep or bring back a cat that is leaving, and no price shows when a cat is about to leave. A no is final for that visit.

**Build scope** (in this order, each piece behind its own switch in the dev place)

| # | System | Smallest version | Size | Owner |
|---|---|---|---|---|
| 1 | Dirt levels and steps | The server rolls level 1 to 4 by rarity, the cat shows that level's mud, steps and pay follow | M | Gameplay-Engineer |
| 2 | Bench, heart bar and pay | Cards with Wash next, the early bonus, the cat leaves at empty, the pay formula | M | Gameplay-Engineer, Design-Agent |
| 3 | Bow and recap | Bow as the last step with a bonus, three bow tiers, the full recap card | S | Gameplay-Engineer, Model-Agent |
| 4 | Workers | Jo with her station, one mode and a progress bar. Then Sam, all four modes and renaming | M | Gameplay-Engineer |
| 5 | Special visitors | One scripted visitor at minute 4 with a crate, then random visits | M | Gameplay-Engineer, Model-Agent |
| 6 | Crates and pets | Whole thing | L | Gameplay-Engineer |
| 6a | smaller version | Earned crates, the chance list, one pet slot and a pet that follows. Then worker slots, fusing and last the Robux crate | M | Gameplay-Engineer |
| 7 | Cat Index | About 12 customer coats on day one, the special visitors' page, card pictures per dirt level | M | Gameplay-Engineer, Model-Agent |
| 8 | Builds and Finish now | One short station build, one long build, the skip button with prices by time left | M | Gameplay-Engineer |
| 9 | Quests and check in | Two daily and two weekly quests, the seven day card | M | Gameplay-Engineer, Design-Agent |
| 10 | Shop | Five passes, the starter pack with its server clock, three shop screens | M | Gameplay-Engineer, Design-Agent, Growth-Agent |
| 11 | Social | The visiting setting, the friend bonus, the gift stand | M | Gameplay-Engineer |
| 12 | First session | The timeline with its ask queue and one button at a time | M | Design-Agent, Gameplay-Engineer |
| 13 | Saving | Every new piece saved with a session lock, shaped for a later reopening | M | Gameplay-Engineer |
| 14 | Look, feel and sound | Bow tiers, gift stand and pet, crate, quest and shop art, soft and cosy effects, the sound batch | M | Model-Agent, Motion-FX-Agent |
| 15 | Numbers and checks | Events for each new piece, the store page, a review and a playtest of every pull request | S each | Growth-Agent, Review-QA-Agent |

The game is playtest worthy when a new player can run the whole first session on a phone, the data saves and Review-QA finds no blocker.

**Risks**
- A crowded first five minutes. Mitigation: the timeline keeps asks a minute apart and each sits behind its own switch, so the numbers show which one costs players.
- Cats that leave can upset young players. Mitigation: early heart bars are long, the first special visitor never rushes and nothing is sold to save a cat.
- Paid skips can weaken the day 2 reason to return. Mitigation: compare the day 2 return of players who skip with those who wait.
- Policy: the Robux crate is a paid random item. Mitigation: the chance list and the per player PolicyService check are built before it is sold.
- A like cannot be read by a game. Mitigation: the card checks the favourite and the group and never pretends to check the like.
- Ten step washes can drag. Mitigation: steps stay at about 5 seconds, no step repeats back to back and it is timed on the iPhone 12.
- Content volume: this is far more than the first draft. Mitigation: the build order gives a playable game after the first three rows.
- Technical: six spas on an old phone. Mitigation: six players a server and a test on the iPhone 12 before more is added to the street.
- Fun: cleaning games fade fast. Mitigation: the index, pets, workers, quests and events give more to chase than the cleaning.
- No proven numbers exist for hooks, waits or job length. Mitigation: choices ship behind switches and Roblox's own numbers decide.

**Out of scope for now:** trading, stealing, fighting, catching cats, friends as customers, coins for Robux, paid luck, a tool menu, stink wisps, Suds as a pet or a washer, a board of future like goals, the Grand Reopening and the Cat Show weekend. The last two are kept for later. Strays kept in a display window are replaced by pets from crates.

**Open questions for the owner** (none blocks the build; each has the version we build unless he says otherwise)
1. The free pet. He is looking into how other games check a like. Recommended: like and favourite asked together, with the favourite and the group checked.
2. Private servers. He wants them free with Roblox Plus or 100 Robux. Recommended: set what Roblox's setting allows once Growth-Agent has checked it.
3. Workers and bows. Recommended, from his note: workers tie no bow, so the bow bonus belongs to cats washed by hand.
4. The like ask at minute 7. Recommended: keep it there, since the special visitor's wash and crate sit at minute 5.

**Decision line:** `2026-11-25: Build Clean a Cat as a busy cat spa with a cat collection: pick the next cat from a bench, wash it by hand in 3 to 10 steps, reveal its coat for the Cat Index, hire workers and collect pets from crates. Why: it is the owner's own playstyle pick after nine playtests, joined to the one thing lasting games share, which is something to collect.`
