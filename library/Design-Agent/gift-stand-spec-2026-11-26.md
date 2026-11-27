# Gift stand and group crate (Design-Agent, 2026-11-26)

Issues 859 (group reward becomes a crate) and the owner's stand note of 2026-11-26: "have the first free gift just be all of the top 3 and then replace it with a different playtime reward thats good after and once thats claimed then remove it from spa so it doesnt take up room".

One switch for the whole flow: `giftFlow`, off by default (first session change). `giftCrate` (issue 859) stays as the crate's own switch.

## Before (today)
- The stand lights at 7:00. Its card has three rows, each claimed on its own:
  1. Like the game: 150 coins, Claim 10 s after the ask (nothing is checked).
  2. 30 minutes of play: one normal crate.
  3. Favourite and join the group: Starcoat, a plain pet.
- The stand stays in the spa for good, prompt and all, until all three are paid.

## After
### Stage 1: the welcome gift (from 7:00, as now)
- The card shows the three gifts as one bundle with one button, "Claim all": 150 coins and the free gift crate.
- The bundle asks for the favourite and the group join, as today; the like stays a request ("Like the game if you enjoy it"), never a condition, and pays either way.
- The playtime row moves to stage 2, so stage 1 is all ready at once.
- One tap pays: 150 coins (a mint card) and the gift crate, which drops by the stand with the trail and the "You got a crate!" guide card (contextAsks).
- The free gift crate (issue 859): kind `gift`, chances shown before opening (Uncommon 69, Rare 24, Epic 6, Legendary 1), pets Starcoat, Pebble and Pickle 23% each, Koi and Bamboo 12%, Coral 6%, Nimbus 1%. Expected boost about +9.6%, under the day 2 good crate.

### Stage 2: the playtime gift
- Once stage 1 is claimed, the stand changes to a timer: "A good crate at 30 minutes of play", with the minutes left.
- At 30 minutes total play it is ready: one Claim gives one **good** crate (was a normal one). It is the second crate of the first session and the reason to keep playing past 10 minutes.

### Stage 3: gone
- Once stage 2 is claimed, the stand leaves the spa for good (a puff, then the floor spot is free). Nothing else moves into its place.
- The like and group asks live on in More, then Gifts, for anyone who skipped them; the bundle there pays the same once.

## Rules and checks
- Each stage pays once per save, decided and saved on the server (save.asks keys giftStage1, giftStage2).
- Old saves: a save that already has Starcoat counts stage 1 as claimed and keeps Starcoat; one that already took the play crate counts stage 2 as claimed, so its stand is gone.
- Robux: none. Random: the crate, with its chances shown before it opens (monetization-policy).
- Pace: 150 coins at about 7:00 is unchanged. With the Grand opening gift (issue 913), the player has Jo by then, so 150 goes to the Second Tub or the soap. The good crate at 30:00 replaces the normal one: about +2% more boost, within the pet cap.

## Who does what
- Gameplay-Engineer: GiftService, FreeRewardService and GiftController stages, the stand's removal, the More, then Gifts entry.
- Design-Agent: GiftCard look (bundle row, Claim all, timer stage), gdd and tuning rows.
- Model-Agent: CleanACat_Prop_GiftCrate (issue 859).
- Motion-FX: the ribbon untie (under 0.6 s) and the stand's puff on removal.
