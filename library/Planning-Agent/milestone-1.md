# Clean a Cat: first milestone plan (2026-11-23 ET, Planning-Agent, status: draft)

This plan is built on [gdd-draft.md](gdd-draft.md), which is not locked until Derek's playtest notes are in. Stages 0 to 2 do not depend on any open question, so they can be built now. Stages 3 and 4 assume customers plus strays, which Derek has not confirmed. Issue numbers are from `derekburnz/Clean-a-Cat` on November 23, 2026. Every issue in the table is now open.

## The slice and its exit test
A brand new player on a phone scrubs a stray clean, keeps it, serves customers, buys Bubble Soap, builds the Brush Table and the dryer and starts the 8 hour VIP Room, all in under 10 minutes. They leave, come back and find their coins, cats and builds as the server left them. No blocker bugs. Nothing else is built until this passes.

## Build order
Sizes: S is under a day of agent work, M is 2 to 3 days. Nothing is L.

| Stage | What is built | Size | Owner | Needs | Issue |
|---|---|---|---|---|---|
| 0 | Game repo seeded from the starter, checks green | S | Gameplay-Engineer | Nothing | 1 |
| 1 | **Scrub and reveal.** One grey cat in a tub, 12 to 20 mud patches that vanish under a finger drag, the rest pops at 80% clean, the coat shows. Server owns the cat's state | M | Gameplay-Engineer | Stage 0, a placeholder cat | 27 |
| 1 | Scrub feel and reveal moment: bubbles, mud chunks, sparkle, shake off, sounds | S | Motion-FX-Agent | Moment signals | 3, 4, 6, 8 |
| 1 | Cat body, dirty look, tub and sponge | M | Model-Agent | Style guide | 10, 11, 12, 13 |
| **Gate** | **Is the scrub fun on a phone?** Derek plays it. If not, stop and rethink before anything else is built | | Derek, with Sync-Agent | Stage 1 | 29 |
| 2 | Brush, bow pick, before and after photo card, first coins | S | Gameplay-Engineer | Stage 1 | 30 |
| 2 | Brush, fluffed look and bows, with their effects | S | Model-Agent, Motion-FX-Agent | Stage 1 art | 7, 14 |
| 2 | Save shape: coins, stars, cats, tools, builds with end times, index. Each later stage adds its own fields | S | Gameplay-Engineer | Stage 0 | 31 |
| 3 | Customers: a door queue from a table of ten cats, need icons, give back for coins, tip and stars, first customer fixed as common | M | Gameplay-Engineer | Stage 2 | 32 |
| 3 | Chance board that reads the same table the server rolls from | S | Gameplay-Engineer | Customers | 33 |
| 3 | Tools board and Bubble Soap | S | Gameplay-Engineer | Coins | 34 |
| 3 | Customer figure, spa room with an open front, display window, door and board | M | Model-Agent | Style guide | 15, 16, 17 |
| 4 | Strays, display window with four cushions, tips online and away with a 1 hour jar | S | Gameplay-Engineer | Stage 3 | 35 |
| 4 | Cat Index with Washed and Resident stamps | S | Gameplay-Engineer | Stage 3 | 36 |
| 5 | Builds: station slot and room slot, timers that run while away, Brush Table, dryer and VIP Room, finish celebration | M | Gameplay-Engineer | Save shape | 37 |
| 5 | Dryer, Brush Table upgrade, builder kitten, building site curtain and sign | S | Model-Agent | Cat body | 18, 20, 21 |
| 6 | Screens: coin counter, need icons, photo card, index, builder window, phone first | M | Design-Agent, then Gameplay-Engineer | Spec | 9 |
| 6 | First session guide: tapped steps, goal line and long build offer behind three off switches | S | Design-Agent, then Gameplay-Engineer | Stages 1 to 5 | 5 |
| 6 | Bell button and one notification when the longest build finishes | S | Gameplay-Engineer | Builds | 38 |
| 6 | Funnel `onboarding_v1` and side events | S | Gameplay-Engineer, read by Growth-Agent | Stages 1 to 5 | 39 |
| 7 | Slice check: phone playtest, fresh and returning save, build timers across a rejoin and across a server change | S | Review-QA-Agent | Everything | 40 |

