#!/usr/bin/env python3
"""Builds the pre-development plan for Derek: an HTML page and a Markdown copy from one data set."""
import html, json, sys

OUT_HTML = sys.argv[1]
OUT_MD = sys.argv[2]
REPO = "https://github.com/derekburnz/Clean-a-Cat"

# ---------------------------------------------------------------- playtests
NOTE_PROMPTS = [
    "How do you get a pet, and how many seconds does it take?",
    "Seconds from spawn until you first did something fun.",
    "Is the washing done by hand (drag, scrub, hold) or by one button?",
    "Seconds until the first reward and the minute of your first upgrade.",
    "Any build or wait timers, and how the wait felt.",
    "What the game told you to do next at minute 1, minute 3 and minute 5.",
    "The first pop-up, shop prompt or Robux offer and when it came.",
    "The moment you got bored or confused, if any.",
    "What it does well, what we should do better and whether you would open it again tomorrow.",
]
EXTRA_PROMPTS = [
    ("Art", "How the dirty and clean looks differ (mud patches, colour change, sparkle) and whether the reveal felt good."),
    ("Effects and sound", "Which washing, reveal or sound moment felt best."),
    ("Screens", "Did any window open by itself? How does the tutorial point (arrows, text, dimming)? Where do the main buttons sit on a phone?"),
    ("Camera", "What the camera does while you care for the pet."),
    ("Screenshot", "One screenshot of each game's phone screen helps the most."),
]
GAMES = [
    dict(id="capybara", name="Capybara Onsen", url="https://www.roblox.com/games/120336108521610",
         stats="368 playing, 97% liked of about 59K votes",
         why="The most played and best liked animal spa game on Roblox.",
         look="What you do with your hands, how capybaras arrive, what you build or unlock and why it holds a few hundred players and not thousands."),
    dict(id="petsalon", name="My Pet Salon!", url="https://www.roblox.com/games/134135989047078",
         stats="175 playing, 86% liked of about 930 votes",
         why="Our closest rival. Its page promises wash, brush, dry and cuddle for customers' pets.",
         look="Whether customers bring the pets, how each step is done, how long one pet takes and what the stations and levels add."),
    dict(id="horse", name="Save a Horse: Wash & Collect", url="https://www.roblox.com/games/119493855221779",
         stats="36 playing, 90% liked of about 1.4K votes",
         why="The only game found that joins washing to collecting, which is our mix.",
         look="How you get a horse, whether washed horses are kept and earn and how the collection is shown."),
]
OPTIONAL_GAMES = [
    dict(id="washpets", name="Wash the Pets", url="https://www.roblox.com/games/106050444354181",
         look="The feel of the washing and how fast it gets dull."),
    dict(id="cleananimal", name="Clean an Animal!", url="https://www.roblox.com/games/75217712603520",
         look="Why 17% disliked it: bugs, waits or pay walls."),
    dict(id="washacat", name="Wash a Cat", url="https://www.roblox.com/games/87832865714820",
         look="Two minutes is enough. What it is and whether it is any good."),
    dict(id="throwfood", name="Throw Food For Animals", url="https://www.roblox.com/games/120219252362013",
         look="The first minute we want to match: how fast the first animal is yours, the first three prices and how it points to the next goal."),
]
PET_OPTS = ["Handed to you at spawn", "A customer brings it", "You go and find it", "You buy it", "You hatch it", "Something else"]
WASH_OPTS = ["By hand (drag, scrub, hold)", "One button press", "No real washing"]
WAIT_OPTS = ["No timers seen", "Short waits, fine", "Long waits, annoying", "Long waits, but I wanted to come back"]

