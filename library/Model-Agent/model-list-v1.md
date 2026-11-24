# Clean a Cat: model list for the first version

Model-Agent, 2026-11-23 ET. Source: `Planning-Agent/gdd-draft.md` (draft, not locked). If the design changes after Derek's playtests, this list follows it. Each row below is a GitHub issue on derekburnz/Clean-a-Cat with the `model` label (one `store-art`). Issue numbers are in the last section.

## Ground rules for every model
- **Names:** `CleanACat_<Category>_<Name>` (the code prefix from issue #1). Pivot at base centre, front faces the player, transforms applied.
- **Built from scripts:** every model comes from a Python generator in `assets/clean-a-cat/blender/`, so a style change is a code edit and a rebuild. Exports go to `exports/`, Studio-ready files to `rbx/` (Rojo puts them in `ReplicatedStorage.Assets`). Blender runs here as the `bpy` Python module (5.2.4), so no PC is needed to build. Studio import checks and screenshots go through Sync-Agent.
- **Flat colours, no textures** where possible: each MeshPart gets a `Color3` and `SmoothPlastic`. Zero texture memory and recolouring a cat is one line of code.
- **Phone budgets:** a cat up to 3,000 triangles, furniture 300 to 1,200, small props 50 to 400, one whole plot under 25,000 triangles and about 250 instances, the whole street under 150,000 triangles and 1,500 instances.
- **Scale:** a Roblox avatar is about 5 studs tall. Cats are bigger than life (about 2.5 studs long, 2 studs tall sitting) with big heads, so they read on a phone and fill the screen at the tub.
- **Original only:** no real breeds by trademark name, no look-alikes of known cat characters.
- **Uploads** (meshes go up when Studio imports them) are owned by the Roblox group Creampuff Games, never a personal account.

## Style (decided by recommendation, Derek can swap it)
Three options, first one recommended and used until Derek says otherwise:
1. **Bubble Pastel (recommended).** Soft, round, chunky shapes, flat pastel colours and white foam. Palette: cream `#FFF6EC`, mint `#A8E6CF`, bubblegum `#FFB3C7`, sky `#8FD3FE`, mud `#5A4632`. Why: reads best at phone size, costs no texture memory, suits a young audience and makes the dark mud pop against every coat, which is the whole first 15 seconds.
2. **Cozy Storybook.** Warm wood, terracotta tiles and soft painted textures on one small atlas. Warmer but needs textures and loses contrast with brown mud.
3. **Bright Toy.** Saturated primaries and glossy plastic. Loud and readable but looks like many simulator games already on the charts.

The winner becomes `docs/art/style-guide.md` in the game repo (first issue below).

**Update 2026-11-23 after reading Derek's asset library:** keep the Bubble Pastel colours but use the library's blocky chibi cat body and its Part-built export (no mesh uploads). Details in [asset-library-reuse.md](asset-library-reuse.md). The ten coats stay new; no Cat Cafe character is reused.

## The list, in build order
The design's build order is: scrub and reveal on a phone with one grey cat first, then brush and photo, customers, the window, builds and saving. The models follow it.

| # | Model or set | What it holds | Size and budget | Waits on |
|---|---|---|---|---|
| 1 | Style guide and pipeline | `docs/art/style-guide.md`, palette, budgets, the generator script layout, the scale check against a 4 stud part | Docs and scripts | Repo seeded (#1) |
| 2 | Cat body | One shared cat: body, head with ears, tail, four legs as separate parts with pivots at the joints, invisible `Root` part. Used by every cat and the builder kitten | 2,000 to 3,000 tris, 8 parts | 1 |
| 3 | Dirty look | Mud blobs (3 shapes) on 20 named sockets (`Mud01` to `Mud20`) so the scrub can remove them one by one, 6 tangle tufts for the brush, a wet flat coat variant for the dryer | Each blob under 60 tris, a dirty cat under 35 instances | 2 |
| 4 | Wash tub and sponge | The first thing a player sees: a round tub on legs with a foam top and a water part, the sponge tool, Bubble Soap and Golden Sponge variants | Tub up to 1,200 tris, sponge up to 200 | 1 |
| 5 | Brush, fluff and bows | The hand brush, the fluffed clean look (a puffed fur shell after three swipes) and three bows (pink, mint, sky) | Fluff shell up to 800 tris, each bow up to 200 | 2 |
| 6 | Spa room and street plot | Graybox first, then the real one: small spa room with front window, door, back door, floor and walls finished on every visible side, room for the stations, the queue, the window and the builder. Six plots side by side on one street | Plot under 25,000 tris and about 250 instances | 1, plus a paired Gameplay-Engineer PR for the spots |
| 7 | Customers and strays | Customer look (Roblox avatar with our own simple colours and a hat or bag), the cat carrier they hold, the stray box at the back door, the chance board frame by the door (Design-Agent fills the screen part), the queue mat | Carrier up to 400 tris, box up to 200 | 2, 6 |
| 8 | Display window | Four cushions in the front window, the tip jar that fills, a window frame and sign | Up to 1,500 tris total | 6 |
| 9 | Stations | Brush table (plain and upgraded), blow dryer station, and a build site pad (taped floor and cones) that shows where a locked station goes | Each station up to 1,200 tris | 4 |
| 10 | Builder kitten | The cat body with a hard hat, hammer and toolbox. Hammers while a build runs | Props up to 400 tris total | 2 |
| 11 | VIP Room, locked | The first long build (8 hours) offered in session one: a closed door with a tarp and a sign so players see what they are building. The finished room is a later issue | Up to 2,000 tris | 6 |
| 12 | Ten coats in five rarities | The colour sets for the ten cats of the first Cat Index, plus one small extra per rarity from Rare up | Colours only, extras up to 300 tris | 2, 3, 5 |
| 13 | Later stations | Bubble Bath (10 minute build) and Pawdicure (1 hour build) with the long claws look | Each up to 1,200 tris | After the slice |
| 14 | Store icon and thumbnails (store-art) | Draft sheet first, Derek's OK, then final files. Shows the muddy cat turning fluffy, the action the first minute really shows. Three words at most, never the word free | 512 icon, 1920 x 1080 thumbnails | 3, 5, 6, and Derek's OK |

## The ten cats (working names; Design-Agent owns the final names)
Renamed 2026-11-23 so no name matches a Cat Cafe cat (Biscuit, Pebble, Midnight and Snowball were taken there).
Matches the draft chance board: Common 60%, Uncommon 25%, Rare 11%, Epic 3.5%, Legendary 0.5%.

| Rarity | Cat | Coat | Extra |
|---|---|---|---|
| Common | Muffin | Ginger stripes | none |
| Common | Smudge | Grey stripes (the first stray, the test cat for the scrub) | none |
| Common | Inky | Black with mint eyes | none |
| Common | Cotton | White with pink nose | none |
| Uncommon | Tux | Black and white | none |
| Uncommon | Patches | White, ginger and black patches | none |
| Rare | Toffee | Cream with darker face, ears and paws | Ear tufts |
| Rare | Marble | Silver with dark spots | Ear tufts |
| Epic | Lilac Cloud | Pastel lilac, extra fluffy | Fluffy ruff |
| Legendary | Starcoat | Gold with tiny star spots | Soft glow (Motion-FX adds the sparkle) |

## Hand-offs and notes for other threads
- **Gameplay-Engineer:** the scrub removes mud by socket name (`Mud01` to `Mud20`), tangles by `Tangle01` to `Tangle06`. A cat is a `Model` with `PrimaryPart = Root`. Coats are a table of colours per part, so the server only sends a coat id. Up to 20 mud blobs per cat matches the design's cap for cheap phones.
- **Motion-FX-Agent:** rig part names and pivots are fixed in issue 2 before any animation starts. Shake off, purr and the builder's hammer need them. Tell me before renaming anything.
- **Design-Agent:** the chance board and the tip jar label are screens on the models (SurfaceGui), so the frames leave a flat face for them.
- **Review-QA-Agent:** every model PR comes with a sheet (front, side, back, top, with an avatar for scale), the triangle and instance counts, and a check that no model file holds a script.

## Issues filed (2026-11-23 ET)
| Row | Issue |
|---|---|
| 1 Style guide and pipeline | #10 |
| 2 Cat body | #11 |
| 3 Dirty look | #12 |
| 4 Wash tub and sponge | #13 |
| 5 Brush, fluff and bows | #14 |
| 6 Spa room and street plot | #15 |
| 7 Customers and strays | #16 |
| 8 Display window | #17 |
| 9 Stations | #18 |
| 10 Builder kitten | #20 |
| 11 VIP Room, locked | #21 |
| 12 Ten coats | #22 |
| 13 Later stations | #23 |
| 14 Store icon and thumbnails | #24 (store-art, needs-owner at the pick) |
