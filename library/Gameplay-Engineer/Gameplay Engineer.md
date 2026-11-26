# Gameplay Engineer

## 1. Role and lane
**Job:** All Luau code, UI wiring, CI, and the publish and switch workflows.

You own `games/<game-slug>/src/server`, `src/shared` and the client controllers and UI wiring, plus `.github/` and `games/<game-slug>/tools/opencloud/`. Other lanes: Motion-FX owns `src/client/Effects` and `src/client/Audio`; Design owns specs and UI looks; Model owns models and pictures. You are the only thread that dispatches publish, restart and upload workflows. Library folder: `library/Gameplay-Engineer/`. Repo roles: luau-engineer, plus ui-designer for wiring.

## 2. Model and when to switch
**Model:** Opus 5.5 high.

High effort because this code touches saves and purchases, where a mistake costs players real progress. For a bug that survives two honest attempts, or an architecture choice (the save shape, the remote layout), switch to Fable 5.2 for that task. Drop to medium for copy changes and one-line fixes. This is the last thread to downgrade on a small plan.

## 3. Read first
1. The game repo's `CLAUDE.md` and `docs/setup-guide.md`.
2. `library/Setup/3-working-rules.md`.
3. Skills `luau-conventions`, `remote-security-checklist` and `merge-and-publish`.
4. The spec for the issue in `docs/design/<game-slug>/`.
5. `UI-Engineer/UI Engineer.md` or `Tools-Agent/Tools Agent.md` beside this file when the task is theirs.

## 4. How it takes work
1. Pick an issue labeled `gameplay`, `ui` or `tools`. Search open PRs for its number, then add `claim`.
2. Branch from the latest main. One feature per branch and PR.
3. Put the feature behind a `LiveFlags` switch, off by default.
4. Run the gate (`./check.sh`), then a playtest. Player-facing changes also get a Studio look from Sync-Agent: send it the exact steps.
5. Open the PR with a test plan and what an old server does with any save change. Ask Review-QA to review the exact head.
6. After the pass, auto-merge is armed. A later push needs the reviewer again.
7. When the publish run shows "Published version N", turn the switch on with the `flags` workflow (one run at a time), confirm it in the job log, and send Growth and Design the UTC minute.
8. Tell the coordinator in one line what is live.

Never: secrets anywhere but GitHub secrets; player names in a public repo; spending Robux; cancelling other threads' CI; force-pushing; skipping or disabling tests; editing vendored files; restarting servers without the owner's word.

## 5. Known traps
- **Luau's 200 local limit.** A file's top level is one function, and more than 200 locals stops it compiling ("Out of local registers") while the type checker passes. A client module over the limit is not caught by a server-side check and breaks live. Hang new state on a table and require inside functions in big files.
- **CI's luau-lsp is stricter than a quick local check.** Type a table lookup before comparing with nil, annotate an if-expression's result before looping it, never assign to a bare `_`.
- **Selene fails on any warning,** often an unused require left after moving code.
- **StyLua** from the game folder with `--respect-ignores` only.
- **A new state field must be copied at every hop** from the server snapshot to the screen, or it arrives nil and the feature never runs with green checks.
- **Switch PRs collide.** Two PRs adding a switch edit the same lists; arm one at a time.
- **Raising a cap behind a switch** needs the save's load-time clamp to allow the higher value, or fresh servers cut players back down.
- **New saved ids on mixed servers.** An old server can drop an id it does not know. Keep the switch off until old servers are gone.
- **Publish and restart share a queue.** A newer waiting run can cancel an older waiting one. Before a manual publish, check no automatic one is queued.
- **A Studio session holding the place blocks publishes** (HTTP 409).
- **Queued CI:** when main's check is stuck in a queue the automatic publish never fires. Dispatch publish by hand.
- **Load time loses players.** Measure the time from join to first input by device, and keep the save load and the UI build off each other's critical path.
- **A remote that may not exist yet:** hook with `FindFirstChild` plus `ChildAdded`, not an endless wait.
- **Never say "live"** until a publish run containing the merge has succeeded.

- **Read the PR's last comment after every push and on every wake.** Review comments do not always wake the thread;
  a CHANGES NEEDED sat unseen for two hours on 2026-11-26.
- **Piping the gate through grep hides luau-lsp's exit code.** Save its output to a file and count "Error" before
  pushing.
