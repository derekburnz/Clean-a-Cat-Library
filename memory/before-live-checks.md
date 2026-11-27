---
name: before-live-checks
description: What must happen before tubBuilds, crateShop, the gift stand and onboardingFunnel go on LIVE (Review-QA and Growth notes, 2026-11-25 ET)
metadata:
  type: project
  modified: 2026-11-26T16:13:51.321Z
---

Moved out of the index 2026-11-26, text unchanged.

- Before tubBuilds goes on LIVE (Review-QA on PR 581, 2026-11-25): saves with Brush Table, Dryer, Bubble Bath or Pawdicure built lose them under tubBuilds plus dirtLevels; refund those coins once or count them as tubs first. The Second Builder pass (518) must lift the one-builder check to 2. BOTH DONE 2026-11-26: refund merged in PR 812 (save map oldRefunds, once, only while tubBuilds and dirtLevels are both on); the builder check reads PassService SecondBuilder.
- Before crateShop goes on LIVE (Review-QA on PR 617, 2026-11-25 ET; updated 2026-11-26 evening): the TEAM now makes CrateOne (49), CrateFive (199) and every other pass and product with the keys (store-setup workflow, PR 852), on dev now and on live on promotion day; Derek's signed in browser is the fallback. Derek still does the maturity questionnaire himself, LAST, and it must declare paid random items before crateShop goes on live. Review-QA's policy check of everything sold is written (docs/reviews/2026-11-26-policy-check.md, PR 797); recheck it once real ids are in. Starter product name must match the in-game card (Spa Starter Pack). Private servers 25 Robux a month, set on promotion day.
- Gift stand (PR 639, 2026-11-25 ET): Derek chose favourite plus group as the gate for the free pet; it stands unless he changes it. No official Roblox rule bans or allows rewarding a favourite (Growth-Agent/like-group-rewards-check-2026-11-25.md); only our house skill (monetization-policy section 3) says never reward likes or favourites. Cite only sourced Roblox rules; never switch an owner decision on our own reading.
- Analytics (2026-11-25 ET): funnels onboarding_v1 (10 steps) and playtime_v1 are on main behind onboardingFunnel (ON in dev, OFF on live). Growth-Agent keeps the name onboarding_v1; rename to v2 only if a step changes after live logs. When onboardingFunnel goes on live, tell Growth-Agent the exact minute.
- gradeStars (PR 870, 2026-11-26): set it ONCE before public release. Stars saved under one setting count 3x differently under the other (on: existing saves drop a tier; off after use: tiers come early). Not a rollback switch after release.

**How to apply:** read this before any switch here is promoted to live. Live needs Derek's own word in any case.
- Promotion day list is GitHub issue 893 (filed 2026-11-26 by Review-QA): live passes and products, server size 6, private servers 25, live notify, questionnaire before crateShop, gradeStars once, oldRefunds, store art and description. Tick lines there.
- wideStreet and bigSpa (Review-QA on PRs 972 and 974, 2026-11-26 evening ET): six plots on the wide street are about 3,040 parts. They need a phone frame rate run (iPhone 12, 30 fps or better) on dev before either goes on live. Both are read when the street is placed, so they need a new server once flipped.

- Asset ownership (Derek 2026-11-27): all 202 ids are owned by group 107520049 (asset-permissions owners run 46006962117). Use was granted on dev (46005763168) and, on Derek's "1.", on live (46007433635), 202 of 202 each. check.yml fails any PR that adds an id the group does not own (PR 1074). After any new upload lands, run the asset-permissions grant for dev, and for live at promotion.
- starterPet (PR 1094, Midas the Epic golden pet in the starter pack): before it goes on anywhere, Design's card and the pack window must list Midas. If the live Roblox product description lists the pack contents, Midas goes there too, on Derek's word only (Review-QA 2026-11-27).
- catHotel goes on together with noVipRoom (on dev and live): with catHotel on and noVipRoom off there is no Garden at all (Gameplay, PR 1102 review 2026-11-27). hotelNotify live id is still empty; live sends nothing until the notify-key hotel_ready string is made on Derek's word.
- Buy prompt pictures (issue 1122, PR 1128): set on dev 2026-11-27 11:33 AM ET by store-setup icons, runs 46034081380, 46034156476, 46034250875, 46034343923 (14 of 14, HTTP 204; plan 46034008747). Live: same action at promotion, only on Derek's word, at most 4 keys per run (only input), stop at the first failure.
