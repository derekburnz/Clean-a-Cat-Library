# Clean a Cat: tools and skills worth adding (2026-11-24 ET, Planning-Agent)

This is the file copy of Derek's tool picks page. Page: https://claude.ai/artifact/UQGWKRdcYzAKcLJJNZUZPC

Derek asked for a deep dive into open source repos and skills that could help before development goes further, with a focus on quality UI, menus and pop ups and on a game that looks and feels good on PC, phone, tablet and console without lag or crashes.

**Short answer:** no outside library beats what we already have for UI. The best finds are free tools that Roblox itself now ships and a few small pieces to fold into our own skills. We recommend 5 additions now, 5 small trials once the first real screens are built and no UI framework yet. Another 24 finds are on the skip list. **Nothing is added to the repo until Derek picks.** For each yes Planning-Agent opens a task for the thread that owns it.

Derek's picks save in the page database, collection `picks`, doc id `s-<id>` with `pick` (the option index, 0 is our pick) and `note`. The skip list note is `s-skip`. Read them with the ArtifactData tool.

Research notes behind this list: `Tools-Research/ui_libraries.md`, `performance_and_devices.md`, `skills_and_mcp.md` and `look_and_feel.md`.

## Add now
Five things that cost little and help every screen from the first one. None of them adds code to the game.

### 1. Use Roblox's own Studio skills for device checks and speed checks (`s-rbxskills`)
- **What it is:** Roblox now ships its own skills inside Studio. Three matter here. One flips Studio's device preview through phone, tablet, console and PC and takes a picture of the UI at each. One reads Roblox's frame timing tool to find what makes a frame slow. One checks draw cost, memory and leaks in the place.
- **Why:** It is the closest we get to seeing the real game on every device. Our test gate checks sizes in a stand-in for Roblox. This checks the real thing in Studio.
- **License:** Part of Roblox Studio. Nothing to copy.
- **Upkeep:** Kept by Roblox. Their page was last updated on November 20, 2026.
- **Cost and risk:** No install. One of our skills already says to use the device check when it is there. The change is to make it a must before any screen is signed off and to add the other two. Sync-Agent first confirms that the three show up in your Studio. That is not checked yet.
- **How it was checked:** Roblox's skills page and Studio MCP page, read today. The three names are confirmed: rbx-device-simulator-lua, rbx-perf-profiling and rbx-scene-analysis.
- **Who would do it:** Sync-Agent and Review-QA-Agent.
- **Options:** 0: Yes, add it / 1: Not now / 2: No. Our pick is 0.

### 2. Update our main Roblox skill from 2.19.0 to 2.23.0 (`s-devskill`)
- **What it is:** roblox-dev-skill by MSayib is the skill every thread reads before it writes Roblox code. Our copy is from October 22. Four releases came out since then. The newest is from November 23.
- **Why:** The new version knows Roblox engine 0.748 and sends threads to Roblox's Studio skills by itself. Stale facts are how threads end up using retired APIs. In the same change we add Roblox's own list of retired APIs and its latest features file as the first place to look.
- **License:** MIT. License file read.
- **Upkeep:** Very active. One author, 36 stars.
- **Cost and risk:** Someone reads the difference before it is copied. We take the skill and its reference files only and never its install scripts.
- **How it was checked:** Change log and license read from the repo today.
- **Who would do it:** The thread that owns the skills folder.
- **Options:** 0: Yes, add it / 1: Not now / 2: No. Our pick is 0.

### 3. Add five small UI and input guides to our skills (`s-uirules`)
- **What it is:** Three short rule files from izzyfrm/roblox-ui-skill (screen sizes, button states and motion, UI bugs) go into our ui-review checklist. Two skills from EL4CTEO/roblox-skills (roblox-ui and roblox-input) are added whole.
- **Why:** They fill thin spots in what we have: controller focus, the eight states of a button, motion times of 0.12 to 0.30 seconds, the order of a big moment (result, emphasis, effects, details, next step), safe areas and bugs like a hidden window that still takes taps.
- **License:** MIT for both. License files read.
- **Upkeep:** Both are small one person repos. Their last changes were in September and October 2026.
- **Cost and risk:** roblox-ui states two dated Roblox changes that we could not confirm. Whoever copies it checks them against Roblox's docs first. Our helpers read these files as summaries, so the full text gets a read before it goes in.
- **How it was checked:** Helper summaries of the files plus license files read today.
- **Who would do it:** Design-Agent and Review-QA-Agent.
- **Options:** 0: Yes, add it / 1: Not now / 2: No. Our pick is 0.

