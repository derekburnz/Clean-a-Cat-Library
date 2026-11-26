# Open questions for Derek, plan page version 48 (2026-11-26 9:32 AM ET, Planning-Agent)

Derek, 9:23 AM ET: "After done current updates give me an updated artifact for plan for anymore questions you might need as its easier to follow from there". The plan page (same link) now carries seven new questions and eight setup steps. His 65 earlier answers are untouched. Our pick is option 0 and stands if he leaves a question.

Answers save in the page database, collection `answers`: questions as `q2-<id>` (pick is the option index), setup steps as `c-s2-<id>` (done, note), the new done tick as `c-done2`.

| id | Question | Our pick | Who acts on the answer |
|---|---|---|---|
| packvalue | Starter pack ad number: true saving is 45% (547 of items for 299) | Keep 299, show SAVE 45%. Others: show SAVE 248 Robux; lower to 199 (true 63%) | Design-Agent (ad), Derek sets the product price |
| helperxp | Helpers have no XP, levels are bought with coins | Keep, popup shows coins only. Others: XP bar unlocks the level that still costs coins; XP alone | Gameplay-Engineer, Design-Agent (popup, issue 743) |
| likeline | Free gifts like row wording (issue 748) | "A gift either way, 150 coins". Others: keep "If you enjoy it"; copy the example game | Design-Agent; freeRewards stays off in dev until settled |
| likeask | Who is asked to like and when | After a good moment, once a visit, never after a purchase or lost cat, no re-ask for 3 visits | Gameplay-Engineer (askQueue), Growth-Agent's note like-ratio-and-ask-timing-2026-11-26.md |
| icons2 | Store icons | A main, E, F and B alternates | Model-Agent; Derek uploads |
| wheremake | Passes and products: dev and live are separate games, 13 things each | Derek makes the dev set now and the live set at promotion. Other: we make the dev set with the group key if it is allowed | Gameplay-Engineer (ids in Passes.luau and Products.luau, one id table today, so two games need two id sets) |
| notifykey | Notifications need a message and a key saved as the game's secret | One new key limited to notifications. Other: reuse the group key; no notifications at launch | Gameplay-Engineer (NotifyService) |

Setup steps (ids `s2-...`): passes, products, questionnaire, serversize, private, groupwall, storeart, computeruse.

Left off on purpose: the RbxSync comparison run (Derek said yes at 9:23 AM ET). The free pet gate (favourite plus group) stands as decided.

## Derek's answers, 2026-11-26 9:47 to 9:51 AM ET (read from the page 10:14 AM ET; he wrote "Answered the rest of plan questions" at 10:13 AM ET)

| id | His pick | His words | Same as our pick? | Passed to |
|---|---|---|---|---|
| packvalue | 2: lower the pack to 199 Robux, a true SAVE 63% | (none) | No | Design-Agent, Gameplay-Engineer, Growth-Agent, Review-QA |
| helperxp | 0: keep levels bought with coins, popup shows coins only | (none) | Yes | Design-Agent, Gameplay-Engineer |
| likeline | 0: "A gift either way, 150 coins" | "you choose rest just do the 10 second thing" | Yes | Design-Agent, Review-QA (issue 748) |
| likeask | 0: after a good moment, once a visit | "Good moment like rare customer cat finished. Maybe also after a purchase just a little bit after." | Yes, with a change: an ask a little after a purchase is allowed | Gameplay-Engineer, Design-Agent, Growth-Agent, Review-QA |
| icons2 | 3: something else | "Just use A as main and E as alt for now but fix the sides of E having orange sticking out the side of the model" | No | Model-Agent |
| wheremake | 0: he makes the dev set now and the live set at promotion | (none) | Yes | Gameplay-Engineer, Growth-Agent |
| notifykey | 1: no new key, save the group key as the game's secret | "Use the same key its fine if there are issues with that let me know" | No | Gameplay-Engineer |

How we read the two notes that need reading (ours, not his words):
- likeask: a special visitor's cat finished is the first good moment. A completed purchase may also lead to a like ask, at least two minutes later, never on the purchase screen, and it sits behind its own constant or switch because he wrote "maybe". Our earlier "never after a purchase" was a judgment, not a sourced Roblox rule.
- icons2: only E is an alternate for now; B, C, D and F are spares. Model-Agent fixes the orange at the sides of E before it is used and checks thumbnail 2 for the same fault.

Numbers: pack parts 99 + 249 + 199 = 547. At 199 the saving is 348 Robux, 63.6%, shown as 63 (rounded down).

Setup steps: none ticked yet, no ids pasted.

## Second round, page v50, 2026-11-26 10:36 AM ET

