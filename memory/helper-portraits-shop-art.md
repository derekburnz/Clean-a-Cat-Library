---
name: helper-portraits-shop-art
description: Helper portraits (smooth busts) and Robux shop card pictures of 2026-11-27 (issues 1036, 1030): ids, how they are made, gate lessons.
metadata:
  type: project
  modified: 2026-11-27T12:58:42.793Z
---

Derek's playtest 2026-11-27: helper pictures "blocky and mid", Extra Worker card showed Jo, shop pictures "suck at selling it". Model-Agent's PR 1052 (merged 7:48 AM ET) answers both.

- Made by `staff_busts.py` (smooth head and shoulders busts, pictures only, no hands or arms, no headband) and `shop_art.py`, rendered with `ui_renders.py --only portrait_Staff_,shop_` then `ui_compose.py` (shop_ pictures: 512 px, trimmed, ink outline).
- Uploaded to the group 2026-11-27 (all passed Review-QA's image gate): Staff_Jo 85051325996520, Staff_Sam 73703341255691, Staff_Lou 114806114354624, Shop ExtraWorker 95165289753902 (Lou with +1), Coins2x 113360699781391, Coins3x 114423850933764, Builder2 79901743380915, GoldenSponge 89559848537020, PetSlot2 114149856510592. Design-Agent wires them.
- Gate lessons: no money sign on coins (a "$" failed; coins carry a star). Words "2x", "3x", "+1" baked in are fine. Dungaree straps on a bust read as arms, so the builder bust has none.
- Blank pictures on Derek's phone (Clover, Helpers icon) were approved on Roblox; the suspected cause is missing Use permission for the experience (asset-permissions workflow, grant), which is the lead's to run. Roblox's thumbnail check only proves moderation state.
- Open questions sent to Design-Agent for the plan page: keep smooth busts for pictures only (pick) or remake helper game models later; keep baked words (pick).
- Starter pack (issue 1090, PR 1093, 2026-11-27 9:03 AM ET): Shop StarterPet 75389504028903 (Midas whole with sparkles; replaces the sponge on the starter card, Derek's word), Portrait Pet_Midas 125587914737060.

Related: [[ui-icons]], [[art-and-models]], [[moderation-hold-2026-11-26]].
