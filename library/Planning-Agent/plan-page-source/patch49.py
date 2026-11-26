p = "build_plan2.py"
s = open(p, encoding="utf-8").read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:70], s.count(a))
    s = s.replace(a, b)

# the seven of this morning are answered: drop their New tag
assert s.count(", new=True,") == 11
s = s.replace(", new=True,", ",")

NEWQ = '''    ("New on November 26, after your answers", "all the builders", "Four small ones that came up after your answers this morning. If you leave one, our pick stands.", [
        dict(id="iconebow", t="Icon E: the bow stays on the top right, over the ear", new=True,
             d="You asked for the bow on icon E to move to the top right of the head so the line stops cutting it. Model-Agent did that on the icon and on thumbnail 2, which shows the same cat. The bow is a little smaller and tipped, and all of it is right of the line. One thing changed with it: the bow now covers most of the ear on the clean half, and only the tip of the ear shows behind it. Our pick is to keep it. It is the placement you asked for, the bow still reads at the small sizes Roblox shows on Home and the muddy half keeps a whole ear. If you would rather see the clean ear, the second option slides the bow further out to the corner so the ear stands clear beside it. You also asked for the bows on cats in the game to sit like this one, and Model-Agent is doing that.",
             imgs=[("art2/icon-e-bow.jpg", "Icon E twice. Before: a pink bow between the cat's ears, cut by the white line between the muddy half and the clean half. After: the bow is tipped on the top right corner of the head, clear of the line, and it covers most of the right ear.", "Before on the left, after on the right"),
                   ("art2/icon-e-bow-small.jpg", "The same two icons at 150 pixels and at 48 pixels. The bow shows as a pink shape at the top right in both.", "At the sizes Roblox shows on Home and in search")], wide=True,
             opts=["Yes, keep the bow where it is now", "Slide the bow out to the corner so the clean ear shows", "Put it back between the ears, small enough to clear the line", ELSE]),
        dict(id="purchaseask", t="The like ask after a purchase: two minutes later, never on the buy screen", new=True,
             d="On the like ask you wrote: Good moment like rare customer cat finished. Maybe also after a purchase just a little bit after. The good moment part is being built as you said. This is how we read the purchase part, so say if it is wrong. When a player has finished buying something, the game may show the like ask at least two minutes later. It never shows on the buy screen or as it closes, and never after a cancelled purchase. It counts as the one ask of that visit, and after a no the game stays quiet for three visits. It has its own off switch, so you can try it on dev and turn it off without touching the other asks. The ask is a small card that reads Enjoying the spa? with two buttons, Like the game and Not now. It never mentions coins. Growth-Agent's first advice was no ask after a purchase at all, because it can feel like pressure to a young player. That was a judgment and not a Roblox rule, so your word stands.",
             opts=["Yes, two minutes after a finished purchase, with its own off switch", "Sooner, about 30 seconds after the purchase", "No like ask after a purchase", ELSE]),
        dict(id="rbxsync", t="RbxSync: skip the comparison run", new=True,
             d="You said yes to one comparison run of the RbxSync test tools against our own. Sync-Agent read its source before installing anything and stopped. Nothing was installed on your PC. What it found: RbxSync is a paid product and its licence does not allow use without buying it. Its Studio plugin works by running code that its helper program sends to it, and it switches on a place setting that lets code be run from text, which Roblox leaves off by default. An older version hid the names of those functions to get past the Creator Store scan. The plugin would load in every Studio window on your PC, the dev and live places included. Its program is unsigned, so Windows would likely block it. What it would add is three tools, for walking, watching and waiting. Our own walker reached 114 of 114 test spots this morning, and getting stuck on walls was the reason for the comparison. Our pick is to skip it. If you still want the run, it needs your OK on buying the licence and on that plugin, and we would use it in a scratch place only.",
             opts=["Yes, skip RbxSync and keep our own walker", "Run it anyway in a scratch place: I buy the licence and accept the plugin", ELSE]),
        dict(id="modelthread", t="Model-Agent keeps its thread for now", new=True,
             d="Model-Agent's thread has reached the limit on files it can attach, so it can no longer attach pictures to its own messages. Its work is not held up. It still builds, renders and opens pull requests, and the coordinator attaches its pictures for you in the main chat, as it did with icon E today. A new thread is only ever started on your word, which is why this is a question. Our pick is to keep the thread for now. It is in the middle of the bigger spa, the counter spots and the bow change, and a new thread starts from the saved notes without today's working detail. The second option starts a fresh Model-Agent thread once those are merged, which is the clean moment to switch. The third starts one now.",
             opts=["Yes, keep the thread, and the coordinator attaches its pictures", "Start a fresh Model-Agent thread once the bigger spa and the bow change are merged", "Start a fresh Model-Agent thread now", ELSE]),
    ]),
'''
rep('QUESTIONS = [\n    ("New since the build started", "all the builders", "These came up on November 26 while the game was being built from your plan. If you leave one, our pick stands.", [',
    'QUESTIONS = [\n' + NEWQ + '    ("New since the build started", "all the builders", "These came up on November 26 while the game was being built from your plan. You answered all seven that morning.", [')

