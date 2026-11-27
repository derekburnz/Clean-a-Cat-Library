# Page v60, 2026-11-27 (Design-Agent): every lane's open question for Derek in one round.
p = "build_plan2.py"
s = open(p, encoding="utf-8").read()
anchor = '''    ("New on November 27, in the morning", "Design-Agent",'''
assert s.count(anchor) == 1
new = '''    ("New on November 27, the last round", "Design-Agent with every team", "Everything any of us still wanted to ask you, in one go. Each has our pick first.", [
        dict(id="salend", t="The launch sale ends 7 days after launch, then back to regular prices",
             d="Everything is 50% off with the regular price struck through, as you asked. For that to stay honest, the struck price has to be a real regular price, so the sale needs an end. Our pick is 7 days after the public launch, then the regular prices. A shorter sale catches fewer players. A sale that never ends turns the struck price into a fake one, which young players and Roblox both frown on.",
             opts=["Yes, 7 days after launch", "3 days after launch", "14 days after launch", "Keep it until I say", ELSE]),
        dict(id="resetbtn", t="The reset account button stays for you and the dev game only",
             d="Settings now has a reset button so you can wipe your save and replay from the tutorial. Our pick keeps it for you and the dev game only. A player who taps it by mistake loses everything, and young players do tap things. If you want players to have it too, it would ask twice and make them type RESET.",
             opts=["Yes, me and dev only", "Players get it too, with a double check", ELSE]),
        dict(id="louname", t="The third helper keeps the name Lou",
             d="The pass is now called Extra Worker everywhere players see it, as you asked. The helper the pass brings is still called Lou in the Helpers window, and players can rename helpers anyway. Our pick keeps Lou.",
             opts=["Yes, keep Lou", "Give the helper a new name", ELSE]),
        dict(id="likecoins", t="The 150 like coins become a thank you that does not depend on the like",
             d="The gift card asks for a like and then gives 150 coins. The coins already come whether or not the player likes, but it still reads as coins for a like. Roblox has no clear rule, and some developers say it can count as buying ratings. Our pick keeps the same 150 coins as a thank you gift on the card, with the like ask beside it and no link between them. The player gets the same, and the risk goes away.",
             opts=["Yes, a thank you that is not tied to the like", "Keep it as it is", "Remove the coins", ELSE]),
        dict(id="favcrate", t="The gift crate comes for joining the group only, not for a favourite",
             d="Today the free gift crate needs a favourite and a group join. Rewarding a group join is a common, accepted pattern. Rewarding a favourite is the same worry as likes. Our pick keeps the crate for the group join only.",
             opts=["Yes, group join only", "Keep favourite and group join", ELSE]),
        dict(id="starterclock", t="The starter pack keeps its 72 hours, with no ticking clock on screen",
             d="The starter pack is for a player's first 72 hours, and the HUD shows the time left in days, hours and minutes. It is real and calm, but a clock is still time pressure on young players. Our pick keeps the same 72 hour offer and shows \\"New player offer\\" with no clock. The other choices are keeping the clock, or no time limit at all.",
             opts=["Yes, same offer, no clock shown", "Keep the clock", "No time limit", ELSE]),
        dict(id="hotelnums", t="The cat hotel starts with these numbers, tuned after you play",
             d="The hotel draft (picture in the thread) unlocks at the back door for 1,500 coins (50 on dev for testing). Two rooms are open at first, and rooms 3 and 4 cost 3,000 and 8,000 coins. A stay of 1, 4 or 8 hours pays 60, 200 or 360 coins, more for rarer guests. Each guest leaves a gift when it checks out, with the chances shown. On an 8 hour stay that is bonus coins 65%, a bow 23% or a crate 12%. There is no Robux inside the hotel. Guests are normal cats, never special visitors. The Garden moves to a side yard. Our pick is to start with these numbers and tune them after you play it on dev.",
             opts=["Yes, start with these", ELSE]),
        dict(id="helperart", t="Helper pictures: smooth busts now, the helpers' game models to match after launch",
             d="Model-Agent redrew Jo, Sam and Lou for their pictures as smooth, rounded busts instead of the blocky game models, as you asked. The game models are still the old ones, so the picture and the person in the spa look a little different. Our pick uses the smooth pictures now and remakes the game models to match after launch. You can also have it done now, or go back to blocky.",
             opts=["Yes, pictures now, models after launch", "Remake the game models now too", "Go back to blocky pictures", ELSE]),
        dict(id="shopwords", t="Shop pictures keep their words, like 2x and 3x, inside the picture",
             d="The new shop pictures have their big words baked in (\\"2x\\", \\"3x\\", \\"+1\\"), so they read at a glance. The other way is plain pictures with the shop drawing the words, which only matters if the game is ever translated. Our pick keeps the words in the picture.",
             opts=["Yes, words in the picture", "Plain pictures, the shop draws the words", ELSE]),
        dict(id="iconE", t="Icon E waits for an A/B test once the game has players",
             d="Roblox's icon page holds one icon only. A second one exists only as an A/B test on the game's Experiments page, which needs players to tell anything. Our pick keeps icon A alone until launch, then tests A against E.",
             opts=["Yes, A now, test E after launch", "Make E the main icon", "Drop E", ELSE]),
    ]),
'''
s = s.replace(anchor, new + anchor, 1)
s = s.replace("Clean a Cat, updated November 27, 7:40 AM", "Clean a Cat, updated November 27, 7:50 AM", 1)
a = s.index('<p class="lede">')
b = s.index('</p>', a)
s = s[:a] + '<p class="lede">Ten new questions are at the top: everything any of us still wanted to ask you, in one round, each with our pick first. Your cat hotel pick is in and drafted. One thing on your to-do list: the four dev thumbnails you said you would upload yourself. Every earlier answer is under <a href="#answered">Answered already</a>, and the one page design is <a href="https://claude.ai/artifact/DzvEnLeFKMnrALQf2BnwB4">here</a>.' + s[b:]
open(p, "w", encoding="utf-8").write(s)
print("ok")