### 4. Build Roblox's comfort and device settings into every screen (`s-settings`)
- **What it is:** Roblox has built-in settings a game can read: the player's text size choice, less see-through backgrounds, reduced motion, the kind of input in use, safe areas around notches and the top bar, controller button pictures and vibration.
- **Why:** This is most of what makes a game feel right on each device and it needs no library. Roblox's console guide asks that a TV player sitting 8 to 10 feet away can read everything and reach every button with four directions, select and back.
- **License:** Built into Roblox.
- **Upkeep:** Kept by Roblox. The old vibration service is retired. HapticEffect replaces it.
- **Cost and risk:** It becomes lines in our ui-review checklist and, where it can be measured, in the test gate. Our effects code already honors reduced motion. Text size and see-through are not handled yet.
- **How it was checked:** Roblox's accessibility, console and GuiService pages, read today. Our code searched.
- **Who would do it:** Design-Agent and Gameplay-Engineer.
- **Options:** 0: Yes, add it / 1: Not now / 2: No. Our pick is 0.

### 5. Pick one low end phone as the test device and make Roblox's speed rules our budget (`s-baseline`)
- **What it is:** Roblox's own advice is to choose one weak device and test on it all the time, because Studio cannot show real phone memory. Roblox gives few numbers: 16.67 ms per frame for 60 frames a second, an example budget of under 1,000 draw calls, most images at 512 by 512 or smaller and a closer look once more than 2 to 3 percent of sessions crash. It gives no memory limit for phones.
- **Why:** Five causes cover most phone lag and crashes in a game like ours. Memory that grows through a session. Large or too many images. See-through layers and heavy particles. Scripts that run every frame and are never disconnected. Leftovers from players who left. A named phone and a short budget catch these early.
- **License:** Roblox's public docs. Nothing to copy.
- **Upkeep:** Kept by Roblox.
- **Cost and risk:** None. It joins the open job on your plan page to name your test devices. Review-QA-Agent turns the numbers into a checklist.
- **How it was checked:** Roblox's performance pages (design, identify, improve, memory), read today.
- **Who would do it:** Review-QA-Agent.
- **Options:** 0: Yes, add it / 1: Not now / 2: No. Our pick is 0.

## Try on one screen
Five small trials for when the first real screens are built. Each one is tried on a single screen and dropped if it adds nothing.

### 6. spr, a one file spring library for bouncy UI (`s-spr`)
- **What it is:** One call makes a window or button move like a spring: a pop in with a little bounce or a squash when pressed.
- **Why:** Springs are what make chunky cartoon UI feel alive and they stay smooth when a move is cut short. Roblox's built-in tweens do not handle that well.
- **License:** MIT. License file read.
- **Upkeep:** 146 stars and 1 open issue. The last change we could see was in July 2024, so treat it as finished and not active. We would keep our own copy of the one file, as we do with ProfileStore. The backup is Spring from RbxUtil, which is MIT and was updated in August 2026.
- **Cost and risk:** It must honor reduced motion and it has to run in our test gate's stand-in for Roblox. Try it on the recap card. If it adds nothing over tweens we drop it.
- **How it was checked:** License file read today. Stars and dates from the repo page and a mirror.
- **Who would do it:** Motion-FX-Agent.
- **Options:** 0: Yes, try it / 1: Not now / 2: No. Our pick is 0.

### 7. Trove, a cleanup helper that stops memory leaks (`s-trove`)
- **What it is:** A screen adds everything it makes to a Trove: connections, windows, running animations. One call cleans it all when the screen closes.
- **Why:** Memory that grows through a session is the top cause of phone crashes. One cleanup habit in every screen prevents most of it.
- **License:** MIT. License file read. It is part of Sleitnick's RbxUtil.
- **Upkeep:** About 475 stars, updated in August 2026. On Wally as sleitnick/trove 1.8.0.
- **Cost and risk:** It would be the first outside package in the game code after ProfileStore. We either set up Wally packages or keep a copy of the one file.
- **How it was checked:** License and package list read from the repo today.
- **Who would do it:** Gameplay-Engineer.
- **Options:** 0: Yes, try it / 1: Not now / 2: No. Our pick is 0.

### 8. Flipbook, a Studio plugin that shows one screen at a time (`s-flipbook`)
- **What it is:** A storybook for Roblox. It shows a single screen or pop-up alone in Studio, in each of its states, without playing the game.
- **Why:** You and Design-Agent can flip through every window on the PC in seconds and compare it with the mockup.
- **License:** MIT wording in its license file. The other tool of this kind, UI Labs, is GPL-3.0, so Flipbook is our pick.
- **Upkeep:** Active. Version 2.5.0 came out in April 2026. The year is our reading of the releases page.
- **Cost and risk:** A plugin install in Studio on your PC and a small story file per screen. It does not run in the test gate. Our HTML mockups and the gate already cover a lot, so this is low on the list.
- **How it was checked:** License file read today. Release list read by a helper.
- **Who would do it:** Sync-Agent and Design-Agent.
- **Options:** 0: Yes, try it / 1: Not now / 2: No. Our pick is 0.

