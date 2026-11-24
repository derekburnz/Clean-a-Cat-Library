# Performance and device research for Clean a Cat

Read on 2026-11-24. Method note: GitHub fields come from api.github.com and github.com pages read through a fetch tool. Some pages did not load (marked UNVERIFIED). The tool summarises pages, so exact license file text was not opened; licenses come from the GitHub license field or the README.

## Summary table

| Name | License | Last release or commit | Verdict |
|---|---|---|---|
| Roblox official performance docs (design, identify, improve, monitor, memory, streaming) | n/a | read 2026-11-24 | ADOPT as rules |
| Zap (red-blox/zap) | MIT | commit 2026-06-23 | KEEP IN MIND |
| Blink (1Axen/blink) | MIT | commit 2026-11-07 | KEEP IN MIND |
| ByteNet (ffrostfall/ByteNet) | MIT (README page) | UNVERIFIED | SKIP |
| CullThrottle (boatbomber) | MPL-2.0 | commit 2026-07-31 | KEEP IN MIND |
| ObjectCache (Pyseph) | MIT (page) | commit 2025-03-19 | TRY |
| PartCache (Xan_TheDragon) | UNVERIFIED, no license stated on DevForum | post 2019 | SKIP (write own pool) |
| RbxUtil (Sleitnick) | MIT | commit 2026-08-11 | TRY (select modules) |
| NevermoreEngine (Quenty) | UNVERIFIED | commit 2026-10-22 | SKIP |
| Vide (centau/vide) | MIT | commit 2026-10-26 | TRY (UI) |
| Fusion (dphfox/Fusion) | UNVERIFIED | commit 2026-02-02 | KEEP IN MIND |
| React Luau (Roblox/react-luau) | MIT | commit 2026-10-29 (read-only mirror) | KEEP IN MIND |
| Jest Roblox (Roblox/jest-roblox) | MIT | commit 2026-11-10 | KEEP IN MIND (CI already has own runner) |
| Lune (lune-org/lune) | MPL-2.0 | release v0.11.1 2026-10-21 | ADOPT for scripts if not already used |
| run-in-roblox (rojo-rbx) | MIT | commit 2020-07-20 | SKIP (abandoned) |
| Open Cloud Luau Execution | official | docs read 2026-11-24 | TRY for cloud tests |
| ScriptBench / Benchmarker | Benchmarker: no license, $5 minimum on itch.io. ScriptBench: UNVERIFIED | n/a | SKIP / KEEP IN MIND |
| Asphalt (jackTabsCode) | MIT | release v2.0.2 2026-07-07 | TRY |
| Tarmac (rojo-rbx) | MIT | commit 2024-01-08 | SKIP (stale) |
| darklua (seaofvoices) | MIT | commit 2026-07-13 | SKIP (no need) |
| Mantle (blake-mealey) | MIT | commit 2026-05-28 | SKIP |
| rbxmk | UNVERIFIED | UNVERIFIED | SKIP |
| sentry-lua (getsentry) | MIT | commit 2025-08-23 | SKIP |

## Official guidance (all read 2026-11-24)

1. Performance overview. https://create.roblox.com/docs/performance-optimization
   - Track three things: frame rate, memory, join time. 60 FPS means 16.67 ms per frame.
   - Memory can crash servers and keeps low-end and mobile players out. No numbers on this page.
2. Design for performance. https://create.roblox.com/docs/performance-optimization/design
   - Pick one low-end baseline device and test on it all the time. Do not trust the Studio emulator for memory, because Studio runs server and client together.
   - Use instance streaming for most places. Reuse meshes and textures. Avoid transparency between 0 and 1 (overdraw). Prefer events over per-frame work. Disconnect connections you no longer need.
   - Do not tie effects to UserGameSettings.SavedQualityLevel. Check the lowest and highest Editor Quality Level.
   - Keep things the client does not need out of ReplicatedStorage (client loads all of it).
   - Example target on that page: under 1,000 draw calls and 1,000,000 triangles for a baseline device. The page says this is one example, not a platform limit.
