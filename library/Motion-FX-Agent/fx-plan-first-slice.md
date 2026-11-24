# Clean a Cat: effects and sound plan for the first slice

Motion-FX-Agent, 2026-11-23 ET. Draft, built on Planning-Agent/gdd-draft.md (design not locked). Changes when the GDD changes.

## Goal
The first 40 seconds (scrub, reveal, fluff, photo) must feel great on a cheap phone. Every touch gets an answer within one frame, the reveal is the payoff, and nothing is loud or flashy. Effects and sounds run only on the player's device and only listen to moments.

## Moments (one shared list for effects and sound)
Gameplay-Engineer fires these as client signals; effects and audio subscribe. Names are PascalCase and live in one place (src/shared or the Effects README, agreed in the hook issue).

| Moment | When | Payload |
|---|---|---|
| ScrubStart / ScrubStop | finger down or up on the cat with the sponge | cat, hit point |
| ScrubMove | each frame the sponge is dragging on the cat | hit point, normal |
| MudPatchCleared | one mud patch vanishes | cat, patch position |
| CatClean | the last patch is gone | cat |
| BrushSwipe | one brush stroke lands (1 to 3) | cat, stroke index |
| CatFluffed | third stroke done | cat |
| BowChosen | player picks a bow | cat, bow id |
| PhotoTaken | before and after card shows | cat |
| CatToWindow / CatReturned | stray hops to the window, customer cat goes home | cat |

## Effects (VFX-Agent mode)
| Moment | Effect | Phone budget |
|---|---|---|
| ScrubMove | Foam: soft white bubbles spawn at the sponge point, drift up, pop. One pooled emitter moved to the hit point. Rate scales with drag speed. | Rate 8 max, life 0.8 s |
| ScrubMove | Bubble Soap tool: wider ring of bubbles. Golden Sponge pass: gold-tinted bubbles, same count | same |
| MudPatchCleared | Mud chunks: 4 to 6 brown flecks fall and fade; patch decal fades out over 0.15 s rather than vanishing | Emit 6 |
| CatClean | Reveal: a quick wipe of the coat (dirty overlay fades out top to bottom 0.4 s), 8 sparkles, cat shake-off with water droplets | Emit 8 + 10 |
| BrushSwipe | Fluff: fur puffs in the coat colour along the stroke, cat body scales up 3 percent per stroke (Back Out, 0.2 s) | Emit 6 per stroke |
| CatFluffed | Soft glow pulse on the cat outline (one Highlight, destroyed after 0.6 s) | 1 Highlight |
| BowChosen | Bow pops in (scale 0 to 1, Back Out 0.25 s) with 3 tiny hearts | Emit 3 |
| CatToWindow | Hop arc tween to the cushion, small dust puff on landing | Emit 4 |
Reduce Motion on: no scale pops, no shake, sparkles kept but halved. Never more than three flashes a second, no full-screen flash.

## Animation (Animation-Engineer mode)
Procedural first, on the shared cat rig from Model-Agent: idle breathing and tail sway, a shake-off on CatClean, a happy wiggle on CatFluffed, the hop to the window. Clips only if procedural looks stiff. Needs agreed part names (Body, Head, Tail, Ears) with Model-Agent.

## Sound (Sound-Agent mode)
Cue list first, no file before a cue row. Soft and short; the player's own action is loudest.
| Cue | Moment | Character |
|---|---|---|
| scrubLoop | ScrubStart to ScrubStop | gentle wet sponge loop, pitch follows drag speed |
| bubblePop | ScrubMove (gap 0.12 s) | tiny soft pops, 3 variants |
| mudPlop | MudPatchCleared | small wet plop, pitch rises as fewer patches remain |
| revealChime | CatClean | short bright two-note chime |
| catShake | CatClean | fur shake with droplets |
| purr | CatFluffed | short purr, 2 variants |
| brushSwish | BrushSwipe | soft swish, pitch up per stroke |
| bowPop | BowChosen | light pop |
| camera | PhotoTaken | soft shutter |
| meow | customer arrives, cat in window | short friendly meow, 3 variants |
| music | spa bed | calm, light, two tracks alternating |
Sourcing order from audio-pipeline: Creator Store first (no upload, use inside Roblox only), then our own synthesized blips, then CC0. Owner listens with a short listening list.

## Order of work
1. Moment list and hook issue to Gameplay-Engineer (blocks everything else): Clean-a-Cat #3.
2. Scrub feel (#4): foam, mud chunks, scrubLoop, bubblePop, mudPlop. Build first, because the GDD says if scrubbing is not fun, stop.
3. Reveal (#6): dirty overlay fade, sparkles, shake-off, revealChime, catShake.
4. Fluff and bow (#7): fur puffs, scale steps, glow, purr, brushSwish, bowPop.
5. Audio module and cue table (#8), sourcing and license log.
Later, not in this slice: build finish celebration, tip jar, window cat idles, page video.

## Depends on
- Issue 1 (seed the game repo) for the Effects and Audio folders.
- Gameplay-Engineer's scrub prototype for the moments.
- Model-Agent's cat rig and coat setup (how the dirty overlay is drawn) and the style guide palette.

## Notes from review
- Review-QA, PR #28: the PR that fills in the first sound ids puts playback behind a LiveFlags off switch.

## Creator Store alternates (Sync-Agent search, 2026-11-23 ET)
Both cues already have synth versions (PR #60). If Derek prefers a recorded sound when he listens: scrubLoop 9125408737 "Brush Spinning Rubbing On Wood Circular" (ProSoundEffects, 3.1 s) or 9117187720 (1.3 s); catShake has no real fur shake, closest are water sloshes 9120582975 (0.6 s) and 9120583261 (0.8 s). Skip 98433355182276 (user upload, license unclear). Full list: Sync-Agent/studio-reports/audio-search-2026-11-23.md.