### 9. Asphalt, a tool that uploads images and sounds and writes their ids (`s-asphalt`)
- **What it is:** Images and sounds stay as files in the repo. Asphalt uploads them under the group, writes a Luau file with every id and keeps a lock file so nothing is uploaded twice. It also turns SVG icons into PNG and fixes dark edges on see-through images.
- **Why:** Icons and UI art will soon arrive in batches. Ids typed by hand are a common cause of blank images and uploads under the wrong owner do not load in a group game.
- **License:** MIT. License file read.
- **Upkeep:** Version 2.0.2 from July 2026, 170 stars, one main author.
- **Cost and risk:** It overlaps our own upload workflow, so we compare the two on the first batch of icons and keep one. It can use the group key that is already a GitHub secret, so no new key. Its guide says nothing about sprite sheets.
- **How it was checked:** License and version read from the repo today. Features from its guide, read by a helper.
- **Who would do it:** The thread that owns CI.
- **Options:** 0: Yes, try it / 1: Not now / 2: No. Our pick is 0.

### 10. Icon and UI shape sources with clean licenses (`s-icons`)
- **What it is:** Phosphor icons come in filled and two tone styles that suit chunky UI. Kenney's UI Pack has 430 files of plain buttons and panels to recolor. Lucide is a thin line set.
- **Why:** Drawn icons take time. These are free for commercial use with no credit line and can be recolored to our pastel set.
- **License:** Phosphor is MIT and Lucide is ISC, both license files read. Kenney's pack is CC0 by its own page.
- **Upkeep:** All three are widely used. The Roblox wrapper for Lucide was archived in July 2026 and leans on someone else's uploads. We skip the wrapper and upload our own copies under the group.
- **Cost and risk:** Your Roblox-Asset-Library is checked first. Design-Agent takes an icon from these only where it fits the style.
- **How it was checked:** License files read today. Kenney's page read by a helper.
- **Who would do it:** Design-Agent.
- **Options:** 0: Yes, try it / 1: Not now / 2: No. Our pick is 0.

## Not now
Four things that look tempting and that I would hold. The first two are the big ones.

### 11. No UI framework for now (`s-framework`)
- **What it is:** Fusion, Vide and React Luau are libraries that redraw the UI by themselves when the data changes.
- **Why:** They save refresh code on screens with long lists. But our test gate builds every screen in a stand-in for Roblox and a framework would have to run there first. Nobody has published phone speed numbers for any of them. Fusion's package on Wally is stuck at 0.3.0 while its main branch is at 0.4.0. React is the heaviest to learn and to ship.
- **License:** All three are MIT. License files read.
- **Upkeep:** Vide is at 0.4.1 from July 2026 with changes in October. Fusion last changed in February 2026. React Luau is active.
- **Cost and risk:** If a list screen such as the Cat Index gets painful in plain code we trial Vide on that one screen.
- **How it was checked:** License and package files read today. Dates from GitHub, read by a helper.
- **Who would do it:** Gameplay-Engineer if it is trialled.
- **Options:** 0: Agree, no framework now / 1: Trial Vide on one screen now / 2: Something else. Our pick is 0.

### 12. Roblox's built-in style sheets: not yet (`s-stylesheet`)
- **What it is:** Roblox now has a system like CSS. One sheet holds colors, fonts and button looks, with hover and press changes that animate. The animated part was fully released on July 27, 2026.
- **Why:** It would give one place for our cream windows and three color buttons. Two of our four research helpers said to adopt it. I say wait. Our test gate's stand-in for Roblox does not know style sheets. The gate could no longer see the fonts and sizes a sheet sets and would pass screens it has not really checked.
- **License:** Built into Roblox.
- **Upkeep:** Kept by Roblox.
- **Cost and risk:** We look again when the stand-in learns style sheets or when tests run in real Roblox.
- **How it was checked:** Roblox's styling page and release post, read today. Our test tool searched for style sheet support and none was found.
- **Who would do it:** Design-Agent if it is trialled.
- **Options:** 0: Agree, not yet / 1: Try it on one screen now / 2: Something else. Our pick is 0.

