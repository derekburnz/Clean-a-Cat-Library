# Analytics events for each new piece (2026-11-25 ET, Growth-Agent)

For issue #530 and Gameplay-Engineer. Funnel name stays `onboarding_v1` (funnel-spec-onboarding-v1.md); these are side events. Server side only, at most 3 custom fields each (the order below), no per frame logging, each name stable. Log the minute any event is added so reads can split on it.

| Event | Fires when | Fields |
|---|---|---|
| wash_done | a wash finishes | dirt_level (1 to 4), steps, seconds |
| cat_lost | a cat leaves with an empty heart bar | dirt_level, rarity |
| worker_hired | a worker is hired | worker (jo, sam, lou), minutes_in_session |
| visitor_result | a special visitor is washed or missed | outcome (washed or missed), first (true or false) |
| crate_earned | a crate is given | source (visitor, quest, checkin) |
| crate_opened | a crate is opened | source (earned or bought), rarity |
| quest_done | a quest is finished | kind (daily or weekly) |
| checkin_claimed | a check in day is claimed | day (1 to 7) |
| ask_shown | an ask appears | ask (notify, like_favourite_group, favourite_second_visit) |
| ask_answered | the player answers | ask, answer (yes, no, closed) |
| gift_claimed | the free pet is claimed | favourite (checked true), group (checked true) |
| shop_opened | the shop is opened | from (button or pack_button) |
| purchase_step | each step of a buy | product, step (prompt, cancelled, granted) |
| skip_offer_seen | a Finish now button is first shown for a build | tier |
| skip_bought | a skip is bought | tier, first_long_build (true or false) |
| skip_credit_used | a skip credit is used | tier |
| pack_offer_shown | the starter pack button first shows for a save, once per save, from about 2:45 of play (PR 617; the 72 hour clock itself starts at first join) | none |
| pack_bought | the pack is bought | hours_since_start |
| pack_expired | the pack clock reaches zero | none |

Notes
- Count fields in review: a fourth field is dropped silently.
- Never log player names or ids in event fields.
- `purchase_step` product names are internal names, not prices, so prices stay out of the repo.

## Day 2 return: skip buyers versus those who wait
- Read once each group has several hundred players who reached day 2 (ab-tests.md). Under that, it is a direction only.
- Groups: skippers of the first long build, skippers of other builds, never skipped. Judge D1 and D2 from Creator Hub plus the `skip_bought` flag.
- Buyers differ from non buyers (more engaged), so a lower return for skippers of the first long build is a signal to look at, not proof. Compare with players who reached the first long build and waited.
- Tell Derek if skippers of the first long build return clearly less. A switch turns the first long build skip off.
