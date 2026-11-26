# Job 5 (issue 872, PR 882; PR 854 cards), main bd424b5 (RC session text)
Unsaved local place, iphone_13, all off-by-default switches on except toolCursor, streetLoadTest, exampleFeature, openingReplay, benchGrow. Seeded save. A LocalScript logged every frame from the join.
Take prompts at join: FAIL on the 1 s rule, PASS on the cause. Customers walk in with crates at the join.
Run 1 (R15): 2.19 s 3 cats drawn, SpotQueue1 prompt present; 2.59 s it is gone; counter prompts at 5.10, 7.12, 7.62 s.
Run 2 (R6): 0.77 s 2 cats, 1.21 s 3 cats; no SpotQueue1 prompt in any frame; counter prompts at 4.75, 7.27, 7.77 s.
Each prompt within about 0.5 s of its cat's CounterReadyAt: syncCounter waits for the cat to sit. Issue 872 (no prompts until a serve) is fixed. Not met: 1 s from the join, and run 1 showed the old SpotQueue1 prompt for 0.4 s. A join to an already seated line (second player): NOT TESTED.
Newcomer cards (PR 854): PASS. 7 newcomers at place 3 (52 to 192 s) each had a card in the first frame; the 4 at the join too.
Walks: Counter1 R15 path 3.6 s; R6 path 3.6 s; midpoint path 0.6 s; all reached.
Console: no errors from our scripts; three rbxassetid://203785492 type mismatches (not in src).