### 13. Run tests inside real Roblox from GitHub (`s-luauexec`)
- **What it is:** Roblox's Open Cloud can run Luau in the real engine from a GitHub workflow. A task runs up to 5 minutes and 10 can run at a time.
- **Why:** It would catch what the stand-in cannot, such as style sheets or engine changes. It cannot measure phone frame rate.
- **License:** A Roblox service.
- **Upkeep:** Marked stable in Roblox's docs.
- **Cost and risk:** The key we have may need one more permission, which is your step. It is worth it the first time a bug slips past the stand-in.
- **How it was checked:** Roblox's Luau Execution page, read by a helper today.
- **Who would do it:** The thread that owns CI.
- **Options:** 0: Agree, later / 1: Set it up now / 2: Something else. Our pick is 0.

### 14. More skills for when that work starts (`s-moreskills`)
- **What it is:** From TabooHarmony/roblox-brain: lighting, camera and localization. From EL4CTEO: performance. nonlooped/roblox-suite as a second opinion on retired APIs. The Chrrxs Studio MCP server for tests with several players.
- **Why:** None is needed for the first screens. Lighting and camera help once the spa room is dressed.
- **License:** All MIT. License files read.
- **Upkeep:** roblox-suite changed on November 20, 2026 and the Chrrxs server on November 2, 2026. The others last changed in September and October 2026.
- **Cost and risk:** Each has small flaws our helpers noted, such as targets with no source. Each gets a full read when its turn comes.
- **How it was checked:** Helper summaries plus license files read today.
- **Who would do it:** The thread whose work it is.
- **Options:** 0: Agree, later / 1: Add lighting and camera now / 2: Something else. Our pick is 0.

## Good to know

- **Fonts:** FredokaOne and Nunito are both built into Roblox, so nothing needs an upload. Uploading a custom font is not confirmed to be possible. Nunito comes in one weight only. The starter HUD still uses Gotham in two places.
- **Lighting:** Roblox's Soft lighting style fits a flat pastel look. The older Technology setting is retired. Roblox gives no cost numbers for screen effects on phones, so we keep to color correction and a light bloom and test on the phone.
- **A 3D cat inside a menu:** The window type that shows 3D inside UI is costly on phones when it moves or resizes. Use one at a fixed size or a picture made ahead of time.
- **Tap sizes:** Roblox gives no numbers for tap size or safe areas. Our 44 pixel rule is our own and matches the common phone app standard.
- **What nobody offers:** We found no open source library worth taking for confetti, counting numbers, tutorial arrows or toasts and no open source cartoon UI kit with a clear license. We build small ones of our own on our theme. For a long list such as the Cat Index we write our own list that reuses its rows.
- **Controller button pictures:** Roblox has its own way to show the right button picture for the player's controller. No library is needed.

## Looked at and skipped

| Find | What it is | License | Why we skip it |
|---|---|---|---|
| React Luau, Roact | UI frameworks | MIT, Apache-2.0 | React is heavy for our needs. Roact was archived in December 2023. |
| UI Labs | Studio screen preview plugin | GPL-3.0 | Flipbook does the same job under MIT. |
| TopbarPlus | Buttons in Roblox's top bar | MPL-2.0 plus a credit rule | We keep out of the top bar. Using it means crediting it in the game description. |
| lucide-roblox | Roblox wrapper for Lucide icons | MIT | Archived in July 2026 and leans on someone else's uploads. |
| Zap, Blink, ByteNet | Libraries that shrink network traffic | MIT (ByteNet by its readme) | Not needed with 6 players per server. |
| CullThrottle | Pauses effects the camera cannot see | MPL-2.0 | Built for thousands of moving objects. A spa plot has few. |
| ObjectCache, PartCache | Part reuse pools | MIT, none stated | A 20 line pool of our own is safer. PartCache has no license. |
| Lune, Jest Roblox | Test runners outside Studio | MPL-2.0, MIT | Our CI already has its own runner. |
| run-in-roblox, Tarmac | Older build tools | MIT | Both are stale. run-in-roblox last changed in 2020. |
| Tungsten | Asset tool with sprite sheets | GPL-3.0 | Copyleft license and 17 stars. |
| darklua, Mantle | Code and settings tools | MIT | We have no need for them. |
| Sentry for Lua | Crash reports to an outside service | MIT | A hack week project that sends data off Roblox. Not for a young audience. Roblox's own dashboard shows crash rate. |
| Benchmarker | Speed test plugin | Paid, no license shown | Not open source. |
| Figma importers, Codify | Design to Roblox tools | Mostly closed or none | We design in HTML and build in code. Codify was archived with no license. |
| brockmartin/roblox-game-skill, JustineDevs/roblox-ai-os | Skill packs | No license | We cannot copy unlicensed files into a public repo. |
| roblox-brain player psychology skill | Retention tactics | MIT | Pity crates, countdown timers and streaks. It breaks our young audience rules. |
| AshExplained, 35 other checklists | Short skill checklists | MIT | Generic. We already took the five useful ones. |
| Other Studio MCP servers | Ways for Claude to drive Studio | MIT | Roblox's old one and the best known community one are archived. The built-in server covers the job. |
| UltimateList, virtualized-list | Long list helpers | MPL-2.0, not shown | Both need React. |
| OpenMoji, game-icons.net | Icon art | CC BY-SA, CC BY | Share-alike art is a no. game-icons needs a credit per icon and is not our style. |
| UIEmitter | 2D UI particles | Closed, sold | Not open source. |
| EZ Camera Shake | Camera shake | MIT | Last changed in 2023. Our effects use no camera shake by default. |
| NevermoreEngine | Very large module collection | MIT | Too big to take on. Good for ideas only. |
| SimpleToasts | Toast pop-ups | MIT | 2 stars and four months old. We build toasts on our theme. |

