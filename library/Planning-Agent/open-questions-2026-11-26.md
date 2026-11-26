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
