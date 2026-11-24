#!/usr/bin/env python3
"""Round two of Derek's plan page: an HTML page and a Markdown copy from one data set.
Usage: build_plan2.py OUT_HTML OUT_MD   (the CSS is taken from build_plan.py next to this file)"""
import html, json, os, re, sys

OUT_HTML, OUT_MD = sys.argv[1], sys.argv[2]
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "https://github.com/derekburnz/Clean-a-Cat"
LOOPDOC = "https://claude.ai/artifact/8NLjC3vdU8tZ34AbGvfjit"
OLD = open(os.path.join(HERE, "build_plan.py"), encoding="utf-8").read()
CSS = re.search(r"<style>(.*?)</style>", OLD, re.S).group(1)

# ---------------------------------------------------------------- playtests
NOTE_PROMPTS = [
    "Seconds from spawn until you first did something fun.",
    "Seconds one job takes from start to reward: one wash, one room or one customer.",
    "The minute it first felt finished or dull.",
    "Whether what you got was ever a surprise.",
    "What would bring you back tomorrow, if anything.",
    "Whether other players mattered.",
    "In the two shop games: what happens when a customer waits too long and what the staff take over.",
]
EXTRA_PROMPTS = [
    ("Screens", "A screenshot of the phone screen during a job and of the card after a job helps the most."),
    ("Store", "The icon or picture that made you want to tap, if any."),
]
PET_OPTS = ["Handed to you at spawn", "A customer brings it", "You go and find it", "You buy it", "You hatch it", "Something else"]
WASH_OPTS = ["By hand (drag, scrub, hold)", "One button press", "No real washing"]
WAIT_OPTS = ["No timers seen", "Short waits, fine", "Long waits, annoying", "Long waits, but I wanted to come back"]
BACK_OPTS = ["Yes", "Maybe", "No"]
LATE_OPTS = ["Nothing happens", "They pay or tip less", "They leave", "Did not see it"]
STAFF_OPTS = ["None seen", "Slower than you", "As fast as you", "They do everything for you"]
PICK_OPTS = ["Yes, you pick", "No, one at a time", "No, a fixed order"]
MATTER_OPTS = ["No", "A little", "Yes, a lot"]

F_FUN = ("txt", "fun", "Seconds to the first fun thing", "for example 20")
F_JOB = ("txt", "job", "Seconds for one job", "for example 60")
F_DULL = ("txt", "dull", "Minute it first felt dull", "for example 8, or never")
F_BACK = ("sel", "back", "Open it again tomorrow?", BACK_OPTS)
SHOP_FIELDS = [F_FUN, F_JOB, ("sel", "pickq", "Can you pick who is next?", PICK_OPTS),
               ("sel", "late", "A customer who waits too long", LATE_OPTS),
               ("sel", "staff", "Helpers or staff", STAFF_OPTS), F_BACK]

GAMES = [
    dict(id="horse", name="Save a Horse: Wash & Collect", url="https://www.roblox.com/games/119493855221779",
         stats="36 playing, 90% liked of about 1.4K votes (November 23)", mins="10 minutes",
         why="Left over from the first list. It is the only game we found that joins washing to collecting, which is the mix we recommend below.",
         look="How you get a horse, whether washed horses are kept and earn, how the collection is shown and whether the horse you got was ever a surprise.",
         fields=[("sel", "pet", "How do you get a pet?", PET_OPTS), F_FUN, ("sel", "wash", "The washing is", WASH_OPTS),
                 ("sel", "wait", "Timers and waits", WAIT_OPTS), F_JOB, F_BACK]),
    dict(id="cleaneverything", name="Clean Everything", url="https://www.roblox.com/games/140576663170542",
         stats="about 6,500 playing, 95% liked of about 74K votes", mins="15 minutes",
         why="The only cleaning game we found that kept its players. It holds about 60% of its peak. Five of the six others from this summer are at 3% or less.",
         look="What there is to do after the first room is clean, the start again step (rebirth), what friends add and the minute it first felt finished.",
         fields=[F_FUN, F_JOB, F_DULL, ("sel", "friends", "Did other players matter?", MATTER_OPTS), F_BACK]),
    dict(id="rt3", name="Restaurant Tycoon 3", url="https://www.roblox.com/games/119048529960596",
         stats="about 5,100 playing, 95% liked of about 429K votes", mins="15 minutes",
         why="The shop game that lasted longest. It still has players after 22 months, with sessions near 26 minutes. It is the closest thing on Roblox to your busy spa idea.",
         look="The queue, what happens when a customer waits, what the staff take over, how rare customers differ, what the game gives you to do at minute 10 and whether customers are made from your friends and how that feels.",
         fields=SHOP_FIELDS),
    dict(id="barber", name="Barber Simulator", url="https://www.roblox.com/games/134026357772960",
         stats="about 5,200 playing, 89% liked of about 25K votes", mins="10 minutes",
         why="A hands-on job game like ours, six weeks old. Its rare customers are pickier, not longer, which is what we suggest in place of 16 step jobs.",
         look="How each step is done by hand, how long one customer takes, how the rare customers differ and when it starts to feel the same.",
         fields=SHOP_FIELDS),
]
OPTIONAL_GAMES = [
    dict(id="petsalon2", name="My Pet Salon!, ten more minutes", url="https://www.roblox.com/games/134135989047078",
         look="Three numbers we still miss: seconds for one normal job, how many jobs before you wanted to stop and how much slower the hired helper is than you."),
    dict(id="ballpit", name="Clean The Ballpit!", url="https://www.roblox.com/games/126221718321318",
         look="The biggest cleaning game right now (about 22,000 playing). Why picking up feels good and what it gives you to do after the first clean."),
    dict(id="washpets", name="Wash the Pets", url="https://www.roblox.com/games/106050444354181",
         look="The feel of the washing and how fast it gets dull."),
    dict(id="cleananimal", name="Clean an Animal!", url="https://www.roblox.com/games/75217712603520",
         look="Why 17% disliked it: bugs, waits or pay walls."),
    dict(id="washacat", name="Wash a Cat", url="https://www.roblox.com/games/87832865714820",
         look="Two minutes is enough. What it is and whether it is any good."),
    dict(id="throwfood", name="Throw Food For Animals", url="https://www.roblox.com/games/120219252362013",
         look="The first minute we want to match: how fast the first animal is yours, the first three prices and how it points to the next goal."),
]
# played in round one; shown as saved, no controls
DONE_GAMES = [
    dict(id="petsalon", name="My Pet Salon!",
         took="You liked the different kinds of step, the praise words with a growing number, the star card with coins and experience after each pet, tool upgrades, the index, rare customers with a lasting reward and hired helpers. You disliked the cutscene with no skip, the same swipe three times, 16 steps in one job, the pet turning by itself and only one customer at a time. First fun thing at about 75 seconds."),
    dict(id="capybara", name="Capybara Onsen",
         took="Not a spa game: step on pads, buy and merge. Useful all the same: a short tutorial with a free first buy, a friend bonus percent on screen from the start and a request for a favourite at about minute 4."),
]

