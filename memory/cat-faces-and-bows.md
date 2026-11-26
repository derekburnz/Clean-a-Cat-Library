---
name: cat-faces-and-bows
description: Derek's 2026-11-26 notes on the cat models: where a bow sits, the cream cat's mouth, round cheeks in place of the eye strips, carriers at the counter
metadata:
  type: project
  modified: 2026-11-26T16:12:36.939Z
---

- Bows (Derek 2026-11-26 ET): on icon E, "angle the bow to the top right of head so it doesn't get cutoff by line", then "make the bows in game to also look like that if they don't". Issue 764, PR 770: every cat's BowSlot Attachment is on the head's top front corner at the cat's left, tipped 30 degrees. Full size in the game, 0.85 on the icon. BowFit follows the Attachment, so no game code.
- Faces (issue 771): "fix the mouth on this cat" (the cream cat Toffee: its brown muzzle block is gone, same mouth as the rest) and "these little strips beside the cats eyes on all models ... I can't tell what theyt are and they look bad" (the blush bars are now small round cheeks under the eyes on every cat). 
- Follow ups (2026-11-26): faces merged in PR 772; the people's cheeks are round too (issue 776, PR 781 merged; one function in `townsfolk.py` draws customers and staff). Store pictures and all portraits were rendered again (portraits in the shared files under Model-Agent/ui-renders/faces-2026-11-26/). Issue 784, PR 787: Suds's uploaded portrait and the Helper and Helpers HUD pictures still showed the bars; rendered again (portrait file in assets/clean-a-cat/ui/icons/portraits/). Uploaded to the group 2026-11-26 1:24 PM ET, ids on issue 784; Design still swaps them in Portraits.luau and HUD/Icons.luau and refreshes its mockup pictures.
- Cats with a head piece (issue 782, PRs 786 and 789): `props.bow_corner` puts BowSlot on the side of the head (0.015 out, 0.12 under the top, 75 degrees); Bathtile, Stardust and Djinn have their own spot in `props.BOW_OWN`. Lesson: a Blender look passed bows that cut in Studio (loops are fuller in Roblox, the bow is worn at 1.0 on a sitting cat built at 0.95). Always run `python3 assets/clean-a-cat/blender/rbx_bowfit.py` after touching a bow, a head piece or BowSlot; it measures the Roblox parts and must end with "every bow clears". Sync's part check sees blocks, so Bathtile's Royal still reports a touch at the cap's empty block corner.
- Carriers at the counter: "make the customers walk up with the cats in their cat crate place them un the table and have the cats walk out and sit then the crate dissapear slowly". Existing carrier models; spots SpotCounterCrate1-6 on the big plot (PR 765); the motion is Motion-FX's (issue 757).
- Side bits (2026-11-26): Derek twice called the tangle clumps and fluff puffs bits sticking out of the cats' sides. Off all store art; issue 791 (open, unclaimed) reworks them on the in-game dirty cats so they read as fur. Names and counts (_TangleNN, _FluffNN, TangleCount 6, FluffCount 10) must stay.
- Open question for Derek (asked through the coordinator 2026-11-26): on the ten head piece cats the game's bow stands off the side of the head; smaller, or left off?
- Threads were remade 2026-11-26: Model-Agent's handoff is library/Model-Agent/handoff-2026-11-26.md (also in the shared files under Model-Agent/).

**Why:** Derek judges the cats at a glance on a phone. Model-Agent's reading: no marking that can read as a mouth, no flat bar touching an eye, a bow must show whole from the front.

**How to apply:** the face is drawn in one place, `cats.py` `_head`; the bow spot is `cats.bow_side`. See [[art-and-models]] and [[store-art]].
