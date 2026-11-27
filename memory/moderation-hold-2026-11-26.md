---
name: moderation-hold-2026-11-26
description: Derek's Roblox account was moderated 2026-11-26 7:54 PM ET; every Open Cloud run (uploads, publish, flags, store-setup) and every merge is on hold until he says it is clear
metadata:
  type: project
  modified: 2026-11-27T01:00:53.159Z
---

**What happened (2026-11-26, ET).** At 7:54:57 PM a dev flags run (likeHowTo, run 45919525551) got HTTP 403 "User is moderated" from Open Cloud. The 7:57 PM dev publish (PR 972 merge) failed the same way, and so did the PR 974 merge publish. A read-only key check (run 45919971979) showed BOTH OWNER_KEY and ROBLOX_GROUP_KEY refused with "API Key or last generated user has been moderated". Derek's own Roblox account generated both keys, so the action is on his account, not on the place or the group.

**Timeline before the refusal.**
- 6:50 and 6:52 PM: Staff apron icon uploads.
- 7:31 to 7:32 PM: seven flags runs worked.
- 7:34 PM: eight new pet portraits uploaded (Clover, Ghost, Ooze, Glitch, Angler, Nebula, Dragon, Blaze).
- 7:43 to 7:53 PM: four dev publishes worked.
- 7:52:50 PM: four like how-to icons uploaded (ThumbsUp, ThumbsUpFilled, TapHand, RingPuff).
- 2 minutes after that, the first refusal.

All uploads showed "Reviewing" at upload time.

**Suspected cause (Review-QA's reading, not Roblox's word).** The suspect is the TapHand icon, asset 121275029069381: a fist seen from the back with one finger raised straight up, which an image filter can misread as a rude gesture. Model-Agent was asked to redraw it as a side view with the finger pressing the thumbs up, and to commit it without uploading.

**Hold until Derek says his account is clear.** That means no asset uploads, no publish, no flags, no store-setup runs, and no PR merges, because a merge starts a dev publish. PR 973 (the like how-to icon ids) is unmerged and disarmed. PR 975 is a draft. Derek was asked to sign in to roblox.com, accept or appeal the notice, and say when it's clear. After that, each failed run gets one retry, and nothing loops.

**Lesson.**
- No hand gesture icons: no raised single finger, no fist from the back, nothing a filter could read as rude.
- Before any upload, look at every image at full size and at thumbnail size, and ask whether an automatic filter could misread it as a gesture, a body part, a weapon, text or a logo. When in doubt, don't upload.
- Upload in small batches, and watch for a refusal before the next batch.

Related: [[before-live-checks]], [[ui-icons]].
