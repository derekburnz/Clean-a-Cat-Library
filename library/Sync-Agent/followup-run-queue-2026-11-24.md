# Follow-up Studio run queue (after the pinned run on main 1a38eeb), kept by Sync-Agent
1. #365 spa sign merged as d94db45: frame is navy with a mint lip, face stays cream. Measure frame against the pink wall (aim at least 3:1) and the name text against the cream face. Face against wall stays near 1.6:1 by design (not a fail). Asked by Review-QA, 2026-11-24 21:47 UTC.
2. #361 tail fix is PR #366, merged as 161cec3: re-take the R6 carry sample. The tail base should clear the right forearm by 0 or more on every frame, walking included (was 0.27 studs penetration; the carry root moved up 0.36 studs). Asked 2026-11-24 21:49 UTC.
3. Backdrop run and seams, if worldBackdrop could not be set locally in the pinned run.
Rules: nothing merges into the pinned run; one build per run; local unsaved builds only.

## Queue update 22:35Z
- #372 (86645f6): box slides off the floor before falling. Recheck the per-frame y drop at the rear edge (limit 0.05 per frame, was 0.08 and 0.12).
- #375 (loafSide -0.45, not merged yet): recheck R6 tail vs right forearm, standing and walking (was 0.17 and 0.24 inside; aim 0 or more).
- #368 open items: bows off screen at "Pick a bow" (second cat), avatar blocking the Pawdicure paws, no ease out after Suds's photo. Recheck when Gameplay-Engineer sends fixes; then second-cat photo camera return and station return.
- Sign name text: no text source; belongs to Model-Agent or Design-Agent. Measure once it has one.
- Two clients: needs Derek or a hand run of Studio's Clients and Servers test.

