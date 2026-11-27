# Page v59, 2026-11-27 (Design-Agent): Derek dropped the VIP Lounge (VIPs already come from the front). Fresh question.
p = "build_plan2.py"
s = open(p, encoding="utf-8").read()
a0 = s.index('    ("New on November 27, in the morning", "Design-Agent"')
a1 = s.index('    ("New on November 26, in the afternoon",')
new = '''    ("New on November 27, in the morning", "Design-Agent", "One question, from your note about the back door. The VIP Lounge is off the list, as you said: special visitors already come in at the front.", [
        dict(id="expansion2", t="Behind the back door: a cat hotel that earns while you are away",
             d="The taped off back door with its coin unlock is being built now, so any of these can go behind it, and nothing inside is built until you pick. One thing to know first: the back door is where the Garden's locked gate stands today (the 25,000 coin build that makes the tip jar hold 12 hours and fill faster). Whatever you pick takes the back door, and the Garden moves to a side yard so the two never clash. Our pick is the cat hotel. Inside are four small rooms with beds and a front desk. While you play, a cat now and then asks to stay, and you pick a stay of 1, 4 or 8 hours (a longer stay pays more). You wash it once at check in, then it sleeps in its room. When its time is up it checks out and pays you, even while you are offline, and on your next visit it leaves a little thank you gift at the desk (coins, a bow, and now and then a crate, with the chances shown as always). Why this one: picking a stay before you log off and coming back to collect is the strongest day 2 return reason we know of, and it is different from the tip jar, which fills by itself with nothing to choose. More rooms can be bought later, which gives a long goal. Second is your own idea, a worker wing with big tubs where helpers wash two cats at once. It makes the spa earn faster but gives no reason to come back the next day. Third is a new idea, a kitten nursery: a basket of kittens arrives, you feed them once each visit, and in about three days each one grows up and joins you as a pet or helps out. It is cute and gives a reason to return each day, but it is a bigger build and overlaps a little with pets from crates. We would start the unlock at a test price on dev and tune it after you play.",
             opts=["Yes, the cat hotel that earns while you are away", "A worker wing with big tubs that wash two cats at once", "A kitten nursery where kittens grow up over a few days", ELSE]),
    ]),
'''
s = s[:a0] + new + s[a1:]
s = s.replace("q2-expansion", "q2-expansion2") if "q2-expansion\"" in s else s
open(p, "w", encoding="utf-8").write(s)
print("ok")
