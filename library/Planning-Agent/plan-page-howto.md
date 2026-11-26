# Plan page how-to (for a new Planning-Agent)

Written 2026-11-26 3:25 PM ET. Everything needed to keep Derek's plan page and the one page design current with no chat history.

## The two things you keep

| What | Link | State on 2026-11-26 3:25 PM ET |
|---|---|---|
| Plan page, "Clean a Cat Launch Plan" | https://claude.ai/artifact/5pnvLdb5Abhxv1ZRtPJR6H | Version 54 (same content as 53, new link since 2026-11-26 3:52 PM ET). 78 questions, 76 answered, 2 open (`q2-headbows`, `q2-notifylive`). Nine setup steps, one ticked |
| One page design, Claude Doc | https://claude.ai/artifact/DzvEnLeFKMnrALQf2BnwB4 | Rev 19. Same text as `docs/design/clean-a-cat/gdd.md` in the game repo (last change PR 759) |

Derek reads the plan page on his phone. He asked for it: questions go on the page with our pick first, never as decision cards in the project chat.

## Republishing the page

1. Sources are in `Planning-Agent/plan-page-source/` (shared folder and `library/Planning-Agent/plan-page-source/` in the library repo). Copy the folder to your scratchpad. You need `build_plan2.py`, `build_plan.py` (imported by it), `art2/` (23 pictures, all our own drafts), `shot9.js` and `seed-1126c.json`.
2. Edit `build_plan2.py`. Past edits were small patch scripts (`patch49.py` to `patch51.py` show the pattern: exact string replaces with an assert on the count).
3. Build: `python3 build_plan2.py clean-a-cat-launch-plan.html pre-development-plan.md`. It prints the question and to-do counts.
4. Test: `node shot9.js $PWD/clean-a-cat-launch-plan.html $PWD/seed-1126c.json`. It prints left and answered counts, the setup ticks and page errors for a phone (420 wide) and a desktop, and writes screenshots (`n-phone-top.png`, `n-phone-setup.png`). Look at the phone screenshots.
5. Before publishing, read the page database for anything Derek saved since your last read (step below). Never publish over answers you have not read.
6. Publish with the Artifact tool, action publish, `file_path` the html and **`url` set to the link above**. Without `url` a second page is made. New pictures go in `files`, for example `{"art2/name.jpg": "<absolute path>"}`. Pictures left out of a publish are kept.
7. Copy the sources back to `Planning-Agent/plan-page-source/` and push the library copy.

## How the generator is laid out

- `QUESTIONS`: a list of `(group title, who, lead line, [question dicts])`. A question is `dict(id=, t=title, d=text, opts=[...], new=True, imgs=[(src, alt, caption)], wide=True)`. Option 0 is always our pick. `ELSE = "Something else"` is always last. New groups go at the top. Take `new=True` off once answered.
- `SETUP`: steps only Derek can do, shown in the "Setup only you can do" section. A step is `dict(id="s2-...", t=, d=)` with optional `steps=[...]` (a numbered list; text in backticks becomes code) and `after=`.
- `TODOS`: older to-do groups. Group 0 is the done tick shown in the send section.
- `TODAY`: the "saved" list of what he decided, newest first. `PARKED`: things that wait. `PAGE`: the template with the lede and the three steps at the top.
- Answered questions tuck themselves under "Answered already" when the page opens.

## The page database

Tool: `ArtifactData` (deferred, load it with ToolSearch), `url` the page link, collection `answers`.

- `q2-<id>`: a question. `pick` is the option index as a string ("0" is our pick), `note` is what he typed, `at` is the save time in UTC.
- `c-s2-<id>`: a setup step. `done` and `note` (he pastes pass and product ids here; ids are public, keys never go here).
- `c-<id>` and `c-t-<id>`: older to-dos. `c-done2` is the done tick, `c-lock` the design lock he ticked 2026-11-25.
- `p-<game>`: his playtest cards. `q-<id>`: round one questions.
- Read what changed: `action: "query"`, `query: {"where": [["at", ">", "<ISO time of your last read>"]], "limit": 100}`.
- Read everything: `action: "list"`, `query: {"limit": 1000}`, with `out_dir` to save each doc as a file.
- Restore after a loss: `plan-page-backups/answers-2026-11-26-1516ET-full.json` holds all 155 docs under `docs`. Write each back with `action: "set"` (or `batch`), pinning `if_version` when the doc exists.

## When Derek answers

