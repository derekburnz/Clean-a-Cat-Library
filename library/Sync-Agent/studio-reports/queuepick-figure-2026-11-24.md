# PR #208 queuePick figure check, main bc53507: FAIL (2026-11-24)

Setup: fresh local place, never saved. spaPlot, customers, customerFigures, queuePick, scrubPrototype on. First visit finished so picks unlock. All three waiting cats were Tux.

Attempt A (E at the door): place 2 prompt nearer (3.1 vs 5.6 studs), so place 2 picked. Result: place 1 unchanged (Scarf), place 2 became the old place 3 (pastel orange SunHat), place 3 a new look. The picked ToteBag customer vanished; the front never changed.

Attempt B (RequestPickCustomer(3) fired from the client; E could not land on place 3, character wedged against figures): place 1 still Scarf, place 2 unchanged, place 3 became a new Scarf look. The picked mint SunHat customer is gone from the line, not at the front.

Likely cause (from reading FigureService at bc53507):
1. picked() moves the look to the front correctly.
2. SpaService then calls sendQueue, showQueue runs looksFor(), which checks movedUp(old, new) first.
3. When neighbouring cats are the same kind (all Tux here), movedUp() is true though nobody moved up. looksFor drops the front look (the one just picked) and adds a new one at the back.
Misfires whenever two adjacent cats in the line are the same kind (common with 4 common cats).
Fix ideas: picked() sets a flag looksFor checks first, or looksFor tests for a pick before movedUp.

Cat kind not tested here (all Tux); the earlier run on 93748d3 showed the right cat (Toffee) arrives.
Console: no game errors, only no-DataStore notices and three rbxassetid://203785492 lines.
Shots (on the PC): Downloads\Clean-a-Cat-captures\queuepick-figure-before.jpg and queuepick-figure-after.jpg (attempt B).
