# Handoff for a fresh Planning-Agent (written November 23, 2026 ET by the outgoing Planning-Agent)

You are picking up planning for **Clean a Cat**, a Roblox game owned by Derek's Roblox group Creampuff Games. The earlier planning thread is being deleted, so everything you need is in this file and in the files it points to. Read this file first, then `gdd-draft.md`, then `playtest-list.md`. Read the rest only when a question needs it.

## Where things stand in one paragraph
The name is locked. The direction is agreed in outline: a hands-on cat spa where players clean dirty cats and upgrade the spa, with upgrades that take longer and longer so players come back. The one-page design is written as a draft and is **not locked**, because Derek wants to playtest the animal spa games on Roblox first. Nothing has been built. The next real event is Derek's playtest notes. When they arrive you update the draft, get his yes, write the first milestone plan and hand over to the coordinator.

## Decisions Derek has made (his words, relayed November 22 and 23, 2026 ET)
- **Name: Clean a Cat.** Locked November 23, chosen over Clean the Cat. Slug `clean-a-cat`. Game repo `derekburnz/Clean-a-Cat`. Do not reopen the name.
- **Cat Spaw is dropped everywhere.** Derek: "no need for cat spaw if kids play they probably wont get it anyways".
- **The game must have cats, and a cat spa is the direction.** A cat spa ad of his did well. He does not want ad numbers looked up. His earlier game Cat Cafe has no spa.
- **The goals.** A fun first 5 minutes so the bounce rate is very low when Home recommendations start, and a reason to come back on day 2. He handles day 7 himself with events.
- **The loop, in his words:** "running some sort of cat spa with upgrades we can make the later upgrades take longer times so that people come back for their upgrades being finished and then we can send notifications that upgrades done to also pull players back. Gameplay would be get a dirty cat ... you clean them in different ways and then return them to customers or put them on display or smth along those lines which gets you money and progresses index etc."
- **No catching.** How players get cats was left open by him, with one firm point: catching cats did poorly in his last game.
- **Playtests before the design is locked.** He will play the animal spa games himself and report what they do well and what to improve.

## What I recommended and Derek has not yet confirmed
These are in the draft as recommendations. Treat them as proposals until he says yes.
- **How players get cats:** customers bring dirty cats to the door (a board shows which cats can come and the chance of each), and now and then a stray turns up at the back door and stays in the display window. The coordinator's summary lists customers bringing cats as decided, but Derek's own message left the method open, so confirm it with the playtest notes.
- **Build timers:** tools are instant, then 10 seconds, 1 minute, 10 minutes, 1 hour, an 8 hour build offered in the first session and 12 to 24 hours at most later. One build at a time and the spa never closes during a build.
- **No paid skips at launch.** A Second Builder game pass instead.
- **Notifications:** one a day at most, when the longest build finishes. Roblox only lets players aged 13 and over opt in to personal notifications, so for younger players the pull has to be shown in the game before they leave.
- **Day 7:** a Cat Show weekend as Derek's first event. Out of scope for the first build.

## What waits on Derek
1. **Playtest notes.** The list is in `playtest-list.md`, best first: Capybara Onsen, My Pet Salon!, Save a Horse: Wash & Collect. The first question for each game is how it hands the player a pet.
2. **Yes or no on customers plus strays** as the way to get cats. Recommended: yes.
3. **Paid skips for build timers.** Recommended: not at launch.
4. **Longest build time.** Recommended: 24 hours at most.
5. **Should the words cat spa go in the description and on the icon?** Recommended: yes.

Do not wait in silence for these. The project rule is to go with the recommendation and keep working. Only the design lock itself waits for his playtests, because he asked for that.

## Next steps, in order
1. When the playtest notes arrive, fold them into `gdd-draft.md`: how rivals hand over a pet, whether washing is by hand, how waits feel and the real timings of their first minutes. Change the first session timeline if the notes show a faster or better start.
2. Ask Derek to agree the design. Put the open questions in one short message, each with the recommended answer.
3. Write `milestone-1.md` in this folder: the vertical slice, systems in build order with sizes and owners, the first issues for the coordinator to open and the analytics steps. The scope table and build order in `gdd-draft.md` are the starting point.
4. Tell the coordinator the design is agreed, the name (Clean a Cat), the slug (`clean-a-cat`) and where the two files are. The design then moves to `docs/design/clean-a-cat/gdd.md` in `derekburnz/Clean-a-Cat` and Design-Agent keeps it from there. Then stop.