## Queue update 22:42Z (Motion-FX)
- Brushing shine: sample several coat parts at different heights every frame after a stroke; top parts should brighten about 0.15 s before the bottom ones, 0.55 s in all (BrushShine writes each part's Color). Needs fluffEffects on.
- Last-stroke sparkle: pooled revealSparkle ParticleEmitter in Effects (Emit burst at the cat's middle) plus the CleanACat_Fx_Glow Highlight on the cat at the same moment. Needs fluffEffects on.
- Carry: #377 sets loafSide back to -0.2; Model-Agent takes the tail. Recheck tail vs right arm and head vs left forearm once their change merges.
- Box edge 2-frame hang is accepted.

## Queue update 22:53Z
- PR 384 (R6 loafGap6 0.4 to 0.2): after it merges and reaches dev, recheck with an R6 carrier: front and play-camera pictures (face not covered, no arm across it; draft PR for pictures), head and body overlap vs arms standing and walking (head gate 0.25), tail still clear, R15 unchanged vs baseline (head 0.240/0.268, body 0.169/0.251, tail 0.181/0.036).
- Wash flow (bows, Pawdicure, photo camera return, Walk, Suds hold): waiting on a real person trying cats on 4ae0e33 or a test hook; asked Gameplay-Engineer.
- Brush sparkle and shine order (needs the last stroke).
- Review-QA ask 22:52Z: R6 carry re-sample from a667cc6 or later (#383 tail at the hip, on top of #381). Standing and walking: tail clears right forearm 0 or more every frame; head and body overlap with arms 0.25 or less every frame; from the play camera (behind and above) and the opening shot no arm crosses his face; R15 unchanged. Combine with the PR 384 recheck (build from the later of a667cc6 and PR 384's merge).

## Queue update 22:55Z (Gameplay-Engineer, waits for #385 3f6d0dc to merge)
Full run, local unsaved build, switches incl. scrubTurn, smallPrompts, washView, fluffEffects, stations/builds/bubbleBath/pawdicure/proBrush. Test hook (Studio only): set Workspace attribute CleanACat_TestStep to any new value (e.g. a counter) and the current drag step finishes through normal code (scrub patches, brush strokes, bath swirl, claw clip). Bows and photo stay taps. Real brush stroke needs 2.5 studs of travel on the cat and 0.2 s since the last one.
Check: Suds turn (flank patches), second cat bows on screen, Pawdicure with avatar hidden, photo camera return, station return, Walk out and back, Suds hold behind "Meet Suds!", brush shine order and last-stroke sparkle, and prompt pills on the phone frame: each small, beside the box or cat not over it, hold prompts take their time, nothing covers the view.

## Queue update 23:23Z
- PR 390 (sign names over 12 chars keep 11 plus "..."): when merged, re-run only the 20-letter name from the road on the iPhone 13 frame. Leave test waits for a two-player run.
- R15 walking carry sample of at least 10 s, head overlap per frame min/median/max (head walking went 0.27 to 0.39 on 0cd502a): requested of the PC session, not yet reported.
- Suds close-up ease out at "Open the spa!" and brush shine timing: recheck after Gameplay-Engineer and Motion-FX fixes.

## Queue update 23:37Z
- PR 393 (sign in two lines: name plus 's scaled to fit, "Spa" below fixed; names over 10 characters keep 9 plus "..."): after it merges, road view on the iPhone 13 frame with 20 W's, a long mixed name, "Tester Mia" and an empty plot. Draft PR for pictures.
- Open: sudsBubble wait at "Open the spa!" (add sudsBubble to the switch set).

## Queue update 00:12Z (2026-11-25)
- PR 398 (TextWrapped false before TextScaled true): when merged, recheck the sign WITHOUT forcing scaling from the client: 20 W's, Bartholomew Montgomery, Tester Mia, empty plot, from pavement and road on the phone frame; cap heights and contrast.
- sudsBubble: "Let's open the spa!" must wait until after the "Meet Suds!" card (failed on ff0803d); recheck when Gameplay-Engineer fixes it.
- Running now: autoTool (a43a67d) and toolCursor (f15cca2) on iPhone 13 frame and iPad.

## Queue update 00:22Z (2026-11-25)
- toolCursor dropped by Derek (off on dev); its FAILs (face cover, top edge) are parked.
- Next from Gameplay-Engineer: toolOnCat (real 3D sponge, brush or clipper on the fur at the touch point); test plan comes when it merges and is on in dev.
- Carry check on 1e0b2e8 (#401, R6 loafOut6 0.3): R6 and R15, requested of the PC session; report to Review-QA with a copy to Motion-FX.
- Sign recheck on 6ebf502 (#398): requested of the PC session.

## Queue update 01:01Z (2026-11-25, Review-QA)
- R6 carry closed at loafOut6 0.3 for both rigs; missing left-side and R15-front captures need no re-run. Keep picture PRs (#409 and the other capture PRs) as drafts, never merge them into the public repo.
- Next run after #408 merges and publishes to dev: customers, customerCarry, washView, washScene, autoTool, toolOnCat on. Use the QA lists on #404, #407 and #408: take, carry and place the cat; wash scene framing and FOV back to 70 after exit; 3D tool on the fur per step, see-through on the head; mid-tier frame time with the blur.
- Already requested of the PC session and pending: toolOnCat on 25eb648 and the customer close-up zoom-out question (Derek: cat in the tub "stays zoomed out").

## Queue update 01:09Z (2026-11-25)
- Main is 542efbc (#410, #411). carryShared check needs two clients (watcher sees the customer cat and Suds across the carrier's arms within about 0.25 s; both clear on place; carrier reset mid-carry leaves no floating cat; no purr from the other player's cat; no new warnings on either client). The PC tool can start only one local client: needs a hand run of Studio's Clients and Servers test (2 players) by Derek, or a way for the PC session to start a second client.

## Queue update 01:33Z (2026-11-25)
- #416 merged at 4b6a190 (0.3 phone blur). Next dev run, washScene on, iPhone 13 frame (stands in for iPhone 12): frame time with the phone blur on vs off (note the fps is this PC's, the real phone is Derek's iPhone 12); once Gameplay-Engineer passes the cat to WashCamera.shot: fill 0.5 to 0.6 and step dots clear of his ears at the tub, Bubble Bath and Pawdicure (were 33x8 and 29x8 px overlap at the last two); no ceiling clip at the highest station.
- Wash-next prompts between customers (about 13 s, the queue pick): still open.
- After #417 merges (cat passed to the wash camera, station shots face-on): at the tub, Bubble Bath and Pawdicure, washScene on then off: his face visible (not side or back), no wall or other station blocks the shot, with the scene on fill 0.5 to 0.6 and dots clear of his ears. Combine with the #416 phone blur frame-time check and the ceiling-clip check. Run once Gameplay-Engineer or Motion-FX sends the merge commit.

## Queue update 2026-11-25 14:40Z (Motion-FX)
- Drop the furPuff check: by design BrushShine replaced it (commit e585b05, Derek asked for shine top to bottom then sparkle).
- #435 foam puffs hidden not removed: with Gameplay-Engineer; recheck after their fix (puff models and part count after pop).
- #443 bow tap slabs overlap about 20 px: recheck after the fix.
- New, once publishes land: truck door eases shut with two small bounces (PR 450): time open, close and bounces; no green stink smoke anywhere (PR 453 deleted the effect): scan the whole run for smoke emitters or green particles.

## Queue update 2026-11-25 19:56Z
- PR 492 (claws step waits for a new press): recheck the claw step after the Bubble Bath in a customer wash. Log: whether my input was still down when the bath ended; whether CleanACat_TestStep was fired at the claws step (that clips every paw at once by design); the step sequence (3 then 4 claws then 5). The earlier skip (step 3 straight to 5) was likely a drag still going when the bath ended.
- Picture PRs (#455, #418, #420 and later) stay drafts; verdicts go as comments only.
- Review-QA ask 19:55Z for PR 492 (once on dev main): customer wash with pawdicure on, keep dragging on the cat right through the end of the Bubble Bath. Pass: the claws step shows the ringed paw and clips nothing until you lift and press again; then each paw clips as before; no new console errors. Also note whether the camera turns while the held finger moves after the step change.
- Review-QA ask 20:05Z for PR 495 (Stardust's solid stars, once on dev main): repeat the Stardust wash camera capture with the same setup as picture 4 (tub seat, scale 1.5, normal spa lighting, wash camera FOV 50, 844x390). Pass: stars keep their shape (no white blob), eyes at least 2:1 against the face, no new console errors. Batch with the PR 492 claws check.
- Review-QA ask 20:23Z for PR 497 (once on dev main): add two cats to the Stardust wash camera look: Sherbet (deep pink Neon hearts on the wings, 0.3 studs) and Jade (deep gold Neon tips, largest 0.35 studs). Same setup and pass rule for each: nothing clips to a white blob, each Neon shape keeps its outline, eyes at least 2:1 against the face, no new console errors.

## 2026-11-25 23:26Z Derek's go ahead
Derek: the plan is fully answered; draft the entire playtest-worthy game now and playtest in Studio for bugs. Expect a run of Studio playtests on the PC as builders land the full game on dev; work with Review-QA. Queue stays: PR 492 claws, PR 495 Stardust, PR 497 Sherbet and Jade. Send the PC session a full-game bug playtest (first 5 minutes, day-2 return, all stations, saves, console errors, phone and iPad frames) once Review-QA or the coordinator says the full game is on dev.

## Queue update 2026-11-26 00:40Z (Review-QA)
- Filed from B2: S4 issues #570 (walk-off clip) and #571 (line flicker); my five questions went to Gameplay; #569 stays a draft.
- Next: rerun on main eab523b or newer once D (special visitor) and the visitor effect land.
- Cover the issue 541 capture (first 2 s frame by frame on a fresh save) if not already reported.
- Measure the crate odds board text height on the iPhone frame when PR 568 merges (pass E).
- G (two players) and F (saves) wait on screen control (denied; asked the coordinator).

## Queue update 2026-11-26 01:33Z (Review-QA, after B3)
- Issues: #574 (reopened, S2, boardKeys taps overlapping), #571 (line flicker), #570 (walk-off overlap) reopened; #595 (S3) tutorial bench timing filed. Expected, not bugs: no Finish now on the Third Tub (Robux products not made yet), no pet models (Model-Agent's queue).
- Next, once main moves: measure the crate window text, chance and footnote (pass E); check the Pets window fits on the phone; check the Who's next? cards with heart bars (PR 586) and the special card (PR 589); recheck #574, #571, #570, #595 when their fixes land. G and F still wait on screen control.

## Queue update 2026-11-26 02:47Z (Review-QA, after B6)
Filed: 634 (S2 saved pet missing on join), 635 (S3 Shop and Starter descriptions cut), 636 (S4 chip vs window time). Window showing minutes not seconds is intended since PR 620. The buy row is in PR 631 (not merged yet).
Once PRs 629, 630, 631 and 621 are on main, recheck: 623 to 628; 625 with all seven buttons; the crate rows (chances, Open crate and both rows on one phone screen; rows vanish with TestPaidRandomRestricted); the ask order with askQueue on; landscapeLock (621); 634 once its fix lands. Also the B5 line fixes PR from Gameplay (2 figures on a leave, newcomer early at the third place, single quest toast) when it merges.
Status: PC session got the earlier B6 list and has benchSave and 'landscapeLock' notes; send it this recheck list once main has 629, 630, 631, 621.

## Queue update 2026-11-26 03:03Z (Review-QA)
- giftStand on in dev since 9:58 PM ET (PR 639 server). The stand shows only once Model-Agent's model lands. Then: fresh save, the stand stays unlit until 7:00; a claim without the group and favourite gives a notice and no pet; a claim with both gives Starcoat in the player slot, the seat copy goes, and a second claim gives nothing.
- PR 640 (visiting), once merged: two clients in local server mode with A's visiting off: B is moved to the pavement within about 0.25 s, gets one notice per minute, A is never moved. Blocked: the PC tool cannot start two clients (screen control denied).

## Queue update 2026-11-26 03:44Z (Review-QA, after B8)
Filed: 658 (S2 crate window too tall on the phone), 659 (S3 gift lamp 3 px from the spawn), 660 (S3 first build too late). 648 closed. 649 and 609 reopened; 571 noted as 12 of 14.
Next fresh-save run: log each coin spend and the coin total at every minute (where the 90 coins went; 'Let's build!' never came, coins only 90 at 8:20). Waiting on others: claim with both steps done needs a real favourite (Derek on dev); visiting with two clients (not drivable from the PC); rename field is PR 654 (not merged).

## Queue 2026-11-26 20:58Z (new Sync-Agent; RC session waiting on Derek's approval)
One run on main e0bfa9e or newer, iPhone frame plus one desktop/iPad frame:
- Review-QA: Review-QA-Agent/dev-switches-plan-2026-11-26.md, 18 steps (bigSpa, counterLine/Cards/Crate incl. PR 785 step-up, hudTidy, fewerPills, helperPopups, buildWindow, freeRewards, abuse pass). Report as studio-reports/dev-switches-<sha>-2026-11-26.md, then ping Review-QA.
- Design (PR 793 and 798): Suds bubble portrait, Helpers HUD button, helper icon; Cat Index, recap card and bench card draw real cat pictures (no blank tiles); dirty level 2 to 4 cats show level 1 picture with dirtLevels on.
- Motion-FX: catWalkOut (wash, Next cat, copy hops out, puff, trots, fades; tub stays empty 20 s after; tap empty tub; once with Reduced Motion), counter walk-up and crate set; spaMusic: SpaA 107621531888888 and SpaB 89957079712346 IsLoaded and TimeLength, Music setting off stops music, console clean. Joining the real dev game is not possible from here: check ids in Studio only.
- Motion-FX 21:31Z (springUi pass): window and More tray open/close sounds (one each; opening from tray only open sound); helper popup one coin pop no ding; Free Reward claim one chime and three sparkles, rejoin silent; counter cards grow/fade, heart bar glides, never two cards per cat; windows ease in with no bounce. Not loud on phone frame (loudness cannot be judged by ear in Studio: report volumes), frame rate with six customers at the counter, console clean.
- Motion-FX 21:39Z: store page video and 30 s social clip shot list at Motion-FX-Agent/video-tools/shot-list-2026-11-26.md (record in a dev playtest only, post nothing). Do after the checks above.
- Model-Agent 21:59Z (issue 791, PR 831 merged 4:37 PM ET): Muffin (muddy light), Inky (dark), Rosette (head piece) in the tub brushed until fluff shows; play camera and tub close up: nothing sticks out of sides, tangles vanish one by one, fluff still shows on dark cat. One screenshot each.
- Motion-FX 22:17Z: shot list updated: no fur clumps or puffs on dirty cats in any video; hide snippet before each dirty cat take, tight framing fallback, check every frame at the cut.
- Review-QA 22:39Z: counter card fix PR 854 (issue 853) armed; once on main rerun the 6 newcomers card step (needs the card at spawn of each newcomer).
- Review-QA 23:03Z: after next dev publish (PR 854 cards, PR 855 pass/product ids, fix for issue 872 if landed) rerun: plan steps 1 (fresh save opening), 4, 5, build start and Finish now, starter saving text. Also still owed from Motion-FX: Reduced Motion catWalkOut, six-customer volumes and fps; bench card (Design).
- Model-Agent 23:12Z: once PR 897 is on main: Rosette or Djinn in the tub with Royal and Golden bows: bow small, top right corner, not cutting the head piece. One screenshot each. (Jobs 5 to 7 sent to RC session 23:12Z: issue 872 and 854 recheck, issue 894 carry R6 and R15, owed reruns.)
- Model-Agent 23:30Z: PR 897 merged 897f2bc; recheck head piece bow (about 0.6 size, top right corner, not cutting the head piece or floating) on a build at or after 897f2bc. Gameplay: board E conflict at counter place 1 (new FAIL, reported).
