# What Clean a Cat reuses from Derek's Roblox Asset Library

Model-Agent, 2026-11-23 ET. Library: derekburnz/Roblox-Asset-Library (public, packed from Catch a Cat Cafe on 2026-11-22). Checked by cloning it and running its cat generator here.

## The big win: the whole model pipeline
- `models/blender-generators/` builds every Cat Cafe model from Python (`common.py` Builder, `palette.py`, `rbx_export.py`, gates, contact sheets). It runs in this cloud thread with the `bpy` pip module: four cats built and rendered in seconds (test render: `reference/asset-library-cat-rig-test-2026-11-23.png`).
- `rbx_export.py` writes **Part-built `.model.json` files** that Rojo syncs straight into `ReplicatedStorage.Assets`. No mesh upload, so the group ownership trap does not apply to models at all. FBX copies stay as the detailed source if we ever want MeshParts.
- Plan: copy the framework files into `assets/clean-a-cat/blender/` under issue #10, rename the prefix to `CleanACat`, swap in our palette and drop the Cat Cafe only parts (catalog readers, icons tied to Cat Cafe screens).

## Cats (#11, #12, #14, #22)
- The cat generator (`cats.py`) has the blocky chibi bodies Derek already approved: walking, sitting and working, every joint its own pivoted part (Body, Head, Eye1, Eye2, EarL, EarR, Tail, four legs), about 1,000 triangles and 10 to 13 parts per cat. It also already has the coat features we need: stripes, patches, points, spots, ruff, ear tufts, fluffy coats, sparkle.
- We reuse the **body generator only**. The design rules out shared characters with Cat Cafe, so every Clean a Cat cat gets its own coat, name and colours, and none of the 462 finished Cat Cafe cats is used as is.
- New for Clean a Cat on top of it: the mud sockets and blobs, tangles, wet coat, the fluff shell and the bow slot.

## Style decision change
The model list recommended "soft round" Bubble Pastel. Using the library's blocky chibi body is better: Derek approved it, it is proven on phones and it saves the longest model job. New recommendation: **Bubble Pastel colours on the library's blocky chibi shapes.** Palette stays cream, mint, bubblegum, sky and mud.

## Other parts worth reskinning
| Library folder | Use in Clean a Cat | Issue |
|---|---|---|
| `models/cafe/buildings-and-plots` (shop shells and plots in four sizes, front and back doors) | Starting point for the spa room and the street plot | #15 |
| `models/npcs` customers (standing looks A to L) | Customer figures, recoloured | #16 |
| `models/filler` (cardboard box, plants, benches, lamps, signs, rubber duck row) | Stray box, street dressing, spa decor | #16, #15 |
| `models/stations` Desert Oasis Spa and spa towel | Reference for the tub and spa look | #13 |
| `models/items` (bowls, crates with lids) | Carrier and tip jar references | #16, #17 |
| `thumbnails-and-icons/RESULTS.md` | Hard lessons for #24: pictures that named a feature failed (0.45% play rate); show the first minute, one big hero, three words at most, real avatar rendered well | #24 |
| `guides/style-guide.md` | Its rules on swatches, budgets and Studio checks carry over | #10 |

Not reusable as is: uploaded asset ids in the library (icons, sounds) belong to the old uploads and must be uploaded again under Creampuff Games before they load.

## For other threads
- Motion-FX-Agent: `audio/` has 82 original sounds and music made from code (`synth/`) with an audio gate, and `effects/luau-effects/` has tween and particle presets, rarity glow, guide arrow and cat motion code.
- Design-Agent and Gameplay-Engineer: `menus/luau-ui-kit/` (Theme, Scale, dim plus arrow, toasts) and `code/` (saves, remotes, live flags) are listed in the library README.
