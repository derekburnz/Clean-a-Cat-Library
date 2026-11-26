# Page v55, 2026-11-26 evening: Derek answered the last two questions and wrote notes on every setup step.
p = "build_plan2.py"
s = open(p, encoding="utf-8").read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:70], s.count(a))
    s = s.replace(a, b)

# 1. the two questions are answered
rep('''("New on November 26, in the afternoon", "Model-Agent and Gameplay-Engineer", "Two questions. If you leave one, our pick stands.", [''',
    '''("New on November 26, in the afternoon", "Model-Agent and Gameplay-Engineer", "Two questions. You answered both by 5:20 PM that evening.", [''')
rep('''dict(id="headbows", t="Bows on the ten special cats with a head piece: make them smaller", new=True,''',
    '''dict(id="headbows", t="Bows on the ten special cats with a head piece: make them smaller",''')
rep('''dict(id="notifylive", t="Notifications on the live game: set up on the day you promote", new=True,''',
    '''dict(id="notifylive", t="Notifications on the live game: set up on the day you promote",''')

# 2. the setup list: what is still his
a = s[s.index('SETUP = ['):s.index('PARKED = [')]
b = '''SETUP = [
    dict(id="s2-devtest", t="Play the dev game on your iPhone and tell us what you find",
         d="You wrote that you are playing now. Everything built so far is switched on in the dev game. Write what felt wrong or slow in the box here or in the chat, in your own words. No screenshots are needed. Three answers help the most, and they are the first check of the whole design: did scrubbing feel good on the phone, was the clean cat a nice moment and would you wash a second cat. Then write keep or rethink for the scrub. Nothing goes to the live game until you say it is good."),
    dict(id="s2-questionnaire", t="Fill in the maturity questionnaire, last",
         d="You said you will leave this to last, and that works. It has one deadline: it must be in before the Robux crate is switched on in the live game, because the crate is a paid random item and Roblox wants that declared. It is on the live game's Creator Hub page. Growth-Agent wrote the answers from the design. Every answer is no except paid random items, which is yes. If it then asks whether the game checks Roblox's policy for each player, that is yes too. The result should be Minimal. If a question does not fit a plain no, write it in the box and we will answer it."),
    dict(id="s2-promote", t="Say the word when the dev game is good",
         d="When the dev game feels right, write send it to live in the chat. That day we make the live passes and products, set the server size to six and private servers to 25 Robux, set up the live notifications and publish the build you tested. Feature switches on live stay off until you say which to turn on. Leave this unticked until then."),
]
'''
s = s.replace(a, b)

rep('<p>These are settings on your own Roblox pages and your PC, and one playtest at the end. The notification step is gone from this list: it is done on the dev game and you have nothing to click for it there. We cannot press these for you. Tick each one when it is done. The box under each is for ids or a note.</p>',
    '<p>Three things are left that only you can do. The list was nine steps this afternoon. Six left it this evening: you handed us the passes, the products and the store art, you confirmed six players and gave a new private server price, which we now set, computer use is allowed, and the group wall step is gone because Roblox no longer has group walls. Tick each one when it is done. The box under each is for a note.</p>')

# 3. the top of the page
rep('updated November 26, 3:25 PM', 'updated November 26, 5:40 PM')
a = s[s.index('<p class="lede">'):s.index('<ol class="steps">')]
b = '''<p class="lede">Nothing is left to answer. All 78 questions have your pick, and your notes from this evening are saved and passed to the builders. What you decided tonight is at the top of <a href="#saved">What is saved</a>. This page has a new link since the threads were remade, and every answer came across. The <a href="#setup">setup list</a> is down to three things only you can do: your playtest notes, the questionnaire and the word to go live. Every earlier answer is under <a href="#answered">Answered already</a>, and the one page design is <a href="https://claude.ai/artifact/DzvEnLeFKMnrALQf2BnwB4">here</a>.</p>
    '''
s = s.replace(a, b)
rep('<li>Answer the two new questions. If you leave one, our pick stands.</li>', '<li>Play the dev game and write what felt wrong or slow, here or in the chat.</li>')
rep('<li>Tick the setup steps as you do them. The shop buttons stay hidden until the passes and products exist.</li>', '<li>If you disagree with something we picked tonight, such as 25 Robux for private servers, say so and we change it.</li>')

