# Clean a Cat: proposed design  (2026-11-24 ET, Planning-Agent, status: PROPOSAL, not agreed)

This is what the one-page design becomes if Derek takes our pick on every question of his plan page, round two (`pre-development-plan.md`). It is written ahead so no time is lost after his answers. **Nothing here is decided. Other threads keep building from `gdd-draft.md` until Derek says yes.** Each line that differs from the draft is marked (new) or (changed). Question ids in brackets point to the plan page. Research: `loop-options.md`. Derek's notes: `playtest-notes.md`.

**Hook (one sentence):** dirty cats line up at your spa, you pick who is next and scrub each one by hand to find out what coat is hiding under the mud.

**Name and first minute:** the name says Clean a Cat, so a new player is scrubbing a cat within 3 seconds of spawning. No cutscene and no story first [firstminute].

**Core loop**
- Every 30 to 60 seconds: pick a cat from the bench, wash it in 4 to 6 short steps and get coins, a tip and stars, which buy tools, helpers and stations. (changed: a pick and several steps)
- Every session (aim for 20 minutes or more): wash about 12 cats, reveal new coats for the Cat Index, keep a stray for the window, hire or speed up a helper and start a build before leaving. (changed: was 10 to 15 minutes)
- Every week: a different visitor cat each day, rare visitors unlocked by spa stars, new coats on a fixed day and Derek's events.

**How players get cats** [keep]
- Customers bring cats and take them home. Every coat revealed fills a slot in the Cat Index.
- Now and then a stray waits at the back door. A washed stray stays in the display window and earns tips. The very first cat is a stray.
- The coat is hidden under the mud until the wash is done. (new) The chance of each coat is on a board, cats are free and nothing sold changes the chances.
- No catching, no buying cats and no trading [trading].

**The bench: who is next** (new) [queue, impatience]
- Three or four cats wait, each with a card: name, how dirty, what kind of dirt and what it pays.
- Cats differ so the pick matters: a muddier cat pays more and a fussy cat tips more but waits less.
- A waiting cat gets grumpy and only its bonus tip shrinks. A cat that waits far too long goes home and comes back later. Nothing is ever lost.

**Helpers** (new) [helpers, helperlook]
- Bought with coins and never with Robux. A helper takes a common cat from the bench, washes it slowly and earns fewer stars than the player would.
- Rare cats and strays always wait for the player.
- Helpers are human staff in spa aprons, not cats. They reuse the customer figures the game already builds. Suds the kitten stays as the spa's mascot, who points things out in the first minutes and cheers but never washes. (changed 2026-11-24: Derek's lean, "helpers are likely going to be staff like humans", then his "ok" in the project chat to staff plus Suds as mascot. Plan page question `helperlook`, saved as option 1.) Whether the builder kitten for stations becomes a person too is still open.

**The wash** (changed) [steps, joblength, turn, praise, tools]
- Four kinds of step at launch: scrub the mud, rinse with the shower, pick burrs out of the fur and towel dry. Later tools add nail trim, comb, shampoo and the dryer.
- Each cat takes 4 to 6 steps of 8 to 15 seconds and never the same step twice in a row. A Step 2 of 4 line shows progress.
- The cat holds still during a step. The game turns it between steps and two buttons let the player turn it.
- Praise words name what the player did. A combo count pauses on a slip and does not reset.
- Tool upgrades change shape and feel as well as speed: a wider sponge, a fan spray, a comb that shows hidden burrs.

**After each cat** (new) [recap]: a recap with stars, coins and the tip. Three stars is normal and a hidden fourth marks a perfect wash. The full card shows for the first cats and for any new or rare cat, a slim strip for the rest.

**Rare visitors** (new) [rare]: unlocked as the spa earns stars. A rare visitor brings a rare cat and wants a near perfect wash, with the same short job as any cat. A finished visit gives a lasting reward, for example a small permanent tip bonus and a framed photo for the wall. Chances are on the board and no visitor can be bought.

**First session** (brand new player, phone; times are targets to test)
- 0:00 Spawn beside the tub. A muddy stray is in it. One arrow says Scrub.
- 0:15 The mud is gone. Rinse, then towel dry: three short steps for the first cat.
- 0:45 The coat is revealed with a New cat card. The stray hops into the window and is yours.
- 1:00 Two customers arrive and the bench shows two cards. The player picks one.
- 2:00 First tool upgrade, instant.
- 3:00 to 5:00 A third kind of dirt appears (burrs). The Index button pops in after the first customer cat, the Tools button at the first upgrade [hud].
- About 6:00 First station build, seconds long.
- About 10:00 The first helper can be hired. A third and fourth cat wait on the bench.
- About 15:00 The first long build is offered (hours), on its own slot [longbuild].
- No like or favourite ask, no shop prompt and no window that opens by itself in this session [favourite]. Tutorial steps are tapped by the player and ship behind an off switch.

