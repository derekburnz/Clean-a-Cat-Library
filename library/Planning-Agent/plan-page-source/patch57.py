# Page v57, 2026-11-26 evening: his four setup notes (5:47 and 6:04 PM ET) and his playtest notes as jobs.
p = "build_plan2.py"
s = open(p, encoding="utf-8").read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:70], s.count(a))
    s = s.replace(a, b)
def cut(a, b, new):
    global s
    i = s.index(a); j = s.index(b, i)
    s = s[:i] + new + s[j:]

# 1. Nothing is left on the setup list.
cut('SETUP = [\n', 'PARKED = [', 'SETUP = []\n')

# 2. His playtest notes, each with its job. Issue numbers stay out of the page; they are in decisions-check-2026-11-26.md.
rep('N_TONIGHT = 5\n', '''N_TONIGHT = 6
NOTES = [
    ("The starter pack card ran off the screen", "Fixed and merged. The card now shrinks to fit the room it has."),
    ("Brushing went way too fast", "Built and merged. Each wash step is set to take about 4 to 5 seconds. We time it on the iPhone 12 next."),
    ("A 3 star wash should give +3 stars", "Built and merged. A customer now gives the wash's stars, with extra for rarer cats."),
    ("A line back to the box, and a line that stands out from the floor", "Built and merged. The guide line is gold with a dark outline, and it points back to the box when a new player walks away from it."),
    ("No Walk or Buy during the wash, and the wash on its own screen", "In review. A bubbly wipe across the screen, a clean backdrop and none of the regular HUD. Gameplay-Engineer built it."),
    ("The washed cat should walk, not bounce while sitting", "In review. It walks out on its legs with a trot. We kept the cat walking out by itself so the loop stays quick."),
    ("The group reward as a crate to open", "Being built. One gift crate you open yourself, with the chances shown before you open it. Design-Agent wrote how it works."),
    ("A better photo moment", "Being built. A red light blinks faster and faster, a gentle flash goes off, then the photo slides out the back."),
    ("A pop up for the 10 second like wait, with a how to picture", "Being built. One point from us: the game cannot read a like, so the pop up says the gift unlocks in 10 seconds either way. It does not say it is checking."),
    ("The dev game still showed the old door line, with floating cats and customer parts off the body", "Being fixed. The bigger spa and the counter window are switched on in the dev game. Your Studio test had no switches on, which is why it showed the old door line, and Studio now has them too. We are checking a fresh join on the dev game itself. The floating cats and carriers are with Gameplay-Engineer, the customers' arm and hat with Model-Agent."),
    ("Pop ups only when they guide the next thing to do", "Being built by Design-Agent. Cards that only announce are cut. Guide cards come with the arrow line. The notification ask waits until the player has built something. A new crate gets the arrow line and a tip from Suds."),
]
notes_html = "".join(f"<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>" for a, b in NOTES)
LEFT = [
    ("Your playtest notes", "You wrote: Gone through some starting changes/issues more will come later. Send more in the chat whenever you have them."),
    ("Icon E as the alternate icon", "You wrote: you can do that. So it is ours. No key can set an alternate icon, so the route left is your signed in Chrome, which you offered for the store art. We never type a password or a code, and we tell you plainly if it does not work."),
    ("The maturity questionnaire", "You wrote: Lets leave for now dont worry about it yet. Left alone. It has one deadline: before the Robux crate is switched on in the live game. We bring it up then and not before."),
    ("The word to go live", "You wrote: Will do no need to put this on a todolist. It is off the list. Nothing goes to the live game until you say so."),
]
left_html = "".join(f"<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>" for a, b in LEFT)
''')
rep('.replace("__TONIGHT__", tonight_html)', '.replace("__TONIGHT__", tonight_html).replace("__NOTES__", notes_html).replace("__LEFT__", left_html)')

# 3. Tonight's list gets his four setup notes first.
rep('TODAY = [\n', '''TODAY = [
    ("Your setup notes, November 26, 6:04 PM", "All four are read. Icon E as the alternate icon is ours to add, as you said. The questionnaire is left alone until the Robux crate is about to go on in the live game. The word to go live is off this page. Your playtest notes are in the list above, and more can come any time."),
''')

# 4. The top of the page.
cut('    <p class="lede">', '    <ol class="steps">', '''    <p class="lede">Nothing is waiting on you. All 78 questions have your pick and your four setup notes are read. The playtest notes you sent this evening are with the builders, and where each one stands is in <a href="#notes">the first list</a> below. We are also checking every earlier decision against the dev game, the bigger spa and the counter window first, so nothing you decided gets lost. Every earlier answer is under <a href="#answered">Answered already</a>, and the one page design is <a href="https://claude.ai/artifact/DzvEnLeFKMnrALQf2BnwB4">here</a>.</p>
''')
rep('<li>Play the dev game and write what felt wrong or slow, here or in the chat.</li>', '<li>Send more playtest notes in the chat whenever you have them, in your own words.</li>')
rep('<li>If you disagree with something we picked tonight, such as 25 Robux for private servers, say so and we change it.</li>', '<li>If a note of yours is missing from the first list, or one reads wrong, say so.</li>\n      <li>If you disagree with something we picked, such as 25 Robux for private servers, say so and we change it.</li>')
rep('What you decided this evening and the setup list are below.</p>', 'Your playtest notes and what you decided this evening are below.</p>')

# 5. New section before "What you decided this evening".
rep('''  <section id="saved">
    <header>
      <h2>What you decided this evening</h2>''', '''  <section id="notes">
    <header>
      <h2>Your playtest notes and where each one is</h2>
      <p>You sent these in the chat from 5:45 to 6:04 PM on November 26. Each one is a job with a builder. Built and merged means it is in the game's code and reaches the dev game behind its own switch, and we tell you in the chat when it is on there. Review-QA is checking that every note you sent has a job.</p>
    </header>
    <dl class="decided">__NOTES__</dl>
  </section>

  <section id="saved">
    <header>
      <h2>What you decided this evening</h2>''')
rep('<p>Read from this page at 5:25 PM on November 26. Each one went to the builder who owns it.', '<p>Read from this page at 5:25 PM and 6:06 PM on November 26. Each one went to the builder who owns it.')

# 6. The setup section becomes a short note on the four things he answered.
cut('      <h2>Setup only you can do</h2>', '  </section>', '''      <h2>Nothing is waiting on you</h2>
      <p>The setup list is empty. You answered the last four steps at 5:47 PM and 6:04 PM, and this is how we read each one.</p>
    </header>
    <dl class="decided">__LEFT__</dl>
''')

# 7. Smaller lines.
rep('("Still open", "No question. Four things on the setup list: your playtest notes, icon E as the alternate, the questionnaire and the word to go live."),', '("Still open", "No question and no setup step. Your playtest notes are being worked through, and more can come any time."),')
rep('("Maturity questionnaire", "The answers are written. Yours to fill in, last, before the Robux crate goes on in the live game."),', '("Maturity questionnaire", "The answers are written. Left alone for now, as you said on November 26. It must be in before the Robux crate goes on in the live game, and we bring it up then."),')
rep('Icon E as the alternate is yours to add, on the setup list."),', 'Icon E as the alternate is ours to add too, as you said on November 26."),')
rep('updated November 26, 5:35 PM', 'updated November 26, __CLOCK__')
open(p, "w", encoding="utf-8").write(s)
print("ok 57")
