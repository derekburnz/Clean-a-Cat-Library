# Hands-on step games: how they keep short steps fun (notes, read 2026-11-24)

Tags: [official] [tracker] [developer statement] [research] [opinion]. All read dates 2026-11-24. Pages were read through a small summarising model, so quotes are as returned, not checked against the original. Mechanics only; no names, art or characters should be copied. Tracker numbers: Rotrends (rotrends.com) and the Roblox games API (games.roblox.com/v1/games, read the same day). Roblox search API worked through the page reader; curl from the shell was blocked.

Not repeated from earlier notes: PowerWash and Unpacking sound, Anthony 2019, NN/g 2018, Toca "no points", hypercasual retention (hooks-and-loops-notes), pet-game census (spa-research-notes).

## 1. My Pet Salon! and the other Roblox salon games

### Takeaway
My Pet Salon! is new and small but healthy: 452 peak, about 217 now, 86.6% liked, 18.9 minute sessions. I could not find any guide or wiki that lists its step types, step counts or star rules. The only step list is the owner's playtest. So the design facts below about it come from him, not from a source.

### Cited findings
- My Pet Salon! (EVOLUTION STUDlOS, universe 10772985378). Created 2026-10-25. Visits 304,574. Playing 217. Peak 452. Likes 836, dislikes 129 in the search API (86.6% in Rotrends, 965 votes). Favorites 10,221. Max 6 players. Rotrends: avg session 18.9 min (down 13.2% in 7 days, 93rd percentile), 7-day avg CCU 264.9 (up 67.9%), favorites per 1,000 visits 33 (down 19.7%), 0 game passes and 0 developer products listed. Last update: Rotrends says Oct 31, the games API says Nov 23; they disagree. [tracker] https://rotrends.com/game/10772985378 and games API.
- Page text: wash, brush, dry, cuddle; puppies, cats, bunnies, turtles, hamsters; buy stations and upgrades; unlock tools, moves, pets and combos; "Chain moves into combos for bigger rewards"; "Meet rarer customers with special looks." The page lists no game passes and no badges, and does not mention stars or VIP by name. [official] https://www.roblox.com/games/134135989047078/My-Pet-Salon
- A different game with a near name, "My Pet Salon" (universe 10774282853): created 2026-11-02, 100,415 visits, 0 playing, 68 up and 20 down. Styles dogs, cats, horses, lions, unicorns; stock products, run the till, hire staff; "earn stars for rarer pets". [tracker, official description]
- Owner playtest of My Pet Salon!: step types (swipe to scrub, aim water, pick burrs and drag them off, hold to trim nails, tap to knock things off); praise pop-ups; combo number; star rating with coins and XP breakdown; tool upgrades; index; rare customers with 16 steps and a permanent boost. Disliked: same swipe three times in a row, 16 steps long, pet rotates by itself so spots are missed. [owner statement, not independently checked]
- Barber Simulator (universe 10770932189): created 2026-10-14, 12.9M visits, peak 21.3K, now 3,738, 89.3% (24.6K votes), avg session 12.9 min (down 10.5% in 7 days), favorites per 1,000 visits 3.69 (down 31.1%). Description: cut, shave, dye; celebrity clients arrive in update 2. [tracker] https://rotrends.com/game/10770932189
- Barber Simulator wiki (fan wiki, date not shown): tools are clippers, scissors, razors; dye and wash apply only when the customer's reference photo calls for them; "Three stars is the normal success result", a secret rainbow star sits above a 3-star match; exact thresholds not published. Customer tiers: Rare pays double and is picky; Epic stricter; Legendary is a celebrity VIP and has a badge earned by 6.7% of players; 20 legendary celebrities, each with its own entrance. Furniture raises the chance of rare clients. Hired barbers earn while you are offline. Game passes R$129 to R$1,699. [guide] https://barbersimulator-wiki.wiki/ and https://newtoplay.com/games/barber-simulator
- Makeup Salon (universe 10769514597): created 2026-10-05, 22.2M visits, peak 22.4K, now 3,804, 96.9% (87.3K votes), avg session 9.1 min (down 9.1%), 5 game passes. Round: build a look that fits a theme before time runs out; looks are rated by players. [tracker, official description] https://www.rotrends.com/game/10769514597/Makeup-Salon
- Wash the Car (universe 10725799494): created 2026-08-16, 37.2M visits, peak 30.6K, now about 2,017, 88.6% (16.3K votes), avg session 13.4 min, 1.2M favorites. Description: build foam arches, brushes, jets, dryers; fast washes earn tips. Guide: manual wash is hold the mouse on the car while a percent climbs, then cash plus tip; bay gear maps to soap, scrub, rinse, dry, and automates the job; Sponge Size upgrade makes manual washing faster; eight rarity tiers; vehicle types expand by zone (cars, helicopters, boats, planes); a Dryer adds a tip multiplier. [tracker, guide] https://rotrends.com/game/10725799494 and https://allthings.how/wash-the-car-on-roblox-every-zone-from-the-first-bay-to-the-airport/
- Wash Foam Dry (10765594060): mud power-wash, foam, rinse, dry; 15 bays; hire staff; rebirth. 645K visits, 0 playing. [official description via API]
- Become A Dentist! (10773117440): created 2026-10-26, 905K visits, peak 1.4K, now 809, 63.6% liked (1.1K votes), avg session 10.0 min. Tools drill, forceps, X-ray; daily patient challenge with leaderboards. [tracker]
- Pet Store Tycoon (10282097014): created 2026-06-06, 27M visits, peak 40.6K, now 3,573, 96.2% (127.7K votes), avg session 29.4 min. Feed, clean, play with animals, stock shelves. Wiki: care is done by interacting with the enclosure (drop food flakes, wipe algae off glass); no minigame described. [tracker, guide] https://petstoretycoonroblox.wiki/
- My Salon Empire (10092472345): created 2026-04-27, 5.2M visits, peak 3K, now 221, 94.4%, avg session 8.4 min. [tracker]
- Barber Bus (older): client waits on a bus, timer, scissors, grow pieces, brush for colour; late clients leave unpaid; stars come in bronze, silver, gold tiers. [guide] https://sportskeeda.com/roblox-news/how-play-barber-bus
- A haircut guide (Barber Showdown): four tools (scissors, trimmers, razor, blend), undo, camera rotation by player; other players rate 1 to 5 stars on theme accuracy, symmetry, clean edges, smooth blending; the guide warns that rushing hurts rating. [guide, 2026-11-10] https://roonby.com/2026/11/10/barber-showdown-beginner-guide-how-to-get-cash-fast-best-haircuts-5-star-ratings/amp/