Derek asked at 10:30 AM ET: "update plan artifact with anything else needed". Gathered from the threads, memory and the needs-owner issues. Four questions, each with our pick first. None answered yet.

| id | Question | Our pick (option 0) | Other options | Owner of the answer |
|---|---|---|---|---|
| iconebow | The bow on icon E and thumbnail 2 moved to the top right as he asked; it now covers most of the clean ear | Keep it where it is | Slide it out to the corner so the ear shows; back between the ears and small enough to clear the line | Model-Agent |
| purchaseask | Reading of his "Maybe also after a purchase just a little bit after" | At least two minutes after a finished purchase, never on the buy screen, own off switch, counts as the visit's one ask | About 30 seconds after; no like ask after a purchase | Gameplay-Engineer (LikeAskRules.AFTER_PURCHASE), Design-Agent (the ask card) |
| rbxsync | The RbxSync comparison run he said yes to | Skip it, keep our own walker | Run it in a scratch place only, he buys the licence and accepts the plugin | Sync-Agent |
| modelthread | Model-Agent's thread hit its attached file limit | Keep the thread, the coordinator attaches its pictures | Fresh thread once the bigger spa and bow change are merged; fresh thread now | Coordinator (a new thread only on Derek's word) |

Sync-Agent's RbxSync findings (2026-11-26, nothing installed): paid product, proprietary licence that prohibits unlicensed use; the plugin runs code sent from its local server (loadstring) and turns on LoadStringEnabled; an older version hid those function names from the Creator Store scan; the plugin would load in every Studio window; the unsigned exe would likely be blocked by Smart App Control; it adds walk, observe and wait tools; our walker reached 114 of 114 spots.

Setup list changes in v50 (ten steps now):
- s2-passes: say which game the ids are from (ids are per game).
- s2-storeart: files are in the main chat; icon E and thumbnail 2 are the new ones (orange gone, bow top right); wait for new files only if he picks another bow.
- s2-notify: now Gameplay-Engineer's exact steps of 10:30 AM ET. Check the group key has User Notification Write (user.user-notification:write) for both games with Restrict IP addresses off; save secret CleanACat_NotifyKey with domain apis.roblox.com; create notification string build_done with the text "Your {buildName} is ready! Come back and show it off."; copy the asset id and paste it. Both games. Roblox sends only to 13 and over who opted in, at most once a day, once a game has 100 visits.
- s2-devtest (new, last): play today's pieces on the dev game on his iPhone once we say all are on. On in dev at 10:36 AM ET: hudTidy, fewerPills, helperPopups, buildWindow. In review: bigSpa (PR 763), counterLine, counterCrate (PR 762 and Gameplay's server PR).
- Ticked so far: s2-computeruse (10:14 AM ET). No ids pasted.

Design PR 759 merged 10:31 AM ET (issue 758 closed).

Page v51, 10:44 AM ET: check of the three needs-owner issues. 530 (server size, private servers, passes and products, questionnaire) and 106 (store art v2: his picks, the files and the bow) were already covered by setup steps and q2-iconebow. 29 (owner playtest of the scrub) was only on a ticked to-do, so its three questions and keep or rethink were added to s2-devtest.

## Derek's answers to the second round, 2026-11-26 3:13 to 3:14 PM ET (read 3:16 PM ET)

| id | His pick | His words | Same as our pick? | Passed to |
|---|---|---|---|---|
| iconebow | 0: keep the bow where it is | "its fine infront of ear but tilted on corner." | Yes | Model-Agent |
| purchaseask | 0: two minutes after a finished purchase, own off switch | (none) | Yes | Gameplay-Engineer |
| rbxsync | 0: skip RbxSync, keep our walker | "If its working well than its fine, no buying license so we can skip" | Yes | Sync-Agent |
| modelthread | 0: keep the thread | "I will manually restart model agent." | Yes, and then at 3:15 PM ET he said in the chat he will delete and remake every thread | Coordinator |

Setup: c-s2-computeruse ticked 10:14 AM ET. c-s2-passes was touched at 3:14 PM ET and reads not done, with no ids. Nothing else ticked.

## Third round, page v52, 2026-11-26 3:20 PM ET

Derek 3:15 PM ET in the chat: "Save all info from plan artifact and update it with any questions needed, get all threads to update their library folders/md skills files with whats needed for them I am going to delete all threads and remake them to have fresh context and image limits per thread reset. Let me know when all threads are ready to be deleted and remade"

One new question, not answered yet:

| id | Question | Our pick (option 0) | Other options | Owner of the answer |
|---|---|---|---|---|
| notifylive | When to set up notifications on the LIVE game (message string and the secret) | On the day he promotes, with the rest of the live set, by our workflow | Now; he does it by hand | Gameplay-Engineer |

