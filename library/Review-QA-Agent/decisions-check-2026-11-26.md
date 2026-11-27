# Decisions check: is everything Derek decided being built? (Planning-Agent, 2026-11-26 6:08 PM ET)

Derek, 6:04 PM ET: "looks like lots of prs failing/having issues look into that and make sure the old updates that were done to things like spa size/answered in the plan are getting worked through".

For Review-QA-Agent to verify against main and the dev switches. One line per decision that needs something built or set. Sources are the memory answer files (derek-plan-answers, derek-money-answers, derek-evening-answers, derek-nov26-answers, derek-nov26-setup-answers, bigger-spa-counter, cat-faces-and-bows, customers-and-carriers) and the plan page database (169 docs, read 6:06 PM ET). His words in full: `Planning-Agent/playtest-notes.md`.

How to read a line: the issue and pull request numbers are the ones I know from memory, the milestone list and the issue titles. I did not open the code. **Closed does not mean built as he asked**, so each line still wants your look. Switch names come from `LiveFlags.luau` on main (cf33eb4 or later); where I guess, it says "guess". **FLAG** marks a decision with no issue I can find, or one where I see a reason to doubt it.

Issue list read 6:05 PM ET: 299 issues, 20 open. Open pull requests: 876, 864 and the draft 797 (QA docs, from a thread that was remade at 3:43 PM ET, so it may be stale).

## 1. The flags, first (11)

| # | Decision | Why it is flagged |
|---|---|---|
| F1 | **Bigger spa and the counter window** (his 9:10 AM words, issue 746). He wrote at his 6 PM playtest: "dev is still on the old model where people line up at door and not in the open window and place their cats on the table" | Issue 871 says his view was a Studio test with no switches. Needs a fresh join on the real dev game to prove bigSpa, counterLine, counterCards and counterCrate show. Bugs 872 (no Take prompts after a join) and 871 (floating cats and carriers) are open. Issue 773 (phone frame rate run with six bigger plots, 2,585 parts) is still open and is the gate for bigSpa reaching players |
| F2 | **Full recap card after every cat** (q2-recap, evening of 11-25) | Issue 868 says "The full recap card still covers the first three customers", and a side strip (recapSide, issue 299) exists. Check what a player sees after cat 4 and later. If it is the strip, that differs from his answer and needs an issue or his word |
| F3 | **Human builder**, not the hard hat kitten (q2-builder) | No issue found. Issue 20 built a builder kitten earlier. Check who stands at a running build |
| F4 | **"cat spa" in the store description** (q2-catspa) | No issue found. Issue 851 covers pictures only. Growth-Agent owns the store text |
| F5 | **Alternate icon E** | No Open Cloud route (issue 851). Derek at 5:47 PM ET on the page: "you can do that". So it is ours, through his signed in Chrome, which he named for store art at 5:20 PM ET. No issue yet |
| F6 | **Promotion day jobs**: live passes and products, server size six on live, private servers 25 Robux, live notification string and secret, the questionnaire check before crateShop | No single issue. They sit in memory (before-live-checks) and the workflow of PR 852. One "Promotion day" issue with needs-owner would stop them being lost |
| F7 | **Head piece cats, game side**: BowFit must multiply by the cat's BowScale | Named inside model issue 845 only. No gameplay issue of its own |
| F8 | **Starter product name**. Before-live note says the Roblox product name must match the in game card "Spa Starter Pack"; issue 850 made "Starter Bundle 199" | Check the name the key made against the card |
| F9 | **Notification ask at 1 to 2 minutes** (q2-notifyask, built as notifyAsk at 1:45, issue 814) | His 6 PM playtest note changes it: "wait until they build something to ask this one" (issue 877, contextAsks, open). The old answer is superseded; the design doc needs the new timing once 877 lands |
| F10 | **Every carry and pose works on R6 and R15** (his decision card, 11-24) | Only the held kitten has issues (361, 378). No check of the customer cat carry (customerCarry) or counter pick up on R6 that I can find |
| F11 | **First event, likely Christmas** (q2-event) | No issue. Not due until the game is close to done; listed so it is not forgotten |

## 2. Core play (answers of 11-24 and 11-25)

