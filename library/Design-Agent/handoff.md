# Design-Agent handoff (rebuilt by Sync-Agent, 2026-11-26 ET)

The Design-Agent thread was deleted before it could hand off. Sync-Agent rebuilt this from GitHub (PRs and issues on derekburnz/Clean-a-Cat) and from the shared Design-Agent folder. Items marked UNCONFIRMED could not be checked from those sources. A new Design-Agent: read this, then `Design Agent.md` (lane and rules), `gdd.md`, `docs/decisions.md`, the `ui-review` skill.

## Lane in one line
Design owns `games/clean-a-cat/src/client/UI/` and `assets/clean-a-cat/ui/screens/` (HTML mockups first, then the Luau port), plus design docs under `docs/design/clean-a-cat/` (gdd.md, tuning.md). Every screen ships behind a switch in `src/shared/LiveFlags.luau`, off by default. Mockups for Derek live in the shared folder `Design-Agent/<topic>-<date>/`.

## Derek's UI calls of 2026-11-26 (after he played dev on his phone)
- Main HUD grid is 2 by 2: Shop, Build, Helpers, More. Helpers shows once one is hired. More opens a cream tray with Quests, Gifts, Pets, Index and Settings. A dot on More shows when a tray button has a note. (switch `hudTidy`, PR 747)
- Coins sit on a cream pill with an ink edge, moved up 12 design px; the friend tag is under it. The coins used to look like they hover.
- No cat bubbles: the waiting faces are hidden (`HUD/Waiting`).
- At most two prompt bubbles near the boards and door, the nearest within 10 studs; a winning pill such as the door's Take cat shows at any distance (switch `fewerPills`, `Spa/PillLayout.keep`).
- Starter pack is a small side ad under the coins (`HUD/StarterAd`), not a gift button: ribbon, three items, struck-through shop total, price, "SAVE N%" and a calm time chip. Price is 199 Robux (PR 756 changed 299 to 199). The numbers are computed from live prices and hidden if any price is missing (`StarterViewRules.saving`); they must stay true. Derek asked for "500% value" and was told that is false for this pack. UNCONFIRMED: the exact saving percent shown now, since the price change; read `StarterViewRules` and the pack parts (547 shop total).
- Build window (`buildWindow`, #751): a Build button opens "Build and upgrades" with builds (price, time, countdown, Built) and tool and bow upgrades. No Robux in the window; Finish now stays on the board.
- Like row wording on the gift card: "A gift either way, 150 coins" (the like is asked and never shown as checked; only favourite and group are checked, and ticks only on those). Free gifts card title is "Free gifts" with rows: Like (10 s wait, then Claim), Favourite, Join the group, Play 30 minutes. (switch `freeRewards`, PR 732 client, PR 733 server)
- Counter cards (switch `counterCards`, needs `counterLine` and `heartBar`): each cat on the counter has a small card with an owner chip in the owner's shirt colour and a heart bar (mint full, gold under 60%, coral at the grumpy point), and the mat takes a pale wash of the owner's colour. Nothing on the card is pressable. PR 767 merged; PR 774 makes the card a fixed 84 by 26 px, alternates every second place 1.9 studs higher, FAR 32, and retries once when CounterPlace arrives for newcomers.

## Merged Design PRs (all 2026-11-26 unless noted)
682 Fuse takes its own taps again; 689 Comfort strong tables; 691 wash meter cheer pops on the bar clear of the cat; 693 Helpers window (level up, mode, rename; issue 526 item 3); 707 HUD icons (Quests, Shop, Pets, Crate, Bow, Helpers pictures); 718 Helpers fixes 697 and 698 plus HUD buttons arrive motion (switch `buttonArrive`); 727 Leave lines (two true friendly lines around Roblox's leave screen, #726); 732 Free gifts client; 747 HUD tidy, starter ad, Build window, fewer pills; 756 like row first line and the 199 starter price; 767 counter cards. Issue 526 (screens for the agreed design) closed as completed 15:41 UTC.

## Open Design work (updated by the remade Design-Agent, 2026-11-26 4:40 PM ET)
- Done since the remake: PR 793 (issue 784, round cheek ids for Suds and the two staff HUD pictures), PR 798 (issue 794, real portraits for all 20 cats: `Portraits.IMAGES` holds `<Cat>` and `<Cat>_Dirty1`; `Portraits.imageFor(cat, dirt)` falls back to the nearest lower level; the bench card passes `card.dirt`), PR 817 (issue 816: the away notification is build finished, not tip jar full), PR 824 (issue 822: the Build window changes only the countdown words, `BuildViewRules.sameShape`), PR 829 (issue 825: grey Buy when unaffordable, `BuildViewRules.markShort`). PR 774 (like ask card) merged earlier.
- Waiting: dirt levels 2 to 4 portraits. Review-QA held them (flaps at the sides, issue 791). Model-Agent's rework PR 831 then re-renders Dirty1 to Dirty4 into shared `Model-Agent/ui-renders/faces-dirt-2026-11-26/`. Next: copy them to `assets/clean-a-cat/ui/icons/portraits/CleanACat_UI_Portrait_<Cat>_Dirty<n>.png`, Review-QA look, group upload by Gameplay-Engineer (upload-asset.yml from this thread's branch), add the ids to `Portraits.IMAGES` (replace the Dirty1 ids if level 1 changed).
- Waiting: Sync-Agent's dev check that the PR 793 and 798 pictures draw (a blank tile means moderation).
- Copy handed to Gameplay-Engineer for BubbleRules: issue 814 "notify" (Want a heads up? / We'll tell you when a build is done. Once a day at most. / Sure!) and issue 815 "favourite" (Find us again! / Favourite the spa to find it fast next time. / Favourite). No reward named.
- Motion-FX agreements: helper popup pop (PR 807), counter card grow only on a cat's first card (PR 808, switch counterCardFx), springUi open 85 percent to 1 in about 0.13 s with no overshoot and an instant close, no More tray pop (PR 811), coin pill bump (issue 826: no pill sound on helper pay, sound at most once every 2 s, no double bump inside 0.5 s).
- Mockup portraits under `assets/clean-a-cat/ui/screens/img/` are the round cheek renders.

## UI file map (`games/clean-a-cat/src/client/UI/`)
init, Kit, Window, Motion, Comfort, Portraits, Spotlight; windows: Shop, Starter, Crate, Pets, Helpers, Queue, Settings, QuestBook, CatIndex, CheckinCard, Recap, RenameCard, GiftCard, BuildWindow, HelperPopup, LeaveLines, SudsBubble, CounterCard; HUD/: init, SideButtons, StarterAd, Waiting, WalkButton, WashMeter, StepList, TipLine, HeldTool, Icons. Pure rules sit in `src/shared/*Rules.luau` with specs (BuildViewRules, GiftViewRules, StarterViewRules, CounterCardRules, LikeAskViewRules, BubbleRules).

## The gate and the habits
- `./check.sh` (or check.ps1) from `games/clean-a-cat`: analyze (src and tests), selene, stylua, tests (612 on PR 774), and `uigate` at four screen sizes with named scenes (new screen means a new scene).
- Nothing under 14 px, prices before any confirm, no window opens by itself, no button in the bottom right corner (Roblox's badge note appears there), HUD numbers are outlined text, only pressable things look like buttons.
- Starter-pack and like wording go through Review-QA; "no reward named" for likes (monetization-policy, issue 748).
- Test devices: iPhone 12 is Derek's weakest (Studio stands in with the iPhone 13 frame 844x390), iPad about 2020. Check phone, tablet, desktop, console.
- Picture and Studio checks are done by Sync-Agent (the only Studio driver); ask it for a run with the commit and the exact things to look at.
- Mockups for Derek: HTML or PNG into shared `Design-Agent/<topic>-<date>/`; he wants questions he can answer in words, no more asks for screenshots.

## Lessons (from the shared notes and PR reviews)
- A UIGradient on a text label tints the text; put the letter on a child label.
- Size cards in px, not studs, for phone legibility (the counter card at 43 x 13 px).
- A neighbour's card must never cover another; stagger.
- A tutorial target can open something on touch; check.
- Merge main into a PR that adds a switch to `LiveFlags.luau` before arming it (the lists collide), and keep one entry per key.
- The thread had a one-branch habit (branch claude/project-thread-997ym5): check the PR merged before resetting the branch.
