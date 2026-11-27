---
name: switches-2026-11-26-evening
description: Dev and studio switch changes from 6 PM ET on 2026-11-26 (washScreen, catWalkStand, trailBold, boxGuide, pillPointer) and the Studio scope copy.
metadata:
  type: project
---
Continues [[switches-2026-11-26]] (that file is full).

- Studio test scope had NO switches, so Studio playtests showed the old door line and old plot. All 105 dev switches copied to studio 5:55 PM ET (runs 45908118585, 45908234362). Copy each new dev switch to studio too.
- trailBold, boxGuide, pillPointer (Motion-FX PR 867) ON in dev 6:06 PM ET, one comma list run 45908813574.
- washScreen (Gameplay PR 864, issue 856) and catWalkStand (Motion-FX PR 876) ON in dev 6:10 PM ET (run 45909187367); the same two plus trailBold, boxGuide, pillPointer ON in studio (run 45909228213).

**How to apply:** live stays off for all of these until Derek's word. Add later changes here.
- tubLife (Motion-FX PR 880) ON in dev and studio 6:14 PM ET (runs 45909679546, 45909718896).
- zoomCap (Motion-FX PR 900) ON in dev and studio 6:20 PM ET (runs 45910141922, 45910178291).
- photoFx (Motion-FX PR 905) ON in dev and studio 6:23 PM ET.
- carryBlink (Motion-FX PR 909) ON in dev and studio 6:30 PM ET.
- foamStep (Gameplay PR 912) and washPops (Motion-FX PR 914) ON in dev and studio 6:33 PM ET; 912 also made the wash screen's front camera and smaller tools live under washScreen.
- joArrive and contextAsks (Motion-FX PR 921) ON in dev and studio 6:42 PM ET.
- bowDrag (Gameplay PR 935, drag a bow onto the cat, best tier shown) ON in dev and studio 6:54 PM ET (runs 45913578543, 45913630508). PR 933 (wash shot framing, issue 924) also live in dev under washScreen.
- petMenuOnly (Gameplay PR 942, no Give a pet prompt at the stands while the Pets menu is on) ON in dev and studio 7:08 PM ET (runs 45914741155, 45914773693).
- washSides and showerAim (Gameplay PR 943: the cat turns half way through scrub, lather and rinse; the shower held off the fur aimed at the cat; Motion-FX's stream PR 950 builds on it) ON in dev and studio 7:14 PM ET (runs 45915187704, 45915227887).
- outdoorWalk (Gameplay PR 946: 24 studs a second outside the spa after 2:45 of play) ON in dev and studio 7:22 PM ET (runs 45915673426, 45915722088).
- helperFetch (Gameplay PR 952: helpers walk to the counter and carry the cat) ON in dev and studio 7:31 PM ET (runs 45916144464, 45916184134).
- humanBuilder (Gameplay PR 955: the human builder in overalls by the build board; Motion-FX PR 957 hammers him) ON in dev and studio 7:28 PM ET (runs 45916613112, 45916645091).
- giftCrate (Gameplay PR 958, merged) stays OFF in dev until giftFlow (PR 960) merges, per Review-QA: the open and chances buttons come with 960. Then turn on giftCrate, then giftFlow, one run at a time.
- giftCrate and giftFlow (Gameplay PRs 958, 960) ON in dev and studio 7:31 PM ET together (runs 45917142719, 45917192911). PR 963 opens the gift crate window after the claim.
- STOP 7:55 PM ET (coordinator): a dev flags run 45919525551 failed with Open Cloud 403 "User is moderated". No flags, uploads, store-setup or publish retries until Derek reports. wideStreet (PR 974, issue 887) waits for that.
- Key check 8:05 PM ET (run 45919971979, one introspect per key): BOTH OWNER_KEY and ROBLOX_GROUP_KEY return 401 "API Key or last generated user has been moderated." Likely Derek's Roblox account (it generated both). Waits on Derek.