### Inferences (mine)
- The 2026 hands-on service games with big numbers (Makeup Salon, Barber Simulator, Wash the Car) all have session lengths of 9 to 13 minutes. My Pet Salon! at 18.9 and Pet Store Tycoon at 29.4 are the long ones. Both long ones have a store or management layer.
- Several rising games pair a hands-on step with a staff or automation layer (Wash the Car, Wash Foam Dry, Barber Simulator). Automation is the usual answer to "the fiftieth time". This is a pattern, not a measured cause.
- Only Wash the Car and Barber Simulator spiked and dropped quickly (30.6K peak to 2K; 21.3K to 3.7K). Favorites per 1,000 visits is falling in Barber Simulator (down 31%). Spikes fade; My Pet Salon! is still rising.

### Gaps
- No source on My Pet Salon! step types, step counts, star rules, upgrade effects or VIP rules. Needs the owner's notes or a screen recording.
- No source found for Skincare Spa, Cook Burgers, Work at a Pizza Place stations, or Roblox surgery games. The omni-search call for "Cook Burgers" failed. Not covered.
- Trackers give no per-job seconds. Job length for every Roblox game here is unknown.

## 2. Fisch and Dress To Impress (long-run proof of a simple repeated action)

### Takeaway
Fisch's reel minigame is one repeated motion kept fresh by changing the rod, not the motion. Dress To Impress shows a timed round with a clear start, middle and star vote.

