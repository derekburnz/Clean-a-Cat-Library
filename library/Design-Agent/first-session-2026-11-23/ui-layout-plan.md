# Clean a Cat: UI layout plan

Design-Agent, 2026-11-23 ET. Status: plan for the build, based on gdd-draft.md (design not locked). Phone first, landscape. Goes with first-session-and-tutorial-plan.md in this folder.

Roblox concepts: a **ScreenGui** is a flat layer of buttons and text drawn over the 3D world. A **BillboardGui** floats over something in the world (for example the icons above a cat). A **ProximityPrompt** is the small "press to use" tag Roblox shows when a player walks up to something.

## Principles
- Calm and brief. Detail sits behind a tap.
- HUD numbers are outlined text with an icon and no box. Only pressable things look like buttons.
- The player opens every window. Only a window's X closes it.
- As much as possible lives in the world, not on the screen: need icons over the cat, the chance board at the door, the tip jar, the builder kitten, the tools board.
- At most three side buttons on the screen at once.

## Screen zones (phone landscape)
| Zone | What goes there | Notes |
|---|---|---|
| Top left | Nothing of ours | Roblox's own menu and chat buttons live here. Use the core UI safe area insets so nothing overlaps |
| Top center | Goal line, one line, starting with Next: when it names a purchase, for example **Next: build the Dryer (75 coins)** or **Clean a customer's cat** | Outlined text, no box. Behind `TutorialGoalLine` |
| Top right | Coins, then stars under it | Outlined text plus icon. Coins count up when earned. Not buttons |
| Left edge, middle | Side buttons, top to bottom: Builder (hammer, with a ring that fills while building and a **Done!** badge), Index (book), Shop (later) | Round buttons, about 56 to 64 px on a phone, at least 24 px apart so each label clears the next button. The Shop button is hidden until the first build is done, so the first minutes stay clear |
| Bottom center | Tool hotbar: sponge, brush, dryer, bath, pawdicure | Locked tools show grey with a lock. The tool a cat needs glows. Keys 1 to 5 on desktop, shoulder buttons on console |
| Bottom left and right | Nothing of ours | Roblox's thumbstick and jump button on touch |

## In the world (BillboardGuis and parts)
- **Need icons** above the cat in the tub, the same icons as the hotbar slots, each ticks off when done.
- **Chance board** by the door: the five rarities with their chances in large text. Tapping it opens the Odds window with the full table per cat. Lights up from the second customer.
- **Builder kitten**: speech bubble for offers and a countdown over the station being built.
- **Tip jar** by the display window: shows coins waiting. Walk up or tap to collect.
- **Tools board** by the tub: tap to open the Tools window.
- **Camera button** next to the tub for the photo.

## Washing view
When a cat is in the tub and the player stands at it, the camera eases to a close view of the tub. On touch the thumbstick hides while washing so drags on the cat never move the player. A small **Stop washing** button sits top center under the goal line. When every need is ticked, the view eases back by itself. This is play, not a scene, so it is fine to hold the camera here.

## Windows (each opened by the player, X top right, a dark backdrop that does not close it)
| Window | Opened by | Content |
|---|---|---|
| Photo card | Camera button | Before and after side by side, coins earned, the cat's kind and Index stamp. X closes |
| Tools | Tools board | A short list: tool, what it does in a few words, price, Buy. Owned tools show a tick |
| Builder | Builder button or kitten | Two sections, one per build slot (gdd-draft, 2026-11-23): Stations (builder kitten) and Rooms (building site). Each shows its running build with countdown and the next builds with price and build time; while a slot is busy its other builds are greyed with "kitten busy" or "site busy", and a room build never blocks a station build; locked ones greyed with what unlocks them; the bell button for notifications on builds over 1 hour, with a visible label "Notify me" under it (phones show no hover text) |
| Index | Index button | Grid of cats, Washed and Resident stamps, set progress and its bonus |
| Odds | Chance board | Every cat that can come, its rarity and chance, and how stars change the chances. The same layout as any future odds screen |
| Shop | Shop button (after the first build) | Game passes, each with one line on what it does. Nothing random |

Windows are centered, take no more than about 70% of the screen on a phone, and use one scroll list at most. No window has a timer, a "limited" tag or a discount mark.

## Day 2 return
Nothing opens by itself on return. The finished build plays its celebration in the world (confetti over the new room or station), the Builder button shows **Done!**, the tip jar shows its coins and the goal line says **Your VIP Room is ready!** (or whatever finished). The board shows tomorrow's VIP customer as a silhouette.

## Look
- Soft pastel spa colors with warm wood; coins gold with a dark outline (UIStroke) so they read on any background.
- Fonts: Fredoka One for headings and buttons, Builder Sans Bold for numbers.
- Text at least 18 px on a small phone. Touch targets at least 44 px.
- A UIGradient on a text label tints the text too, so lettering on gradient buttons sits on a child label.

## Devices
- Phone small and large, tablet, desktop, console.
- Sizes use Scale with an aspect ratio constraint and a max size, so tablets and desktops do not get giant buttons.
- Console: every button selectable with the gamepad, button glyphs shown on the hotbar, text a step larger for the TV distance.

## For the build
- One folder of shared UI parts (button, window frame, outlined number) so every window looks the same.
- Every arrow target in the tutorial gets a stable name, so a later layout change does not leave an arrow pointing at nothing. Any UI change near the start re-runs the tutorial on a phone.
- A mockup picture of the phone HUD and the Builder window goes in this folder before the owner is asked to OK the look.
