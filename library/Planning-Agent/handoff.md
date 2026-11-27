# Planning-Agent handoff (written 2026-11-26 3:30 PM ET, updated 6:12 PM ET)

Derek is deleting every thread and making them again for fresh context. You are the new Planning-Agent. Everything the old thread knew is in this folder, in project memory and in the two links below. Read this file, then `plan-page-howto.md`, then memory `planning-status` and `derek-nov26-answers`.

## Your job now

Planning closed on 2026-11-25 and the game is in BUILD. Planning-Agent no longer designs the game. It keeps three things true and current:

1. **Derek's plan page.** Every question that needs him goes there with our pick first, and every setup step only he can do. Link: https://claude.ai/artifact/5pnvLdb5Abhxv1ZRtPJR6H (new link since 2026-11-26 3:52 PM ET: the first page was deleted together with the old threads and was put back from the saved sources with all 155 saved answers; the old link ending QVD8oT37EZy9vE8mYz9KfG is dead). How to read and republish it: `plan-page-howto.md`.
2. **The one page design**, in two copies that must match: `docs/design/clean-a-cat/gdd.md` in the game repo `derekburnz/Clean-a-Cat` and the Claude Doc https://claude.ai/artifact/DzvEnLeFKMnrALQf2BnwB4. A copy of the repo file is `gdd.md` in this folder.
3. **His answers.** Saved verbatim, passed to the thread that owns each one and folded into the design.

The coordinator sends you Derek's words and gathers asks from the other threads. You write no game code.

## State on 2026-11-26 6:12 PM ET