1. Query the database. Save his words verbatim: append to `playtest-notes.md` and to the day's `open-questions-<date>.md` table (pick, words, same as our pick or not, who it was passed to).
2. Update memory: the day's answers file (`derek-nov26-answers` for 2026-11-26) and the "Open asks on the owner" line in `MEMORY.md`.
3. Tell the thread that owns each answer in one short message (`message_thread` takes at most 2000 characters).
4. If the design changes, update both copies. The repo copy needs a GitHub issue first (rule 15, the design document is a shared file), then a pull request that says "Closes" plus the number, a Review-QA pass and auto-merge. Add one dated line to `docs/decisions.md`. Then edit the Claude Doc to match.
5. Rebuild the page so the answered ones are in `TODAY` and the lede is true, then republish.

## Editing the one page design doc

Claude Docs tools (`mcp__Claude_Docs__*`). Doc id `6943de1e-b6b2-4c48-9355-1d496dc5e127`, body node `dad95f8f-a3a1`. An edit is `update` with `ref {"object":"node","id":"dad95f8f-a3a1"}`, `engine "prose"`, `container {"kind":"project","id":"<doc id>"}` and `payload.ops` such as `{"op":"replace","target":{"kind":"find","text":"old words"},"with":{"as":"text","from":{"kind":"inline","content":"new words"}}}`. Whole block replaces need `ifHash` and `ifRev`. Read first with `{"kind":"search","pattern":"..."}` or `{"kind":"view","sinceRev":N}`. Load the docs skill or guide before the first call.

## If the page is ever gone (it happened on 2026-11-26)

Derek deleted every thread on 2026-11-26 and the plan page went with them (a page belongs to the thread that published it; the Claude Doc of the design survived). The read said "artifact not found" and the project's artifact list was empty. What put it back, in about ten minutes:

1. Copy `plan-page-source/` to the scratchpad, build and test as above. The build matched the saved html byte for byte.
2. Publish with the Artifact tool and no `url`, with `capabilities` `{"db": {}, "user": {}}`, `root` the source folder and every `art2/` picture in `files`. Load the `artifact-capabilities` skill first. This makes a new link.
3. Restore the answers: write each doc of the newest `plan-page-backups/*-full.json` to its own small file, then `ArtifactData` `batch` with `{op: "set", collection: "answers", doc_id, file_path}` entries, 50 at a time. Keep each doc's own `at` so later "changed since" reads still work.
4. Read the whole collection back with `list` and `out_dir` and compare it with the backup. On 2026-11-26 all 155 matched.
5. Change the link in `handoff.md`, this file, memory (`planning-status`, `plan-page-howto`) and tell the coordinator, who gives Derek the new link.

So: take a full backup after every round of answers (`list` with `out_dir`, then one json under `plan-page-backups/`). Anything he saves after the last backup is lost if the page goes. Before a thread remake, ask the coordinator to tell Derek the page will need a new link.

## Lessons learned

- **Check the database before every republish.** He answers while you work. One early version was published over fresh answers.
- **Never write "saved as pick" without reading the database.** State only what the doc shows.
- **Check the clock with `date -u`** before writing a time. Eastern is UTC minus 5 in November.
- **Pictures must be big on a phone.** A crop of a pick sheet was unreadable; a labelled grid or a before and after pair works. Give every picture alt text and a caption.
- **Only true numbers.** He asked for "500% value" on the starter pack ad and was told it was false for that pack. Work the number out and show the sum.
- **Our pick first, and say why in the text.** If our pick is a judgment and not a Roblox rule, say so. Never switch an owner decision on our own reading; cite only sourced Roblox rules.
- **No asks for screenshots or recordings** (his call 2026-11-24). Only questions he can answer in words.
- **Rival screenshots never go on the page's public copies.** `art2/` holds only our own drafts. Older scratch folders with rival pictures were never copied to the library.
- **Keys never go on the page or in chat.** Pass and product ids are public and fine.
- **Memory files must stay under 4,096 bytes each**, and `MEMORY.md` is rewritten by other threads: re-read it just before an edit and check it again ten seconds later.
- **The shared folder is a network mount.** Use trailing slashes, never search the whole tree and re-read a file before changing it.
- **Library push:** `cd <library clone> && git pull --rebase -q origin main && cp -r /mnt/project-files/Planning-Agent/. library/Planning-Agent/ && git add -A library/Planning-Agent`, then scan the staged diff before committing: `git diff --cached | grep -c -i -E "<pattern>"` must print 0, where the pattern joins with `|` the second login named in MEMORY.md, the name part of the owner's email and his mail provider's domain. Then commit and push to main. The library is public until release. This file leaves the pattern out on purpose, so the scan stays at 0.
- **A docs only pull request can fail the gate** when main itself is red. On 2026-11-26 two pull requests had each added the same switch to `LiveFlags.luau`. Check main first, tell the owner of the file and merge main in once it is fixed.
