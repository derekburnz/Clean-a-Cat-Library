---
name: suds-opening
description: Derek's decisions of 2026-11-24 for the game's opening (a watched truck intro, a muddy kitten in a brown box, washing him is the tutorial, he becomes Suds) and Suds as a four legged mascot; what is built and what is still open
metadata:
  type: project
  modified: 2026-11-24T17:25:08.951Z
---

Derek's words, 2026-11-24 12:21 PM ET (a lean, not a locked decision): Suds "shouldn't stand". The game could open with "a quick scene": a truck drives past, a box falls off the back and lands in front of you on the street, you open it and it is Suds all muddy, the tutorial is cleaning him and getting a score, then he stays "as your spa mascot through the game that explains stuff/is used for when you unlock new things". He said "somehow maybe", so how Suds is found is open.

Earlier the same day he said ok to: human staff do the washing, Suds stays as a mascot who never washes (plan page `q2-helperlook`, option 1). Builder kitten for stations: still open.

How it is written up (Planning-Agent/gdd-proposed.md, sections "Name and first minute", "Suds, the mascot", "First session" and "Checks on the Suds opening"; step by step plan by Design-Agent in Design-Agent/first-session-2026-11-24/opening-and-tutorial-plan.md):
- Truck passes in about 3 seconds as a watched intro (decided, see below), tap the box at about second 4, scrub at about second 12. Plays once per save.
- Suds's wash always ends on three stars. He is the same for everyone, has his own card outside the index count (decided), sits on a cushion on the front desk, does not sit in the window and earns no tips.
- After Suds comes the guaranteed easy common customer cat (first coins, tip and index stamp), then the bench pick opens at about 1:45. First window stray at about minute 4.
- Suds as guide: four paws, trots to a new thing and sits by it with a bubble of a few words. Shows each thing once, never opens a window, never points at anything that costs Robux, never sad or cross, also not on day 2.
- The opening and the guide each ship behind their own off switch so the first test can compare against spawning at the tub.

DECIDED by Derek 2026-11-24 12:27 PM ET: the box is "a random brown box", NOT a soap crate (we proposed a crate because My Pet Salon also opens with a muddy cat in a box; he said no, do not raise it again). The kitten has no name until he is clean, then "he becomes suds". Suds is not in the Cat Index ("dont include him").

DECIDED by Derek 2026-11-24 1:36 PM ET ("A for sure for truck"): the scene is a quick intro the player watches, the truck going by and the box falling in front of them, about 4 seconds, then the camera comes back. The played version is dropped. Saved on the plan page as `q2-firstminute` option 0. The scrub starts about 9 seconds later than spawning at the tub, and the switch allows a test against the tub start.
- For Gameplay-Engineer: SpaService opens bench picks when the save has stars above zero. Suds's stars would open picks one cat early, so the gate has to count customers served.

See [[planning-status]] and [[art-and-models]].

BUILT 2026-11-24 ET (game PRs 289, 291, 292, 295, claim issue 285), all switches OFF: sudsWash (a new save's first cat is the kitten; no bows; card "Meet Suds!", 3 stars as a score only, nothing paid or stamped; save field suds 0/1/2), openingBox (needs sudsWash; server holds the kitten until the player's own box tap, player stands on SpotOpening on the near pavement, box on SpotBox), sudsMascot (Suds on CleanACat_Prop_SudsBed at SpotMascot by the door, tap = purr and hop). Still to do before the switches go on: a Studio playtest of the three, the bed prop, and wiring Suds's uploaded portrait id into UI/Portraits (black cat glyph until then).


- Carry hold pose: Derek said 2026-11-24 ET the hold was wrong. His example is in (confirmed "sent" 3:31 PM ET): a clip in Coordinator/references/carry-hold-2026-11-24/ and six screenshots of the carry in his Catch a Cat Cafe (cat held high against the chest, both arms around it).
