p = "build_plan2.py"
s = open(p, encoding="utf-8").read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:70], s.count(a))
    s = s.replace(a, b)
assert s.count(", new=True,") == 4
s = s.replace(", new=True,", ",")
NEWQ = '''    ("New on November 26, in the afternoon", "Gameplay-Engineer", "One question. If you leave it, our pick stands.", [
        dict(id="notifylive", t="Notifications on the live game: set up on the day you promote", new=True,
             d="Notifications are set up on the dev game, and you did not have to click anything. Our workflow on GitHub made the message, build_done, and saved the group key you already have as the dev game's secret, CleanACat_NotifyKey. The keys went from GitHub's secrets straight to Roblox and were never shown in the chat. So the notification step is gone from your setup list. The live game needs the same two things, and anything on live waits for your word. Our pick follows your dev first rule and your answer on passes and products: we run the same workflow on the live game on the day you promote, with the rest of the live set. The second option does it now, so one thing less is left for that day. Either way nothing a player can see changes, and no notification goes out until the feature is switched on in the live game and the game has 100 visits.",
             opts=["Yes, set up live notifications on the day I promote", "Set them up on the live game now", "I will make the live message and secret by hand", ELSE]),
    ]),
'''
rep('QUESTIONS = [\n    ("New on November 26, after your answers", "all the builders", "Four small ones that came up after your answers this morning. If you leave one, our pick stands.", [',
    'QUESTIONS = [\n' + NEWQ + '    ("New on November 26, after your answers", "all the builders", "Four small ones that came up after your answers that morning. You answered all four at 3:14 PM.", [')

# setup: notifications are done on dev by the workflow, so the step goes
a = s[s.index('    dict(id="s2-notify",'):s.index('    dict(id="s2-computeruse",')]
s = s.replace(a, "")
a = s[s.index('    dict(id="s2-storeart",'):s.index('    dict(id="s2-computeruse",')]
b = '''    dict(id="s2-storeart", t="Put the store art in",
         d="Your pick: icon A as the main icon and icon E as the only alternate for now, then the thumbnails in your order 2, 1, 3, 5. The bow on E stays where it is, your answer of November 26. Every picture was drawn again that day after the cats' faces changed, and the last two thumbnails were still being finished in the afternoon. So use the newest set in the main chat, and ask there if you are not sure which is newest. We cannot put files on the store page from here. When they are in, tick this and Model-Agent checks the page and the order."),
'''
s = s.replace(a, b)
a = s[s.index('    dict(id="s2-devtest",'):s.index('PARKED = [')]
b = '''    dict(id="s2-devtest", t="Play today's new pieces on the dev game, on your iPhone",
         d="Ready now. All of it has been on in the dev game since 12:21 PM on November 26: the bigger spa, the counter window where waiting cats sit, the carrier a customer sets on the counter, the cards over the waiting cats, the tidy HUD with the More tray, the Build button, fewer prompt bubbles at once and the coin popup over a helper. One fault we know of: when the line moves up, a carrier can land on the wrong mat. The fix is in review. Play about ten minutes and write in the box what felt wrong or slow. Three answers help the most, and they are the first check of the whole design: did scrubbing feel good on the phone, was the clean cat a nice moment and would you wash a second cat. Then write keep or rethink for the scrub. Nothing here goes to the live game until you say it is good."),
]
'''
s = s.replace(a, b)

a = s[s.index('    <p class="lede">Four small questions came up'):s.index('    </ol>\n  </div>')]
b = '''    <p class="lede">One new question is at the top, with our pick first. You answered the four from this morning at 3:14 PM and they are saved. The <a href="#setup">setup list</a> is shorter: notifications are done on the dev game, and the playtest of today's pieces is ready. You are making the threads again with fresh memory. This page and every answer on it stay, and all of it is also saved in the project notes and the library. Every earlier answer is under <a href="#answered">Answered already</a>, and the one page design is <a href="https://claude.ai/artifact/DzvEnLeFKMnrALQf2BnwB4">here</a>.</p>
    <ol class="steps">
      <li>Answer the one new question. If you leave it, our pick stands.</li>
      <li>Tick the setup steps as you do them. The shop buttons stay hidden until the passes and products exist.</li>
      <li>To change an answer, open <a href="#answered">Answered already</a> and tap another option or add words.</li>
'''
s = s.replace(a, b)
rep('TODAY = [\n', '''TODAY = [
    ("Fresh threads, November 26", "You are deleting every thread and making them again for fresh memory and file limits. This page, its link and its saved answers stay. Every answer, note and setup step is also saved in the project notes and in the library, so a new Planning-Agent keeps this page up without the old chat."),
    ("Your answers, November 26 afternoon", "The bow on icon E stays where it is, in front of the ear and tilted on the corner. The like ask may follow a finished purchase by two minutes, never on the buy screen, with its own off switch. On top of your rule, it never comes back after a yes or after two nos, and never shows during the tutorial. RbxSync is skipped and no licence is bought. You said you will restart Model-Agent yourself."),
    ("Notifications, November 26", "Done on the dev game at 12:40 PM by our GitHub workflow: the message build_done exists and the group key is saved as the game's secret. The live game waits on the question at the top of this page."),
''')
rep('("Still open", "The four new questions at the top of this page and the setup list, which is yours."),',
    '("Still open", "The one new question at the top of this page and the setup list, which is yours."),')
rep('("Notification text and key", "Answered on November 26: the group key you already have. The exact clicks are in the setup list. Players under 13 cannot get notifications."),',
    '("Notification text and key", "Done on the dev game on November 26 with the group key you already have. The live game is the question at the top of this page. Players under 13 cannot get notifications."),')
rep('("Store art, second version", "Drawn on November 26. Thumbnails 2, 1, 3, 5, icon A as the main one and E as the alternate. The fixed files are in the chat."),',
    '("Store art, second version", "Drawn on November 26, and drawn again that day with the new faces. Thumbnails 2, 1, 3, 5, icon A as the main one and E as the alternate. The newest files are in the chat."),')
rep('<p class="eyebrow">Clean a Cat, updated November 26</p>', '<p class="eyebrow">Clean a Cat, updated November 26, 3:20 PM</p>')
open(p, "w", encoding="utf-8").write(s)
print("ok")
