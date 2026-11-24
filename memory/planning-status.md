---
name: planning-status
description: Where planning for Clean a Cat stands - name locked; cat spa; loops B and D proposed; plan page round two (40 questions) waits on Derek's playtests and picks
metadata:
  type: project
  modified: 2026-11-24T13:04:49.163Z
---

Derek's decisions so far (his own words, 2026-11-22 and 11-23 ET):
- The game must include cats. A cat spa is the direction (a cat spa ad of his did well; Cat Cafe has no spa).
- Goal: a fun first 5 minutes for a very low bounce rate off Home recommendations and a strong reason to return on day 2. He handles day 7 himself with events.
- Loop he wants: get a dirty cat, clean it, return it or put it on display for money and index progress. Later upgrades take longer so players come back. Catching cats did poorly in his last game.
- Name LOCKED 2026-11-23 ET: Clean a Cat, slug clean-a-cat. Cat Spaw is dropped.

Proposed to Derek, NOT yet agreed: loops B and D together. B = cat collector (hidden coat revealed by the wash, index, strays stay and earn, Grand Reopening reset, friend bonus). D = Derek's busy spa (pick the next cat from a bench, coin-bought slow helpers for common cats, rare visitors by spa stars, grumpy but never lost cats, 4 to 6 short varied steps, a star recap). Write-up: doc "Clean a Cat: loop options" https://claude.ai/artifact/8NLjC3vdU8tZ34AbGvfjit (short copy Planning-Agent/loop-options.md; research in Planning-Agent/Idea-Research/). See [[derek-playtest-notes]]. gdd-draft.md is unchanged until he answers.

Derek's plan page: https://claude.ai/artifact/QVD8oT37EZy9vE8mYz9KfG. Round two published 2026-11-24 8:30 AM ET at the same link, at his ask:
- Playtests still to do: Save a Horse, Clean Everything, Restaurant Tycoon 3, Barber Simulator, plus six optional.
- Six open jobs for him: confirm the ruleset on main, turn on Studio API access in the dev copy, read the loop doc, look at the 14 draft screens, name his test devices, then play our scrub on his phone (issue 29) after the playtests.
- 40 questions rewritten from his feedback, our pick first. The first eight decide the game. They also carry the open calls: recap full card or slim strip, HUD buttons one at a time, mud coat, stink wisps, baths, store icon and thumbnail, a half dirty half clean thumbnail.
- Parked until the game is picked, do not ask before then: server size, maturity questionnaire, 100 plays, build notification, store art v2, sound uploads, Plus, private repos.
- His answers save in the page database, collection `answers`: `p-<game>`, `c-<todo>`, `q2-<question>` (pick is the option index, 0 is our pick). Round one `q-` docs were all parked on "Something else" and are replaced. Read with the ArtifactData tool.
- File copy with every id: Planning-Agent/pre-development-plan.md. Round one record: Planning-Agent/plan-page-round-one.md. Generator: Planning-Agent/plan-page-source/build_plan2.py (needs build_plan.py beside it and the pictures in art2/).

Pace numbers agreed with Design-Agent on issue 5 (common cat 10 coins plus tip 2 and so on) are in docs/design/clean-a-cat/tuning.md; Design-Agent owns them. 14 draft UI screens merged in PR 121 (Design-Agent/ui-screens-2026-11-24/). The helper kitten is Suds; Pip is a customer.

A fresh Planning-Agent starts from Planning-Agent/handoff.md. Other files there: gdd-draft.md, milestone-1.md (draft), playtest-list.md, cat-spa-concepts.md, playtest-notes.md. The folder is copied to library/Planning-Agent/ in derekburnz/Clean-a-Cat-Library (public, no secrets).

Next: read his round two answers, fold them and the playtest notes into gdd-draft.md, ask for the design lock, finish milestone-1.md, hand over to the coordinator.

See [[project-setup]], [[roblox-age-rules]], [[art-and-models]] and [[roblox-research-howto]].
