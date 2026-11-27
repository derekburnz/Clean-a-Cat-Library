# Image gate (Review-QA, since 2026-11-27)

Every image goes through this gate before it reaches Roblox by any route: the upload-asset workflow, store-setup, or by hand. The reason: Derek's account was suspended for 7 days after Roblox's filter misread our pink thumbs up icon (ThumbsUpFilled) as sexual content.

An image FAILS if it has any of these:
- hands, fingers or thumbs, in any pose
- a long rounded shape standing on its own: a stub, a tube, an upright capsule or a knob on top
- skin tone blobs, or large skin tone fields
- floating brown blobs or splats
- text other than the game's title, logos, weapons, or body parts

How to check: look at it full size, at 48 px and at 24 px, and as a black silhouette of the subject. When in doubt, it's a FAIL.

Upload rules:
- Only files whose "sha256  path" line is on main's .github/upload-allow.txt can upload. Review-QA signs each line.
- At most four images per run, a few minutes apart, stopping at the first refusal.
- The store page art is Derek's to upload himself.

## Added 2026-11-27 (PR 1052)
- Short item badges such as "2x", "3x" and "+1" are allowed. Words are still a FAIL.
- FAIL: real-money symbols ($, €, £ and the like) on any picture. Our coins carry a paw or a star.

## Store page set batch 1 (issue 1066), 2026-11-27 8:50 AM ET: PASS
Model-Agent/store-art/page-set-2026-11-27/: home-1 to home-4, detail-1, detail-2, icon-a-plain, icon-a-with-title. No hands, no words but the title, no money signs, no fur clumps or puffs (mud patches only). Notes: home-2's title sits in the bottom tenth where the player count can cover it (lift it); the icon's title is small at 150 px (Derek's pick). Store art is dragged in by Derek, no upload run.

## PR 1093 (issue 1090), 2026-11-27 9:00 AM ET: PASS
CleanACat_UI_Shop_StarterPet.png 8601ae110b326f9f22038fd363cc364b5fc28b27325827f635242a608813aa2c and CleanACat_UI_Portrait_Pet_Midas.png 5c9c75d36195280178fd55a6541232bc411fc6e3ccb774489cbcddacded30a86: golden crowned cat, plus-shaped sparkles, no words or hands, clear at 48 and 24 px.

## Store page set batch 2 (issue 1066), 2026-11-27 9:10 AM ET: PASS
detail-1, detail-2 (title now at the top), detail-3-helpers-at-work (new: three staff in aprons beside two tubs, arms at their sides, no hand gestures), home-1, home-3. No words but the title, no money signs, no fur clumps. Checked the files as they were at 9:08 AM ET (sha256 prefixes 2cb9acc3949d, 3fb177114817, 20dfd08c41db, 02243688d8f0, e2e609ca5f0d); these differ from the prefixes Model-Agent sent, so the files were saved again after its note.

## Store page set batch 3 (issue 1066, PR 1099), 2026-11-27 9:16 AM ET: PASS
detail-4-cats-waiting-at-the-counter 72331ad4ea9e, detail-5-pets-from-crates 28024699704e (sums read on the share; the share adds bytes to PNGs on write, so always gate the share's own sums). Owners with arms down, mud patches only, no words.

## 2026-11-27 10:15 AM ET: PR 1112, Helpers HUD icon options (issue 1110)
- Blobs fetched at head bac4882, sums match Model-Agent's: HelpersTeam d5ab954d…, HelpersApron cf0faf66…, HelpersBadge a1a4bccd….
- Own sheet (full, 48, 24, silhouette): blocky helper heads and an apron, no hands or arms, no words. All three PASS the look.
- Allowed: HelpersTeam only (PR 1113). Apron and Badge get a line only if Derek picks one.
- 2026-11-27 ~10:18 AM ET: HelpersTeam uploaded after PR 1113 merged, run 46023608868, one file, no refusal: 97491083681037. Apron is not wanted (Derek rejected the apron look).

## 2026-11-27 11:25 AM ET: PR 1126, 25 buy pictures (issue 1122)
- All 25 blobs at head c14ac9e match Model-Agent's allow-lines.txt. Own sheets: PASS (long shapes fine, badges only, star coins). Allowed in PR 1127. Upload four per run.
- 2026-11-27 ~11:30 AM ET, buy prompt pictures on DEV passes and products (store-setup icons, PR 1128): plan 46034008747 (14 approved), confirm runs 46034081380, 46034156476, 46034250875 (4 each), 46034343923 (2). All HTTP 204, no refusal, 14 of 14. Live waits on Derek.

## 2026-11-27 12:55 PM ET: PR 1132, HUD coin with a star
- Blob at 370814d matches 52fe8468…. Own sheet PASS (star face, no money sign). Allowed in PR 1133. Replaces 116447888023490 (S with a bar).
- 2026-11-27 ~12:58 PM ET: HUD coin uploaded, run 46046127946, id 108922632736355, state Reviewing at upload (no refusal). Wired in PR 1134; Sync to confirm it loads on dev.
- 2026-11-27 1:12 PM ET: Sync confirmed 108922632736355 loads (Success) on main f6e2370 in the coin pill and 12 other coin spots; past moderation.
