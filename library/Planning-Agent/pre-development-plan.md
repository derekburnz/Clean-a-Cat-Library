# Clean a Cat: what we need from Derek before we build (2026-11-23 ET, Planning-Agent)

This is the file copy of the plan page. The page lets Derek tick jobs, pick answers and type playtest notes, and it saves them where the team can read them. Page: https://claude.ai/artifact/QVD8oT37EZy9vE8mYz9KfG

Three parts: play three games, do the setup jobs and confirm our picks. Every question has a recommended answer and the team is already working on it. Nothing here locks the design before the playtest notes are in.

## 1. Play these three first
Ten minutes each, as a brand new player, on a phone if possible, with a timer running. Player counts are from the morning of November 23, 2026.

| Game | Players and votes | Why it is on the list | Look for |
|---|---|---|---|
| [Capybara Onsen](https://www.roblox.com/games/120336108521610) | 368 playing, 97% liked of about 59K votes | The most played and best liked animal spa game on Roblox. | What you do with your hands, how capybaras arrive, what you build or unlock and why it holds a few hundred players and not thousands. |
| [My Pet Salon!](https://www.roblox.com/games/134135989047078) | 175 playing, 86% liked of about 930 votes | Our closest rival. Its page promises wash, brush, dry and cuddle for customers' pets. | Whether customers bring the pets, how each step is done, how long one pet takes and what the stations and levels add. |
| [Save a Horse: Wash & Collect](https://www.roblox.com/games/119493855221779) | 36 playing, 90% liked of about 1.4K votes | The only game found that joins washing to collecting, which is our mix. | How you get a horse, whether washed horses are kept and earn and how the collection is shown. |

**What to write down for each game**
1. How do you get a pet, and how many seconds does it take?
2. Seconds from spawn until you first did something fun.
3. Is the washing done by hand (drag, scrub, hold) or by one button?
4. Seconds until the first reward and the minute of your first upgrade.
5. Any build or wait timers, and how the wait felt.
6. What the game told you to do next at minute 1, minute 3 and minute 5.
7. The first pop-up, shop prompt or Robux offer and when it came.
8. The moment you got bored or confused, if any.
9. What it does well, what we should do better and whether you would open it again tomorrow.

**The team also asked for**
- Art: How the dirty and clean looks differ (mud patches, colour change, sparkle) and whether the reveal felt good.
- Effects and sound: Which washing, reveal or sound moment felt best.
- Screens: Did any window open by itself? How does the tutorial point (arrows, text, dimming)? Where do the main buttons sit on a phone?
- Camera: What the camera does while you care for the pet.
- Screenshot: One screenshot of each game's phone screen helps the most.

**If there is time**
- [Wash the Pets](https://www.roblox.com/games/106050444354181): The feel of the washing and how fast it gets dull.
- [Clean an Animal!](https://www.roblox.com/games/75217712603520): Why 17% disliked it: bugs, waits or pay walls.
- [Wash a Cat](https://www.roblox.com/games/87832865714820): Two minutes is enough. What it is and whether it is any good.
- [Throw Food For Animals](https://www.roblox.com/games/120219252362013): The first minute we want to match: how fast the first animal is yours, the first three prices and how it points to the next goal.
- Wash the Car (how washing is done by hand), Clean The Ballpit! (why picking up feels good) and Steal An Egg (the arrows and the menu that shows what grows while you are away).

## 2. Derek's to-do list
Ids are not secret and can go in chat. Keys are secret and only ever go into GitHub.

**Now, so building is not blocked**
- [ ] **Send the Creampuff Games group id.** It is the number in the group page's address. It is not secret. Uploads and the game must have the same owner, so we need it before any art or sound goes up.
- [ ] **Create the experience under the group and send its two ids.** An experience is Roblox's word for a game. In Creator Hub create it under Creampuff Games, then send the universe id (the whole game) and the start place id (its first map). Both are in the page address and are not secret.
- [ ] **Make a dev copy of the place.** Agents never work in the published place. In the dev copy turn on Game Settings, Security, Enable Studio Access to API Services so saves and switches work in Studio.
- [ ] **Get the PC ready for Studio work.** On DESKTOP-DFOGFG7: Git, Rokit and the Rojo plugin installed, the repo cloned under Downloads and Remote Control on. Rojo copies our files into Studio. Sync-Agent walks you through it. [Setup guide, steps 2 to 5](https://github.com/derekburnz/Clean-a-Cat/blob/main/docs/setup-guide.md)
- [ ] **Listen to the 11 sounds (about 2 minutes).** Bubble pops, mud plop, reveal chime, brush swishes, bow pop, camera and click. Say which are too loud, too sharp or wrong. [The sound files](https://github.com/derekburnz/Clean-a-Cat/tree/main/assets/clean-a-cat/audio)

**Before the first publish**
- [ ] **Create the Open Cloud key and paste it into GitHub.** Open Cloud is Roblox's web API and a key is a password for it. Create it under the group, then paste it into GitHub as the secret ROBLOX_PUBLISH_KEY. Never paste it in chat. Claude never sees it. [Setup guide, step 8](https://github.com/derekburnz/Clean-a-Cat/blob/main/docs/setup-guide.md#8-the-open-cloud-key-lets-github-publish)
- [ ] **Add the three repo variables.** In GitHub, Settings, Secrets and variables, Actions, Variables: ROBLOX_UNIVERSE_ID, ROBLOX_PLACE_ID and ROBLOX_GROUP_ID. These tell the publish workflow which game and who owns uploads.
- [ ] **Optional: a second key for uploads.** ROBLOX_GROUP_KEY, created under the group with only asset read, asset write and asset permissions write. It keeps the publish key from uploading and the upload key from publishing.
- [ ] **Check auto-merge and the two required checks.** In GitHub: Allow auto-merge is ticked and the ruleset for main requires both checks. Without required checks a pull request would merge before its tests ran. [Setup guide, step 9](https://github.com/derekburnz/Clean-a-Cat/blob/main/docs/setup-guide.md#9-required-check-and-auto-merge)
- [ ] **Set the server size to match the street.** In the experience settings set the maximum players per server to the number of spas per street (our pick is 6, see the question near the end). Each player needs their own plot. [Issue 88](https://github.com/derekburnz/Clean-a-Cat/issues/88)
- [ ] **Play the scrub prototype on your phone.** Two minutes when it is ready. Say keep or rethink. Nothing past the brush and photo step is built until you say keep. [Issue 29](https://github.com/derekburnz/Clean-a-Cat/issues/29)

**Before build notifications go on**
- [ ] **Create the build finished message and send its id.** Once the experience exists: Creator Dashboard, Engagement, Notifications. Create a message with a {buildName} parameter, for example: Your {buildName} is finished and the cats are waiting. Send us the message id. It is not secret and goes in the NotifyMessageId setting. [Pull request 90](https://github.com/derekburnz/Clean-a-Cat/pull/90)
- [ ] **Create a key for sending notifications and save it as an experience secret.** An Open Cloud API key with user notification write access only. Save it yourself in the experience's secrets under the name CleanACat_NotifyKey, where only the game's server can read it. Never share the key, in chat or anywhere else. [Pull request 90](https://github.com/derekburnz/Clean-a-Cat/pull/90)

**Before the first public test: Roblox Kids and Select**
- [ ] **Creator account age-checked and verified, with 2-step verification.** Roblox shows a new game only to age-checked players of 16 and over until it passes the Kids and Select evaluation. Kids is ages 5 to 8 and Select is ages 9 to 15, which is our audience.
- [ ] **An active Plus or Premium subscription, or the one-time fee.** The page asks for a subscription that is at least 2 months old, or a refundable fee per game.
- [ ] **Fill in the full maturity questionnaire.** We write down the answers for you first. The game needs a Minimal or Mild result. Our reading is that it qualifies: only cats are bathed, on an open shop floor, with no chat rooms and no closed rooms for avatars.
- [ ] **100 plays from highly engaged players within 60 days.** Roblox evaluates the game after that. Growth-Agent plans how to get them. Your group's players from the other game can help.

Read on Roblox's Kids and Select page on November 23, 2026. Roblox changes these rules, so check the page again before acting.

**At release**
- [ ] **OK the final icon and thumbnails before upload.** Pick from the drafts in the Store art questions at the end of this page. Model-Agent then makes the finals and nothing is uploaded without your OK. [Issue 24](https://github.com/derekburnz/Clean-a-Cat/issues/24)
- [ ] **Make both repos private.** Your call from November 23: public for now, private at release.

## 3. Questions, each with our recommended answer
The first option is the recommendation.

**The game** (from Planning-Agent)

| # | Question | What it means | Options, recommended first |
|---|---|---|---|
| 1 | Customers bring dirty cats and strays stay with you | People queue at the door holding a dirty cat. A board shows which cats can come and the chance of each. Now and then a stray turns up at the back door, and once clean it lives in your display window. The very first cat is a stray, so every player owns a cat inside the first minute. No catching. Your playtests decide this one. See how the three games hand you a pet. | Yes, go with it / Customers only, no strays / Something else |
| 2 | Two build slots | The builder kitten builds one station at a time (seconds up to 1 hour). A building site builds one room at a time (hours). With one slot a first session never reached the 8 hour build, and once it ran nothing else could be built for 8 hours. | Yes, go with it / One build at a time / Something else |
| 3 | Longest build is 24 hours and the first 8 hour build starts in the first session | Tools are instant. Then 10 seconds, 1 minute, 10 minutes and 1 hour for stations. The VIP Room takes 8 hours and is offered at about minute 6. Later rooms take 12 to 24 hours and never longer. A finished build waits for the player and nothing is lost by coming back late. | Yes, go with it / Shorter, 12 hours at most / Longer builds are fine / Something else |
| 4 | No paid skips for build timers at launch | We sell a Second Builder pass instead. Paid skips on timers read as pressure for a young audience and reviewers of spa games complain about them most. | Yes, no paid skips / Sell skips at launch / Something else |
| 5 | Starting prices and pay | A common cat pays 10 coins plus a tip of 2. Bubble Soap 30, Brush Table 40, dryer 75, VIP Room 100. A window cat tips 1 coin every 10 seconds and the away jar holds 1 hour of tips. This gives a purchase at about minute 2, 3 and 5 and the long build near minute 8. Paper numbers until the scrub is timed on a phone. | Yes, go with it / Something else |
| 6 | A shared street with one spa each | Spas sit side by side so players see each other's windows and reveals. Not in the game: stealing, trading, fighting and typed text. Cat names come from a list. How many spas and whether players can walk in are the last two questions. | Yes, go with it / Something else |
| 7 | Three game passes at launch and coins cannot be bought | 2x Coins, Second Builder and Golden Sponge (a wider scrub with gold bubbles). No buyable coins, so the random customer never counts as a paid random item. Nothing sold changes the chances. | Yes, go with it / Something else |
| 8 | Put the words cat spa in the description and on the icon | Your cat spa ad did well. The title stays Clean a Cat. | Yes, go with it / Title only, no cat spa wording / Something else |
| 9 | A Cat Show weekend as your first event | Day 7 is yours. A themed show with voting is the natural first event. It is out of scope for the first build. | Yes, plan it for later / I have a different event in mind / Something else |

**The first minutes and screens** (from Design-Agent)

| # | Question | What it means | Options, recommended first |
|---|---|---|---|
| 10 | Notifications are asked for with a bell button | The player taps a bell beside any build over 1 hour. No prompt opens by itself. Only players of 13 and over can get these messages, so younger players see Ready in 8 h. Come back to see it! | Yes, the bell / A prompt after the first long build starts / Something else |
| 11 | Pick a bow on every cat | One tap to finish each cat with one of three bows. | Yes, every cat / Only the first cat / Something else |
| 12 | A close camera at the tub with the thumbstick hidden on phones | While washing, the camera moves in on the cat and the move stick hides so the whole screen is for scrubbing. | Yes, go with it / Keep the normal camera / Something else |
| 13 | Hide the Shop button until the first build is done | Keeps the first three minutes about the cat. Roblox counts players who leave in that window. | Yes, go with it / Show the Shop from the start / Something else |
| 14 | Lock phones to landscape | One layout to get right, with more room for the tub and the tools. | Yes, go with it / Allow portrait too / Something else |

**The look** (from Model-Agent)

| # | Question | What it means | Options, recommended first |
|---|---|---|---|
| 15 | Art style | Bubble Pastel colours (cream, mint, bubblegum, sky and dark mud) on the blocky chibi cat body from your asset library. It reads on phones, needs no mesh uploads and makes the mud pop. | Yes, Bubble Pastel on the library body / Cozy Storybook (warm wood, painted textures) / Bright Toy (saturated, glossy) / Something else |
| 16 | Reuse the Cat Cafe cat body with all new coats | Same body shape, new coats and names, plus spa extras (mud, fluff and bows). No Cat Cafe character is reused. | Yes, go with it / Make the cats look clearly different from Cat Cafe / Something else |
| 17 | Ten working cat names for the first Cat Index | Muffin, Smudge (the first stray), Inky, Cotton, Tux, Patches, Toffee, Marble, Lilac Cloud and Starcoat. None is used in Cat Cafe. | Yes, use these / I want to name them / Something else |
| 18 | Cats bigger than life | About half an avatar's height, so the cat fills the screen at the tub on a phone. | Yes, go with it / Something else |

**Sound and feel** (from Motion-FX-Agent)

| # | Question | What it means | Options, recommended first |
|---|---|---|---|
| 19 | The feel of the cleaning | Soft and cosy means pastel bubbles, gentle sounds and small sparkles. Splashy and cartoony means big suds and bouncy pops. | Soft and cosy / Splashy and cartoony / Something else |
| 20 | Reuse the purr and meow sound code and make two new music tracks | The purr and meow code comes from your asset library. The music is new, from the same generator, so Clean a Cat has its own. | Yes, go with it / All new sounds / Something else |
| 21 | Upload about 15 short sounds and 2 music tracks under the group | As one batch, after you have listened. It uses some of the monthly audio upload quota. | Yes, as one batch after I listen / Not yet / Something else |

**The street** (from Gameplay-Engineer)

| # | Question | What it means | Options, recommended first |
|---|---|---|---|
| 22 | Spas per street, which is also the server size | Each server is one street and every player gets their own spa plot on it. Six keeps the street lively, keeps every window close enough to see and stays light on cheap phones. You set the same number as the server size in the experience settings. | 6 spas per street / 4 spas / 8 spas / Something else |
| 23 | Can players walk into a neighbour's spa? | Our pick: players see each other's windows and reveals from the street but cannot walk in. Walking in is built behind a switch that stays off, so friends helping in your spa can be turned on later without a rebuild. It keeps the first build simple and stops a crowd standing on someone's tub. | Look through the window only / Walk in from the start / Something else |

**Store art** (from Model-Agent)

| # | Question | What it means | Options, recommended first |
|---|---|---|---|
| 24 | Pick the icon | The icon is the small square players see on Home and in search, often at only 48 pixels. Icon B shows the whole muddy cat with the sponge and keeps the name readable when small. Rendered from the real models. Nothing is uploaded until you say so. Pictures: `Model-Agent/store-art/store-art-draft-2026-11-23.png` in the shared folder. | Icon B / Icon A / Icon C / Something else |
| 25 | Pick the thumbnails | Thumbnails are the wide pictures on the game's page and on Home. Roblox can rotate a set and show which one wins the most taps, so more than one is useful. Thumbnail 1 shows the scrub and thumbnail 2 shows muddy to fluffy, which are both things a new player does in the first minute. Pictures: `Model-Agent/store-art/store-art-draft-2026-11-23.png` in the shared folder. | Thumbnails 1 and 2 / All three / A different set / Something else |

## Already decided
- **Name:** Clean a Cat, locked November 23. Slug clean-a-cat.
- **Direction:** A hands-on cat spa: clean dirty cats, earn, upgrade the spa. No catching.
- **Goals:** A fun first 5 minutes for a very low bounce rate and a reason to come back on day 2. You handle day 7 with events.
- **Repos:** Public for now, private at release.
- **How we work:** Every passing pull request merges itself. Publishing is silent. Restarts are fine until public release.

## What happens when Derek is done
Planning-Agent reads the answers from the page, folds the playtest notes into `gdd-draft.md`, asks for the design lock, finishes `milestone-1.md` and hands over to the coordinator.