# ---------------------------------------------------------------- to-dos
TODOS = [
    ("Now, so building is not blocked", [
        dict(id="group-id", t="Send the Creampuff Games group id",
             d="Done. The group id is 107520049."),
        dict(id="experience", t="Create the experience under the group and send its two ids",
             d="Done. Universe id 10778773655 and start place id 79301459457383. An experience is Roblox's word for a game, the universe id names the whole game and the place id its first map."),
        dict(id="devplace", t="Make a dev copy of the place",
             d="Done: Clean-a-Cat-Dev. No extra key is needed for it. Studio on your PC signs in as you, and your keys already cover it. Still to tick in the dev copy: Game Settings, Security, Enable Studio Access to API Services, so saves and switches work in Studio."),
        dict(id="pc", t="Get the PC ready for Studio work",
             d="You gave the go-ahead. Sync-Agent is checking DESKTOP-DFOGFG7 through Remote Control and installing what is missing (Git, Rokit, the Rojo plugin and the repo under Downloads). Nothing for you unless it gets stuck.",
             link=(REPO + "/blob/main/docs/setup-guide.md", "Setup guide, steps 2 to 5")),
        dict(id="sounds", t="Listen to the 11 sounds (about 2 minutes)",
             d="Done. You said they are fine for now and tuning waits until the gameplay is decided."),
    ]),
    ("Before the first publish", [
        dict(id="key", t="Create the Open Cloud key and paste it into GitHub",
             d="Done. You saved it as OWNER_KEY. Our workflows looked for the name ROBLOX_PUBLISH_KEY, so we changed them to accept yours. Nothing more for you.",
             link=(REPO + "/pull/110", "Pull request 110")),
        dict(id="vars", t="Add the three repo variables",
             d="Done on our side. The three ids are public, so they are now built into the workflows and you do not need to add them.",
             link=(REPO + "/pull/110", "Pull request 110")),
        dict(id="groupkey", t="Optional: a second key for uploads",
             d="Done. You saved it as ROBLOX_GROUP_KEY, which is the name the upload workflows read first."),
        dict(id="automerge", t="Check the rule that makes pull requests wait for their tests",
             d="Auto-merge is on, thank you, and pull requests have been merging only after both test runs pass. We cannot see the repo rules from here, so one look from you settles it. In the Clean-a-Cat repo open Settings, Rules, Rulesets. If an active rule for main lists these two checks, tick this job: Rojo sourcemap, luau-lsp, Selene, StyLua and Unit tests, strict types, UI gate. If the list is empty, make one: New ruleset, New branch ruleset, name it main, set Enforcement status to Active, under Target branches choose Include default branch, tick Require a pull request before merging, tick Require status checks to pass and add the two checks by name, then press Create. About 2 minutes.",
             link=(REPO + "/blob/main/docs/setup-guide.md#9-required-check-and-auto-merge", "Setup guide, step 9")),
        dict(id="serversize", t="Set the server size to match the street",
             d="You said this waits until the game design and playtests are done. When the number is decided, set the maximum players per server to match in the experience settings.",
             link=(REPO + "/issues/88", "Issue 88")),
        dict(id="scrub", t="Play the scrub prototype on your phone",
             d="You said no prototypes until the playtests and the research on hooks and loops are done. This stays parked until then.",
             link=(REPO + "/issues/29", "Issue 29")),
    ]),
    ("Before build notifications go on", [
        dict(id="notify-message", t="Later: write the text of the build finished notification",
             d="Only needed if we keep the idea of telling players when a long build is done. Roblox does not let a game send any text it likes. You write the sentence once in the Creator Dashboard (Engagement, Notifications), for example: Your {buildName} is finished and the cats are waiting. Roblox gives that sentence an id and we need the id. It is not secret. Park this until the gameplay is decided.",
             link=(REPO + "/pull/90", "Pull request 90")),
        dict(id="notify-key", t="Later: a key the game itself uses to send that notification",
             d="This is separate from your two GitHub keys. GitHub cannot hand a key to a running game, so this one is saved inside Roblox: Creator Dashboard, your experience, Secrets, under the name CleanACat_NotifyKey. It needs only user notification write access. Park this until the gameplay is decided, and never share the key.",
             link=(REPO + "/pull/90", "Pull request 90")),
    ]),
    ("Before the first public test: Roblox Kids and Select", [
        dict(id="agecheck", t="Creator account age-checked and verified, with 2-step verification",
             d="Done."),
        dict(id="plus", t="An active Plus or Premium subscription, or the one-time fee",
             d="You said this is not needed. If Roblox asks for it when we apply for Kids and Select, we will tell you then."),
        dict(id="questionnaire", t="Fill in the full maturity questionnaire",
             d="You said this waits until the gameplay is decided. We write down the answers for you first. The game needs a Minimal or Mild result."),
        dict(id="plays", t="100 plays from highly engaged players within 60 days",
             d="You said ads for this come after the game is ready for more public testers. Roblox shows a new game only to age-checked players of 16 and over until it passes this evaluation."),
    ]),
    ("At release", [
        dict(id="storeart", t="OK the final icon and thumbnails before upload",
             d="A later problem, as you said. The draft picks are in the Store art questions at the end of this page.",
             link=(REPO + "/issues/24", "Issue 24")),
        dict(id="private", t="Make both repos private",
             d="A later problem, as you said, and maybe not needed until the game gets popular."),
    ]),
]
KIDS_NOTE = "Read on Roblox's Kids and Select page on November 23, 2026. Roblox changes these rules, so check the page again before acting."

