# Parked Studio checks, main b9c0008, 2026-11-25
Local unsaved place. iPhone 13 frame stands in for iPhone 12; iPad 10th gen. Switches dev-like with toolsBoard and builds on, toolCursor and strays off. Pictures: draft PR #455.
PROBLEMS
1. #435 foam puffs are hidden, not removed: all 6 puff models stay in the cat after popping, 48 parts at full transparency.
2. #7 fur puff never played: no furPuff emitter created during 6 real brush strokes that finished the step.
3. #443 bow buttons: invisible tap slabs overlap about 20 px vertically (Pink with Mint, Mint with Sky).
PASS / notes
- #429 step pill: Pick step pill 220x38 at top centre (x 265, y 6), chip "1 / 3" size 19, "Pick him up" size 26, both fit. Wash step pill 205x38, "2 / 3", "Wash him". Overlaps nothing (between Index/Settings and coins, above the cat). Ink on gold chip about 9:1. Gold ring parts in place (gold 5 px, ink edge 4 px, glow 8 px); gold vs ink edge about 9:1, gold alone on cream UI about 1.3:1, so the ink edge makes it read. No lit-button dim step came up, so no ring-on-button picture.
- #432 boards: Tools board at (-6, 3, -12), 6 studs left of the tub; Build board at (-18.1, 3, -4) by the VIP door; both face the room. Prompts on shelf rows and row cards; bell prompt by the bell; two built stations' prompts off. Titles "Tools" and "Builds" about 14 px tall on the phone, 30 px on iPad from 7 studs: readable but small on the phone. Build board row cards blank (as the PR says). Both tool shelf displays show while not owned (hide-when-bought not checked). Busy wall behind (door, mirror, frame); nothing clips.
- #435 foam: 6 puffs, 3 shapes in turn, each 0.77 to 1.10 studs, about 47 to 62 px wide on the phone; face out; float 0.2 to 0.5 studs off the fur, none buried. Real circular swirls (one unbroken press of about 12 studs of travel) popped all 6 and finished the step. Frame time unchanged (capped at 240).
- #443 bows (merged): round buttons with bows show, all three on screen (y 157 to 324 of 332); tapping Mint put the mint bow on the cat, hearts fired.
- Effects #4/#6/#7: foam rate follows drag speed, max 8 (phone cap holds), life 0.5 to 0.8 s. Mud chunks, sparkles, droplets fire on the pooled emitters (Emit, counts not readable). Bow hearts fire. Mud and brush finished with real drags on the phone frame.
- iPhone blur, wash scene (this PC, 240 cap): blur on 0.30: avg 240.0 fps, 1% low 147.1, worst 8.0 ms; blur off: 240.1 / 158.3 / 7.3 ms.
- #182 Studio figures during the wash on the phone frame (not the phone): 114 draw calls, 96,694 triangles, 73,528 instances; far under Roblox's example budget. Memory 2,886 MB is all of Studio, not a phone figure.
Console: no game errors (MemoryStore, DataStore lines; 3 "asset type does not match" for rbxassetid://203785492 at the opening).