### Cited findings
- Fisch (universe 5750914919): created 2024-03-13, 4.9B visits (5.17B in API), peak 1.3M, now 84K (API playing 54K), 90.7% liked, avg session 26.1 min, 3.6M favorites. [tracker] https://rotrends.com/game/5750914919
- Steps: cast a bobber, shake the rod to attract a bite, follow a line in the reel minigame. [official] games API description.
- Reel: move a bar left and right to keep a gray line inside it; higher-rarity fish make the line wobblier. Resilience steadies the line and lowers the bar's click sensitivity. [guide] https://esports.gg/guides/roblox/what-does-resilience-do-in-fisch
- Rod stats: Lure Speed (over 99% means no shaking needed), Luck, Control (size of the bar), Resilience. Special abilities change the minigame itself: freeze the fish for a time, fill part of the progress bar at once, automatic stabs that add progress. [guide, wiki] https://fisch.fandom.com/wiki/Fishing_Rods
- Developer: each fish has a Resilience that sets how fast its bar moves; rods "are not a simple ranking", each has its own use and special ability; fishing is based on Stardew Valley's system; "retention of players relies on the ability to play a game in multiple ways". [developer statement, Roblox DevForum spotlight, 2024] https://devforum.roblox.com/t/creator-spotlight-woozynate-makes-a-splash-with-fisch/3269481
- Fishing mini-game essay: tiny visual and sound cues matter; a balance meter "can become repetitive if it's the only mechanic"; Dredge changes its rhythm zones by species; reaction tests tire a player, so pair them with downtime. [opinion, developer devlog, Apr 2025] https://practiceflip.substack.com/p/exploring-fish-catching-mechanics
- Dress To Impress (universe 5203828273): created 2023-10-18, 11.4B visits, peak 1.7M, now 37.8K, 90.5%, avg session 16.9 min. [tracker] Round: just over five minutes to style an outfit (PC Gamer), or six minutes (RoWatcher); runway walk; all players rate 1 to 5 stars; top three on a podium; 14-tier star rank; Style Showdown mode uses three-minute rounds. [journalist, tracker news] https://www.pcgamer.com/games/sim/i-played-robloxs-hottest-game-thats-sweeping-social-media-and-got-my-ass-handed-to-me-by-a-bunch-of-12-year-olds and https://rowatcher.com/news/dress-to-impress-how-a-teen-developer-s-fashion-game-hit-9-7-billion-visits

### Inferences (mine)
- Fisch answers question 6: rods change the feel of the same step (bigger bar, steadier line, freeze, auto progress), and fish rarity changes the difficulty. Speed is only one of four stats.
- Dress To Impress answers a different problem: variety comes from a new theme every round, so the player does the same verb with a new goal.

### Gaps
- No developer talk found on the Fisch reel bar timing or how many seconds a catch takes.
- Dress To Impress has no developer quote on timer choice.

## 3. Outside Roblox

