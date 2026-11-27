# Overnight checks, main 792d2dd, 2026-11-27 (local Studio, iphone_13 749 x 388)

Unsaved local place, every off-by-default switch on except toolCursor, streetLoadTest, exampleFeature and openingReplay (so bigSpa, wideStreet, counterLine, counterCrate, counterCards, customerCarry, townsfolk, customerWalk and washScreen are on). Seeded save: bench 6, Jo and Sam hired, all bows owned. The tester name is the only name.

## Bows (issues 948 and 845)
Each head-piece cat's Dirty_Sit model got BowFit.wear for PinkRoyal and PinkGolden. I counted the bow parts that intersect the head piece (_Prop) parts.
- Rosette and Djinn: 0 overlaps with both bows. PASS (was 3 each on eb27dde). Pictures: bow-rosette-royal-clear.jpg, bow-djinn-golden-clear.jpg.
- Bathtile, Jade, Moonstag, Phoenix, Prism, Sherbet and WhiteTiger: 0 overlaps. PASS.
- Stardust: Royal has 2 overlapping parts and Golden has 1; the bow loop crosses the wand stick. FAIL. Picture: bow-stardust-royal-overlaps-wand.jpg.
- Workspace.Terrain is empty: 0 cells of any material.

## Drop-off and counter (issue 871)
1. Six cats on their mats: PASS. Each cat's bottom is at y 3.37 against a mat top of 3.38 (gap -0.01). Box centres are 0.03 to 0.08 studs from each mat spot (place 1 -1.60/-24.93 ... place 6 14.36/-24.94). Picture: dropoff-1-six-cats-on-mats.jpg.
2. Walk in: FAIL for the cat. The customer's hand Grip and the carrier Grip were 0.00 apart at every sample, so the carrier is in the hand. But while the customer walks in, the CounterCat moves on its own at counter height: its bottom stays at y 3.37 over the street (2.87 above the pavement, about 5.2 to 6.5 studs from the carrier's CatSeat). It shows as a cat floating beside the line. Pictures: dropoff-2a and dropoff-2b; video dropoff-2-walk-in-side.mp4.
3. Set-down at place 6 (newcomers join at the back, so there was no place 1 drop-off): PASS for the frames shown. The crate lands on the mat, the door opens and the cat walks out (dropoff-3). The sit and crate fade fall after the end of the clip.
4. Step-up after taking place 1's cat: PASS. Kit moved 4 to 3 (x 11.2 to 7.9), Pearl 5 to 4 (14.3 to 11.1) and Bea stayed on 3 (4.8); the newcomer was set at place 6 (14.3); every cat ended on its mat. Pictures dropoff-4a and dropoff-4b, video dropoff-4-take-place1-step-up.mp4.
5. Heart runs out: NOT TESTED. HeartFill stayed at 0.56 over 6 s; bars last minutes.
6. Take at place 3: NOT CONCLUSIVE. From 7.0 studs from place 3 (7.4 from place 2), E made the player walk 3.9 studs and lift a cat, but it was LilacCloud, not place 3's Toffee. E takes whichever prompt Roblox picks. Video: dropoff-6-take-near-place3.mp4.

## Wash room (issue 856, real CleanACat_Area_WashRoom and PR 983)
- During the wash: PASS. 0 enabled world guis on screen at the scrub. No counter cat or customer part is visible to a ray from the camera at scrub, brush, foam or bow (the step-skip hook ran through them). At most 1 gui counted for a single sample during step changes. Pictures: wash-room-1-scrub-room-only.jpg, wash-room-1b-bow-step-room-only.jpg.
- After the wash: PASS. The billboards are back (6 CounterCard, WorkerBar, VisitorStar, GiftBeacon, 2 prompts), and all 2,481 counter and customer parts are unhidden. Picture: wash-room-2-after-wash-bars-back.jpg.

## Also seen
- On iphone_13 the recap card's Next cat button is centred at y 333 in a 330 tall GUI area, half below the screen edge (recap-next-cat-cut-off-iphone13.jpg). It was still tappable at y 318.
