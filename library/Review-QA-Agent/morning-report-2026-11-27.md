# Morning report, Friday 2026-11-27

Written by Review-QA-Agent overnight and final at 6:30 AM. Times are Eastern.

## The short version
- Every issue Claude could finish is closed: 24 tonight. Only 4 are open, and each one needs you (listed below).
- The floating cats are fixed. Customers now walk in with the cat inside the carrier, set the crate on the counter, and the cat walks out onto its mat. When a customer leaves, the cat goes home in the carrier, as you described. Sync checked this in Studio.
- Helpers now walk the aisles to the cat's own counter spot, pick it up and carry it to their station without walking through anything.
- Everything is on the dev game, not live. The latest dev publish is main 66ae8fc, at 12:53 AM, and it is green. Live is untouched.
- 31 pull requests merged overnight: 973, 977 to 980, 982 to 987, 989, 992, 993, 995 to 1000, 1003 to 1006, 1008 to 1011, 1013, 1016 and 1018. Each got a review before merging. Nothing is waiting to merge.
- The hand icons are gone from the repos, and no hand image can be uploaded again (an allow list on every upload route). Four new images went up tonight, each checked first, with no refusal.

## Done and on dev
| Your ask | Issue | Result |
|---|---|---|
| Cats floating beside the line (drop-off out of the crate) | 871 | Fixed (PRs 993, 1008, 1010). Sync passed walk-in, counter and leave checks. |
| Helpers fetch the cat and carry it to their station | 884 | Fixed (PRs 1009, 1011). Sync passed: they stop behind the counter and cross nothing. |
| Spas further apart on the street | 887 | Six plots 84 studs apart with gardens between (wideStreet on in dev). |
| Map not a plain square | 885 | Hills, mountains and sky at full zoom; no edge or void. |
| Bows on the top right corner of head piece cats | 845, 948 | All cats pass, including Stardust's star tiara (24 fits clear). |
| Eight crate pets made really cool | 883 | All remade. Clover and Glitch portraits redrawn and uploaded. |
| Like how-to without hands | 869 | Heart and tap dot only, on in dev. |
| Recap "Next cat" off the bottom of an iPhone 13 | 991 | Fixed: rows go two per line on short screens. |
| No "Take cat" for a few seconds after the recap | 1017 | Fixed behind a new switch, tipTake, now on in dev. Sync: the wait went from 6.1 s to 0.5 s. |
| Starter pack ad showed a huge sparkle | 1015 | Fixed. |
| Bigger stations, arms, wash screen, small phone text, Android windows | 878, 874, 856, 838, 988 | Fixed and checked. |
| First loop under 10 minutes | 40 | Third customer reached at 6:11 on phone emulation. |
| Policy check of everything sold | 531 | No violation found (docs/reviews/2026-11-27-policy-check.md). Two of your own calls are flagged below. |
| Go-live checklist, analytics, speed budget | 893, 530, 182 | Written in docs/growth/ and docs/playtests/. |

One honest note: one fix tonight (PR 992) split some counter cats into pieces in Studio. I passed it in review and missed that. It was reverted within the hour (PR 1008) and never reached live.

## Switches set in dev tonight
wideStreet (with bigSpa), likeHowTo and tipTake. All are off on live.

## Only you can do these
1. **iPhone 12 run** on dev, at the lowest and highest quality: the wash, then the full street with six customers. This is the gate for wideStreet and bigSpa on live (30 fps or better). Steps are in docs/playtests/speed-budget.md.
2. **Store art:** drag in icon A, alternate icon E and the thumbnails in your order (2, 1, 3, 5). The files are in the shared folder Model-Agent/store-art/picked-2026-11-26/. Open Cloud cannot set them, and the upload from the other account was declined. This covers issues 851, 901 and 106.
3. **Is the scrub fun on your phone** (issue 29). Only you can answer it.
4. **Archive old images** in Creator Dashboard, Development Items, Images, Creampuff Games:
   - Hand icons: 76096338201947 and 121275029069381. Roblox already took down 135826908608436.
   - Old portraits: Clover 87691200049996 and Glitch 115707461545852.
   - Open Cloud cannot archive images.
5. **Dev restart, if you want one.** Running dev servers still have the old street layout, because wideStreet is read when a server starts. New servers get it anyway.
6. **When you are ready to go live:** follow docs/growth/go-live-checklist.md. It covers the questionnaire, server size six, the private server price and your word to publish.

## Two of your own calls the policy check flags (no change made)
- Coins for the like row, and the gift crate for favourite plus group join. Roblox has no clear rule on this, but the house rule says never reward likes. Re-check Roblox's guidelines before live.
- The 72 hour starter countdown is real and calm, but it is still time pressure on young players.

## Your account
The appeal is still pending. The game's group key is clean, and nothing tonight touched your account.