# setup steps
rep('Paste the five ids in the box, each with its name. Pass ids are public',
    'Paste the five ids in the box, each with its name, and say which game they are from. Pass ids are public')
rep('''    dict(id="s2-storeart", t="Put the store art in",
         d="Your pick: icon A as the main icon and icon E as the only alternate for now. Model-Agent is fixing the orange at the sides of E first and will attach the new file in the chat, so wait for that one. Then the thumbnails in your order 2, 1, 3, 5. We cannot put files on the store page from here. When they are in, tick this and Model-Agent checks the page and the order."),''',
    '''    dict(id="s2-storeart", t="Put the store art in",
         d="Your pick: icon A as the main icon and icon E as the only alternate for now, then the thumbnails in your order 2, 1, 3, 5. The files are in the main chat. Icon E and thumbnail 2 are the new ones, with the orange at the sides gone and the bow on the top right. If you pick another bow in the question at the top of this page, wait for the new files. We cannot put files on the store page from here. When they are in, tick this and Model-Agent checks the page and the order."),''')
a = s[s.index('    dict(id="s2-notify",'):s.index('    dict(id="s2-computeruse",')]
b = '''    dict(id="s2-notify", t="Set up notifications: check the key, save it as the game's secret and make the message",
         d="Your pick: no new key, the group key you already have. We cannot see inside the key, so the first step is a check. Do these four steps for Clean a Cat, then the same four for Clean-a-Cat-Dev. The key goes straight from Roblox into the game's secrets. Never paste it on this page or in the chat.",
         steps=["Check the key. Go to Creator Dashboard, API Keys and open the group key. Under Access Permissions it needs User Notification with Write, for both games. The scope reads `user.user-notification:write`. Under Security, Restrict IP addresses must be off, because Roblox's servers call from many addresses. If User Notification is missing, add it and press Save.",
                "Save the key as a secret. Open the game, then Secrets, Create Secret. Name: `CleanACat_NotifyKey`. Secret: paste the key. Domain: `apis.roblox.com`.",
                "Make the message. Open the game, then Engagement, Notifications, Create a Notification String. Name: `build_done`. Text: `Your {buildName} is ready! Come back and show it off.`",
                "Copy the id. On that message press the three dots, then Copy Asset ID. Paste the id in the box below with the game's name. The id is not a secret, and it goes in the code for each game."],
         after="Roblox only sends to players of 13 and over who opted in, at most once a day, and only once a game has 100 or more visits. So the dev game may send nothing even when all of this is set up right."),
'''
s = s.replace(a, b)
rep('''         d="When the card shows in the Claude app on your PC, press Allow. It lets Sync-Agent work Studio's own windows during test runs. We never press Allow for you."),
]''', '''         d="When the card shows in the Claude app on your PC, press Allow. It lets Sync-Agent work Studio's own windows during test runs. We never press Allow for you."),
    dict(id="s2-devtest", t="Play today's new pieces on the dev game, on your iPhone",
         d="Not ready yet. We say in the chat when everything is on, so leave this until then. On in the dev game now: the tidy HUD with the More tray, the Build button, fewer prompt bubbles at once and the coin popup over a helper. Still in review today: the bigger spa, the counter window where waiting cats sit and the carrier a customer sets on the counter. When all of it is on, play about ten minutes and write in the box what felt wrong or slow. Nothing here goes to the live game until you say it is good."),
]''')

