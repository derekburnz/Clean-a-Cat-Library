# Page v60, Gameplay-Engineer's 2x/3x price question.
p = "build_plan2.py"
s = open(p, encoding="utf-8").read()
anchor = '''        dict(id="resetbtn",'''
assert s.count(anchor) == 1
new = '''        dict(id="coinprices", t="2x and 3x Coins cost 50 and 100 Robux, shown at 25 and 50 during the launch sale",
             d="You asked for 2x and 3x Coins as the cheap entry at 25 and 50 Robux. Our pick makes 50 and 100 the regular prices, so during the launch sale the cards show 25 and 50 with the real price struck through, the same as everything else. When the sale ends they go back to 50 and 100. The other way keeps 25 and 50 as the regular prices with no sale on these two, since half of 25 rounds to 12.",
             opts=["Yes, 50 and 100 regular, 25 and 50 in the sale", "25 and 50 always, no sale on these two", ELSE]),
'''
s = s.replace(anchor, new + anchor, 1)
s = s.replace("Ten new questions are at the top", "Eleven new questions are at the top", 1)
open(p, "w", encoding="utf-8").write(s)
print("ok")
