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
