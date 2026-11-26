# Planning-Agent handoff (written 2026-11-26 3:30 PM ET)

Derek is deleting every thread and making them again for fresh context. You are the new Planning-Agent. Everything the old thread knew is in this folder, in project memory and in the two links below. Read this file, then `plan-page-howto.md`, then memory `planning-status` and `derek-nov26-answers`.

## Your job now

Planning closed on 2026-11-25 and the game is in BUILD. Planning-Agent no longer designs the game. It keeps three things true and current:

1. **Derek's plan page.** Every question that needs him goes there with our pick first, and every setup step only he can do. Link: https://claude.ai/artifact/QVD8oT37EZy9vE8mYz9KfG. How to read and republish it: `plan-page-howto.md`.
2. **The one page design**, in two copies that must match: `docs/design/clean-a-cat/gdd.md` in the game repo `derekburnz/Clean-a-Cat` and the Claude Doc https://claude.ai/artifact/DzvEnLeFKMnrALQf2BnwB4. A copy of the repo file is `gdd.md` in this folder.
3. **His answers.** Saved verbatim, passed to the thread that owns each one and folded into the design.

The coordinator sends you Derek's words and gathers asks from the other threads. You write no game code.

## State on 2026-11-26 3:25 PM ET

- Plan page version 53: 78 questions, 76 answered, 2 open. If he leaves one, our pick stands.
- **Open question 1:** `q2-headbows`, bows on the ten special cats that wear a head piece. Our pick (option 0): a smaller bow on those ten. Option 1: no bow on them. Option 2: leave them. The coordinator also asked him this in the chat at about 3:20 PM ET, so the answer may come there. Owner of the answer: Model-Agent.
- **Open question 2:** `q2-notifylive`, when to set up notifications on the live game. Our pick: on the day he promotes, by our workflow. Owner of the answer: Gameplay-Engineer.
- Store art: the six files in `Model-Agent/store-art/picked-2026-11-26/` are final and passed by Review-QA. The page tells him they are safe to upload. He drags them in himself.
- **Setup steps still his** (page database `c-s2-...`): passes on the dev game, products on the dev game (no ids pasted yet), maturity questionnaire, server size six, private servers 100 Robux, group wall off or moderated, store art (he drags the files in himself) and the dev playtest of the 2026-11-26 pieces with the three scrub questions. Ticked: computer use for Studio.
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
