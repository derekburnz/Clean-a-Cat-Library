---
name: ui-icons
description: Derek's HUD icon style decision (2026-11-24): a mix of his library's 3D renders and our current clear icons; no Phosphor, Lucide or Kenney.
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
