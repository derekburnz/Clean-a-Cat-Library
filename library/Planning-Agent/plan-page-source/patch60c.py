# Page v60, Growth's game links question.
p = "build_plan2.py"
s = open(p, encoding="utf-8").read()
anchor = '''        dict(id="iconE",'''
assert s.count(anchor) == 1
new = '''        dict(id="gamelinks", t="The game page links to the Creampuff Games group only, at first",
             d="Roblox lets the game page show links, such as the group and social accounts. Our pick shows the group link only at first. It is where players join for the gift crate, and social links can come once there is something to post. Links to social sites also have their own age rules on Roblox, so fewer is simpler for young players.",
             opts=["Yes, group link only for now", "Add social links too (tell us which)", ELSE]),
'''
s = s.replace(anchor, new + anchor, 1)
s = s.replace("Eleven new questions are at the top", "Twelve new questions are at the top", 1)
open(p, "w", encoding="utf-8").write(s)
print("ok")