# ---------------------------------------------------------------- to-dos
TODOS = [
    ("Now, about 15 minutes in all", [
        dict(id="automerge", t="Add the rule that makes pull requests wait for their tests",
             d="We checked on November 24 and main has no rule yet. Pull requests have waited for their tests only because each thread waits by hand, so nothing stops a merge with a failed test. To add it: in the Clean-a-Cat repo open Settings, Rules, Rulesets, New ruleset, New branch ruleset. Name it main, set Enforcement status to Active, under Target branches choose Include default branch, tick Require a pull request before merging, tick Require status checks to pass and add these two checks by name: Rojo sourcemap, luau-lsp, Selene, StyLua and Unit tests, strict types, UI gate. Then press Create. About 2 minutes, or say the word and we do it through your Chrome.",
             link=(REPO + "/blob/main/docs/setup-guide.md#9-required-check-and-auto-merge", "Setup guide, step 9")),
        dict(id="apiaccess", t="Turn on saves for Studio in the dev copy",
             d="Open Clean-a-Cat-Dev in Studio, then Game Settings, Security, switch on Enable Studio Access to API Services and save. Without it, saved data and the live switches do not work when we test in Studio."),
        dict(id="loopdoc", t="Read the loop options write-up",
             d="Five minutes. It is the research behind the first nine questions below: why cleaning games fade, what the games that last share and how your busy spa idea fits.",
             link=(LOOPDOC, "Clean a Cat: loop options")),
        dict(id="screens", t="Flip through the 14 draft screens",
             d="Phone and desktop pictures of every screen the game will likely need. The questions below show eight of them. Say in chat if any screen looks wrong.",
             link=(REPO + "/tree/main/docs/concepts/clean-a-cat/ui-2026-11-24", "Screen pictures")),
        dict(id="devices", t="Tell us which phone and tablet you test on",
             d="One line in the project chat, for example the model of your phone and that you have an iPad. We match our test sizes to them."),
    ]),
    ("After today's playtests", [
        dict(id="scrub2", t="Play our scrub on your phone for two minutes",
             d="You said no prototypes until the playtests and the research were done. The research is done, so this is next once your games are played. Two fixes land first: scrubbing over the move stick also walked the player and one drag cleared too much mud. We set the session up for you. Three answers are all we need: did scrubbing feel good, was the reveal a nice surprise and would you wash a second cat.",
             link=(REPO + "/issues/29", "Issue 29")),
    ]),
]
PARKED = [
    ("Server size", "Set once the street and the design are picked."),
    ("Maturity questionnaire", "We write the answers down for you once the gameplay is decided. The game needs a Minimal or Mild result."),
    ("100 plays from engaged players", "Your ads for this come when the game is ready for public testers."),
    ("Build finished notification", "The text and its key are only needed if we keep that idea. Players under 13 cannot get it."),
    ("Store art, second version", "A more detailed icon and thumbnails wait for the design to lock."),
    ("Sound uploads", "One batch after the game is picked."),
    ("Plus or Premium", "Only if Roblox asks for it when we apply for Kids and Select."),
    ("Private repos", "At release."),
]