| # | Decision | Issue, pull request | Switch or code name |
|---|---|---|---|
| 1 | Busy spa and cat collection together | 506 to 531 (milestone 1) | many |
| 2 | Waiting cats are picked from a menu, plus a next in line button; polished and easy | 201, 246, 299, then 746 (taken from any counter place) | queuePick, queueWindow, counterLine |
| 3 | Pay = base x speed stars x how soon taken x dirt. Big bonus inside the first 10% of the heart bar, no penalty for a normal wait | 507 | heartBar, dirtLevels |
| 4 | A cat whose heart bar is empty turns grumpy and leaves; the job is lost | 507 | heartBar |
| 5 | Never sell a way to keep a leaving cat, never show a price while a cat is about to leave | none of its own (rule) | check finishNow and shop prompts near a leaving cat |
| 6 | Helpers take the next cat of ANY rarity, earn much less, are slower on dirtier cats, each has a mode (about to leave, rarest, dirtiest, first in line) | 509, 696, PR 693 | workers, helpersWindow |
| 7 | A worker comes with their station in one purchase and shows a progress bar over the cat. Suds never helps | 509 | workers |
| 8 | Jo and Sam cost coins; Lou is the Robux pass and comes with his station | 509, 518, 841 (Jo 300) | workers, passes, joPrice |
| 9 | Players can rename staff, through Roblox text filtering | 487, 669, 697 | staffRename |
| 10 | Helpers have no XP; levels cost coins; the popup shows coins only | 743, PR 744, 801 | helperPopups, helperPopFx |
| 11 | Special visitors appear and expire, only the player washes them, their cats have their own index page | 510, 524, 587 | specialVisitors, catIndexWindow |
| 12 | The FIRST special visitor is scripted inside the first 5 minutes and drops a crate; later ones drop one only rarely | 510 | specialVisitors |
| 13 | No tool menu: the tool changes by itself | not known to me | autoTool, toolOnCat |
| 14 | All step kinds from the start, 3 to 10 steps by dirt; the tutorial uses only the simple 3 or 4 | 506, 267 | dirtLevels, bubbleBath, pawdicure. Check a dirtiest cat really reaches up to 10 steps |
| 15 | Area steps (foam, rinse, trim) get a top bar, full at about 90%, then a shake off | not known to me (built 11-25) | washMeter, latherFoam |
| 16 | The cat turns by itself when a side is done | 82 | scrubTurn |
| 17 | Each wash step takes about 4 to 5 seconds (5 seconds was the plan; he repeated it at 5:56 PM ET) | 865 (closed) | washPace. To be timed on the iPhone 12 |
| 18 | Pets: one for the player, one per worker; Suds is never a pet; doubles are kept and three fuse into a star up | 511, 512, 634, 678 | pets, petsWindow |
| 19 | Every pet can be earned without paying | rule | check the crate lists |
| 20 | Earlier builds are really good; more to build on day one; long builds exist | 515, 579, 660 | tubBuilds, builds, buildWindow |
| 21 | Seven day check in card, no streak; the free crate on day 2 is a good one | 517, 627 | checkinCard |
| 22 | Tip jar fills while away | 517, 71 | tipJar |
| 23 | Daily quests (reset per player each day) and weekly quests; finishing ALL weekly ones gives a crate | 516, 624 | quests |
| 24 | Saves shaped so a Grand Reopening can come later; not at launch | 523, 551 | SaveSchema |
| 25 | Friend bonus yes; no trading; no friends as customers | 520 | friendBonus. Check nothing trades |
| 26 | Other players can walk into a spa, ON by default, with an owner setting to turn it off; a visitor can never act there | 520 | visiting |
| 27 | Asks never all at once; never interrupt a wash | 522 | askQueue |
| 28 | HUD buttons arrive one at a time, each with a tip; final grid Shop, Build, Helpers, More (Pets, Quests, Gifts, Index, Settings in More); coin pill moved up; no waiting faces | 522, 738, PR 747, PR 754, 873 (open) | buttonArrive, hudTidy |
| 29 | At most two prompt pills within 10 studs; fewer white bubbles | 745 | fewerPills |
| 30 | Build and Upgrades window from the HUD | 751, 822, 825 | buildWindow |
| 31 | Phones locked to landscape | 522 | landscapeLock |
| 32 | A bow on every cat as an easy last step that adds money, with bow upgrades; workers tie none | 508, 501, 441 | bowTiers |
| 33 | Suds: mascot on four paws, first cat washed, never washes, not in the index; a bubble along the bottom explains | 278, 285, 299 | sudsMascot, sudsWash, sudsBubble |
| 34 | Opening starts the moment the character loads: truck, box falls, no loading screen, no standing still; camera version A; the player carries the kitten to the tub; a close up wash view teaches the steps | 279, 281, 285, 336, 337, 346, 406, 541 | openingBox, carryHold, washView, placeAfterHop |
| 35 | No stink wisps; darker mud on dark fur | 326 (stinkEffects deleted) | none |
| 36 | Washed cats fill an index; customer cat names from the draft list, Cat Cafe names and looks allowed for rare ones | 36, 238, 524, 527 | catIndex, catIndexWindow |
| 37 | Never write "working cats" in any text | rule | grep the UI strings |

