# Page v55, second pass after looking at the phone screenshots.
p = "build_plan2.py"
s = open(p, encoding="utf-8").read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:70], s.count(a))
    s = s.replace(a, b)
# He ticked the playtest and the questionnaire with notes that mean "not yet", so both showed crossed out.
# They get new ids and start unticked; his notes stay in the database under the old ids and are quoted.
rep('dict(id="s2-devtest", t="Play the dev game on your iPhone and tell us what you find",\n         d="You wrote that you are playing now. Everything',
    'dict(id="s2-playnotes", t="Tell us what you found in your playtest",\n         d="At 5:23 PM you wrote: Will playtest now and let you know. Everything')
rep('dict(id="s2-questionnaire", t="Fill in the maturity questionnaire, last",\n         d="You said you will leave this to last, and that works.',
    'dict(id="s2-maturity", t="Fill in the maturity questionnaire, last",\n         d="You wrote: Will leave this to last. That works.')
rep('you confirmed six players and gave a new private server price, which we now set, computer use is allowed,',
    'you confirmed six players and gave a new private server price, which we set for you, computer use is allowed,')
rep('Tick each one when it is done. The box under each is for a note.</p>', 'Tick each one when it is really done. The box under each is for a note.</p>')
rep('What you decided tonight is at the top of <a href="#saved">What is saved</a>.', 'What you decided tonight is in <a href="#saved">its own list</a> just below.')
rep('Gameplay-Engineer is making the five passes and eight products on the dev game with the group key first.', 'Gameplay-Engineer has the job: the five passes and eight products on the dev game, with the group key first.')
open(p, "w", encoding="utf-8").write(s)
print("ok b")
