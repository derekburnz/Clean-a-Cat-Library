# Page v58, 2026-11-27 morning (Design-Agent): Derek's back door expansion ask, as a question to pick from.
p = "build_plan2.py"
s = open(p, encoding="utf-8").read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:70], s.count(a))
    s = s.replace(a, b)

rep('''QUESTIONS = [
    ("New on November 26, in the afternoon",''', '''QUESTIONS = [
    ("New on November 27, in the morning", "Design-Agent", "One question, from your note about the back door.", [
        dict(id="expansion", t="Behind the back door: a VIP Lounge where rare VIPs drop off cats",
             d="You asked for the back door to read as an expansion the player has to unlock, blocked off with caution tape and building materials, and opened with coins for now (a rebirth unlock only if we make rebirths). That part is being built so that any idea below can go behind it, and nothing inside is built until you pick. Today the VIP Room is a build on the Build board: it costs 15,000 coins, takes 12 hours and makes special visitors come more often, but it is not a place you can walk into. Our pick turns your VIP drop off idea and that build into one place. The back door opens onto a VIP Lounge with a golden drop off counter. About once every 10 to 15 minutes of play a VIP pulls up at the back, leaves a rare cat in a golden carrier and waits in the lounge. Washing it pays several times a normal cat and always gives a crate, with the chances shown as always. Why this one: it reuses the special cats Model-Agent already made, it gives a rare exciting moment players come back for on day 2, and it gives the back door a story. The second option is your other idea, a worker wing with big tubs where helpers wash two cats at once. It is a strong second unlock later, when the first door is open. The third is a garden patio where washed cats dry off and your pets play, and the tip jar fills faster. It is calmer, more for show and for collecting. The fourth is a cat hotel: cats stay while you are offline, and you collect coins when you come back. That gives a reason to return but little to do in the room itself. We would start the unlock at a test price on dev and tune it after you play.",
             opts=["Yes, a VIP Lounge where rare VIPs drop off cats", "A worker wing with big tubs that wash two cats at once", "A garden patio where cats dry off and pets play", "A cat hotel that earns while you are offline", ELSE]),
    ]),
    ("New on November 26, in the afternoon",''')
open(p, "w", encoding="utf-8").write(s)
print("ok")
