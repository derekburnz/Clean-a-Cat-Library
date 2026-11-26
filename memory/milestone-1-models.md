---
name: milestone-1-models
description: Model-Agent's milestone 1 work (issues 527, 670 and 688): what is merged, what is left, the order, and the standing calls from Derek, Review-QA and Motion-FX
metadata:
  type: project
  modified: 2026-11-26T10:00:00.000Z
---

Issue 527 in the game repo is Model-Agent's list for the playtest draft. One PR per piece, Review-QA passes each. Names and contracts of merged models: docs/art/style-guide.md.

Merged by 2026-11-26 ET: bow tiers with the Golden bow, worker wash stands, nine pets, the crate, the gift stand with its pet Starcoat and its bigger heart balloon (issue 659), the VIP Room's eight resident seats, the Garden, the stray box, the wall pieces' camera fix (issue 670), the VIP Room trim (244 to 202 parts) and the light sitting twins `CleanACat_Cat_<Name>_Sit_Lite` of the special cats (`cats.build_cat_lite`, root attribute `Lite`). Issue 688 stays open until Gameplay-Engineer's VipRules seats the twins (Review-QA's call).

Also merged 2026-11-26: PR 705, four more special visitors' cats from Catch a Cat Cafe (Phoenix, Moonstag, Djinn, WhiteTiger, five models each) plus the darker mud rule (brown mud on fur of middling darkness; only Moonstag changed). Gameplay-Engineer adds the names to CatRules when wanted. Card pictures for Design-Agent: shared files, Model-Agent/special-cats-more-2026-11-26/portraits/. PR 706: six menu pictures `CleanACat_Icon_Hud_{Quests,Shop,Pets,Crate,Bow,Helpers}`, uploaded to the group; the ids are in Design-Agent's `HUD/Icons.luau`.

PR 710 merged 2026-11-26: Phoenix has dark pupils (gold on copper vanished at 40 px); style guide rule: plain lit eyes (`glow_eyes`) only where the eye colour is 3:1 off the face. 527's model list is DONE; it stays open only until the game shows the models on dev (Review-QA closes it).

Trap: write "Part of #N" in PR bodies. Any "closes" wording near an issue number closes it (527 was closed that way 2026-11-26).

Standing calls:
- Derek 2026-11-25 6:23 PM ET (via Planning-Agent, in Planning-Agent/playtest-notes.md): "can use that or names and designs from cats for catcafe especially for rare customers as catcafes detailed cats have some really cool designs". So Catch a Cat Cafe cat names and designs MAY be reused, above all for special visitors' cats, tweaked to our style. The ten draft names stay for customer cats.
- Pet names (Cozy, Scrubby, Pebble, Pickle, Koi, Bamboo, Coral, Nimbus) are DRAFT names. Derek was shown the pet sheet 2026-11-25 night and has not answered; Review-QA parked the names for him.
- Review-QA: if a Royal bow clips Rosette's crown or Stardust's gem in game, add a per-cat `BowScale` attribute of about 0.85, do not move BowSlot. Every cat with a head piece carries `HeadPiece` true so BowFit drops the Golden bow's `_Fan`.
- The gift pet's `Rarity` is Uncommon because the game says so (`CrateRules.GIFT_PETS`); the game shows it on the stand at the stand's `CatScale` 1.0 and reads the plot Attachment `SpotGift`.
- Motion-FX 2026-11-25 on issue 659 (lit gift stand too small on a phone): NO Neon heart. The Neon rule: a shape that must keep its outline stays SmoothPlastic. They fix it with a screen sized sparkle. A slightly bigger plain heart is welcome if it stays inside the child Model `_Balloon` (pivot at the knot, they sway it).
- VIP Room residents: `ResidentScale` 1.2; ten seats `SpotResident1` to `SpotResident10` since PR 715 (2026-11-26, eight before). The game reads `ResidentSeats`.

- Wall pieces (issue 670): four rules for inside walls are in the style guide section 14 (Roblox's camera rests 0.1 studs behind a solid face); `assets/clean-a-cat/blender/camera_rest_check.py` tests them without Studio.
- Review-QA 2026-11-26: a fully built plot is about 660 parts, six plots about 4,000. Sync-Agent measures frame time once the game places them; trim only if that says so.

**How to apply:** tell Gameplay-Engineer and Motion-FX before any merged name or pivot changes.

See [[art-and-models]], [[special-cats-and-dirt-levels]], [[derek-plan-answers]].