# ---------------------------------------------------------------- questions
YES = "Yes, go with it"
ELSE = "Something else"
QUESTIONS = [
    ("The game", "Planning-Agent", "These nine decide what we build. Your playtests today test them.", [
        dict(id="loop", t="Your busy spa and a cat collection, together",
             d="Your idea after My Pet Salon becomes the minute to minute play: several cats wait, you pick who is next and helpers take the easy ones. The collection is the reason to keep going: every cat's coat is hidden under the mud, and each new one fills a slot in your Cat Index. Five of the six cleaning games from this summer are at 3% of their peak or less. The one that held on gives players more to chase than the cleaning.",
             opts=["Yes, both together", "Busy spa only", "Collection only, one cat at a time", ELSE],
             note="The loop options write-up in your to-do list has the research behind this."),
        dict(id="queue", t="Cats wait on a bench and you pick who is next",
             d="You called one customer at a time kinda lame. Three or four cats wait, each with a card: name, how dirty, what kind of dirt and what it pays. Picking only matters when the cats differ, so a muddier cat pays more and a fussy one tips more but waits less. Each card also gets one line of our own on how the cat got so dirty, an idea from the story line on the wash screen you sent. You checked on November 24: My Pet Salon lets you press next pet on the table or choose which waiting pet goes next. So picking is not new on Roblox, and we were wrong to say no game has it. What ours adds is a reason to choose: the cats on the bench differ in what they pay, how long they wait and what kind of dirt they have, and the card shows it. We also take the one tap Next cat button for players who do not want to choose.",
             imgs=[("art2/queue-normal.jpg", "Draft screen: a row of waiting cats with a name, rarity, dirt icons, a mood bar, a coin amount and a Wash button each. One card says Helper Suds is washing.", "Draft: who is next")],
             solo=True,
             opts=["Yes, a bench and a pick", "One cat at a time", ELSE]),
        dict(id="impatience", t="Waiting cats get grumpy but are never lost",
             d="You floated customers who get impatient and leave. Lost customers are what parents and reviewers complain about most in shop games. Our pick: a waiting cat's mood drops and only its bonus tip shrinks. A cat that waits far too long goes home and comes back later.",
             opts=["Yes, grumpy and a smaller tip", "They leave and the job is lost", "No waiting pressure at all", ELSE]),
        dict(id="helpers", t="Hired helpers wash common cats, slower than you",
             d="Your idea. Helpers are bought with coins and never with Robux. A helper takes a common cat from the bench, washes it slowly and earns fewer stars. Rare cats and strays always wait for you. The picture still shows kitten helpers. Who the helpers are is the next question.",
             imgs=[("art2/helpers.jpg", "Draft screen: a Helpers window with two helper kittens, their speed bars, what each is washing and a Hire button on an empty spot.", "Draft: helpers")],
             solo=True,
             opts=["Yes, slow helpers for common cats", "Helpers can wash any cat", "No helpers at launch", ELSE]),
        dict(id="helperlook", t="Helpers are human staff, not cats",
             d="You said on November 24 that helpers are likely staff like humans. Our pick agrees. A person in a spa apron reads as staff at a glance, has hands for the sponge and the towel and can reuse the customer figures we already build, so it costs less than a kitten that has to hold tools. One other idea: staff do the washing and Suds the kitten stays as the spa's mascot, who points things out in the first minutes and cheers but never washes. The builder kitten for stations is a separate call. Say in the note if the builder should be a person too. Update: you said ok to staff with Suds as the mascot, and that Suds should not stand. So he walks on four paws like every other cat, which also means he cannot hold a tool. He explains things by trotting to them and sitting beside them with a speech bubble of a few words, and he shows up again each time something new unlocks.",
             opts=["Human staff, no helper cats", "Human staff, and Suds stays as the mascot", "Kitten helpers as drawn", ELSE]),
        dict(id="rare", t="Rare visitors who are pickier, not longer",
             d="You liked the influencer customers and their lasting reward, but 16 steps felt long. Ours bring a rare cat and want a near perfect wash, with the same short job as any cat. A finished visit gives a lasting reward, for example a small permanent tip bonus and a framed photo for your wall. Visitors unlock as your spa earns stars. The chance of each is on a board and none can be bought.",
             opts=["Yes, pickier and not longer", "Longer jobs for rare visitors", "No rare visitors at launch", ELSE]),
        dict(id="keep", t="How cats become yours",
             d="Customers take their cats home, and every coat you reveal fills a slot in your Cat Index. Now and then a stray turns up at the back door. A washed stray stays in your display window and earns tips. The very first cat is Suds, the kitten you rescue in the opening, so every player has a cat of their own inside the first minute. Suds is the same for everyone and is not in the index, as you said on November 24. He has his own card outside the count. He is the mascot, so he does not sit in the window or earn tips. The first customer after him is an easy common cat, which gives the first index stamp, and the first window stray turns up at about minute 4. No catching and no buying cats.",
             imgs=[("art2/reveal-rare.jpg", "Draft screen: a New cat card for a white cat called Marble, marked Rare, 11% of customers, added to your Index.", "Draft: a new coat is revealed")],
             solo=True,
             opts=["Yes, index for all and strays stay", "Index only, no cats live in the spa", ELSE]),
        dict(id="firstminute", t="You rescue a muddy kitten from a box, and he becomes Suds",
             d="Your idea from November 24: a truck drives past, a plain brown box falls off the back and lands in front of you, you open it and find a messy, muddy kitten, and the tutorial is cleaning him up for a score. Once he is clean he becomes Suds. The box is settled: a random brown box, so his name comes from the wash. Still open, and you said you will come back to it: how the scene plays. Your thought is a quick intro you watch, the truck going by and the box falling in front of you, and then you get your camera back and play. We first wrote it as a scene you play with the camera yours the whole time. Your version has one clear plus, which is that nobody can be looking the wrong way and miss the box, so it is now our pick too with one limit: about 4 seconds and no more, because you disliked the cutscene with no skip in My Pet Salon. Either way you tap the box at about second 4 and scrub at about second 12, which is about 9 seconds later than spawning at the tub. So we would run it against the tub start behind a switch and keep the one that holds more new players. His wash always ends on three stars, so nobody fails the opening.",
             imgs=[("art2/tutorial-trail.jpg", "Draft screen: green arrows on the ground lead to the spa door, a yellow arrow bobs over the goal and the top line reads Step 1 of 3: Follow the arrows.", "Draft: the trail that leads from the box to the tub")],
             solo=True,
             opts=["A quick intro you watch, about 4 seconds, then play", "A scene you play, the camera is always yours", "No scene, spawn at the tub and scrub", ELSE]),
        dict(id="session", t="Aim for a first session of 20 minutes or more",
             d="In one report on Roblox games, about 11 in 100 new players came back the next day when sessions ran over 25 minutes and about 4 in 100 when they ran under 3. That is a link, not proof. It means more on day one than we first planned: about 12 cats, 3 kinds of dirt and 4 tools. Your screenshot of My Pet Salon's album shows 59 pets in six rarities. Twelve coats would look thin beside that, and a coat costs us far less than a new animal because every cat shares one body. So we would go to about 24 coats on day one if Model-Agent confirms the cost.",
             opts=["Yes, build more for day one", "Keep the first build small and add later", ELSE]),
    ]),
    ("The wash", "Planning-Agent and Design-Agent", "", [
        dict(id="steps", t="Four kinds of step at the start",
             d="You liked the variety in My Pet Salon. Ours at launch: scrub the mud, rinse with the shower, pick burrs out of the fur and towel dry. Later tools add nail trim, comb, shampoo and the dryer. The models for all of these are drafted.",
             imgs=[("art2/wash-scrub.jpg", "Draft screen: a muddy cat in a tub, the line Step 1 of 4 Scrub the mud, four tool buttons at the bottom, a progress bar, the praise word Awesome with x12 and a round turn button on each side.", "Draft: the wash")],
             solo=True,
             opts=["Yes, these four first", "Fewer: scrub, rinse and dry", "All of them from the start", ELSE]),
        dict(id="joblength", t="Four to six short steps per cat, never the same step twice in a row",
             d="You found the same swipe three times boring and 16 steps too long. Each step lasts 8 to 15 seconds, so a cat takes about a minute. A Step 2 of 4 line shows how far along you are.",
             opts=["Yes, 4 to 6 short steps", "Shorter, 3 steps", "Longer jobs are fine", ELSE]),
        dict(id="turn", t="The cat holds still while you scrub",
             d="You said the pet turning the whole time made you miss spots. Ours stays put during a step. The game turns it between steps, and two round arrow buttons let you turn it when you want.",
             opts=["Yes, still while scrubbing", "Slow turning all the time", ELSE]),
        dict(id="praise", t="Praise words and a combo that pauses on a slip",
             d="You noticed Awesome and Excellent with a growing number. Ours: short words that name what you did, one at a time and never under your finger, beside a combo count. A slip pauses the combo and does not reset it to zero, which feels unfair to young players.",
             opts=["Yes, pause on a slip", "Reset the combo on a slip", "No combo", ELSE]),
        dict(id="tools", t="Tool upgrades change how the tool feels",
             d="You liked upgrading tools. Each tier changes the shape and what the tool does as well as the speed: a wider sponge, a shower with a fan spray, a comb that shows hidden burrs. Tier 2 is lilac and tier 3 is gold.",
             opts=["Yes, each tier feels different", "Speed only, simpler to build", ELSE]),
    ]),
    ("Coming back", "Planning-Agent", "", [
        dict(id="longbuild", t="The first long build comes after about minute 15, not minute 6",
             d="The old plan offered an 8 hour VIP Room at minute 6. In the hit games waits start at seconds and reach hours only once the player cares. The rest stays: the builder kitten builds one station at a time, a building site one room at a time, nothing takes over 24 hours and a finished build waits for you.",
             imgs=[("art2/builder-busy.jpg", "Draft screen: a Builder window with a station building for 4 more minutes and a VIP Room building for 7 more hours with a Notify me bell.", "Draft: the builder")],
             solo=True,
             opts=["Yes, long builds later", "Keep it at minute 6", "No builds over 1 hour at launch", ELSE]),
        dict(id="skips", t="No paid skips on timers",
             d="We sell a Second Builder pass instead. Paid skips read as pressure for a young audience and are what reviewers of spa games complain about most.",
             opts=["Yes, no paid skips", "Sell skips at launch", ELSE]),
        dict(id="return", t="Three reasons to come back tomorrow, and no streak",
             d="Players under 13 cannot get our notifications, so a bell cannot be the main hook. Ours: a tip jar that fills while you are away and stops at a cap, the empty slots in your index and one different visitor cat each day. There is no streak to lose. Suds meets you at the door and points at the full tip jar and today's visitor. He is always glad to see you and never sad that you were away. The bell stays as a small extra for players of 13 and over.",
             opts=["Yes, these three", "Add a daily streak reward", ELSE]),
        dict(id="reopen", t="A Grand Reopening for players who finish the spa",
             d="The games that last have a start again step, and so does Clean Everything. Ours: move to a bigger spa, keep every cat and gain a permanent tip bonus. It is not needed for the first test, but the saved data has to allow for it from the start.",
             opts=["Yes, plan it now and build it after the first test", "Build it for launch", "No start again step", ELSE]),
        dict(id="friends", t="A small bonus for each friend in your server",
             d="You saw the friend percent on screen in Capybara Onsen. Ours: 10% more tips per friend in the server, shown from the start. Helping inside a friend's spa comes later.",
             opts=["Yes, a friend bonus", "No friend bonus", ELSE]),
        dict(id="friendcust", t="Friends as customers: open until you have seen Restaurant Tycoon 3",
             d="You noticed that My Pet Salon makes its customers from your friend list, and said you are not sure it is good and will look at how Restaurant Tycoon 3 does it. So this stays open and nothing is built. What we know so far. For it: a friend's name in the first minute catches the eye and makes a quiet street feel social. Against: a full friend avatar costs memory on phones and does not match our art style, and on a shared street it would show your friends to strangers. Roblox has no rule against it that we could find, but creators reported in September that the friend list came back empty for a few days, so written names must always be the fallback. If you want it, our pick is the light version: a friend's name and face picture on the cat's card, on your own screen only, with our own customer figure in the spa.",
             opts=["Light version: a friend's name and face on the card", "Friends walk in as full avatars", "No friends as customers", ELSE]),
        dict(id="visit", t="Neighbours look through the window but do not walk in",
             d="Players see each other's windows and reveals from the street. Walking in is built behind a switch that stays off, so friends helping in your spa can be turned on later without a rebuild. It stops a crowd standing on someone's tub.",
             opts=["Yes, window only for now", "Walk in from the start", ELSE]),
        dict(id="trading", t="No trading of cats",
             d="Trading is the one feature with a clear record of harm to young players, mostly scams. Cats are earned by washing only.",
             opts=["Yes, no trading", "Plan trading for later", ELSE]),
        dict(id="favourite", t="No like or favourite ask in the first session",
             d="Capybara Onsen asked you for a favourite at about minute 4. Roblox judges a game on its first minutes, and an ask there is one more thing between a new player and the fun. Our pick: nothing in the first session, then one small ask after a great wash on a later visit. It never comes with a reward, because Roblox does not allow rewards for likes or favourites. Your screenshot shows My Pet Salon paying cash for both in its Rewards window. By our reading of the rules that is their risk and we do not copy it.",
             opts=["Yes, one ask on a later visit", "Ask once at about minute 5", "Never ask", ELSE]),
    ]),
    ("Screens", "Design-Agent", "", [
        dict(id="recap", t="After each cat: the full card or a slim strip",
             d="You called the star card with a coins and experience breakdown kinda cool. With a line of cats waiting, a full window after every wash slows you down. Our pick: the full card for your first cats and for any new or rare cat, and the slim strip for the rest. Two things from your My Pet Salon screenshots go into ours. Their card sits at the side so the clean pet stays in view, with one line for each reason you earned. And Roblox's own badge note covered their Collect button, so our button stays out of that corner.",
             imgs=[("art2/recap-full.jpg", "Draft screen: a Great job window with the cat's picture, three stars, three rows of coins earned, a total and a Next cat button.", "Full card"),
                   ("art2/recap-compact.jpg", "Draft screen: a slim strip at the bottom with the cat's face, three stars, the coins earned and a Next cat button, the tub still in view.", "Slim strip")],
             wide=True,
             opts=["Full card for new cats, slim strip for the rest", "Full card after every cat", "Slim strip after every cat", ELSE]),
        dict(id="hud", t="Menu buttons appear one at a time",
             d="The draft has four round buttons on the left: Index, Tools, Helpers and Build. Our pick: a new player sees none, and each pops in with a short pointer the first time it is useful. Index after the first cat, Tools at the first upgrade, Build and Helpers later. That keeps the first minutes about the cat. Suds does the pointing: he trots to the new thing and sits by it. He shows each thing once, never opens a window himself and never points at anything that costs Robux. For comparison, your screenshot shows My Pet Salon with all four of its buttons on screen from the first second.",
             imgs=[("art2/hud.jpg", "Draft screen: the main view with four round buttons at the left, a goal line at the top, coins at the top right and two waiting cats at the right.", "Draft: the main screen with all four buttons")],
             solo=True,
             opts=["Yes, one at a time", "All four from the start", ELSE]),
        dict(id="sudsbubble", t="Suds explains in a help bubble at the bottom of the screen",
             d="You sent My Pet Salon's help bubbles as an idea: a guide at the left, a bold line, a short sentence and one big button that does the step. Our pick is the same idea in our own look. Suds's face is at the left, the bubble holds one short title and one sentence that says why, and one button does the step, so you still do every tap. It shows one at a time for tutorial steps and new unlocks, and goes away after the tap. Theirs runs under the jump button, so ours stops short of the stick and the jump button on every phone. A Tips switch in Settings turns the bubbles off once the tutorial is done.",
             opts=["Yes, a bottom bubble with one button", "Only a small bubble over Suds in the spa", ELSE]),
        dict(id="camera", t="A close camera at the tub with the move stick hidden",
             d="While you wash, the camera moves in on the cat and the move stick hides, so the whole screen is for scrubbing. Our own test found that scrubbing over the stick also walked the player away, and this fixes it.",
             opts=[YES, "Keep the normal camera", ELSE]),
        dict(id="landscape", t="Lock phones to landscape",
             d="One layout to get right, with more room for the tub and the tools.",
             opts=[YES, "Allow portrait too", ELSE]),
        dict(id="bows", t="A bow as the finishing touch",
             d="The first plan had you pick a bow on every cat. With a line waiting that is one tap too many. Our pick: bows for cats that stay with you and for rare visitors.",
             opts=["Bows for your own cats and rare visitors", "A bow on every cat", "No bows", ELSE]),
    ]),
    ("The look", "Model-Agent", "", [
        dict(id="mud", t="Mud as a coat that wraps the cat",
             d="Your words on the three tries: random blobs, dirt blocks, then not smeared but built into the fur or coated in it. This version wraps the cat's own shapes, with drips under the jaw and belly. You have not said yet whether it works.",
             imgs=[("art2/mud-coat.jpg", "Three blocky cats, orange, grey and black, each with patches of mud wrapped around the head, body and paws.", "The mud coat on three cats")],
             solo=True,
             opts=["Yes, the coat works", "Closer, keep going", ELSE]),
        dict(id="mudphone", t="Stink wisps so a dirty cat reads on a small phone",
             d="At phone size, mud on a pale cat can look like a patterned coat. Our pick: wavy stink lines rise off a dirty cat and stop when it is clean, so dirty reads at any size.",
             opts=["Yes, stink wisps", "Darker mud instead", "Both", ELSE]),
        dict(id="baths", t="Baths with deep blue water, white lather and clear bubbles",
             d="You said the pale water looked like the water was missing. The water is now deep blue to just under the rim. A nicer tub shape is being drawn now.",
             imgs=[("art2/baths.jpg", "Two baths, a mint one and a pink round one, each with a cat in deep blue water with white lather and clear bubbles.", "The baths now")],
             solo=True,
             opts=["Yes, this water", "Still not right", ELSE]),
        dict(id="style", t="Art style",
             d="Bubble Pastel colours (cream, mint, bubblegum, sky and dark mud) on the blocky cat body from your asset library. It reads on phones, needs no mesh uploads and makes the mud stand out. Every picture on this page is in it.",
             opts=["Yes, Bubble Pastel", "Cozy Storybook (warm wood, painted textures)", "Bright Toy (saturated, glossy)", ELSE]),
        dict(id="body", t="Reuse the Cat Cafe cat body with all new coats",
             d="Same body shape, new coats and names, plus spa extras such as mud, fluff and bows. No Cat Cafe character is reused.",
             opts=[YES, "Make the cats look clearly different from Cat Cafe", ELSE]),
        dict(id="names", t="Working cat names",
             d="Muffin, Smudge (the first window stray), Inky, Cotton, Tux, Patches, Toffee, Marble, Lilac Cloud and Starcoat. Suds is the mascot kitten and the first cat every player washes. He has no name until he is clean. None is used in Cat Cafe.",
             opts=["Yes, use these", "I want to name them", ELSE]),
    ]),
    ("Sound and feel", "Motion-FX-Agent", "", [
        dict(id="feel", t="The feel of the cleaning",
             d="Soft and cosy means pastel bubbles, gentle sounds and small sparkles. Splashy and cartoony means big suds and bouncy pops.",
             opts=["Soft and cosy", "Splashy and cartoony", ELSE]),
        dict(id="upload", t="Upload the sounds once the game is picked",
             d="You listened and said they are fine for now. Uploading uses some of the group's monthly audio quota, so it needs your OK. Our pick: wait, then send them as one batch.",
             opts=["Yes, one batch after the game is picked", "Upload now", ELSE]),
    ]),
    ("Store page", "Model-Agent and Growth-Agent", "", [
        dict(id="icon", t="The store icon",
             d="You asked for the bath from your Cat Cafe ad, blown up, with no mud. This is the result, close on the cat's face. Nothing is uploaded until you say so, and a more detailed version waits for the design.",
             imgs=[("art2/icon-final.jpg", "Store icon: an orange cat sitting in a bubble bath with a rubber duck, towels behind it, on teal.", "The icon")],
             icon=True,
             opts=["Yes, use it for the first test", "Change it", ELSE]),
        dict(id="thumb", t="The store thumbnail",
             d="The wide picture on the game's page: the chunky title on a teal bubble backdrop beside the claw-foot bath.",
             imgs=[("art2/thumb-final.jpg", "Store thumbnail: the words CLEAN A CAT beside an orange cat in a claw-foot bath with a shower, towels and bubbles, on teal.", "The thumbnail")],
             solo=True,
             opts=["Yes, use it for the first test", "Change it", ELSE]),
        dict(id="split", t="Add a half dirty, half clean picture",
             d="You liked My Pet Salon's side by side picture with a thin line down the middle. Roblox can rotate thumbnails and show which one wins the most taps. Our pick: make one as the second thumbnail once the mud look is settled.",
             opts=["Yes, as the second thumbnail", "Make it the main one", "No", ELSE]),
        dict(id="catspa", t="Put the words cat spa in the description",
             d="Your cat spa ad did well. The title stays Clean a Cat and the icon stays free of words.",
             opts=[YES, "No cat spa wording", ELSE]),
        dict(id="newtag", t="No [NEW] in front of the game name at launch",
             d="You asked us to look into whether putting new in brackets before the name helps. Growth-Agent read six pages on it. Nobody has measured it: we found no test with numbers, only opinions. Roblox has no rule against it, but says titles must describe the game and that tags are not used in its ranking. Search weighs the front of a title most, so a bracket there pushes the real words back, and the tag goes stale within weeks. What makes people tap on Home is mostly the icon and the thumbnails. Our pick: launch as plain Clean a Cat and put the word new in the description's update line and on event cards. If you want to know for sure, the second option tries the tag after launch for one clean week and compares it with the week before. A title cannot be split between players, so that is a before and after read and one weak reason at best.",
             opts=["Plain Clean a Cat, new goes in the description", "Try the tag after launch for one week", "[NEW] in the name from day one", ELSE]),
    ]),
    ("Money and events", "Planning-Agent and Growth-Agent", "", [
        dict(id="passes", t="Three game passes, and coins, helpers and rare cats are never sold",
             d="2x Coins, Second Builder and Golden Sponge, a wider scrub with gold bubbles. Coins cannot be bought, so the random customer never counts as a paid random item. Nothing sold changes the chances, and the chance of every cat is always on a board. Your screenshots show how hard My Pet Salon sells: a starter pack on the main screen from the first minute, a limited pack with an Only 82 left counter, cash for Robux and a paid upgrade that maxes every worker. We stay with no offer on screen in the first session, no stock counters and no coins for Robux. Say in the note if you want a starter pack later. Ours would hold looks and not coins.",
             opts=[YES, ELSE]),
        dict(id="event", t="A Cat Show weekend as your first event",
             d="Day 7 is yours. A themed show with voting is the natural first event. It is not part of the first build.",
             opts=["Yes, plan it for later", "I have a different event in mind", ELSE]),
    ]),
]
SAVED = [
    ("Your idea after My Pet Salon", "You wash by hand, hired helpers take customers too but much slower, more customers show up so you pick who is next, and maybe customers who wait too long leave. Saved as a direction, not a decision."),
    ("Mud", "Random blobs, then dirt blocks, then: not smeared, built into the fur or coated in it."),
    ("Baths", "Pale water under white foam looked like the water was missing."),
    ("Store art", "A chunky title on teal bubbles, no mud and the bath from your Cat Cafe ad blown up. You liked a half dirty, half clean picture."),
    ("Setup you finished", "Group id, experience ids, the dev copy, both keys, the PC, the sound listen and the age check. The first publish ran on November 23 at 10:14 PM ET."),
    ("The first 25 questions", "You left them all parked. The questions on this page replace them."),
]
DECIDED = [
    ("Name", "Clean a Cat, locked November 23."),
    ("Direction", "A hands-on cat spa. No catching."),
    ("Goals", "A fun first 5 minutes and a reason to come back on day 2. You handle day 7 with events."),
    ("How we work", "Passing pull requests merge themselves. Publishing is silent. Restarts are fine until public release."),
]