3. Identify. https://create.roblox.com/docs/performance-optimization/identify
   - Developer Console (F9): use the client, not Studio, for memory. MicroProfiler (Ctrl+Alt+F6): look for frames over 16.67 ms.
   - Investigate if client crash rate in the Performance dashboard goes above 2 to 3 percent.
   - Script Profiler and Luau Heap are not covered on this page (UNVERIFIED here).
4. Improve. https://create.roblox.com/docs/performance-optimization/improve
   - A 1024x1024 texture uses four times the graphics memory of a 512x512 one. Most images need at most 512x512; minor images under 256x256.
   - Shadows are off below graphics quality 4.
   - Clean up player objects and characters after leaving (Workspace.PlayerCharacterDestroyBehavior).
   - Use sprite sheets for UI (ImageRectOffset and ImageRectSize). Changing ParticleEmitter properties at runtime can hurt a lot.
5. Monitor. https://create.roblox.com/docs/performance-optimization/monitor
   - Performance dashboard shows client crash rate and client and server memory. No thresholds, no frame rate or device breakdown mentioned on that page.
6. Memory. https://create.roblox.com/docs/projects/performance-optimization/memory
   - Categories: LuaHeap (growth means leak), InstanceCount (growth means leaked references), PlaceScriptMemory, GraphicsMeshParts, GraphicsTexture, Sounds. No numeric mobile limit given.
7. Streaming. https://create.roblox.com/docs/workspace/streaming
   - StreamingMinRadius default 64, StreamingTargetRadius default 1024.
   - Recommended: ModelStreamingBehavior Improved, StreamOutBehavior Opportunistic (to cut out-of-memory crashes), StreamingIntegrityMode PauseOutsideLoadedArea.
   - Nothing specific for tiny maps. For a small indoor street, streaming is likely not needed to save memory, but the doc says use it for most places. Decide by testing on a low-end phone.
8. Device emulator. https://create.roblox.com/docs/studio/testing-modes
   - Previews screen size, pixel density, touch, keyboard. Page says nothing about memory or graphics quality accuracy.
9. GuiService. https://create.roblox.com/docs/reference/engine/classes/GuiService
   - PreferredTextSize (read-only enum, listen to property changes and resize text). ReducedMotionEnabled (boolean, no description on page). GetInsetArea(Enum.ScreenInsets) gives safe areas: DeviceSafeInsets, CoreUISafeInsets, TopbarSafeInsets. SelectedObject for gamepad focus.
10. Console guidelines. https://create.roblox.com/docs/production/publishing/console-guidelines
   - Design for 8 to 10 feet. Keep key UI inside TV-safe area (no numbers). Every element reachable with four directions, select, back. Use relative sizes, UISizeConstraint, build for low resolution first. Disable chat on console. Use InputActionLabel for button icons. Haptics through HapticEffect for key events, not too often.
11. Input Action System. https://create.roblox.com/docs/input/input-action-system
   - InputContext, InputAction, InputBinding. PreferredBinding gives the binding that matches the current device. InputActionLabel and Input Action Manager are labelled beta on the page.
12. HapticService page is marked deprecated. https://create.roblox.com/docs/reference/engine/classes/HapticService . Use HapticEffect (per console guidelines).
13. Luau Execution (Open Cloud). https://create.roblox.com/docs/cloud/reference/features/luau-execution
   - Tasks up to 5 minutes, 10 concurrent tasks per place. Endpoints marked Stable. Use cases include automated testing. It runs server-side in the engine, so it cannot measure phone frame rate.
14. Not read (page failed to load): ui performance page. PreferredInput page was not fetched (UNVERIFIED).

## Library and tool notes

### CullThrottle
- https://github.com/boatbomber/CullThrottle . Client library that culls by camera view and throttles per-frame effect updates by priority and time budget.
- License MPL-2.0. Pushed 2026-07-31, 80 stars, 0 open issues, not archived (API, 2026-11-24). README Wally example pins an rc version, so it is pre-1.0 (UNVERIFIED release date).
- Fit: Luau, Wally or rbxm. Needs Roblox client, cannot run in plain CI.
- Helps when thousands of objects animate. Our game has one small plot per player, so it is not needed now. Risk: extra complexity.
- Verdict: KEEP IN MIND, only if a spa plot gets many animated props.

