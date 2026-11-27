# Carrier float (871), main c2eeb78 (with PRs 1008, 1009, 1010 and 1011)

Unsaved local Studio place built with rojo from origin/main c2eeb78. Every off-by-default switch was on except toolCursor, streetLoadTest, exampleFeature and openingReplay. Seeded save, desktop frame. Never dev or live.

## Files
- walk-in-and-set-down-street-side-c2eeb78.mp4 (12.7 s): newcomer Pip walks in, filmed close from the street side at the hand's height, and sets the crate down at counter place 1.
- walk-in-from-behind-c2eeb78.mp4 (10.6 s): newcomer Juno walks in, filmed close from behind.
- walk-in-from-street-side-c2eeb78.jpg: Pip mid walk with the carrier in the right hand. No cat beside the line.
- walk-in-from-behind-c2eeb78.jpg: Juno mid walk with the blue carrier held by its handle.
- set-down-at-place-1-c2eeb78.jpg: Pip at the mat after the set-down.
- walk-out-packed-cat-7e033d1.jpg: Kit walking out with the packed cat in the carrier (main 7e033d1, PR 1010).

## Hand Grip and Carrier Grip (newcomer Mo, sampled every 0.5 s)
- Mid walk: t1.5, hand Grip (-1.34, 2.74, -35.34), Carrier Grip (-1.34, 2.74, -35.34), distance 0.00.
- At set-down (on the mat): t4.0, hand Grip (13.87, 2.74, -30.77), Carrier Grip (13.87, 2.74, -30.77), distance 0.00.
- All 22 samples over 10.6 s read 0.00.
- The Carrier's parent is CleanACat_NPC_Customer_Mo_ArmR the whole time.
- Walk-out with a packed cat (main 7e033d1): the PackedCat sits inside the Carrier, 1.47 studs from the figure at every sample (Theo 13 samples, Kit 12). The NPC rig names its hand attachment Grip on ArmR.

## Counter cats
On 208dc9d, 7e033d1 and c2eeb78, every place reads N of N parts on its mat, and newcomers show 0 counter cat parts while walking in.

## Not tested
R6 and R15 player views: the customers are NPCs with a single rig, and the player's own rig does not change how they are drawn. I did not switch the player rig for this.