def e(s):
    return html.escape(s, quote=True)

# ================================================================= HTML
def field(d, f):
    if f[0] == "sel":
        _, k, label, opts = f
        o = '<option value="">Choose</option>' + "".join(f'<option value="{i}">{e(x)}</option>' for i, x in enumerate(opts))
        return f'<label class="field"><span>{e(label)}</span><select id="{d}__{k}" data-doc="{d}" data-key="{k}">{o}</select></label>'
    _, k, label, ph = f
    return f'<label class="field"><span>{e(label)}</span><input type="text" id="{d}__{k}" data-doc="{d}" data-key="{k}" placeholder="{e(ph)}"></label>'

def game_card(g, n):
    d = "p-" + g["id"]
    return f'''
<article class="game" id="game-{g["id"]}">
  <header>
    <span class="num">{n}</span>
    <div class="gh">
      <h3><a href="{g["url"]}" target="_blank" rel="noopener">{e(g["name"])}</a></h3>
      <p class="stats">{e(g["mins"])} · {e(g["stats"])}</p>
    </div>
    <label class="played"><input type="checkbox" id="{d}__played" data-doc="{d}" data-key="played"><span>Played</span></label>
  </header>
  <p><strong>Why it is on the list.</strong> {e(g["why"])}</p>
  <p><strong>Look for.</strong> {e(g["look"])}</p>
  <div class="fields">{"".join(field(d, f) for f in g["fields"])}</div>
  <label class="field wide"><span>Your notes</span><textarea id="{d}__notes" data-doc="{d}" data-key="notes" rows="4" placeholder="What it does well, what we should do better, what made you want to stop"></textarea></label>
</article>'''

