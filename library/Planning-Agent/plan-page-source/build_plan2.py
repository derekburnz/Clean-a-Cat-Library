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
    "What happens when a customer waits too long and what the staff take over.",
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

GAMES = []
OPTIONAL_GAMES = []
# played and saved; shown with what we took, no controls
DONE_GAMES = [
    dict(id="animaldaycare", name="Clean the Animal Daycare!", tag=" (played November 24)",
         took="Played November 24. Your verdict: pretty much the same as Clean Everything and unrelated to ours. Nothing taken. It was the last game on the list."),
    dict(id="petstore", name="Pet Store Tycoon", tag=" (played November 24)",
         took="Played November 24. Your words: it uses the same little guys for tips and you like it, it is played in first person which is odd, the tutorial steps are very well done and easy to follow, and it shows the daily check in rewards right after the tutorial, with a good reward on day 2. You also sent the starter bundle pop up it shows after day 2 and said it might not be a bad idea for starter packs. What we take, from your 14 pictures: a count on every tutorial step, such as 1 / 10, with one short line, one big arrow and a bright outline on the single thing to press while the rest of the screen dims. A guide in a bubble at the bottom with one button, which is how Suds talks in ours. A pack you open with your own hand by dragging across the foil, then cards with a New tag and a rarity. A summary when the shop day ends. A level road that shows what you just unlocked and what the next level gives. A check in card for seven days, shown once the tutorial is done. A daily quest card in the corner. Locked items that stay in view, greyed, with the level that opens each. A named event on a strip at the bottom that raises demand for one kind of pet, and a pill that shows a bonus on the next customer. A board on the street that features another player's store. What we asked you to look for: pets come in packs bought with the shop's own cash, the tutorial hands you the first one and the pets are the stock you sell, not helpers. The staff are a cashier, a stocker and a pet keeper, and its Robux shop sells them for 199 to 299 Robux each. Not taken: staff, cash and pet packs sold for Robux, since our helpers cost coins and our crates are earned. Five menu buttons on screen from the start. First person, since ours stays in third person so you see your character carry the kitten. A crossed out price, unless ours really was the higher one."),
    dict(id="horse", name="Save a Horse: Wash & Collect, the horse game", tag=" (played November 24)",
         took="Played November 24. Your verdict: another Steal an Egg copy with nothing really to do with cleaning, where waiting for the horse to be clean is the same as waiting for an egg to hatch. What we take from it: in ours the wash is always done by hand and a timer never stands in for it. Waits belong to builds and upgrades only. From your five pictures: one clear step line at the top with a short line under it and arrows on the floor work well. Its tutorial opens a shop with Robux prices beside the coin prices, which ours never does in the first session."),
    dict(id="cleaneverything", name="Clean Everything", tag=" (played November 24)",
         took="Played November 24. Your summary: you choose a map, load into it with 1 to 4 players and pick up scattered items and place them where they belong until the place is clean. So it is a sorting game with friends, not a wash game. What we take, from your eight pictures: it gives players a lot to chase besides the cleaning, with nine maps and three more shown as question marks, two bars that count every object and shelf, and a glowing target that shows where the thing in your hand goes. That fits why it kept its players. What we avoid: two loading screens before you play, a Robux offer on the screen from the first second, a reward for a like and a group join, helpers rented by the minute for Robux and a watch an ad button. One bakery holds 1,040 objects, which is a long job for one sitting."),
    dict(id="rt3", name="Restaurant Tycoon 3", tag=" (played November 24)",
         took="Played November 24. Your finding: they do not use friends as waiters or customers, and we can take some ideas from them. Ideas we take, from your 20 pictures: one goal bar at the top with a count, such as Cook 5 dishes, 0 of 5. Work that is one short swipe with a bar that fills and a Cancel button. A trail from you to the customer with a plain line that says what to do. A line that says a VIP customer just came in, with a Show Me button. An upgrades window with a tab for what you can buy now and a tab for what is locked, where each locked one says what it requires, so the long road is in view. Workers with a name, a job, a hire price and a price to level up. Not taken: three setup screens before the first customer, a starter pack with a countdown on the screen in the first minute and a premium worker in the hire list."),
    dict(id="puppyspa", name="Puppy Spa", tag=" (played November 24)",
         took="Played November 24 on your PC. Your take: it felt pretty bad overall and low quality, the trimming did not really work, it was not step by step about what to groom and it did not point at what you needed to use or do. So the lesson for ours is the guiding: one step at a time, the right tool already in your hand and a marker on what to do. What we still take from your eight pictures: small prompt pills, such as Admit and Clean, which are the answer to the big black buttons you disliked. The owner's wish in a bubble during the groom. A star meter with a percent that fills while you work. A tint on the part still to do. A rainbow bonus star and a separate tip line for a flawless job. You also carry the dog to the table there, as you carry the kitten to our tub. Not taken: a plus button beside the coins, since ours are never sold."),
    dict(id="barber", name="Barber Simulator", tag=" (played November 24)",
         took="Played November 24. Your words: holding on an area to cut while your right thumb turns the camera around the head was smooth and felt good. You could not find a way to get pets without paying, apart from a pop up that said to come back tomorrow for a pet egg when you walked out of the shop. What we take, from your 13 pictures: the hold and turn control as an idea for our wash view. A free pet egg promised for tomorrow, and a pet roll as the day 2 reward. A level up that unlocks a new tool. A card that shows what this customer wants. A marker over the next thing to do. A line of customers waiting outside. Not taken: pet spins sold only for Robux, pet slots sold for Robux, a starter pack with a countdown and a random pet in it and a watch an ad button."),
    dict(id="petsalon", name="My Pet Salon!",
         took="You liked the different kinds of step, the praise words with a growing number, the star card with coins and experience after each pet, tool upgrades, the index, rare customers with a lasting reward and hired helpers. You disliked the cutscene with no skip, the same swipe three times, 16 steps in one job, the pet turning by itself and only one customer at a time. First fun thing at about 75 seconds. Your replay on November 24 added ten pictures of the washing and one answer: the pet rotates round and round and you cannot turn it yourself."),
    dict(id="capybara", name="Capybara Onsen",
         took="Not a spa game: step on pads, buy and merge. Useful all the same: a short tutorial with a free first buy, a friend bonus percent on screen from the start and a request for a favourite at about minute 4."),
]