## How sure this is

- License files were read directly from the repo for 34 projects. Where a license came from a project's page and not its file, the card says so.
- This thread cannot open GitHub's commit pages for other people's repos. Last change dates come from research helpers and a few come from mirror sites. Treat them as close, not exact.
- Nobody has published phone speed numbers for any UI library. Any claim that one is fast on a weak phone is untested.
- Helpers read skill files as summaries. Anything we copy gets a full read first.

## Derek's picks (2026-11-24, 9:29 AM ET) and what happened next

| # | Find | Derek's pick | His note | What we did |
|---|---|---|---|---|
| 1 | Roblox's Studio skills | Yes, add it | | Task [#178](https://github.com/derekburnz/Clean-a-Cat/issues/178) |
| 2 | roblox-dev-skill 2.23.0 | Yes, add it | | Task [#179](https://github.com/derekburnz/Clean-a-Cat/issues/179) |
| 3 | Five UI and input guides | Yes, add it | | Task [#180](https://github.com/derekburnz/Clean-a-Cat/issues/180) |
| 4 | Roblox's comfort and device settings | Yes, add it | | Task [#181](https://github.com/derekburnz/Clean-a-Cat/issues/181) |
| 5 | One low end test phone and a speed budget | Yes, add it | | Task [#182](https://github.com/derekburnz/Clean-a-Cat/issues/182). Derek's weakest phone is an iPhone 12, so it is the real test phone and the cheap Android gap is covered as the issue says |
| 6 | spr springs | Yes, try it | show me example to see if we keep | Task [#183](https://github.com/derekburnz/Clean-a-Cat/issues/183), ends with a side by side clip |
| 7 | Trove | Yes, try it | add it if it adds no harm and doesn't hurt token usage | Task [#184](https://github.com/derekburnz/Clean-a-Cat/issues/184), kept only if three conditions hold |
| 8 | Flipbook | Not now | I will leave it up to you | Our call: not installed for now |
| 9 | Asphalt | No | no need since ai does it | Dropped |
| 10 | Icon sources | Yes, try it | show me example to see if we keep | Task [#185](https://github.com/derekburnz/Clean-a-Cat/issues/185), ends with a sample sheet |
| 11 | No UI framework | Agree, no framework now | | Decision recorded |
| 12 | Roblox style sheets | Try it on one screen now | show me example to see if we keep | Task [#186](https://github.com/derekburnz/Clean-a-Cat/issues/186), ends with pictures and a clip |
| 13 | Tests inside real Roblox from GitHub | Something else | use it if you think it would help without slowing updates too much or increasing token usage | Our call: wait |
| 14 | More skills | Something else | not sure | Parked until that work starts |

**The two calls Derek left to us**
- Flipbook: not installed for now. It needs a plugin on Derek's PC and a story file for every screen, which is more work per screen. The HTML mockups, the UI gate and Roblox's device check (#178) already show each screen. We look again if screens start to slip past those three.
- Tests inside real Roblox from GitHub: wait. Each run adds minutes to CI and the key may need one more permission from Derek. We set them up only if the style sheet trial (#186) is kept or a bug slips past the stand-in, and then on merges to main only so that pull requests stay fast.

The decisions are recorded in `docs/decisions.md` of the game repo (pull request linked in the thread).

**Update, 2026-11-24 10:19 AM ET:** Design-Agent reports that Derek dropped the style sheet trial (#186) after seeing it ("drop them we dont need it"). Screens stay in plain code and pull request 218 removes the trial. Tests inside real Roblox from GitHub were tied to keeping it, so they stay parked unless a bug slips past the stand-in.
