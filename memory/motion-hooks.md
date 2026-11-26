---
name: motion-hooks
description: Moment names, attributes and model parts that Motion-FX's effects and sounds hook onto for the issue 528/529 moments (agreed 2026-11-25 ET)
metadata:
  type: project
  modified: 2026-11-26T00:10:44.772Z
---

Agreed with Gameplay-Engineer and Model-Agent on 2026-11-25 ET; the effects and sounds bind by these names and stay inert until each one exists.

**Moments** (Gameplay fires them; AudioController and EffectsController bind only if present):
- HeartLow(figure) and CatLeft(figure): on main (PR 543). They pass the CleanACatCustomer-tagged townsfolk figure and fire only with townsfolk on.
- VisitorArrived(visitor) and CrateDropped(crate) come with special visitors (510). BowTied(cat) comes with bow tiers (508).
- CrateOpened(crate), PetRevealed(pet) and PetStarUp(pet) come with crates and pets (511, 512).
- WorkerFinished(cat) and WorkerProgress(worker, cat, fraction) come with workers (509). BuildFinished(build) with 515, QuestDone() with 516, CheckInClaimed() with 517.

**Attributes:**
- HeartFill (0 to 1) and LinePlace on the customer figure.
- Washing (true while washing) on the staff model: drives the staff scrub (PR 563); asked of Gameplay for 509 on 2026-11-26. Review-QA: if a worker ever carries something on Grip, add a Carrying attribute so StaffPose.freeArms keeps that arm still.
- Worker cats (Gameplay, 509): server Model WorkerCat_<id> under Workspace.SpaPlots.Plot<n>.Workers.<id>, swapped for the clean _Sit model at 1, gone 1.5 s later.
- WorkerProgress (0 to 1) on the worker's cat. It must be set before the cat is parented, because WorkerBar watches DescendantAdded on models with the Cat attribute.

**Model parts** (Model-Agent):
- CleanACat_Prop_PetCrate: child _Lid_Swing turns +LidOpenDegrees (110) about its pivot X. Attachments PetSeat, Burst and Odds; CatScale 1.25.
- Staff CleanACat_NPC_Staff_Jo, Sam and Lou: joints _Head, _ArmL, _ArmR, _LegL and _LegR, like townsfolk. Attachments Grip, GripL and Overhead.
- Pets (Model-Agent PR 619): CleanACat_Pet_Cozy, Scrubby, Pebble, Pickle, Koi, Bamboo, Coral, Nimbus. Star pieces are child Models _Star2 and _Star3 (StarLevel 2 or 3; _Star3 holds a lit gem _Star3_Glow). Joints are the cat's: _Head, _Tail, legs _LegF1, _LegF2, _LegB1, _LegB2, _Prop2 on the back; parts carry Follows. Burst attachment 0.2 studs over the head; root attribute PetScale 0.7.
- Garden (Model-Agent PR 674, #579, FYI only): CleanACat_Area_Garden with child Models _Bulbs (two gate lanterns, for a night light), _Canopy (four pink blossom clouds, could sway or drop petals), _Flowers, and toys in _Decor; pet spots SpotPetSit1-4 and SpotPetPlay1-4. No effect asked yet.
- Coming:
  - CleanACat_Station_WashStand<Name>, with CatSeat and WorkerSpot.
  - CleanACat_Prop_GiftStand, with PetSeat, Prompt and Glow attachments and a small part Lamp to switch to Neon at about minute 7.

**Review-QA visual rules learned:** never draw stars or twinkles from crossed bars, because they read as a plus or a close mark; use Icons.IMAGES.Star or Sparkle. Lilac means special customers, so use ink (#45226B) for outlines.

Related: [[art-and-models]], [[suds-models]].
