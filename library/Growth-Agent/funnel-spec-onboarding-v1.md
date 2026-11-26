# Funnel spec: onboarding_v1 and playtime marks (2026-11-25 ET, Growth-Agent)

Draft from gdd-draft.md (first session section). Rename steps if the design changes; a changed funnel gets a new name (onboarding_v2). Built per playbooks/funnels.md. All events are logged on the server, each step once per save. Custom fields: at most 3 per event (cohort or test arm, one detail, and keep the third free).

## Onboarding funnel, name `onboarding_v1`
| # | Step name | Fires when | Logged today |
|---|---|---|---|
| 1 | joined | the player's first join | ____ |
| 2 | loaded | the client finished loading and can move | ____ |
| 3 | first_move | first input | ____ |
| 4 | first_scrub | first scrub input on the stray's mud | ____ |
| 5 | first_reveal | the mud is gone and the real coat shows | ____ |
| 6 | first_photo | the before and after photo card is shown | ____ |
| 7 | first_customer | the first customer walks in with a dirty cat | ____ |
| 8 | first_upgrade | first tool or station bought | ____ |
| 9 | first_build_started | first build timer started | ____ |
| 10 | first_long_build_started | first build of an hour or more started | ____ |

Step 10 is optional in session one by design, so read it separately and do not count it as a drop in the first session read. Return is read as D1 and D7 in Creator Hub, plus a `returned_next_day` event only if the Creator Hub number cannot be split by group.

## Playtime funnel, name `playtime_v1`
Time marks for every joined player: moved, 30 s, 1, 2, 3, 4, 5, 10, 15, 30 minutes, 1 hour.

## Side events (custom)
- `milestone_time`: one per step above, value = seconds since load.
- `hint_shown` and `hint_followed_10s` (did the player move on within 10 seconds).
- `window_opened`: name of the window, in the first 5 minutes only. By plan there should be none unless the player tapped.
- `skip`: which scene, after how many seconds.
- `left_at`: on leave in the first session, the last step reached.
- `pack_offer_shown`, `pack_offer_closed`, `pack_bought`: only if the starter pack ships (see starter-pack-check-2026-11-25.md).

## Rules
- Server logs only. Mind the event budget: no per frame logging.
- A step filled in by a later step: choose and record. Recommended: do not backfill, so holes stay visible.
- Tell Growth the minute of every switch, publish and restart.
- Test arms go in a custom field; both arms log the same funnel.

## Status 2026-11-25
Built in PR #437 (merged to dev): onboardingFunnel switch on in dev, off on live. Not built yet: `skip` (no scene can be skipped) and the `pack_*` events (wait on the starter pack).
Decision: keep the name `onboarding_v1`. Live never logged this funnel, so live starts clean under v1. Dev data from before #437 used an older step list and is test data only: never read it for a decision and never compare it with live. Rename to onboarding_v2 only if a step changes after live starts logging.
