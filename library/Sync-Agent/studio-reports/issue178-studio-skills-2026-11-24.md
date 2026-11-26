# Issue #178 step 1: Roblox's own Studio skills from an outside client, 2026-11-24

Result: all three skills work from an outside client (the PC session, through Claude Code's Studio MCP), and each was run on the game.

Setup: Roblox Studio 0.748.0.7481526, Studio MCP server on. Fresh local place from main at f021830, never saved or published.

## The tool
There is no `skill` tool any more. This Studio build has `list_roblox_skills` and `get_roblox_skill` (the old `skill` and `list_skills` were removed when Studio updated during the session). Studio also has `create_skill` and `edit_skill` for custom skills.

## Skills listed (13)
rbx-configs-experimentation, rbx-create-skill, rbx-debug, rbx-device-simulator-lua, rbx-docs-search, rbx-import-asset, rbx-instrument-analytics, rbx-network-simulator, rbx-open-cloud-usage, rbx-perf-profiling, rbx-permissions, rbx-scene-analysis, rbx-unit-test.

## The three we wanted: all returned full text, no errors
- rbx-device-simulator-lua: SKILL plus API_SPEC, about 30 KB. In use since the #122 job.
- rbx-perf-profiling: 54.6 KB, saved on the PC at C:\Users\Derek\Downloads\Clean-a-Cat-captures\skills-text\rbx-perf-profiling.md
- rbx-scene-analysis: 53.1 KB, saved at ...\skills-text\rbx-scene-analysis.md

## Device simulator
Works, including from the Play client. Four presets captured (spaPlot, customerFigures, stations, streetLoadTest, scrubPrototype, customers, stinkEffects on), on the PC in Downloads\Clean-a-Cat-captures\: skills-device-phone-iphone14.jpg (749 x 388), skills-device-tablet-ipad10.jpg (1179 x 819), skills-device-console-xboxone.jpg (1919 x 1079), skills-device-pc-average-windows.jpg (1365 x 768). The camera was parked beside the VIP door after the profiling run, so these show that view, not the street.
Closest to Derek's iPhone 12 (#182): the list has no iPhone 12. iPhone 13 and 14 are both 844 x 390 logical points at 460 ppi, the same screen size as the iPhone 12, so the iPhone 14 preset is effectively an iPhone 12 screen. The presets do not model its speed.

## Scene analysis (SceneAnalysisService, in Play, full street)
- Draw cost: 9,445 triangles, 11 draw calls from the spawn camera. Worst views: west end along all six plots 173,962 triangles and 97 draws; east end looking back 186,316 and 106; high above the street 190,760 and 96. Almost all in the Opaque pass. The skill's reference for 60 fps on most devices is about 800,000 triangles and 600 draw calls, so we use about a quarter of the triangles and a sixth of the draw calls.
- Instances 20,934: 3D objects 14,139 (Part 10,962, Model 2,819, MeshPart 286); values 2,069 (Vector3Value 1,331, mostly part data in the cat models); SpecialMesh 907; Animation 513.
- Script memory 1.8 MB; biggest ours: ScrubController 99 KB and CatMotion 95 KB, then Roblox's player scripts.
- Unparented (kept in memory but out of the game, a leak sign): 12, all inside Roblox's own PlayerModule, Animate and Freecam scripts. None in our code.
- Animation memory 0.14 MB, audio memory 2.8 MB.

## Perf profiling (MicroProfiler through LibMP, 97 frames, camera at the west end of the full street)
CPU frame time 4.16 ms average, 4.06 median, 5.11 at the 95th percentile, 5.87 max (this PC). Nothing in our code stands out. Largest non-idle work per frame: foreground thread 1.5 ms, events 1.0, physics arbiter 0.9, render Perform 0.6, Present 0.3, Simulation 0.3, Heartbeat 0.3.

## Console
No game errors. Usual no-DataStore notices and the three rbxassetid://203785492 lines.

## Not done
The Roblox docs page could not be opened (the MCP's http_get only reads .md pages); not needed, the skill texts came straight from Studio.
