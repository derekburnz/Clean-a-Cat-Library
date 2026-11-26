# Clean a Cat: QA plan and first 5 minutes checklist

Review-QA-Agent, 2026-11-23 ET. Built from Planning-Agent/gdd-draft.md (draft, not locked). When the design changes, update this file, not a copy. Once the game repo is seeded, the feature plans move to `docs/playtests/` there and this file links to them.

## 1. How a PR gets through
1. Author asks for review at an exact head. I record that head; the verdict covers only it.
2. `git diff --stat main...<head>` first. Any vendored file, `Packages/` file or formatter noise outside the PR's scope fails it.
3. Gate: `games/clean-a-cat/check.sh` (rojo sourcemap, luau-lsp, selene, stylua --respect-ignores) green in CI.
4. Review in this order: remotes, saves, live switch, analytics, odds, leaks, UI and the five QoL checks.
5. Verdict PASS, CHANGES NEEDED or SAME_CODE, with restart needed yes or no and one QA line. On PASS arm auto-merge (merge commit) unless labeled on-hold.
6. Effort: high for the first review of the save service, any remote that pays coins, builds and timers, and game passes.

## 2. Gates that fail a PR outright
- A tutorial or first-session change not behind an off switch (the first minute guide, the stray in the tub, the opt-in prompt timing).
- A remote handler missing a type, range, ownership, distance or rate check.
- The client deciding coins, stars, cat rarity, need completion or a build end time.
- A save change with no answer to what an older server does with it.
- Shown chances on the board that do not match the code table, or anything paid that changes the chances.
- A script inside a model file.
- Any menu or prompt that opens by itself in session one (no shop prompt, no like request, no forced popup).

## 3. Per system checks (what I look for in each PR of the slice)
| System | Must hold | Abuse pass |
|---|---|---|
| Scrub and reveal | 12 to 20 mud patches max; patches cleared on the client for feel, completion confirmed by the server; works by finger drag and mouse hold | Fire "scrub done" with no cat, someone else's cat, twice, or 50 times a second: no pay |
| Brush and bow | Three swipes; bow choice from a fixed list by id | Send an unknown bow id or a string where a number goes: rejected |
| Customers and strays | Server picks the cat from the chance table; stars change odds only as the board says; first cat is always the stray | Request a customer while one is queued; pick a rarity from the client: ignored |
| Needs and stations | A locked station cannot be used; each need cleared once | Use the dryer before it is built; clear the same need twice |
| Display window | Tips while away are capped; window holds four cats | Set the clock back, rejoin fast many times: no extra tips past the cap |
| Builds | Server stores the end time as server time; two slots (kitten: one station at a time; building site: one room at a time; Second Builder pass adds a second kitten); finished build waits; nothing lost by coming back late | Start two stations without the pass; start with too few coins; finish early from the client; rejoin mid build |
| Index | Washed and Resident stamps once each; set bonus paid once | Re-wash to farm the set bonus |
| Saving | Every field has a default and a clamp; session lock; old save loads on new code | Leave during a build and during a purchase; two servers at once |
| Notification | Opt-in only, offered once after the first long build starts; one message per day max; no pressure wording | Start and cancel builds to spam messages |
| Game passes | PolicyService fetched per player; pass perks checked on the server | Claim pass perks without owning the pass |
| Analytics | Event names stable; at most three custom fields per event; values bounded | |

## 4. First 5 minutes playtest checklist
Run on a fresh account with no owner perks, phone size first. Each line has a target time from the design. A miss of more than 15 seconds is a ticket; a step that cannot be done is a blocker.

| # | Time | Step | Pass when |
|---|---|---|---|
| 1 | 0:00 | Spawn | Player is in their own spa at the tub, a muddy stray in it, sponge in hand. One arrow says Scrub. No popup, no menu open. Console clean within 10 s. |
| 2 | 0:03 | First scrub | First mud patch clears on the first drag or click. Bubbles and squeak play. |
| 3 | 0:15 | Reveal | Mud gone, real coat shows, cat shakes off. |
| 4 | 0:25 | Brush | Three swipes fluff the cat. Three bows offered, each tappable at phone size. |
| 5 | 0:40 | Photo and reward | Before and after card, coins go up by 10 on the HUD, stray hops into the window and is owned. |
| 6 | 1:00 | First customer | Customer walks in with a dirty cat, chance board lights up with the five chances, goal shows Cat Index 1 of 10. |
| 7 | 2:00 | First buy | Bubble Soap (30 coins) is marked as affordable, buys instantly, scrub gets wider, balance drops by 30. |
| 8 | 3:00 | First build | Brush Table upgrade: builder kitten hammers, countdown shows 10 s, spa stays usable during the build. |
| 9 | 4:00 | Locked need | A customer needs a blow dry; icon shows locked; dryer shows 150 coins and 1 minute, grey until affordable. |
| 10 | 5:00 | Dryer done | Dryer works and pays more per cat. Builder shows Bubble Bath at 10 minutes next. |
| 11 | later | Long build | Builder offers the VIP Room (8 hours) with "Start it before you go". The VIP Room builds on its own slot, so the kitten stays free. The bell shows on builds over 1 hour, and only a tap on it opens the opt-in prompt. |
| 12 | rejoin | Return | Rejoin: coins, cats, window, index and the build end time are all kept; window tips capped; finished build celebrates. Needs a published test server, not a local Studio place. |

