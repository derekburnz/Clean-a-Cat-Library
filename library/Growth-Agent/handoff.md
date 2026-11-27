# Growth-Agent handoff (2026-11-26 ET)

A brand new Growth-Agent starts here. Then read Growth Agent.md (lane and rules), Setup/3-working-rules.md and the five skills in .claude/skills on derekburnz/Clean-a-Cat (roblox-publishing-discovery, roblox-release-operations, roblox-policy-compliance, monetization-policy, devlog).

## State
- Game: Clean a Cat, a cat spa on Roblox, owner Derek (Eastern time). Design agreed in docs/design/clean-a-cat/gdd.md (Planning-Agent finished). Everything goes to dev first; nothing live or social without Derek.
- No build is live, so our own benchmark has not started. benchmark-sheet.md holds the rival games (animal spa list with player counts from 2026-11-23) and the empty own benchmark; D1 target 15% or better.
- Funnels: funnel-spec-onboarding-v1.md. Built in PR 437 (onboardingFunnel on in dev, off on live); name stays onboarding_v1; skip and pack events later. events-spec-2026-11-25.md lists every side event, max 3 custom fields. pack_offer_shown fires when the pack button first shows (PR 617). Dev data before PR 437 is test data.
- Issue 530 (events, questionnaire answers, private server note): comments posted; answers written; waits on Derek for the game settings. Issue 531 policy check: monetization-calls-2026-11-26.md has the table and 12 point checklist. Issue 106 store art v2 and 500 second thumbnail: not mine to build (Model-Agent), I do copy and tests.

