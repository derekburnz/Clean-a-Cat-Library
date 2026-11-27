# Cat Hotel (issue 1042, Derek's pick 2026-11-27)

Derek, 7:36 AM ET: "go with cat Hotel and draft it". It sits behind the back door that 1041 tapes off and unlocks with coins.

## The idea in one line
Before you log off, put a cat to bed in the hotel. It pays you while you are away, and when you come back it is waiting with your coins and a thank you gift.

## Unlock
- The back door (1041, switch `expansionDoor`) shows caution tape, a sawhorse, planks and a cone, with one prompt: "Unlock the Cat Hotel · 1,500 coins". The test price on dev is 50 coins.
- 1,500 coins lands at about minute 15 to 20 of the first session, so a new player can book their first stay before they leave on day 1. That is the day 2 hook.
- Once it is unlocked, the tape and materials go, the door opens and Suds says: "Book a stay before you go. Guests pay you while you're away."
- The Garden's locked gate stands at that door today. The Garden moves to the side yard, at a new spot `SpotGardenSide`. Its price, time and tip jar effect are unchanged.

## Inside
- A front desk with a bell, and four rooms along the walls, each with a round cat bed and a door sign (Bubble Pastel).
- Rooms 1 and 2 are open at unlock. Room 3 costs 3,000 coins and room 4 costs 8,000. Each is a Build board item with the usual build time and Finish now, which gives a long goal.

## A stay
1. While a room is free, a guest cat waits at the desk with a little suitcase. Guests are normal customer coats from Common to Legendary, rolled like the bench. They are never special visitors, who stay at the front.
2. A tap on the guest (or the desk bell) opens the stay card, which offers 1 hour, 4 hours or 8 hours. Each option shows its pay, and the card shows the gift chances.
3. The guest walks to its room and sleeps, with a small clock over its bed.
4. The stay runs on server time, online and offline.
5. When it ends, the guest sits up in bed with a coin bubble. The player walks in and taps the room, or taps "Collect all" at the desk. The coins come in and the gift shows in the reward popup. The room is then free again.

## Pay (tuning `hotel.*`)
| key | value | why |
|---|---|---|
| `hotel.unlock` | 1,500 coins (dev test 50) | First stay booked on day 1 |
| `hotel.rooms` | 2 at unlock, room 3 3,000, room 4 8,000 | Long goal |
| `hotel.stay` | 1 h 60, 4 h 200, 8 h 360 coins | A little better per hour on short stays, so an active player is not punished; 8 h is the "sleep" pick |
| `hotel.rarity` | Common ×1, Uncommon ×1.25, Rare ×1.5, Epic ×2, Legendary ×3 | A rare guest is a nice surprise |
| `hotel.gift` | 1 h: bonus coins 90%, a bow 8%, a crate 2%. 4 h: 75%, 18%, 7%. 8 h: 65%, 23%, 12% | Longer stays give better gifts. The chances are always shown on the stay card |
| `hotel.bonusCoins` | +25% of that stay's pay | |
| `hotel.notify` | "Your hotel guests are ready to check out", 13 and over who said yes, at most once a day, shared with `jar.notify`'s daily cap | |

For comparison, the tip jar with one worker earns 240 coins over 8 hours. Two hotel rooms on 8 hour stays earn 720, and they need the player to book them, which is the point.

## Rules
- No Robux inside the hotel. Room builds use the normal Build board, including its Finish now. A stay has no paid skip. Gifts are free and their chances are shown.
- The server decides everything. There are two remotes, `BookStay(room, hours)` and `CollectRoom(room)`, both validated and rate limited. The guest is rolled on the server.
- The save holds `hotel = { rooms, stays = { [room] = { kind, rarity, endsAt, hours } } }`. Stays are paid once (the stay is cleared before the pay is added).
- Behind switch `catHotel`, off by default, which needs `expansionDoor`.

## Who builds what
- Gameplay-Engineer: the server, save, remotes, guest roll, offline time, notification, the Garden spot move.
- Model-Agent: the hotel interior (desk and bell, four rooms, locked room signs), the guest's suitcase and sleeping pose, the side yard spot for the Garden.
- Design-Agent: the stay card, room bubbles, Collect all, the gift in the reward popup, Suds's line and the gate scenes.