### Takeaway
The long-lived short-step games vary the verb every few seconds (WarioWare), grade each step (Papa's, Cooking Mama), and are criticised when steps repeat (Cooking Mama reviews).

### Cited findings
- WarioWare, Iwata Asks (D.I.Y. interview, 2009): "Short microgames last about four seconds, long ones, about eight." They kept to the few functions needed and "apply them in a variety of patterns"; the creators found they could combine existing functions to get more games. [developer statement] https://iwataasks.nintendo.com/interviews/ds/diy/0/2
- WarioWare Smooth Moves: players have "five seconds at most to grasp the way they have to play", so instructions had to be understood at once; nineteen "forms" (ways of holding the remote) "had a huge impact". [developer statement] https://iwataasks.nintendo.com/interviews/wii/warioware_smooth_moves/0/1 The pages did not discuss speed-up or boss stages.
- Cooking Mama: each task is a minigame usually under 10 seconds; a dish has one to as many as a dozen; touch screen does most input; each dish is rated on the average of its minigames and earns bronze, silver or gold; a serious mistake gives an angry Mama and "Don't worry, Mama will fix it!"; over 40 recipes in the 2022 game. [Wikipedia summary] https://en.wikipedia.org/wiki/Cooking_Mama
- GameSpot review: "at least a few dozen minigames" but "some of those are variants on the same basic game"; stylus is "a breeze to use"; "you'll undoubtedly end up doing many of the same games dozens of times"; Mama "makes some amusing faces when you succeed". Low replay value. [review] https://gamespot.com/reviews/cooking-mama-review/1900-6157831/ A Wii review: "Gets repetitive too quickly". [review] https://www.gamesradar.com/cooking-mama-cook-off-review Game Developer piece: "some generous grading at the end"; criticised "lack of challenge". [opinion] https://gamedeveloper.com/design/the-unrealized-potential-of-cooking-in-games
- Papa's (Flipline, blog): tips were the first score, but players wanted to spend money, so a separate points tally for levelling was added; each task is graded on execution; tips depend on how well you did; each regular has a name, look and favourite order; a shop sells upgrades and decor; other oven time options "added some more variety". The goal was challenge "without getting unbearably frustrating", and confusing rules showed onboarding must teach clearly. [developer statement] https://www.flipline.com/blog/?p=3887 Another post: push-button machines with moving meters for portions, good timing gives extra tips. [developer statement] https://www.flipline.com/blog/?p=6959
- Papa's Burgeria guide: three stations (order, grill, assemble); flip at the halfway point; burgers burn if left; upgrades such as a heat lamp and timers. Station score numbers not on the page. [guide] https://coolmathgames.com/blog/how-to-play-papas-burgeria
- Trauma Center: Under the Knife: ten tools chosen from icons on the touch screen; a time limit per operation; points for speed and efficiency graded "Bad" to "Cool"; rank C to S; replay in Challenge mode; reviewers praised touch control and criticised difficulty spikes and repetition. [Wikipedia summary] https://en.wikipedia.org/wiki/Trauma_Center:_Under_the_Knife
- Nintendogs: pet, play, walk, brush and wash through the touch screen; coat condition from "Beautiful" to "Filthy"; contests are the money source; 23.96M sold; Metacritic 83. [Wikipedia summary] https://en.wikipedia.org/wiki/Nintendogs Nintendogs + Cats, Iwata Asks: a dog "runs straight" at what it wants while a cat "stops and looks at it" before a pounce; the team found it "much harder because we put in cats"; height and the camera needed rethinking because cats climb. [developer statement] https://www.nintendo.com/en-gb/Iwata-Asks/Iwata-Asks-Nintendo-3DS/Vol-4-nintendogs-cats/2-Adding-Kittens-Doubled-the-Work/2-Adding-Kittens-Doubled-the-Work-204778.html
- PowerWash Simulator 2: new Swirlforce Surf Ace, a big circular surface cleaner; the reviewer says old nozzles are "slow going" on big flat areas and the new head avoids "two or three passes over the same spot"; sometimes "misses a bit of dirt". No developer quote on the page. [journalist] https://www.pcgamer.com/games/sim/powerwash-simulator-2-introduces-a-new-tool-that-makes-washing-mud-from-a-billboard-more-enjoyable-than-ever
- CrazyLabs Soap Cutting case study: one finger, cut down and sweep up; each bar hides a mystery item; zen pace and no fail; first build had no sound or haptics, later builds added recorded soap sound and haptics matched to crumbles; a third soft launch with meta (mystery box, knife catalog) improved retention; no numbers given. [publisher statement] https://www.crazylabs.com/?p=15785

### Inferences (mine)
- WarioWare shows the extreme: 4 to 8 second steps, new verb each time, understood in about five seconds. A cat step of 8 to 20 seconds with one clear verb fits that spirit.
- Cooking Mama and Papa's both tie the job grade to execution of each step, not only to completion. Cooking Mama gets repetition complaints even with a few dozen types, so variety in type alone is not enough; the variants must feel different.
- Nintendo's own cat note supports an idea for the studio: a cat that moves and reacts is part of the step, not only a target.

### Gaps
- Cooking Mama: no creator interview found. Wikipedia and reviews only. The "praise" detail is from the GameSpot review (faces), not from the maker.
- Papa's score formula per station not found.
- Trauma Center: no developer talk found; tool introduction order not on the page.
- House Flipper and Sago Mini not covered. Toca covered in earlier notes.

## 4. Praise words, combos and kids

### Takeaway
I found no study of combo counters or praise words in grooming-type games. The nearest research is on praise to young children and on feedback in children's games. It is thin and indirect.

### Cited findings
- 135 kindergarteners (2010): process praise ("good job drawing") raised motivation; even a little trait praise ("good drawer") lowered persistence after setbacks. [research] https://pubmed.ncbi.nlm.nih.gov/20570281/
- Harvard review of 76 preschool edutainment games: most had some feedback; few gave elaborative feedback that explains why; positive feedback was common, negative often absent; games leaned on repeated instructions to motivate. Describes design, not learning effects; US preschool only. [research] https://reacheveryreader.gse.harvard.edu/review-of-feedback-in-edutainment-games-for-preschoolers-in-the-usa
- Roller Splat and Unpacking sound points are already in earlier notes.

### Inferences (mine)
- Praise that names the action ("nice scrub", "all the burrs gone") fits the process-praise result; praise that names the player ("you are amazing") is the trait kind the study warns about. This is an extension from kindergarten to ages 7 to 12 and from drawing to games; it is untested here.
- A combo that resets on a slip may punish the youngest; a combo that only pauses is safer. No source.

### Gaps
- The PubMed abstract for "Assessing Feedback in a Mobile Videogame" did not load. No caution found specifically on combo counters for children.

## 5. Object view and rotation on touch

### Takeaway
No developer statement or study answered the question. I could not open the one paper that matches (primary school students rotating a 3D scene; blocked by a bot filter).

### Cited findings
- Haircut guide: the player rotates the camera and looks from above to see hard spots. [guide] Barber Showdown link above.
- Nintendogs + Cats: cat height and camera needed rethinking. [developer statement] link above.
- Owner's playtest: auto-rotation of the pet made him miss spots. [owner statement]

### Inferences (mine)
- Three options: (a) fixed side shown, then the game turns the cat when that side is done; (b) player turns it with one finger on empty space; (c) auto-turn. Option (a) hands the player the order and shows a visible side counter; it avoids two-finger rotation, which conflicts with a scrub drag. Untested.

### Gaps
- Evidence for touch object rotation by children: none read. Search result: Hal.science paper "Exploratory Experimentation of Three Techniques for Rotating a 3D Scene by Primary School Students" (hal-01219135), not read.

## 6. Tool upgrades

### Takeaway
Players meet both kinds. The long-lived Fisch changes the motion (bar size, freeze, auto stab). Wash the Car and PowerWash mostly change speed or area. I found no player preference data.

### Cited findings
- Fisch rod abilities and developer quote in section 2. [wiki, developer statement]
- Wash the Car sponge size and walk speed make manual washing faster; gear automates steps. [guide]
- PowerWash 2 surface cleaner covers more area per pass. [journalist]
- Papa's: later shop upgrades and a timer option. [developer statement]
- SayGames pickaxe after vacuum (earlier notes).

### Inferences (mine)
- A speed-only upgrade makes the same step shorter; a motion upgrade (wider brush, a steadier hand, a special effect on one step type) makes it feel different. Fisch is the only evidence I found that the second kind keeps long play.

### Gaps
- No A/B or survey on preference.

## 7. Touch control for children (beyond Anthony 2019 and NN/g 2018)

### Takeaway
Two more studies support big, forgiving targets and warn about drag.

### Cited findings
- Woodward et al., CHI 2016, 30 children ages 5 to 10: first-try miss rates around 23 to 24% for children versus 15 to 17% for adults; small targets much harder; targets padded from the edge nearly doubled misses (children 31% vs 17%); children missed more on the right and top; gesture accuracy for ages 8 to 10 76%, ages 5 to 7 65% (user-independent); recommendations: prominent immediate feedback for accepted touches, avoid small targets at edges, allow out-of-bounds touches. [research] https://init.cise.ufl.edu/wp-content/uploads/sites/378/2017/05/Woodward-et-al-CHI2016_0.pdf
- Cassidy, Read, MacKenzie 2019, 28 children ages 8 and 9 on tablets: drag and drop errors about 8% on large targets and 15 to 21% on small; finger error 12.6% versus stylus 9.3%; authors suggest select-and-tap may suit children better (their inference, not tested). [research] https://www.yorku.ca/mack/interact2019.html

### Inferences (mine)
- A scrub drag is forgiving because no target is hit; the risky steps are drag to a small drop point (burrs) and hold at a small spot (nails). Make those targets large and accept near misses.

### Gaps
- No study on hold duration for children. No data on large phones versus small. No study of Roblox touch controls.

## 8. What this means for washing a cat (my own inference, not sourced)

Starting step types (4 at the start, add 1 every few jobs): (1) scrub, a drag over the dirty fur with a generous brush and live suds; (2) rinse, a drag with a water spray that must also pass over soap spots; (3) dry or towel, a different motion such as a circular rub; (4) a pick step, tap or drag a burr out, with both allowed (NN/g tap or drag helped). Later: nail trim hold, brush tangles, ear clean, treat step. The owner's dislike of three same swipes suggests never putting two of the same step in a row in the first jobs; rinse and scrub are both drags, so give them different feel (suds versus water, different sound, different tool).

Job length: 5 to 6 steps of 8 to 15 seconds each, about 60 to 90 seconds in total. WarioWare is 4 to 8 seconds a game; Cooking Mama up to a dozen steps; Roblox salon sessions are 9 to 19 minutes, so about 8 to 15 jobs a session. Show a step counter (1 of 5).

Scoring: grade each step, then average (Cooking Mama and Papa's). Use 3 stars as the normal good result (Barber Simulator), a secret fourth for a perfect run, and never remove coins for a low grade; show a breakdown line per step with praise that names the action. Never show a fail screen; a miss only lowers the stars. Keep the combo as a bonus that pauses and does not reset.

Camera: show the side being cleaned and turn the cat for the player between steps, with a visible "side 2 of 3". Let the player flick to turn only if testing shows they want it.

Upgrades: mix speed and motion. Examples: a wider brush, a spray that fans out, a comb that shows hidden burrs, a tool that auto-picks one burr per step (Fisch auto-progress idea).

Long VIP job (16 steps in the competitor): split into three or four chapters of 4 or 5 steps with a checkpoint pop-up and a visible bar; change tool or step type at each chapter; give a mid-job reward (a cat reaction, a sparkle) and a bigger payoff at the end (the cat looks different, a collection entry, a permanent boost). Let a quit save progress. Keep the same step type from repeating inside a chapter. Barber Simulator makes its VIPs picky rather than longer (stricter match, double pay); that is another way to make them special without 16 steps. Test both.

## Biggest gaps
- My Pet Salon! step list, step count, star rules and upgrade effects, which only the owner can supply.
- No job length in seconds for any Roblox game; no evidence on combo counters for children; no evidence on touch rotation.
