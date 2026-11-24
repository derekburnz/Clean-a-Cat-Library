---
name: art-and-models
description: Clean a Cat art style, Derek's feedback on mud, baths and store art, the draft models made in the 2026-11-24 deep dive and the review rules that came out of it
metadata:
  type: project
  modified: 2026-11-24T06:22:16.733Z
---

- Style since 2026-11-23 ET: Bubble Pastel (soft chunky shapes, flat colours, palette cream FFF6EC, mint A8E6CF, bubblegum FFB3C7, sky 8FD3FE, mud 5A4632). Model-Agent's pick, not yet confirmed by Derek.
- How models are made: Python generators in the game repo at assets/clean-a-cat/blender (pip bpy 5.2.4 in a cloud thread, no Blender app), exported as Part-built .model.json, no mesh uploads. Derek's library derekburnz/Roblox-Asset-Library (from Cat Cafe) is the source to port from: props yes, Cat Cafe characters never. Names, attachments and contracts for every model are in docs/art/style-guide.md, so read that, not this file.
- Review-QA merges Model-Agent PRs once both checks are green (Model-Agent pings them, no decision cards). Each batch needs a check sheet: two or three sides, a play camera frame, that frame at 667 px, 64 and 32 px tiles, part and triangle counts. They answer KEEP, FIX or DROP per model.
- Mud, Derek's words in order (2026-11-23 ET): balls = "random blobs"; raised rectangles = "dirt blocks"; thin smears = "not mud smeered put it almost like built into their fur or like coated in it". Now a coat of pieces that wrap the cat's own blocks, with drips past the jaw and belly and grey dust on dark fur. Limit: at phone size pale cats can still read as patterned, so Motion-FX's stink wisps carry the cue. Derek has not answered on the coat.
- Baths: deep blue water to just under the rim, white lather, clear bubbles. He rejected pale water under white foam ("missing water").
- Store art (Derek 2026-11-23 ET): chunky CLEAN A CAT title on a teal bubble backdrop, no mud; he wanted "the towel and stuff from the original ad picture in tub ... just blown up" (his Cat Cafe ad's bathtub), done as a store-art-only claw-foot bath. Finals in Model-Agent/store-art/final/. He liked a half dirty, half clean split picture. Detailed v2 waits for the design.
- Deep dive (Derek 2026-11-23 11 PM ET: draft the models very likely needed, quality over speed). Merged drafts, none wired: seven wash tools (shower, comb, tweezers, towel, clipper, hand dryer, shampoo), coin, star and coin stack, burr, leaf and twig, waiting bench, front desk, three helper kitten looks with bath caps, rare visitor's beret and shades, fluffy and golden brush, rain and golden shower, the visitor's framed star photo. Check sheets in Model-Agent/drafts-2026-11-24/.
- Rules Review-QA's checks produced: every tool tier changes shape or size as well as colour (tier 2 is lilac, tier 3 gold) and a tool icon must hold on the mint HUD panel; no tool body is mostly grey (grey only for metal tips); mud and debris stay off the eyes and face; staff must not look like a customer's cat (the helper wears a full mint smock); a thing under about 10 px at phone size needs a moving or marked cue from the game.
- Screen pictures: ui_renders.py then ui_compose.py in the blender folder render see-through cat portraits (512 px) and model icons (256 px) from the real models, plain and with an ink outline. Outputs in Model-Agent/ui-renders/ (66 pictures); Design-Agent uses the _ink versions only (Review-QA's call). A new model gets an icon by one line in ICONS.

See [[planning-status]].
