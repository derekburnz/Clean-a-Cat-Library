# Restaurant Tycoon 3 screenshots: what helps our plan  (2026-11-24 ET, Planning-Agent)

Derek played Restaurant Tycoon 3 on his phone and sent 20 screenshots. His words: "they don't use friends as waiters or customers can take some ideas from them". The pictures and a list of them are in `Coordinator/references/restaurant-tycoon-3-2026-11-24/`. They are reference only and stay out of the public repos. Clean a Cat is original: we take ideas about how things work and never their art, names, wording or layouts. Numbers in brackets are the picture numbers in that folder.

## Friends as customers
Restaurant Tycoon 3 does not do it. The shop game that has lasted longest goes without, and My Pet Salon is the only game we know that does it. Our pick on the plan page (`friendcust`) is now no friends as customers at launch. It waits for Derek's tap or word. Their start window has a Managers row with a plus button (4), which looks like a way to let a friend help run the place. That fits our own plan: a bonus for a friend in the server now, and friends helping in the spa later behind its switch.

## Ideas worth taking, in our own form

| What they do | Where | What we do with it | Who |
|---|---|---|---|
| One goal bar at the top with a count ("Cook 5 dishes", 0 of 5), a new goal when one is done. | 5 to 7, 10 to 12 | One line goal with a count at the top of our screen. Suds points at it once. Plan page question `hud`. Theirs has a skip button on the bar. Ours has no paid skip. | Design-Agent |
| The work is one short swipe with a bar that fills and a Cancel button (8, 9). | 8, 9 | Confirms short jobs done by hand. Ours has several kinds of step and never the same step twice in a row. We take the Cancel button, so a player can leave a wash. | Design-Agent, Gameplay-Engineer |
| A trail of arrows from the player to the customer and one plain line at the bottom that says what to do, with Cancel. | 10 | Our trail already exists. The plain line fits the carry: one line while the kitten is in your arms. | Design-Agent |
| "A VIP Customer just entered your restaurant!" with a Show Me button. | 11 | A rare visitor gets one line and a Show Me button that points the trail at them, so nobody misses one. Plan page question `rare`. | Design-Agent, Gameplay-Engineer |
| Upgrades window with two tabs, what you can buy now and what is locked. Each locked one says "Requires" and the upgrade before it. | 12, 15 to 18 | The best idea in the set for a reason to come back. Our upgrades window shows the road ahead: the next two or three locked things and what each needs. Plan page question `longbuild`. | Design-Agent, Planning-Agent for the chain |
| Upgrades add new things to do, not only bigger numbers: drinks, a kids menu, delivery with a driver, more floor space. Advertising raises how often customers come. | 12, 15 to 18 | Our chain mixes the same kinds: a new service (nail trim, blow dry), a new kind of customer, more room, a door sign that brings cats more often and a tip jar. | Planning-Agent, once the loop is picked |
| Workers have a name, a job, a hire price and a price to level up. Some upgrades need staff at a level ("Staff must be level 3"). | 13, 14, 12 | Matches human staff, Derek's pick. Ours: Jo and Sam, hired and levelled with coins. A tool that needs a worker level links the two upgrade paths. | Design-Agent, Gameplay-Engineer |
| You choose your plot from a map view and pick one of several building looks. | 1 to 3 | A choice of spa front is a cheap way to make the place feel yours. Ours comes after the first wash, never before it, because the truck scene has to start the moment the character loads. | Model-Agent, Design-Agent, later |
| A clock for the day in the corner (Day 1, 8:00am). | 5 to 20 | Maybe later. A spa day that ends in a short summary could give a session a natural end. Not for the first build. | Planning-Agent, parked |
| A town with other shops and houses around the plots. | 19, 20 | Matches our shared street. Nothing to change. | none |

## What we do not take, and why
- Three setup screens before the first customer: claim a plot, pick a design and a window with a name, a starter food and managers (1 to 4). Ours has the first tap at about second 4.
- A typed name for the place (4). Typed text from young players needs filtering, and typed names are out of scope for now. If Derek wants spa names, they come from word lists.
- A starter pack with a countdown and an event button on the screen in the first minute (5). Our rule: no offer on screen in the first session and no countdown on an offer.
- A premium worker shown in the same list as the workers you hire with cash (13, 14). Ours sells nothing that skips the game.
- A skip button on the goal bar (5). Paid skips are out.

## Things to check
- Whether the skip on their goal bar costs Robux or only hides the goal. Derek can say if he pressed it.
- How their staff compare with the player for speed, and what happens when a customer waits. The pictures do not show it, and the plan page fields for this game were left empty.
