---
name: moderation-hold-2026-11-26
description: RESOLVED 2026-11-27 6:31 AM ET (appeal granted). Derek's Roblox account was suspended over our ThumbsUpFilled icon; image gate lessons stay
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

**Roblox's verdict (Derek, 2026-11-26 10:03 PM ET, with a screenshot of the notice).** The account is "Suspended for 7 days" for Sexual Content over ONE image: asset 135826908608436, ThumbsUpFilled, the pink thumbs up, whose thumb was misread. In his words: "they thought this was a dick or something I appealed it". The block can run until about 2026-12-03 7:54 PM ET unless the appeal wins. So the TapHand guess was wrong, and a thumbs up alone was enough.

**Plan from 10:04 PM ET (coordinator).**
- No Roblox writes of any kind (uploads, publish, flags, store-setup) until Derek says the account is clear. No other accounts or keys.
- Gameplay-Engineer turns the automatic publish on merge off, then PRs merge to main again with green checks.
- Review-QA keeps the list of what is merged but not published, and the switches owed in dev, in order, at Review-QA-Agent/unpublished-queue.md in the shared files.
- When the account is back: put the automatic publish back on, run one dev publish, then set the switches one at a time, then do the uploads. Replace and remove the three hand icons (76096338201947, 135826908608436, 121275029069381); PR 973 already points at the no-hands art from PR 976.

**Earlier hold (superseded for code):** until Derek says his account is clear.** That means no asset uploads, no publish, no flags, no store-setup runs, and no PR merges, because a merge starts a dev publish. PR 973 (the like how-to icon ids) is unmerged and disarmed. PR 975 is a draft. Derek was asked to sign in to roblox.com, accept or appeal the notice, and say when it's clear. After that, each failed run gets one retry, and nothing loops.

**Lesson (Review-QA gates every image before upload, see [[review-qa-working-notes]]).**
- No hand gesture icons: no raised single finger, no fist from the back, nothing a filter could read as rude.
- Before any upload, look at every image at full size and at thumbnail size, and ask whether an automatic filter could misread it as a gesture, a body part, a weapon, text or a logo. When in doubt, don't upload.
- Upload in small batches, and watch for a refusal before the next batch.

Related: [[before-live-checks]], [[ui-icons]].

**Resolved (2026-11-27 6:31 AM ET):** Roblox granted Derek's appeal; his main account is back. The image gate and upload allow list stay in force.