# ---------------------------------------------------------------- questions
YES = "Yes, go with it"
QUESTIONS = [
    ("The game", "Planning-Agent", [
        dict(id="cats", t="Customers bring dirty cats and strays stay with you",
             d="People queue at the door holding a dirty cat. A board shows which cats can come and the chance of each. Now and then a stray turns up at the back door, and once clean it lives in your display window. The very first cat is a stray, so every player owns a cat inside the first minute. No catching.",
             opts=[YES, "Customers only, no strays", "Something else"],
             note="Your playtests decide this one. See how the three games hand you a pet."),
        dict(id="slots", t="Two build slots",
             d="The builder kitten builds one station at a time (seconds up to 1 hour). A building site builds one room at a time (hours). With one slot a first session never reached the 8 hour build, and once it ran nothing else could be built for 8 hours.",
             opts=[YES, "One build at a time", "Something else"]),
        dict(id="longest", t="Longest build is 24 hours and the first 8 hour build starts in the first session",
             d="Tools are instant. Then 10 seconds, 1 minute, 10 minutes and 1 hour for stations. The VIP Room takes 8 hours and is offered at about minute 6. Later rooms take 12 to 24 hours and never longer. A finished build waits for the player and nothing is lost by coming back late.",
             opts=[YES, "Shorter, 12 hours at most", "Longer builds are fine", "Something else"]),
        dict(id="skips", t="No paid skips for build timers at launch",
             d="We sell a Second Builder pass instead. Paid skips on timers read as pressure for a young audience and reviewers of spa games complain about them most.",
             opts=["Yes, no paid skips", "Sell skips at launch", "Something else"]),
        dict(id="prices", t="Starting prices and pay",
             d="A common cat pays 10 coins plus a tip of 2. Bubble Soap 30, Brush Table 40, dryer 75, VIP Room 100. A window cat tips 1 coin every 10 seconds and the away jar holds 1 hour of tips. This gives a purchase at about minute 2, 3 and 5 and the long build near minute 8. Paper numbers until the scrub is timed on a phone.",
             opts=[YES, "Something else"]),
        dict(id="street", t="A shared street with one spa each",
             d="Spas sit side by side so players see each other's windows and reveals. Not in the game: stealing, trading, fighting and typed text. Cat names come from a list. How many spas and whether players can walk in are the last two questions.",
             opts=[YES, "Something else"]),
        dict(id="passes", t="Three game passes at launch and coins cannot be bought",
             d="2x Coins, Second Builder and Golden Sponge (a wider scrub with gold bubbles). No buyable coins, so the random customer never counts as a paid random item. Nothing sold changes the chances.",
             opts=[YES, "Something else"]),
        dict(id="catspa", t="Put the words cat spa in the description and on the icon",
             d="Your cat spa ad did well. The title stays Clean a Cat.",
             opts=[YES, "Title only, no cat spa wording", "Something else"]),
        dict(id="event", t="A Cat Show weekend as your first event",
             d="Day 7 is yours. A themed show with voting is the natural first event. It is out of scope for the first build.",
             opts=["Yes, plan it for later", "I have a different event in mind", "Something else"]),
    ]),
    ("The first minutes and screens", "Design-Agent", [
        dict(id="bell", t="Notifications are asked for with a bell button",
             d="The player taps a bell beside any build over 1 hour. No prompt opens by itself. Only players of 13 and over can get these messages, so younger players see Ready in 8 h. Come back to see it!",
             opts=["Yes, the bell", "A prompt after the first long build starts", "Something else"]),
        dict(id="bows", t="Pick a bow on every cat",
             d="One tap to finish each cat with one of three bows.",
             opts=["Yes, every cat", "Only the first cat", "Something else"]),
        dict(id="camera", t="A close camera at the tub with the thumbstick hidden on phones",
             d="While washing, the camera moves in on the cat and the move stick hides so the whole screen is for scrubbing.",
             opts=[YES, "Keep the normal camera", "Something else"]),
        dict(id="shop", t="Hide the Shop button until the first build is done",
             d="Keeps the first three minutes about the cat. Roblox counts players who leave in that window.",
             opts=[YES, "Show the Shop from the start", "Something else"]),
        dict(id="landscape", t="Lock phones to landscape",
             d="One layout to get right, with more room for the tub and the tools.",
             opts=[YES, "Allow portrait too", "Something else"]),
    ]),
    ("The look", "Model-Agent", [
        dict(id="style", t="Art style",
             d="Bubble Pastel colours (cream, mint, bubblegum, sky and dark mud) on the blocky chibi cat body from your asset library. It reads on phones, needs no mesh uploads and makes the mud pop.",
             opts=["Yes, Bubble Pastel on the library body", "Cozy Storybook (warm wood, painted textures)", "Bright Toy (saturated, glossy)", "Something else"]),
        dict(id="body", t="Reuse the Cat Cafe cat body with all new coats",
             d="Same body shape, new coats and names, plus spa extras (mud, fluff and bows). No Cat Cafe character is reused.",
             opts=[YES, "Make the cats look clearly different from Cat Cafe", "Something else"]),
        dict(id="names", t="Ten working cat names for the first Cat Index",
             d="Muffin, Smudge (the first stray), Inky, Cotton, Tux, Patches, Toffee, Marble, Lilac Cloud and Starcoat. None is used in Cat Cafe.",
             opts=["Yes, use these", "I want to name them", "Something else"]),
        dict(id="size", t="Cats bigger than life",
             d="About half an avatar's height, so the cat fills the screen at the tub on a phone.",
             opts=[YES, "Something else"]),
    ]),
    ("Sound and feel", "Motion-FX-Agent", [
        dict(id="feel", t="The feel of the cleaning",
             d="Soft and cosy means pastel bubbles, gentle sounds and small sparkles. Splashy and cartoony means big suds and bouncy pops.",
             opts=["Soft and cosy", "Splashy and cartoony", "Something else"]),
        dict(id="soundreuse", t="Reuse the purr and meow sound code and make two new music tracks",
             d="The purr and meow code comes from your asset library. The music is new, from the same generator, so Clean a Cat has its own.",
             opts=[YES, "All new sounds", "Something else"]),
        dict(id="upload", t="Upload about 15 short sounds and 2 music tracks under the group",
             d="As one batch, after you have listened. It uses some of the monthly audio upload quota.",
             opts=["Yes, as one batch after I listen", "Not yet", "Something else"]),
    ]),
    ("The street", "Gameplay-Engineer", [
        dict(id="streetsize", t="Spas per street, which is also the server size",
             d="Each server is one street and every player gets their own spa plot on it. Six keeps the street lively, keeps every window close enough to see and stays light on cheap phones. You set the same number as the server size in the experience settings.",
             opts=["6 spas per street", "4 spas", "8 spas", "Something else"]),
        dict(id="visit", t="Can players walk into a neighbour's spa?",
             d="Our pick: players see each other's windows and reveals from the street but cannot walk in. Walking in is built behind a switch that stays off, so friends helping in your spa can be turned on later without a rebuild. It keeps the first build simple and stops a crowd standing on someone's tub.",
             opts=["Look through the window only", "Walk in from the start", "Something else"]),
    ]),
    ("Store art", "Model-Agent", [
        dict(id="icon", t="Pick the icon",
             d="The icon is the small square players see on Home and in search, often at only 48 pixels. Icon B shows the whole muddy cat with the sponge and keeps the name readable when small. Rendered from the real models. Nothing is uploaded until you say so.",
             imgs=[("art/icon-b.jpg", "Icon B: an orange muddy cat with a sponge on blue, with the words CLEAN A CAT", "B: the whole cat, with the name"),
                   ("art/icon-a.jpg", "Icon A: a grey muddy cat being scrubbed in a tub on pink, no words", "A: the scrub, no words"),
                   ("art/icon-c.jpg", "Icon C: a clean white cat with a pink bow in a foamy tub on pink, no words", "C: clean and fluffy, no words")],
             opts=["Icon B", "Icon A", "Icon C", "Something else"]),
        dict(id="thumbs", t="Pick the thumbnails",
             d="Thumbnails are the wide pictures on the game's page and on Home. Roblox can rotate a set and show which one wins the most taps, so more than one is useful. Thumbnail 1 shows the scrub and thumbnail 2 shows muddy to fluffy, which are both things a new player does in the first minute.",
             imgs=[("art/thumb-1.jpg", "Thumbnail 1: a player scrubbing a grey cat at the tub on blue, with the words CLEAN A CAT", "1: scrubbing at the tub"),
                   ("art/thumb-2.jpg", "Thumbnail 2: a muddy orange cat, an arrow and the same cat clean with a bow on pink, with the words CLEAN A CAT", "2: muddy to fluffy"),
                   ("art/thumb-3.jpg", "Thumbnail 3: two customers with cat carriers waiting while a player scrubs a cat on green, no words", "3: your spa at work, no words")],
             wide=True,
             opts=["Thumbnails 1 and 2", "All three", "A different set", "Something else"]),
    ]),
]
DECIDED = [
    ("Name", "Clean a Cat, locked November 23. Slug clean-a-cat."),
    ("Direction", "A hands-on cat spa: clean dirty cats, earn, upgrade the spa. No catching."),
    ("Goals", "A fun first 5 minutes for a very low bounce rate and a reason to come back on day 2. You handle day 7 with events."),
    ("Repos", "Public for now, private at release."),
    ("How we work", "Every passing pull request merges itself. Publishing is silent. Restarts are fine until public release."),
]

