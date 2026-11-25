# Milestone 1: the playtest worthy draft on dev (2026-11-25 ET, Planning-Agent)

Derek, 2026-11-25 6:24 PM ET: "any more planning options or good to draft entire playtest worthy game now and playtest in studio for bugs!" Planning is closed. This milestone is the whole agreed design as a draft in the dev place, checked in Studio for bugs, then handed to Derek to play on dev. Nothing goes to live without his word.

Design: `docs/design/clean-a-cat/gdd.md` in the game repo (pull request 505) and the Claude Doc "Clean a Cat: one page design" (https://claude.ai/artifact/DzvEnLeFKMnrALQf2BnwB4). His words: `playtest-notes.md`. Every answer: `plan-page-backups/answers-2026-11-25-1812ET-full.json`.

## Done when
A new player can run the whole first session on a phone in the dev place, the data saves across a rejoin, Review-QA finds no blocker and Derek has been told the draft is ready for him on dev.

## Build jobs (GitHub issues in derekburnz/Clean-a-Cat), in build order
| Order | Issue | Job | Lane |
|---|---|---|---|
| 1 | 506 | Dirt levels set the mud, the steps and the pay | Gameplay-Engineer |
| 2 | 507 | Heart bar while waiting, the early bonus and the pay formula | Gameplay-Engineer |
| 3 | 508 | Bow as the easy last step that pays, with bow upgrades (models 501, effects 7) | Gameplay-Engineer |
| 4 | 509 | Workers Jo and Sam with station, mode and progress bar (rename 487) | Gameplay-Engineer |
| 5 | 510 | Special visitors, the first one scripted with a crate | Gameplay-Engineer |
| 6a | 511 | Earned crates, the chance list and the first pet slot | Gameplay-Engineer |
| 6b | 512 | Worker pet slots, doubles and fusing into a star up | Gameplay-Engineer |
| 6c | 514 | The Robux crate with chances shown and PolicyService | Gameplay-Engineer |
| 7 | 524 | Cat Index with customer cat names and the special visitors' page | Gameplay-Engineer |
| 8 | 515 | Builds on a timer with a Finish now button | Gameplay-Engineer |
| 9a | 516 | Daily and weekly quests | Gameplay-Engineer |
| 9b | 517 | Seven day check in card and the tip jar | Gameplay-Engineer |
| 10a | 518 | Five game passes, Lou among them | Gameplay-Engineer |
| 10b | 519 | Starter pack with the real 72 hour countdown | Gameplay-Engineer |
| 11a | 520 | Walk in visits with an owner setting, and the friend bonus | Gameplay-Engineer |
| 11b | 521 | Gift stand: free pet for like, favourite and group (model 502) | Gameplay-Engineer |
| 12 | 522 | First session ask queue, one button at a time, landscape lock (spec 5) | Gameplay-Engineer, Design-Agent |
| 13 | 523 | Save every new piece, shaped for a later Grand Reopening | Gameplay-Engineer |
| any | 525 | Tuning pass: every number in tuning.md | Design-Agent |
| any | 526 | Screens: bench card, recap, workers, pets and crates, quests, check in, builder, shop, gift card, settings | Design-Agent |
| any | 527 | Models: crate, pets, more special cats, worker stations, icons (also 501, 502) | Model-Agent |
| any | 528 | Motion and effects for the new moments (also 4, 6, 7) | Motion-FX-Agent |
| any | 529 | Sounds: upload the first batch and add the new cues | Motion-FX-Agent |
| any | 530 | Events for each piece, maturity answers, private server check, the owner's settings list (also 500, 106) | Growth-Agent, Derek |
| each PR | 531 | Review, policy check of everything sold and the full first session playtest (also 40, 182) | Review-QA-Agent |

## Rules for the whole milestone
- Dev first. Every piece ships behind its own switch, off by default, on in dev. Live switches stay off until Derek says so.
- Server authority on every new remote. Visitors can never act in another player's spa.
- Nothing is sold in the dev place for real until Review-QA's policy check has passed; the Robux crate is built last.
- One feature per pull request, reviewed by someone other than its author.

## Still open, none blocks the build
1. The free pet: Derek is looking into how other games check a like. Built as like and favourite asked together, favourite and group checked.
2. Private servers: free with Roblox Plus or 100 Robux, once Growth-Agent has checked what the setting allows.
3. Workers tie no bow (our reading of his note).
4. The like ask sits at about minute 7, after the special visitor's crate.

## For Derek to do when the time comes
- Create the five game passes and the developer products on the group's game.
- Set the server size to six and the private server price.
- Play the draft on dev and say what to change.
