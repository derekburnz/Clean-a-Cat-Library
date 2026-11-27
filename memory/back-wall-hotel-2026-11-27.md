---
name: back-wall-hotel-2026-11-27
description: Derek's 2026-11-27 calls on the back wall (VIP Room removed, one back door, tape with no pink), the Cat Hotel models and the customers' arm bug
metadata:
  type: project
---

- Derek 2026-11-27 8:07 AM ET: "remove the vip room entirely and switch it to just be one door at the back (fill other one in with a wall) make the caution tape model better with no pink" (issue 1063). Model-Agent's PR 1071: `CleanACat_Area_BackDoorLocked` redone (yellow and ink tape, warning sign, orange board, lamp, no pink; same name, barrier, PromptAnchor) and new `CleanACat_Area_VipDoorFill` at SpotVipDoor (plot model untouched). Gameplay's PR 1067 removes the room behind switch `noVipRoom`.
- **How to apply:** no pink on building site props; building site colours are fur_golden, fur_ink, paw_neighbourhood. Do not build anything new for the VIP Room.
- Back door looks (issue 1041, PR 1057 merged): `CleanACat_Area_BackDoorLocked` and `CleanACat_Area_BackDoorOpen` at SpotGardenDoor, switch `expansionDoor`. Behind it goes the Cat Hotel (Derek's pick, issue 1050, spec in the shared files at Design-Agent/cat-hotel/). The Garden moves to a side yard spot `SpotGardenSide` (still to add in plot.py).
- Derek's plan page answer 2026-11-27: the hotel unlock and rooms 3 and 4 are timed builds like the others, so the door and the two rooms need under construction looks.
- Hotel models merged 2026-11-27 (PRs 1071, 1079, 1087): `CleanACat_Area_Hotel`, `CleanACat_Prop_Suitcase`, `CleanACat_Area_BackDoorBuilding` (the door while it builds), sleeping guests `CleanACat_Cat_<Name>_Loaf_Lite`. Garden's way in: Design picked a side gate in the hotel's right wall (Derek may still change it); built and merged in PR 1103 (2026-11-27): doorway in the hotel's right wall (`SpotHotelGardenDoor`), plot spot `SpotGardenSide` (same place as SpotVipDoor), side looks `CleanACat_Area_GardenSideLocked/Building/GardenSide` with one gate leaf in the left edge; the back door looks are unchanged. Still optional (Review-QA's notes): a sign on the hotel's yard wall, Tux's white muzzle on the sleeper.
- Starter pack pet (Derek 8:46 AM ET, issue 1090: "don't use a sponge as the image make it like a golden flashing pet or crate or something crazy"): Midas, `CleanACat_Pet_Midas` in `pets.STARTER_PETS` (Epic, attribute Starter, never in a crate), card picture `shop_StarterPet`. PR 1093 merged.
- Customers' arm sticking out at the counter (Derek 8:06 AM ET, issue 1062): the models are straight; the cause was CustomerMotion not turning the carrying arm back in (Motion-FX PR 1064). Pip's pink shape at the hip is his water bottle.
- Derek's other answers that day: helper bust pictures stay and the Jo, Sam, Lou game models get remade after launch; shop pictures keep their baked words; Lou keeps his name.
- Growth's ask (issue 1066): store page picture set in Model-Agent/store-art/page-set-2026-11-27/ (4 home thumbnails, 5 detail pictures, icon A with and without title), all passed the image gate; made by `store_page.py` (PR 1099 merged). The shared mount adds bytes to PNGs on write, so send Review-QA sha sums read back from the share, not local ones.

Related: [[helper-portraits-shop-art]], [[store-art]], [[customers-and-carriers]].
