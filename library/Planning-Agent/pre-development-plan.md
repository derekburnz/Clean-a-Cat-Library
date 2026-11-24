# Clean a Cat: what is left before we build, round two (2026-11-24 ET, Planning-Agent)

This is the file copy of Derek's plan page, second version. The page lets Derek tick jobs, pick answers and type playtest notes, and it saves them where the team can read them. Page: https://claude.ai/artifact/QVD8oT37EZy9vE8mYz9KfG

Round one is saved (playtest-notes.md, plan-page-round-one.md). This version holds only what is open. The questions are new and came from Derek's playtest notes, his comments on the mud, the baths and the store art, the two research rounds and the open calls from the other threads. Database ids: playtests `p-<id>`, to-dos `c-<id>`, questions `q2-<id>` (the round one questions were `q-<id>` and stay in the database untouched).

## 1. Play these 4 next
Player counts are from the morning of November 24, 2026.

| Game (id) | Time | Players and votes | Why it is on the list | Look for |
|---|---|---|---|---|
| [Save a Horse: Wash & Collect](https://www.roblox.com/games/119493855221779) (`horse`) | 10 minutes | 36 playing, 90% liked of about 1.4K votes (November 23) | Left over from the first list. It is the only game we found that joins washing to collecting, which is the mix we recommend below. | How you get a horse, whether washed horses are kept and earn, how the collection is shown and whether the horse you got was ever a surprise. |
| [Clean Everything](https://www.roblox.com/games/140576663170542) (`cleaneverything`) | 15 minutes | about 6,500 playing, 95% liked of about 74K votes | The only cleaning game we found that kept its players. It holds about 60% of its peak. Five of the six others from this summer are at 3% or less. | What there is to do after the first room is clean, the start again step (rebirth), what friends add and the minute it first felt finished. |
| [Restaurant Tycoon 3](https://www.roblox.com/games/119048529960596) (`rt3`) | 15 minutes | about 5,100 playing, 95% liked of about 429K votes | The shop game that lasted longest. It still has players after 22 months, with sessions near 26 minutes. It is the closest thing on Roblox to your busy spa idea. | The queue, what happens when a customer waits, what the staff take over, how rare customers differ and what the game gives you to do at minute 10. |
| [Barber Simulator](https://www.roblox.com/games/134026357772960) (`barber`) | 10 minutes | about 5,200 playing, 89% liked of about 25K votes | A hands-on job game like ours, six weeks old. Its rare customers are pickier, not longer, which is what we suggest in place of 16 step jobs. | How each step is done by hand, how long one customer takes, how the rare customers differ and when it starts to feel the same. |

**What to write down for each game**
1. Seconds from spawn until you first did something fun.
2. Seconds one job takes from start to reward: one wash, one room or one customer.
3. The minute it first felt finished or dull.
4. Whether what you got was ever a surprise.
5. What would bring you back tomorrow, if anything.
6. Whether other players mattered.
7. In the two shop games: what happens when a customer waits too long and what the staff take over.

**The team also asked for**
- Screens: A screenshot of the phone screen during a job and of the card after a job helps the most.
- Store: The icon or picture that made you want to tap, if any.

**If there is time**
- [My Pet Salon!, ten more minutes](https://www.roblox.com/games/134135989047078) (`petsalon2`): Four things we still miss: seconds for one normal job, how many jobs before you wanted to stop, how much slower the hired helper is than you and, once the waiting bench is bought, whether you can choose which waiting pet goes first.
- [Clean The Ballpit!](https://www.roblox.com/games/126221718321318) (`ballpit`): The biggest cleaning game right now (about 22,000 playing). Why picking up feels good and what it gives you to do after the first clean.
- [Wash the Pets](https://www.roblox.com/games/106050444354181) (`washpets`): The feel of the washing and how fast it gets dull.
- [Clean an Animal!](https://www.roblox.com/games/75217712603520) (`cleananimal`): Why 17% disliked it: bugs, waits or pay walls.
- [Wash a Cat](https://www.roblox.com/games/87832865714820) (`washacat`): Two minutes is enough. What it is and whether it is any good.
- [Throw Food For Animals](https://www.roblox.com/games/120219252362013) (`throwfood`): The first minute we want to match: how fast the first animal is yours, the first three prices and how it points to the next goal.
- Wash the Car (washing by hand) and Steal An Egg (the arrows and the menu that shows what grows while you are away).

**Played and saved in round one**
- My Pet Salon!: You liked the different kinds of step, the praise words with a growing number, the star card with coins and experience after each pet, tool upgrades, the index, rare customers with a lasting reward and hired helpers. You disliked the cutscene with no skip, the same swipe three times, 16 steps in one job, the pet turning by itself and only one customer at a time. First fun thing at about 75 seconds.
- Capybara Onsen: Not a spa game: step on pads, buy and merge. Useful all the same: a short tutorial with a free first buy, a friend bonus percent on screen from the start and a request for a favourite at about minute 4.

## 2. Derek's to-do list (open jobs only)

**Now, about 15 minutes in all**
- [ ] **Add the rule that makes pull requests wait for their tests** (`automerge`). We checked on November 24 and main has no rule yet. Pull requests have waited for their tests only because each thread waits by hand, so nothing stops a merge with a failed test. To add it: in the Clean-a-Cat repo open Settings, Rules, Rulesets, New ruleset, New branch ruleset. Name it main, set Enforcement status to Active, under Target branches choose Include default branch, tick Require a pull request before merging, tick Require status checks to pass and add these two checks by name: Rojo sourcemap, luau-lsp, Selene, StyLua and Unit tests, strict types, UI gate. Then press Create. About 2 minutes, or say the word and we do it through your Chrome. [Setup guide, step 9](https://github.com/derekburnz/Clean-a-Cat/blob/main/docs/setup-guide.md#9-required-check-and-auto-merge)
- [ ] **Turn on saves for Studio in the dev copy** (`apiaccess`). Open Clean-a-Cat-Dev in Studio, then Game Settings, Security, switch on Enable Studio Access to API Services and save. Without it, saved data and the live switches do not work when we test in Studio.
- [ ] **Read the loop options write-up** (`loopdoc`). Five minutes. It is the research behind the first nine questions below: why cleaning games fade, what the games that last share and how your busy spa idea fits. [Clean a Cat: loop options](https://claude.ai/artifact/8NLjC3vdU8tZ34AbGvfjit)
- [ ] **Flip through the 14 draft screens** (`screens`). Phone and desktop pictures of every screen the game will likely need. The questions below show eight of them. Say in chat if any screen looks wrong. [Screen pictures](https://github.com/derekburnz/Clean-a-Cat/tree/main/docs/concepts/clean-a-cat/ui-2026-11-24)
- [ ] **Tell us which phone and tablet you test on** (`devices`). One line in the project chat, for example the model of your phone and that you have an iPad. We match our test sizes to them.

**After today's playtests**
- [ ] **Play our scrub on your phone for two minutes** (`scrub2`). You said no prototypes until the playtests and the research were done. The research is done, so this is next once your games are played. Two fixes land first: scrubbing over the move stick also walked the player and one drag cleared too much mud. We set the session up for you. Three answers are all we need: did scrubbing feel good, was the reveal a nice surprise and would you wash a second cat. [Issue 29](https://github.com/derekburnz/Clean-a-Cat/issues/29)

**Parked until the game is picked**
- Server size: Set once the street and the design are picked.
- Maturity questionnaire: We write the answers down for you once the gameplay is decided. The game needs a Minimal or Mild result.
- 100 plays from engaged players: Your ads for this come when the game is ready for public testers.
- Build finished notification: The text and its key are only needed if we keep that idea. Players under 13 cannot get it.
- Store art, second version: A more detailed icon and thumbnails wait for the design to lock.
- Sound uploads: One batch after the game is picked.
- Plus or Premium: Only if Roblox asks for it when we apply for Kids and Select.
- Private repos: At release.

## 3. 42 questions, each with our pick first

**The game** (from Planning-Agent) These nine decide what we build. Your playtests today test them.

| # | Question (id) | What it means | Options, our pick first |
|---|---|---|---|
| 1 | Your busy spa and a cat collection, together (`loop`) | Your idea after My Pet Salon becomes the minute to minute play: several cats wait, you pick who is next and helpers take the easy ones. The collection is the reason to keep going: every cat's coat is hidden under the mud, and each new one fills a slot in your Cat Index. Five of the six cleaning games from this summer are at 3% of their peak or less. The one that held on gives players more to chase than the cleaning. The loop options write-up in your to-do list has the research behind this. | Yes, both together / Busy spa only / Collection only, one cat at a time / Something else |
| 2 | Cats wait on a bench and you pick who is next (`queue`) | You called one customer at a time kinda lame. Three or four cats wait, each with a card: name, how dirty, what kind of dirt and what it pays. Picking only matters when the cats differ, so a muddier cat pays more and a fussy one tips more but waits less. Each card also gets one line of our own on how the cat got so dirty, an idea from the story line on the wash screen you sent. Your screenshots show My Pet Salon sells a waiting bench and says Groom next pet. We do not know yet if you can choose among the pets waiting there, so that is now on its ten more minutes below. | Yes, a bench and a pick / One cat at a time / Something else |
| 3 | Waiting cats get grumpy but are never lost (`impatience`) | You floated customers who get impatient and leave. Lost customers are what parents and reviewers complain about most in shop games. Our pick: a waiting cat's mood drops and only its bonus tip shrinks. A cat that waits far too long goes home and comes back later. | Yes, grumpy and a smaller tip / They leave and the job is lost / No waiting pressure at all / Something else |
| 4 | Hired helpers wash common cats, slower than you (`helpers`) | Your idea. Helpers are bought with coins and never with Robux. A helper takes a common cat from the bench, washes it slowly and earns fewer stars. Rare cats and strays always wait for you. The picture still shows kitten helpers. Who the helpers are is the next question. | Yes, slow helpers for common cats / Helpers can wash any cat / No helpers at launch / Something else |
| 5 | Helpers are human staff, not cats (`helperlook`) | You said on November 24 that helpers are likely staff like humans. Our pick agrees. A person in a spa apron reads as staff at a glance, has hands for the sponge and the towel and can reuse the customer figures we already build, so it costs less than a kitten that has to hold tools. One other idea: staff do the washing and Suds the kitten stays as the spa's mascot, who points things out in the first minutes and cheers but never washes. The builder kitten for stations is a separate call. Say in the note if the builder should be a person too. Update: you said ok to staff with Suds as the mascot, and that Suds should not stand. So he walks on four paws like every other cat, which also means he cannot hold a tool. He explains things by trotting to them and sitting beside them with a speech bubble of a few words, and he shows up again each time something new unlocks. | Human staff, no helper cats / Human staff, and Suds stays as the mascot / Kitten helpers as drawn / Something else |
| 6 | Rare visitors who are pickier, not longer (`rare`) | You liked the influencer customers and their lasting reward, but 16 steps felt long. Ours bring a rare cat and want a near perfect wash, with the same short job as any cat. A finished visit gives a lasting reward, for example a small permanent tip bonus and a framed photo for your wall. Visitors unlock as your spa earns stars. The chance of each is on a board and none can be bought. | Yes, pickier and not longer / Longer jobs for rare visitors / No rare visitors at launch / Something else |
| 7 | How cats become yours (`keep`) | Customers take their cats home, and every coat you reveal fills a slot in your Cat Index. Now and then a stray turns up at the back door. A washed stray stays in your display window and earns tips. The very first cat is Suds, the kitten you rescue in the opening, so every player has a cat of their own inside the first minute. Suds is the same for everyone and is not in the index, as you said on November 24. He has his own card outside the count. He is the mascot, so he does not sit in the window or earn tips. The first customer after him is an easy common cat, which gives the first index stamp, and the first window stray turns up at about minute 4. No catching and no buying cats. | Yes, index for all and strays stay / Index only, no cats live in the spa / Something else |
| 8 | You rescue a muddy kitten from a box, and he becomes Suds (`firstminute`) | Your idea from November 24: a truck drives past, a plain brown box falls off the back and lands in front of you, you open it and find a messy, muddy kitten, and the tutorial is cleaning him up for a score. Once he is clean he becomes Suds. The box is settled: a random brown box, so his name comes from the wash. Still open, and you said you will come back to it: how the scene plays. Your thought is a quick intro you watch, the truck going by and the box falling in front of you, and then you get your camera back and play. We first wrote it as a scene you play with the camera yours the whole time. Your version has one clear plus, which is that nobody can be looking the wrong way and miss the box, so it is now our pick too with one limit: about 4 seconds and no more, because you disliked the cutscene with no skip in My Pet Salon. Either way you tap the box at about second 4 and scrub at about second 12, which is about 9 seconds later than spawning at the tub. So we would run it against the tub start behind a switch and keep the one that holds more new players. His wash always ends on three stars, so nobody fails the opening. | A quick intro you watch, about 4 seconds, then play / A scene you play, the camera is always yours / No scene, spawn at the tub and scrub / Something else |
| 9 | Aim for a first session of 20 minutes or more (`session`) | In one report on Roblox games, about 11 in 100 new players came back the next day when sessions ran over 25 minutes and about 4 in 100 when they ran under 3. That is a link, not proof. It means more on day one than we first planned: about 12 cats, 3 kinds of dirt and 4 tools. Your screenshot of My Pet Salon's album shows 59 pets in six rarities. Twelve coats would look thin beside that, and a coat costs us far less than a new animal because every cat shares one body. So we would go to about 24 coats on day one if Model-Agent confirms the cost. | Yes, build more for day one / Keep the first build small and add later / Something else |

**The wash** (from Planning-Agent and Design-Agent)

| # | Question (id) | What it means | Options, our pick first |
|---|---|---|---|
| 10 | Four kinds of step at the start (`steps`) | You liked the variety in My Pet Salon. Ours at launch: scrub the mud, rinse with the shower, pick burrs out of the fur and towel dry. Later tools add nail trim, comb, shampoo and the dryer. The models for all of these are drafted. | Yes, these four first / Fewer: scrub, rinse and dry / All of them from the start / Something else |
| 11 | Four to six short steps per cat, never the same step twice in a row (`joblength`) | You found the same swipe three times boring and 16 steps too long. Each step lasts 8 to 15 seconds, so a cat takes about a minute. A Step 2 of 4 line shows how far along you are. | Yes, 4 to 6 short steps / Shorter, 3 steps / Longer jobs are fine / Something else |
| 12 | The cat holds still while you scrub (`turn`) | You said the pet turning the whole time made you miss spots. Ours stays put during a step. The game turns it between steps, and two round arrow buttons let you turn it when you want. | Yes, still while scrubbing / Slow turning all the time / Something else |
| 13 | Praise words and a combo that pauses on a slip (`praise`) | You noticed Awesome and Excellent with a growing number. Ours: short words that name what you did, one at a time and never under your finger, beside a combo count. A slip pauses the combo and does not reset it to zero, which feels unfair to young players. | Yes, pause on a slip / Reset the combo on a slip / No combo / Something else |
| 14 | Tool upgrades change how the tool feels (`tools`) | You liked upgrading tools. Each tier changes the shape and what the tool does as well as the speed: a wider sponge, a shower with a fan spray, a comb that shows hidden burrs. Tier 2 is lilac and tier 3 is gold. | Yes, each tier feels different / Speed only, simpler to build / Something else |

**Coming back** (from Planning-Agent)

| # | Question (id) | What it means | Options, our pick first |
|---|---|---|---|
| 15 | The first long build comes after about minute 15, not minute 6 (`longbuild`) | The old plan offered an 8 hour VIP Room at minute 6. In the hit games waits start at seconds and reach hours only once the player cares. The rest stays: the builder kitten builds one station at a time, a building site one room at a time, nothing takes over 24 hours and a finished build waits for you. | Yes, long builds later / Keep it at minute 6 / No builds over 1 hour at launch / Something else |
| 16 | No paid skips on timers (`skips`) | We sell a Second Builder pass instead. Paid skips read as pressure for a young audience and are what reviewers of spa games complain about most. | Yes, no paid skips / Sell skips at launch / Something else |
| 17 | Three reasons to come back tomorrow, and no streak (`return`) | Players under 13 cannot get our notifications, so a bell cannot be the main hook. Ours: a tip jar that fills while you are away and stops at a cap, the empty slots in your index and one different visitor cat each day. There is no streak to lose. Suds meets you at the door and points at the full tip jar and today's visitor. He is always glad to see you and never sad that you were away. The bell stays as a small extra for players of 13 and over. | Yes, these three / Add a daily streak reward / Something else |
| 18 | A Grand Reopening for players who finish the spa (`reopen`) | The games that last have a start again step, and so does Clean Everything. Ours: move to a bigger spa, keep every cat and gain a permanent tip bonus. It is not needed for the first test, but the saved data has to allow for it from the start. | Yes, plan it now and build it after the first test / Build it for launch / No start again step / Something else |
| 19 | A small bonus for each friend in your server (`friends`) | You saw the friend percent on screen in Capybara Onsen. Ours: 10% more tips per friend in the server, shown from the start. Helping inside a friend's spa comes later. | Yes, a friend bonus / No friend bonus / Something else |
| 20 | Neighbours look through the window but do not walk in (`visit`) | Players see each other's windows and reveals from the street. Walking in is built behind a switch that stays off, so friends helping in your spa can be turned on later without a rebuild. It stops a crowd standing on someone's tub. | Yes, window only for now / Walk in from the start / Something else |
| 21 | No trading of cats (`trading`) | Trading is the one feature with a clear record of harm to young players, mostly scams. Cats are earned by washing only. | Yes, no trading / Plan trading for later / Something else |
| 22 | No like or favourite ask in the first session (`favourite`) | Capybara Onsen asked you for a favourite at about minute 4. Roblox judges a game on its first minutes, and an ask there is one more thing between a new player and the fun. Our pick: nothing in the first session, then one small ask after a great wash on a later visit. It never comes with a reward, because Roblox does not allow rewards for likes or favourites. Your screenshot shows My Pet Salon paying cash for both in its Rewards window. By our reading of the rules that is their risk and we do not copy it. | Yes, one ask on a later visit / Ask once at about minute 5 / Never ask / Something else |

**Screens** (from Design-Agent)

| # | Question (id) | What it means | Options, our pick first |
|---|---|---|---|
| 23 | After each cat: the full card or a slim strip (`recap`) | You called the star card with a coins and experience breakdown kinda cool. With a line of cats waiting, a full window after every wash slows you down. Our pick: the full card for your first cats and for any new or rare cat, and the slim strip for the rest. Two things from your My Pet Salon screenshots go into ours. Their card sits at the side so the clean pet stays in view, with one line for each reason you earned. And Roblox's own badge note covered their Collect button, so our button stays out of that corner. | Full card for new cats, slim strip for the rest / Full card after every cat / Slim strip after every cat / Something else |
| 24 | Menu buttons appear one at a time (`hud`) | The draft has four round buttons on the left: Index, Tools, Helpers and Build. Our pick: a new player sees none, and each pops in with a short pointer the first time it is useful. Index after the first cat, Tools at the first upgrade, Build and Helpers later. That keeps the first minutes about the cat. Suds does the pointing: he trots to the new thing and sits by it. He shows each thing once, never opens a window himself and never points at anything that costs Robux. For comparison, your screenshot shows My Pet Salon with all four of its buttons on screen from the first second. | Yes, one at a time / All four from the start / Something else |
| 25 | Suds explains in a help bubble at the bottom of the screen (`sudsbubble`) | You sent My Pet Salon's help bubbles as an idea: a guide at the left, a bold line, a short sentence and one big button that does the step. Our pick is the same idea in our own look. Suds's face is at the left, the bubble holds one short title and one sentence that says why, and one button does the step, so you still do every tap. It shows one at a time for tutorial steps and new unlocks, and goes away after the tap. Theirs runs under the jump button, so ours stops short of the stick and the jump button on every phone. A Tips switch in Settings turns the bubbles off once the tutorial is done. | Yes, a bottom bubble with one button / Only a small bubble over Suds in the spa / Something else |
| 26 | A close camera at the tub with the move stick hidden (`camera`) | While you wash, the camera moves in on the cat and the move stick hides, so the whole screen is for scrubbing. Our own test found that scrubbing over the stick also walked the player away, and this fixes it. | Yes, go with it / Keep the normal camera / Something else |
| 27 | Lock phones to landscape (`landscape`) | One layout to get right, with more room for the tub and the tools. | Yes, go with it / Allow portrait too / Something else |
| 28 | A bow as the finishing touch (`bows`) | The first plan had you pick a bow on every cat. With a line waiting that is one tap too many. Our pick: bows for cats that stay with you and for rare visitors. | Bows for your own cats and rare visitors / A bow on every cat / No bows / Something else |

**The look** (from Model-Agent)

| # | Question (id) | What it means | Options, our pick first |
|---|---|---|---|
| 29 | Mud as a coat that wraps the cat (`mud`) | Your words on the three tries: random blobs, dirt blocks, then not smeared but built into the fur or coated in it. This version wraps the cat's own shapes, with drips under the jaw and belly. You have not said yet whether it works. | Yes, the coat works / Closer, keep going / Something else |
| 30 | Stink wisps so a dirty cat reads on a small phone (`mudphone`) | At phone size, mud on a pale cat can look like a patterned coat. Our pick: wavy stink lines rise off a dirty cat and stop when it is clean, so dirty reads at any size. | Yes, stink wisps / Darker mud instead / Both / Something else |
| 31 | Baths with deep blue water, white lather and clear bubbles (`baths`) | You said the pale water looked like the water was missing. The water is now deep blue to just under the rim. A nicer tub shape is being drawn now. | Yes, this water / Still not right / Something else |
| 32 | Art style (`style`) | Bubble Pastel colours (cream, mint, bubblegum, sky and dark mud) on the blocky cat body from your asset library. It reads on phones, needs no mesh uploads and makes the mud stand out. Every picture on this page is in it. | Yes, Bubble Pastel / Cozy Storybook (warm wood, painted textures) / Bright Toy (saturated, glossy) / Something else |
| 33 | Reuse the Cat Cafe cat body with all new coats (`body`) | Same body shape, new coats and names, plus spa extras such as mud, fluff and bows. No Cat Cafe character is reused. | Yes, go with it / Make the cats look clearly different from Cat Cafe / Something else |
| 34 | Working cat names (`names`) | Muffin, Smudge (the first window stray), Inky, Cotton, Tux, Patches, Toffee, Marble, Lilac Cloud and Starcoat. Suds is the mascot kitten and the first cat every player washes. He has no name until he is clean. None is used in Cat Cafe. | Yes, use these / I want to name them / Something else |

**Sound and feel** (from Motion-FX-Agent)

| # | Question (id) | What it means | Options, our pick first |
|---|---|---|---|
| 35 | The feel of the cleaning (`feel`) | Soft and cosy means pastel bubbles, gentle sounds and small sparkles. Splashy and cartoony means big suds and bouncy pops. | Soft and cosy / Splashy and cartoony / Something else |
| 36 | Upload the sounds once the game is picked (`upload`) | You listened and said they are fine for now. Uploading uses some of the group's monthly audio quota, so it needs your OK. Our pick: wait, then send them as one batch. | Yes, one batch after the game is picked / Upload now / Something else |

**Store page** (from Model-Agent and Growth-Agent)

| # | Question (id) | What it means | Options, our pick first |
|---|---|---|---|
| 37 | The store icon (`icon`) | You asked for the bath from your Cat Cafe ad, blown up, with no mud. This is the result, close on the cat's face. Nothing is uploaded until you say so, and a more detailed version waits for the design. | Yes, use it for the first test / Change it / Something else |
| 38 | The store thumbnail (`thumb`) | The wide picture on the game's page: the chunky title on a teal bubble backdrop beside the claw-foot bath. | Yes, use it for the first test / Change it / Something else |
| 39 | Add a half dirty, half clean picture (`split`) | You liked My Pet Salon's side by side picture with a thin line down the middle. Roblox can rotate thumbnails and show which one wins the most taps. Our pick: make one as the second thumbnail once the mud look is settled. | Yes, as the second thumbnail / Make it the main one / No / Something else |
| 40 | Put the words cat spa in the description (`catspa`) | Your cat spa ad did well. The title stays Clean a Cat and the icon stays free of words. | Yes, go with it / No cat spa wording / Something else |

**Money and events** (from Planning-Agent and Growth-Agent)

| # | Question (id) | What it means | Options, our pick first |
|---|---|---|---|
| 41 | Three game passes, and coins, helpers and rare cats are never sold (`passes`) | 2x Coins, Second Builder and Golden Sponge, a wider scrub with gold bubbles. Coins cannot be bought, so the random customer never counts as a paid random item. Nothing sold changes the chances, and the chance of every cat is always on a board. Your screenshots show how hard My Pet Salon sells: a starter pack on the main screen from the first minute, a limited pack with an Only 82 left counter, cash for Robux and a paid upgrade that maxes every worker. We stay with no offer on screen in the first session, no stock counters and no coins for Robux. Say in the note if you want a starter pack later. Ours would hold looks and not coins. | Yes, go with it / Something else |
| 42 | A Cat Show weekend as your first event (`event`) | Day 7 is yours. A themed show with voting is the natural first event. It is not part of the first build. | Yes, plan it for later / I have a different event in mind / Something else |

## Saved from round one
- **Your idea after My Pet Salon:** You wash by hand, hired helpers take customers too but much slower, more customers show up so you pick who is next, and maybe customers who wait too long leave. Saved as a direction, not a decision.
- **Mud:** Random blobs, then dirt blocks, then: not smeared, built into the fur or coated in it.
- **Baths:** Pale water under white foam looked like the water was missing.
- **Store art:** A chunky title on teal bubbles, no mud and the bath from your Cat Cafe ad blown up. You liked a half dirty, half clean picture.
- **Setup you finished:** Group id, experience ids, the dev copy, both keys, the PC, the sound listen and the age check. The first publish ran on November 23 at 10:14 PM ET.
- **The first 25 questions:** You left them all parked. The questions on this page replace them.
- **Name:** Clean a Cat, locked November 23.
- **Direction:** A hands-on cat spa. No catching.
- **Goals:** A fun first 5 minutes and a reason to come back on day 2. You handle day 7 with events.
- **How we work:** Passing pull requests merge themselves. Publishing is silent. Restarts are fine until public release.

## What happens when Derek is done
Planning-Agent reads the answers from the page, folds them and the playtest notes into `gdd-draft.md`, asks for the design lock, finishes `milestone-1.md` and hands over to the coordinator.