## 3. Money (11-25 and 11-26)

| # | Decision | Issue, pull request | Switch or code name |
|---|---|---|---|
| 38 | Robux crate: 49, five for 199, no daily limit, chances shown as percentages before purchase, PolicyService per player, hidden from restricted players | 514, 650, 658, 668, 836 | crateShop, crateWindow |
| 39 | Earned and bought crates are the same crate; coins never buy crates; no Robux product gives coins; the "unlucky run" crate is removed | 511, 514 | check Products and the crate grants |
| 40 | Finish now on EVERY build, the first long build and short ones too. Tiers by time left: 5 under 2 minutes, 15 up to 1 hour, then 35, 75, 99. Small button, hidden under 15 seconds, no pop up | 515, 679 | finishNow |
| 41 | Five passes: 2x Coins 199, Second Builder 299, Lou 249, second pet slot 249, Golden Sponge 99 | 518, 810 (Second Builder lifts the builder limit) | passes, PassService |
| 42 | ONE second pet slot pass opens a second slot for the player AND every worker | 518 | petsWindow second slot mode |
| 43 | Starter pack: Golden Sponge + second pet slot + 2x Coins, 547 struck through, **199 Robux, "save 63%"** (never 64), only for players who own none of the three, no crate and no coins inside | 519, 739, 857, 635, 636 | starterPack, hudTidy (side ad) |
| 44 | Starter pack clock: a real 72 hours from first join, kept on the server, never restarts, gone for good at zero; a small button, no window opening by itself | 519 | starterPack |
| 45 | We make the passes and products with the keys; ids per game | 850 (closed), PR 852 | Passes.IDS_BY_GAME, Products.IDS_BY_GAME. Check the dev ids are in and a dev purchase prompt opens |
| 46 | Server size six | 850 (dev); live on promotion day (F6) | game setting |
| 47 | Private servers 25 Robux a month, set once on promotion day | 846, PR 848 (design only), F6 | game setting |
| 48 | Old stations refunded once before tubBuilds goes live | 810, PR 812 | oldRefunds |

## 4. Asks, likes and the group reward

