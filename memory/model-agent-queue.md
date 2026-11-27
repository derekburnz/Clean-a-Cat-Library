---
name: model-agent-queue
description: Model-Agent's finished work held while Derek's account is moderated (2026-11-27): the PR order and where each piece waits.
metadata:
  type: project
  modified: 2026-11-27T05:15:05.748Z
---

Held because of [[moderation-hold-2026-11-26]]: no uploads and no merges until Derek says his account is clear. Model-Agent can push to only one branch, so its PRs go up one at a time, in this order:

UPDATE 2026-11-26 10:53 PM ET: hold lifted (Derek's go-ahead 10:50 PM; his main account is STILL suspended with the appeal open, the new group key comes from his other admin account). Images: Review-QA's allow list only, at most four per run, stop at the first refusal. PR 977 merged; gift crate is PR 984. Open the rest one at a time from fresh main; PRs with images add "sha256  path" lines to .github/upload-allow.txt for Review-QA.
STATE 2026-11-26 11:35 PM ET: 984 (gift crate), 985 (wash room), 986 (map edge), 996 (like icons), 997 (image gate redraws) all MERGED. Uploaded via upload-asset: HeartOutline 98146759736466, TapDot 112847264343092, Pet_Clover 77963078642728, Pet_Glitch 80341127367421 (Design-Agent swaps them in). PR 1003 (map edge slab off, Stardust bow off the wand, #885/#948) MERGED 11:36 PM ET. Queue EMPTY. Items 1 to 6 below are done. 883 and 948 CLOSED by Review-QA 2026-11-27 12:15 AM ET after Sync's Studio passes. Model-Agent has NO open issues or PRs.

1. PR 977, issue 948 (bows on head piece cats; Bathtile's bow on the cap's top right corner at BowScale 0.51). Review-QA PASS 2026-11-27, held. Merges first.
2. Gift crate, issue 859 (CleanACat_Prop_GiftCrate). Review-QA pre-review PASS from the sheet and patch.
3. Wash room, issue 856 (CleanACat_Area_WashRoom). Review-QA pre-review PASS; side towel and mirror were moved back after that.
4. Map edge, issue 885 (all three backdrops get far hills on an elliptical ground and a new _Peaks child). Gameplay and Sync say no code change is needed. Review-QA still has to check the camera's far clip and the phone frame rate on dev.
5. Like icons, issue 869 (HeartOutline and TapDot, no hands). The commit is from the closed PR 976. Upload them only after Derek's account is clear, then send the ids to Design-Agent.
6. Image gate redraws (branch mpetgate): Clover and Glitch head pieces and portraits (04d39303), and store thumbnails 1 and 3 re-rendered (9d7be023). Thumbnail 3 has the staff in long sleeves that cover the hands and no shower pole. Thumbnail 1 has no mud splats and a grey glow. Review-QA image gate PASS on all four, 2026-11-27. They upload only through Review-QA's signed allow list, after Derek's word.

Sheets and source patches are in the shared files under Model-Agent/<topic>/. When a PR goes up, Review-QA only checks that the commit matches the pre-review and that the gate passes.