def e(s):
    return html.escape(s, quote=True)

# ================================================================= HTML
def sel(idv, label, opts):
    o = '<option value="">Choose</option>' + "".join(f'<option value="{i}">{e(x)}</option>' for i, x in enumerate(opts))
    return f'<label class="field"><span>{e(label)}</span><select id="{idv}" data-doc="{idv.rsplit("__",1)[0]}" data-key="{idv.rsplit("__",1)[1]}">{o}</select></label>'

def game_card(g, n):
    d = "p-" + g["id"]
    return f'''
<article class="game" id="game-{g["id"]}">
  <header>
    <span class="num">{n}</span>
    <div class="gh">
      <h3><a href="{g["url"]}" target="_blank" rel="noopener">{e(g["name"])}</a></h3>
      <p class="stats">{e(g["stats"])}</p>
    </div>
    <label class="played"><input type="checkbox" id="{d}__played" data-doc="{d}" data-key="played" data-count="play"><span>Played</span></label>
  </header>
  <p><strong>Why it is on the list.</strong> {e(g["why"])}</p>
  <p><strong>Look for.</strong> {e(g["look"])}</p>
  <div class="fields">
    {sel(d+"__pet", "How do you get a pet?", PET_OPTS)}
    <label class="field"><span>Seconds to the first fun thing</span><input type="text" inputmode="numeric" id="{d}__fun" data-doc="{d}" data-key="fun" placeholder="for example 20"></label>
    {sel(d+"__wash", "The washing is", WASH_OPTS)}
    {sel(d+"__wait", "Timers and waits", WAIT_OPTS)}
  </div>
  <label class="field wide"><span>Your notes</span><textarea id="{d}__notes" data-doc="{d}" data-key="notes" rows="4" placeholder="What it does well, what we should do better, what made you want to stop, would you open it tomorrow"></textarea></label>
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
  <input type="checkbox" id="{d}__done" data-doc="{d}" data-key="done" data-count="todo">
  <label for="{d}__done"><strong>{e(t["t"])}</strong><span>{e(t["d"])}{link}</span></label>
</li>'''

def question(q, n):
    d = "q-" + q["id"]
    opts = ""
    for i, o in enumerate(q["opts"]):
        rec = '<em>Recommended</em>' if i == 0 else ""
        opts += f'<label class="opt"><input type="radio" name="{d}" id="{d}__pick{i}" value="{i}" data-doc="{d}" data-key="pick" data-count="q"><span>{e(o)}{rec}</span></label>'
    note = f'<p class="qnote">{e(q["note"])}</p>' if q.get("note") else ""
    if q.get("imgs"):
        figs = "".join(f'<figure><img src="{src}" alt="{e(alt)}" loading="lazy"><figcaption>{e(cap)}</figcaption></figure>' for src, alt, cap in q["imgs"])
        note += f'<div class="art{" wide" if q.get("wide") else ""}">{figs}</div>'
    return f'''
<article class="q" id="{d}">
  <h3><span class="qn">{n}</span>{e(q["t"])}</h3>
  <p>{e(q["d"])}</p>{note}
  <div class="opts" role="radiogroup" aria-label="{e(q["t"])}">{opts}</div>
  <input type="text" class="qtext" id="{d}__note" data-doc="{d}" data-key="note" placeholder="Anything to add (optional)" aria-label="Note on: {e(q["t"])}">
</article>'''

