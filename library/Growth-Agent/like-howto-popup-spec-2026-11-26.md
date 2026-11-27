# Like how to pop up: spec (2026-11-26 ET, Growth-Agent)
Derek, playtest, 2026-11-26 6:01 PM ET: when the 10 second like countdown starts, a pop up says checking for the like takes about 10 seconds to update so people go do it, plus a little picture or mini looping clip of what liking looks like so they can copy it. Labels: OFFICIAL, SEEN (a page I read), JUDGMENT.

## Two changes to his wording, for honesty (JUDGMENT, explained to him in one line)
1. The game cannot read a like (Planning's check and mine; nothing is checked, the gift comes either way). So the pop up must NOT say "checking for the like": that tells a young player we are verifying something we cannot, and it breaks the card's promise. Say what is true: the gift unlocks in 10 seconds, and there is time to like meanwhile.
2. Where the like is made: SEEN (Beebom and Tech Nerdiness, 2026): the thumbs up is on the game's page, under the title or Play button, not in the running game. I found no source for a like button in the in game menu, so do not point at one. The picture shows a generic thumbs up being tapped, with the words "on the game's page". Where it sits on each device is NOT confirmed, so no arrows to a place.

## Rules check
- OFFICIAL: Roblox has no page I found that forbids or allows asking for a like or rewarding one (like-group-rewards-check-2026-11-25.md); Derek decided it is in, with the gift coming either way. Keep that: "if you like" wording, reward never depends on it, no hurry words, no red or timer pressure beyond the existing button.
- Young audience: plain words, one short pop up, a close button, never blocks Claim, never covers the countdown button, shown once per ask (when Like is tapped), not repeated on later asks the same visit.
- No Roblox screenshots or logos in the picture: ours is an original drawing in our style (Roblox's own UI is theirs).

## Copy (no emojis, no dashes, plain)
Title: Your gift is on its way
Body: It unlocks in 10 seconds. If you like Clean a Cat, tap the thumbs up on the game's page. Your gift comes either way.
Button: Got it
(The countdown text on the row stays "8 s" style; add nothing about checking.)
Caption under the picture: Tap the thumbs up
Reduced Motion: show the last frame still.

## The picture (small looping clip, about 2 s, built in the UI, not a video file)
Frames: 1) thumbs up outline in soft grey, hand hovering; 2) hand taps (hand scales down, small ring); 3) thumbs up fills pink with a tiny sparkle; hold, then loop. Colours from the HUD palette (heart pink, plum outline). Assets needed from Model-Agent in the HUD icon style: thumbs up outline, thumbs up filled, tapping hand, ring puff. Design-Agent tweens them in Luau (no new video asset; client only). Uploads go to the group (rule 18) and the ids go to Icons.

## Build
- Switch `likeHowTo` in LiveFlags, off by default, on in dev right away; on live only on Derek's word (feature switches stay off live).
- Shows when the like row's Like button is tapped (the server stamps likeAskedAt); needs `freeRewards` on.
- Events: `ask_shown` / `ask_answered` with id `likeHowTo` (add it to AskRules.IDS or the events drop silently; answer closed or yes on Got it).
- Review-QA looks at it on a phone size; picture on dev goes back to the coordinator.
- Tests: pop up shows once per ask; Claim still works while it is open; closing never loses the countdown; Reduced Motion still frame.

## Update 2026-11-26 night: icons changed (Model-Agent, PR 976)
Hand icons retired after the account moderation flag. The loop uses a grey heart (HeartOutline), the pink Heart for pressed, a cream TapDot and the RingPuff. Nothing uploaded until Derek's account is clear. Copy change so words and picture agree: Roblox's like button is a thumbs up, but our picture is a heart, so the body says "tap the Like button on the game's page" (not "thumbs up") and the caption under the picture is "Tap Like". Body: It unlocks in 10 seconds. If you like Clean a Cat, tap the Like button on the game's page. Your gift comes either way.