# what the six playtests told us, sorted by theme
THEMES = [
    ("The wash is the game", "The horse game put a timer where the wash should be and felt like an egg game to you. In My Pet Salon you liked the different kinds of step and disliked the same swipe three times, 16 steps in one job and the pet turning by itself. Your replay pictures show how it teaches a step: one line at the top, a hand that shows the move, a card that ticks off the steps and a bonus for perfect washes in a row. In Barber Simulator, holding on an area while your right thumb turns the view felt smooth and good. Restaurant Tycoon keeps its work to one short swipe. Puppy Spa tints the part still to do and fills a star meter while you work. Puppy Spa felt bad to you because it never said what to groom or which tool to use. Your call on November 24: no tool menu, the tool changes by itself as in My Pet Salon. Ours: always by hand, four to six short steps that differ, the right tool already in your hand and a cat that holds still and turns by itself when a side is done."),
    ("The first minute", "My Pet Salon made you wait through about 10 seconds of loading and a cutscene with no skip. Clean Everything has two loading screens and Restaurant Tycoon has three setup screens before the first customer. Capybara Onsen's short tutorial with a free first buy worked. Pet Store Tycoon's tutorial was the best you played: ten numbered steps, one arrow and one thing lit up at a time. Ours: the truck and the box start the moment you load and your first tap comes at about second 4."),
    ("Customers and the line", "One customer at a time felt lame in My Pet Salon, though you can choose who is next there. Barber Simulator shows a line of customers waiting outside. Restaurant Tycoon tells you when a VIP walks in, with a Show Me button. Ours: a bench of cats that differ, a Next cat button and rare visitors that are announced."),
    ("Workers", "My Pet Salon and Restaurant Tycoon both have named workers you hire and level up, and Restaurant Tycoon ties some upgrades to a worker's level. Ours: human staff, Jo and Sam, hired and levelled with coins, slower than you."),
    ("Pets", "My Pet Salon has a My Pets window where pets boost cash. In Barber Simulator pets come from spins sold for Robux, and the only free one you found was a pet egg promised for tomorrow. In Pet Store Tycoon pets come in packs bought with the shop's own cash, and you rip the pack open yourself. Your idea: washing earns the money and the pets you own come from crates, one for you and one for each worker. Our pick: every pet can be earned, crates are never sold for Robux and the chances are shown."),
    ("Things to chase and reasons to come back", "Clean Everything, the cleaning game that kept its players, has maps, counters and modes on top of the tidying. Restaurant Tycoon shows a long chain of locked upgrades and what each requires. My Pet Salon's album has 59 pets. Barber Simulator gives a pet roll on day 2 and a new tool on level up. The horse game shows what you made while away. Pet Store Tycoon shows a seven day check in card right after the tutorial, with a good reward on day 2, and a daily quest in the corner. Ours: the index of coats, an upgrade road you can see, a free crate tomorrow and a tip jar that fills while you are away."),
    ("The screen and the guiding", "Help bubbles along the bottom and a result card with stars in My Pet Salon. A goal bar with a count in Restaurant Tycoon. A step line at the top and arrows on the floor in the horse game. A marker over the next thing and a card of what the customer wants in Barber Simulator. A friend bonus percent on screen in Capybara Onsen and Barber Simulator. We take all of these in our own look. One thing we do not take: the big black prompt buttons, which you said block the view on a phone. Puppy Spa shows the fix, a small pill with one word."),
    ("Asking and selling", "Nearly all of these games ask for notifications in the first minute or two, and you said the timing never felt smooth. Restaurant Tycoon sells a skip for Robux. In My Pet Salon you found no way to get a pet except Robux, which you called kinda scummy. Capybara Onsen asked for a favourite at about minute 4. My Pet Salon and Clean Everything reward likes. Starter packs with countdowns sit on the screen in the first minute in Restaurant Tycoon, Barber Simulator and My Pet Salon. Pet Store Tycoon waits until after day 2 and shows its bundle once, with no countdown, and you said that might not be a bad idea for ours. Clean Everything and Barber Simulator have watch an ad buttons. My Pet Salon makes customers from your friends and Restaurant Tycoon does not. Ours: one notification ask from Suds after his wash, no paid skips, pets that are earned, no offer in the first session, no countdowns, no rewards for likes and no friends as customers at launch."),
]

# ---------------------------------------------------------------- to-dos
TODOS = [
    ("The game: seven picks decide what we build", [
        dict(id="t2-loop", q="loop", t="Pick the playstyle",
             d="The pick the rest waits on. Our pick: your busy spa and the cat collection together. Your answers on the index, the crates and the pet slots already lean that way."),
        dict(id="t-queue", q="queue", t="Cats wait on a bench and you pick who is next",
             d="Our pick: yes, with a Next cat button for players who do not want to choose."),
        dict(id="t-impatience", q="impatience", t="Waiting cats get grumpy but are never lost",
             d="Our pick: only the bonus tip shrinks."),
        dict(id="t-helpers", q="helpers", t="Hired helpers wash common cats, slower than you",
             d="Our pick: yes, for coins only and about twice as slow as you."),
        dict(id="t-rare", q="rare", t="Rare visitors who are pickier, not longer",
             d="Our pick: yes, with a lasting reward."),
        dict(id="t-pets", q="pets", t="The pets you own: cats, seen in the spa",
             d="New. Our pick: cats only, and Suds takes no slot."),
        dict(id="t-session", q="session", t="Build enough for a first session of 20 minutes",
             d="Our pick: yes, about 24 coats on day one."),
    ]),
    ("New since your last answers", [
        dict(id="t-starterpack", q="starterpack", t="A starter pack: yes or no, and what is in it",
             d="From the bundle Pet Store Tycoon showed you. Our pick: fixed contents for 99 Robux, shown once on your second visit."),
        dict(id="t-checkin", q="checkin", t="A card after the tutorial with what waits on your next days",
             d="From the check in card you noted in Pet Store Tycoon. Our pick: yes, counted by days you play, with no streak."),
        dict(id="t-quests", q="quests", t="Weekly quests that give a crate",
             d="From your answer that crates should be hard to get, like finishing all the weekly quests."),
        dict(id="t-builder", q="builder", t="The builder: a person or a kitten",
             d="Our pick: a person, since the staff are people now."),
    ]),
    ("Then the rest, and done", [
        dict(id="takeall", t="The other picks: tap through them or take ours in one press",
             d="They cover the wash, coming back, the screens, the look, the sound and the store page. Under Tap through our picks there is a button that takes our pick for everything you have not answered. Press it, change any you disagree with and tick this."),
        dict(id="lock", t="Say done",
             d="Tick this or say done in chat. We then write the final one page design from your picks and show it to you before the build starts. Nothing reaches the live game without your word."),
    ]),
    ("Answered already, your words are saved", [
        dict(id="puppytake", t="Your own take on Puppy Spa",
             d="You sent the pictures with no notes. Did the grooming feel good, what made you want to stop, how did the green tick that ends the groom feel and did [NEW] in its name do anything for you? Nearly half its voters disliked it, and we cannot tell why from pictures."),
        dict(id="mpswords", t="My Pet Salon, four things from memory",
             d="Roughly how many seconds one normal wash takes. How much slower the hired helper is than you. How you get a pet there: an egg or a crate, for cash or for Robux. And what loses a star, if you ever got less than full stars. A guess is fine, and so is do not know."),
        dict(id="rtskip", t="Does the skip button on Restaurant Tycoon's goal bar cost Robux?",
             d="It sits beside Cook 5 dishes at the top. If you did not press it, say so and we leave it."),
        dict(id="notifwords", t="Which games asked for notifications, and how soon",
             d="You noted that many of these games ask almost at once. From memory: which ones, and was it in the first seconds or after the first job? That sets the timing of ours."),
        dict(id="t-friendcust", q="friendcust", t="Friends as customers: our pick is no",
             d="You found that Restaurant Tycoon does not use friends as customers or waiters."),
        dict(id="t-heldeyes", q="heldeyes", t="The kitten's eyes while you carry him: open or shut",
             d="Model-Agent's question from the carry."),
        dict(id="t-turn", q="turn", t="The cat turns by itself when a side is done",
             d="Your idea from the to-do list. The right thumb turn from Barber Simulator is the second option."),
        dict(id="t-notifyask", q="notifyask", t="When we ask for notifications",
             d="From your note that popular games ask almost at once."),
        dict(id="t-return", q="return", t="A free crate waiting tomorrow",
             d="From the pet egg Barber Simulator promised you for tomorrow. Only if pets come from crates."),
        dict(id="t-sudsbubble", q="sudsbubble", t="Suds talks in a help bubble at the bottom",
             d="From the My Pet Salon bubbles you sent."),
        dict(id="t-newtag", q="newtag", t="[NEW] in front of the game name or not",
             d="You asked us to look into it. Puppy Spa uses it and you have now played it, so say whether the tag did anything for you."),
        dict(id="t-keep", q="keep", t="Washed cats still fill an index",
             d="First of three picks on your idea that the pets you own come from crates."),
        dict(id="t-crates", q="crates", t="Your pets idea: the four crate rules",
             d="Every pet can be earned. Barber Simulator sold them only for Robux and you looked for another way."),
        dict(id="t-petslots", q="petslots", t="Your pets idea: one pet for you and one for each worker",
             d="What the worker's pet boosts and what coins buy."),
        dict(id="devtest", t="Play the draft in the dev place",
             d="Your rule from November 24: everything goes to the dev place first and nothing reaches the live game until you say it is good. You ticked this on November 24. Each time a new draft is up we say so in chat. Three answers help the most: did scrubbing feel good, was the clean kitten a nice moment and would you wash a second cat."),
    ]),
]
PARKED = [
    ("Server size", "Set once the street and the design are picked."),
    ("Maturity questionnaire", "We write the answers down for you once the gameplay is decided. The game needs a Minimal or Mild result."),
    ("100 plays from engaged players", "Your ads for this come when the game is ready for public testers."),
    ("Notification text and key", "Needed once you pick when we ask, which is in the questions below. Players under 13 cannot get notifications."),
    ("Store art, second version", "A more detailed icon and thumbnails wait for the design to lock."),
    ("Sound uploads", "One batch after the game is picked."),
    ("Plus or Premium", "Only if Roblox asks for it when we apply for Kids and Select."),
    ("Private repos", "At release."),
]