parts = []
games_html = "".join(game_card(g, i + 1) for i, g in enumerate(GAMES))
opt_html = "".join(opt_game(g) for g in OPTIONAL_GAMES)
prompts_html = "".join(f"<li>{e(p)}</li>" for p in NOTE_PROMPTS)
extra_html = "".join(f"<li><strong>{e(a)}.</strong> {e(b)}</li>" for a, b in EXTRA_PROMPTS)
todos_html = ""
for title, items in TODOS:
    note = f'<p class="fine">{e(KIDS_NOTE)}</p>' if "Kids and Select" in title else ""
    todos_html += f'<h3 class="group">{e(title)}</h3><ul class="todos">{"".join(todo_item(t) for t in items)}</ul>{note}'
q_html = ""
n = 0
for title, who, items in QUESTIONS:
    block = ""
    for q in items:
        n += 1
        block += question(q, n)
    q_html += f'<h3 class="group">{e(title)} <small>from {e(who)}</small></h3>{block}'
NQ = n
NT = sum(len(i) for _, i in TODOS)
decided_html = "".join(f"<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>" for a, b in DECIDED)

DATA = dict(
    games=[dict(id="p-" + g["id"], name=g["name"]) for g in GAMES + OPTIONAL_GAMES],
    pet=PET_OPTS, wash=WASH_OPTS, wait=WAIT_OPTS,
    todos=[dict(id="c-" + t["id"], t=t["t"]) for _, items in TODOS for t in items],
    qs=[dict(id="q-" + q["id"], t=q["t"], opts=q["opts"]) for _, _, items in QUESTIONS for q in items],
)