## Checks done and checks still owed
- **Name check, done November 23.** Roblox's own search showed no game named Clean a Cat. A web search found no game or app with the name. The nearest trademark records are CLEAN CAT for cleaning cloths (registered), kitty litter boxes (dead) and a degreaser (dead), none for games. This was a web search of public listings, not a search of the trademark office's database and not legal advice. A tiny Roblox game called Wash a Cat exists (1 player on November 23). Clean the Cat was never searched.
- **Still owed: the maturity label.** The design keeps the spa an open shop floor where only cats are bathed, with no private rooms for avatars. Check it against Roblox's maturity questionnaire before launch (the `roblox-policy-compliance` skill).
- **Still owed: copying this folder into the library repo** (`library/Planning-Agent/` in `derekburnz/roblox-game`). The outgoing thread could not reach that repo. The shared folder is the source of truth until that is done.

## Files in this folder
| File | What it holds | State |
|---|---|---|
| `gdd-draft.md` | The one-page design: hook, loop, how cats arrive, cleaning steps, first session by the second, build time table, economy, notifications, monetization, prototype scope with owners, risks | Draft. Update this file, do not start a new one |
| `playtest-list.md` | Games for Derek to play, with links, and the nine things to note per game | Sent to Derek |
| `cat-spa-concepts.md` | Why the name was chosen, the six options for how players get cats, what the research means, the first 5 minutes table, day 2 hooks | Current |
| `idea-shortlist.md` | The earlier three idea pitch | Superseded by the cat spa direction. Kept for the record |
| `Idea-Research/Roblox spa games and first minutes.md` | The main research report: spa, salon and animal care games on Roblox, first minutes of the hits, day 1 benchmarks, spa games outside Roblox | Reference |
| `Idea-Research/Roblox cat game opportunities.md` | The first research report: cat games, rising game types | Reference |
| `Idea-Research/name-check-2026-11-22.md` | Roblox search results for every name considered, today's naming patterns and the name check on Clean a Cat | Done |
| `Idea-Research/roblox-snapshot-2026-11.md` | Chart snapshot from November 2026 | Reference |
| `Idea-Research/cat-deep-dive-notes/` and `Idea-Research/spa-research-notes/` | Raw researcher notes with sources behind the two reports | Reference only |
| `Planning Agent.md` | Your role file | Read section 0 first |

## The findings that shaped the design (so you can defend it)
- Slow spa and salon tycoons stay small on Roblox (peaks of about 800 to 3K players even at 87 to 94% liked). So the game is hands-on washing, not placing stations and waiting.
- Cleaning games are well liked (92 to 93%) but fell to 1 to 2% of their peak within months, and new cat hits fell 88 to 95% in 7 to 10 weeks. So builds, the display window and the index start in the first session.
- The hits put an item in the player's hand at spawn, give a base inside a minute, use arrows and one goal, sell a very cheap first upgrade and then raise prices about 5 to 27 times per step.
- Day 2 hooks in the hits are things that finish while the player is away (Grow a Garden, Steal An Egg, Throw Food For Animals).
- Roblox Home counts players who leave in under 60 seconds and at 61 to 180 seconds, and since June 15, 2026 ranks on 28 day retention. Gameplay video autoplays on Home since July 29, 2026. A muddy cat turning fluffy is the clip.
- Roblox publishes no good day 1 number. Our target is 15% or better, from outside benchmarks.
- No source gives second by second timings for any game's first minutes, and no source proves that offline timers raise day 1 return. That is why Derek's playtests matter.

## How to work with Derek
- He reads the coordinator's summaries, so lead every reply with the answer in plain words and keep it short.
- No emojis, no dashes and no Oxford commas. Lists only when he asks. Give options as plain text with a recommended pick. Times in Eastern.
- Recommend and let him say no. Do not send him a list of questions.
- He can playtest Roblox games. You cannot, so say so and hand him a list.
- Game rules: original names and art only, chances always shown, no dark patterns, young audience by default.

## How to research Roblox from a cloud thread
Plain curl to Roblox domains is blocked. The web fetch helper can read Roblox's search at `https://apis.roblox.com/search-api/omni-search?searchQuery=TERM&sessionId=1&pageType=all`, which gives live players, votes and root place ids for 40 results and rate limits after about a dozen calls in a burst. A game's link is `https://www.roblox.com/games/ROOTPLACEID`. For history use the trackers: rolimons, rowatcher, rotrends, rostats, rblxdb, bloxodes and statroblox. Web search returns only links, so fetch the pages. Research helpers run on Sonnet 5.5 per `Idea-Research/Idea Research.md`.