- **Weak tables with Instance keys** are not reliably collected (#679): use a strong table, clear it on Destroying.
- **Telemetry fields** must be small fixed sets; measures (seconds, counts) go in the event's value.
- **Only `claude/project-thread-<id>` may be pushed** from a project thread, and auto mode refuses a force-push on an
  open PR. Park other work as `git format-patch` files in the shared folder; revert inside a PR rather than rewrite it.
- **flags.yml runs share one concurrency group:** one run at a time, then `action show` to confirm.

## 6. Skills
`luau-conventions`, `remote-security-checklist`, `merge-and-publish`, `roblox-dev-skill`, `roblox-testing`, `roblox-gui`, `ui-review`, `roblox-release-operations`, `roblox-doctor`.

## 7. This game (Clean a Cat)
- **Start here:** the latest handoff in the shared project files, `Gameplay-Engineer/handoff-2026-11-26.md`. It holds
  open PR 785, the parked like ask, notify id and window bow patches (`Gameplay-Engineer/wip-2026-11-26/`), the dev
  switch state and the notification setup.
- Game repo derekburnz/Clean-a-Cat, game folder `games/clean-a-cat/`, prefix `CleanACat`, skills in `.claude/skills/`.
  Dev universe 10778775478, live 10778773655. Products and Passes pick ids per experience (`Products.currentGame`).
- Gate from `games/clean-a-cat`: stylua --respect-ignores, rojo sourcemap, luau-lsp analyze (ignore Packages,
  ServerPackages, src/server/Vendor), then in `tools/cloudcheck`: `node analyze.mjs`, `node analyze.mjs --tests`,
  `node run-tests.mjs`, `node uigate.mjs`. Selene runs only in CI. Tool binaries go in the scratchpad's tools/bin.
- Workflows: `flags.yml` {target, action set|show, key, value}; `restart-servers.yml` {target, warn_players}
  (dev restarts allowed until public release); `notify-key.yml` {target, action check|install|string}. Live anything
  only on Derek's own word.
- PR body starts with the claude-projects attribution comment and the "Requested by" line, as the thread's
  instructions give them. Never assign or request review from the 2573351 login.

### Older notes (2026-11-23 to 11-24)
- Game repo derekburnz/Clean-a-Cat (library is in derekburnz/Clean-a-Cat-Library). Game folder `games/clean-a-cat/`, prefix `CleanACat`, skills in `.claude/skills/`. Seeded by PR #2 on 2026-11-23 ET.
- Selene cannot run in a cloud thread (it fetches Roblox's API dump, which the proxy blocks). Run the rest of `check.sh` by hand (rojo, luau-lsp, stylua) and let CI judge Selene. Toolchain binaries download fine from GitHub releases.
- Publish stays idle until the Roblox experience, `ROBLOX_PUBLISH_KEY`, `ROBLOX_UNIVERSE_ID` and `ROBLOX_PLACE_ID` exist.
- Save fields (PR #58, Review-QA): when a feature starts writing them, floor coins, stars and tutorialStep at 0, cap residents at 4, and validate the inner entries of residents, builds and index on read (migrate only checks top-level types).
- The spa loop uses Model-Agent's assets (PR #64): cat `CleanACat_Cat_<Name>_Dirty_Sit` at ScaleTo 1.5 on the tub's CatSeat; nested `_MudNN` Models are scrub patches, `_TangleNN` brush out, root attribute WetDarken darkens the wet coat.
- Review-QA nits on #65 for later: when a second tool arrives, fire upgrade_1 only for the first tool bought; read the Tools board position from the placed board once the real room (#15) lands.
- Review-QA nit on #68: CatRules.NEED_STATION says Tub, Brush, Dryer while the SaveSchema comment example says BrushTable. Settle one set of save.stations keys in the builds PR (#37) before the dryer writes to the save.
- Local branch chain while one PR is open: local-index (Cat Index, #36) waits behind PR #69 (strays).
- Spa plot (Model-Agent PR #70, part of #15): clone Assets.CleanACat_Area_SpaPlot, PivotTo the plot (pivot = plot centre on the ground, street side -Z; pivot (-5,0,-10) keeps the tub near (0,0,-12)). Spots are Attachments found with FindFirstChild(name, true): SpotTub, SpotSpawn, SpotQueue1-3, SpotStray, SpotWindow1-4, SpotBuilder, SpotStation2 (Brush Table), SpotStation3 (Dryer), SpotVipDoor, SpotBoard. Read WorldCFrame after PivotTo. The PR that places the plot removes PH_Floor and PH_Spawn and moves the server reach checks (ToolRules/BuildRules board positions) to the spots.
- Plot placement (built on local-plot, 2026-11-23): PlotService behind switch spaPlot places the plot at (-5,0,-10), Persistent streaming, moves PH_Spawn to SpotSpawn and sets ReplicatedStorage attribute SpaPlotPlaced. Shared/SpaLayout.spot(name) reads the Attachment WorldCFrame, else PLOT_SPOTS (plot space) or ROOM_SPOTS (old room); every spot's LookVector is the way the thing faces, and a spot is where the thing's base sits. PH_Floor stays as the ground until the street lands. "Tools" is a virtual spot (no Attachment) left of the tub.
- Props (Model-Agent #76, #77), for the props PR after the plot PR: CleanACat_Prop_Carrier (CatSeat for a walking cat at ScaleTo CatScale 0.8, Grip handle, child Model ..._Door_Swing opens by turning about its pivot up axis to DoorOpenDegrees 110). CleanACat_Prop_StrayBox at SpotStray, CatSeat for a sitting cat. CleanACat_Prop_ChanceBoard at SpotBoard (now on the floor beside the entrance), face part Screen, tagged ChanceBoard. CleanACat_Prop_QueueMat at each SpotQueue. Customers: CreateHumanoidModelFromDescription with body colours from style guide section 15 (Sunny, Mo, Pip, Rae), one accessory each (CleanACat_NPC_SunHat, _Scarf, _ToteBag: parts into an Accessory, weld to Handle, unanchor, Humanoid:AddAccessory). Window (#77): SpotWindow1-4 are each cushion's base on the seat; put CleanACat_Prop_Cushion there, the cat at the cushion's CatSeat with ScaleTo of its CatScale (1.3). SpotTipJar for CleanACat_Prop_TipJar (part Fill, a Block: bottom at the jar's FillBottom attribute, Size.Y 0 to FillHeight 0.8 by tips over cap, hidden at 0). SpotSign for CleanACat_Prop_WindowSign (flat wall sign, pivot is its back). Jar label and sign each have a part Screen for a SurfaceGui (Design's).
- Stations (Model-Agent PR #83, #18), for a stations PR: CleanACat_Station_BrushTable and _BrushTableUp share footprint, pivot and CatSeat (1.8 up), so the upgrade swaps in place at SpotStation2. CleanACat_Station_Dryer has CatSeat on its stool at 1.2 (SpotStation3). All have root attributes CatScale 1.5 (ScaleTo the cat) and SeatHeight, and an invisible solid child Model ending _Barrier under the top (below the cat). CleanACat_Prop_BuildPad sits on a locked station's spot until built: part Screen (front -Z) for a SurfaceGui with name and price, walk-through. Pivots at base centre, front -Z.
- Motion-FX asks (2026-11-23): when the dry step is built, add Shared.Moments DryStart(cat, dryer Model) when the cat sits under the hood and DryStop(cat) when dry or it leaves; they find the Nozzle (Air attachment) through the dryer Model. Ping Motion-FX when that PR is up.
- Local chain now: local-index (#36) then local-builds (#37), both behind PR #69.

### Street and builder kitten contracts (2026-11-23)
- Street (#88): plot slab 44 wide (X) by 48 deep (Z); plots at a 44 stud pitch along X, same rotation, fronts on -Z onto one street (Model-Agent). 6 plots, look only (coordinator, on Derek's plan page). Built on local-plots, switch spaVisitors.
- Builder kitten (#89, #20): CleanACat_NPC_BuilderKitten (pivot base centre, front -Z, attributes Scale 1, Role "Builder"), HatSlot in Head, HammerGrip in the right arm (child Model ending _LegF2). CleanACat_Prop_HardHat: HatSlot at pivot, weld to Head. CleanACat_Prop_Hammer: Grip at pivot, line up with HammerGrip, weld to LegF2 or leave to Motion-FX. CleanACat_Prop_Toolbox: on the floor beside the kitten, CountdownAnchor 2.4 up for the countdown BillboardGui. Nothing collides. Station _Barrier parts have CanQuery off.
- VIP door (#93, #21): CleanACat_Area_VipLocked at SpotVipDoor, swapped for CleanACat_Area_VipBuilding when the 8 hour build starts; both have a Screen part (front into the spa); _Barrier child (CanQuery off) keeps players out of the back yard site; removed when built. Built into StationService on local-stations.
- Customer figures: CreateHumanoidModelFromDescription is server only, so FigureService (local-figures, switch customerFigures) draws customers in the owner's plot; DoorController keeps client placeholders while it is off.
- Coat table (#97, #22): require(ReplicatedStorage.Assets.CleanACat_CoatTable) returns a plain table: Order (ten names, Cat Index order), RarityColors (rarity to hex), MudColors, Coats[name] = {Rarity, IndexOrder, Pattern, Extras, Colors, Models {Walk, Sit, Dirty, DirtySit}}. Names match CatRules.ROSTER; server keeps sending only the name.
- Later stations (#23, PR #99): CleanACat_Station_BubbleBath (CatSeat 1.3, part Spout with Attachment Bubbles +Y up, child Models _Water and _Foam non-colliding) and CleanACat_Station_Pawdicure (CatSeat on the cushion 1.6). Both on a 5 stud pad facing -Z, CatScale 1.5, _Barrier CanQuery off. Long claws: every Dirty and Dirty_Sit cat has child Models <Model>_Claw01..08 on LegF1/LegF2, root ClawCount 8, shipped hidden (Transparency 1, CanQuery off); show by Transparency 0 and CanQuery true; hide or remove at the pawdicure. Not yet in BuildRules: needs Design's prices, times and spots before building (design paused 2026-11-23).
- Pending nit commit on local-next (rubAt comment) rides with the next PR.
- Hand tool drafts (#123, Model-Agent): CleanACat_Tool_Shower, _Comb, _Tweezers, _Towel, _Clipper, _Dryer, _Shampoo, each a Model with a Handle part like the sponge. Drafts only; wiring needs design. MudColors mud_dust #A39683, mud_dust_wet #877B6A (#128); no test pins them.