def opt_game(g):
    d = "p-" + g["id"]
    return f'''
<li class="optgame">
  <label class="played"><input type="checkbox" id="{d}__played" data-doc="{d}" data-key="played"><span class="sr">Played</span></label>
  <div>
    <a href="{g["url"]}" target="_blank" rel="noopener">{e(g["name"])}</a>
    <p>{e(g["look"])}</p>
    <input type="text" id="{d}__notes" data-doc="{d}" data-key="notes" placeholder="A line of notes" aria-label="Notes on {e(g["name"])}">
  </div>
</li>'''

def todo_item(t):
    d = "c-" + t["id"]
    link = f' <a href="{t["link"][0]}" target="_blank" rel="noopener">{e(t["link"][1])}</a>' if t.get("link") else ""
    return f'''
<li class="todo">
  <input type="checkbox" id="{d}__done" data-doc="{d}" data-key="done">
  <label for="{d}__done"><strong>{e(t["t"])}</strong><span>{e(t["d"])}{link}</span></label>
</li>'''

def question(q, n):
    d = "q2-" + q["id"]
    opts = ""
    for i, o in enumerate(q["opts"]):
        rec = '<em>Our pick</em>' if i == 0 else ""
        opts += f'<label class="opt"><input type="radio" name="{d}" id="{d}__pick{i}" value="{i}" data-doc="{d}" data-key="pick"><span>{e(o)}{rec}</span></label>'
    note = f'<p class="qnote">{e(q["note"])}</p>' if q.get("note") else ""
    if q.get("imgs"):
        figs = "".join(f'<figure><img src="{src}" alt="{e(alt)}" loading="lazy"><figcaption>{e(cap)}</figcaption></figure>' for src, alt, cap in q["imgs"])
        cls = "art wide" if q.get("wide") else "art solo" if q.get("solo") else "art icon" if q.get("icon") else "art"
        note += f'<div class="{cls}">{figs}</div>'
    return f'''
<article class="q" id="{d}">
  <h3><span class="qn">{n}</span>{e(q["t"])}</h3>
  <p>{e(q["d"])}</p>{note}
  <div class="opts" role="radiogroup" aria-label="{e(q["t"])}">{opts}</div>
  <input type="text" class="qtext" id="{d}__note" data-doc="{d}" data-key="note" placeholder="Anything to add (optional)" aria-label="Note on: {e(q["t"])}">
</article>'''

