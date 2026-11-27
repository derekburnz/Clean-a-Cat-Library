---
name: model-agent-queue
description: Model-Agent's finished work held while Derek's account is moderated (2026-11-27): the PR order and where each piece waits.
metadata:
  type: project
  modified: 2026-11-27T01:55:05.982Z
---

Held because of [[moderation-hold-2026-11-26]]: no uploads and no merges until Derek says his account is clear. Model-Agent can push to only one branch, so its PRs go up one at a time, in this order:

1. PR 977, issue 948 (bows on head piece cats; Bathtile's bow on the cap's top right corner at BowScale 0.51). Review-QA PASS 2026-11-27, held. Merges first.
2. Gift crate, issue 859 (CleanACat_Prop_GiftCrate). Review-QA pre-review PASS from the sheet and patch.
3. Wash room, issue 856 (CleanACat_Area_WashRoom). Review-QA pre-review PASS; side towel and mirror were moved back after that.
4. Map edge, issue 885 (all three backdrops get far hills on an elliptical ground and a new _Peaks child). Gameplay and Sync say no code change is needed. Review-QA still has to check the camera's far clip and the phone frame rate on dev.
5. Like icons, issue 869 (HeartOutline and TapDot, no hands). The commit is from the closed PR 976. Upload them only after Derek's account is clear, then send the ids to Design-Agent.

Sheets and source patches are in the shared files under Model-Agent/<topic>/. When a PR goes up, Review-QA only checks that the commit matches the pre-review and that the gate passes.
