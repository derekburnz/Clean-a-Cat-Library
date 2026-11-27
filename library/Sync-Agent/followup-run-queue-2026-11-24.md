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
- Motion-FX 23:34Z: capture sheets (tubLife, photoFx, washPops with washMeter) on iphone frame, sent to RC as job 12 with the PR 897 bow recheck; pictures go through a draft docs PR, then I copy them to /mnt/project-files/Motion-FX-Agent/sheets-2026-11-26/.
- Gameplay 23:38Z issue 924 (RC job 13): wash screen front camera numbers: FieldOfView, ViewportSize, camera distance to cat pivot, cat GetBoundingBox size, tub or station, on-screen cat height px. Send to Gameplay-Engineer.
- 00:12Z (Review-QA): bow overlap is issue 948 (Model-Agent): recheck Rosette Royal and Djinn Golden (was 3 parts each on eb27dde) when Model says fixed. Pending RC job 16: video takes through draft PR, v2 sheets after PR 941.
- Review-QA 00:16Z (issue 884): once PR 952 (helperFetch) is on main, with helperFetch, counterLine, bigSpa on: Jo and Sam fetch cats from counter places 1, 3, 6 on the big spa: walk to counter, carry back, wash, carry out; flag any straight line through a stand, tub or wall.
- STOP 00:57Z (coordinator): Open Cloud 403 'User is moderated' at 7:55 PM ET. No uploads, no store page changes, no publish from Studio until Derek reports. Local Studio tests fine. Store page job (issue 901) is on hold.
- Gameplay 03:11Z (PR 979, Derek's wash screen note): RC job 18 sent: before on main without 979, after with 979 at scrub, rinse, camera turn: no heart bar, name tag, worker bar or pill; all back after wash. One before sheet and one after sheet for Derek via draft PR qa/wash-hide-2026-11-27. PC session was parked/asleep at send time.
- Derek 03:13Z (via coordinator): in Chrome on the PC, if a Roblox page is needed, use switch accounts and pick icecloak (his other account, admin in the group); main account suspended 7 days; group key regenerated from icecloak. Only jobs he asked for, no passwords or codes, stop at sign in prompts, NO image uploads until Review-QA passes the exact files under the new image gate (store thumbnail with staff holding a pole is on Model-Agent's high risk list). Store page job (issue 901) stays on hold.
- Review-QA 03:17Z image gate: PASS icon-main-512, icon-alternate-e-512, thumbnail-order-2 (name and bath), thumbnail-order-4 (stray box). FAIL for now: order-3 busy spa (bare arms, pole), order-1 half muddy (dark blobs); Model-Agent re-renders. DO NOT upload anything, not even the four, until Review-QA says the hold is lifted (Derek: flagged image removed first). Then upload only the four passed, in one batch, via Chrome on icecloak.
- Review-QA 03:36Z: all six store files pass the image gate (icon-main-512, icon-alternate-e-512, thumbnail-order-1 to 4, 1 and 3 re-rendered). Still NO upload tonight; store art waits for Derek's next word (then upload via Chrome on icecloak, one batch, stop at sign in).
- 03:50Z Derek's go ahead for the store art upload (via coordinator: 'go ahead for all'). RC job 19 prepared; waits for 'UPLOAD NOW' from me after Review-QA confirms code publishes on the new key worked. Library commit c0fcff6 holds re-rendered thumbnails 1 and 3 (sha256 cdb986caab235d62..., b5ea4cec140f066b...).
- 04:00Z RC session paused job 19: using icecloak while main account is suspended may count as evading the suspension; wants Derek's direct confirmation. My recommendation to coordinator: wait for appeal or 7 days (about Dec 3 7:54 PM ET), upload from main account. Files ready (library c0fcff6).
- 04:05Z RC session declined job 19 (store art via icecloak) as working around a Roblox enforcement action, even with Derek's OK. Files hash-checked and ready at Downloads\Clean-a-Cat-Library-qa\library\Model-Agent\store-art\picked-2026-11-26\: icon-main-512, icon-alternate-e-512, thumbnail-order-1 to 4. Derek can upload himself, or we do it from the main account once restored (about Dec 3 7:54 PM ET). I do not try other routes.
- 04:04Z Derek asleep (11:03 PM ET): overnight orders: run local Studio checks on every merge (floating cats and drop off flow, enclosed wash screen, helperFetch 884, gift stand, new pets 883, spaced spas and zoom, phone UI, 773, 40, 838); send failures with pictures to the threads at once; store page stays Derek's; if the PC goes offline note the time and what is left here and tell Review-QA (it writes the morning report). RC overnight loop job sent 04:05Z.
- Review-QA 04:04Z overnight checks sent to RC: 948 and 845 (bows, PR 977), 856 (enclosed wash, PRs 979 983 985), 887 (wideStreet, 84 studs), 885 (zoom out edge, PR 986). Report each to Review-QA.
- Motion-FX 04:05Z issue 871 capture (carriers float beside customers) sent to RC; result goes to /mnt/project-files/Motion-FX-Agent/carrier-float-871/ (copy from the draft PR).
- Gameplay 04:06Z issue 871 proof for Derek (drop-off flow, six cats on mats, step-up, heart out, take place 3): sent to RC; copy pictures to /mnt/project-files/Gameplay-Engineer/dropoff-2026-11-27/ and report to Gameplay-Engineer.
- Gameplay 04:07Z extras to the drop-off run: 887 wideStreet (84 studs, truck, walk paths, neighbour visit, fps, before/after pictures) and 856 wash room recheck (WashRoom 6180e703 plus PR 983, six counter cats waiting, nothing shows through, all back after).
- Gameplay 04:23Z: (1) after PRs 992 and 993 are on main: six newcomers walk-in recheck (no cat at counter height beside a walking customer; cat only out of its crate; all six on mats) for issue 871; (2) issue 994: re-run plot 3 to plot 5 walk with qaWalk, print waypoints and the part it stalled against near (-117.8, 8.8) (name, CanCollide, CanQuery). Sent to RC.
- Design 04:24Z issue 991 (PR 995): iphone_13 recap with 7+ coin rows: rows two to a line, Next cat and total fully on screen with 44 px tap height. Sent to RC; results to Design-Agent.
- Review-QA 04:27Z queue after 885, 838: 871 walk-in recheck, 991 recap, 773 dev look + wideStreet fps, 40 full loop under 10 min with times, 531 first session playtest with console list. Sent to RC. Report each to Review-QA with commit.
- Review-QA 04:34Z: (a) 948 Stardust bows 0 overlap (PR 1003), (b) 869 like how-to images load, (c) 883 Clover and Glitch portraits load; image load checks may be NOT CONCLUSIVE while the account is suspended (403 User is moderated). Sent to RC.
- Gameplay 04:41Z: PR 1008 reverts 992 seating; rerun walk-in after it is on main with per-place parts on the mat N of M after six newcomers and after one step-up, anything beside the line, and Workspace.StreamingEnabled (plus StreamingMinRadius, ModelStreamingBehavior). Sent to RC (high priority).
- 991 recap iphone_13 on 844315b (PR 995): PASS, 9 rows, Next cat 109x45 px, bottom y 304.5 of 330. E on 'Put in tub' did nothing 3x (not conclusive; RequestPlaceCat from client worked). 1008 still open; walk-in rerun waits for it.
- Gameplay 04:43Z: add one leave (heart bar empty) to the 871 rerun; report where PackedCat shows (carrier at mat or pavement spot -10,3.4,-35) with world position; parts on mat after leave. Sent to RC.
- 884 helpers fetch on 844315b: FAIL (walks all aim at pavement (-10,3.4,-35) because server CounterCat pivot; Jo line crosses ThirdTub station). Sent to Gameplay.
- 948 Stardust bows on 208dc9d (PR 1003,1008): PASS, 24 fits no overlap. 871 rerun on 208dc9d running.
- 871 on 208dc9d first numbers: all places N of N, 0 off mats. Leave/PackedCat check pending.
- Gameplay 04:49Z: 884 rerun on PR 1009 (branch claude/project-thread-r0i85j): stop 2 studs behind counter at own place, held cat stays on mat, top view of paths. After the 871 leave check. Sent to RC.
- 871 leave check on 208dc9d: FAIL, PackedCat in carrier 16.4 studs from figure at pavement (-11.4,0.9,-39.5), not at hand. Walk-in passes (N of N). Sent to Gameplay. Next: 884 on PR 1009.
- Gameplay 04:53Z: 1009 on main (rerun 884 on main); PR 1010 seats PackedCat at carrier CatSeat: rerun 871 leave check when on main (pass 1-2 studs from figure, N of N). Sent to RC.
- Gameplay 04:56Z: 1009 and 1010 on main; RC told to run 884 and 871 leave check on current main.
- 884 rerun on 49f4f89 (PR 1009): stops right, held cat stays; FAIL lane x-6 crosses ToolsBoard (x -7.85..-4.15, z -11); minor 0.3 stud counter clip. Sent to Gameplay.
- Gameplay 05:00Z: PR 1011 fixes 884 (lane, stop 2.6); after leave check run one Jo fetch top view on 1011. Sent to RC.
- 871 leave check on 7e033d1 (1009,1010): PASS, 1.47 studs, N of N. Relayed to Gameplay and Review-QA. Pending: 884 Jo fetch on 1011; picture PR from PC.
- Gameplay 05:02Z: wants counter-208dc9d-six-whole-cats.jpg, leave-7e033d1-kit-packed-cat-in-carrier.jpg and 1011 helper top view in /mnt/project-files/Gameplay-Engineer/dropoff-2026-11-27/. Asked RC to push the picture PR now; I copy from refs/pull/N/head.
- Copied PR 1012 (qa/night3-2026-11-27) pictures to Gameplay-Engineer/dropoff-2026-11-27/. 1011 Jo fetch view still to come.
- 05:03Z: 1011 on main; RC told to run Jo fetch top view, push to PR 1012 branch.
- 884 close-out on c2eeb78 (PR 1011): PASS. Picture copied to dropoff-2026-11-27. Next RC: 869, 883, 871 carrier close-ups.
- 869 like how-to on c2eeb78: images load/draw (preload 403 moderation not conclusive); colour question (pink always) sent to Design. Next RC: 883 portraits.
- 883 portraits on c2eeb78: PASS (sent to Model-Agent). Next RC: 871 carrier close-ups R15/R6.
- Design 05:14Z: after PR 1013 on main, sample 869 like how-to heart every 0.1 s for 2 s (grey ~0.75 s per loop, frame renamed Tap). Sent to RC.
- 871 carrier float on c2eeb78: PASS (grip distance 0.00 x22, parent ArmR). Files copied to Motion-FX-Agent/carrier-float-871 from PR 1014. R6/R15 not applicable (NPC rig).
- 869 on fb23dab (PR 1013): PASS loop+Tap name; Reduced Motion pending. Sent to Design.
- 869 Reduced Motion on fb23dab: PASS. Sent to Design. Next RC: 773.
- 773 on fb23dab: mostly PASS; Golden/Royal bows overhang head edge half-way, question to Design. fps 235 avg desktop. Next RC: 40, 531.
- Design 05:22Z: Golden/Royal bow overhang wanted; 773 passes. Owed: bow in display window and walk-out. Sent to RC.
- 40/531/773 done on fb23dab; report written studio-reports/overnight-2026-11-27-night3.md
- 0e6a8f5 (PR 1016, 1015): Take prompt gap after Next cat reproduced (>=5.6 s, CarryCat 'door'); starter ad big sparkle not reproduced. Sent to Gameplay.
- Gameplay 05:41Z: issue 1017 Take gap: sample every 0.5 s after Next cat (CounterReadyAt/SetAt/WalkAt vs now, Served, CarryPrompt part, PPS.Enabled, figure count, first Take return). Sent to RC.
- 1017 on 0e6a8f5: Take prompts absent ~6.1 s after Next cat while CarryCat nil until door customer holds next cat; ReadyAt not the cause. Sent to Gameplay.
- 1017 recheck on 66ae8fc (PR 1018): PASS, gap 0.5 s.
- 11:31Z Derek: appeal granted, suspension lifted. Coordinator: retry store art upload (icon A main, E alt, thumbs 2,1,3,5 redrawn 1 and 3) on dev and game pages; close 106, 851, 901; dev look check images load. Sent to RC.
- 11:4xZ image check on 66ae8fc: all six PreloadAsync Success (heart outline/filled, tap dot, ring, Clover, Glitch). Store art: RC waits for Derek's own words for dev page; asked coordinator.
- 11:34Z Derek 'yes to all' (dev + live store art, icon E alt, A main, four thumbs). Passed to RC.
- 11:4xZ RC could not upload store art: Chrome navigation to create.roblox.com refused by PC permission guard. Needs Derek to allow Claude in Chrome there or upload himself. Told coordinator.
- 11:35Z Derek 'use my pc for anything needed' passed to RC; retry store art upload.
- 11:4xZ store art refused again by PC auto mode classifier [Undermining Oversight]; Derek must leave auto mode at PC or upload himself. Told coordinator.
- 11:4xZ third try: dev Icon page opened (signed in 257335), file upload refused by auto mode classifier [Destructive or Unwanted Actions]. Derek must switch out of auto mode at PC or upload himself. Alt icon E slot location unknown.
- 11:5xZ 4th try after Derek's written approval: PC auto mode classifier [Undermining Oversight] again. Alt icon E: Icon page has one slot; only Experiments (A/B) page offers second icon. Derek must switch PC session out of auto mode or upload himself.
- 11:58Z dev icon A uploaded (InReview TN3); dev thumbnails need Derek (Windows file picker); live untouched; dev media API shows 0 thumbnails.
- e0ffc75 (PR 1020, 1019 pass name): PASS. Sent to Review-QA. Next RC: PR 1023 counterSlim.
- 44b11d1 (PR 1023 counterSlim): PASS by properties, 1.00 stud gaps. Sent to Review-QA.
- 1f2895a (PR 1025, 1021 noVisitBoard): PASS incl. rollback. Sent to Review-QA.
- 1022 counterSlim on iphone_13 1f2895a: FAIL size (spawn 17-22 px wide 3-4 px tall; door line overlaps 16-21 px). 1021 door picture done. Next RC: PR 1026.
- b92db46 (PR 1026, 1024 rewardPop): PASS; notes: dim misses top 58 px inset, hint card and starter ad draw over dim. Sent to Design.
- Design 12:21Z: issue 1040 check on DEV GAME (fresh server): SpaPlotBig 48x32, tub 1.3x, wash stands 1.35x, counter window; wide shot. Sent to RC.
- 1040 bigger spa: all four pieces present on b92db46 (= dev sha, bigSpa true in dev); local place, not dev server. Sent to Design.
- 6f4569d: 1039 reward layer PASS (Design); 1043 menuOnly prompts PASS but GAP no Helpers entry before first hire (Gameplay).
- 3bd8932 (PR 1044, 1037 resetSave): server PASS; rejoin/save/rank/receipts need dev game; no UI button yet. Sent to Gameplay.
- Gameplay 12:31Z: PR 1046 fixes Helpers gap; recheck when on main. 1037 dev checks wait for Settings row and resetSave on in dev (Gameplay pings).
- 79d7c5b (PR 1046): button shows at 300 PASS; FAIL no Hire button in HelpersWindow (row.hire unread). Sent to Gameplay.
- Gameplay 12:38Z: Hire button is Design's PR; recheck hire once it merges (menuOnly off in dev until then). PR 1047 coin ladder/launch sale needs a dev pass later.
- 9a1a3f8 (PR 1047): smoke PASS; full ladder/sale pass waits for Gameplay setup (needs dev prices).
- 5873817: 1035 petSingles PASS; 1052 assets only. Sent to Review-QA.
- eafb264 (PR 1053, 1041 expansionDoor): logic PASS, FAIL missing BackDoorLocked/Open models (walk-through). Sent to Gameplay and Model-Agent. Next RC: PR 1054.
- Gameplay 12:54Z: expansionDoor off until Model-Agent's door models land; then rerun Garden + old-save checks. Queued to RC.
- Model-Agent 12:55Z: door models in PR 1057; when merged check both plots (blocks doorway, clear of stray box and Sam stand; open clear, door flat yard side). Queued to RC.
- URGENT 69b9548 (PR 1054, 1034): all pictures swapped for emoji stand-ins (PreloadAsync string form always fails). No switch, on dev. Sent to Design and Review-QA; revert or preload label.
- Design 12:58Z: PR 1060 fixes 1054; recheck icons/coins/portrait when on main. Queued high priority to RC.
- Review-QA 12:59Z: revert PR 1059 armed (check pictures back after); check PR 1060 from PR head before arming (real icons + bad id stand-in). Queued to RC.
- 12:59Z: hold 1060 check until Design rebuilds it on the revert; 1059 check proceeds.
- cbdcdb6: hire from Helpers PASS (1056); locked back door PASS (1057, 3.43 to Sam stand); unlock not fired (window open? Studio crashed), rerunning. Sent to Gameplay and Model.
- Design 13:03Z: PR 1060 rebuilt on a7da269; test head now (icons stay pictures, bad id stand-in). Sent high priority to RC.
- Gameplay 13:04Z: menuOnly ON in dev+studio. Unlock retest: close windows; if fails print distance to SpotGardenDoor. Sent to RC.
- a7da269 (revert 1059): PASS pictures back (105 vs 0). Testing PR 1060 head 880d0cb2.
- PR 1060 head 880d0cb2: PASS (real icons 105, bad id stand-in only on that icon). Sent to Review-QA and Design.
- a7da269: 1041 unlock PASS (windows closed), 1057 open look PASS, 1056 reset confirm PASS. Garden behind door + old save untested; second plot not checkable solo.
- PR 1060 merged as 41da07f, tree identical to tested head; PASS stands.
- Model 13:08Z: issue 1062 right arm out at counter: read CarryArmOut, CarrierHidden, Carrier transparency per figure; pictures behind+side. Later 1063 tape no pink + VipDoorFill. Sent to RC.
- 13:09Z Derek: only use C:\Users\Derek\Downloads\games\Clean-a-Cat on PC from now on. RC told; no deletes or moves; asked for folder state.
- 1062 on 41da07f: arm out by CarryArmOut even with CarrierHidden; CustomerMotion.armIn not applied. Sent to Model, Motion-FX, Gameplay.
- 13:1xZ folder check: games\Clean-a-Cat is the game clone with library clone and captures inside; store art path updated; ~46 temp worktrees left for Derek's cleanup call.
- Motion-FX 13:12Z: PR 1064 fixes 1062; run its 4-point test plan when merged. Queued to RC.
- Review-QA 13:12Z: PR 1064 armed; add check walking carriers past 60 studs keep arm out. Queued to RC.
- Derek plan page: icon E 'A now, test E after launch'. Memory updated.
- 13:16Z Derek 'delete them': RC removing temp scratchpad qa worktrees and .rbxl test places (check unpushed first); nothing else.
- 13:2xZ cleanup blocked by PC auto mode [Destructive or Unwanted Actions]; dry run: 41 worktrees clean, ~10 GB. Derek told options.
- Review-QA 13:19Z: closed old QA picture PRs 936,947,954,956,981,990,1001,1002,1007,1014 (branches kept). Keep using 1012.
- f701af9 (PR 1064, 1062): FAIL arms still at CarryArmOut with CarrierHidden; walking far PASS. Sent to Motion-FX and Review-QA. Next RC: 1061, 1067.
- 13:2xZ cleanup DONE: 41 worktrees removed + prune, 282 test places deleted, 10.2 GB freed. Told Derek.
- Motion-FX 13:21Z: confirm 1064 sample side; redo from client (ArmR, CarrierHidden, CarryArmOut, LegL swing) plus server side-by-side. Sent RC high priority.
- Gameplay 13:23Z: 1063 noVipRoom on 61dff0a: one door, VipDoorFill, VIP gone from board/build, tape no pink, refund notice once. Queued to RC.
- 1062 probes f701af9 client: flag true, 0 logs, manual arm change persists, no leg swing => CustomerMotion not running/attaching. Sent to Motion-FX. Next RC: 1063 on 61dff0a.
- 1062 frame probe 61dff0a: PreRender 120/2s, Heartbeat 480; bodies move, legs and arm not posed. Sent to Motion-FX.
- 61dff0a 1063 noVipRoom: PASS (fill, VIP gone, no pink, +15000); notice text not seen, once-only needs dev. Sent to Gameplay. Next RC: 1074, 1075.
- Design 13:28Z: windowClear (1075/1038) badge in title band, HUD hides; 1065 round slider ends; iphone_13 + tablet. Queued to RC.
- Motion-FX 13:29Z: PR 1078 debug branch claude/project-thread-vamibm: read CustomerMotionState x2 and MotionRig per customer on client. Sent RC high priority.
- 1078 debug f190d71: CustomerMotionState on rigs=16 steps ~60/s; MotionRig 'no joints' on all counter customers; lead: attach() joints loop. Sent to Motion-FX.
- Motion-FX 13:32Z: 1062 cause = isCustomer matched joint models; fix on claude/project-thread-vamibm after 1078 merges; verify MotionRig rig..., ArmR 0, legs swing. Queued to RC.
- e0ebe2f: windowClear 1038 PASS iphone_13+iPad; 1065 round fills PASS. Sent to Design.
- Gameplay 13:33Z: issue 1080 read ProductPrice_StarterPack, PassPrice_GoldenSponge, PurchaseService warnings (local only; dev needs Derek). Sent to RC.
- 1080 local e0ebe2f: GameId 0, no price attrs, no PurchaseService logs (expected); dev game read needed. Sent to Gameplay.
- Motion-FX 13:34Z: PR 1082 (3f41199) fixes 1062; verify MotionRig, ArmR 0, walk arm out, LegL swing, leave. Sent RC high priority.
- PR 1082 3f41199: 1062 PASS (rigs attach, ArmR 0, walk arm out, legs swing); leave/far/budget pending. Sent Motion-FX + Review-QA.
- e058a276 (1082): 1062 checks 1-4 PASS; PackedCat leave FAIL (clone keeps turned-in arm). Sent Motion-FX + Review-QA.
- Review-QA 13:43Z: 1062 closed; leave arm is issue 1086 (Motion-FX). Recheck when fix lands.
- Design 13:44Z: starter card 1069/1080 check (plum, no bob, price, no clock, prompt, i window). Queued to RC (local; dev not reachable).
- Motion-FX 13:47Z: PR 1089 (f1f5fd1) fixes 1086 leave arm; check walk-off ArmR = CarryArmOut, legs swing, counter unchanged. Queued to RC.
- 29e9249 starter card 1069/1080: PASS; note HERO 'Sponge' draws emoji not ShopGoldenSponge art. Sent to Design. Next: PR 1089.
- PR 1089 f1f5fd1: 1086 PASS (4 leaves at CarryArmOut). Sent Motion-FX + Review-QA.
- Design 13:54Z: menuContrast2 (1029, PR 1088, ffa59f4) phone check of 10 windows. Queued to RC.
- 52dfced menuContrast2 1029: body text PASS 10 windows; flags: white button labels low contrast (1.55-2.7), Takes chip gradient, Build check 2.68, Settings no cards, Shop empty. Sent to Design.
- Growth 14:14Z: issue 1066 store-page-uploads copied to library main debdd00; RC copying to C:\Users\Derek\Downloads\games\Clean-a-Cat\store-page-uploads. Re-copy GATE-STATUS when Growth updates.
- 1066 folder on PC done (18 files). Told Growth.
- Review-QA 14:43Z: Cat Hotel 1049/1050/1051 on 1f4f9c1 (garden looks at VIP site, hotel at back door builds/collects, pets in garden, console). Queued to RC.
- Review-QA 14:52Z: issue 1027 shortText check 8 windows. Queued to RC.
- 1f4f9c1 Cat Hotel 1049/1050/1051: PASS both plots. Sent to Review-QA. Next: 1027 shortText.
- 2026-11-27 ~10:00 AM ET: 1027 shortText PASS (main 009c407, iphone_13, all 8 windows; Uncommon pill 89/88 and Check in title 84/79 slightly wide; starter shows save 71% vs memory 66%). Pictures PR 1012 branch e0c39493. Sent to Review-QA.
- 2026-11-27 10:15 AM ET: Review-QA asked (a) exact spots of the Uncommon pill 89/88 and Check in 84/79 for Design-Agent, (b) PR 1114 menuContrast3 check once merged. Both queued on the PC (local place, switch on).
- 2026-11-27 10:25 AM ET: Sent Design-Agent the exact spots: Uncommon pill = Crate odds list Pet3/Pet4 (Ooze, Glitch) 89x19 in 88x18; Check in = Checkin Band.Title 84x24 in 79x23. 1114 check waits for merge.
- 2026-11-27 ~10:50 AM ET: 1114 menuContrast3 PASS (main 59e74dc local, iphone_13): outline 12.4, vs button 5.15/3.34/3.01; taps OK; ticks 4.80; gold 6.64/4.76; Gift buttons read from properties only. Pictures 1012 branch 855fa224. Sent to Review-QA.
- 2026-11-27 10:25 AM ET: Queued on PC: 1114 retap and reopen check plus Gift retry; then 1116 (issue 1110) Helpers picture 97491083681037 and the two fits, after merge.
- 2026-11-27 ~11:00 AM ET: 1114 retap PASS (Helpers level up, Build buy, Gift all 4 buttons, reopen; 0 double text or lost outline). Pictures 1012 branch e833ae82. Sent to Review-QA. 1116 waits for merge.
- 2026-11-27 ~11:20 AM ET: 1116 (1110) PASS on main 1a5ebf1: Helpers icon 97491083681037 loads on button and badge; Uncommon 89 in 89.25 (height 19 in 18 still, draws fine); Check in title fits. Pictures 1012 branch 6dec8638. Sent to Review-QA.
- 2026-11-27 10:42 AM ET: Queued 1118 ButtonInk toggle check (TextTransparency 1/0, SignalBehavior) on PC after merge.
- 2026-11-27 10:45 AM ET: Queued 1111 groupVerify gift stand check (local, never really join a group; membership simulated in the place only).
- 2026-11-27 ~11:10 AM ET: 1111 groupVerify mostly PASS (main 8729c8a, inGroup stubbed locally, no group joined); FAIL 6b: Starcoat-owned save gets no board so cannot claim 150 coins in UI (server OK). Sent to Review-QA and Gameplay. SignalBehavior Default (probe looked Immediate, unconfirmed). Pictures 1012 branch 845e74b3.
- 2026-11-27 ~11:30 AM ET: 1118 ButtonInk on main f27874d: toggles PASS (no flicker or double text); FAIL set TextTransparency 1 does not hide outlined words (no-op write, own value already 1). SignalBehavior Default, behaved Immediate. Pictures 1012 branch 57987d61. Sent to Review-QA.
- 2026-11-27 10:55 AM ET: Queued 1120 (1111 fix + TestInGroup hook) recheck of 6b on PC after merge.
- 2026-11-27 11:04 AM ET: 1120 recheck now waits for PR 1123 too (board words 'For 150 coins' / 'Yours already. Join for 150 coins'); playtime step check added.
- 2026-11-27 ~11:20 AM ET: 1120 PASS on main 6360b8c (pre-1123; TestInGroup hook; 6b board shows, +150 only, playtime row stays; copy still 'For 150 coins and the Starcoat'). Pictures 1012 branch 9d0a4f4d. Rerun after 1123 pending.
- 2026-11-27 11:05 AM ET: Queued 1119 starterFloat (PR 1121) check on iPhone 13, iPad and small phone; no purchase completed, prompt cancelled.
- 2026-11-27 11:11 AM ET: Queue on PC: 6b board words (1123 merged), then 1119 starterFloat, then 1124 ButtonInk 0.999 rerun of 1118 after merge.
- 2026-11-27 ~11:35 AM ET: 1119 starterFloat mostly PASS (main 139a6a2, 3 devices); ISSUE A SAVE tag covers STARTER PACK words; ISSUE B lower half of price tap fails (press scale top-left anchor); iphone_7 card touches jump (0 gap). True saving 697 vs 199 = 71.4%. Pictures 1012 branch 77048822. Sent to Review-QA.
- 2026-11-27 ~11:45 AM ET: 1123 6b board words PASS on main f27b5c4 ('For 150 coins', 'Yours already. Join for 150 coins'; +150 only). Pictures 1012 branch 244a27a1. Sent to Review-QA; 1111 can close.
- 2026-11-27 11:18 AM ET: Queued 1125 recheck (SAVE tag under words, full-ad taps, Midas dip, iphone_7 gap) on PC after merge; 1124 rerun still queued.
- 2026-11-27 ~12:00 PM ET: 1124 FAIL on main 463866d: first Set 1 swallowed (float32 0.999 != 0.999, pending counter leaks). Fix: tolerance or 1023/1024. No double text. Pictures 1012 branch 8eb461ff. Sent to Review-QA.
- 2026-11-27 11:24 AM ET: Queue: 1125 starterFloat recheck now (merged), then 1129 ButtonInk float32 fix hide check after merge.
- 2026-11-27 ~12:15 PM ET: 1125 PASS on main 16cc5c1 (tag under words, all taps fire, Midas dips, iphone_7 gap 5.2 px); note Suds tip X over price on iphone_7. Pictures 1012 branch ca34419b. Sent to Review-QA.
- 2026-11-27 ~12:30 PM ET: 1129 ButtonInk tolerance PASS on main 3e4c12b (first Set 1 hides on fresh and redrawn buttons; 0 double text). Pictures 1012 branch 938c1c27. Sent to Review-QA. Queue empty.
- 2026-11-27 11:33 AM ET: Queued 1122 dev buy prompt pictures (dev place in Studio play test, cancel each, never buy or save).
- 2026-11-27 11:40 AM ET: 1122 held: PC needs Derek's own OK to open dev in Studio; decision card posted to Derek. Review-QA told.
- 2026-11-27 11:42 AM ET: Queued 1130 (ad hides under Suds tip on iphone_7) local check after merge. 1122 still waits for Derek's card (coordinator withdrew its call).
- 2026-11-27 ~12:50 PM ET: 1130 on main 31ebf1a: PASS iphone_7 and iPad; FAIL brief on iphone_13 (ad also hides; 'short' flag, use 'tiny'). Pictures 1012 branch 7725615c. Sent to Review-QA.
- 2026-11-27 11:50 AM ET: Queued 1131 local picture check (Build 11+2+3 bows, Shop 2x/3x, Starter = Shop ids).
- 2026-11-27 ~1:00 PM ET: 1131 PASS on main 734d1d7 (18 ids unique, all preload Success; 2x/3x apart; starter ids = Shop). Pictures 1012 branch 878748a1. Sent to Review-QA. 1122 dev still on Derek's card.
- 2026-11-27 12:41 PM ET: Derek's own words in project chat ('2. you test I will test later') approve the 1122 dev Studio prompt check. Sent to PC; card closed with option 1.
- 2026-11-27 1:07 PM ET: Queued 1134 star coin load check (108922632736355, retry if blank). 1122 waits for Derek's words in thread.
- 2026-11-27 ~1:20 PM ET: 1134 star coin PASS on main f6e2370 (Success, IsLoaded, star coin shows). Pictures 1012 branch 9ef654db. Sent to Review-QA.
- 2026-11-27 1:35 PM ET: Queued 1136 helper wash tools check for Motion-FX (branch vamibm 71c68bc).
- 2026-11-27 ~2:00 PM ET: 1136 helper tools at 71c68bc: works; shampoo and shower holds look off, brush patch moves small; water ends in fur; cleanup clean; no perf cost. Pictures 1012 branch ff5dee71. Sent to Motion-FX.
- 2026-11-27 1:45 PM ET: Queued 1136 recheck at 559f490 (shampoo tip, shower way round, water end, brush spread).
- 2026-11-27 ~2:15 PM ET: 1136 recheck 559f490: shower, water, brush sideways PASS; shampoo still level (aim at box centre; aim at top); brush along-cat still 0.14. Pictures 1012 branch aeb22247. Sent to Motion-FX.
- 2026-11-27 1:52 PM ET: Queued 1136 last recheck at 694e2fc (shampoo tilt, brush along spread).
- 2026-11-27 ~2:30 PM ET: 1136 at 694e2fc: shampoo tipped ~20-30 deg (hits tail, not back); brush along 0.21 studs. Pictures 1012 branch d01a6077. Sent to Motion-FX.
- 2026-11-27 1:59 PM ET: Queued 1136 final (9aac077) local check from main after merge: shampoo on back, all four steps.
- 2026-11-27 ~2:30 PM ET: 1136 final on main f34d690: 4 steps PASS; shampoo still hits tail (hand below back; raise hand or aim high with less tip). Pictures 1012 branch 411ff0da. pr1136 worktree removed by PC. Sent to Motion-FX.
- 2026-11-27 ~2:25 PM ET: Derek's 2:14 PM no-price starter ad = my local place qf34d690 (no prices set, Pass_Lou only); dark bar = Hero.Shadow bgT 0.72. Pictures 1012 branch d9519b7d. Sent to Design; told Derek.
- 2026-11-27 2:40 PM ET: Handoff sync for Derek's account move: library 63bbe0a (pass 1, 1771 files) and 22e6b74 (pass 2). Out on purpose: Coordinator/references, Growth monetization research, new Growth store-page-uploads.
