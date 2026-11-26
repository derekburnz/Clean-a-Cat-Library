# First five minutes: one timeline (Design-Agent, 2026-11-25 ET)

Owner: Design-Agent, from Derek's fifth pass (Planning-Agent/playtest-notes.md): "make sure to not crowd any player with all at once", "make sure they don't appear all at same time and overload a player", "maybe script the first one to drop a crate and make a rare customer come within the first 5 minutes so they stay". Times are from `loaded` on a phone, for a player who does what each step asks. They are targets for the build and the funnel `onboarding_v1`, not promises.

## The rules every item below follows
1. **One ask at a time, a minute apart.** An "ask" is anything that wants something from the player that is not the wash: the notification prompt, the check-in card, the gift stand (like, join group, claim pet), the favourite prompt, the starter pack button's first appearance, and a new HUD button with its tip (outside the tutorial). A special visitor walking in is not an ask (it is play), but it still keeps 15 seconds clear of an ask. No two asks land within 60 seconds of each other, and the first ask after the tutorial's last step waits a full minute too.
2. **Never during a wash or a recap.** While the close-up wash view or the recap card is up, nothing else shows. An ask that comes due then waits until the recap closes plus 3 seconds of free walking.
3. **Never over a tutorial step.** A tutorial tip (step pill, dim, floor line) and an ask never share the screen. An ask waits for the step to finish.
4. **Queue, don't drop.** If two asks come due together, the later one waits its full minute. Order of priority: tutorial step, then special visitor, then HUD button, then cards, then platform prompts (notify, like, favourite).
5. **Nothing opens by itself except Roblox's own prompts we trigger on purpose** (notify, favourite) and the check-in card, which opens once. Everything else is a button or a stand the player chooses to tap. A "no" or X is final for that visit.
6. **Every first-session change ships behind its own switch, off by default** (rule 16), so `onboarding_v1` can show each one's effect on first-session quits.

## The timeline

| Time | What happens | Kind | Notes |
|---|---|---|---|
| 0:00 | Spawn across the road from the spa; the truck drops the box | Opening | No HUD but coins |
| 0:04 | **Open!** the box, Suds peeks out | Tutorial 1 | |
| 0:07 | **Pick him up!**, carry him to the tub along the green floor line | Tutorial 2 | Guide line (switch trailLine) |
| 0:12 to 0:38 | Suds's wash in the close-up view: scrub, brush (3 simple steps) | Tutorial 3 to 4 | Wash meter bar on area steps |
| 0:38 | Recap card: 3 stars, his name appears, collar | Recap | Full card (Derek: after every cat) |
| 0:42 | Suds trots to his cushion: "I'm Suds! Let's open the spa!" | Suds line | |
| 1:00 | First customer walks in (fixed easy common cat, 3 steps) | Tutorial 5 | Bench pick not yet, Suds points |
| 1:05 to 1:35 | Wash the first customer's cat | Wash | |
| 1:35 | Recap card, coins | Recap | Tutorial 6 "Collect your coins" |
| **1:45** | **Notification ask**, in Suds's bubble ("Want a ping when your tip jar fills?"), then Roblox's prompt on his button | Ask 1 | 13+ only (Roblox shows it to them only); Derek: "1-2min in" |
| 2:00 | Two customers wait: the bench opens on a tap of their faces; **Wash next** shown | Tutorial 7 | The bench is a button, not a pop up |
| 2:05 to 2:40 | Wash the second customer's cat | Wash | |
| 2:45 | **Index** button arrives with a short tip: "Your washed cats live here" | Tutorial 8 = HUD button 1 | Ends the tutorial |
| 2:50 | Free play: the player picks from the bench | | |
| **3:45** | **Check-in card** (seven days played, day 2 the good crate), once, between washes | Ask 2 | Waits if a wash started; one tap to close |
| **4:00** | **First special visitor** walks in (scripted, glow, "Special" chip on the bench card, long heart bar so nobody rushes) | Special | Inside 5 minutes as Derek asked |
| 4:05 to 5:00 | The player washes the special visitor's cat (level 4, about 8 steps) | Wash | If they ignore it, it waits; its heart bar is generous |
| 5:00 | Recap card with the **crate drop** (scripted for the first one only), opened by the player's own tap | Recap | Earned crate; the chance list shows |
| **6:00** | **Quests** button arrives with a tip: "Daily and weekly jobs" | Ask 3 = HUD button 2 | |
| **7:00** | **Gift stand** lights up in the spa (it has stood there since 0:00, unlit), Suds says "A free pet! Like and favourite the game and join our group" once. The card asks the like and favourite together; the pet waits on the favourite and the group join (Derek, 2026-11-25) | Ask 4 | Always findable after: the stand stays in the spa, and the HUD never covers it |
| later | **Helpers** button when the first station is affordable, **Build** when the first build is affordable, each with its own tip and at least a minute from the last ask | HUD buttons 3, 4 | Order set by the economy, never two at once |
| session 2 or after 10 cats | **Favourite ask** via Roblox's prompt, from Suds once, only for a player who skipped the gift stand | Ask 5 | The stand already asks it; this is the one reminder |
| starter pack | Button on the HUD per Derek's pick (after the tutorial or the second visit). If in session one: **still**, no bob or sparkles until the second visit (Review-QA, Growth rule: no shop prompt moving in session one) | Ask 6 | Countdown 72 hours from first join |

