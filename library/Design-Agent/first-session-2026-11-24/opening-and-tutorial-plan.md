# Clean a Cat: the opening (Suds in a box) and the tutorial

Design-Agent, 2026-11-24 ET. Replaces the opening of `first-session-2026-11-23/first-session-and-tutorial-plan.md` (spawn at the tub with a stray). Steps from the first customer onward are unchanged from that plan. Status: draft from Derek's idea. Planning-Agent OK'd the flow 2026-11-24 (notes folded in below; timings also in Planning-Agent/gdd-proposed.md). Waiting on Model-Agent's renders. Nothing here is locked until Derek decides the game.

## Derek's idea (2026-11-24, his words, short)
Suds shouldn't stand. The game opens with a quick scene: a truck drives past, a box falls off the back and lands in front of you on the street. You open it and it's Suds, all muddy. The tutorial is cleaning him and getting a score. Then he stays with you as your spa mascot through the game, explains things and shows up when you unlock new things.

## Two ways to show the truck: DECIDED A (Derek, 2026-11-24 1:36 PM ET: "A for sure for truck")
- **A. Quick intro shot.** The camera takes a short framed shot of the truck going by and the box falling in front of the player, about 3 seconds, then the camera snaps back behind the player and they play. No skip button: it is short enough not to need one. The player cannot move during those 3 seconds.
- **B. Played.** The camera stays the player's from the first frame; the truck passes in view because they spawn facing their spa across the road. Nothing is taken from them, but some players will look away and miss the box falling.
**The bump (Derek, 2026-11-24):** it is an animation. The truck rolls along, its wheels hit a bump in the road, the truck jolts up, the back door swings open and the box flies out, bounces once and lands right in front of the player. The truck rattles on and away, nobody notices.
Beats (about 3.5 s in A): 0.0 truck enters; 1.2 front wheels hit the bump (jolt, small dust puff, a thunk); 1.4 back wheels hit it, back door swings open; 1.5 box flies out in an arc, spinning a little; 2.2 box hits the pavement, squash and one bounce; 2.6 box settles; 3.5 truck gone, camera back to the player.
Both end the same way: box on the pavement, dim plus arrow, **Open!** Recommended: A, kept to 3 seconds, because the box landing is the hook and B can miss it; the timer in the table below is the same for both.

## What changes for Suds
- Suds is a normal cat on four paws, the same blocky build as the customer cats: black coat, blue eyes, pink nose. No hat or smock. A mint collar with a small gold bell marks him as the mascot; he gets it at the naming moment, so the muddy kitten in the box has no collar.
- He is the mascot, not a resident. He does not earn window tips and does not count toward Cat Index 1 of 10; he has his own card in front of the Index (proposed, Planning-Agent to confirm).
- He never washes (staff Jo and Sam do). He talks in a speech bubble of a few words, never a window.

## Rules this has to keep (from the Tutorial-Agent rules)
1. The scene is short and cannot be skipped: under 4 seconds. In version B the player can still move and look around; in version A the camera is taken for about 3.5 s and handed back before the first tap. Reduced Motion or Less shake drops the jolt, the spin and the camera shot. A skippable scene is skipped by most players, so it only adds a wait.
2. The player taps every step. Nothing opens by itself; the box opens only on the player's tap.
3. The fun action comes early: the first tap (the box) at about 0:04, scrubbing by about 0:12. That is about 9 seconds later than the old opening; the box is the trade (a surprise and a cat of your own in the first 6 seconds). Growth watches `box_opened` and `first_scrub` against the old funnel.
4. One arrow and a few words at a time, readable on a small phone.
5. Everything ships behind off switches (below).