games_html = "".join(game_card(g, i + 1) for i, g in enumerate(GAMES))
opt_html = "".join(opt_game(g) for g in OPTIONAL_GAMES)
done_html = "".join(f'<li><strong>{e(g["name"])}</strong><span>{e(g["took"])}</span></li>' for g in DONE_GAMES)
prompts_html = "".join(f"<li>{e(p)}</li>" for p in NOTE_PROMPTS)
extra_html = "".join(f"<li><strong>{e(a)}.</strong> {e(b)}</li>" for a, b in EXTRA_PROMPTS)
todos_html = ""
for title, items in TODOS:
    todos_html += f'<h3 class="group">{e(title)}</h3><ul class="todos">{"".join(todo_item(t) for t in items)}</ul>'
parked_html = "".join(f"<li><strong>{e(a)}.</strong> {e(b)}</li>" for a, b in PARKED)
q_html, n = "", 0
for title, who, lead, items in QUESTIONS:
    block = ""
    for q in items:
        n += 1
        block += question(q, n)
    leadp = f'<p class="grouplead">{e(lead)}</p>' if lead else ""
    q_html += f'<h3 class="group">{e(title)} <small>from {e(who)}</small></h3>{leadp}{block}'
NQ = n
NT = sum(len(i) for _, i in TODOS)
NG = len(GAMES)
saved_html = "".join(f"<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>" for a, b in SAVED + DECIDED)

OLD_FIELDS = [("sel", "pet", "pet", PET_OPTS), ("txt", "fun", "first fun at (s)", ""), ("sel", "wash", "washing", WASH_OPTS), ("sel", "wait", "waits", WAIT_OPTS)]
def jf(fields):
    return [dict(k=f[1], label=f[2], opts=(f[3] if f[0] == "sel" else None)) for f in fields]
DATA = dict(
    main=[dict(id="p-" + g["id"], name=g["name"], fields=jf(g["fields"])) for g in GAMES],
    other=[dict(id="p-" + g["id"], name=g["name"], fields=[]) for g in OPTIONAL_GAMES]
          + [dict(id="p-" + g["id"], name=g["name"] + " (round one)", fields=jf(OLD_FIELDS)) for g in DONE_GAMES],
    todos=[dict(id="c-" + t["id"], t=t["t"]) for _, items in TODOS for t in items],
    qs=[dict(id="q2-" + q["id"], t=q["t"], opts=q["opts"]) for _, _, _, items in QUESTIONS for q in items],
)

EXTRA_CSS = r'''
.art.solo{grid-template-columns:minmax(0,560px)}
.art.icon{grid-template-columns:minmax(0,200px)}
.grouplead{color:var(--soft);font-size:.95rem;margin-top:-6px}
.saved{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:10px}
.saved li{background:var(--mint-bg);border-radius:12px;padding:12px 14px;display:flex;flex-direction:column;gap:2px}
.saved li strong{font-family:var(--display);font-weight:600}
.saved li span{font-size:.92rem}
.parked{margin:0;padding-left:20px;display:flex;flex-direction:column;gap:4px;font-size:.92rem;color:var(--soft)}
.parked strong{color:var(--ink)}
details.more{border:1px solid var(--line);border-radius:12px;padding:10px 14px;background:var(--surface)}
details.more summary{cursor:pointer;font-weight:700}
details.more[open] summary{margin-bottom:10px}
.gapnote{background:var(--gum-bg);border-radius:12px;padding:12px 14px;font-size:.94rem}
'''

