---
name: bigger-spa-counter
description: Derek's 2026-11-26 ask for a bigger spa building and a counter window for waiting cats: the models, switches, sizes and spots (issue 746)
metadata:
  type: project
---

- Derek 2026-11-26 9:10 AM ET, his words: "too many white bubbles for popups around spa it makes it too cluttered also I think maybe making the base spa building bigger and an easier way for customers to line up maybe an open window from desk where they put their cats on the table while waiting so grabbing them is easy and can see patience bar but its still obvious who they below to is a good idea that way your not walking to the back of line to grab cats".
- Issue 746 (filed by Gameplay-Engineer). Two switches, both off by default: `bigSpa` places the bigger models, `counterLine` moves the waiting line to the counter. Design-Agent tints each counter mat to its customer and floats a small card over each cat.
- Model-Agent's part: `CleanACat_Area_SpaPlotBig`, a second plot model beside the small one (plot.py, `big_layout`), then `CleanACat_Area_StreetBig` and `CleanACat_Area_BackdropBig` at plot spacing 56 (44 today). The old models stay untouched until Derek confirms the big one on dev.
- State 2026-11-26 ET: the plot is on main (PR 753, passed by Review-QA). StreetBig and BackdropBig are built from the same code (street.py `big_layout`, backdrop.py `build_backdrop_big`): PlotSlot1-6 56 apart, PlotSpacing 56, pivot still slot 1's plot pivot with no turn, street 352 studs long (280 today), 460 parts. The world with six bigger plots is 2,585 parts (2,222 today), so it needs its own phone frame rate run in Studio before bigSpa goes on for players.
- Sizes (Roblox plot coordinates): room inside x -24..24, z -16..16 (was 36 by 26 studs, now 48 by 32). Plot x -28..28, z -24..30. Front wall, entrance and everything in front of the building unchanged, so the opening scene keeps its spots.
- Counter: open window on the tub's side, x 0.8..21.6, top 2.8 over the floor. Six places 3.2 apart, place 1 nearest the entrance: SpotCounterCat<i> at (3.4 + 3.2(i-1), 3.38, -15.6), SpotCounter<i> at (same x, 0.5, -19.4). Mats are parts named CleanACat_Area_SpaPlotBig_CounterMat<i>. An invisible barrier (CanQuery off) fills the space over the counter.
- Residents' cushions SpotWindow1-4 moved to a new display window on the other side of the entrance, the sign on the wall over it. SpotBoard and SpotGift moved along that side wall; SpotTipJar is on the counter.

**How to apply:** build with `build_all.py --only Area_SpaPlot` (or `Area_Street`, `Area_Backdrop`). The check sheet is Model-Agent/bigger-spa-2026-11-26/ in the shared files. See [[art-and-models]] and [[derek-plan-answers]].
