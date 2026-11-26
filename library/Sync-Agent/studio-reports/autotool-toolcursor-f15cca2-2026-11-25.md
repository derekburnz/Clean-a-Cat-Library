# autoTool and toolCursor, main f15cca2 (includes a43a67d), 2026-11-25
Local unsaved place. Views: iPhone 13 frame 750x390 (stands in for iPhone 12, no preset), iPad 10th gen preset 1178x819. Pictures: draft PR #402.

autoTool: PASS in every captured view, washChecklist on and off. No tool tray; nothing left in the old tray area. Step pips show on the phone even with the checklist on (no room for the list). On iPad with the checklist on the tick list takes the pips' place. Top line names each step: Scrub the mud, Brush the fur, Pick a bow, Take the photo. Missing view: Suds's wash on iPad with the checklist on.

toolCursor (real drags; tool position vs touch logged every frame):
- PASS: sponge then brush follow the finger. Nothing shows on bow or photo taps. On lift the tool shrinks 1.0 to 0.6 over 0.1 s, then hides. At the left edge the tool flips right and is not cut off. Tool only shows when a drag starts on the cat.
- FAIL, covers his face: phone, touch on the cat's left half (x 359 to 367) puts the tool up-right over his face; at x 351 to 355 it goes left instead, so a small stroke there flips side to side every frame. iPad, touch below the face on the right half (610,320) puts the tool up-left over his chin: tool top y 237, head box runs to y 258. The head check uses the head centre (y 191), more than 1.25 tool sizes above the touch, so no flip.
- FAIL, top edge: dragging from the cat up to touch y 4 puts the tool at GUI y -63 to 0, top 5 px off the screen, inside the top bar strip, covering the step line.