# 4. what is saved, newest first
rep('''TODAY = [
''', '''TODAY = [
    ("Your answers, November 26 evening", "The ten special cats with a head piece get a much smaller bow, moved from the side of the head to the top right corner like every other cat. Model-Agent has it and will show you a before and after. Notifications on the live game are set up on the day you promote. Six players a server is confirmed. The questionnaire is yours and comes last. You are playtesting the dev game and will tell us what you find."),
    ("Passes, products and store art are ours now, November 26", "You said we can make the game passes and developer products with the keys or through Claude in Chrome, and upload the store art the same way. So you make nothing by hand. Gameplay-Engineer is making the five passes and eight products on the dev game with the group key first. Roblox has pages for doing this with a key, and we are checking that your key is allowed to. If it is not, we will name the one box to tick or use your signed in Chrome for that job only. We never type a password or a code. The store art was tried through Chrome this morning and Chrome could not pick a file from our side, so we are trying other ways. If none works we will say so here, and dragging the six files in stays a one minute job."),
    ("Private servers at 25 Robux, November 26", "You wrote 50 or 25, since being alone in a server has no real benefit, and free with Roblox Plus. We picked 25, the lower of your two, and that is a judgment, so say 50 if you prefer it. Roblox gives paid private servers to Plus members free by itself, so one price does both. It is set once, on the day you promote, because changing it later cancels the private servers players already pay for. The design file says 25 now."),
    ("The group wall step is gone, November 26", "You wrote that you did not know what the wall was. That step was ours and it was out of date. The wall was the public message board on a group's page, and from what we can find Roblox retired walls at the end of March 2026. So there is nothing to turn off. Joining the group for a good reward is in the game as you want it: the gift stand gives one pet for a favourite and joining Creampuff Games."),
    ("A new link for this page, November 26", "The first page was deleted together with the old threads at 3:43 PM. It was put back from the saved copy at a new link at 3:52 PM with all 155 saved answers, and you have answered on the new one since. The old link no longer opens."),
''')
rep('("Still open", "The two new questions at the top of this page and the setup list, which is yours."),',
    '("Still open", "No question. Three things on the setup list: your playtest notes, the questionnaire and the word to go live."),')
rep('("Fresh threads, November 26", "You are deleting every thread and making them again for fresh memory and file limits. This page, its link and its saved answers stay. Every answer, note and setup step is also saved in the project notes and in the library, so a new Planning-Agent keeps this page up without the old chat."),',
    '("Fresh threads, November 26", "You deleted every thread and made them again for fresh memory and file limits. Every answer, note and setup step is also saved in the project notes and in the library, so the new Planning-Agent keeps this page up without the old chat."),')
rep('The live game waits on the second question at the top of this page."),', 'The live game is set up on the day you promote, your pick of that evening."),')

# 5. things that wait
rep('("Server size", "Six, your pick. Setting it is in the setup list on this page."),', '("Server size", "Six, confirmed on November 26. We set it."),')
rep('("Maturity questionnaire", "The answers are written, and filling it in is in the setup list on this page."),', '("Maturity questionnaire", "The answers are written. Yours to fill in, last, before the Robux crate goes on in the live game."),')
rep('The live game is the question at the top of this page. Players under 13 cannot get notifications."),', 'The live game is set up on the day you promote. Players under 13 cannot get notifications."),')
rep('The newest files are in the chat."),', 'The six files are final. We are uploading them ourselves, as you asked on November 26."),')
open(p, "w", encoding="utf-8").write(s)
print("ok")

# 6. tonight's decisions get their own visible section above the setup list
s = open(p, encoding="utf-8").read()
N_TONIGHT = 5
rep('today_html = "".join(f"<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>" for a, b in TODAY)',
    'N_TONIGHT = 5\ntonight_html = "".join(f"<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>" for a, b in TODAY[:N_TONIGHT])\ntoday_html = "".join(f"<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>" for a, b in TODAY[N_TONIGHT:])')
rep('.replace("__TODAY__", today_html)', '.replace("__TODAY__", today_html).replace("__TONIGHT__", tonight_html)')
rep('''  <section id="setup">
    <header>
      <h2>Setup only you can do</h2>''', '''  <section id="saved">
    <header>
      <h2>What you decided this evening</h2>
      <p>Read from this page at 5:25 PM on November 26. Each one went to the builder who owns it. Nothing to do here unless one reads wrong to you.</p>
    </header>
    <dl class="decided">__TONIGHT__</dl>
  </section>

  <section id="setup">
    <header>
      <h2>Setup only you can do</h2>''')
rep('<header><h2>Decided on November 24 and 25</h2></header>', '<header><h2>Decided from November 24 to 26</h2></header>')
rep('<p class="alldone" id="alldone" hidden><strong>Nothing is left to answer.</strong> The setup list is below.</p>',
    '<p class="alldone" id="alldone" hidden><strong>Nothing is left to answer.</strong> What you decided this evening and the setup list are below.</p>')
open(p, "w", encoding="utf-8").write(s)
print("ok 2")
