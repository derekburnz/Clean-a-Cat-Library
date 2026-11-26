---
name: customers-and-carriers
description: Derek's 2026-11-25 asks to rework the customers (look and walk in) and the cat carrier, what was chosen and who does what
metadata:
  type: project
  modified: 2026-11-25T14:56:12.116Z
---

- Derek 2026-11-25 morning ET, his words: "rework customers to be much better can check asset library if needed"; what bothers him most is "look/walk in" (how they look and how they walk in); "add better cat crate model they look depressing right now" (read as the carrier customers bring cats in, not the reward crate).
- Same morning: "start drafting models for things that you know will be needed and qa check them use the proper skills and toolboxes and make sure everything is clean". Model-Agent's list avoids anything that hinges on the open playstyle pick: customers (issue 446), carrier (449), the finished VIP Room (448).
- Carrier (PR 458): a little pastel house with no bars, the cat's face in the open over a low scalloped gate. `CleanACat_Prop_Carrier` kept its name, size, Attachments and attributes, so it swaps with no code change; extra looks `CleanACat_Prop_CarrierSky` and `CleanACat_Prop_CarrierButter`. Rule kept in the style guide: nothing a cat sits in has bars or grey metal.
  **Why:** the old one had a grey grille over the cat's face, which is what read as depressing.
- Customers (PR 460, built 2026-11-25): eight part-built townsfolk `CleanACat_NPC_Customer_Sunny, Mo, Pip, Rae, Juno, Bea, Theo, Kit` (townsfolk.py), built on the customer builder in Derek's Roblox-Asset-Library with new looks in Bubble Pastel; 4.9 to 5.7 studs, no child (a child's hand is too low for the carrier). They replace the bare body-colour R15 figures once FigureService swaps. Derek has the sheet (Model-Agent/customers-rework-2026-11-25/) and has not answered yet.
- The carrier was then made lower (1.36 x 2.0 x 1.75, Grip 1.95 up, CatScale 0.7) so a hand carries it beside the leg; the right arm is built held out by `CarryArmDegrees`.
- Joints agreed with Motion-FX for the walk in: child Models `_Head`, `_ArmL`, `_ArmR`, `_LegL`, `_LegR`, each pivoted at its joint and turning about local X; the carrier hangs from a `Grip` in the right hand; a walk speed attribute on the model. Gameplay-Engineer makes FigureService clone them and walk them in and out behind a switch. Dev only, live untouched.
- **How to apply:** judge any customer or carrier change against "look" and "walk in" first; check the asset library before building; the CatCafe_ customers from his own earlier game are fair to reuse as a base.

See [[art-and-models]], [[suds-models]].