## Derek's decisions (his words in Planning-Agent/playtest-notes.md and Planning-Agent/open-questions-2026-11-26.md)
- Money: five passes (2x Coins 199, Second Builder 299, Golden Sponge 99, Lou 249, Second pet slot 249 for the player and every worker); crate 49 and 5 for 199 (random, odds shown, PolicyService); Finish now tiers 5, 15, 35, 75, 99 (5 min or less, 30 min, 2 h, 8 h, over 8 h) on any build; Starter Bundle 199 (parts 547, shows 63% off, real 72 hour server clock from first join, gone for good); private server 100 Robux a month (Plus subscribers get it free from Roblox). Prices are mine to tune from sales ("do whatever prices").
- Gift stand: one fixed pet; the favourite and the group are checked, the like is asked and never shown as checked. Derek decided rewards for likes are in. No Roblox page allows or bans it, a small unconfirmed risk he took. Like ask rule (his): good moments only (special visitor's cat finished, crate opened, 3 star card, helper hired), one ask a visit, no re-ask for 3 visits after a no, never within 2 minutes of a lost cat or cancelled purchase, an ask after a purchase allowed at least 2 minutes later and switchable. Like row wording: "A gift either way, 150 coins".
- Store: icon A main, E the only alternate for now; second thumbnail half dirty and half clean; "cat spa" in the description; Christmas probably the first event, Cat Show kept in the vault. Dev set of passes and products first, live set at promotion; both games' ids go to Gameplay-Engineer.
- Server size six. Voices: use github.com/debpalash/voicestudio, never ElevenLabs.

## Files (all in Growth-Agent/ in the shared folder; Sync-Agent copies to the library)
store-copy-2026-11-23/store-copy-draft.md (title, description for the agreed design, passes, icons, thumbnails); starter-pack-check, crate-monetization-check, paid-skips-check, shop-weight-and-helper (2026-11-25); like-group-rewards-check-2026-11-25; glorybound-like-reward-2026-11-25; like-ratio-and-ask-timing-2026-11-26; private-servers-check; maturity-questionnaire-answers; events-spec; owner-settings-list; monetization-calls-2026-11-26; new-tag-in-title-2026-11-24 (plain name, no "[NEW]"); video-notes-2026-11-24; funnel-spec-onboarding-v1; benchmark-sheet.

## Open items
1. First benchmark when a live build exists: write the stop lines before the first read.
2. Read the like percentage and vote count weekly (with the date) and each ask moment's ask_answered numbers.
3. Day 2 return of players who skipped the first long build versus those who waited (events-spec).
4. Check the Starter Bundle's effect on single pass sales; check first-minute quits before and after the pack button and the gift stand switches.
5. Store art: contact sheet to Derek before any upload; nothing uploaded without his OK.
6. Voice studio repo: not run yet; read its installer script before running anything, do not pipe it to a shell blindly.
7. GloryBound's own ask method is unknown; only a player past the first sessions can tell.

## Lessons learned
- Public Roblox pages work through the web fetch helper (and Claude in Chrome for pages it refuses); a plain curl to Roblox is blocked. Roblox search API gives live players and votes. A couple of Roblox docs pages 404 or redirect to maintenance; say so instead of guessing.
- Reels were read from a logged out browser: only captions and comments, no voices. Use Derek's signed-in browser only when he says so.
- Mark every claim OFFICIAL, SEEN, DEV (developer opinion) or JUDGMENT. Say "not confirmed" when no Roblox page allows or bans something.
- A fixed price on a developer product means price tiers, not a moving price. A bundle must hide for owners of a part. A countdown is only fair if accurate, server owned, never restarting and gone for good at zero.
- Passes cannot be deleted: create each after the code is merged.
- The coordinator pushes idle threads: when idle, take the next lane issue, write a check or spec file, and message the other thread directly.
- Only the shared folder is writable from this thread; the library repo is copied by Sync-Agent. Put a copy of memory notes in Sync-Agent/incoming/.


## Update 2026-11-26 evening (new Growth-Agent)
Read everything above. Events spec now lists the real ask ids and the like ask id gap (see its update section). No unclaimed growth issue is open: 530 waits on Derek's game settings, 531 policy table is done in monetization-calls-2026-11-26.md, 106 is Model-Agent's art. Tools and tasks list is in Growth Agent.md section 9.

## Standing rule 2026-11-26 ET evening (Derek)
No fur clumps or puffs (tangles and fluff, PR 831 rework) in any ad, thumbnail, icon, video or social image. They stay in the game only. Check every promo frame.

## Overnight status 2026-11-27 (Growth-Agent, for Review-QA's morning report)
- Done: store description text ready (store-copy-draft.md, update 2026-11-26; issue 892 waits on Gameplay-Engineer's tools PR and the account); like how-to pop up spec (like-howto-popup-spec-2026-11-26.md, issue 869, copy updated for the heart icon; build waits on Design-Agent and Model-Agent PR 976); appeal note for the suspension (appeal-note-thumbsup-2026-11-27.md); Open Cloud "User is moderated" write-up; reel notes; store video and social footage reviewed.
- Promo check 2026-11-27 4 AM ET: final store video (14.3 s) and the six store art files, viewed frame by frame: no fur clumps or puffs, no HUD, no prices, no hand icons. One pale green square (the scrub sponge, real gameplay) shows in seconds 2 to 3 of the store video; Motion-FX kept it on purpose. Social footage: same check passed earlier; re-cut not seen since. I did not see the new image gate's rules, so I did not apply them; no promo piece contains the three retired hand icons.
- Not done, on hold by order: any upload or change on store or social pages (store page art and icon E, issue 901, stays declined tonight); the page thumbnails are still not on the game page (key route failed).

## Update 2026-11-27 afternoon ET (Growth-Agent, for a new account or thread)
Done and merged in the game repo: go-live checklist (PR 998, issue 893), plan pages events/questionnaire/private servers/owner settings (PR 1004, issue 530), speed budget street numbers (PR 1006, issue 182), launchSale end date line (PR 1048), shop layout research (PR 1072, issue 1070). No branch of mine has unmerged work.
Open issues in my lane: 1066 store page folder (waits only on the image gate for detail-07 and detail-08, then refresh GATE-STATUS.txt and tell Sync-Agent to recopy that file); 901, 851, 106 store art (Derek drags files in; check the game pages after); 869 like how-to (Design built it, likeHowTo on in dev).
Store page folder: Growth-Agent/store-page-uploads/ (3 sets, README with Roblox slots and order, GATE-STATUS.txt, phone-size-check.png). On Derek's PC at C:\Users\Derek\Downloads\games\Clean-a-Cat\store-page-uploads. Icon: A with or without title (my pick with title); icon E stays a spare (A alone until launch, then A against E as an Experiments test). Detail page order 01 to 08, homepage thumbnails 1 to 4 (Home Page tab, 2 to 5 active, under 3 MB). Nothing was uploaded to Roblox by us; Derek drags them in.
Monetization research (price-aware, never into a public repo): Growth-Agent/monetization-research-2026-11-27.md. Handed to Design-Agent for shop layout 1030 and the starter pack card. My answers to Design: keep the starter pack at 199 (no evidence 249 converts better); Second Builder is fine only if usable in the first session, else Lou; separate pass prices must stay live; show Owned.
Derek's answers (via Design-Agent): like coins kept as is then replaced by issue 1111 (one free reward board: group join verified, like asked apart, no reward for the like); gift crate for group join only; starter pack 72 hours, no clock shown, chip "New player offer" (1069); game links: group only; icon A alone until launch; sale ends only when he says (Review-QA asked him for a date).
Gift board wording check (issue 1111): fine; like line apart below a divider, no tick or timer, Verify mentions only the group. Logged in like-group-rewards-check-2026-11-25.md.
Still Derek's: server size six (done), private server price set once, questionnaire (answers ready), drag store art in, game links, his word to go live.
