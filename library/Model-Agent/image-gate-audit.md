# Image gate audit, 2026-11-27 (Model-Agent, for Review-QA)

**Why this exists.** Roblox flagged ThumbsUpFilled (135826908608436) as "Sexual Content". The account is suspended for 7 days and appealed. Review-QA's new gate fails any image that has:
- hands, fingers or thumbs
- a long rounded shape that could be misread (a stub, a tube or an upright capsule)
- skin tone blobs

Each image is checked at 48 px, at 24 px and as a black silhouette. **No uploads until Derek says the account is clear.**

## What was checked

**157 images** in total:
- Every Image from all 20 upload-asset runs (runs 1 to 20, 2026-11-24 to 11-27), including older versions that were later replaced.
- The store icon and four thumbnails on the dev game page.
- The queued alternate store icon E.

Audio uploads were skipped. Game passes and products have no images.

Every image appears on the sheets in the shared files under Model-Agent/image-gate-audit/:
- sheet-1.png to sheet-7.png: each image at 96, 48 and 24 px, then as a silhouette at 48 and 24 px.
- store-thumbnails.png

"Wired" means the id is in Icons.luau or Portraits.luau on main.

**Removing.** Open Cloud cannot archive an Image (HTTP 400, found 2026-11-24). Only Derek can archive one by hand: Creator Dashboard, Creations, Development Items, Decals/Images, filtered by the Creampuff Games group.

## FAIL: remove (hands)

All three are queued for removal. The like how-to icons are redrawn as HeartOutline (98146759736466) and TapDot (112847264343092), no hands, merged in PR 996 and uploaded 2026-11-27.

| Image | Id | Wired | Notes |
|---|---|---|---|
| Hud ThumbsUp | 76096338201947 | no (PR 973 held) | Hand with a thumb |
| Hud ThumbsUpFilled | 135826908608436 | no (PR 973 held) | The flagged one |
| Hud TapHand | 121275029069381 | no (PR 973 held) | Raised index finger |
| Hud RingPuff | 113448726935917 | no | Same upload run. A ring with rays, no hands: passes. Keep it. |

## HIGH risk: replace before uploads resume, then remove the old id

| Image | Id | Wired | What could be misread | Fix |
|---|---|---|---|---|
| Portrait Pet_Glitch | 115707461545852 | no (pets not wired yet) | The silhouette's diagonal antenna reads as a raised pointing finger at 24 px | DONE 2026-11-27: cubes on a low scanline bar; new id 80341127367421 (PR 997), old id to archive. Sheet: image-gate-audit/pets-clover-glitch-gate.png |
| Portrait Pet_Clover | 87691200049996 | no | The silhouette is a tall rounded body with a knob on top: an upright capsule | DONE 2026-11-27: clover low and tipped forward; new id 77963078642728 (PR 997), old id to archive. Same sheet as Glitch |
| Hud Mud | 137792046843119 | yes (need chip) | A brown blob | Recolour: a grey-brown splat with drops around it, not one rounded blob. Or a different sign, such as a dirty paw print. |
| Hud Tangles | 115237769890322 | yes (need chip) | The silhouette is a round ball with a curled tail | Yarn ball with no loose strand, or a comb with a knot |
| Store thumbnail 3, busy spa | 95954331759010 (dev page); live page 79981284321647 | store page | Human staff with hands and arms; one holds a long pole (the shower head) | DONE offline 2026-11-27: arms straight down in long sleeves that cover the hands, no shower. Sheet: store-art/picked-2026-11-26/thumbnail-3-image-gate-before-after.png |

## MEDIUM risk: Review-QA's call