PAGE = r'''<title>Clean a Cat Launch Plan</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600&family=Nunito+Sans:opsz,wght@6..12,400;6..12,600;6..12,700&display=swap">
<style>
/* Layout: one reading column on a tiled spa floor; a sticky bar of three counters; mud is ink, mint means done, bubblegum marks our pick. */
:root{
  --bg:#FFF6EC; --surface:#FFFFFF; --ink:#3A2C20; --soft:#7A6656; --line:#EBDCCB;
  --mint:#2F9E7A; --mint-bg:#DDF5EA; --gum:#C8436E; --gum-bg:#FFE3EC; --sky:#1F6FA8; --sky-bg:#E2F2FE; --mud:#5A4632;
  --display:"Fredoka","Trebuchet MS",system-ui,sans-serif; --body:"Nunito Sans","Segoe UI",system-ui,sans-serif;
}
@media (prefers-color-scheme: dark){ :root:not([data-theme="light"]){
  --bg:#211912; --surface:#2C2219; --ink:#FBEFE2; --soft:#C4AF9C; --line:#46372A;
  --mint:#7FDDB8; --mint-bg:#1F3B30; --gum:#FF9DBA; --gum-bg:#4A2330; --sky:#8FD3FE; --sky-bg:#1C3447; --mud:#C9A988; color-scheme:dark } }
:root[data-theme="dark"]{
  --bg:#211912; --surface:#2C2219; --ink:#FBEFE2; --soft:#C4AF9C; --line:#46372A;
  --mint:#7FDDB8; --mint-bg:#1F3B30; --gum:#FF9DBA; --gum-bg:#4A2330; --sky:#8FD3FE; --sky-bg:#1C3447; --mud:#C9A988; color-scheme:dark }
*{box-sizing:border-box}
body{background:var(--bg);color:var(--ink);font-family:var(--body);font-size:16px;line-height:1.55}
.wrap{max-width:820px;margin:0 auto;padding-block:28px 72px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:flex;flex-direction:column;gap:36px}
h1,h2,h3{font-family:var(--display);font-weight:600;text-wrap:balance;margin:0;line-height:1.2}
h1{font-size:clamp(1.9rem,6vw,2.6rem)}
h2{font-size:1.5rem}
h3{font-size:1.1rem}
p{margin:0}
a{color:var(--sky);text-underline-offset:2px}
a:focus-visible,input:focus-visible,select:focus-visible,textarea:focus-visible,button:focus-visible{outline:3px solid var(--sky);outline-offset:2px}
.eyebrow{font-size:.78rem;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--gum)}
.lede{font-size:1.08rem;color:var(--soft);max-width:62ch;margin-top:10px}
.intro{display:flex;flex-direction:column;gap:6px}
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin-top:18px;padding:0;list-style:none;counter-reset:s}
.steps li{counter-increment:s;background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:14px 16px;font-size:.95rem}
.steps li::before{content:counter(s);display:inline-grid;place-items:center;width:24px;height:24px;border-radius:50%;background:var(--mud);color:var(--bg);font-family:var(--display);font-size:.85rem;margin-right:8px}
.steps a{font-weight:700}

.bar{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--bg);border-bottom:1px solid var(--line);margin-inline:-4px;padding:10px 4px;display:flex;flex-wrap:wrap;gap:8px 10px;align-items:center}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:10;background:var(--bg)}
.pill{display:inline-flex;gap:6px;align-items:baseline;padding:5px 12px;border-radius:999px;background:var(--surface);border:1px solid var(--line);font-size:.86rem;text-decoration:none;color:var(--ink);font-variant-numeric:tabular-nums}
.pill b{font-family:var(--display);font-weight:600}
.pill.full{background:var(--mint-bg);border-color:var(--mint)}
.status{margin-left:auto;font-size:.8rem;color:var(--soft)}
.status.warn{color:var(--gum)}

section{display:flex;flex-direction:column;gap:16px;scroll-margin-top:120px}
.game,.q{scroll-margin-top:120px}
section>header{display:flex;flex-direction:column;gap:6px}
section>header p{color:var(--soft);max-width:65ch}
.group{margin-top:10px;padding-bottom:6px;border-bottom:2px solid var(--line)}
.group small{font-family:var(--body);font-weight:400;font-size:.8rem;color:var(--soft)}
.fine{font-size:.85rem;color:var(--soft)}

.notes{background:var(--sky-bg);border-radius:14px;padding:16px 18px;display:flex;flex-direction:column;gap:10px}
.notes ol,.notes ul{margin:0;padding-left:20px;display:flex;flex-direction:column;gap:4px;font-size:.94rem}
.notes ul{list-style:none;padding-left:0}

.game{background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:18px;display:flex;flex-direction:column;gap:12px}
.game>header{display:flex;gap:12px;align-items:center}
.gh{flex:1;min-width:0}
.num{flex:none;display:grid;place-items:center;width:34px;height:34px;border-radius:50%;background:var(--mud);color:var(--bg);font-family:var(--display);font-weight:600}
.stats{font-size:.85rem;color:var(--soft);font-variant-numeric:tabular-nums}
.played{flex:none;display:inline-flex;gap:6px;align-items:center;font-weight:700;font-size:.9rem;cursor:pointer}
.fields{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px}
.field{display:flex;flex-direction:column;gap:4px;min-width:0}
.field>span{font-size:.82rem;font-weight:700;color:var(--soft)}
input[type=text],select,textarea{font:inherit;color:var(--ink);background:var(--bg);border:1px solid var(--line);border-radius:10px;padding:9px 11px;width:100%;min-width:0}
textarea{resize:vertical}
input[type=checkbox],input[type=radio]{accent-color:var(--mint);width:20px;height:20px;flex:none;margin:0}
.optlist{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:10px}
.optgame{display:flex;gap:12px;align-items:flex-start;padding:12px 14px;background:var(--surface);border:1px solid var(--line);border-radius:12px}
.optgame>div{flex:1;min-width:0;display:flex;flex-direction:column;gap:6px}
.optgame p{font-size:.9rem;color:var(--soft)}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%)}

.todos{list-style:none;margin:0;padding:0;display:flex;flex-direction:column}
.todo{display:flex;gap:12px;align-items:flex-start;padding:12px 2px;border-bottom:1px dashed var(--line)}
.todo input{margin-top:3px}
.todo label{display:flex;flex-direction:column;gap:2px;cursor:pointer;min-width:0}
.todo label span{font-size:.92rem;color:var(--soft)}
.todo input:checked+label strong{text-decoration:line-through;text-decoration-color:var(--mint)}

.q{padding:16px 0;border-bottom:1px dashed var(--line);display:flex;flex-direction:column;gap:10px}
.q h3{display:flex;gap:10px;align-items:baseline}
.qn{flex:none;font-size:.8rem;color:var(--soft);font-family:var(--body);font-weight:700;font-variant-numeric:tabular-nums;min-width:1.6em}
.q>p{color:var(--soft);font-size:.95rem;max-width:68ch}
.q .qnote{color:var(--gum);font-weight:600}
.opts{display:flex;flex-wrap:wrap;gap:8px}
.opt{position:relative;cursor:pointer}
.opt input{position:absolute;opacity:0;inset:0;width:100%;height:100%;cursor:pointer}
.opt span{display:inline-flex;gap:8px;align-items:center;padding:8px 14px;border:1.5px solid var(--line);border-radius:999px;background:var(--surface);font-size:.92rem;font-weight:600}
.opt em{font-style:normal;font-size:.7rem;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--gum);background:var(--gum-bg);padding:2px 8px;border-radius:999px}
.opt input:checked+span{border-color:var(--mint);background:var(--mint-bg)}
.opt input:focus-visible+span{outline:3px solid var(--sky);outline-offset:2px}
.qtext{max-width:520px}
.art{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.art.wide{grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}
.art figure{margin:0;display:flex;flex-direction:column;gap:6px}
.art img{width:100%;height:auto;border-radius:14px;border:1px solid var(--line);display:block}
.art.wide img{border-radius:10px}
.art figcaption{font-size:.85rem;font-weight:700}
.q.other .qtext{border-color:var(--gum)}

dl.decided{margin:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px}
dl.decided div{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:12px 14px}
dl.decided dt{font-family:var(--display);font-weight:600}
dl.decided dd{margin:2px 0 0;font-size:.92rem;color:var(--soft)}

.send{background:var(--mint-bg);border-radius:16px;padding:20px;display:flex;flex-direction:column;gap:12px}
button{font:inherit;font-weight:700;font-family:var(--display);color:var(--bg);background:var(--mud);border:0;border-radius:999px;padding:10px 20px;cursor:pointer;align-self:flex-start}
button.ghost{background:transparent;color:var(--ink);border:1.5px solid var(--line)}
.row{display:flex;flex-wrap:wrap;gap:10px;align-items:center}
#copyout{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.82rem}
@media (max-width:480px){ .game>header{flex-wrap:wrap} .status{margin-left:0;width:100%} }
@media (prefers-reduced-motion:no-preference){ .opt span,.pill{transition:background .15s,border-color .15s} }
</style>

<div class="wrap">
  <div class="intro">
    <p class="eyebrow">Clean a Cat, before we build</p>
    <h1>Everything we need from you, on one page</h1>
    <p class="lede">Play three games, tick off a few setup jobs and confirm our picks. Each question has a recommended answer, so one tap is enough. Your answers save as you go and the team reads them from here.</p>
    <ol class="steps">
      <li><a href="#playtests">Play three games</a> and note how each one hands you a pet.</li>
      <li><a href="#todo">Do the setup jobs</a>. One is left for now.</li>
      <li><a href="#questions">Confirm __NQ__ picks</a>. One tap each.</li>
    </ol>
  </div>

  <nav class="bar" aria-label="Progress">
    <a class="pill" href="#playtests" id="pill-play">Playtests <b><span id="n-play">0</span> of 3</b></a>
    <a class="pill" href="#todo" id="pill-todo">To do <b><span id="n-todo">0</span> of __NT__</b></a>
    <a class="pill" href="#questions" id="pill-q">Answers <b><span id="n-q">0</span> of __NQ__</b></a>
    <span class="status" id="status" role="status">Loading your answers</span>
  </nav>

  <section id="playtests">
    <header>
      <h2>Play these three first</h2>
      <p>Ten minutes each, as a brand new player, on a phone if you can, with a timer running. Claude cannot play Roblox games and no written guide gives these timings, so your notes settle how our players get their cats and how fast our first minutes must be. Player counts are from the morning of November 23, 2026 and move all day.</p>
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
    <p class="fine">Also worth five minutes each: Wash the Car (how washing is done by hand), Clean The Ballpit! (why picking up feels good) and Steal An Egg (the arrows and the menu that shows what grows while you are away). Added after the second research round: Clean Everything, the only cleaning game we found that kept its players. Fifteen minutes there shows what it does that the others do not. Also Restaurant Tycoon 3, the shop game that lasted longest (watch the queue, the staff and the rare customers), and Barber Simulator, where rare customers are pickier and not longer.</p>
  </section>

  <section id="todo">
    <header>
      <h2>Your to-do list</h2>
      <p>Jobs only you can do, in the order they block us. Ids are not secret and can go in chat. Keys are secret and only ever go into GitHub.</p>
    </header>
    __TODOS__
  </section>

  <section id="questions">
    <header>
      <h2>Confirm our picks</h2>
      <p>The first option is always our recommendation and the team is already working on it. Tap it to confirm or pick another. Nothing here locks the design before your playtest notes are in.</p>
    </header>
    <div class="row"><button type="button" class="ghost" id="acceptall">Accept every recommendation I have not answered</button></div>
    __QUESTIONS__
  </section>

  <section id="decided">
    <header><h2>Already decided</h2><p>For reference. Nothing to do here.</p></header>
    <dl class="decided">__DECIDED__</dl>
  </section>

  <section id="send">
    <div class="send">
      <h2>When you are done</h2>
      <p>Your answers are saved on this page and the team can read them. Say done in the project chat and we lock the design, finish the milestone plan and start building. If saving shows a problem above, copy your answers and paste them in the chat.</p>
      <div class="row"><button type="button" id="copy">Copy my answers</button><span class="fine" id="copied" role="status"></span></div>
      <textarea id="copyout" rows="8" hidden readonly aria-label="Your answers as text"></textarea>
    </div>
  </section>
</div>

<script>
(function(){
  var DATA = __DATA__;
  var LS = "clean-a-cat-plan-v1";
  var state = {};      // docId -> {key: value}
  var dirty = {};      // docId -> true while a local change is unsaved
  var timers = {}, writing = {}, again = {};
  var db = null, online = false;
  var statusEl = document.getElementById("status");

  function setStatus(t, warn){ statusEl.textContent = t; statusEl.classList.toggle("warn", !!warn); }
  function controls(doc){ return document.querySelectorAll('[data-doc="' + doc + '"]'); }

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
      else if (el.type === "radio") el.checked = (v !== undefined && v !== null && String(v) === el.value);
      else el.value = v == null ? "" : String(v);
    });
    markOther(doc);
  }
  function markOther(doc){
    if (doc.indexOf("q-") !== 0) return;
    var art = document.getElementById(doc); if (!art) return;
    var q = DATA.qs.filter(function(x){ return x.id === doc; })[0];
    var p = (state[doc] || {}).pick;
    art.classList.toggle("other", !!q && p !== undefined && p !== "" && Number(p) === q.opts.length - 1 && q.opts[q.opts.length - 1] === "Something else");
  }
  function counts(){
    var play = 0, todo = 0, q = 0;
    DATA.games.slice(0, 3).forEach(function(g){ if ((state[g.id] || {}).played === true) play++; });
    DATA.todos.forEach(function(t){ if ((state[t.id] || {}).done === true) todo++; });
    DATA.qs.forEach(function(x){ var p = (state[x.id] || {}).pick; if (p !== undefined && p !== null && p !== "") q++; });
    document.getElementById("n-play").textContent = play;
    document.getElementById("n-todo").textContent = todo;
    document.getElementById("n-q").textContent = q;
    document.getElementById("pill-play").classList.toggle("full", play === 3);
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
      var p = (state[x.id] || {}).pick;
      if (p === undefined || p === null || p === "") {
        state[x.id] = Object.assign({}, state[x.id] || {}, { pick: "0" });
        applyDoc(x.id); changed(x.id, 150);
      }
    });
  });

  function summary(){
    var L = ["Clean a Cat: my answers", ""];
    L.push("PLAYTESTS");
    DATA.games.forEach(function(g){
      var d = state[g.id] || {};
      if (!d.played && !d.notes && !d.pet && !d.fun && !d.wash && !d.wait) return;
      var bits = [];
      if (d.pet !== undefined && d.pet !== "") bits.push("pet: " + DATA.pet[Number(d.pet)]);
      if (d.fun) bits.push("first fun at " + d.fun + " s");
      if (d.wash !== undefined && d.wash !== "") bits.push("washing: " + DATA.wash[Number(d.wash)]);
      if (d.wait !== undefined && d.wait !== "") bits.push("waits: " + DATA.wait[Number(d.wait)]);
      L.push("- " + g.name + (d.played ? " (played)" : "") + (bits.length ? ". " + bits.join("; ") : ""));
      if (d.notes) L.push("  Notes: " + d.notes);
    });
    L.push("", "TO DO, DONE");
    DATA.todos.forEach(function(t){ if ((state[t.id] || {}).done === true) L.push("- " + t.t); });
    L.push("", "ANSWERS");
    DATA.qs.forEach(function(x, i){
      var d = state[x.id] || {};
      var has = d.pick !== undefined && d.pick !== null && d.pick !== "";
      L.push((i + 1) + ". " + x.t + ": " + (has ? x.opts[Number(d.pick)] : "not answered") + (d.note ? " (" + d.note + ")" : ""));
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
          // send anything typed before the store answered
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
page = (PAGE.replace("__PROMPTS__", prompts_html).replace("__EXTRA__", extra_html).replace("__GAMES__", games_html)
        .replace("__OPT__", opt_html).replace("__TODOS__", todos_html).replace("__QUESTIONS__", q_html)
        .replace("__DECIDED__", decided_html).replace("__NQ__", str(NQ)).replace("__NT__", str(NT))
        .replace("__DATA__", json.dumps(DATA)))
open(OUT_HTML, "w", encoding="utf-8").write(page)

# ================================================================= Markdown copy
M = []
M.append("# Clean a Cat: what we need from Derek before we build (2026-11-23 ET, Planning-Agent)")
M.append("")
M.append("This is the file copy of the plan page. The page lets Derek tick jobs, pick answers and type playtest notes, and it saves them where the team can read them. PAGE_LINK")
M.append("")
M.append("Three parts: play three games, do the setup jobs and confirm our picks. Every question has a recommended answer and the team is already working on it. Nothing here locks the design before the playtest notes are in.")
M.append("")
M.append("## 1. Play these three first")
M.append("Ten minutes each, as a brand new player, on a phone if possible, with a timer running. Player counts are from the morning of November 23, 2026.")
M.append("")
M.append("| Game | Players and votes | Why it is on the list | Look for |")
M.append("|---|---|---|---|")
for g in GAMES:
    M.append(f"| [{g['name']}]({g['url']}) | {g['stats']} | {g['why']} | {g['look']} |")
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
    M.append(f"- [{g['name']}]({g['url']}): {g['look']}")
M.append("- Wash the Car (how washing is done by hand), Clean The Ballpit! (why picking up feels good) and Steal An Egg (the arrows and the menu that shows what grows while you are away). Added after the second research round: Clean Everything, the only cleaning game we found that kept its players. Also Restaurant Tycoon 3 and Barber Simulator.")
M.append("")
M.append("## 2. Derek's to-do list")
M.append("Ids are not secret and can go in chat. Keys are secret and only ever go into GitHub.")
for title, items in TODOS:
    M.append("")
    M.append(f"**{title}**")
    for t in items:
        link = f" [{t['link'][1]}]({t['link'][0]})" if t.get("link") else ""
        M.append(f"- [ ] **{t['t']}.** {t['d']}{link}")
    if "Kids and Select" in title:
        M.append("")
        M.append(KIDS_NOTE)
M.append("")
M.append("## 3. Questions, each with our recommended answer")
M.append("The first option is the recommendation.")
n = 0
for title, who, items in QUESTIONS:
    M.append("")
    M.append(f"**{title}** (from {who})")
    M.append("")
    M.append("| # | Question | What it means | Options, recommended first |")
    M.append("|---|---|---|---|")
    for q in items:
        n += 1
        d = q["d"] + (" " + q["note"] if q.get("note") else "")
        if q.get("imgs"):
            d += " Pictures: `Model-Agent/store-art/store-art-draft-2026-11-23.png` in the shared folder."
        M.append(f"| {n} | {q['t']} | {d} | {' / '.join(q['opts'])} |")
M.append("")
M.append("## Already decided")
for a, b in DECIDED:
    M.append(f"- **{a}:** {b}")
M.append("")
M.append("## What happens when Derek is done")
M.append("Planning-Agent reads the answers from the page, folds the playtest notes into `gdd-draft.md`, asks for the design lock, finishes `milestone-1.md` and hands over to the coordinator.")
open(OUT_MD, "w", encoding="utf-8").write("\n".join(M) + "\n")
print("questions", NQ, "todos", NT, "html bytes", len(page))
