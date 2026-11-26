# Effects and motion: what to check against the speed budget (#182)

Motion-FX-Agent, 2026-11-25. Input for Review-QA's speed budget page (PR #423). Read from the code on main 7f6bbe0, no Studio run. The Studio numbers wait until the Studio PC is back.

## Hard caps already in code
`Effects/Presets.luau` checks every preset against these caps, and the specs fail if one goes over.

| Tier | Max rate | Max burst | Max lifetime | Max Highlights |
|---|---|---|---|---|
| low (every touch device, so the iPhone 12) | 8 | 12 | 1.5 s | 2 |
| high | 16 | 24 | 1.5 s | 4 |

Emitters are pooled. There is one emitter per preset, and bursts reuse it. The live count on the PC run (#54) was at most 4 emitters and 8 instances.

## Per-frame work (cause 4 on the page)

| Module | Hooked to | Runs when | Lets go |
|---|---|---|---|
| Effects (init) glow | RenderStepped | only while a glow pulse fades | disconnects when done |
| BrushShine | RenderStepped | only while a brush sweep runs | disconnects when no cat is tracked |
| Carry | PreSimulation | only while holding, or while the hop runs | disconnects after the hop or on destroy |
| CarryShared | a 0.25 s loop | always, but cheap: reads two attributes per other player | drops copies when the attribute clears or the carrier leaves |
| WashCamera | BindToRenderStep | only while the wash view is up | unbinds on the exit |
| CatMotion | PreSimulation | always connected; checks its switch once a second; steps rigs only while on (4 cats, 30 Hz, half rate past 30 studs, none past 60) | never, by design |
| Stink | Heartbeat | always connected; one clock compare per frame, refresh once a second; switch off on dev and live | never, by design |
| EffectsController dryer | Heartbeat | only between DryStart and DryStop | on DryStop or when the nozzle goes |

Particle settings are not rewritten every frame. `streamFrom` writes the attachment only when it moved, and the rate only when it changed (cause 3).

## Things the iPhone 12 run should measure (parked until the Studio PC is back)
1. **Wash scene blur.** washScene adds a DepthOfField at FarIntensity 0.3 on phones. Measure frame time with the wash view up, at the lowest and the highest graphics setting. Roblox drops DepthOfField at low quality by itself, so expect no cost at the lowest setting. If the 95th percentile frame at the highest setting goes over about 12 ms, drop the blur on phones.
2. **CarryShared with several carriers.** Each copy is a full cat model plus Carry's per-frame arm writes. The phone cap is the 3 nearest carriers. Check the frame time with 3 carriers in view.
3. **The opening.** It has the most effects at once: truck, road dust, box tumble, kitten. The 95th percentile frame should stay under 16.67 ms.
4. **Memory trend over 20 minutes** (check 3 on the page). Every effect here is pooled or destroyed, so client memory should stay flat over a long wash loop. Growth means a leak; the first places to look are CarryShared copies and BrushShine entries.
