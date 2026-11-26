# Maturity and compliance questionnaire: proposed answers (2026-11-25 ET, Growth-Agent)

For issue #530, from the agreed design (docs/design/clean-a-cat/gdd.md, pull request 505). Source: Roblox's "Content maturity and compliance" page (create.roblox.com/docs/production/promotion/content-maturity, last updated 2026-11-10). The page says to answer for "the most mature or extreme content players can encounter". Derek fills it in on the game's page; this is the text to copy. Review-QA should check each answer against the build before launch.

Expected result: **Minimal** (the target is Minimal or Mild; Kids and Select needs one of them). The page does not give a scoring formula, so the label is Roblox's to compute; every "No" below is what the design shows today.

| Category | Answer | Why, from the design |
|---|---|---|
| Violence | No | Nothing is hit or hurt; cats leave when the heart bar is empty, nothing else is taken |
| Blood | No | Mud and foam only; no blood |
| Fear | No | Cats are cute and grumpy, nothing scary |
| Crude humor | No | Dirt level is mud. Recheck if any smell, poop or toilet joke is ever added (that would be at least Mild) |
| Unplayable gambling content | No | No casino style content |
| Strong language | No | Only typed text is a worker's name, filtered by Roblox |
| Romantic themes | No | None |
| Alcohol | No | None |
| Social hangout | No | The main activity is washing cats; spas side by side and visiting are extras |
| (if asked) private spaces | No | Open shop front, no closed rooms, only cats are bathed (our 2026-11-23 reading) |
| Free-form user creation | No | Players do not build or draw. A worker name is a filtered short text only; if the question counts that, ask Derek |
| Sensitive issues | No | None |
| Paid random items | **Yes** | The Robux crate. Second question: Yes, the game reads PolicyService per player and hides the Robux crate where restricted |
| Paid item trading | No | No trading at launch |
| Media (sharing gameplay media, auto-playing feeds, content from other games) | No to all three | None in the design |
| AI interaction | No | None |

Notes
- The page says paid random items change access (policy rules), not the label. The crate chance list and PolicyService check must be built before the crate is sold.
- Assets are moderated on their own: no realistic violence, blood or crude humor in images, meshes or audio whatever the label says.
- Reused names and designs from Catch a Cat Cafe for special visitors must also fit these answers; Model-Agent should avoid anything scary.
- Answer again after any new feature (a new feature that changes an answer changes the label).
