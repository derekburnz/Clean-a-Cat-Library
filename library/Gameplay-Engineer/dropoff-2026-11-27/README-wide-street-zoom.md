# Wide street (887) and zoom out (885), main 5073f46

Unsaved local Studio place built with rojo from origin/main 5073f46. Every off-by-default switch on except toolCursor, streetLoadTest, exampleFeature and openingReplay. Seeded save, iphone_13 frame. Never dev or live.

## 887 wideStreet: PASS
- wide-street-before-56-apart.jpg: wideStreet off, plot centres 56 studs apart.
- wide-street-after-84-apart-gardens.jpg: wideStreet on, plot centres 84 apart (x -173, -89, -5, 79, 163, 247), gardens between the spas.
- wide-street-opening-box-landed.jpg and wide-street-opening-pick-him-up.jpg: fresh save opening on the wide street. The truck moved 0.36 s after the join, and the box landed in front of the spa.
- Fresh save parts: 4,369 with wideStreet on against 3,914 off. Frame rate 240 fps on the PC (its cap).
- Customers in other plots and Visiting: not testable solo.
- One qaWalk stall at the plot slab edge (issue 994). This is a test walker problem, not the game's.

## 885 zoom out: PASS
CameraZoomController.MAX_ZOOM 40 and Player.CameraMaxZoomDistance 40. Workspace.Terrain has 0 cells. The camera was held at the full 40 studs from a head point at y 5:
- zoom-max-west-end.jpg: from the plot 5 end of the street, looking west along it.
- zoom-max-looking-north.jpg: from across the street, looking north over the plots.
- zoom-max-looking-south.jpg: from the street, looking south at the far-side houses.
- zoom-max-steep-down.jpg: pitched 70 degrees down over plot 6.
Each view ends in hills, mountains and sky. No map edge, void or bare baseplate shows anywhere.