## The opening, second by second (from `loaded`, on a phone)
| Time | What the player sees | What they do | Funnel step |
|---|---|---|---|
| 0:00 | Spawn on the pavement across the quiet road from their own spa, facing it, so the first thing they see is their spa. Nothing on screen but coins (0). | Can already move and turn | `loaded` |
| 0:01 | A small pastel delivery truck comes from the left along the road between the player and the spa, honks once and rattles past. Its back door flaps open and a box tumbles out. The truck never comes onto the pavement. | Nothing; the camera stays theirs | none |
| 0:03 | The box bounces once and lands on the pavement about 6 studs in front of the player. The truck drives off right. | Nothing | none |
| 0:04 | The box wiggles and a small meow plays. Screen dims except the box; gold arrow bobs over it: **Open!** | Tap the box (or walk up and press the prompt; gamepad A) | `box_opened` |
| 0:05 | Flaps pop open. A muddy black kitten peeks out, blinks, shakes, a few mud drops fly. Line over him: **Meow?** (no name yet) | Nothing, 1 second | none |
| 0:06 | Dim plus arrow on the kitten: **Pick him up!** | Tap him | none |
| 0:07 | The player lifts him out of the box (Derek, 2026-11-24): arms fold across the chest and he sits in a loaf in their arms with a purr (Catch a Cat Cafe's carry, `Carry.luau` in the asset library). Green floor arrows run across the road (now empty) and through the spa door to the tub. Tip line: **Take him inside** | Walk (about 4 seconds) | none |
| 0:11 | At the tub, prompt **Wash him** | Tap the prompt; the arms open and he hops into the tub | none |
| 0:12 | **The view switches to the close-up wash view** (Derek, 2026-11-24): the camera eases in over about 0.6 s to our wash camera (wash.html: the cat big in the middle, the step line and pips or tick list at the top, no tool tray: Derek 2026-11-24, the tool changes by itself as in My Pet Salon, switch autoTool, PR 394). This is where the cleaning is taught, one tool at a time, so the opening flows straight from the carry into the wash with no menu. | Nothing | none |
| 0:12 | He sits in the tub. Arrow on him: **Scrub!** | Drag over the mud | `first_scrub` |
| 0:25 | At 80% clean the rest pops off and he shakes off with sparkles. 1.5 s, no skip. | Nothing | `first_reveal` |
| 0:30 | Arrow on the brush: **Brush!** | Tap the brush, three swipes | `first_brush` |
| 0:38 | Star score card (the recap card): 3 stars, always, so nobody fails the opening. His name appears on the card for the first time: **Suds**, and a mint collar with a gold bell pops on with a jingle. | Tap Done | `first_photo` |
| 0:42 | Suds hops out of the tub, trots to his cushion on the front desk by the door and curls up. Bubble: **I'm Suds! Let's open the spa!** | Nothing; the bubble fades after 3 s | `suds_home` |
| 1:00 | The first customer walks in with a fixed easy common cat. The bench pick opens after that customer (about 1:45) and the first window stray moves to about minute 4. From here the 2026-11-23 plan carries on (step 7 onward), with Suds as the pointer for world things. | | `first_customer` |

Total to the first customer stays at about 1:00, the same as before.

## The box (Derek's call, 2026-11-24)
A plain, random brown cardboard box with no writing, the kind that falls off any delivery truck. Not a soap crate. The cat inside is messy and muddy and has no name yet; he becomes Suds when the wash is done, so the name first appears on the score card (the naming moment). Before that, every line calls him "the kitten" or "him".

## Teaching the wash in the close-up view
- The kitten's wash has two steps, Scrub and Brush, so the tick list (`washChecklist`) shows two rows; customers later add Dry, Bath, Claws and the rest, each taught the first time it shows up, in the same view and the same way.
- Each step's first use (no tool pick: the tool follows the step, as in every wash): an arrow points at the mud (no tray to point at, since autoTool hides it), with **Scrub the mud!**; the ghost hand drags across it after 8 s idle. Then the same for the tangles with **Brush him!**. The tick list ticks each step. One instruction at a time; nothing is done for the player.
- After the last step, the shake-off and sparkles play in the close view, then the naming card shows at the side (recap `side` state) so Suds stays in view.
- On Open the spa! the camera eases back out to the player (about 0.6 s) and he hops to his bed.
- Reference was Derek's My Pet Salon screenshots (files 11 and 17): close camera, big step line, a tick list, tools beside the pet. Ours is our own wash view; nothing is copied.

## Suds after the opening
- **Pointer for world things.** When something in the world unlocks or needs a tap (the Tools board, the builder, a new station), Suds trots to it, sits beside it and shows a bubble of two or three words (**New soap!**, **Build here!**). That replaces the floating gold arrow for world things. HUD buttons still use the dim plus arrow, with Suds' face beside the words.
- **Unlocks.** When a new station opens, Suds sits by it with a sparkle and a bubble. He never opens a window; the player taps.
- **His four rules** (Planning-Agent): he points at each thing once, never opens a window, never points at anything that costs Robux, and is never sad or cross, including on day 2.
- **Idle.** Otherwise he is on his cushion, sometimes stretching or watching a customer. Tapping him plays a purr and a hop. No menu.
- **Welcome back.** The welcome-back card keeps his face as the speaker.

## Things only the client sees
The truck, the box and the scene are local to the new player's client, so other players on the server never see a truck. Suds is placed on the server like any cat once the box opens, so friends visiting the spa see him on his cushion. The server keeps the step reached; the client only plays the pictures.

## For the build (Gameplay-Engineer)
SpaService opens customer picks on stars above zero, so Suds's 3 stars would open them one cat early. That gate should count customers served instead.

## Resume
- The scene plays once per save. Left before opening the box: the next visit plays it again (under 5 seconds).
- Left after opening but before the score: the next visit starts with muddy Suds sitting in the tub, arrow on him.
- Finished: never repeats.

## Switches (LiveFlags, off by default)
| Switch | What it controls | With it off |
|---|---|---|
| `openingBox` (new) | The truck, the falling box, the box tap and Suds' first walk inside | The old start: spawn at the tub with muddy Suds already in it |
| `sudsMascot` (new) | Suds on his cushion, his bubbles and his pointing walks | Suds stays on his cushion with no bubbles; gold arrows point as before |
| `tutorialDim`, `tutorialTip`, `tutorialTrail` (existing) | Dim plus arrow, the tip line, the floor arrows | As now |

Per standing orders all switches stay off until Derek decides the game.

## Funnel changes
Add `box_opened` (between `loaded` and `first_scrub`) and `suds_home`. Keep the others.

## Motion (Motion-FX-Agent, issue #281)
Code-driven curves, no animation clip, all beats in one timing table. One setting picks shot (A, default) or player camera (B).

## Models (Model-Agent)
Suds on four paws (muddy and clean; sitting, peeking from the box, in the tub, shaking, curled on a cushion), the closed and open box, a small pastel truck with no brand or writing, a cushion on the front desk, a clean Suds UI portrait.

## Open points
1. Planning-Agent: Suds outside the Index count, the fixed 3 star first score, and the gdd-draft first session lines.
2. Derek: the builder kitten also stands upright. Keep it, or make the builder a staff member too?
3. Derek: does the truck honk (sound) or stay quiet? Recommended: one soft honk, so players look up.

## Build calls agreed with Gameplay-Engineer (issue #285, 2026-11-24)
- Three switches: `sudsWash` (a new save's first cat is the muddy kitten; with `openingBox` off he waits in the tub), `openingBox` (truck, box, tap), `sudsMascot` (Suds stays afterwards).
- No bows for him: the collar at the naming is his style moment. The first customer teaches the bows.
- His 3 stars are a score only: 0 coins, no Index stamp, nothing added to the save's stars.
- Only brand-new saves get him.
- ~~He trots ahead to the tub~~ Changed by Derek 2026-11-24: the player picks him up out of the box (tap) and carries him to the tub, using Catch a Cat Cafe's carry from the asset library (effects/luau-effects/Carry.luau, CarryPurr sound).
- Cushion first; the pointing walks come with the tutorial driver.

## Suds' help bubble (from Derek's My Pet Salon screenshots, reference only)
What works in theirs (files 12 and 16): a guide at the bottom with a bold short title, one or two lines and one big action button. What we do our own way:
- Suds (a cat on four paws, our blocky style) peeks up from the bubble's left edge; the bubble is our cream card with the ink outline and the kit's fonts, not their dark-on-white panel.
- Bottom centre, at most about 55% of the screen width on a phone, so it never covers the thumbstick (bottom left) or the jump button (bottom right).
- A title of two or three words, one line of at most about eight words, one button that does the step (for example **Wash him** walks the trail focus to the tub). Never a second button, never a Robux offer.
- The bubble never covers a button the player needs (their file 13 lets a badge toast cover Collect; ours queues toasts while a bubble or card is up).
- It shows only at a step or an unlock, never on its own timer, and fades when the step is done.
- Lines in his voice: short, warm, never sad or cross. Examples: **Meow?** (in the box, no name yet); **Thanks! I'm Suds!** / **Let's open the spa!** (after the wash); **New soap!** / **Try it on the next cat** (unlock).

## Bubble lines, first set (given to Gameplay-Engineer 2026-11-24, switch `sudsBubble`)
Title / line / button. Each shows once per save; "Show me" moves the focus and never opens a window.
- After the naming card: Let's open the spa! / A customer is on the way. / OK!
- First customer: First customer! / Wash their cat to earn coins. / Show me
- Bubble Soap affordable: New soap! / Bigger bubbles, faster scrubs. / Show me
- Brush Table affordable: Let's build! / Upgrades make your spa better. / Show me
- First wet cat: Wet cat! / Build a dryer to dry them. / Show me
- Long build offer: Before you go / The VIP Room builds while you're away. / Show me
- A station finished: It's ready! / Try it on the next cat. / OK!
Naming card: Meet Suds! / He's your spa cat now! / Open the spa!
