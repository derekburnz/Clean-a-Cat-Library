# Satisfying cleaning: what makes a hands-on scrub feel good and stay good (notes, read 2026-11-24)

Method: web search plus page fetches. Fetched pages were summarised by a small model, so quotes are as returned there, not checked against the original page. Search gave link lists only. Tags: [developer statement], [research], [data], [opinion]. All "read" dates are 2026-11-24. Nothing here suggests copying any game's name, characters or art. Coverage is PARTIAL; gaps are stated per section.

Already covered elsewhere (not repeated): spa-research-notes/spa_salon_games_outside_roblox.md (Toca Hair Salon 4 shampoo station, Sally's Spa, Nintendogs, Spirittea).

## 1. What makers of satisfying cleaning games say

### Takeaway
Developers say very little about the mechanics of satisfaction in so many words. What they do say clusters around: visible, immediate progress; no time pressure; familiar tools; and sound that makes objects feel tactile. Almost nothing public explains the "last 5%" problem beyond one tool-based answer.

### Cited findings
- PowerWash Simulator, FuturLab. Development director Kirsty Rigden "always loved games where you see immediate visual progress" (de Blob cited). Enemy threats and time limits are "deliberately absent" so players go at their own pace. Players most often call it "Satisfying". [developer statement] Kotaku, 2022 (date not shown on page). https://kotaku.com/powerwash-sim-devs-on-making-cleaning-fun-advanced-cro-1847319502
- Lead designer Nick McCarthy: the team should have recognised "the power that an incomplete, dirty thing can have"; there are "different ways that you can turn something from dirty to clean"; keeping tools familiar was a priority. [developer statement] GamingBible, 2025-10-23. https://www.gamingbible.com/features/powerwash-simulator-2-interview-473041-20251023
- Last-bit problem: Dan Chequer says the adaptable nozzle lets players "get that last nice clean line" with only a few inches left; the team turned down requests for extra friction such as dirt splashing back, to stay "relaxing, zen-like". Optional waypoints highlighting remaining dirt are reported by the writer, not a dev quote. [developer statement plus writer note] GamesRadar, 2025. https://www.gamesradar.com/games/simulation/theres-a-ravenous-sense-that-people-want-to-wash-more-stuff-powerwash-simulator-2s-devs-are-rolling-out-the-red-carpet-for-cleaning-sickos-and-theyve-already-got-big-plans-for-2026
- Job length: FuturLab asked if players would "jump into for 20-30 minutes and come back to later"; they found it was not that, and built for longer play. Much of the team's work is creating new jobs "with interesting things to clean". [developer statement] same GamesRadar page. Players ended up finishing the whole campaign (McCarthy, GamingBible above).
- Dirt layers: artists built layered dirt types (rust, muddy footprints) and chose "dirt thresholds". [writer summary of developer talk] GameRant. https://gamerant.com/powerwash-simulator-game-design-new-content/
- Unpacking, Witch Beam. Sound: pick-up sounds kept short because a slow sound "felt laggy. We kept everything tight so it felt responsive and tactile"; real recorded objects rather than one item faking another; shared material sounds (plastic, glass, ceramic) reused with small "sweetener" layers; a speed-sensitive system makes a slow move on a piggy bank quiet and a fast fling rattle loudly; hero objects get unique sounds "to surprise and delight". The quiet, sparse world lets players hear the sounds. [developer statement, GDC 2022 talk write-up] Game Developer. https://www.gamedeveloper.com/marketing/auditory-tales-from-the-making-of-zen-puzzler-unpacking
- Unpacking pacing: no fail; players who miss details still progress; new interface elements arrive one at a time without tutorial boxes. [developer statement] GamesRadar, 2023-01-04. https://www.gamesradar.com/the-making-of-unpacking-developer-witch-beam-on-bringing-the-moving-indie-hit-to-life
- A Little to the Left, Max Inferno. "The sound effects play a huge role in the tactility of the objects"; everyday sounds (sliding paper, ticking dials) with musical sounds reserved for achievements and transitions; immediate feedback on every interaction plus a snapping mechanic helps placement; "We love short games that are focused in scope" with themed chapters for variety; the cat "punctuates your gameplay, sometimes as a surprise". [developer statement] Game Developer, 2022-02-15. https://www.gamedeveloper.com/design/the-methodical-catharsis-of-tidying-in-a-little-to-the-left
- Supersonic case study (Funcell trash game): "Persistent cleaning: cleaned areas stay clean" was treated as core to the satisfaction loop; many small tap-to-collect upgrades replaced long waits. No retention percentages given. [publisher statement] 2024-10-10. https://supersonic.com/learn/case-studies/funcell-and-supersonic-turn-trash-tycoon-into-a-hybrid-casual-hit/
- Voodoo/Neon Play Roller Splat postmortem (a paint-fill game, not strictly cleaning): the first build had weak D1 and CPI, which the authors tie to unclear feedback (camera hid the avatar, control latency); they sped the response to swipes to "almost instantaneous"; squish on walls made it feel powerful; onboarding levels short and easy. [developer statement] page updated 2025-02-26 (MVP 2018). https://www.gameanalytics.com/blog/key-lessons-from-developing-roller-splat-voodoo-neon-play

### Inferences (mine)
- The common thread is: the dirt is the progress bar. Every stroke must visibly change the surface, and the surface stays changed.
- Sound is the most-documented "feel" lever in the non-hypercasual sources; it is cheap in Roblox.

### Gaps
- House Flipper: no developer statement on cleaning found (search only returned House Flipper 2 interviews, not opened).
- No developer talk found for pressure-washing, rug or pet-grooming hypercasual hits from Voodoo, SayGames, Crazy Labs, Lion Studios. Supersonic page above is the closest.
- No developer statement on a progress meter or percent-complete display, or on how to handle the last 5% beyond the nozzle comment. The Epic PowerWash 2 interview failed to load.
- The Shacknews FuturLab interview (2022-07-19) had no design statements.

## 2. Game feel and juice for drag-to-scrub on touch

### Takeaway
The core texts agree that response must be near-instant and that layered feedback makes simple actions pleasing, but the public record I could actually read is thin: a talk description, a survey paper and a latency paper. There is also a counter-view that too much juice hurts.

### Cited findings
- "Juice It or Lose It", Martin Jonasson and Petri Purho, GDC Europe 2012: shows how small, simple techniques such as particles make a plain game more satisfying, enhanced live on stage. [developer statement; description only, I did not read the slides] https://gdcvault.com/play/1016487/Juice-It-or-Lose
- Counter-view: Folmer Kelly's "Don't Juice It or Lose It" argues polish can reduce immersion. [opinion] Game Developer, 2014-10-17. https://gamedeveloper.com/design/video-indies-resist-the-urge-to-juice-it-or-lose-it-
- Swink's Game Feel is summarised in Pichlmair and Johansen, "Designing Game Feel: A Survey" (arXiv 2011.09201, 2020): Swink names three time thresholds for real-time control (no values given in that paper); one cited study found medium and high juiciness beat both none and extreme. [research] https://arxiv.org/pdf/2011.09201
- Touch latency: about 2 ms is perceptible when dragging an object under a finger; about 20 ms is the just-noticeable difference for tapping; 25 to 50 ms measurably hurts task time and errors; about 70 ms affects perceived quality of a virtual button. [research, cited in a CHI 2026 paper] Schmid et al. https://epub.uni-regensburg.de/78952/1/varying-latency-chi26.pdf
- Roller Splat and Unpacking above give practical echoes: short tight sounds, near-instant response.

### Inferences (mine)
- A scrub is a drag, so the sponge or brush must stay under the finger with no visible lag; reveal of clean skin should be tied to the same frame.
- Roblox has network latency, so the scrub visuals and sound must run on the client, with the server only confirming progress.

### Gaps
- I did not read the Game Feel book itself, nor the juice slides. No source found specific to children and juice. No source found on particle counts or screen-shake for touch cleaning. Haptics (phone vibration) not covered.

## 3. Keeping a repeated action from becoming a chore

### Takeaway
Evidence is mostly developer and publisher statement, not measured experiments. The reported methods: new tools that change the job, new things to clean, a second mechanic added only after the first is learned, many small upgrades, and shorter chapters.

### Cited findings
- New jobs are the main lever in PowerWash: "much of the team's work is creating new jobs with interesting things to clean"; different tools (nozzle, surface cleaner) give different motions; players found uses the designers did not expect. [developer statement] GamesRadar 2025 (link in section 1).
- SayGames, Wasteland Life: the vacuum is learned first; the pickaxe appears only after the core is understood and opens a new progression axis; overloading hurts KPIs; layer short and long goals. [developer statement, no numbers] Game Developer, 2024-12-06. https://gamedeveloper.com/business/mastering-hybrid-casual-game-design-lessons-in-balancing-depth-and-accessibility
- Supersonic: several small collectible upgrades so "there is always something to do", cleaned areas persist. [publisher statement] link above.
- A Little to the Left: themed chapters and a short whole game as the answer to repetition. [developer statement] link above.
- Voodoo's Mob Control team built retention systems for day 30 and day 120, not only day 7. [developer statement via Deconstructor of Fun, 2023-04-04] https://www.deconstructoroffun.com/blog/2023/4/04/hybridcasual-gamble

### Inferences (mine)
- Automation taking over old tasks, combo ceilings and optional mastery were in your list; I found no source on them in cleaning games. Treat as untested design ideas.

### Gaps
- No controlled evidence that any method reduces boredom. No numbers tying a specific method to a retention change.

## 4. Designing for ages 6 to 12 on touch

### Takeaway
Children's touch accuracy is clearly worse than adults', worst at ages 5 to 7, and improves to near-adult after about 10. Large targets, forgiving recognition and visible feedback are the research-backed rules. Toca Boca's published stance is no goals, no points, no instructions.

### Cited findings
- Anthony et al., "Physical dimensions of children's touchscreen interactions", IJHCS vol. 128, 2019: gesture recognition averages about 81% for children (adults above 90%); 5 to 7 year olds worst (as low as 66% at age 5); 91% reliably only above age 10; children miss small targets more and do better as targets grow; "holdover" extra touches are common (about 4% on phones, 10% on tablets). Recommendations: enlarge active areas, use easy familiar gestures, give visual feedback for accepted input, filter holdover touches. [research] https://init.cise.ufl.edu/wp-content/uploads/sites/378/2019/03/anthony-et-al-IJHCS2019-MTAGIC-final-preprint.pdf
- NN/g (Feifei Liu, 2018-07-08): ages 3 to 5 handled tap, swipe and drag on touch; targets of at least 2 cm by 2 cm advised for young children; precise dragging was hard (a 5 year old was frustrated when a slight misplacement made an item vanish); offering both tap and drag for the same action helped. Note the 6 to 8 difficulty with dragging was found on desktop mouse, not touch. [research] https://www.nngroup.com/articles/children-ux-physical-development/
- Toca Boca: "We give you no goals or time constraints, nor do we reward certain behavior with points" (Kidscreen, 2014-02-20, https://kidscreen.com/?p=49360). "A good toy doesn't need instructions"; watch kids as "experts at play" (Kill Screen, 2015-03-24, https://www.killscreen.com/what-designers-can-learn-about-play-children/). [developer statements]
- Care and virtual pets: a pet was "doing well" when happy, healthy, full or soothed, not when it levelled up; the pleasure was watching the creature's happiness. Extended abstract, not a child study. [research, weak] Gunn, DiGRA 2026. https://dl.digra.org/index.php/dl/article/download/3066/3050/3109
- Time on mobile games: children averaged 37 minutes a day in gaming apps in 2024; Roblox 139 minutes a day globally. [data] Qustodio, page modified 2025-01-16. https://www.qustodio.com/en/the-digital-dilemma/gaming/

### Inferences (mine)
- Scrubbing is a continuous drag, which suits touch, but the active brush area should be generous and tolerant of slips.
- Kids in Roblox come for long sessions, so the first minute matters for hook, not for session length.

### Gaps
- Nothing found on session length by age for care games, failure-state testing, or text reading level for 6 to 12. Sago Mini and Dr. Panda design statements not found. BBC/Common Sense style guidance not read. The Toca pieces predate the 2024 store removal.

## 5. Retention and session numbers

### Takeaway
No cleaning-, ASMR- or grooming-specific retention numbers were found. General hypercasual figures exist and the qualitative reasons for weak long-term retention are stated by industry analysts.

### Cited findings
- GameAnalytics, 2020 data, top 5% of hypercasual games by sub-genre (timing, traversal, physics, shooting): D1 about 40 to 44%, D7 about 13 to 17%, daily playtime about 36 to 45 minutes. Cleaning is not a listed sub-genre. [data] https://investgame.net/wp-content/uploads/2023/06/Hyper-Casual-Sub-Genre-Snapshot_GameAnalytics.pdf (2021 report)
- GameAnalytics all-game medians (2026 benchmarks article, undated): D1 about 22%, D7 about 4%, D30 about 0.7%; top 10% D1 about 40%, D7 about 12%, D30 about 4%. [data] https://investgame.net/wp-content/uploads/2026/01/2026-01-20-Mobile_retention_benchmarks_2026.pdf
- Reasons given: hypercasual is "no real progression"; "you chew them for a bit and spit them out"; revenue and growth rely on ad and heavy user acquisition; lifespan about three years with most revenue in year one (Homa). [opinion and developer statements] Deconstructor of Fun, 2023-04-04 (link above). "Notoriously low medium-long term retention woes", with meta layers expected to help (DoF, 2019-12-11) https://www.deconstructoroffun.com/blog/four-reasons-why-the-hypercasual-gold-rush-is-coming-to-an-end
- Roller Splat: weak D1 tied to unclear feedback (link above).

### Inferences (mine)
- A strong first minute is the norm among top hypercasual titles (D1 about 40%); the drop between D1 and D7 is the problem a cat-care loop must solve with a second layer.

### Gaps
- No Sensor Tower, GameRefinery or Naavik pages read. No numbers for cleaning, ASMR or pet-grooming titles. The cleaning-ASMR app store listings were only seen as search results.

## 6. Checklist for the first 60 seconds of scrubbing a muddy cat

Each rule has a source; "mine" marks my own extension.

1. Put the first scrub in the first seconds with no tutorial box; show one hand-gesture hint, then let the player go. Unpacking introduces elements one at a time without tutorial boxes; Toca says a toy needs no instructions. (GamesRadar 2023; Kill Screen 2015)
2. Make the brush follow the finger with no visible lag; run scrub visuals and sound on the client. (Schmid et al. CHI 2026 thresholds; Roller Splat postmortem)
3. Every stroke visibly removes mud: dirt is the progress bar. (Rigden via Kotaku; McCarthy "power of an incomplete, dirty thing")
4. Cleaned fur stays clean and mud does not return during the job. (Supersonic case study)
5. Use layered dirt types in the first minute (thick mud, then thin film, then specks), each needing slightly different effort. (GameRant on layered dirt thresholds; mine on how to stage them)
6. Short, tight scrub sound per stroke, varying with speed and material, with a small unique sweetener per dirt type; keep the rest quiet. (Game Developer on Unpacking audio)
7. Reserve musical sounds for milestones and the finish; use everyday tactile sounds for strokes. (Game Developer, A Little to the Left)
8. Make the brush hit area generous and tolerant of slips and extra touches; no tiny controls. (Anthony et al. 2019; NN/g 2018 for 2 cm targets)
9. Use medium juice: a few particles (suds, mud flecks) and a small cat reaction, not screen shake storms. (Pichlmair and Johansen on medium versus extreme; Kelly 2014 counter-view)
10. Let the cat react to each stroke (ear flick, purr) as the emotional reward; "doing well" means happy and soothed, not points. (Gunn 2026, weak evidence; Toca no points)
11. No fail state and no timer in the first minute; do not penalise missed spots. (Kotaku on no time limits; Toca; Unpacking no-fail)
12. Solve the last 5% with a help, not friction: remaining mud spots glow or sparkle, or the brush gets a finer tip near the end. (GamesRadar nozzle quote; optional highlight reported by writer; the glow idea is mine)
13. Finish with a clear flourish within about one minute: a rinse, a visible before and after, a cat reaction, and a photo moment. First job is short and easy. (Roller Splat short onboarding levels; Toca photo booth from the earlier notes; the 60-second figure is mine)
14. Offer a second tool or new dirt after the first job, not during it, to change the motion. (SayGames pickaxe after vacuum; PowerWash tools)
15. Allow tap-to-clean spots as an alternative to dragging for the youngest players. (NN/g: tap or drag for same action helped)

## Biggest gaps
- No public numbers for cleaning, ASMR or pet-grooming retention; no timing for how long one job should be in a mobile hit.
- No developer statement found on progress meters or the "last 5%" except the nozzle quote.
- Sago Mini, Dr. Panda and child session-length research not found.
