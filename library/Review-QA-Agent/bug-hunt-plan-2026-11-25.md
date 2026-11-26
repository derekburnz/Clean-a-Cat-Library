# Bug hunt plan: full playtest-worthy draft on dev (Review-QA, 2026-11-25)

Derek, 2026-11-25 23:24 UTC: "good to draft entire playtest worthy game now and playtest in studio for bugs!"
Sync-Agent drives Studio on Derek's PC; Review-QA is the gate and files the issues. Dev only, never live, never save the QA place.

## How each pass runs
1. Sync-Agent reports the main sha it pulled and the dev switch list (flags.sh dev output), both copied exactly.
2. Run the pass on the 844x390 iPhone frame first, then iPad. R15 first, then one R6 run of the carry steps.
3. Report per check: PASS / FAIL, a picture for every FAIL, and every console line that is not on the known list
   (Studio MemoryStore/DataStore lines; the 3 "rbxassetid://203785492 asset type does not match" lines at the opening).
4. Review-QA turns each FAIL into a GitHub Task issue (area label, severity S1-S4 from the playtest-report skill) and
   writes docs/playtests/<date>.md through a docs PR.

## Order of coverage (most player impact first)
A. First 5 minutes from a fresh join (fresh save): truck scene starts at once, no loading screen; Suds box, lift,
   carry, place in tub; the taught wash steps; first payout; first customer walk-in (a Common at dirt level 1, the second at level 2, per tuning dirt.tutorial). Time each beat.
B. One full customer: door, carry the carrier's cat, tub, every wash step for its dirt level, wash meter and shake-off,
   rinse, claws (PR 492: keep dragging through the Bubble Bath end, claws must wait for a new press), dry, bow, photo,
   recap pay lines add up (wash coins x 1 / 1.25 / 1.6 / 2 by dirt level, tip and bow unscaled), coins and XP land.
   Sounds (PR 535): once each Moment exists, heartLow, catLeave, crateOpen, petReveal, starUp, workerDone, buildDone,
   questDone, checkIn play with no 'failed to load' line.
C. Every station built and used once: Brush Table, Blow Dryer, Bubble Bath, Pawdicure; build timers; builder kitten.
D. Special visitor (when it lands): lilac customer, royal carrier, special cat pieces clear of bow; Stardust, Sherbet,
   Jade Neon at the wash camera (eyes at least 2:1 vs face, nothing clips to a white blob).
E. Menus: bench "Who's next?", Index, Tools, Helpers, Quests, Settings, Gift stand, Starter pack (timer real, never
   restarts, gone at zero; bob 3 times then still). Every close button works; nothing opens by itself in session one.
F. Saves: leave and rejoin; coins, tools, stations, Index, quests, first-join stamp all kept. Day-2 return path.
G. Two players in one server: carried cats visible to the other (carryShared), visitors toggle, no cross-plot actions.
H. Speed: iPhone 12 budget (docs/playtests/speed-budget.md) during a busy wash with 3 carriers in view; 20-minute
   memory reading.

## Pass rule
No S1/S2 bug, no new console error, every step reachable on touch alone.

## Added checks (2026-11-26 UTC, from reviews)
- D: pet reveal in the world (PR 561): head and tail stay on the body during the pop; wiggle after; normal motion after 10 s.
- D: Royal bow on Rosette and Stardust (PR 556): no clip with the crown or the stalk gem at the wash camera.
- D: visitor star (PR 549) loads, sits clear of the hat; outline gone by about 3 s.
- E: starter pack only on a fresh save (PR 554: older saves have a past end). Attention sparkles (PR 555) load.
- B: promptFocus (PR 550) pill check; meter starts at 0; walk-off (PR 552) after 10:00; moods (PR 536).

## Test movement (added 2026-11-26)
Every Studio run moves the character only with the `studio-test-movement` helper (`_G.qaWalkNamed("<Spot>")`). Never use `character_navigation`, held W/A/S/D, or a straight `MoveTo`. Report each walk as reached, method and seconds. Wall, door and slab checks also include a moving jump (A or D plus Space), on both R15 and R6.