# renderer: optional numbered steps under a setup item
rep('''    link = f' <a href="{t["link"][0]}" target="_blank" rel="noopener">{e(t["link"][1])}</a>' if t.get("link") else ""
    return f\'\'\'
<li class="todo">
  <input type="checkbox" id="{d}__done" data-doc="{d}" data-key="done">
  <div class="tbody">
    <label for="{d}__done"><strong>{e(t["t"])}</strong><span>{e(t["d"])}{link}</span></label>
    {note}''', '''    link = f' <a href="{t["link"][0]}" target="_blank" rel="noopener">{e(t["link"][1])}</a>' if t.get("link") else ""
    extra = ""
    if t.get("steps"):
        extra += '<ol class="tsteps">' + "".join("<li>" + code(e(x)) + "</li>" for x in t["steps"]) + "</ol>"
    if t.get("after"):
        extra += f'<p class="tafter">{e(t["after"])}</p>'
    return f\'\'\'
<li class="todo">
  <input type="checkbox" id="{d}__done" data-doc="{d}" data-key="done">
  <div class="tbody">
    <label for="{d}__done"><strong>{e(t["t"])}</strong><span>{e(t["d"])}{link}</span></label>
    {extra}{note}''')
rep('def todo_item(t):\n', 'import re as _re\ndef code(x):\n    return _re.sub(r"`([^`]+)`", r"<code>\\1</code>", x)\n\ndef todo_item(t):\n')
rep('.todo input[data-q]{cursor:pointer}', '.todo input[data-q]{cursor:pointer}\n.tsteps{margin:0;padding-left:22px;display:flex;flex-direction:column;gap:8px;font-size:.95rem}\n.tsteps code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:.88em;background:var(--mint-bg);border-radius:6px;padding:1px 5px;overflow-wrap:anywhere}\n.tafter{margin:0;font-size:.92rem;color:var(--soft)}')
rep('<p>These are settings on your own Roblox pages and your PC. We cannot press them for you. Tick each one when it is done. The box under each is for ids or a note.</p>',
    '<p>These are settings on your own Roblox pages and your PC, and one playtest at the end. We cannot press them for you. Tick each one when it is done. The box under each is for ids or a note.</p>')
rep('''    M.append(f"- [ ] **{t['t']}** (`{t['id']}`). {t['d']}")
M.append("")
M.append("**Parked''', '''    M.append(f"- [ ] **{t['t']}** (`{t['id']}`). {t['d']}")
    for i, x in enumerate(t.get("steps", [])):
        M.append(f"  {i + 1}. {x}")
    if t.get("after"):
        M.append(f"  {t['after']}")
M.append("")
M.append("**Parked''')

# intro
a = s[s.index('    <p class="lede">You answered all seven new questions'):s.index('    </ol>\n  </div>')]
b = '''    <p class="lede">Four small questions came up after your answers this morning. They are at the top, each with our pick first. The <a href="#setup">setup list</a> has two changes: the notification step now has the exact clicks, and a new last step is a playtest of today's pieces on the dev game. Every earlier answer is saved under <a href="#answered">Answered already</a>, and the one page design is <a href="https://claude.ai/artifact/DzvEnLeFKMnrALQf2BnwB4">here</a>.</p>
    <ol class="steps">
      <li>Answer the four new questions. If you leave one, our pick stands.</li>
      <li>Tick the setup steps as you do them. The shop buttons stay hidden until the passes and products exist.</li>
      <li>To change an answer, open <a href="#answered">Answered already</a> and tap another option or add words.</li>
'''
s = s.replace(a, b)
rep('TODAY = [\n', '''TODAY = [
    ("Later on November 26", "Four small questions are at the top of this page: the bow on icon E, the like ask after a purchase, RbxSync and the Model-Agent thread. Your seven answers of the morning are in the design file. The notification clicks are in the setup list. On in the dev game now: the tidy HUD, the Build button, fewer prompt bubbles and the helper coin popup. The bigger spa, the counter window and the carrier on the counter are in review."),
''')
rep('("Still open", "No questions. The setup list on this page is what is left, and it is yours."),',
    '("Still open", "The four new questions at the top of this page and the setup list, which is yours."),')
rep('("Notification text and key", "Answered on November 26: the group key you already have. The step is in the setup list. Players under 13 cannot get notifications."),',
    '("Notification text and key", "Answered on November 26: the group key you already have. The exact clicks are in the setup list. Players under 13 cannot get notifications."),')
rep('("Store art, second version", "Drawn on November 26. Thumbnails 2, 1, 3, 5, icon A as the main one and E as the alternate once it is fixed."),',
    '("Store art, second version", "Drawn on November 26. Thumbnails 2, 1, 3, 5, icon A as the main one and E as the alternate. The fixed files are in the chat."),')
open(p, "w", encoding="utf-8").write(s)
print("ok")
