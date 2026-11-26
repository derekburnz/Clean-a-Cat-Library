# How games reach a 99% like ratio, and who and when we should ask (2026-11-26 ET, Growth-Agent)

Derek: playing GloryBound he was never asked to like it, yet it has about 99%; maybe it asks only players who buy items. Labels: SOURCED = on a page I read, DEV = developer opinion, INFERRED = my reasoning, no source.

## What we know about GloryBound (SOURCED, 2026-11-25)
- 560,181 up and 5,592 down votes, 99.0%, about 16,600 players. Codes come from Discord, the group and milestones; no page I found mentions a like prompt or a like reward. How GloryBound asks, or if it asks at all, is NOT sourced. Derek's own play (never asked) is the only direct observation, and it is one session.

## What the platform allows (SOURCED unless noted)
- Votes: a high ratio is only the share of voters who vote up. No Roblox page I read sets who may vote (no playtime or account age rule found). A developer asked for a 10 to 15 minute minimum in Oct 2025 (a request, not a rule).
- A game can prompt a favourite (Roblox's own prompt) but not a like (DEV, and consistent with Planning's check). Roblox's PlayerFeedback API (announced 2025-10-30) lets a game show a text feedback dialog once per player per day per game; it does not take a rating. Roblox advises asking "after the core gameplay loop": after a milestone, a tutorial or a successful session.
- Discovery effect: one developer says the like ratio does nothing for ranking and favourites give a small boost (DEV, unsourced). Roblox's Home signals are play rate, quits, return and time played (home-recommendations.md), so a rating is not on the list.

## Why a ratio can be that high without asking (INFERRED)
1. Voters are self selected. Unhappy players tend to leave without voting; players who vote up are often loyal fans (Discord, codes, group), so a big fan base pushes the ratio up.
2. Votes from a large steady audience dilute the early negative ones. 565K votes means the game gets a vote from a lot of players; Roblox's own game page may be where most votes come from, with no in game ask at all.
3. Asking only buyers is possible but unsourced. Buyers are invested and more likely to be happy, so it would push a ratio up. I found nothing showing GloryBound does this; treat it as a guess.

## Recommendation for our like ask (JUDGMENT)
Who: players who just had a good moment, not everyone at once and not only buyers. Do not tie the ask to a purchase (a young player asked to like right after paying can read it as pressure), and do not filter by sentiment so that unhappy players are never asked (hiding the ask from the unhappy can read as steering the rating, and no Roblox page covers it). Time and milestone gating is fine.
When: our current plan is close to right: the first ask at about minute 7 follows the first special visitor's crate (about minute 5), which is a success moment. Tighten it:
- Show it only after a success: a crate opened, a 3 star recap, or a worker hired; at least a minute after any other ask.
- Never within two minutes of a lost cat, a failed purchase or a cancelled buy, never during a wash or a recap.
- One ask per session; a no is final for that visit.
- Second visit or after 10 cats: the favourite ask for players who have not favourited (already planned). This is the better ask: a favourite can be checked and prompted, and developers say it helps discovery a little.
- If a player says no, do not ask for a like again for 3 sessions.
- Keep the like line separate from the pet, as decided. The reward still depends only on the favourite and group.
Offer unhappy players somewhere to go: the PlayerFeedback dialog (text, once a day) after a cat is lost or a long session ends, as an option never as a replacement for the vote. JUDGMENT: low priority, ship later.
Measure: `ask_shown` and `ask_answered` are already logged; read answers by ask moment. Read the page's like percentage and vote count weekly in the benchmark sheet with the date, and note each switch change, because a ratio on a small vote count moves a lot (under a few hundred votes it is a direction only).

## Open
How GloryBound itself asks is unknown from here. Only someone playing it past the first sessions, or its developer, can say. Derek does not need to find out for our decision to hold.

## Update 2026-11-26: Derek's rule for the like ask (q2-likeask, with his note)
Good moments first (a special visitor's cat finished first, then a crate opened, a three star card, a helper hired); one ask per visit; no re-ask for three visits after a no; never within two minutes of a lost cat or a cancelled purchase. Derek also allows an ask after a completed purchase, at least two minutes later, never on the purchase screen, with an off switch. I called that a judgment, not a Roblox rule: I found no Roblox page against asking after a purchase, so his word stands. Keep the guards (two minutes, off the purchase screen, never after a cancel, a switch) and read like percentage and ask_answered by moment, purchase asks separately, so we can see whether they help or hurt.
