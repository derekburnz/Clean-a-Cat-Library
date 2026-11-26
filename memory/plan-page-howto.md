---
name: plan-page-howto
description: How Planning-Agent reads, rebuilds, tests and republishes Derek's plan page and edits the one page design doc; database ids; lessons learned
metadata:
  type: reference
---

Full version: Planning-Agent/plan-page-howto.md in the shared files (and library/Planning-Agent/ in Clean-a-Cat-Library). Short version:

- Page: https://claude.ai/artifact/QVD8oT37EZy9vE8mYz9KfG. Publish with the Artifact tool and ALWAYS pass this `url`, or a second page is made. Pictures go in `files` as `art2/<name>.jpg`; pictures left out of a publish are kept.
- Sources: Planning-Agent/plan-page-source/ (build_plan2.py, build_plan.py, art2/, shot9.js, seed-1126c.json). Build: `python3 build_plan2.py clean-a-cat-launch-plan.html pre-development-plan.md`. Test: `node shot9.js $PWD/clean-a-cat-launch-plan.html $PWD/seed-1126c.json` and look at the phone screenshots.
- In the generator: QUESTIONS (option 0 is always our pick, "Something else" last, new groups on top), SETUP (steps only Derek can do), TODAY (what he decided, newest first), PARKED, PAGE (lede and steps).
- Database: ArtifactData, collection `answers`. `q2-<id>` has pick (option index as a string) and note; `c-s2-<id>` setup steps have done and note (he pastes pass and product ids there; never keys); `c-done2` is the done tick. Query `at` greater than your last read before EVERY republish.
- When he answers: save his words verbatim (Planning-Agent/playtest-notes.md and the day's open-questions file), update memory, tell the owning thread, change the design if needed, then republish.
- Design in two copies that must match: docs/design/clean-a-cat/gdd.md in the game repo (issue first, then a PR with "Closes", Review-QA pass, auto-merge, one line in docs/decisions.md) and the Claude Doc https://claude.ai/artifact/DzvEnLeFKMnrALQf2BnwB4 (doc id 6943de1e-b6b2-4c48-9355-1d496dc5e127, body node dad95f8f-a3a1; edit calls are in the full version).

Lessons: never publish over answers you have not read; never say an answer is saved without reading the database; check the clock with `date -u` (ET is UTC minus 5 in November); pictures must read on a phone; only true numbers; say when our pick is a judgment and not a Roblox rule; no rival screenshots in art2/ or the library; a docs only PR fails when main itself is red, so check main first.

**How to apply:** read this before touching the page. State of the page: [[planning-status]]. His answers: [[derek-nov26-answers]], [[derek-plan-answers]], [[derek-money-answers]], [[derek-evening-answers]].