PAGE = r'''<title>Clean a Cat Launch Plan</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600&family=Nunito+Sans:opsz,wght@6..12,400;6..12,600;6..12,700&display=swap">
<style>__CSS__</style>

<div class="wrap">
  <div class="intro">
    <p class="eyebrow">Clean a Cat, round two, November 24</p>
    <h1>What is left before we build</h1>
    <p class="lede">Round one is saved: your two playtests, your notes on the mud, the baths and the store art and every setup job you finished. This page holds only what is still open. The questions are new, rewritten from what you told us, so nothing from the parked first set carries over.</p>
    <ol class="steps">
      <li><a href="#playtests">Play __NG__ more games</a> that test your busy spa idea.</li>
      <li><a href="#todo">Do __NT__ short jobs</a>. Most take a minute or two.</li>
      <li><a href="#questions">Tap through __NQ__ picks</a>. The first nine decide the game.</li>
    </ol>
  </div>

  <nav class="bar" aria-label="Progress">
    <a class="pill" href="#playtests" id="pill-play">Playtests <b><span id="n-play">0</span> of __NG__</b></a>
    <a class="pill" href="#todo" id="pill-todo">To do <b><span id="n-todo">0</span> of __NT__</b></a>
    <a class="pill" href="#questions" id="pill-q">Picks <b><span id="n-q">0</span> of __NQ__</b></a>
    <span class="status" id="status" role="status">Loading your answers</span>
  </nav>

  <section id="playtests">
    <header>
      <h2>Play these __NG__ next</h2>
      <p>As a brand new player, on a phone if you can, with a timer running. The first list asked how games hand you a pet. This one asks what keeps players past the first ten minutes and how a busy shop feels, because that is what your idea and the research now turn on. Player counts are from the morning of November 24, 2026 and move all day.</p>
    </header>
    <div class="notes">
      <h3>What to write down for each game</h3>
      <ol>__PROMPTS__</ol>
      <h3>The team also asked for</h3>
      <ul>__EXTRA__</ul>
    </div>
    __GAMES__
    <h3 class="group">If there is time</h3>
    <ul class="optlist">__OPT__</ul>
    <p class="fine">Also worth five minutes each: Wash the Car (washing by hand) and Steal An Egg (the arrows and the menu that shows what grows while you are away).</p>
    <h3 class="group">Played and saved</h3>
    <ul class="saved">__DONE__</ul>
  </section>

  <section id="todo">
    <header>
      <h2>Your to-do list</h2>
      <p>Only open jobs are listed. Everything you finished in round one is off the list and saved.</p>
    </header>
    __TODOS__
    <details class="more">
      <summary>Parked until the game is picked (nothing to do yet)</summary>
      <ul class="parked">__PARKED__</ul>
    </details>
  </section>

  <section id="questions">
    <header>
      <h2>Tap through our picks</h2>
      <p>The first option is always our pick. Tap it to agree or choose another. Where a question came from something you said, it says so. Nothing locks until you say done.</p>
    </header>
    <div class="row"><button type="button" class="ghost" id="acceptall">Take our pick for everything I have not answered</button></div>
    __QUESTIONS__
    <p class="gapnote"><strong>What nobody can tell us.</strong> No source gives a proven number for any hook, for how long a wait can be or for the right job length. We find out after launch by running two versions behind switches and reading Roblox's own numbers.</p>
  </section>

  <section id="decided">
    <header><h2>Saved from round one</h2><p>For reference. Nothing to do here. The team has all of this in its notes.</p></header>
    <dl class="decided">__SAVED__</dl>
  </section>

  <section id="send">
    <div class="send">
      <h2>When you are done</h2>
      <p>Your answers save on this page as you go and the team reads them from here. Say done in the project chat and we lock the design, finish the first milestone plan and start building. If saving shows a problem above, copy your answers and paste them in the chat.</p>
      <div class="row"><button type="button" id="copy">Copy my answers</button><span class="fine" id="copied" role="status"></span></div>
      <textarea id="copyout" rows="8" hidden readonly aria-label="Your answers as text"></textarea>
    </div>
  </section>
</div>

<script>
(function(){
  var DATA = __DATA__;
  var LS = "clean-a-cat-plan-v2";
  var state = {};      // docId -> {key: value}
  var dirty = {};      // docId -> true while a local change is unsaved
  var timers = {}, writing = {}, again = {};
  var db = null, online = false;
  var statusEl = document.getElementById("status");

  function setStatus(t, warn){ statusEl.textContent = t; statusEl.classList.toggle("warn", !!warn); }
  function controls(doc){ return document.querySelectorAll('[data-doc="' + doc + '"]'); }
  function has(v){ return v !== undefined && v !== null && v !== ""; }

  function readControl(el){
    if (el.type === "checkbox") return el.checked;
    if (el.type === "radio") return el.checked ? el.value : undefined;
    return el.value;
  }
  function applyDoc(doc){
    var d = state[doc] || {};
    controls(doc).forEach(function(el){
      var k = el.dataset.key, v = d[k];
      if (el === document.activeElement && dirty[doc]) return;
      if (el.type === "checkbox") el.checked = v === true;
      else if (el.type === "radio") el.checked = (has(v) && String(v) === el.value);
      else el.value = v == null ? "" : String(v);
    });
    markOther(doc);
  }
  function markOther(doc){
    if (doc.indexOf("q2-") !== 0) return;
    var art = document.getElementById(doc); if (!art) return;
    var q = DATA.qs.filter(function(x){ return x.id === doc; })[0];
    var p = (state[doc] || {}).pick;
    art.classList.toggle("other", !!q && has(p) && Number(p) === q.opts.length - 1 && q.opts[q.opts.length - 1] === "Something else");
  }
  function counts(){
    var play = 0, todo = 0, q = 0;
    DATA.main.forEach(function(g){ if ((state[g.id] || {}).played === true) play++; });
    DATA.todos.forEach(function(t){ if ((state[t.id] || {}).done === true) todo++; });
    DATA.qs.forEach(function(x){ if (has((state[x.id] || {}).pick)) q++; });
    document.getElementById("n-play").textContent = play;
    document.getElementById("n-todo").textContent = todo;
    document.getElementById("n-q").textContent = q;
    document.getElementById("pill-play").classList.toggle("full", play === DATA.main.length);
    document.getElementById("pill-todo").classList.toggle("full", todo === DATA.todos.length);
    document.getElementById("pill-q").classList.toggle("full", q === DATA.qs.length);
  }
  function saveLocal(){ try { localStorage.setItem(LS, JSON.stringify(state)); } catch (e) {} }
  function loadLocal(){ try { var s = JSON.parse(localStorage.getItem(LS) || "{}"); if (s && typeof s === "object") state = s; } catch (e) {} }

  function flush(doc){
    if (!db) { dirty[doc] = false; return; }
    if (writing[doc]) { again[doc] = true; return; }
    writing[doc] = true;
    setStatus("Saving");
    var body = Object.assign({}, state[doc] || {}, { at: new Date().toISOString() });
    db.doc("answers/" + doc).set(body).then(function(){
      writing[doc] = false;
      if (again[doc]) { again[doc] = false; flush(doc); return; }
      dirty[doc] = false;
      setStatus("All answers saved");
    }, function(){
      writing[doc] = false; again[doc] = false;
      setStatus("Could not save online. Use Copy my answers below.", true);
    });
  }
  function changed(doc, delay){
    dirty[doc] = true; saveLocal(); counts(); markOther(doc);
    clearTimeout(timers[doc]);
    timers[doc] = setTimeout(function(){ flush(doc); }, delay);
  }
  function onInput(ev){
    var el = ev.target; if (!el.dataset || !el.dataset.doc) return;
    var doc = el.dataset.doc, k = el.dataset.key, v = readControl(el);
    if (v === undefined) return;
    state[doc] = Object.assign({}, state[doc] || {});
    state[doc][k] = v;
    changed(doc, (el.type === "text" || el.tagName === "TEXTAREA") ? 900 : 150);
  }
  document.addEventListener("input", onInput);
  document.addEventListener("change", onInput);

  document.getElementById("acceptall").addEventListener("click", function(){
    DATA.qs.forEach(function(x){
      if (!has((state[x.id] || {}).pick)) {
        state[x.id] = Object.assign({}, state[x.id] || {}, { pick: "0" });
        applyDoc(x.id); changed(x.id, 150);
      }
    });
  });

  function summary(){
    var L = ["Clean a Cat: my answers, round two", "", "PLAYTESTS"];
    DATA.main.concat(DATA.other).forEach(function(g){
      var d = state[g.id] || {}, bits = [];
      g.fields.forEach(function(f){
        var v = d[f.k]; if (!has(v)) return;
        bits.push(f.label + ": " + (f.opts ? f.opts[Number(v)] : v));
      });
      if (!d.played && !d.notes && !bits.length) return;
      L.push("- " + g.name + (d.played ? " (played)" : "") + (bits.length ? ". " + bits.join("; ") : ""));
      if (d.notes) L.push("  Notes: " + d.notes);
    });
    L.push("", "TO DO, DONE");
    DATA.todos.forEach(function(t){ if ((state[t.id] || {}).done === true) L.push("- " + t.t); });
    L.push("", "PICKS");
    DATA.qs.forEach(function(x, i){
      var d = state[x.id] || {};
      L.push((i + 1) + ". " + x.t + ": " + (has(d.pick) ? x.opts[Number(d.pick)] : "not answered") + (d.note ? " (" + d.note + ")" : ""));
    });
    return L.join("\n");
  }
  document.getElementById("copy").addEventListener("click", function(){
    var text = summary(), out = document.getElementById("copyout"), msg = document.getElementById("copied");
    function fallback(){ out.hidden = false; out.value = text; out.focus(); out.select(); msg.textContent = "Select all and copy the text below."; }
    try {
      navigator.clipboard.writeText(text).then(function(){ msg.textContent = "Copied. Paste it in the project chat."; }, fallback);
    } catch (e) { fallback(); }
  });

  function renderAll(){
    var ids = {};
    document.querySelectorAll("[data-doc]").forEach(function(el){ ids[el.dataset.doc] = 1; });
    Object.keys(ids).forEach(applyDoc);
    counts();
  }

  loadLocal(); renderAll();

  var gave = setTimeout(function(){ if (!online) setStatus("Answers are kept in this browser for now. Use Copy my answers to send them.", true); }, 10000);
  var use = window.claude && window.claude.use ? window.claude.use("db") : Promise.resolve(null);
  use.then(function(d){
    if (!d) { clearTimeout(gave); setStatus("Answers are kept in this browser. Use Copy my answers to send them.", true); return; }
    db = d;
    db.collection("answers").onSnapshot(function(snap){
      snap.docs.forEach(function(doc){
        if (dirty[doc.id] || writing[doc.id]) return;
        var body = Object.assign({}, doc.data() || {}); delete body.at;
        state[doc.id] = body; applyDoc(doc.id);
      });
      counts(); saveLocal();
      if (!snap.metadata.fromCache) {
        clearTimeout(gave);
        if (!online) {
          online = true;
          Object.keys(dirty).forEach(function(k){ if (dirty[k]) flush(k); });
        }
        var busy = Object.keys(writing).some(function(k){ return writing[k]; });
        if (!busy) setStatus("All answers saved");
      }
    }, function(){
      clearTimeout(gave);
      setStatus("Could not reach your saved answers. Use Copy my answers below.", true);
    });
  }, function(){ clearTimeout(gave); setStatus("Answers are kept in this browser. Use Copy my answers to send them.", true); });
})();
</script>
'''
page = (PAGE.replace("__CSS__", CSS + EXTRA_CSS).replace("__PROMPTS__", prompts_html).replace("__EXTRA__", extra_html)
        .replace("__GAMES__", games_html).replace("__OPT__", opt_html).replace("__DONE__", done_html)
        .replace("__TODOS__", todos_html).replace("__PARKED__", parked_html).replace("__QUESTIONS__", q_html)
        .replace("__SAVED__", saved_html).replace("__NQ__", str(NQ)).replace("__NT__", str(NT)).replace("__NG__", str(NG))
        .replace("__DATA__", json.dumps(DATA)))
