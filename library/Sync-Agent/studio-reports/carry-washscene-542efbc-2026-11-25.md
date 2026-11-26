# Customer carry, wash scene, toolOnCat, close-up question, main 542efbc (#410, #411; also 5a9e0f0, 25eb648), 2026-11-25
Local unsaved places, iPhone 13 frame (stands in for iPhone 12), single client. iPad not run. Draft PR #412 (pictures, numbers from earlier builds too).
Setup: every switch on (closest match to dev I could read from the repo); off: toolCursor, test-only switches, strays (so the first cat after Suds is a customer). carryShared on, no new warnings. Studio graphics tier was low, so the wash scene blur was never created; fps from a desktop (240 avg, worst frame 7 to 8 ms), not a mid-tier phone.

Customer carry:
1. PASS. After "Open the spa!" camera eases back at FOV 70; front customer keeps the cat in the carrier, "Take cat" is the only prompt.
2. PASS. "Take cat" puts the cat in your arms, that customer leaves, line refills (E within 10 studs; a click on the pill did not register in the simulator).
3. PASS with a problem. "Put in tub" starts the wash scene the same frame, no gap; the new cat sits in the tub 0.45 s later. PROBLEM: the last washed cat is never taken out of the tub: clean Suds sits in the tub while also on his bed through the whole carry (picture in the PR; same on 5a9e0f0).
4. Wash scene: cat fills 0.64 to 0.65 of screen height (target 0.55) at FOV 50. Step line and Walk bar clear, but step pips sit over the cat's ears. FOV back to 70 on exit. Blur not created at this tier.
5. Second customer works. After Next cat two "Wash next" prompts show about 19 s, then "Take cat". PROBLEM: the two "Wash next" prompts come back while carrying, next to "Put in tub".
6. FAIL: reset while carrying. CarryCat stays set and "Put in tub" is offered, but the carried cat model sits at the world origin (0,0,0), not in the arms.
7. Console: no new game errors (Studio MemoryStore and DataStore lines; 3 "rbxassetid://203785492 asset type does not match" at the opening).

Wash scene problems: Pick a bow: BowPink off the left edge (x -21), the other two at the very edge (x 39, x 83). Trim the claws: shot looks from the tub's front, but at the Pawdicure the cat faces sideways; rays to both claws hit the Pawdicure station first so paws cannot be touched (claws finished with the test hook).

Tool on cat: PASS sponge 0.02 to 0.04 studs off the fur (neither sunk nor floating); size 54x43 px in the old close-up, 101x79 to 122x92 px in the wash scene. PASS brush 36x48 px; bubble sponge about 135x120 px. Clipper 19x59 px on 25eb648 and it never shows in the wash scene (paws behind the station). PASS see-through 0.60 on the head, face shows. PASS goes away on lift, on sliding off the cat, on step change; nothing on bow or photo taps. PASS Suds's front mud and brush step finished with real drags. OPEN: twenty swirls did not finish a customer's suds; I finished it with the hook and did not pin down why.

Customer close-up question: on 25eb648 (washView without washScene), after Suds's photo the camera eased out to a far shot 38 studs away; the cat filled only 0.12 of screen height; it stayed there (not the player's view) about 20 s until the next cat; then the first customer's close-up eased in over 0.6 s to 0.36 to 0.40, avatar hidden. That far shot after Suds may be the "zoomed out" Derek saw. On 542efbc the normal player view shows the cat at 0.30 to 0.36 and the wash scene at 0.64 to 0.65, avatar hidden. Camera stays on the player view with: washView off, Walk button stepped out, visit stage "waiting" or "done", and with customerCarry until "Put in tub".