# ---------------------------------------------------------------- questions
YES = "Yes, go with it"
ELSE = "Something else"
QUESTIONS = [
    ("The game", "Planning-Agent", "These twelve decide what we build. Your playtests are done and five are answered already. The other seven are at the top of your to-do list.", [
        dict(id="loop", t="Your busy spa and a cat collection, together",
             d="All nine playtests are in, sorted under What the games told us near the top of this page. They point one way: the wash has to be real hand work, and the games that last give players more to chase than the work itself. Our pick puts your two ideas together. The busy spa is the minute to minute play: several cats wait, you pick who is next and helpers take the easy ones. The collection is the reason to keep going: every cat's coat is hidden under the mud, each new one fills a slot in your Cat Index and the pets you own come from crates that are hard to earn. Your own answers already lean this way. You said washed cats fill an index, crates are earned and a pet for you and each worker is a good idea. So this pick mostly confirms what you have said. Five of the six cleaning games from this summer are at 3% of their peak or less. The one that held on gives players more to chase than the cleaning.",
             opts=["Yes, both together", "Busy spa only", "Collection only, one cat at a time", ELSE],
             note="You said you would decide this after the playtests, and they are done. This is the pick the rest waits on. Nothing is built from it until you tap it or say so."),
        dict(id="queue", t="Cats wait on a bench and you pick who is next",
             d="You called one customer at a time kinda lame. Three or four cats wait, each with a card: name, how dirty, what kind of dirt and what it pays. Picking only matters when the cats differ, so a muddier cat pays more and a fussy one tips more but waits less. Each card also gets one line of our own on how the cat got so dirty, an idea from the story line on the wash screen you sent. You checked on November 24: My Pet Salon lets you press next pet on the table or choose which waiting pet goes next. So picking is not new on Roblox, and we were wrong to say no game has it. What ours adds is a reason to choose: the cats on the bench differ in what they pay, how long they wait and what kind of dirt they have, and the card shows it. We also take the one tap Next cat button for players who do not want to choose.",
             imgs=[("art2/queue-normal.jpg", "Draft screen: a row of waiting cats with a name, rarity, dirt icons, a mood bar, a coin amount and a Wash button each. One card says Helper Suds is washing.", "Draft: who is next")],
             solo=True,
             opts=["Yes, a bench and a pick", "One cat at a time", ELSE]),
        dict(id="impatience", t="Waiting cats get grumpy but are never lost",
             d="You floated customers who get impatient and leave. Lost customers are what parents and reviewers complain about most in shop games. Our pick: a waiting cat's mood drops and only its bonus tip shrinks. A cat that waits far too long goes home and comes back later.",
             opts=["Yes, grumpy and a smaller tip", "They leave and the job is lost", "No waiting pressure at all", ELSE]),
        dict(id="helpers", t="Hired helpers wash common cats, slower than you",
             d="Your idea. Helpers are bought with coins and never with Robux. A helper takes a common cat from the bench, washes it slowly and earns fewer stars. Rare cats always wait for you. The picture still shows kitten helpers. They are human staff now, which is the next question. Your number from My Pet Salon: a hired helper takes somewhere from 30 to 60 seconds a pet, about twice as long as you. Ours keeps that gap. Pet Store Tycoon sells its staff for Robux, 199 to 299 each: a cashier, a stocker and a pet keeper. Ours stay coins only, as you first said.",
             imgs=[("art2/helpers.jpg", "Draft screen: a Helpers window with two helper kittens, their speed bars, what each is washing and a Hire button on an empty spot.", "Draft: helpers")],
             solo=True,
             opts=["Yes, slow helpers for common cats", "Helpers can wash any cat", "No helpers at launch", ELSE]),
        dict(id="helperlook", t="Helpers are human staff, not cats",
             d="You said on November 24 that helpers are likely staff like humans. Our pick agrees. A person in a spa apron reads as staff at a glance, has hands for the sponge and the towel and can reuse the customer figures we already build, so it costs less than a kitten that has to hold tools. One other idea: staff do the washing and Suds the kitten stays as the spa's mascot, who points things out in the first minutes and cheers but never washes. The builder kitten for stations is a separate call. Say in the note if the builder should be a person too. Update: you said ok to staff with Suds as the mascot, and that Suds should not stand. So he walks on four paws like every other cat, which also means he cannot hold a tool. He explains things by trotting to them and sitting beside them with a speech bubble of a few words, and he shows up again each time something new unlocks.",
             opts=["Human staff, no helper cats", "Human staff, and Suds stays as the mascot", "Kitten helpers as drawn", ELSE]),
        dict(id="rare", t="Rare visitors who are pickier, not longer",
             d="You liked the influencer customers and their lasting reward, but 16 steps felt long. Ours bring a rare cat and want a near perfect wash, with the same short job as any cat. A finished visit gives a lasting reward, for example a small permanent tip bonus and a framed photo for your wall. Visitors unlock as your spa earns stars. The chance of each is on a board and none can be bought. Restaurant Tycoon 3 tells you when a VIP customer walks in, with a Show Me button that points you to them. Ours does the same for a rare visitor, so nobody misses one. Puppy Spa shows what the owner wants in a small bubble during the groom, such as short and even all over. A rare visitor in ours states a wish the same way, so being pickier is clear before you start.",
             opts=["Yes, pickier and not longer", "Longer jobs for rare visitors", "No rare visitors at launch", ELSE]),
        dict(id="keep", t="Washing earns the money, and the pets you own come from crates",
             d="Your answer on the to-do list on November 24: washed cats fill an index. So our pick stands and both stay. Your thought earlier that day: cleaning cats is how you make money, and it has nothing to do with the pets your shop owns. Those come from crates that are hard to earn or are bought with coins, like the My Pets window you sent. This replaces our first idea, strays you wash and keep in the window. What it leaves open is the Cat Index. Our pick keeps it: every customer cat's coat is still hidden under the mud, and each new coat you wash fills a slot and counts toward a bonus. That way the wash keeps its surprise and the crates are a second thing to chase, not the only one. Suds stays outside both.",
             imgs=[("art2/reveal-rare.jpg", "Draft screen: a New cat card for a white cat called Marble, marked Rare, 11% of customers, added to your Index.", "Draft: a new coat is revealed")],
             solo=True,
             opts=["Pets from crates, washed cats still fill the index", "Pets from crates, no index of washed cats", "Strays you wash and keep, as first drafted", ELSE]),
        dict(id="crates", t="Crates follow four rules",
             d="A crate is a random reward, so Roblox's rules and our own rules for young players apply. Your answer on November 24: crates can be earned and roll for pets, but they are really hard to get, like finishing all the weekly quests, and the pets are rewarding and help a lot. You also said that pets you can only get with Robux, as in My Pet Salon, seem kinda scummy. Our pick now: one, crates are earned by playing, are hard to get and are never sold for Robux or for coins. The main way is a short list of weekly quests, and finishing all of them gives a crate. Two, the chance of every pet is shown on the crate before you open it. Three, after a set number of crates the next one is sure to hold a pet you do not have, so nobody has a long unlucky run. Four, no timers, no stock counters and no near miss tricks on the opening. A rare visitor's reward could be a crate, which gives the hard to earn kind. Since coins do not buy crates, the 2x Coins pass has nothing to do with them, which keeps us well inside Roblox's rule on paid random items. The chances are shown all the same. Weekly quests are a new piece and have their own question under Coming back. Barber Simulator shows why: its pet spins are sold only for Robux, and you looked for another way to get a pet and found none. In Pet Store Tycoon you rip a pack open yourself by dragging across the foil. Ours is opened by hand too, in our own way, such as pulling the ribbon off the crate.",
             opts=["Yes, these four rules", "Also sell crates for Robux", ELSE]),
        dict(id="petslots", t="One pet for you and one for each worker",
             d="Your answer on November 24: you think this is a good idea but might change it later. So it is our working plan and stays easy to change. Your idea: you assign one pet to yourself and one to each worker, the worker's slot is an upgrade that is unlocked or paid for, the worker's pet boosts either speed or money and the other one is an upgrade bought with coins. Our pick on the details: your own slot is open from the start, a worker's slot unlocks with coins, the pet boosts the money that worker makes and coins buy the worker's speed. A steady speed upgrade keeps the spa's pace easy to tune, and a rare pet then feels valuable without making workers faster than you. Workers with their pets still earn less than your own washing.",
             opts=["Yes: slot for coins, pet boosts money, coins buy speed", "Pet boosts speed, coins buy money", "Sell the worker slot as a game pass", ELSE]),
        dict(id="pets", t="The pets you own are cats, and you see them in the spa",
             d="Not asked before, and the builders need it. The game is about cats, so our pick is that crate pets are cats too: special breeds and coats that never come in as customers, so a pet from a crate is easy to tell from a cat you washed. Your own pet follows you around the spa and each worker's pet sits by that worker's tub, so players on the street can see what you have. Suds is not a pet and takes no slot. He stays the mascot, so every new player starts with an empty slot and a reason to want the first crate.",
             opts=["Cats only, seen in the spa, and Suds takes no slot", "Other small animals too, such as bunnies and puppies", "Suds fills your own slot as a free starter pet", ELSE]),
        dict(id="firstminute", t="You rescue a muddy kitten from a box, and he becomes Suds",
             d="Your idea from November 24: a truck drives past, a plain brown box falls off the back and lands in front of you, you open it and find a messy, muddy kitten, and the tutorial is cleaning him up for a score. Once he is clean he becomes Suds. The box is settled: a random brown box, so his name comes from the wash. How the scene plays is settled too: you said A for sure, the quick intro you watch, the truck going by and the box falling in front of you, and then you get your camera back and play. We keep it to about 4 seconds, because you disliked the cutscene with no skip in My Pet Salon, and it starts the moment your character loads, with no loading screen. Also settled on November 24: you lift the kitten out of the box and carry him to the tub, and placing him in the tub switches to the close up wash view where the steps are taught. You tap the box at about second 4 and scrub at about second 12, which is about 9 seconds later than spawning at the tub. It is built behind a switch, so the first test can still compare it with the tub start if you want that. His wash always ends on three stars, so nobody fails the opening.",
             imgs=[("art2/tutorial-trail.jpg", "Draft screen: green arrows on the ground lead to the spa door, a yellow arrow bobs over the goal and the top line reads Step 1 of 3: Follow the arrows.", "Draft: the trail that leads from the box to the tub")],
             solo=True,
             opts=["A quick intro you watch, about 4 seconds, then play", "A scene you play, the camera is always yours", "No scene, spawn at the tub and scrub", ELSE]),
        dict(id="session", t="Aim for a first session of 20 minutes or more",
             d="In one report on Roblox games, about 11 in 100 new players came back the next day when sessions ran over 25 minutes and about 4 in 100 when they ran under 3. That is a link, not proof. It means more on day one than we first planned: about 12 cats, 3 kinds of dirt and 4 tools. Your screenshot of My Pet Salon's album shows 59 pets in six rarities. Twelve coats would look thin beside that, and a coat costs us far less than a new animal because every cat shares one body. So we would go to about 24 coats on day one if Model-Agent confirms the cost.",
             opts=["Yes, build more for day one", "Keep the first build small and add later", ELSE]),
    ]),
    ("The wash", "Planning-Agent and Design-Agent", "", [
        dict(id="steps", t="Four kinds of step at the start",
             d="You liked the variety in My Pet Salon. Ours at launch: scrub the mud, rinse with the shower, pick burrs out of the fur and towel dry. Later tools add nail trim, comb, shampoo and the dryer. The models for all of these are drafted. Barber Simulator gives a new tool at level 2 with a Level Up banner. Ours hands out the later tools the same way, so the first ten minutes hold two or three of those moments. Decided by you on November 24: no tool menu. The game changes to the right tool for each step by itself, as My Pet Salon does, so you never pick a tool and the whole screen is for washing. The picture below was drawn before that and still shows four tool buttons. They go, and the screen is being redrawn. The next tool you unlock shows on the step list and on the upgrade road, so it is still in view.",
             imgs=[("art2/wash-scrub.jpg", "Draft screen: a muddy cat in a tub, the line Step 1 of 4 Scrub the mud, four tool buttons at the bottom (now removed, the tool changes by itself), a progress bar, the praise word Awesome with x12 and a round turn button on each side.", "Draft: the wash, drawn before the tool buttons were removed")],
             solo=True,
             opts=["Yes, these four first", "Fewer: scrub, rinse and dry", "All of them from the start", ELSE]),
        dict(id="joblength", t="Four to six short steps per cat, never the same step twice in a row",
             d="You found the same swipe three times boring and 16 steps too long. Our first draft had steps of 8 to 15 seconds, so about a minute a cat. A Step 2 of 4 line shows how far along you are. In your replay a common pet had three or four steps and a rare cat had six, so their rare jobs are about twice as long. Ours stay the same length and ask for more care. Your numbers from My Pet Salon on November 24: a step takes about 4 to 6 seconds and most washes were 3 to 5 steps, so a wash there is about 15 to 30 seconds. Ours was twice that. We shorten ours to steps of about 5 to 8 seconds, so a cat takes about half a minute, and time it on a phone in the dev place.",
             opts=["Yes, 4 to 6 short steps", "Shorter, 3 steps", "Longer jobs are fine", ELSE]),
        dict(id="turn", t="The cat holds still and turns by itself when a side is done",
             d="You said the pet turning the whole time in My Pet Salon made you miss spots, and you confirmed that you cannot turn it yourself there. Your idea on the to-do list on November 24: maybe make it so that when you complete a side, the game turns the cat for you. That is now our pick. The cat never moves while you work on a side. When that side is clean it turns once, with a small sound, and you carry on. Together with the tool that changes by itself, the wash needs one finger and no buttons: you scrub and the game does the rest. In Barber Simulator you liked turning the view with your right thumb while you cut. That stays as the second option, and the builders can put it behind a switch in the dev place so you can feel both. The camera still moves to the part you work on between steps, such as down to the paws for a trim.",
             opts=["Still cat, turns by itself when a side is done", "Still cat, right thumb turns the view", "Still cat, two arrow buttons to turn", "Slow turning all the time", ELSE]),
        dict(id="praise", t="Praise words and a combo that pauses on a slip",
             d="You noticed Awesome and Excellent with a growing number. Ours: short words that name what you did, one at a time and never under your finger, beside a combo count. A slip pauses the combo and does not reset it to zero, which feels unfair to young players. Your replay pictures of My Pet Salon show two more things we take in our own words: a word when a step is done, and a streak for perfect washes in a row that adds a little to each tip, 10% for one and 20% for two there. A slip ends the streak and costs nothing else.",
             opts=["Yes, pause on a slip", "Reset the combo on a slip", "No combo", ELSE]),
        dict(id="tools", t="Tool upgrades change how the tool feels",
             d="You liked upgrading tools. Each tier changes the shape and what the tool does as well as the speed: a wider sponge, a shower with a fan spray, a comb that shows hidden burrs. Tier 2 is lilac and tier 3 is gold.",
             opts=["Yes, each tier feels different", "Speed only, simpler to build", ELSE]),
    ]),
    ("Coming back", "Planning-Agent", "", [
        dict(id="longbuild", t="The first long build comes after about minute 15, not minute 6",
             d="The old plan offered an 8 hour VIP Room at minute 6. In the hit games waits start at seconds and reach hours only once the player cares. The rest stays: the builder kitten builds one station at a time, a building site one room at a time, nothing takes over 24 hours and a finished build waits for you. One idea from Restaurant Tycoon 3 goes with this: its upgrades window has a tab for locked upgrades, and each one says what it requires. Ours shows the same road ahead, so a player always sees the next two or three things to work toward.",
             imgs=[("art2/builder-busy.jpg", "Draft screen: a Builder window with a station building for 4 more minutes and a VIP Room building for 7 more hours with a Notify me bell.", "Draft: the builder")],
             solo=True,
             opts=["Yes, long builds later", "Keep it at minute 6", "No builds over 1 hour at launch", ELSE]),
        dict(id="skips", t="No paid skips on timers",
             d="We sell a Second Builder pass instead. Paid skips read as pressure for a young audience and are what reviewers of spa games complain about most. You checked on November 24: the skip button in Restaurant Tycoon 3 costs Robux. Ours stays without one.",
             opts=["Yes, no paid skips", "Sell skips at launch", ELSE]),
        dict(id="return", t="Three reasons to come back tomorrow, and no streak",
             d="Players under 13 cannot get our notifications, so a bell cannot be the main hook. Ours: a tip jar that fills while you are away and stops at a cap, the empty slots in your index and one different visitor cat each day. There is no streak to lose. Suds meets you at the door and points at the full tip jar and today's visitor. He is always glad to see you and never sad that you were away. The bell is for players of 13 and over only. When we ask for it is the next question. New on November 24: Barber Simulator told you to come back tomorrow for a pet egg as you left the shop, and its day 2 reward is a pet roll. If pets come from crates, ours does the same without a streak: near the end of the first session Suds says a free crate will be waiting tomorrow. Missing a day loses nothing. Your answer on November 24: that works. Make the free crate a good one, with other crates earnable but hard, like completing all the weekly quests. The check in card that Pet Store Tycoon shows after its tutorial is the next question.",
             opts=["Yes, these three, plus a free crate tomorrow if pets come from crates", "These three only", "Add a daily streak reward", ELSE]),
        dict(id="checkin", t="A card after the tutorial shows what waits on your next days",
             d="Pet Store Tycoon shows a seven day check in card right after its tutorial, and you noted the good reward on day 2. Ours: once Suds is clean and the tutorial is done, he shows one card with a small reward for each of your next seven days of play. Day 2 is the good crate you asked for and day 7 is the biggest. It counts days you play, not days in a row, so missing a day loses nothing and nothing resets. That keeps it fair for young players, which a streak is not, and still gives a reason to open the game tomorrow. It shows once and then sits behind a small button.",
             opts=["Yes, seven days, counted by days you play", "A streak that starts over if you miss a day", "No card, Suds only says a crate waits tomorrow", ELSE]),
        dict(id="quests", t="Weekly quests, and finishing all of them gives a crate",
             d="From your answer on crates: really hard to get, like finishing all the weekly quests, but rewarding. Ours: a list of about five quests that changes each week, such as wash 40 cats, get 10 perfect washes or serve 3 rare visitors. Each quest pays coins and finishing the whole list gives one crate. That makes a crate about a week of steady play, which is hard to get without being out of reach. Pet Store Tycoon also keeps one small daily quest in the corner of the screen. Ours adds that for coins only, so every visit has a short goal. The list sits behind one button and Suds points at it once. The exact quests and numbers are set after you pick the playstyle.",
             opts=["Yes, a weekly list for a crate, plus one small daily quest for coins", "The weekly list only", "No quests at launch, crates come from rare visitors only", ELSE]),
        dict(id="notifyask", t="Ask for notifications early, right after the first clean cat",
             d="Your note from November 24: a lot of the popular games you played ask for notifications almost at once after you start. Our plan had the bell only as a small extra on a long build, which most new players would never reach on day one. So we move the ask up. Our pick: once, right after Suds is clean and named, at about minute 1, in his bubble and in our own words, for example a line that he will tell you when the tip jar is full. Not at second one, because nothing should sit on top of the truck and the box, and a player who has just had the first win has a reason to say yes. Roblox only shows the ask to players of 13 and over, so younger players see nothing. A player who says no is not asked again in that session. The timing sits behind a switch, so we can test ours against the instant ask. We check Roblox's own rules for the ask before it is built. Your answers on November 24: ask 1 to 2 minutes in. You also said nearly every game you played asked in the first minute or two and the timing never felt smooth, even in the popular ones. So ours has to feel like part of the story: Suds asks once, in his own bubble, right after his wash, and never as a pop up over play.",
             opts=["Once, after the first clean cat", "At the very start, like the games you played", "Only when the first long build starts", ELSE]),
        dict(id="reopen", t="A Grand Reopening for players who finish the spa",
             d="The games that last have a start again step, and so does Clean Everything. Ours: move to a bigger spa, keep every cat and gain a permanent tip bonus. It is not needed for the first test, but the saved data has to allow for it from the start.",
             opts=["Yes, plan it now and build it after the first test", "Build it for launch", "No start again step", ELSE]),
        dict(id="friends", t="A small bonus for each friend in your server",
             d="You saw the friend percent on screen in Capybara Onsen. Ours: 10% more tips per friend in the server, shown from the start. Helping inside a friend's spa comes later.",
             opts=["Yes, a friend bonus", "No friend bonus", ELSE]),
        dict(id="friendcust", t="No friends as customers at launch",
             d="You said you would decide this after seeing Restaurant Tycoon 3. Your finding on November 24: they do not use friends as waiters or customers. So the shop game that has lasted longest does without it, and My Pet Salon is the only one we know that does it. Our pick is now to leave it out at launch. It also saves memory on phones, keeps your friends from being shown to strangers on a shared street and avoids the days when Roblox's friend list comes back empty. Restaurant Tycoon's start window has a Managers row with a plus button, which looks like a way to let a friend help run your place. That fits our plan for friends better: the bonus for a friend in your server now, and friends helping in your spa later behind its switch. You wrote no friends on the to-do list on November 24, so this is settled.",
             opts=["No friends as customers", "Light version: a friend's name and face on the card", "Friends walk in as full avatars", ELSE]),
        dict(id="visit", t="Neighbours look through the window but do not walk in",
             d="Players see each other's windows and reveals from the street. Walking in is built behind a switch that stays off, so friends helping in your spa can be turned on later without a rebuild. It stops a crowd standing on someone's tub.",
             opts=["Yes, window only for now", "Walk in from the start", ELSE]),
        dict(id="trading", t="No trading of cats",
             d="Trading is the one feature with a clear record of harm to young players, mostly scams. This holds for crate pets too.",
             opts=["Yes, no trading", "Plan trading for later", ELSE]),
        dict(id="favourite", t="No like or favourite ask in the first session",
             d="Capybara Onsen asked you for a favourite at about minute 4. Roblox judges a game on its first minutes, and an ask there is one more thing between a new player and the fun. Our pick: nothing in the first session, then one small ask after a great wash on a later visit. It never comes with a reward, because Roblox does not allow rewards for likes or favourites. Your screenshot shows My Pet Salon paying cash for both in its Rewards window. By our reading of the rules that is their risk and we do not copy it.",
             opts=["Yes, one ask on a later visit", "Ask once at about minute 5", "Never ask", ELSE]),
    ]),
    ("Screens", "Design-Agent", "", [
        dict(id="recap", t="After each cat: the full card or a slim strip",
             d="You called the star card with a coins and experience breakdown kinda cool. With a line of cats waiting, a full window after every wash slows you down. Our pick: the full card for your first cats and for any new or rare cat, and the slim strip for the rest. Two things from your My Pet Salon screenshots go into ours. Their card sits at the side so the clean pet stays in view, with one line for each reason you earned. And Roblox's own badge note covered their Collect button, so our button stays out of that corner. Puppy Spa adds a rainbow bonus star and a separate tip line when a job is flawless. Ours shows the tip on its own line too, so a perfect wash visibly pays more. You did not notice anything that loses a star in My Pet Salon and guessed it might be time. Ours says on the card what each star was for, so nobody has to guess.",
             imgs=[("art2/recap-full.jpg", "Draft screen: a Great job window with the cat's picture, three stars, three rows of coins earned, a total and a Next cat button.", "Full card"),
                   ("art2/recap-compact.jpg", "Draft screen: a slim strip at the bottom with the cat's face, three stars, the coins earned and a Next cat button, the tub still in view.", "Slim strip")],
             wide=True,
             opts=["Full card for new cats, slim strip for the rest", "Full card after every cat", "Slim strip after every cat", ELSE]),
        dict(id="hud", t="Menu buttons appear one at a time",
             d="The draft has four round buttons on the left: Index, Tools, Helpers and Build. Our pick: a new player sees none, and each pops in with a short pointer the first time it is useful. Index after the first cat, Tools at the first upgrade, Build and Helpers later. That keeps the first minutes about the cat. Suds does the pointing: he trots to the new thing and sits by it. He shows each thing once, never opens a window himself and never points at anything that costs Robux. For comparison, your screenshot shows My Pet Salon with all four of its buttons on screen from the first second. Restaurant Tycoon 3 keeps one goal bar at the top with a count, such as Cook 5 dishes, 0 of 5. Ours gets the same one line goal with a count, which Suds points at once.",
             imgs=[("art2/hud.jpg", "Draft screen: the main view with four round buttons at the left, a goal line at the top, coins at the top right and two waiting cats at the right.", "Draft: the main screen with all four buttons")],
             solo=True,
             opts=["Yes, one at a time", "All four from the start", ELSE]),
        dict(id="sudsbubble", t="Suds explains in a help bubble at the bottom of the screen",
             d="You sent My Pet Salon's help bubbles as an idea: a guide at the left, a bold line, a short sentence and one big button that does the step. Our pick is the same idea in our own look. Suds's face is at the left, the bubble holds one short title and one sentence that says why, and one button does the step, so you still do every tap. It shows one at a time for tutorial steps and new unlocks, and goes away after the tap. Theirs runs under the jump button, so ours stops short of the stick and the jump button on every phone. A Tips switch in Settings turns the bubbles off once the tutorial is done. The replay pictures show their bubble during the first wash too, with one line: the top says what to do, copy the hand. Suds says his own version of that once, on the first wash only. Your answer on November 24: do it like the bottom text in My Pet Salon with the guide at the side, but Suds for us. Settled. Pet Store Tycoon guides the same way with its shop helper, and you said you like it and that its tutorial steps are very well done and easy to follow. We take its three habits for our tutorial, in our own look: a step count at the top, one arrow, and a bright outline on the one thing to press while the rest of the screen dims.",
             opts=["Yes, a bottom bubble with one button", "Only a small bubble over Suds in the spa", ELSE]),
        dict(id="camera", t="A close camera at the tub with the move stick hidden",
             d="Settled by you on November 24: placing the kitten in the tub switches to a close up wash view, where the steps are taught. We saved that as our pick here. While you wash, the camera moves in on the cat and the move stick hides, so the whole screen is for scrubbing. Our own test found that scrubbing over the stick also walked the player away, and this fixes it. Change the pick if you want the stick to stay.",
             opts=[YES, "Keep the normal camera", ELSE]),
        dict(id="landscape", t="Lock phones to landscape",
             d="One layout to get right, with more room for the tub.",
             opts=[YES, "Allow portrait too", ELSE]),
        dict(id="bows", t="A bow as the finishing touch",
             d="The first plan had you pick a bow on every cat. With a line waiting that is one tap too many. Our pick: bows for the pets you own and for rare visitors. My Pet Salon ends some washes with a tap to feed the pet a snack, a step nobody can fail. Our bow does the same job: an easy last step that ends the wash on a good note.",
             opts=["Bows for your own cats and rare visitors", "A bow on every cat", "No bows", ELSE]),
    ]),
    ("The look", "Model-Agent", "", [
        dict(id="heldeyes", t="The kitten's eyes while you carry him",
             d="Model-Agent's question. The held kitten now matches the pose you sent: lying across your arms with his chin tucked on his paws. His eyes are open in the current model. Open reads as awake and looking at you, which suits a kitten who was just found. Shut reads as asleep and safe. Your answer on November 24: go with what we suggest, and it depends on whether you carry customers' pets. Our call: open, as he is now. Suds is the only cat the plan has you carry so far. If customers' cats are carried later, their eyes are open too, so you can read their mood.",
             opts=["Open, as it is now", "Shut, asleep in your arms", ELSE]),
        dict(id="builder", t="The builder is a person in overalls, not a kitten",
             d="Stations and rooms are built by a builder, and the old drafts show a kitten in a hard hat. Since the helpers are human staff and Suds walks on four paws and never works, a kitten that builds no longer fits. Our pick: a person in overalls, made from the same figure as the staff, so it costs nothing new.",
             opts=["A human builder", "Keep the builder kitten", "No builder shown, new things just appear", ELSE]),
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
             d="Muffin, Smudge, Inky, Cotton, Tux, Patches, Toffee, Marble, Lilac Cloud and Starcoat. Suds is the mascot kitten and the first cat every player washes. He has no name until he is clean. None is used in Cat Cafe.",
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
             d="You asked us to look into whether putting new in brackets before the name helps. Growth-Agent read six pages on it. Nobody has measured it: we found no test with numbers, only opinions. Roblox has no rule against it, but says titles must describe the game and that tags are not used in its ranking. Search weighs the front of a title most, so a bracket there pushes the real words back, and the tag goes stale within weeks. What makes people tap on Home is mostly the icon and the thumbnails. Our pick: launch as plain Clean a Cat and put the word new in the description's update line and on event cards. If you want to know for sure, the second option tries the tag after launch for one clean week and compares it with the week before. A title cannot be split between players, so that is a before and after read and one weak reason at best. Your answer on November 24: probably not, you never see it on top games in popular or trending. So it is plain Clean a Cat.",
             opts=["Plain Clean a Cat, new goes in the description", "Try the tag after launch for one week", "[NEW] in the name from day one", ELSE]),
    ]),
    ("Money and events", "Planning-Agent and Growth-Agent", "", [
        dict(id="passes", t="Three game passes, and coins, helpers and rare cats are never sold",
             d="2x Coins, Second Builder and Golden Sponge, a wider scrub with gold bubbles. Coins cannot be bought, so the random customer never counts as a paid random item. Nothing sold changes the chances, and the chance of every cat is always on a board. Your screenshots show how hard My Pet Salon sells: a starter pack on the main screen from the first minute, a limited pack with an Only 82 left counter, cash for Robux and a paid upgrade that maxes every worker. We stay with no offer on screen in the first session, no stock counters and no coins for Robux. You said on November 24 that a starter pack might not be a bad idea, so it has its own question next. Pet Store Tycoon's Robux shop has seven tabs: featured, staff, boosts, pet packs, secret, upgrades and cash. Ours stays one short list. Its one idea worth keeping for later is a gift button beside each price, so a player can buy a pass for a friend.",
             opts=[YES, ELSE]),
        dict(id="starterpack", t="One starter pack, shown once, with fixed contents",
             d="You sent the Grand Opening Bundle that Pet Store Tycoon shows after day 2 and said it might not be a bad idea for starter packs. Theirs: a pet pack with three random pets, 10,000 cash and an hour of double coins for 99 Robux, with a crossed out price of 198 and a 50% off tag. It has one close button and no countdown, which is the calm part worth taking. Three things in it do not fit our rules as they stand. A random pack bought with Robux is a paid random item, and you said crates are earned and never sold. Coins for Robux would make everything coins buy count as paid. A crossed out price is only fair if it really was the price. Our pick keeps the idea and drops those three: one Spa Starter Pack with fixed contents you can see, such as a special look for your tub, a bandana for Suds and one hour of double tips. It has a plain price, no countdown and no stock counter. Growth-Agent checked it against Roblox's pages on November 24 and it fits their rules and ours. Two things came out of that check. The price: 99 Robux, the same as the bundle you saw, with 49 as the fall back if few players buy. Roblox publishes no guide price, so that is a judgment. The moment: not in the first visit at all. Our own rule keeps pop ups out of the first session, because that is what Roblox judges a new game on. So it shows once at the start of your second visit, after Suds has shown you the tip jar, never over a wash. A no is final for that visit and after that it sits in the shop. That is close to what Pet Store Tycoon does, which waits until its day 2. It is built behind a switch that starts off.",
             opts=["Yes, fixed contents for 99 Robux, shown once on your second visit", "Same pack, plus one crate with the chances shown on it", "Only in the shop, no pop up", "No starter pack at launch", ELSE]),
        dict(id="event", t="A Cat Show weekend as your first event",
             d="Day 7 is yours. A themed show with voting is the natural first event. It is not part of the first build. Pet Store Tycoon runs a named event on a strip at the bottom of the screen that raises demand for one kind of pet, a Goldfish Derby with 60% more fish demand, and a button that counts down the days left. That is a light kind of event to run between the big ones: for a few days one kind of dirty cat tips more.",
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
TODAY = [
    ("The opening", "A quick intro you watch, about 4 seconds: a truck goes by and a plain brown box falls in front of you. It starts the moment your character loads, with no loading screen and no standing still. Then the camera is yours."),
    ("The carry and the wash view", "You lift the muddy kitten out of the box and carry him to the tub. Placing him in the tub switches to a close up wash view, where the steps are taught. Your example of the hold is in, a clip and six pictures from Catch a Cat Cafe."),
    ("Suds", "The kitten becomes Suds once he is clean. He is the mascot, walks on four paws, never washes and is not in the index. Human staff do the washing."),
    ("Prompt buttons", "You noticed that the big black buttons block the view on a phone, in My Pet Salon and in ours when you pick the kitten up out of the box. Ours are being replaced with a small button in our own look, starting with the box."),
    ("No tool menu in the wash", "The game changes to the right tool for each step by itself, as My Pet Salon does. You never pick a tool. Gameplay-Engineer has the build."),
    ("Playtests closed", "Nine games played. Clean the Animal Daycare was the last, and you found it pretty much the same as Clean Everything and unrelated. No more are needed."),
    ("From your to-do list", "No friends as customers. The notification ask comes 1 to 2 minutes in. Suds explains in a bubble along the bottom. Plain Clean a Cat with no [NEW] tag. Washed cats fill an index. Crates are earned, hard to get and worth it, and the free one on day 2 is a good one. The kitten's eyes stay open while you carry him. A pet for you and one for each worker is the working plan and may change."),
    ("Dev first", "Everything is uploaded to the dev place first. Nothing goes to the live game until you confirm it is good, and the feature switches stay off on live."),
    ("Playing like My Pet Salon", "Fine by you. We stop steering away from it and aim to do each part better."),
    ("Open on purpose", "The playstyle. You wrote that we will sort it out later, and the playtests are now done, so it is the first thing on your to-do list."),
    ("Jobs you finished", "The rule on the main branch, saves for Studio in the dev copy, the loop write-up, the 14 draft screens, your test devices (an iPhone 12 and an iPad from about 2020), two minutes of our scrub and the example of how the kitten is held."),
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

def shots_html(g):
    if not g.get("shots"):
        return ""
    return '<ol class="shots">' + "".join(f"<li>{e(x)}</li>" for x in g["shots"]) + "</ol>"

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
  <p><strong>Look for.</strong> {e(g["look"])}</p>{shots_html(g)}
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
    note = f'<textarea class="tnote" id="{d}__note" data-doc="{d}" data-key="note" rows="2" placeholder="Write your answer here, or not needed" aria-label="Your answer: {e(t["t"])}"></textarea>'
    if t.get("q"):
        qd = "q2-" + t["q"]
        return f'''
<li class="todo">
  <input type="checkbox" id="{d}__done" data-q="{qd}" data-note="{d}" aria-label="Answered: {e(t["t"])}">
  <div class="tbody">
    <label for="{d}__done"><strong>{e(t["t"])}</strong><span>{e(t["d"])} <a href="#{qd}">Go to the pick</a>. It ticks itself when you pick, or when you write in the box.</span></label>
    {note}
  </div>
</li>'''
    link = f' <a href="{t["link"][0]}" target="_blank" rel="noopener">{e(t["link"][1])}</a>' if t.get("link") else ""
    return f'''
<li class="todo">
  <input type="checkbox" id="{d}__done" data-doc="{d}" data-key="done">
  <div class="tbody">
    <label for="{d}__done"><strong>{e(t["t"])}</strong><span>{e(t["d"])}{link}</span></label>
    {note}
  </div>
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
themes_html = "".join(f'<li><strong>{e(a)}</strong><span>{e(b)}</span></li>' for a, b in THEMES)
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
today_html = "".join(f"<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>" for a, b in TODAY)

OLD_FIELDS = [("sel", "pet", "pet", PET_OPTS), ("txt", "fun", "first fun at (s)", ""), ("sel", "wash", "washing", WASH_OPTS), ("sel", "wait", "waits", WAIT_OPTS)]
def jf(fields):
    return [dict(k=f[1], label=f[2], opts=(f[3] if f[0] == "sel" else None)) for f in fields]
DATA = dict(
    main=[dict(id="p-" + g["id"], name=g["name"], fields=jf(g["fields"])) for g in GAMES],
    other=[dict(id="p-" + g["id"], name=g["name"], fields=[]) for g in OPTIONAL_GAMES]
          + [dict(id="p-" + g["id"], name=g["name"] + g.get("tag", " (round one)"), fields=jf(OLD_FIELDS)) for g in DONE_GAMES],
    todos=[dict(id="c-" + t["id"], t=t["t"], q=("q2-" + t["q"]) if t.get("q") else None) for _, items in TODOS for t in items],
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
.shots{margin:0 0 4px;padding-left:22px;display:flex;flex-direction:column;gap:6px;font-size:.95rem}
.todo input[data-q]{cursor:pointer}
.tbody{display:flex;flex-direction:column;gap:8px;min-width:0;flex:1}
.todo input:checked+.tbody strong{text-decoration:line-through;text-decoration-color:var(--mint)}
.tnote{width:100%;box-sizing:border-box;border:1px solid var(--line);border-radius:10px;padding:8px 10px;background:var(--surface);color:var(--ink);font:inherit;font-size:.95rem;resize:vertical;min-height:44px}
.tnote:focus{outline:2px solid var(--mint);outline-offset:1px}
.gapnote{background:var(--gum-bg);border-radius:12px;padding:12px 14px;font-size:.94rem}
'''

PAGE = r'''<title>Clean a Cat Launch Plan</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600&family=Nunito+Sans:opsz,wght@6..12,400;6..12,600;6..12,700&display=swap">
<style>__CSS__</style>

<div class="wrap">
  <div class="intro">
    <p class="eyebrow">Clean a Cat, final questions, November 24</p>
    <h1>What is left before we build</h1>
    <p class="lede">The final list, November 24 in the evening. The playtests are done: nine games played and no more are needed. Nothing else is needed from you except picks. Every question has our pick first, so each one is a tap. What you decided today is <a href="#today">near the bottom</a>.</p>
    <ol class="steps">
      <li><a href="#q2-loop">Pick the playstyle</a>. Our pick: your busy spa and the cat collection together.</li>
      <li><a href="#todo">Your to-do list</a>: six more picks that decide the game, four new ones, then the rest in one press.</li>
      <li><a href="#questions">Tap through __NQ__ picks</a>. The first twelve decide the game. Then say done.</li>
    </ol>
  </div>

  <nav class="bar" aria-label="Progress">
    <a class="pill full" href="#playtests" id="pill-play">Playtests <b>all 9 done<span id="n-play" hidden>0</span></b></a>
    <a class="pill" href="#todo" id="pill-todo">To do <b><span id="n-todo">0</span> of __NT__</b></a>
    <a class="pill" href="#questions" id="pill-q">Picks <b><span id="n-q">0</span> of __NQ__</b></a>
    <span class="status" id="status" role="status">Loading your answers</span>
  </nav>

  <section id="playtests">
    <header>
      <h2>Playtests</h2>
      <p>Nine games are played and saved, and the playtests are closed. Below is what they told us and what we took from each. Nothing to do here.</p>
    </header>
    <h3 class="group">What the games told us</h3>
    <ul class="saved">__THEMES__</ul>
    __GAMES__
    <p class="fine"><strong>More playtests: none.</strong> Nine games cover the wash, the first minute, workers, pets, things to chase and selling, and the last two added little that was new. What we still do not know, such as whether our own scrub feels good and how long a cat should take, only your test of our draft in the dev place can answer. Dropped from the old list because the games you played already answer them: Clean The Ballpit, Wash the Pets, Clean an Animal, Wash a Cat, Wash the Car, Throw Food For Animals and Steal An Egg. We searched Roblox again on the evening of November 24 for pet spa, salon and wash games. Besides My Pet Salon, none has more than about 25 players, so nothing else earns a playtest.</p>
    <h3 class="group">Played and saved</h3>
    <ul class="saved">__DONE__</ul>
  </section>

  <section id="todo">
    <header>
      <h2>Your to-do list</h2>
      <p>Everything still open is here, in the order that helps most, and all of it is picks. An item ticks itself when you answer its question. Every item has a box: write your answer there when it is not a simple pick. What you write is saved like your picks and the team reads it. Jobs you finished are saved under Decided on November 24.</p>
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

  <section id="today">
    <header><h2>Decided on November 24</h2><p>What you settled today and what you left open on purpose. Nothing to do here.</p></header>
    <dl class="decided">__TODAY__</dl>
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
    DATA.todos.forEach(function(t){ if (t.q ? (has((state[t.q] || {}).pick) || has((state[t.id] || {}).note)) : (state[t.id] || {}).done === true) todo++; });
    document.querySelectorAll("input[data-q]").forEach(function(el){ el.checked = has((state[el.dataset.q] || {}).pick) || has((state[el.dataset.note] || {}).note); });
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
    if (k === "note" && doc.indexOf("c-") === 0 && has(v) && state[doc].done !== true) {
      var box = document.getElementById(doc + "__done");
      if (box && box.dataset.doc) { state[doc].done = true; box.checked = true; }
    }
    changed(doc, (el.type === "text" || el.tagName === "TEXTAREA") ? 900 : 150);
  }
  document.addEventListener("input", onInput);
  document.addEventListener("change", onInput);
  document.addEventListener("click", function(ev){
    var el = ev.target;
    if (el && el.matches && el.matches("input[data-q]")) {
      ev.preventDefault();
      var a = document.getElementById(el.dataset.q);
      if (a) a.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  });

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
    L.push("", "TO DO, DONE OR ANSWERED");
    DATA.todos.forEach(function(t){
      var d = state[t.id] || {};
      if ((!t.q && d.done === true) || has(d.note)) L.push("- " + t.t + (has(d.note) ? ": " + d.note : ""));
    });
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
        .replace("__THEMES__", themes_html).replace("__GAMES__", games_html).replace("__OPT__", opt_html).replace("__DONE__", done_html)
        .replace("__TODAY__", today_html).replace("__TODOS__", todos_html).replace("__PARKED__", parked_html).replace("__QUESTIONS__", q_html)
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
M.append("## 1. Playtests: closed, nine played, none left and none more wanted (final list of 2026-11-24 evening ET)")
M.append("")
M.append("**What the games told us**")
for a, b in THEMES:
    M.append(f"- **{a}.** {b}")
M.append("")
M.append("Player counts are from the evening of November 24, 2026.")
M.append("")
M.append("| Game (id) | Time | Players and votes | Why it is on the list | Look for |")
M.append("|---|---|---|---|---|")
for g in GAMES:
    M.append(f"| [{g['name']}]({g['url']}) (`{g['id']}`) | {g['mins']} | {g['stats']} | {g['why']} | {g['look']}{' ' + ' / '.join(g['shots']) if g.get('shots') else ''} |")
M.append("")
M.append("Notes in words are enough. No more screenshots or recordings are asked for.")
M.append("- Dropped from the old list: Clean The Ballpit, Wash the Pets, Clean an Animal, Wash a Cat, Wash the Car, Throw Food For Animals and Steal An Egg.")
M.append("")
M.append("**Played and saved**")
for g in DONE_GAMES:
    M.append(f"- {g['name']}: {g['took']}")
M.append("")
M.append("## 2. Derek's to-do list (open jobs only)")
for title, items in TODOS:
    M.append("")
    M.append(f"**{title}**")
    for t in items:
        link = f" [{t['link'][1]}]({t['link'][0]})" if t.get("link") else ""
        qn = f" Linked to question `{t['q']}`, ticks itself when answered." if t.get("q") else ""
        M.append(f"- [ ] **{t['t']}** (`{t['id']}`). {t['d']}{link}{qn}")
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
M.append("## Decided on November 24")
for a, b in TODAY:
    M.append(f"- **{a}:** {b}")
M.append("")
M.append("## Saved from round one")
for a, b in SAVED + DECIDED:
    M.append(f"- **{a}:** {b}")
M.append("")
M.append("## What happens when Derek is done")
M.append("Planning-Agent reads the answers from the page, folds them and the playtest notes into `gdd-draft.md`, asks for the design lock, finishes `milestone-1.md` and hands over to the coordinator.")
open(OUT_MD, "w", encoding="utf-8").write("\n".join(M) + "\n")
print("questions", NQ, "todos", NT, "games", NG, "html bytes", len(page))
