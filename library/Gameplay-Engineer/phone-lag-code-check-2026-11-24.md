# Phone-lag code check, 2026-11-24 (#182, code side)

By Gameplay-Engineer, on main at 9957d9a. This checks our Luau against the five causes in #182, for Review-QA's speed-budget page. Read-only: nothing here changed code, except where a PR is named.

## 1. Memory that grows through a session (leaks)
**Server: clean.** Every per-player table is cleared when the player leaves:
- DataService `sessions`
- SpaService `cats`, `nextId`, `lastSeq`, `queues`, `handedOut`
- FigureService `lastKinds`, `served` (and its folder, via `clear(player)`)
- FunnelService `pending`. `firstSession` is cleared in `DataService.beforeRelease`. If a save release failed, that one boolean would stay. That's harmless.
- PlotService `owners`, StreetLoadService `filled`. These are keyed by slot, with at most PLOT_COUNT entries.
- `player.CharacterAdded` connections die with the Player instance.

**Client: clean.**
- Stink prunes its `entries` once a second, for cats whose model is gone.
- `Effects.popIn` disconnects itself.
- The dryer stream disconnects on `DryStop` and when its nozzle goes.
- BuildBoardController cancels its 1 s ticker and connections in `disable`.
- ScrubController's visit cleans up with one Trove (#195).

## 2. Large or too many images
- Only 2 of the 24 PNGs under `assets/` are bigger than 512 on a side: `CleanACat_Palette.png` and `CleanACat_Palette_Metal.png`. Both are 256 x 1024, the same pixel count as 512 x 512, so they are within the budget.
- Code references 2 `rbxassetid://` images.

## 3. See-through layers and heavy particles. Changing particle settings while they run.
These three are **in Motion-FX-Agent's folder** (`src/client/Effects/`, `EffectsController`), so I didn't change them. They are small fixes:
- `Effects.streamFrom` runs **every frame** while the dryer blows (EffectsController's Heartbeat). Each frame it writes `Rate`, `Enabled`, `EmissionDirection` and the attachment's `WorldCFrame`, even when nothing changed. Fix: write each property only when its value changes, and set `EmissionDirection` once when the emitter is made.
- `Effects.stream` (scrub foam) writes `Rate` on every pointer move during a scrub, as drag speed changes. Fix: round the rate to a few steps, for example multiples of 10 percent of `maxRate`, and write it only when the step changes.
- `Stink.refresh` runs once a second and writes `Rate` and `Enabled` on every stink emitter, changed or not. Fix: compare before writing.

## 4. Scripts that run every frame, and connections never disconnected
Every per-frame hook in our code:

| Where | When it runs | Work per frame |
|---|---|---|
| ScrubController Heartbeat | only while the visit is on | one nil check; gamepad trigger only |
| Stink Heartbeat | whole session | one clock compare; real work once a second |
| EffectsController dryer Heartbeat | only while drying | `streamFrom` (see 3) |
| `Effects.popIn` RenderStepped | a pop-in's length, then it disconnects | one model scale |

- The server loops all wait 1 s or longer: BuildService 1 s, WindowService `TIP_SECONDS`, NotifyService and LiveFlagService on their check intervals.
- Stink also listens to `Workspace.DescendantAdded` for the whole session. Each call is an `IsA` plus an attribute read, so it's cheap. Even a full street of about 5,500 parts arriving at once costs well under a frame.

## 5. Leftovers from players who left, and what's loaded from ReplicatedStorage
- When a player leaves, their plot's stations and door line are cleared (StationService and FigureService `PlayerRemoving`). With `streetLoadTest` on, the slot refills after 1 s.
- Plots and the street are `ModelStreamingMode.Persistent`, so every phone holds all 6 plots all the time. That's about 980 parts per plot, and about 563 of them are the door line (Review-QA's watch item from the full-street frame check). It is the biggest single lever if a phone runs short of memory. Options are atomic streaming for plots that aren't yours, or a lighter door line on low-tier devices. Measure first: the full street ran at 60 fps at Level 1 on the A06 profile.

## Hand-offs
- Motion-FX-Agent: the three write-on-change fixes in section 3.
- Review-QA: link this page from the speed-budget page as the code-side check, and re-run it once per milestone.
