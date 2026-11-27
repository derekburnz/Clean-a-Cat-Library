---
name: ui-icons
description: HUD icon style (Derek 2026-11-24), upload rules, and the 2026-11-27 image gate after Derek's account was suspended over a thumbs up icon.
metadata:
  type: project
  modified: 2026-11-24T17:38:00.000Z
---

Derek's decision on issue 185, 2026-11-24 ET. He answered in three messages:
- Use the high-quality style of his asset library (derekburnz/Roblox-Asset-Library, models/blender-generators/hud_icons.py).
- The library coin (CatCafe_Icon_Coins) is the quality bar: "obvious what it is and looks good". The library Index icon is to be remade.
- Final refinement: "a mix of derek's style and our current one so its obvious what they are clicking but not ugly".

Applied as:
- One bold, simple object per icon that reads at 48 px.
- Our ink outline #45226b and Bubble Pastel colours.
- The library's chunky 3D render, soft shading and highlight.

All six HUD icons get this treatment for consistency: coins, Cat Index, tools, settings, helper and build. Model-Agent renders them, and Design-Agent shows Derek a sheet.

No outside icon files are used (Phosphor, Lucide, Kenney); Phosphor two tone only informs the look. The trial folder assets/clean-a-cat/ui/icon-trial/ is to be cut down to the chosen set.

See [[art-and-models]] and [[planning-status]].

DECIDED 2026-11-24 ET: Derek picked B (1+2, Model-Agent's 3D renders), "for now", so a swap must stay easy (one lookup table in Luau). The final six are CleanACat_Icon_Hud_*.png in Model-Agent/ui-renders/hud-2026-11-24/, going into the repo at assets/clean-a-cat/ui/icons/hud/. The three-way mix and the 1+4 flat set are shelved; the 1+4 SVGs are kept only in the shared folder.

Tweak 2026-11-24 ET: Derek wants the coin icon to be his library coin (CatCafe_Icon_Coins: gold stack with a $), not the new paw coin ("did it badly"). He then asked for it to be re-outlined: hud_coin.py redraws only its outline in #45226B.

Tweaks 2026-11-24 10:42 AM ET, Derek on the B set: "looks good apart from the bubbles on the back of brush makes no sense and honestly maybe making it a toolbox would be better", and "helpers are likely going to be staff like humans". So Tools is now a pink toolbox and Helper is a human staff head (game PR 234). Review-QA then found the shut toolbox read as a lunchbox at the phone's button size (about 36 pt), so it now stands open with the white carry handle above the lid, a brush standing at the left and a soap bottle (PRs 244, 248). Derek has not yet commented on the open version. Rule from this: check HUD pictures at 36 px, and keep the one cue that names the object. Dropped drafts are in hud-2026-11-24/dropped/. Staff look: see [[art-and-models]].

More pictures in the same folder and style (hud_icons.py), for names the UI drew as emoji: ten small ones (PR 253: Camera, Paw, Heart, Gift, Music, Speaker, Shake, Sparkle, Dice, Check) and five tiny ones for the queue window (PR 257: Crown, Lock, Mud, Tangles, Wet; flat on, thicker outline, checked at 18 px in the need chip). PR 261 adds Pointer, Star, Station; after it no icon name draws an emoji.

Upload (2026-11-24 ET): Derek, "if your talking about the hud icons always upload assets to group". Standing rule: in-game pictures go to the Creampuff Games group via the upload-asset workflow once Review-QA passes them, no ask each time. All HUD and small pictures are uploaded; the ids went to Gameplay-Engineer for Icons.luau. Same day: "the toolbox and hammer paw is not needed", "fix that before upload". Tools and Build were redrawn without the paw (PR 273); their paw versions had already gone up seconds earlier and must never be wired. Rule: no paw stamped on a picture to brand it.

Wired 2026-11-24 ET (game PR 280): all 25 group ids are in Icons.IMAGES. Sponge, Brush, Bow, Smell and Claws still have no upload. The two paw versions (Tools, Build) are still in the group: Open Cloud refuses to archive an Image (HTTP 400 "not an archivable asset type", archive-asset run on #275). Only Derek can archive them by hand in the Creator Dashboard, and nothing in the game names them.

Draft screens (Derek 2026-11-24 2:14 PM ET): "look good"; the pictures and HUD icons inside them need swapping to the current set plus a little polish, but that waits until the game questions are decided. Do it when next touching those screens.

No hand gestures (2026-11-27 ET): Open Cloud started answering "User is moderated" for the group key at 7:55 PM ET, minutes after Model-Agent uploaded the like how-to icons (#869), which included a thumbs up and a fist with one finger raised. That they caused it is a guess. Rule: draw no hand gestures for any uploaded picture. The like loop now uses HeartOutline, the existing Heart, TapDot and RingPuff (game PR 976, not uploaded). All uploads stay paused until Derek says his account is clear.

Image gate (2026-11-27, after Roblox named ThumbsUpFilled 135826908608436 "Sexual Content" and suspended Derek for 7 days, appealed): every image passes Review-QA before any upload. It fails on hands, fingers or thumbs, any long rounded shape that could be misread (stub, tube, upright capsule) and skin tone blobs, checked at 48 px, 24 px and as a black silhouette. Model-Agent's audit of all 157 uploaded or queued images, with what to replace and remove, is in the shared files at Model-Agent/image-gate-audit.md. Only Derek can archive an Image (Creator Dashboard). See [[moderation-hold-2026-11-26]]. Review-QA's calls on the audit (2026-11-27): an image Roblox already reviewed and let stand stays (re-uploading is the risk), so Mud, Tangles, the MEDIUM list and the 80 dirt portraits stay as they are; Pet Glitch and Pet Clover get redrawn before their upload, and store thumbnail 3 is re-rendered (staff arms at their sides, no pole) before the live page. Upload in batches of at most four, a few minutes apart, each image first sent to Review-QA at 48 px, 24 px and as a silhouette.

Helpers button (Derek 2026-11-27 11:06 and 11:15 AM ET, issue 1110): "make a better helper icon", then of the thin apron (`Staff`) "this icon sucks remake it". The apron idea is dropped for good. Replacement: `CleanACat_Icon_Hud_HelpersTeam.png` (two helpers side by side, chunky; PR 1112, image gate passed; uploaded to the group as 97491083681037, Design wires it). Lesson: no thin straps or small details on a HUD button; one chunky subject as heavy as Shop and Build.

HUD coin (2026-11-27): star on the face in place of the money sign, Derek's OK ("star is fine"); id 108922632736355. Detail in [[buy-pictures-1122]].
