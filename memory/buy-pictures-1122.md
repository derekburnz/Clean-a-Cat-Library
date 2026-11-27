---
name: buy-pictures-1122
description: Derek's rule that no two buyable items share a picture (issue 1122, 2026-11-27), the audit, the 25 pictures and who wires them.
metadata:
  type: project
  modified: 2026-11-27T16:28:07.150Z
---

Derek 2026-11-27 10:56 AM ET: "issue I am seeing certain items to buy sharing same icon fix that". Standing rule from it: every buyable thing (build, tool, bow, pass, product, crate) gets its own picture, different in shape and colour at card size, never only a tag on a shared picture.

**Why:** the Build window drew one hammer for all 11 builds, one toolbox for both tools, one bow for all tiers; 2x and 3x Coins were one heap; passes and products on Roblox had no picture.

**How to apply:** a new buyable item ships with its own picture in assets/clean-a-cat/ui/icons/shop/ (CleanACat_UI_Shop_Build_<Id>, _Tool_<Id>, _Bow_<Tier>, Crate1, Crate5, Finish1 to 5), drawn by buy_art.py through ui_renders.py. Model-Agent PR 1126 (merged), allow lines PR 1127. Design wires the Build and Starter windows and adds the duplicate-image spec; Gameplay's store-setup action "icons" (PR 1128) sets pass and product pictures on dev, live only on Derek's word. Ids are in the issue 1122 comment.

HUD coin: Derek's library coin now has a star on its face in place of the money sign (Derek 2026-11-27 12:50 PM ET, after a side by side: "star is fine"). hud_coin_star.py, PR 1132, group upload 108922632736355 replaces 116447888023490; Design swaps Icons.Coins. See [[ui-icons]].

Group upload ids (2026-11-27, upload-asset runs 46033517259 to 46034487988): Build BrushTable 134838156181235, Dryer 113752193949870, BubbleBath 119011776128951, Pawdicure 103012559669119, SecondTub 107311962709814, ThirdTub 70697308780805, FourthTub 127426724307729, Garden 123151974285073, CatHotel 118129881118187, HotelRoom3 91255774144520, HotelRoom4 79200153366694. Tool BubbleSoap 130017740181643, ProBrush 73568133107511. Bow Silk 95988167326795, Satin 128022272665511, Golden 113725361249226. Crate1 121200477147545, Crate5 84617473865317. Finish1 118527438367209, Finish2 122466714749088, Finish3 125135618207829, Finish4 95331701140704, Finish5 99864922299941. Coins2x 71955337810834 (replaces 113360699781391), Coins3x 118344697143431 (replaces 114423850933764). Gameplay set all 14 buy prompt pictures on dev the same day; live waits for Derek.