### Zap, Blink, ByteNet
- Zap https://github.com/red-blox/zap MIT, pushed 2026-06-23, 190 stars, 9 issues. Blink https://github.com/1Axen/blink MIT, pushed 2026-11-07, 192 stars, 21 issues. Both are code generators from an IDL that make buffer-based remotes. ByteNet https://github.com/ffrostfall/ByteNet MIT, 184 stars (page); commit date and API data could not be read (UNVERIFIED).
- For 6 players and a few small remotes, bandwidth is not a problem. A generator adds a build step and CI complexity. Our remotes already need validation and rate limits by hand.
- Verdict: Zap and Blink KEEP IN MIND (type safe remote definitions might be nice later). ByteNet SKIP.

### ObjectCache and PartCache
- ObjectCache https://github.com/Pyseph/ObjectCache MIT per page, 19 stars, last commit 2025-03-19 (about 20 months old, so near the 12 month abandonment line; counts as stale). Reuses parts and models instead of creating and destroying them.
- PartCache by Xan_TheDragon, DevForum 2019, https://devforum.roblox.com/t/partcache-for-all-your-quick-part-creation-needs/246641 . No license or GitHub link on the page (UNVERIFIED). Do not vendor it.
- For bubble parts or mud blobs a 20-line own pool is safer than a dependency. Verdict: ObjectCache TRY only if a pool is needed; otherwise write our own. PartCache SKIP.

### RbxUtil
- https://github.com/Sleitnick/RbxUtil MIT, pushed 2026-08-11, 471 stars, 48 open issues. Modules include Trove, Signal, Timer, Tween helpers and others (module list not re-checked, UNVERIFIED). Wally packages, strict Luau.
- Trove style cleanup helps prevent memory leaks (official docs name leaks as a main crash cause). Verdict: TRY, take only the modules we need.

### NevermoreEngine
- https://github.com/Quenty/NevermoreEngine . Huge module collection. Commit 2026-10-22. License not read (UNVERIFIED). Large, opinionated, Studio-centered. Verdict: SKIP.

### UI frameworks: Vide, Fusion, React Luau
- Vide https://github.com/centau/vide MIT, 320 stars, commit 2026-10-26. Small reactive UI library (Solid style), Luau.
- Fusion https://github.com/dphfox/Fusion commit 2026-02-02; license and stars not read (UNVERIFIED). Note: last commit about 9 months old.
- React Luau https://github.com/Roblox/react-luau MIT, 584 stars, commit 2026-10-29, described as a read-only mirror of ReactJS 17 translation. Heavier than Vide.
- For a game with many 2D screens, a reactive library reduces manual UI update code and bugs, but adds a learning load and the agent must be able to test it on the fake Roblox in CI. Verdict: Vide TRY in one screen as a trial; Fusion and React Luau KEEP IN MIND. If the team prefers plain Instance code, SKIP all.

### Testing: Jest Roblox, Lune, run-in-roblox, Luau Execution
- Jest Roblox https://github.com/Roblox/jest-roblox MIT, 50 stars, no GitHub releases, latest commit 2026-11-10 (added AGENTS.md). Active. Verdict KEEP IN MIND; our CI already runs a Luau WebAssembly build.
- Lune https://github.com/lune-org/lune MPL-2.0, 949 stars, 66 open issues, latest release v0.11.1 (page showed 21 Oct, API commit date 2026-10-21). Standalone Luau runtime for scripts and tests outside Roblox. Verdict ADOPT if the CI runner is not already Lune-based.
- run-in-roblox https://github.com/rojo-rbx/run-in-roblox MIT, 78 stars, last commit 2020-07-20. Abandoned. SKIP. Use Luau Execution instead.
- Luau Execution: TRY for engine-level tests that need real Roblox APIs (5 minute limit).

