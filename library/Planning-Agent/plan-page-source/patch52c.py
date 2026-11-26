# Page v56, 2026-11-26 5:50 PM ET: Gameplay-Engineer and Growth-Agent report what the keys can do.
p = "build_plan2.py"
s = open(p, encoding="utf-8").read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:70], s.count(a))
    s = s.replace(a, b)
a = s[s.index('    ("Passes, products and store art are ours now, November 26",'):s.index('    ("Private servers at 25 Robux, November 26",')]
b = '''    ("Passes, products and store art are ours now, November 26", "You said we can make the game passes and developer products with the keys or through Claude in Chrome, and upload the store art the same way. Gameplay-Engineer and Growth-Agent checked: the keys you already gave can make the dev passes and products, set the server size and upload the main icon and the four thumbnails. That work is in review now, so you make none of it by hand. One piece is left that no key can do: adding icon E as the alternate icon. Roblox has no key route for alternate icons, so that one is on your setup list below. We never type a password or a code."),
'''
s = s.replace(a, b)
rep('''    dict(id="s2-maturity", t="Fill in the maturity questionnaire, last",''',
'''    dict(id="s2-icone", t="Add icon E as the alternate icon",
         d="The one store art job a key cannot do. We upload the main icon and the four thumbnails ourselves. An alternate icon can only be added by hand in Creator Hub, on the live game's page where the main icon is set. The file is icon-alternate-e-512.png, in the project's files under Model-Agent, store-art, picked-2026-11-26. Say the word in the chat and we attach it there for you. It can wait until the day you promote. Tick this when it is in and we check the page."),
    dict(id="s2-maturity", t="Fill in the maturity questionnaire, last",''')
rep('<p>Three things are left that only you can do.', '<p>Four things are left that only you can do.')
rep('you handed us the passes, the products and the store art,', 'you handed us the passes, the products and most of the store art,')
rep('is down to three things only you can do: your playtest notes, the questionnaire and the word to go live.', 'is down to four things only you can do: your playtest notes, one alternate icon, the questionnaire and the word to go live.')
rep('("Still open", "No question. Three things on the setup list: your playtest notes, the questionnaire and the word to go live."),', '("Still open", "No question. Four things on the setup list: your playtest notes, icon E as the alternate, the questionnaire and the word to go live."),')
rep('The six files are final. We are uploading them ourselves, as you asked on November 26."),', 'The six files are final. We upload the main icon and the four thumbnails with the key. Icon E as the alternate is yours to add, on the setup list."),')
rep('updated November 26, 5:40 PM', 'updated November 26, 5:35 PM')  # the clock read 5:34 PM ET; 5:40 was ahead of it
open(p, "w", encoding="utf-8").write(s)
print("ok c")