Also on every run of this checklist:
- Tutorial off switch off: the game still works with no guide, nothing breaks.
- Tutorial steps are tapped by the player (dim plus arrow). Nothing advances by itself.
- No step needs a keyboard. All tap targets at least 44 px. Nothing hides under the thumbstick, jump button or notch.
- Funnel events fire once each in order: joined, loaded, first scrub, first reveal, first photo, first customer, first upgrade, first build started, first long build started.
- Record the time to first scrub. Home counts a bounce under 60 seconds, so the first scrub must land well inside that.

## 5. Devices
Studio device emulator sizes per run: small phone, large phone, tablet, desktop. Studio cannot fake real touch or real phone speed, so before the first session is called done, Derek does a two minute check on his own phone with exact steps from me. Sync-Agent drives every Studio run on DESKTOP-DFOGFG7; I send it numbered steps and what counts as pass.

## 6. Release checklist (each publish that touches the first session)
- Publish run green and names the version; the merged PRs are in it.
- Switches in their intended state; new switch on the same hour it publishes.
- Section 4 steps 1 to 6 still pass on phone size.
- No restart unless allowed (allowed until public release; after that only on Derek's OK).

## 7. What this plan assumes
- The design draft holds: customers plus strays, timed builds from seconds to 24 hours, no paid skips, three game passes. If Derek's playtests change the loop, sections 3 and 4 change with it.
- Scrub runs on the client for feel and the server confirms the result. I will hold the scrub PR to that.

## 8. Visual QA for draft models and screens (Derek's ask, 2026-11-24 ET)
Every draft model or screen from Model-Agent or Design-Agent gets this pass on top of the code checks. I look at the rendered picture, not only the file.
- Phone size: shown at 48 px (icons), at real phone screen size (screens) and from the default camera distance (models). It must still say what it is.
- One read: a new player can name the thing in one second without a label. Silhouette first, colour second, detail last.
- Style: Bubble Pastel palette, chunky rounded shapes, same outline and light as the merged cats, tub and plot. Nothing realistic or gritty next to it.
- Contrast: text at least 4.5:1, key shapes against their usual background at least 3:1 (the mud fix on Inky set the bar).
- Tap targets: at least 44 px, nothing under the thumbstick, jump button or notch; no menu opens by itself.
- Honest: no fake urgency, no "free", odds shown before anything random that Robux can reach.
- Budget and safety: inside the style guide budgets, no scripts in models, CanQuery off on hidden or invisible parts, uploads owned by the group.
- Verdict per item: KEEP, FIX (with the one change that matters most) or DROP.

### Open visual checks for the first human playtest (2026-11-24)
- Dirty cat read: show a new player a dirty Cotton at the tub at the default phone camera and ask "what is wrong with this cat?" with no prompt. It passes on "dirty" or "muddy". The emulator check passed for #155, but without the wisps a pale cat can still read as markings at 38 px.
- Scrub feel (#149): count the strokes needed to clear a cat. One swipe clearing most of the mud is too fast.

## Full street frame check (2026-11-24, #40)
- Sync-Agent ran it on main 9996bee in the dev place: 6 plots full (5 stand-ins from streetLoadTest), 5,471 BaseParts, worst spot about 102 draw calls and 166k triangles.
- A06 profile at Level 1: 60 fps at the cap, no dips. iPhone 14 profile: 240 fps at the cap, but also at Level 1, because Studio's graphics setting is manual on that PC. No new console errors.
- Verdict: relative PASS. The emulator fps is the PC's, not a phone's. Still open: a real low-end phone run (Derek), and the run at automatic quality, which needs Studio's graphics set to Automatic on the PC.
- Watch item: the door line is the heaviest part of a plot (about 563 of 980 parts). If the real phone run dips, cut there first, for example with clean or simpler cats in the door line at a distance.
- Found on the way: the player spawns against plot 1's wall, so the first view is a blur. This is a first-minute problem and needs its own issue.
- Code side of the speed budget (#182): Gameplay-Engineer's phone-lag code check is at /mnt/project-files/Gameplay-Engineer/phone-lag-code-check-2026-11-24.md. It found no leaks, bounded per-frame hooks, three particle write-every-time spots (sent to Motion-FX), and that persistent plots (about 980 parts each) are the biggest memory lever.
- Studio skills baseline (#178): the worst view is about 186k triangles and 106 draw calls, with a CPU frame of 4.2 ms average on the PC. The thresholds are in the playtest-report skill.
- First frame for a second player (#188, PR #197): every plot now has its own spawn. Sync-Agent's slot-change test passed except the first respawn right after a slot change, where the camera carries over from the old plot. That's a test-only path. A real join starts with a fresh camera, but that is unproven because Studio's MCP can't run two clients. Check it in the first human playtest with two phones: the second player's first frame shows their own cat's face.

## Added 2026-11-24 15:45 UTC: game HUD checks for the owner's phone run (#182)
- The HUD from #221 (gameHud) was captured at four presets in #228 (docs/playtests/2026-11-24-hud/). Every preset passes.
- On the owner's iPhone 12, with gameHud on and mid-scrub, check that nothing greys out the Menu or the lower left. In the emulator's iPhone step 1 shot a grey see-through band covered it, and it was gone at step 4. It is probably the emulator's touch overlay, but it needs a real phone to confirm.
- On the owner's iPhone 12, check that the 36 pt coin picture and the 39 pt tray pictures read at arm's length.

## Test movement (added 2026-11-26)
Every Studio run moves the character only with the `studio-test-movement` helper (`_G.qaWalkNamed("<Spot>")`). Never use `character_navigation`, held W/A/S/D, or a straight `MoveTo`. Report each walk as reached, method and seconds. Wall, door and slab checks also include a moving jump (A or D plus Space), on both R15 and R6.