## The first issues
All opened on November 23, 2026. A is issue 27, B to G are 29 to 34, H is 15 to 17 (Model-Agent's), I to K are 35 to 37, L is 18, 20 and 21 (Model-Agent's) and M to O are 38 to 40.
- **A. Scrub and reveal on a phone with one grey cat** (gameplay). Done when a finger drag clears mud patches on a phone, the server decides when the cat is clean and the reveal fires the moment signals from issue 3. Safe to build before the design lock.
- **B. Owner playtest: is the scrub fun?** (qa, needs-owner). Done when Derek has played stage 1 on a phone and said keep or rethink.
- **C. Brush, bow and photo card** (gameplay). Done when three swipes fluff the cat, one tap picks a bow and the card pays the first 10 coins.
- **D. Save shape for the slice** (gameplay). Done when coins, stars, cats, tools, builds with end times and the index save and load, and the PR says what an old server does with the new save.
- **E. Customers at the door** (gameplay). Done when customers queue, hand over a cat with one to three needs and pay on return, with every request checked and rate limited. Waits on Derek's yes to customers plus strays.
- **F. Chance board** (gameplay). Done when the board shows the same chances the server rolls from, they sum to 100% and a test proves both read one table.
- **G. Tools board and Bubble Soap** (gameplay). Done when the soap can be bought once for 30 coins and widens the scrub.
- **H. Spa room, customer figure and window** (model). Done when the room has an open front with no closing door, a tub, a display window with four cushions, a door spot and a board.
- **I. Strays and the display window** (gameplay). Done when a stray arrives every few customers, moves into the window when clean and tips while online and away up to the 1 hour jar.
- **J. Cat Index** (gameplay). Done when each of the ten cats gets a Washed and a Resident stamp once and a full set pays its bonus once.
- **K. Builds with two slots** (gameplay). Done when a station and a room can build at the same time, end times are set by the server, a build finishes while the player is away and nothing is lost by coming back late.
- **L. Stations and builder kitten models** (model).
- **M. Bell button and build finished notification** (gameplay). Done when only a tap on the bell opens Roblox's opt-in prompt, one message a day at most is sent and players who cannot get messages see the come back line instead.
- **N. Funnel onboarding_v1** (gameplay). Done when each step in issue 5 fires once per save from the server with two fields at most.
- **O. Slice check** (qa). Done when the exit test above passes on a small phone.

Also needed, not as build issues: a tuning table at `docs/design/clean-a-cat/tuning.md` (Design-Agent, part of issue 5) and the maturity questionnaire answers written down before the first public test (Design-Agent or Growth-Agent, with Derek).

## Analytics from day one
The funnel is `onboarding_v1`, fired by the server once per save: `joined`, `loaded`, `first_scrub`, `first_reveal`, `first_photo`, `first_customer`, `first_return`, `upgrade_1`, `first_build`, `dryer_built`. Side events: `long_build_started`, `notify_opt_in`, `tutorial_hint`, `time_to_step` and `left_at`. Add `returned_day_2` with one field saying whether a long build was running when the player left. That one number tells us if the day 2 hook works. If the steps ever change, the funnel gets a new name.

## What to read first once real players arrive
1. Share who leave before `first_scrub` (loading) and before `first_reveal` (the scrub itself).
2. Share who leave between 61 and 180 seconds, against `first_customer` and `upgrade_1`.
3. Share of players who reach `long_build_started`, and day 2 return with and without it.

## What changes if the playtests change the plan
- If rival games hand over pets in a better way than customers at the door, stages 3 and 4 change and stages 0 to 2, 5 and 6 stay as they are.
- If washing by hand feels like a chore in the rival games, the gate after stage 1 is where we find out for our own game. Fix the scrub before building more.
- If Derek wants paid skips or a different longest build, only the numbers in stage 5 change.

## Before the first public test (Derek's account steps)
Roblox shows a new game only to age-checked players of 16 and over until it passes the Kids and Select evaluation. That needs the full maturity questionnaire with a Minimal or Mild result, an age-checked and verified creator account with 2-step verification, a one-time refundable fee per game or an active Plus or Premium subscription and 100 unique plays from highly engaged players within 60 days. Read on Roblox's Kids and Select page on November 23, 2026. Check the page again before acting on it.
