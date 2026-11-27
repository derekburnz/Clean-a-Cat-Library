# Motion-FX capture sheets, 2026-11-26 (Studio, iphone_13 frame)

Build: main cea951b2 (includes PR 897). Unsaved local place from rojo, every off-by-default switch on except toolCursor, streetLoadTest, exampleFeature, openingReplay; switches flipped locally with LiveFlag_<key> attributes on ReplicatedStorage from the server. Seeded save. Frames are cut from Studio video captures (592 x 272) with ffmpeg; times are seconds into the clip or after the tap, about 0.1 s accurate. Cats in the tub were drawn as Rosette and Djinn by re-sending CatReady on the client (the server's cat was another kind).

## tubLife
- tublife-off-frame1-0.5s.png, frame2-0.8s, frame3-1.1s: LiveFlag_tubLife false, Rosette in the tub, tap running.
- tublife-on-frame1-0.5s.png, frame2-0.8s, frame3-1.1s: switch back on, same wash.
Note: the switch was flipped mid-wash; the off frames still show rising bubbles, so tubLife may read the switch only when the wash starts. Not a clean A/B.

## photoFx
- photofx-off-0.2s/0.5s/0.7s/1.2s-after-tap.png: switch off. The camera vanishes about 0.5 s after the tap, no LED blink, then the bubble wipe back to the spa.
- photofx-on-0.2s/0.5s/0.7s/1.2s-after-tap.png: switch on. The LED blinks red three times over about 0.8 s, then the bubble wipe starts about 0.9 s after the tap. No flash and no printed card were seen before the wipe covers the screen.

## washPops (with washMeter)
- washpops-1-nice-combo-x3.png: "Nice!" over the step dots and "x3" by the cat during a quick run of scrub hits.
- washpops-2-nearly-there-combo-x4.png: "Nearly there!" with "x4"; the bar reads "Almost!".
- washpops-3-squeaky-clean-done-word.png: "Squeaky clean!" as the scrub finishes; it is drawn over the step title "Step 2 of 4 · Brush the fur" for about 0.5 s.

## Bow recheck (PR 897), head piece cats
- bow-royal-rosette-full.jpg, bow-royal-rosette-zoom.png: Royal (Satin tier) pink bow on Rosette. BowScale 0.6, bow 1.04 x 0.55 x 0.47 studs, on the head's top right corner as seen, sticking 0.40 stud past the head edge (intended). Its loop goes into the crown: 10 bow parts overlap the head piece (Prop).
- bow-golden-djinn-full.jpg, bow-golden-djinn-zoom.png: Golden pink bow on Djinn. BowScale 0.6, bow 1.01 x 0.43 x 0.49, top right corner, 0.25 stud past the head edge. Its left loop cuts into the turban (head piece Prop overlap).
Per the brief, cutting into the head piece is a fail for both.

No player names appear in these pictures.
