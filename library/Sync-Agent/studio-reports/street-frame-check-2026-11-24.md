# Street frame check, issue #40, 2026-11-24

Verdict: pass on this PC, with a gap: run 2 was not at automatic quality (see below). Not a phone result: the emulator only sets screen size and graphics level, so fps is this PC's. A real low-end phone run by Derek stays the final gate.

Build: fresh local place from main at 9996bee (includes 008fbd4 and PR #167). Not the dev or published place; nothing saved; no flags workflow. spaPlot, customerFigures, stations and streetLoadTest set true from the server.

## Street fill: pass
All 5 empty plots (2 to 6) had 3 door customers holding dirty cats (Marble, LilacCloud, Smudge), all 5 stations (BrushTable, Dryer, BuilderKitten, Toolbox, VipRoom), the kitten and the VIP building site. Plot 1 (own): stations and a locked VIP.

## BasePart counts
Workspace 5,471 (client 5,476 with avatar). Street 105. Plot 1 441. Plot 2: 979 (Customers 563, Stations 174, Props 81). Plots 3 to 6: 984, 982, 982, 979.

## Method
Client script logged every frame (RenderStepped). avg fps = frames / seconds; low 1 s fps = worst sliding 1 s window. Every 0.25 s it read Stats.FrameRateManager (Batches as draw calls, Indices / 3 as triangles, AverageQualityLevel) and Stats.RenderCPUFrameTime. Walk: from plot 1 out to z -40, far west (x -112), far east (x 146), back. Worst spot: west end looking along all 6 plots.

## Run 1: Samsung Galaxy A06 (706 x 339), graphics Level 1 (confirmed)
- Stand 30 s: 1,800 frames, 60.0 avg, 59.9 low 1 s, worst frame 19.2 ms; 34 draw calls, 21,636 triangles.
- Walk 34.9 s: 60.0 avg, 59.6 low 1 s (near x -36), worst frame 22.2 ms.
- Worst spot 10 s: 60.0 avg, 59.9 low 1 s, worst frame 18.9 ms; 102 draw calls, 166,628 triangles; render CPU 3.2 ms.
- Ran at a 60 fps cap: never dropped below the cap, but this does not show headroom.

## Run 2: iPhone 14 (750 x 390)
- Stand 30 s: 240.0 avg, 239.2 low 1 s, worst frame 6.8 ms.
- Walk 35.0 s: 240.0 avg, 239.5 low 1 s, worst 8.5 ms; up to 67 draw calls, 115,920 triangles.
- Worst spot 10 s: 240.0 avg, 239.4 low 1 s, worst 6.7 ms; 101 draw calls, 164,696 triangles; render CPU up to 4.0 ms. Capped at 240 fps.
- Gap: the stats show quality Level 1 in both runs. Studio's in-game graphics setting on this PC is saved as manual Level 1 and scripts cannot change it, so "automatic" was not met. Studio's edit-view quality also reads Level 1 now (was Automatic before; it flips back after Play).

## Console
No new errors or warnings in either run. Only the usual no-DataStore notices and the three rbxassetid://203785492 lines.

## Shots (on the PC, C:\Users\Derek\Downloads\Clean-a-Cat-captures\)
street-frame-a06-q1-worst-view.jpg, street-frame-iphone14-auto-worst-view.jpg (iPhone 14 size, but Level 1).

## Side note
At spawn the player stands right against plot 1's wall, so the camera starts inside the wall and the first view is a blur until the player walks out.

## To redo run 2 at automatic
Someone at the PC: in Play, Esc, Settings, Graphics Mode to Automatic; in File, Studio Settings, Rendering, Quality Level to Automatic. Then the run can be repeated.
