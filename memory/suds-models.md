---
name: suds-models
description: Model-Agent's Suds and opening scene models, plot spots, the group portrait id, and two limits (Images cannot be archived, Model-Agent does not edit SpaLayout).
metadata:
  type: project
  modified: 2026-11-24T22:55:00.000Z
---

Models for Derek's Suds opening ([[suds-opening]]) (generators in assets/clean-a-cat/blender, style guide sections 21g to 21j).

- Suds: `CleanACat_Cat_Suds`, `_Sit` (clean, mint collar with a gold bell as a child Model ending `_Collar`), `_Dirty`, `_Dirty_Sit` (the stray, no collar). Root attribute `Mascot` true. He is in `cats.EXTRA_CATS`, not the roster, because Derek said "yeah dont include him on indez".
- Opening props: `CleanACat_Prop_DeliveryTruck` (no brand, door and four wheels as child Models), `CleanACat_Prop_DeliveryBox` (Derek: "a random brown box", not a soap crate; four flaps), `CleanACat_Prop_Pothole` (Derek: "speed bump should be changed to pothole", pull request 350; `CleanACat_Prop_SpeedBump` is unused and goes once no code clones it). Same message asked for a better looking truck (done, pull request 352) and "draft the world/background and sky": pull request 356 rebuilt the houses across the road and added `CleanACat_Area_Backdrop` (no collision or shadows; Gameplay-Engineer places it at the street's pivot, Motion-FX has the sky). Review-QA's hold: none of it goes live until the backdrop is placed and a phone frame-rate run passes.
- Bed: `CleanACat_Prop_SudsBed` (Attachment `CatSeat`, attribute `CatScale` 1.2) is a low round basket since pull request 339 (the stand read as a pedestal).
- Held loaf: `CleanACat_Cat_Suds_Dirty_Loaf` and `CleanACat_Cat_Suds_Loaf` (loaf.py, carry only, no MudCount). Derek 2026-11-24: "we should pick him up out of crate"; his clip of the hold (Coordinator/references/carry-hold-2026-11-24/): the load lies across the arms, head end at the carrier's LEFT. His ten-angle picture set the pose (pose only, Suds keeps his look). Since pull request 355 the loaf matches it: head tipped 45 degrees nose down with the chin tucked on short tucked paws, tail up at his outer (right) hip with nothing across the rump (pull request 383: the R6 right arm comes up under the chest half of his rear, so any tail part there clips), eyes open (Derek, relayed by Planning-Agent 2026-11-24: "go with whatever you suggest depends if you carry customers pets or not"), root attribute `CarryScale` 1.4 (1.0 in the box, 1.5 at a station). Motion-FX owns the arms (Effects/Carry.luau).
- Mud on dark fur (pull request 328): wet dust, drab every third piece; pale dust read as a calico.
- `CleanACat_Prop_PhotoCamera` (pull request 359) replaces the black block by the tub once Gameplay-Engineer swaps it in. The spa name sign has a navy frame since 365: no pale colour reaches 3 to 1 on the pink wall.
- Plot Attachments: `SpotOpening`, `SpotBox`, `SpotBump`, `SpotMascot`.
- Since pull request 350 the pothole lies 2.5 studs before the player on the truck's way and the box stops 5 studs to their right (Roblox: SpotBump x -7.5, SpotBox x 0, player x -5), never straight ahead.
- Portrait: `portrait_Suds_ink.png` uploaded to the group as rbxassetid 92665897768427 (2026-11-24 ET) for `Portraits.IMAGES.Suds`. Round cheek version uploaded 2026-11-26 as 134546291029280 (issue 784); Design swaps the id.

Limits learned:
- Open Cloud cannot archive Images ("not an archivable asset type"). Derek's "delete the old ones after" for the two old paw HUD versions needs him to remove them by hand in the Creator Dashboard (group, Development Items, Images). See issue 275. Their ids stay out of every file on purpose.
- Model-Agent does not edit `SpaLayout.luau` even when Gameplay-Engineer asks: it is outside the role's folders and the edit gets blocked. **How to apply:** change the plot Attachments in the model and send Gameplay-Engineer the fallback lines read from the exported model.
- Staff looks still wait for Derek's references; do not polish Jo and Sam ([[art-and-models]]).