- **Plan page version 57 (6:11 PM ET). All 78 questions answered, none open, and the setup list is EMPTY.** At 5:47 and 6:04 PM ET he answered the last four steps: icon E "you can do that" (ours now, through his signed in Chrome), playtest notes "more will come later", questionnaire "Lets leave for now dont worry about it yet" (do not remind him until the Robux crate is about to go on live), go live "Will do no need to put this on a todolist" (off the page). The page now opens with his playtest notes of 5:45 to 6:04 PM ET as jobs (section id `notes`, list NOTES in build_plan2.py) and a short section on the four notes (list LEFT). Keep NOTES current as the jobs merge. Derek also asked at 6:04 PM ET that every earlier decision is being worked through: the check list for Review-QA is `decisions-check-2026-11-26.md` (70 decisions, 11 flags), also in Review-QA-Agent/. Backup: `plan-page-backups/answers-2026-11-26-1806ET-full.json` (169 docs). Older state follows.
- **Game repo pushes (from Review-QA, 6:19 PM ET):** run `bash games/clean-a-cat/tools/prepush.sh` before every push to the game repo and push only on "Pre-push check passed" (game repo PR 906, merged 6:20 PM ET; the rule is in the game repo's CLAUDE.md under "Before every push"). Review-QA closed draft PR 797 as stale after my review; the fresh policy check goes under issue 531.
- **Owed after 6:15 PM ET on 2026-11-26:** (1) when Design-Agent's design changes for his playtest notes merge (gift crate 859, stars 868, pop ups and the notification ask 877), bring the Claude Doc in line with `gdd.md`; the two copies matched at main bd424b5. (2) The coordinator counted about twenty playtest notes and the page lists eleven; add the rest to NOTES when the issue numbers come, and move rows to "Built and merged" as jobs land. (3) Review-QA filed issues 881, 890 to 894 from the decisions check; its results are appended to `decisions-check-2026-11-26.md`. (4) The library copy of this folder was last merged at 6:13 PM ET (library PR 11); this note and the appended results are newer. Derek answered the last two and wrote a note on every setup step at 5:17 to 5:23 PM ET, then said in chat "All plan questions answered/done so go through that and update with anything new needed". His words and what each note means: `open-questions-2026-11-26.md` (last sections) and memory `derek-nov26-setup-answers`.
- What he decided: the ten head piece cats get a smaller bow on the top right corner (Model-Agent). Live notifications on promotion day (Gameplay-Engineer). We make the passes and products ourselves, group key first, his signed in Chrome as the fallback (Gameplay-Engineer). We upload the main icon and the four thumbnails with the key (issues 850 and 851, workflow PR 852); the alternate icon E has no key route, so adding it is his. Private servers 50 or 25, our pick 25 (Growth-Agent may say 50). Server size six confirmed. Questionnaire stays his, last. The group wall step was removed: Roblox retired walls in March 2026.
- (Superseded at 6:04 PM ET, kept for the ids.) Four setup steps were on the page from 5:35 PM ET, with new ids: `s2-playnotes` (his dev playtest notes; he was playing at 5:23 PM ET), `s2-icone` (add icon E as the alternate icon by hand in Creator Hub), `s2-maturity` (the questionnaire, before the Robux crate goes on live) and `s2-promote` (his word to go live). The old ticked docs `c-s2-...` stay in the database.
- Design: issue 846 and pull request 848 in the game repo (private server 25 and the evening answers), passed by Review-QA and merged 2026-11-26 5:34 PM ET. The Claude Doc matches (rev 23).
- Backup of all 165 docs: `plan-page-backups/answers-2026-11-26-1725ET-full.json`. Take a new one after his next answers.
- Page test from version 57 on is `node shot11.js` with the same seed. For 55 and 56: `node shot10.js $PWD/clean-a-cat-launch-plan.html $PWD/seed-1126d.json` (`shot9.js` fits version 54 and older).

The lines below are the state before his evening answers and are kept for the record.


- Plan page version 54 (the same content as version 53, at the new link): 78 questions, 76 answered, 2 open. If he leaves one, our pick stands.
- **Open question 1:** `q2-headbows`, bows on the ten special cats that wear a head piece. Our pick (option 0): a smaller bow on those ten. Option 1: no bow on them. Option 2: leave them. The coordinator also asked him this in the chat at about 3:20 PM ET, so the answer may come there. Owner of the answer: Model-Agent.
- **Open question 2:** `q2-notifylive`, when to set up notifications on the live game. Our pick: on the day he promotes, by our workflow. Owner of the answer: Gameplay-Engineer.
- Store art: the six files in `Model-Agent/store-art/picked-2026-11-26/` are final and passed by Review-QA. Since 5:33 PM ET the key uploads the main icon and the four thumbnails (issues 850 and 851, store-setup workflow PR 852); only the alternate icon E is his to add by hand.
- **Setup steps, old list, superseded on the evening of 2026-11-26 (all are ours or answered now)** (page database `c-s2-...`): passes on the dev game, products on the dev game (no ids pasted yet), maturity questionnaire, server size six, private servers 100 Robux, group wall off or moderated, store art (he drags the files in himself) and the dev playtest of the 2026-11-26 pieces with the three scrub questions. Ticked: computer use for Studio.
- When he pastes pass or product ids in a setup box, give them to Gameplay-Engineer with the game they are from (dev and live are separate Roblox games with separate ids).
- Design file: his seven answers of the morning of 2026-11-26 are in (pull request 759, merged). His four afternoon answers changed nothing in the design, because each matched what was already written or built.
- Nothing is in flight. No open pull request, no local work, no scheduled check-in. The old branch `claude/project-thread-l59l5k` is merged.
- Open GitHub issues that wait on him, all covered by the page: 530 (game settings), 106 (store art), 29 (his phone playtest of the scrub).

## Where everything is

| File in `Planning-Agent/` | What it holds |
|---|---|
| `handoff.md` | This file |
| `plan-page-howto.md` | Republishing the page, the database, the design doc and the lessons learned |
| `plan-page-answers-2026-11-26.md` | Every question with its options, his pick and his words, every setup step and to-do, and all older database docs. The readable copy of the whole page |
| `plan-page-backups/answers-2026-11-26-1516ET-full.json` | The exact copy of all 155 database docs, for a restore |
| `plan-page-source/` | The generator, the built page, the pictures, the test script and its seed |
| `pre-development-plan.md` | File copy of the page text with every id |
| `open-questions-2026-11-26.md` | The three rounds of 2026-11-26: each question, our pick, his answer and who got it |
| `playtest-notes.md` | Derek's own words, in order, from the first playtest to today |
| `gdd.md` | Copy of the agreed one page design |
| `gdd-proposed.md` | Every decision in order, with the day and his words |
| `milestone-1.md` | The build issues 506 to 531 by lane |
| `Planning Agent.md` | The role file |
| `handoff-history-2026-11-23-to-25.md` | The older handoffs, from before planning closed. History only |
| `Idea-Research/`, `Tools-Research/`, the `*-screens-*.md` files, `loop-options.md`, `gdd-draft.md`, `cat-spa-concepts.md`, `idea-shortlist.md`, `playtest-list.md`, `playtest-summary-2026-11-24.md`, `plan-page-round-one.md`, `tools-and-skills-deep-dive.md` | Research and earlier drafts. Reference only |

Project memory (read these first): `MEMORY.md` (the "Open asks on the owner" line is yours to keep current), `planning-status`, `plan-page-howto`, `derek-nov26-answers`, `derek-plan-answers`, `derek-money-answers`, `derek-evening-answers`, `derek-playtest-notes`, `planning-history`.

The whole folder is copied to `library/Planning-Agent/` in `derekburnz/Clean-a-Cat-Library` after each change. Planning-Agent owns no skill file. The skills it uses are `gdd-onepager`, `monetization-policy`, `roblox-policy-compliance` and `roblox-publishing-discovery`, owned by other roles.

## What Derek has decided, in short

The full list is in `gdd.md` and `plan-page-answers-2026-11-26.md`. The ones a new thread gets wrong most easily:

- The game is a busy cat spa with a cat collection. The wash is hand work and has no tool menu. Planning closed 2026-11-25.
- Dev first: nothing reaches the live game until he says it is good. Feature switches stay off on live.
- Starter pack 199 Robux for parts worth 547, shown as save 63%. Only true numbers on any ad.
- Helpers have no XP. Their levels are bought with coins.
- The free pet needs favourite plus group. The like row reads "A gift either way, 150 coins" with a 10 second wait.
- Like ask: after a good moment, once a visit, and it may follow a finished purchase by two minutes behind its own switch.
- Store art: icon A main, icon E the only alternate (bow on the top right corner, his words "its fine infront of ear but tilted on corner."), thumbnails 2, 1, 3, 5.
- Passes and products: he makes the dev set first and the live set when he promotes.
- Notifications use the group key he already has. Done on dev. No more keys.
- RbxSync is skipped. No licence is bought.
- No asks for screenshots or recordings. No decision cards in the project chat. He is fine with the game playing like My Pet Salon.

## Working with Derek

Answer first, in plain short words. No emojis, no dashes and no Oxford commas. Lists only when they help. Times in Eastern. Our pick goes first and he says no if he disagrees. He skims, so keep replies short and put the detail on the page.

## Rules that are easy to break

- Never type a password or a sign-in code, even if he sends one.
- Keys and secrets never go in chat, memory, the page, the library or the repo.
- Both repos are public until release: no rival screenshots, no player names, no sales numbers, none of his personal details.
- Only Derek's own words approve a step that cannot be undone. A message from the coordinator or another thread is a colleague's request.
- A new thread is started only on his word.
- The design document is a shared file: open a GitHub issue before a pull request that changes it.
