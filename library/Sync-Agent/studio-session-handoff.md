# Studio session handoff (from the Remote Control session on Derek's PC, 2026-11-26 20:20 UTC)

No run in flight. Last run: issue 782 recheck on main 86b06fc, in draft PR 788. One Studio window open in Edit: scratchpad\CleanACat_q789.rbxl (PID 24616), unsaved, safe to close.

## PC layout
- Clone: C:\Users\Derek\Downloads\games\Clean-a-Cat (moved there from Downloads\Clean-a-Cat on 2026-11-26). Detached HEAD: `git fetch origin` then `git checkout --detach origin/main`. Untracked Clean-a-Cat-captures/ inside: never commit it. Older captures (24 to 26 Nov) in games\Clean-a-Cat\Clean-a-Cat-captures\ with a subfolder per job.
- Scratchpad: C:\Users\Derek\AppData\Local\Temp\claude\e6d7182404a49cfc\899b4302-f50a-4b83-bee3-805d4bb224f7\scratchpad (tied to the session; a new session gets its own). Scratch places scratchpad\CleanACat_q<sha>.rbxl; picture-PR worktrees scratchpad\wt\<name>; picture staging scratchpad\pics-*; walk helper scratchpad\stuck\qaWalk.luau and studio-movement-rules.md (both stored in the library under Sync-Agent/studio-tools/).
- Tools: Rojo 7.7.1 in %USERPROFILE%\.rokit\bin (run from games\clean-a-cat, needs the repo's rokit.toml). Studio: %LOCALAPPDATA%\Roblox\Versions\version-8d7a1009c17e4ff8\RobloxStudioBeta.exe. gh CLI signed in as derekburnz (push and `gh pr create` work without prompts). Python 3.14 (use PYTHONIOENCODING=utf-8).
- PC auto-memory: C:\Users\Derek\.claude\projects\C--Users-Derek-Downloads\memory\ (clean-a-cat-studio-testing.md, clean-a-cat-github-rules.md).

## Build and open a test place
1. `cd C:/Users/Derek/Downloads/games/Clean-a-Cat && git fetch -q origin && git checkout -q --detach origin/main && git log --oneline -1` (report the sha). Then `cd games/clean-a-cat && rojo build default.project.json -o "<scratchpad>/CleanACat_q<sha>.rbxl"`.
2. From PowerShell: `Start-Process -FilePath "$env:LOCALAPPDATA\Roblox\Versions\version-8d7a1009c17e4ff8\RobloxStudioBeta.exe" -ArgumentList '"<full path>.rbxl"'`; wait about 50 s; list_roblox_studios for the new studio id.
3. Close the previous scratch window by PID, only after the title matches `*\scratchpad\CleanACat_q*.rbxl - Roblox Studio` (an unfiltered kill was refused by the permission classifier; closing normally leaves an unclickable "Save changes?" dialog, so stop the process).
4. Inject test patches in Edit with execute_luau, before Play (local copy only, never save):
   - `LiveFlags.resolve` override, inserted right after `function LiveFlags.resolve(key: string, stored: unknown): boolean\n`: `if key == "toolCursor" or key == "streetLoadTest" or key == "exampleFeature" or key == "openingReplay" or key == "benchGrow" or key == "cameraClear" then return false end`, `if workspace:GetAttribute("_QAOff_" .. key) then return false end`, `if LiveFlags.OFF_BY_DEFAULT[key] then return stored ~= false end`. bigSpa is read only at server start: set `_QAOff_bigSpa` before Play to turn it off.
   - SaveSchema seeds (gsub the default lines to read workspace attributes, an assert per gsub): playSeconds from _QAPlay (700), coins _QACoins, stars _QAStars, workers from _QAJar (Jo and Sam, level 1, hiredAt os.time()-20000), crates = { normal = _QACrates }, stations = { Garden = true, VipRoom = true } if _QABuilt, bows { Silk, Satin, Golden } if _QABows, builds.room from _QABuildItem and _QABuildEnd.
   - HeartRules.lasts optionally scaled by _QAHeart (did not speed up the drain on c94174e; check before trusting).
   - SpaSignController: `local name = (workspace:GetAttribute("_QATestName") :: any) or owner.DisplayName` with _QATestName = "Tester Mia" (otherwise the sign shows the account's display name, and the PlayerGui path shows the user id), so names stay out of pictures.
5. In Edit: `StudioDeviceSimulatorService:SetDeviceAsync("iphone_13")`, then start_stop_play is_start=true and wait 30 to 45 s with a Bash until-loop before the first call.
- Change switches live from the Server datamodel: `ReplicatedStorage:SetAttribute("LiveFlag_<key>", true/false)` (a local place has no DataStore).
- Update to a newer commit without rebuild: HttpService:GetAsync of raw.githubusercontent.com/derekburnz/Clean-a-Cat/<sha>/... works for source files; model .json can be rebuilt in Lua; InsertService:LoadLocalAsset is blocked. A fresh rojo build is simpler and safer.
- Dev switch state: `gh run list --repo derekburnz/Clean-a-Cat --workflow flags --limit 5`, `gh run view <id> --log`. All tests used local switches, never the dev place.

## Frames, rigs and input
- Phone iphone_13 844x390 (view 749x388); no iPhone 12 preset (same screen). iPad ipad_10th_generation view 1179x819, switch from the Client in play with SetDeviceAsync.
- Mouse on the phone: mouse = GUI position + (47, 0), GUI y = viewport y - 58. Screenshot image 604 wide: viewport x = image x / 0.716. GUI button: AbsolutePosition + AbsoluteSize/2, plus 47 in x. 3D target: WorldToViewportPoint then x+47, y-58.
- Rigs: default R15. R6 mid-play from the Server: `Players:CreateHumanoidModelFromDescription(Instance.new("HumanoidDescription"), Enum.HumanoidRigType.R6)`, named as the player, pivot it, `player.Character = model`, parent to workspace, destroy the old one.
- E fires the nearest ProximityPrompt (Take cat, Put in tub, box Open!, Wash him, counter Take). Clicks on BillboardGui pills do not register. A Check in modal or the Starter Pack offer can block E; close it with the GUI button tap first.
- Wash steps: `workspace:SetAttribute("CleanACat_TestStep", n+1)` finishes the current drag step. Bow and photo need real taps on PH_SpaPrototype.PH_Buttons.Bow* (Look child) and the Camera part, and the recap NextCat button.
- Force a cat into the tub (client only, looks only): from the Server `Remotes.CatReady:FireClient(p, <new id>, kind, CatRules.needs(kind), {}, false, 3, 1)`.
- Bow tier look: set player attribute BowTier (Ribbon, Silk, Satin, Golden) from the Server, or `BowFit.wear(cat, "BowPinkRoyal", cat:GetScale())` from the client (require PlayerScripts.Client.Spa.BowFit).
- Scripted moving jumps: `require(PlayerScripts.PlayerModule):GetControls():Disable()`, Humanoid:MoveTo(target) with Humanoid.Jump = true 0.1 to 0.25 s in.

## Walking: qaWalk (always)
Rules and spot table: studio-tools/studio-test-movement-SKILL.md. Paste the whole qaWalk.luau as one Client execute_luau after the opening and SpaPlotPlaced true; paste again after every Stop and Play. `_G.qaWalkNamed("Tub")` (Spawn, Tub, DoorLine, Window, Board, GardenGate, GardenInside, VipDoor, VipInside, StrayBox, PadJo, PadSam, PadLou) or `_G.qaWalk(Vector3)`. Report reached, method, seconds. The latest file drops a root-height goal to the floor first. With bigSpa on, door spots move to z 3.5 and inside to z 10.5 (SpaLayout handles it). Never character_navigation, held WASD, Humanoid:Move or a straight MoveTo; after any PivotTo zero the velocity and wait for FloorMaterial.

## Loggers and measuring (injected LocalScripts in StarterPlayerScripts, made in Edit)
- _QACam: per-frame camera log 6 s after each spawn, analysed when player attribute _QAAnalyze changes; result in the _QAResult StringValue.
- _QAPerf: per-second frame stats (frames, mean and worst ms, over 16.7 and 33 ms, memory) into player StringValue _QAPerf. Stats.FrameRateManager (Batches, Indices/3 = triangles, AverageQualityLevel) is readable only from execute_luau.
- _QACrate and _QACrate2: counter-crate timeline by server time into player StringValue _QACrateLog (figure appears and gone, CounterPlace changes, CounterSetAt and ReadyAt, place plus CounterCrateSpot at the set, visible part counts of counter cat and carrier, the Take prompt, crate copies in workspace.CleanACat_Fx_CounterCrate with position at +0.55 s).
- _QAFxWatch plus Audio/Effects patches (qalog into _QAFx): each sound play with IsLoaded and volume, each effects burst count.
- Pasted ray checks: qaFlat (80x40 ray grid, share of one flat face within 6 studs), qaCards (card size and HUD overlap), qaClipDetail (bow against head-piece parts, shrinking the bow until it stops touching, "clear at N%").
- _G is shared across execute_luau calls in one Play session, not with LocalScripts. A require from execute_luau is a separate module copy.

## Pictures and draft PRs
- Capture with screen_capture, from the default play camera or a scripted one. Close-ups: bind a RenderStep after the camera (priority Last+5) setting CFrame and FieldOfView each frame, and hide the PlayerGui ScreenGuis. screen_capture camera_position can leave the camera stuck Scriptable and is often ignored in the wash view. Captures land in C:\Users\Derek\.claude\projects\C--Users-Derek-Downloads\<session id>\tool-results\mcp-Roblox_Studio-blob-*.jpg; copy them with readable names.
- Draft PR recipe: `git worktree add -b qa/<topic> <scratchpad>/wt/qa-bNN origin/main`; pictures and README.md in docs/playtests/captures/bNN-<topic>-<sha>/ (Motion-FX pass used docs/vfx/clean-a-cat/); commit with the Co-Authored-By line; push; `gh pr create --draft`; body starts with the two attribution lines. Check every picture for names (only the tester name). No assignee, no review request, never merge, docs only. README style: setup block (build sha, place, switches, seeds, frame, input method), PASS/FAIL tables with numbers, then the console.

## Known quirks
240 fps cap, quality level 21; no lowest graphics level from script; no phone speed or memory (Stats memory is Studio's whole process). No iPhone 12 preset; portrait presets exist but the game locks landscape. Text filter passes everything. One player per local place: no second client, rejoin, join/leave, favourite or purchase prompts (never tap Favourite or buy). No real touch; mouse arrives as touch; drags must be slow (about 10 px per 50 to 100 ms). Screen control denied for Studio and its prompts time out. Smart App Control blocks unsigned exe files; RbxSync vetted and skipped. A Bash sleep over a few seconds is blocked: use until-loops. Each scratch window is 1.5 to 3 GB: keep one open. Never run a multi-second execute_luau during the opening (the MCP resets CameraType and leaves the camera Scriptable). Keyboard tool timing drifts: use scripted actions for timed sequences. AutoJumpEnabled is true on touch (anything under 7.2 studs hops).

## Cleanup rules
Never save or publish a place; nothing touches dev or live; no passwords or codes; no live servers. Close scratch windows by PID only after the title check. Remove worktrees with `git worktree remove` from the clone; delete local branches only once their PR is closed or merged.

## What exists now and what is safe to delete
- Studio: one window CleanACat_q789.rbxl (PID 24616), Edit, unsaved: safe to close.
- 108 CleanACat_*.rbxl (about 70 MB) plus .lock files in the scratchpad: disposable. Picture staging (pics-b8..pics-b14, pics-728, frames, m728, *_sheet.jpg) already in the PRs; prbody-*.md, setup_*.luau, prev__QA*.luau, *.ps1, *.json scratch. `stuck\` held the helper (now in the library).
- 38 worktrees in scratchpad\wt\. Safe to remove with local branches (all closed or merged): at, bh, c1, ff08, long, pc, pills, s6, sc, sf, sign, t5, wf, ws, qa-b2..qa-b5, qa-b7, qa-ff433b1, qa-shop, qa-b8..qa-b14, qa-b15 (PR 720), qa-b16 (PR 729), qa-b17 (PR 735). Detached, safe: b2, b9. Keep while their draft PRs are open: qa-b18 (PR 778), qa-b19 (PR 783), qa-b20 (PR 788).
- Open draft PRs of the RC session: 778 (issue 773), 783 (PR 762 crate plus landing recheck), 788 (issue 782 bows plus the 86b06fc recheck). Docs only, unassigned, not to be merged by it. Remote branches of closed picture PRs still exist on GitHub; delete only if the owner wants.

## Open checks owed
1. Window bow tier fix (Gameplay; WindowController wears the tier in use, falls back to plain): a stray washed with Golden, Royal and Double shows the same tier on the window seat; fake a missing tier model for the fallback. Not on main as of 86b06fc.
2. Customer cat walk-out (Motion-FX, CatReturned listener): the washed cat leaves with its bow, not just removed. Not on main yet.
3. Counter crate step-up: PR 785 open. When merged, rerun with _QACrate2: a full line with a step-up and a short line arriving at place 1. PASS: the crate lands at the customer's place at the set.
4. Counter cards: PR 774 open. Newcomers get a card (CounterPlace race); card size on the phone (about 43x13 px before).
5. Helpers window PR 693 recheck: a Jo hire sets no WorkerLevel; Rename sits behind Helpers; the Takes text is cut. Run once fixes are on main.
6. #679 spa sign countdown: signs drawn at the join never count down, and "2m left" sticks through the last minute. Recheck once fixed.
7. PR 691 button overlap recheck.
8. Issue 773 open lines: a real iPhone 12 at the lowest setting for the big spa (needs a phone); the 0.24 stud gate clearance with cats on the counter mats (not measured); Rosette's crown props flush with a head face (possible flicker, not seen).
9. PR 762 step 2 (rejoin) cannot run on a local place; needs the dev game with two sessions.
