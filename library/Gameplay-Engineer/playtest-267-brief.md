# Playtest brief: Bubble Bath, Pawdicure, Pro Brush (#267)

Main at 97778eb. Use a fresh local place only. Everything here is a Studio attribute or a Studio save.

## Switches
- Under test: `bubbleBath`, `pawdicure`, `proBrush`.
- Base they need: `spaPlot`, `scrubPrototype`, `customers`, `stations`, `builds`, `toolsBoard`, `gameHud`, `queueWindow`, `queuePick`, `recapCard`.
- Optional but worth having on: `catMotion`, `scrubFeel`, `scrubEffects`, `revealEffects`, `fluffEffects`, `dryEffects`.

Set them as ReplicatedStorage attributes `LiveFlag_<name> = true`, or through LiveFlagService's Studio path.

## Seed a save
The builds take 10 and 60 minutes, so seed the save instead. In Play, Server view, run this in the command bar:

```lua
local p = game.Players:GetPlayers()[1]
local S = game.ServerScriptService.Server.Services
local s = require(S.DataService).get(p)
s.coins = 5000
s.stations.BrushTable = true; s.stations.Dryer = true
s.stations.BubbleBath = true; s.stations.Pawdicure = true
require(S.StationService).refresh(p)
```

If `get` returns nil, the command bar has its own copy of the module. Tell me and I'll add a Studio-only seed. For the Pro Brush, buy it on the Tools board (120 coins).

## What each step does
1. **Who's next? card.** A Rare, Epic or Legendary customer shows the Smell (🫧) and Claws (💅) needs beside mud, tangles and wet. These are emoji stand-ins, with no upload yet.
   - With 4 or more needs on a short screen, the needs stack above the pay and the dots shrink.
   - The rolls: smell is 50% on Uncommon and 100% on Rare and up. Claws is 50% on Rare and 100% on Epic and Legendary. Commons get neither, so it may take a few customers before a claws cat shows up.
2. **Order.** Scrub the mud, brush the tangles, then the Dryer. After that comes the Bubble Bath (if the cat has smell), then the Pawdicure (if it has claws), and last the bows.
3. **Bubble Bath.**
   - The cat moves to the station's CatSeat, with 6 white `PH_Suds` puffs round it.
   - The player drags a finger on the cat, about 12 studs of swirl (roughly 3 seconds), and the puffs pop one by one.
   - The bar reads "Step N of 6 · Swirl the suds". It already names the bath while the cat dries.
4. **Pawdicure.**
   - The cat moves to the station's CatSeat with long claws showing.
   - A gold outline (`PH_PawRing`) marks one front paw. A 0.5 second hold snips its 4 claws one after another.
   - The ring then moves to the other front paw, and a second hold finishes the step.
   - The bar reads "Trim the claws" and the hint reads "Hold on each paw".
5. **End.** The cat goes back to the tub for the bows, then the recap shows.
6. **Pro Brush.** Once bought, the tangles brush out in 2 strokes instead of 3.

## Pass criteria
- **Step bar:** it shows exactly as many steps as this cat takes, 4 plus 1 for each later need. There are no gaps and no stray pips.
- **Input:** each later step needs the player's own input. Nothing completes by itself.
- **Station seats:**
  - After the bows, the cat is never left floating or stuck at a station.
  - Rolling back or leaving mid-step leaves no `PH_Suds` or `PH_PawRing` behind.
- **Pay:** the recap bonus adds 8 coins with the Bubble Bath built and 15 more with the Pawdicure. Coins rise by the recap total.
- **Console:** there are no new console errors.
- **Off check:**
  - With `bubbleBath` and `pawdicure` off, the same seeded save shows no Smell or Claws needs, no later steps and no extra pay.
  - Neither station is drawn, and the 4-step bar is unchanged.
  - Turning a switch off while that cat waits in the line redraws its card without the need.

## Risky, look closely
- The step bar's pip spacing at 6 steps on the phone profiles.
- The cat's scale and facing on the two new CatSeats (Model-Agent's CatSeat and CatScale attributes).
- Whether the claws are visible and can be held on a phone.
- The recap bonus and the coin totals.
- The Tools board redrawing when `proBrush` flips.
- The Smell and Claws HUD icons are emoji stand-ins. That is expected, not a bug.

## Screenshots wanted
- The 6-step bar.
- Each station step.
- The queue card with 5 needs.
