---
name: special-cats-and-dirt-levels
description: Model-Agent's drafts from Derek's 2026-11-25 playstyle pick: dirt levels on the dirty cats, six special customers' cats and their built-in pieces, the finished VIP Room
metadata:
  type: project
  modified: 2026-11-25T20:30:00.000Z
---

- Derek's picks on the plan page, 2026-11-25 ET (his words, in Planning-Agent/playtest-notes.md): special customers "that expire that only I can take their cats and have them have the really cool cat designs (can look in asset library)"; "the cats look dirtier in their pictures the more dirty they are and take more steps to clean. Rarer the cat the more likely its dirtier/has more steps but pays a lot more". The design is not locked, so all of this is a draft with no rules in the models.
- Dirt levels (issue 470, PR 472 merged 2026-11-25): one dirty model serves four levels. Each `_MudNN` and `_TangleNN` child Model has `DirtLevel` (1 to 4); the game destroys pieces above the cat's level on arrival. Root attributes `DirtLevels`, `MudAtLevel1..4`, `TanglesAtLevel1..4`. Card pictures per level are in the shared files at Model-Agent/dirt-levels-2026-11-25/portraits/ (not uploaded; Design-Agent picks).
  Since issue 478 (PR 481, 2026-11-25) each level adds mud in its own place in the card picture: 1 top left corner, 2 lower left and bib, 3 top of the head, 4 the whole right side. Judge any change at 64 px on a light, a mid and a dark coat.
- Special customers' cats (issue 471, PR 473 merged 2026-11-25): six in `cats.SPECIAL_CATS`, working names Bathtile, Sherbet, Stardust, Rosette, Prism, Jade. Outside the Cat Index and the coat table until Derek and Planning-Agent say where they belong. Rarity "Special".
  **How to apply:** a special cat needs one big cue judged at 64 px beside roster cats: a coat colour no roster cat has, ears in another colour, or one mark a third of the face wide.
- Special customers (issue 476, 2026-11-25): Vivi, Rex and Pearl in `townsfolk.SPECIAL_LOOKS`, `Special` true, lilac and gold with a gold star, carrying `CleanACat_Prop_CarrierRoyal`. Nothing spawns them. No townsperson wears lilac or gold (issue 479).
- Finished VIP Room (issue 448, merged 2026-11-25): `CleanACat_Area_VipRoom` at `SpotVipDoor`, named spots, no rules.
- "Even better" (Derek 2026-11-25 1:18 PM ET: "make the special cats even better", "look through roblox asset pack cats repo"; issue 486, PR 489): in his library the top cats differ by pieces built onto them, so each special cat now has a head piece (`_Prop`, in the Head), a back piece (`_Prop2`) and Neon `_Glow` parts, drawn by `props.py` (the library's Pen and Ctx, ported; the twelve pieces are new). Mud stays off the pieces. The royal carrier lost its roof so they fit and show. Cost: up to 2,040 triangles and 143 parts clean, 4,050 and 244 muddy, so rare visitors only.
  **How to apply:** to lift any cat above the roster, add a built-in piece before more coat detail. Keep back pieces within 0.78 studs each side; nothing may float; no two see-through parts may touch. Review-QA's rules from its first pass: no white foam built onto a cat (it reads as soap left to rinse), nothing over the brow, and on a cat with a head piece BowSlot goes on the head's front corner with Carry above the piece. Neon (Sync-Agent's Studio look, issues 491 and 496): cream, white or pastel Neon clips to white with a halo in game, so a big shape is SmoothPlastic and Neon is only small gems in deep gold, pink, sky or mint, none near the eyes. Blender cannot show bloom, so any Neon needs a Studio look.
- Sheets Derek has: Model-Agent/vip-room-2026-11-25/, dirt-levels-2026-11-25/, special-cats-better-2026-11-25/ (the current special cats sheet and card pictures). No answer on these as of 2026-11-25 2:30 PM ET.

See [[customers-and-carriers]], [[art-and-models]], [[planning-status]].