### Benchmarking
- boatbomber Benchmarker: sold on itch.io as pay-what-you-want with a $5 minimum, no license shown on the page (https://boatbomber.itch.io/benchmarker, read 2026-11-24). Not open source as far as the page shows. SKIP for a public repo.
- An open source alternative "ScriptBench v3.0.0" exists on DevForum (https://devforum.roblox.com/t/scriptbench-v300-free-open-source-heavy-duty-graphing-benchmarker/3815286). The page content did not load, so license and repo are UNVERIFIED.
- Script microbenchmarks matter little here. The real tools are the MicroProfiler and Developer Console on a real phone.

### Build and asset tools
- Asphalt https://github.com/jackTabsCode/asphalt MIT, 170 stars, 15 issues, release v2.0.2 (2026-07-07), push 2026-07-28. Syncs asset files to Roblox and generates code that references ids. Fits our Rojo and group-owned upload rule if upload targets the group (check). Verdict TRY.
- Tarmac https://github.com/rojo-rbx/tarmac MIT, 35 stars, last commit 2024-01-08. Stale. SKIP.
- darklua https://github.com/seaofvoices/darklua MIT, 239 stars, commit 2026-07-13. Code transformer. Not needed. SKIP.
- Mantle https://github.com/blake-mealey/mantle MIT, 116 stars, commit 2026-05-28. Manages experience settings. We have Open Cloud workflows. SKIP.
- rbxmk: not read. UNVERIFIED, SKIP.

### Crash reporting
- getsentry/sentry-lua https://github.com/getsentry/sentry-lua MIT, 18 stars, last commit 2025-08-23. README: "hackweek project and not officially supported by Sentry". Needs HTTP to an outside service, which sends data off-platform, and HttpService calls are limited. For a young-audience game this is a risk. SKIP. Use the Creator Hub Performance dashboard and the Developer Console.

## What I could not find or verify
- No official mobile memory number (MB) exists in the pages read. Roblox staff gave none in the threads read.
- No open source frame rate or quality scaler built for Roblox was found in this pass. The official advice is to let Roblox auto-scale and not tie effects to SavedQualityLevel. A simple own module that checks average frame time and lowers particle rate is the likely answer. UNVERIFIED that none exists; I ran only a few searches.
- No open source mobile gesture or gamepad helper was researched in depth. Roblox's own UserInputService and Input Action System cover touch and gamepad.
- Official example repos: Roblox/place-ci-cd-demo is named by the Luau Execution page (not opened, UNVERIFIED). No mobile-tuned production template was verified.
- Libraries not checked: boatbomber's other tools, TopbarPlus, Red, Warp, Bridgenet2, Replica.

## (a) Device budgets

Official (Roblox docs, read 2026-11-24)
- Frame time 16.67 ms for 60 FPS (performance-optimization overview).
- Example baseline device target: under 1,000 draw calls and 1,000,000 triangles (design page, an example only).
- Textures: usually at most 512x512; minor images under 256x256; 1024 uses 4x memory of 512 (improve and memory pages).
- Lowest quality draw distance at least 500 studs (design page).
- Shadows disabled below graphics quality 4 (improve page).
- Streaming defaults 64 and 1024 studs (streaming page).
- Crash rate: investigate above 2 to 3 percent (identify page).
- Server memory: keep below 50 percent of 6.25 GiB plus 100 MiB per player (identify page).
- Heavy script work: keep per-frame work to a few ms (design page example: 5 ms per frame).

Community or unverified (no source read this pass)
- Our own budgets of about 1,000 triangles per cat and 10 to 13 parts are set by the team, not by Roblox.
- No official or widely cited number was verified for particles per second, UI instance counts or mobile memory in MB. Treat any such number as UNVERIFIED until measured on a real low-end phone.

## (b) Five common causes of lag or crashes on phones

1. Memory growth over a session (leaks, parts parented to nil and back, instances not streamed out). Sources: https://devforum.roblox.com/t/increase-in-memory-causing-crashing-on-mobile-devices/2805203 (developer reports; staff confirmed a mobile workaround, no numbers) and the Roblox identify page (LuaHeap and InstanceCount growth).
2. Large textures and too many unique images. Source: improve page (1024 costs 4x of 512).
3. Overdraw from transparency and many particles or changing particle properties at runtime. Sources: design page (avoid transparency 0 to 1) and improve page (ParticleEmitter changes).
4. Per-frame scripts and uncleaned connections. Sources: design page.
5. Leftover player and character objects, and loading everything in ReplicatedStorage. Sources: improve page (PlayerCharacterDestroyBehavior) and design page (ReplicatedStorage).
Note: iOS app memory error is also covered at https://en.help.roblox.com/hc/en-us/articles/203313540-iOS-App-Memory-Error (search result only, not opened, UNVERIFIED).