| # | Decision | Issue, pull request | Switch or code name |
|---|---|---|---|
| 49 | Gift stand: favourite and group are checked, the like is asked and never faked as checked; "obvious to find" | 521, 502, 655, 659 | giftStand |
| 50 | Free gifts like row: first line "A gift either way, 150 coins", the 10 second wait stays | 730, 748, 837 | freeRewards |
| 51 | New at his 5:45 PM playtest: the group reward is a gift crate to open, not the plain Starcoat pet | 859 (open) | giftCrate |
| 52 | New at 6:01 PM: a short pop up while the 10 seconds run, with a looping how to like picture | 869 (open) | not built |
| 53 | Like ask after a good moment (a special visitor's cat finished), once a visit, no re-ask for three visits after a no, never within two minutes of a lost cat or a cancelled purchase | 795, PR 799 | likeAsk, LikeAskRules |
| 54 | Like ask also two minutes after a finished purchase, never on the buy screen, own switch | 813, PR 818 | likeAskPurchase |
| 55 | Favourite reminder on the second visit or after 10 cats for players who skipped the stand | 815, PR 820 | favouriteAsk |
| 56 | One build finished notification a day; dev string build_done and the group key as secret; live on promotion day | 38, 816, PR 796, F6 | longBuildOffer, NotifyService |
| 57 | Joining the group for a good reward "should be a thing" (5:22 PM ET) | 521, 859 | giftStand, giftCrate |

## 5. Models, looks and the spa building (11-25 and 11-26)

| # | Decision | Issue, pull request | Switch or code name |
|---|---|---|---|
| 58 | Bigger spa building (room 48 by 32 studs, plot spacing 56) | 746, PR 753, PR 763, 773 (open) | bigSpa. See F1 |
| 59 | Waiting cats sit on a counter at an open window by the desk, with a heart bar and a clear owner, taken from any place | 746, 745, PR 752, PR 762, 853, 872 (open) | counterLine, counterCards, counterCardFx |
| 60 | Customers walk up with the cat in its carrier, set it on the counter, the cat walks out and sits, the carrier fades | 757, PR 765, 828, 871 (open) | counterCrate, counterSounds |
| 61 | Customers reworked: look and walk in | 446, PR 460, 479, 484, 874 (open) | townsfolk, customerWalk |
| 62 | Cheerful carrier with no bars | 449, PR 458 | CleanACat_Prop_Carrier |
| 63 | Bows sit on the top corner of the head, tipped, like the store icon | 764, PR 770, 773 (open, dev look owed) | BowSlot, BowFit |
| 64 | Ten head piece cats: a smaller bow on the top right corner, not at the side | 845 (open), 782 (the old side spot) | BowScale. See F7 |
| 65 | Cream cat's mouth fixed; cheek strips are round cheeks on cats, customers and staff; uploaded pictures redone | 771, 776, 784, 794 | Portraits.luau, HUD/Icons.luau |
| 66 | Tangle clumps and fluff puffs must read as fur in the game, and never appear in ads, thumbnails or promo pictures | 791 (open, waits on the dev look), PR 831 | dirt.tangle_colours |
| 67 | Dirt levels on the dirty cats; six special customers' cats; the finished VIP Room with ten seats | 470, 471, 478, 486, 448, 688, 712 | dirtLevels |
| 68 | Human staff Jo and Sam in mint | 482 | workers |
| 69 | Store art: A main, E alternate (orange gone, bow tilted on the corner), thumbnails in his order 2, 1, 3, 5, the second one half dirty and half clean | 106 (open), 500, 851 (open) | store. See F4, F5 |
| 70 | Sounds uploaded in one batch; soft and cosy feel | 529, 800, 827, 828 | spaMusic, uiSounds, sudsVoice |

## 6. His playtest notes of this evening (5:45 to 6:04 PM ET), as issues

The coordinator counted about twenty notes in the chat. These are the issues I can find for them. Please check each note in the chat has one.

| His note, short | Issue, pull request | Switch |
|---|---|---|
| Starter pack card runs off the screen in Studio | 857 (closed) | hudTidy |
| Group reward as a crate | 859 (open) | giftCrate |
| No Walk or Buy during the wash; the wash on its own screen with a bubbly wipe, no HUD | 856 (open), PR 864 (open) | washScreen |
| Guide line back to the box; line blends into the floor | 861 (closed) | boxGuide, trailBold |
| Photo moment: red light, flash, print | 862 (open) | photoFx |
| Brushing too fast, 4 to 5 seconds a step | 865 (closed) | washPace |
| A 3 star wash gives +3 stars | 868 (closed), PR 870 | gradeStars. Set once before release (before-live-checks) |
| Like row pop up and how to picture | 869 (open) | none yet |
| Old door line on dev; floating cats and carriers; customer parts off the body | 871, 874 (open) | see F1 |
| Washed cat walks out on its legs, not bobbing while sitting | 875 (open), PR 876 (open) | catWalkStand |
| Pop ups only when they guide the next action; better special visitor pop up; arrows to a new crate | 877 (open) | contextAsks |

## 7. Not a build job, listed so nobody re-asks

RbxSync skipped. No new keys. Passes and prices are ours to tune. Playing like My Pet Salon is fine. No screenshots or recordings asked of him. Questionnaire: his, and at 6:04 PM ET he wrote "Lets leave for now dont worry about it yet"; it still must be in before crateShop goes on live. The word to go live: "Will do no need to put this on a todolist".

## Review-QA's first results (6:11 PM ET, from its note)

- F2 full recap after every cat: new issue 890.
- F3 human builder: new issue 891.
- F4 "cat spa" in the store description: new issue 892.
- F5 alternate icon E: noted on issue 851.
- F6 promotion day list: new issue 893.
- F7 built: BowFit reads BowScale.
- F8 fine: the dev product is named Spa Starter Pack.
- F9 covered by issue 877.
- F10 R6 carry check: new issue 894.
- F11 first event: stays unfiled until the game is near done.
- Also new: issue 881, Finish now edges.