| Image | Id(s) | Wired | What could be misread |
|---|---|---|---|
| Portrait Pet_Angler | 107617453014958 | no | The silhouette looks like a fist with a raised knuckle (the lure) |
| Portraits Sherbet, Dirty1 to Dirty4 | 124924090636385, 102861276283434, 80910111657134, 99309578237973, 89391291978262 | yes | The sundae lobe on the right makes a mitten or thumb silhouette |
| Portraits Prism, Dirty1 to Dirty4 | 74332001223114, 77142244148141, 100818351454303, 122558099778552, 84651845088842 | yes | The rainbow arc on the right makes a mitten silhouette |
| Portraits Rosette, Dirty1 to Dirty4 | 123002968671356, 103391589010434, 82402858139633, 138974850982583, 92332868749907 | yes | Crown points plus the side ear read as a raised fist; cream fur |
| Portraits Jade, Dirty1 to Dirty4 | 92101460375197, 109529679809623, 110110321934140, 91205509807847, 77203951376625 | yes | Two horns and the side fin read as raised fingers and a thumb |
| Portraits Phoenix, Dirty1 to Dirty4 | 118082407857643, 132833230431582, 126788086927816, 109785083182074, 109761525322539 | yes | The flame crest and feathers read as spread fingers |
| Portraits Djinn, Dirty1 to Dirty4 | 109186971661634, 104938201513784, 71136825395038, 105010225463490, 124587678339342 | yes | A tall rounded silhouette with a pointed tip |
| Portraits Muffin, Dirty1 to Dirty4 | 97606052567188, 103732360664273, 135173358834258, 95151893323177, 126041857156058 | yes | Peach-orange fur close to a skin tone, with brown patches on the dirty ones |
| Portraits Toffee, Dirty1 to Dirty4 | 130371035242121, 119739945379078, 85593504689652, 127159878345036, 78826708044535 | yes | Cream-peach fur close to a skin tone, with brown patches |
| Hud Build (hammer) | 84861881998122 | yes | A long rounded handle |
| Older Build with paw | 90790412001068 | no, never wired | Same handle. Remove it anyway: it was already on the remove list. |
| Hud Helper (staff head) | 73988627805858 | yes | A human face is a large skin tone area |
| Older Helper | 112634017426563 | no | Same |
| Older Helpers (Jo's head) | 86032284297873 and 115493249688079 | no (Helpers now uses Staff) | Same. Not wired, so remove them. |
| Hud Shake | 85720072168320 | yes | Upright rounded phone with short rounded motion bars |
| Store thumbnail 1, half muddy | 71735522887956 (dev page); live page 105795079697238 | store page | Brown blobs on the muddy half. DONE offline 2026-11-27: splats removed, grey glow. Sheet: store-art/picked-2026-11-26/thumbnail-1-image-gate-before-after.png |
| Store icon E alternate | not uploaded | queued | Checked 2026-11-27: icon E never used the splat backdrop. Still waits for the gate. |

**Dirt portraits in general.** All 80 Dirty1 to Dirty4 portraits carry brown mud patches. Dirty3 and Dirty4 have the largest patches, and they are most visible on the light-furred cats:

| Cat | Dirty3 | Dirty4 |
|---|---|---|
| Cotton | 94565195519463 | 111878139570591 |
| Marble | 121563404782426 | 116591089955294 |
| Patches | 75709165640705 | 76106038693945 |
| LilacCloud | 86047873180553 | 101825651814740 |
| WhiteTiger | 105265029405232 | 123255647273640 |
| Starcoat | 117207608160037 | 84400608270214 |

If the gate counts brown patches as skin tone blobs, the fix is one change to the dirt colour (a cooler grey-brown mud) and one re-render of all 80. I'd rather do that than edit them one by one.

## Passes (no hand, stub, tube, capsule or skin blob found)

| Group | Images |
|---|---|
| HUD | Bow, Camera, Check, Coins, Crate, Crown, Dice, Gift, Heart, Index, Lock, Music, Paw, Pets, Pointer, Quests, RingPuff, Settings, Shop, Sparkle, Speaker, Staff (current 75869829179271 and older 70378908998679), Star, Station, Tools (current 100929090324662 and the older paw one 131551740191318), Wet |
| Clean portraits and dirt levels, apart from the light-fur note above | Bathtile, Cotton, Inky, LilacCloud, Marble, Moonstag, Patches, Smudge, Starcoat, Stardust, Tux, WhiteTiger |
| Other portraits | Suds (current 134546291029280 and the old ink one 92665897768427) |
| Pets | Blaze, Dragon, Ghost, Nebula, Ooze |
| Store | Main icon 88589278447404 (live page 92729298316581); thumbnails 2, name and bath (live 112653869263896), and 4, stray box (live 120549383496799) |

## Suggested order once the account is back
1. Derek archives the 3 hand icons, plus the never-wired older ids (90790412001068, 131551740191318, 112634017426563, 86032284297873, 115493249688079, 70378908998679, 92665897768427). Fewer flaggable images left in the group means less risk.
2. Model-Agent redraws the HIGH list offline now. Review-QA gates each image before any upload.
3. Review-QA decides on the MEDIUM list. Model-Agent then redraws the agreed ones, still offline.