## Gaps check (minutes apart)
Notify 1:45, tutorial ends 2:45 (+1:00), check-in 3:45 (+1:00), special visitor walks in 4:00 (play, +0:15), quests 6:00 (+2:15 after the check-in, +1:00 after the crate recap), gift stand 7:00 (+1:00). No ask lands in a wash or a recap at these times for a player on pace. A slower player pushes everything later by rule 2 and the queue keeps the minute.

## Open for Derek (not blocking)
- Like ask at "about minute 5" was our earlier pick; the special visitor's wash and crate sit there now, so the gift stand (which carries the like ask) moves to about 7:00. If he wants it inside five minutes, it swaps with the quests button (gift stand 6:00, quests 7:00).
- Favourite ask outside the first five minutes (session 2 or after 10 cats).

## Ask ids and copy (for AskQueueController, Gameplay-Engineer, 2026-11-25)

One row per ask. `id` is what `ask(id, show, opts)` takes. Priority follows rule 4 (lower number wins a tie). `not before` is seconds of play in the first session. The tip is the one line beside a new HUD button (Suds's bubble at the bottom for asks he makes). Every line is at most about 40 letters so it fits one line on a small phone. Plain words, no "now", no "hurry", no "don't miss".

| id | priority | not before | What shows | Copy |
|---|---|---|---|---|
| `notify` | 5 | 105 | Suds's bubble, then Roblox's prompt on his button (13+ only) | "Want a ping when your tip jar fills?" Button: "Yes please" / X |
| `hud_index` | 3 | 165 | Index button with a tip | "Your washed cats live here" |
| `checkin` | 4 | 225 | Check in card, opens once | (the card itself) |
| `hud_quests` | 3 | 360 | Quests button with a tip | "Daily and weekly jobs for coins" |
| `giftstand` | 4 | 420 | Stand lights up, Suds's bubble once | "A free pet! Like, favourite and join our group" |
| `hud_helpers` | 3 | when Jo is affordable | Helpers button with a tip | "Hire help for the busy days" |
| `hud_build` | 3 | when the Second Tub is affordable | Build button with a tip | "Build a second tub" |
| `hud_tools` | 3 | when Sponge level 2 is affordable | Tools button with a tip | "Better tools, quicker washes" |
| `hud_shop` | 3 | after the tutorial ends (165) | Shop button, no tip, no bob in session one | none |
| `hud_pets` | 3 | when the first pet is owned | Pets button with a tip | "Give your pet a job" |
| `favourite` | 5 | session 2 or after 10 cats, only if the stand was skipped | Suds's bubble, then Roblox's favourite prompt | "Favourite us to find the spa again" |

The special visitor (240 s) is play, not an ask: it does not call `ask`, but the queue keeps 15 s clear on either side of its arrival.
