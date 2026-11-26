---
name: art-and-models
description: Clean a Cat art style, Derek's feedback on mud, baths, store art and the spa staff (Jo, Sam, Lou) and the review rules
metadata:
  type: project
  modified: 2026-11-26T16:12:44.380Z
---

- Style since 2026-11-23 ET: Bubble Pastel (soft chunky shapes, flat colours). APPROVED by Derek 2026-11-25 6:09 PM ET with the design lock, along with the human builder in overalls, the mud coat and the deep blue baths.
- Models: Python generators in the game repo at assets/clean-a-cat/blender (pip bpy), exported as Part-built .model.json, no mesh uploads. Derek's library derekburnz/Roblox-Asset-Library is the source to port from: props yes, Cat Cafe characters never. Names and contracts are in docs/art/style-guide.md: read that, not this file.
- Review-QA merges Model-Agent PRs once both checks are green (Model-Agent pings them, no decision cards). Each batch needs a check sheet: sides, a play camera frame, 64 and 32 px tiles, counts.
- Mud (Derek 2026-11-23): not blobs, blocks or smears: "almost like built into their fur or like coated in it". 2026-11-25: "none of stink wisps, dirt is fine make it darker if needed". So no wisps ever, darker mud only where needed.
- Baths: deep blue solid water to just under the rim, white lather, clear bubbles. The game tub is the store picture's claw-foot bath; its upgrade is the pink bubble bath.
- Store art: see [[store-art]]. Cat faces, bows and counter carriers (Derek 2026-11-26): see [[cat-faces-and-bows]].
- Rules from Review-QA's checks: every tool tier changes shape or size as well as colour; no tool body is mostly grey; mud and debris stay off the eyes and face; staff must not look like a customer's cat; a thing under about 10 px at phone size needs a cue from the game.
- Screen pictures: ui_renders.py then ui_compose.py render cat portraits (512 px) and model icons (256 px) from the real models; Design-Agent uses the _ink versions only. HUD button pictures: see [[ui-icons]], ink #45226B.
- Human staff: Derek 2026-11-24: people wash, Suds stays mascot and does not help. Jo, Sam and Lou (spa_staff.py): mint uniform, cream apron with a pink paw. Derek 2026-11-25: "spa staff looks good for now". Only staff wear mint bodies.
- From the 2026-11-25 lock: Derek on cat bodies: "can re-use and I would suggest some models for customer variants or cat models etc but make sure they fit this game and tweak where needed". Never write "working cats" or "working names" to Derek: say customer cats and draft names. Milestone 1 model list: [[milestone-1-models]].

See [[model-qa-checks]], [[planning-status]].
