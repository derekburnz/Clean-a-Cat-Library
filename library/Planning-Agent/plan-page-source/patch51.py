p = "build_plan2.py"
s = open(p, encoding="utf-8").read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:70], s.count(a))
    s = s.replace(a, b)
rep('''    ("New on November 26, in the afternoon", "Gameplay-Engineer", "One question. If you leave it, our pick stands.", [''',
'''    ("New on November 26, in the afternoon", "Model-Agent and Gameplay-Engineer", "Two questions. If you leave one, our pick stands.", [
        dict(id="headbows", t="Bows on the ten special cats with a head piece: make them smaller", new=True,
             d="In the game a clean cat wears a bow, in the bow tier the player has reached. Ten of the special visitors' cats also wear a head piece, such as Bathtile's bath cap, Stardust's star crown and Djinn's turban. On those cats the bow cannot sit on the corner of the head, so it stands at the side of the head at full size. You saw that look today when a big blue bow showed up on the pink cat in thumbnail 3, and you had it taken off. That was the game's own bow at the game's size. The picture shows how three of these cats wear the top bow in the game now. Our pick is to make the bow smaller on those ten cats, so it sits neatly beside the head piece and the head piece stays the star. The second option gives those ten cats no bow at all. Their head piece already marks them as special, but the player's bow tier then shows on every cat except the rarest ones. The third leaves them as they are. The store pictures are not touched by this, because no special cat wears a bow in them.",
             imgs=[("art2/headpiece-bows.jpg", "Three special cats from the front, each with a large pink and gold bow standing at the side of the head: a blue cat in a pink bath cap with a rubber duck, a dark blue cat with a star crown and a red cat with a turban.", "Bathtile, Stardust and Djinn with the top bow, as the game shows them now")], wide=True,
             opts=["Yes, a smaller bow on the ten cats with a head piece", "No bow on cats with a head piece", "Leave the bows as they are", ELSE]),''')
a = s[s.index('    dict(id="s2-storeart",'):s.index('    dict(id="s2-computeruse",')]
b = '''    dict(id="s2-storeart", t="Put the store art in",
         d="The six files are final and safe to upload. Review-QA passed the last two on the afternoon of November 26. Your picks: icon A as the main icon, icon E as the only alternate for now with the bow where it is, then the thumbnails in your order 2, 1, 3, 5. The files are icon-main-512.png, icon-alternate-e-512.png and the four named thumbnail-order-1 to thumbnail-order-4, which are already in your order. They are in the project's files under Model-Agent, store-art, picked-2026-11-26, and we can attach them in the chat again if you ask. We cannot put files on the store page from here. When they are in, tick this and a check of the page and the order follows."),
'''
s = s.replace(a, b)
rep('and one playtest at the end. We cannot press them for you.', 'and one playtest at the end. The notification step is gone from this list: it is done on the dev game and you have nothing to click for it there. We cannot press these for you.')
rep('<p class="lede">One new question is at the top, with our pick first.', '<p class="lede">Two new questions are at the top, each with our pick first.')
rep('The <a href="#setup">setup list</a> is shorter: notifications are done on the dev game, and the playtest of today\'s pieces is ready.', 'The <a href="#setup">setup list</a> is shorter: notifications are done on the dev game, the six store art files are final and safe to upload, and the playtest of today\'s pieces is ready.')
rep('<li>Answer the one new question. If you leave it, our pick stands.</li>', '<li>Answer the two new questions. If you leave one, our pick stands.</li>')
rep('("Still open", "The one new question at the top of this page and the setup list, which is yours."),', '("Still open", "The two new questions at the top of this page and the setup list, which is yours."),')
rep('The live game waits on the question at the top of this page."),', 'The live game waits on the second question at the top of this page."),\n    ("Store art, November 26", "All six files are final and passed by Review-QA: the main icon, the alternate icon E and the four thumbnails in your order. The bits at the cats\' sides are off every cat and the blue bow is off the pink cat."),')
rep('updated November 26, 3:20 PM', 'updated November 26, 3:25 PM')
open(p, "w", encoding="utf-8").write(s)
print("ok")
