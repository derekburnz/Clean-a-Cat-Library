---
name: art-and-models
description: Clean a Cat art style (recommended, not yet confirmed by Derek), model list v1 issue numbers and how Blender runs in cloud threads
metadata:
  type: project
---

- Style in use since 2026-11-23 ET: Bubble Pastel (soft chunky shapes, flat colours, SmoothPlastic, palette cream FFF6EC, mint A8E6CF, bubblegum FFB3C7, sky 8FD3FE, mud 5A4632). Recommended by Model-Agent, not yet confirmed by Derek; alternates Cozy Storybook and Bright Toy.
- Model list v1: Model-Agent/model-list-v1.md in the shared folder. Model issues on derekburnz/Clean-a-Cat: #10 style guide, #11 cat body, #12 dirty look, #13 tub and sponge, #14 brush and bows, #15 spa plot, #16 customers and strays, #17 display window, #18 stations, #20 builder kitten, #21 VIP locked, #22 ten coats, #23 later stations, #24 store art (needs Derek's pick).
- Derek's asset library derekburnz/Roblox-Asset-Library (public, from Cat Cafe): reuse its Blender generator framework, the blocky chibi cat body and the Part-built .model.json export (no mesh uploads needed). New coats only; no Cat Cafe characters (design rule). Notes: Model-Agent/asset-library-reuse.md.
- Code prefix CleanACat (from issue #1). Asset names CleanACat_<Category>_<Name>.
- Blender in a cloud thread: no Blender app and blender.org is blocked, but pip install bpy==5.2.4 (Python 3.13) works for generator scripts and renders.

See [[planning-status]].
- Progress 2026-11-23 ET: merged #10 to #14, #15 graybox plot, #16 customers and props, #17 display window (PR #77). #18 stations merged (PR #83). #20 builder kitten merged (PR #89). #21 VIP looks merged (PR #93). #22 coat table, dusty mud and index sheet merged (PR #97). #23 bubble bath, pawdicure and hidden claws merged (PR #99). #24 store art draft sheet in PR #102 (store_art.py renders, store_compose.py lays out); waits on Derek's pick of icon A/B/C and thumbnails 1/2/3 (recommended B, 1 and 2), then finals 512 and 1920x1080. #15 stays open for the real plot and the street of 6. Review-QA merges Model-Agent PRs once both checks are green (Model-Agent pings them; no decision cards). #15 real plot and CleanACat_Area_Street merged (PR #103) (street pivot = slot 1 pivot at SpaLayout.PIVOT_POSITION, PlotSlot1..6 attachments; Gameplay to place it and drop PH_Floor). Next: any new model issue; #24 finals after Derek's pick (Planning-Agent relays it from the plan page).
- Contracts given to Gameplay and Motion-FX: tub CatSeat attachment at 1.2 studs; tools have a Handle part; dirty cats carry _MudNN, _TangleNN and hidden _FluffNN child Models (FluffCount), WetDarken; every cat Head has Carry and BowSlot attachments; bows have BowSlot at the knot.
- Station contracts (#18): brush tables (plain and Up swap in place) CatSeat 1.8, dryer CatSeat 1.2 with a Nozzle part and Air attachment (+Y down), all CatScale 1.5 with an invisible _Barrier under the top; BuildPad has a Screen part. Later stations stay at or under 1,200 tris (Review-QA).
- Builder kitten contracts (#20): kitten has HatSlot (Head) and HammerGrip (LegF2); hat HatSlot, hammer Grip at the grip (swing about X), toolbox CountdownAnchor. Street pitch told to Gameplay: 44 studs, plots side by side along X, fronts to -Z.
- Coat table (#22): ReplicatedStorage.Assets.CleanACat_CoatTable (Rojo JSON module, written by build_all). Dark fur gets mud_dust instead of mud (per blob, whichever contrasts more). Palette row 20 holds mud_dust, mud_dust_wet, rarity_uncommon and 5 free cells.
- Later stations (#23): BubbleBath has a Spout part with a Bubbles attachment (+Y up); Pawdicure CatSeat at 1.6. Dirty cats carry hidden _Claw01 to _Claw08 (ClawCount 8). Dirty cat budget is 3,200 tris and 120 parts.
