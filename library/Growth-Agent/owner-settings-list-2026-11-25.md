# What Derek creates or changes himself (2026-11-25 ET, Growth-Agent)

From the agreed design (docs/design/clean-a-cat/gdd.md). Create each only when the code that grants it is merged: passes cannot be deleted and products are awkward to remove. Prices are starting values to tune later (Derek: "do whatever prices for mono for now can tweak later"). Names say exactly what an item gives; never write "free" next to a paid item. Claude does not touch store settings; Derek creates these in Creator Hub on the group's game (Creampuff Games).

## Game passes (code merged in PR 614; Derek creates each, then sends its id to Gameplay-Engineer for shared/Passes.luau)
Code keys: DoubleCoins, SecondBuilder, GoldenSponge, Lou, SecondPetSlot.
| Name | Price | Description text |
|---|---|---|
| 2x Coins | 199 | Earn double coins from every cat you wash. |
| Second Builder | 299 | Run two spa builds at the same time. |
| Golden Sponge | 99 | A wider scrub with gold bubbles. |
| Lou, the extra helper | 249 | Lou joins your spa with his own station. He works like Jo and Sam. |
| Second pet slot | 249 | One more pet slot for you and for every worker. |

## Developer products (send each id to Gameplay-Engineer for shared/Products.luau)
Code keys: FinishTier1 to FinishTier5 (merged), StarterPack (PR 615 in review), CrateOne and CrateFive (next PR; shown only where PolicyService allows). Prices are read from Roblox, so what Derek sets is what players see.
| Name | Price | Notes |
|---|---|---|
| Crate | 49 | Random. Chance of every pet shown before buying. |
| 5 Crates | 199 | Same crate, same chances. |
| Finish now (5 min) = FinishTier1, 5 minutes or less left | 5 | One product per tier; Gameplay-Engineer needs each product's id for shared/Products.luau. The button never shows until they exist. |
| Finish now (30 min) = FinishTier2, 30 minutes or less | 15 | |
| Finish now (2 hours) = FinishTier3, 2 hours or less | 35 | |
| Finish now (8 hours) = FinishTier4, 8 hours or less | 75 | |
| Finish now (more than 8 hours) = FinishTier5 | 99 | |
| Starter Bundle | 199 | Golden Sponge, second pet slot and 2x Coins in one buy. Real 72 hour clock from first join, then gone. Hidden if the player owns any of the three. Bundle price is worth 547 (saving 348 Robux, 63%, shown as 63%); recompute if any price changes. |

## Game page settings
- Private servers: Creator Dashboard > Audience > Access Settings > Requires Robux, 100 (monthly). Roblox Plus subscribers get it free. See private-servers-check-2026-11-25.md.
- Max players per server: 6.
- Maturity questionnaire: copy answers from maturity-questionnaire-answers-2026-11-25.md.
- Icon and thumbnails: first test set as agreed; second half dirty and half clean thumbnail is #500; every upload waits for Derek's OK on a contact sheet.
- Description: first line what you do, "cat spa" in it, no "free", update line only after an update is live (store-copy-2026-11-23/).
- (Removed 2026-11-26: Roblox retired group walls; nothing to switch off. See private-servers-check update.)
- Create the group and game links before launch; no secrets in any text.

## Which game (Derek, 2026-11-26)
He makes the passes and products on the dev game now and on the live game at promotion, so every id goes to Gameplay-Engineer per game (dev ids first, live ids later). The notification key reuses the group key as the game's secret, no new key. Icons: A main, E the only alternate for now, after Model-Agent fixes the orange at the sides of E.