open(OUT_HTML, "w", encoding="utf-8").write(page)

# ================================================================= Markdown copy
M = []
M.append("# Clean a Cat: what is left before we build, round two (2026-11-24 ET, Planning-Agent)")
M.append("")
M.append("This is the file copy of Derek's plan page, second version. The page lets Derek tick jobs, pick answers and type playtest notes, and it saves them where the team can read them. PAGE_LINK")
M.append("")
M.append("Round one is saved (playtest-notes.md, plan-page-round-one.md). This version holds only what is open. The questions are new and came from Derek's playtest notes, his comments on the mud, the baths and the store art, the two research rounds and the open calls from the other threads. Database ids: playtests `p-<id>`, to-dos `c-<id>`, questions `q2-<id>` (the round one questions were `q-<id>` and stay in the database untouched).")
M.append("")
M.append(f"## 1. Play these {NG} next")
M.append("Player counts are from the morning of November 24, 2026.")
M.append("")
M.append("| Game (id) | Time | Players and votes | Why it is on the list | Look for |")
M.append("|---|---|---|---|---|")
for g in GAMES:
    M.append(f"| [{g['name']}]({g['url']}) (`{g['id']}`) | {g['mins']} | {g['stats']} | {g['why']} | {g['look']} |")
M.append("")
M.append("**What to write down for each game**")
for i, p in enumerate(NOTE_PROMPTS, 1):
    M.append(f"{i}. {p}")
M.append("")
M.append("**The team also asked for**")
for a, b in EXTRA_PROMPTS:
    M.append(f"- {a}: {b}")
M.append("")
M.append("**If there is time**")
for g in OPTIONAL_GAMES:
    M.append(f"- [{g['name']}]({g['url']}) (`{g['id']}`): {g['look']}")
M.append("- Wash the Car (washing by hand) and Steal An Egg (the arrows and the menu that shows what grows while you are away).")
M.append("")
M.append("**Played and saved in round one**")
for g in DONE_GAMES:
    M.append(f"- {g['name']}: {g['took']}")
M.append("")
M.append("## 2. Derek's to-do list (open jobs only)")
for title, items in TODOS:
    M.append("")
    M.append(f"**{title}**")
    for t in items:
        link = f" [{t['link'][1]}]({t['link'][0]})" if t.get("link") else ""
        M.append(f"- [ ] **{t['t']}** (`{t['id']}`). {t['d']}{link}")
M.append("")
M.append("**Parked until the game is picked**")
for a, b in PARKED:
    M.append(f"- {a}: {b}")
M.append("")
M.append(f"## 3. {NQ} questions, each with our pick first")
n = 0
for title, who, lead, items in QUESTIONS:
    M.append("")
    M.append(f"**{title}** (from {who}){' ' + lead if lead else ''}")
    M.append("")
    M.append("| # | Question (id) | What it means | Options, our pick first |")
    M.append("|---|---|---|---|")
    for q in items:
        n += 1
        d = q["d"] + (" " + q["note"] if q.get("note") else "")
        M.append(f"| {n} | {q['t']} (`{q['id']}`) | {d} | {' / '.join(q['opts'])} |")
M.append("")
M.append("## Saved from round one")
for a, b in SAVED + DECIDED:
    M.append(f"- **{a}:** {b}")
M.append("")
M.append("## What happens when Derek is done")
M.append("Planning-Agent reads the answers from the page, folds them and the playtest notes into `gdd-draft.md`, asks for the design lock, finishes `milestone-1.md` and hands over to the coordinator.")
open(OUT_MD, "w", encoding="utf-8").write("\n".join(M) + "\n")
print("questions", NQ, "todos", NT, "games", NG, "html bytes", len(page))