Why it is asked: notifications were set up on dev at 12:40 PM ET by the GitHub workflow (string build_done made, group key saved as secret CleanACat_NotifyKey), and anything on live waits for his word.

Setup list in v52 (nine steps): s2-passes, s2-products, s2-questionnaire, s2-serversize, s2-private, s2-groupwall, s2-storeart (use the newest set in the chat; the bow stays), s2-computeruse (ticked), s2-devtest (ready now: everything on in dev since 12:21 PM ET; asks issue 29's three scrub questions and keep or rethink). s2-notify was removed because dev is done.

Every answer in one readable file: plan-page-answers-2026-11-26.md. Exact restore copy: plan-page-backups/answers-2026-11-26-1516ET-full.json.

## Page v53, 2026-11-26 3:23 PM ET: one more question, from the coordinator

| id | Question | Our pick (option 0) | Other options | Owner of the answer |
|---|---|---|---|---|
| headbows | Bows on the ten special cats that wear a head piece. In the game the bow stands at the side of the head at full size (he had a big blue bow taken off the pink cat in thumbnail 3: "remove the giant blue bow that appeared on pink cats head") | A smaller bow on those ten | No bow on cats with a head piece; leave as they are | Model-Agent |

The coordinator gave him the same three options in the chat, so his answer may come there and not on the page. Not answered at 3:23 PM ET. Two questions are open: headbows and notifylive.

Also in v53: the store art step says the six files in Model-Agent/store-art/picked-2026-11-26/ are final and safe to upload (icon-main-512.png, icon-alternate-e-512.png, thumbnail-order-1 to 4), and the setup intro says the notification step is done on dev and no longer his.


## Derek's answers of the evening, 2026-11-26 5:17 to 5:23 PM ET (read 5:25 PM ET; page v54 at the new link)

Derek in the chat, 5:23 PM ET: "All plan questions answered/done so go through that and update with anything new needed". All 78 questions now have a pick. Backup: plan-page-backups/answers-2026-11-26-1725ET-full.json (165 docs).

| id | His pick | His words | Same as our pick? | Passed to |
|---|---|---|---|---|
| headbows | 0: a smaller bow on the ten cats with a head piece | "Those bows are wayyyy too big and should be on top right corner not on side" | Yes, with a change: the bow also moves from the side of the head to the top right corner | Model-Agent |
| notifylive | 0: set up live notifications on the day he promotes | (none) | Yes | Gameplay-Engineer |

Setup steps. He ticked all nine, but a tick here does not always mean the step is done on Roblox. What each note means (the reading is ours):

| id | His words | What it means | Passed to |
|---|---|---|---|
| s2-passes | "You can do gamepasses I have seen it done with keys or use claude in chrome" | Not made yet. We make the five passes ourselves: Open Cloud with the group key first, his signed in Chrome if the key cannot. This replaces his morning pick that he makes the dev set | Gameplay-Engineer |
| s2-products | "You can do dev productsI have seen it done with keys or use claude in chrome" | Not made yet. Same as the passes, for the eight products | Gameplay-Engineer |
| s2-questionnaire | "Will leave this to last" | Not done. Stays his, last. It must be in before the Robux crate goes on in the live game | Growth-Agent (answers are written), Review-QA (before live check) |
| s2-serversize | "6 is fine" | Six confirmed. Read as a confirmation, not as proof the setting is changed, so we set it | Gameplay-Engineer |
| s2-private | "Honestly 50, or 25 since there is no real benefit to being alone in your own server, give it free with robux plus" | Price changes from 100 to 50 or 25, his either. Our pick 25, a judgment (his own reason points to the lower one). Free with Roblox Plus comes from Roblox by itself once a price is set (Growth-Agent's check of 2026-11-25) | Growth-Agent (price), Gameplay-Engineer (setting), the design (issue and pull request) |
| s2-groupwall | "I don't know what you mean by wall but joining group for a good reward should be a thing." | The step was unclear and out of date. A web search on 2026-11-26 found Roblox retired community walls at the end of March 2026 in favour of forums the owner turns on, so there is nothing to turn off. Step removed. The group reward he wants exists: the gift stand gives one pet for favourite plus group | Nobody. Growth-Agent told for the record |
| s2-storeart | "You should be able to do this with keys or use claude in chrome" | Not uploaded yet. We try again ourselves. On the morning of 2026-11-26 Chrome could not pick a file from our side, so the owning thread tries the key and other routes and says plainly if none works | Coordinator to route (Growth-Agent owns the store page, Model-Agent the files) |
| s2-computeruse | "Allowed" | Done | Sync-Agent |
| s2-devtest | "Will playtest now and let you know" | In progress. His notes come in the chat | Coordinator, Review-QA |

Sources for the wall: search result titles "roblox community walls retired end of march" (piunikaweb.com, 2026-04-01) and "Forums Are Now Live for All Community Owners" (devforum.roblox.com). Open Cloud has reference pages for game passes and developer products (create.roblox.com/docs/cloud/reference/features/game-passes and developer-products), so making them with a key is a real route; whether the group key has those permissions is for Gameplay-Engineer to check.

## Page v55, 2026-11-26 5:40 PM ET

No question is open and none was added: nothing from today's work needs a choice from him. Checked: the three needs-owner issues (530, 106, 29), the memory topics other threads changed today and the open issues list.

- New visible section "What you decided this evening" (five entries): his answers, passes, products and store art are ours now, private servers at 25 Robux (our pick of his 50 or 25, he can say 50), the group wall step is gone, the new link.
- Setup list is three steps, with new ids so they start unticked: s2-playnotes (his dev playtest notes and the three scrub questions of issue 29), s2-maturity (questionnaire, last, before the Robux crate goes on live), s2-promote (write "send it to live"; that day we make the live passes and products, set six players and 25 Robux, set up live notifications and publish the tested build).
- Removed from his list: s2-passes, s2-products, s2-storeart (ours now), s2-serversize, s2-private (we set them), s2-computeruse (done), s2-groupwall (out of date).
- Design: issue 846, pull request 848 (private server 25, who makes passes and products, head piece bows, live notifications, six players). Claude Doc edited to match, rev 23.
- Passed on at 5:35 PM ET: Model-Agent (head piece bows), Gameplay-Engineer (live notifications, passes and products, server size, private server price), Growth-Agent (private server price, questionnaire, store art, wall), coordinator (store art route, review of 848).

## Page v56, 2026-11-26 5:35 PM ET (v55 went out at 5:32 PM ET; the 5:40 and 5:45 PM stamps above were ahead of the clock)

From Gameplay-Engineer and Growth-Agent through the coordinator, 5:33 PM ET: the existing keys can make the dev passes and products, set the server size and upload the main icon and four thumbnails (issues 850 and 851, workflow pull request 852 in review). No Open Cloud route exists for the alternate icon. Private server price is 25, set on promotion day.

- The "ours now" entry says exactly that.
- New setup step s2-icone: add icon E as the alternate icon by hand in Creator Hub (file icon-alternate-e-512.png in Model-Agent/store-art/picked-2026-11-26/). Four steps now: s2-playnotes, s2-icone, s2-maturity, s2-promote.


## His notes on the four setup steps, 5:47 and 6:04 PM ET (read 6:06 PM ET)

Derek in the chat, 6:04 PM ET: "Plan answered". He ticked all four. A tick is not proof a step is done; the reading is ours.

| id | His words | What it means | Passed to |
|---|---|---|---|
| s2-icone | "you can do that" | Not added yet. Ours now. No key can set an alternate icon, so the route is his signed in Chrome, which he named for store art at 5:20 PM ET. If that fails too we say exactly what failed | Growth-Agent, coordinator to route |
| s2-playnotes | "Gone through some starting changes/issues more will come later" | His first notes came in the chat from 5:45 to 6:04 PM ET and are issues 856 to 877. More will come. Not a to-do for him | Review-QA (the decisions check) |
| s2-maturity | "Lets leave for now dont worry about it yet" | Still his, later. Do not remind him until the Robux crate is about to go on in the live game, where it is a must | Growth-Agent, Review-QA |
| s2-promote | "Will do no need to put this on a todolist" | Off the page. He says the word in his own time | Nobody |

Same turn, his other chat message at 6:04 PM ET asked that his earlier decisions (the bigger spa, everything answered in the plan) are being worked through. The check list for Review-QA is `decisions-check-2026-11-26.md` (70 decisions, 11 flags), also in Review-QA-Agent/.

## Page v57, 2026-11-26 6:11 PM ET

- SETUP is empty. The setup section is now "Nothing is waiting on you" with four rows (list LEFT): his words on each step and our reading.
- New first section "Your playtest notes and where each one is" (id notes, list NOTES): eleven notes from the chat, 5:45 to 6:04 PM ET, each with its state. Built and merged: starter card (issue 857, PR 858), wash pace (865, PR 866), 3 star wash (868, PR 870), guide line (861, PR 867). In review: wash on its own screen (856, PR 864), cat walks out on its legs (875, PR 876). Being built: gift crate (859), photo moment (862), like wait pop up (869), old door line and floating cats (871, 874), pop ups only as guides (877).
- Tonight's list has a new first entry for the four setup notes (N_TONIGHT 6).
- Test: shot11.js (no setup inputs any more). Database read before publish: no change since 6:04 PM ET.