**Progression:** tools (instant), stations (seconds to 1 hour), helpers (coins), rooms (hours, 24 at most, offered after about minute 15), rare visitors (spa stars), then a Grand Reopening: move to a bigger spa, keep every cat and gain a permanent tip bonus [reopen]. The Grand Reopening is built after the first test, but the save data allows for it from the start. No paid skips on any timer [skips].

**Economy**
- Sources: coins, tips and stars per cat, tips from window cats, index bonuses and a small bonus per friend in the server.
- Sinks: tools, helpers and their speed, stations, rooms and decor.
- The one pace number stays cats washed to afford the next purchase. The numbers in `docs/design/clean-a-cat/tuning.md` were set for a single 8 second scrub. With a job of about a minute they all need a new pass by Design-Agent once the job length is timed on a phone.
- Guard rail: helpers and window cats together earn less than the player's own washing at the same stage, so washing by hand stays the best way to earn.

**Reason to come back tomorrow** (changed) [return]: empty slots in the index, a tip jar that fills while away and stops at a cap and one different visitor cat each day. No streak and nothing lost by missing a day. A bell for finished builds stays as a small extra for players of 13 and over, who are the only ones Roblox lets us notify.

**Social** [friends, visit]: spas sit side by side on one street. Players see each other's windows and reveals but do not walk in at launch. Each friend in the server adds 10% to tips, shown on screen from the start. Not in: stealing, trading, fighting and typed text.

**Monetization** (follows monetization-policy) [passes]: three game passes at launch: 2x Coins, Second Builder and Golden Sponge. Coins, helpers, rare visitors and cats are never sold, so nothing random is ever paid for. PolicyService is fetched per player from day one.

**Prototype scope: what changes against the draft's table**
| System | Smallest version | Size | Owner |
|---|---|---|---|
| Wash steps | Scrub exists. Add rinse, burr pick and towel dry, a step counter and the turn between steps | M | Gameplay-Engineer |
| Bench and pick | Three waiting cats with cards, mood that only lowers the tip, go home and return | M | Gameplay-Engineer |
| Hidden coat and index | The coat is rolled by the server when the cat arrives and shown at the end of the wash | S | Gameplay-Engineer |
| Recap | Stars, coins and tip, full card and slim strip | S | Design-Agent then Gameplay-Engineer |
| One helper | One staff member washes one common cat at a time at a fixed slow speed | M | Gameplay-Engineer |
| Rare visitors | One visitor behind a star goal, after the first test | M, smaller version: none in the slice | Gameplay-Engineer |
| Day one content | About 12 coats, 3 kinds of dirt and 4 tools | M | Model-Agent |
| Analytics | Add: first pick from the bench, first helper hired, cats washed per session, session length | S | Growth-Agent |

Build order: the scrub on a phone first (issue 29). Then the other three steps, the bench, the reveal and index, the recap, one helper, builds and saving.

**Risks**
- Fading: five of the six cleaning games from this summer are at 3% of their peak or less. Mitigation: the collection, helpers and the Grand Reopening give more to chase than the cleaning.
- A longer job can bore: My Pet Salon's same swipe three times did. Mitigation: 4 to 6 short steps, never two alike in a row and Derek's phone test before more is built.
- Waiting pressure can upset young players. Mitigation: only a bonus tip shrinks and no cat is lost.
- Scope: this is more than the first draft. Mitigation: the slice is one helper, three bench seats, 12 coats and no rare visitor.
- No proof: no source gives a tested number for any hook, wait or job length. Mitigation: ship choices behind switches, run two versions and read Roblox's own numbers.
- Policy: the hidden coat is random. Mitigation: it is free, the chances are shown and coins cannot be bought. The spa keeps an open front and only cats are bathed.

**Out of scope for now:** trading, stealing, fighting, catching cats, paid luck, paid skips, buyable coins, typed cat names, rooms or tubs for avatars, walking into a neighbour's spa, more than one helper in the slice, the Cat Show event and any shared characters with Cat Cafe.

**Open questions for the owner:** the 41 on the plan page. The first nine decide the game.

**Proposed decision line:** `2026-11-24: Build Clean a Cat as a busy cat spa with a cat collection: pick the next cat from a bench, wash it by hand in a few short steps, reveal its hidden coat for the index and hire slow helpers. Why: it is Derek's own idea after My Pet Salon, joined to the one thing the lasting games share, which is something to collect.`
