# Roblox skills and MCP research

Read on 2026-11-24. Method: GitHub pages, GitHub API and raw files fetched through a web-reading tool that summarises pages with a small model. Every "what it says" below is that summary, not a byte-exact read. Items I could not confirm are marked UNVERIFIED. I did not clone, install or run anything. The `gh` CLI was blocked for these repos, so I used web fetches.

## Table of finds

| Name | License | Last push or commit | Verdict |
|---|---|---|---|
| Roblox official: rbx-device-simulator-lua (Studio skill) | Roblox product, no repo | Docs page read 2026-11-24 | ADOPT (use via Studio MCP `skill` tool) |
| Roblox official: rbx-perf-profiling, rbx-scene-analysis | same | same | ADOPT |
| Roblox docs llms.txt, latest-features.json, deprecated.md | Docs: CC-BY-4.0, code samples MIT | llms.txt stamped 2026-11-23 | ADOPT (as a reference to point agents at) |
| Roblox/creator-docs | CC-BY-4.0 prose, MIT code | not shown (2,179 commits) | KEEP IN MIND |
| Roblox/studio-rust-mcp-server | MIT | archived 2026-04-03 | SKIP |
| Chrrxs/robloxstudio-mcp | MIT | 2026-11-02 | KEEP IN MIND |
| boshyxd/robloxstudio-mcp | MIT | 2026-06-06, archived | SKIP |
| princeofscale/bloxforge | MIT | 2026-10-15 | SKIP |
| JohnnyMorganz/luau-lsp | MIT | not shown (1,961 commits) | ADOPT (already in CI) |
| TabooHarmony/roblox-brain (other skills) | MIT | 2026-10-15 | ADOPT PART: roblox-input, roblox-camera, roblox-lighting, roblox-localization, roblox-performance |
| EL4CTEO/roblox-skills (other skills) | MIT | 2026-09-28 (conflict, see section) | ADOPT PART: roblox-ui, roblox-input, roblox-performance |
| izzyfrm/roblox-ui-skill (other rules) | MIT | 2026-10-04 | ADOPT PART: rules/responsive.md, interaction-motion.md, debugging.md |
| MSayib/roblox-dev-skill | MIT | 2026-11-23 (v2.23.0) | ADOPT (refresh our v2.19.0 copy) |
| WojciechJelen/roblox-dev-kit | MIT | 2026-10-26 | KEEP IN MIND |
| AshExplained/roblox-skills (other 35) | MIT | not shown | SKIP, except KEEP IN MIND for roblox-game-ux design brief gate |
| JoCoding-Inc/roblox-skills (other 3) | MIT | 2026-11-24 | SKIP |
| EL4CTEO/blender-skills (other) | MIT | 2026-11-21 | KEEP IN MIND |
| nonlooped/roblox-suite | MIT | 2026-11-20 | KEEP IN MIND |
| brockmartin/roblox-game-skill | NONE | 2026-03-04 | SKIP (no licence) |
| JustineDevs/roblox-ai-os | NONE | 2026-05-12 | SKIP |
| anthropics/skills | Apache 2.0 for many, check per skill | not shown | KEEP IN MIND |

## 1. Official Roblox material (best finds)

### Roblox-authored Studio skills (`rbx-` prefix)
- Source: https://create.roblox.com/docs/assistant/skills.md , read 2026-11-24.
- These ship inside Studio. The built-in Studio MCP server has a `skill` tool that "retrieves reference material" (source: https://create.roblox.com/docs/studio/mcp , 2026-11-24). The MCP page names "debugging, device simulation, and documentation search" as areas. So our agents already have these through the MCP we use. Nothing to copy, nothing to license.
- `rbx-device-simulator-lua`: switches Studio Device Simulator presets (phone, tablet, console, PC), toggles orientation and captures the UI at each form factor to check layout and safe areas. This is exactly the "see the game on a phone" tool we asked for.
- `rbx-perf-profiling`: reads MicroProfiler traces for CPU and GPU bottlenecks, frame spikes and memory by subsystem.
- `rbx-scene-analysis`: audits rendering cost, memory, instance counts, unparented leaks and asset inventory.
- Also listed: `rbx-debug`, `rbx-unit-test`, `rbx-docs-search`, `rbx-create-skill`, `rbx-configs-experimentation`, `rbx-instrument-analytics`.
- Creator-authored skills (announced 2026-07-09, https://devforum.roblox.com/t/assistant-updates-introducing-creator-authored-skills/4728447): a single Markdown file with `name` and `description`. Tied to the account, place-scoped skills only on the roadmap. Works through the Studio MCP in Claude Code.
- Safety: `rbx-instrument-analytics` says it adds tracking "after you approve the plan". Others UNVERIFIED (I read only the index page, not each skill body).
- Verdict: ADOPT. Add a line to our `roblox-gui`, `ui-review` and `roblox-mobile-playtest` skills telling agents to call `skill` with `rbx-device-simulator-lua` before signing off any UI.
- Caveat: the `rbx-` names are reserved, and Roblox may change them. Check they appear in the live `skill` tool list (UNVERIFIED on our machine).

### Official docs for agents: llms.txt
- https://create.roblox.com/docs/llms.txt , read 2026-11-24. Timestamp in file: 2026-11-23T23:13:18Z.
- Entry points for agents: `/docs/latest-features.json` ("correct your out-of-date training data"), `/docs/api/search?q=...`, Engine API index `/docs/reference/engine/llms.txt`, Open Cloud index `/docs/cloud/llms.txt`, and a deprecated API list `/docs/reference/engine/deprecated.md`.
- Quoted rules: "Never guess a URL." "Never use the APIs of a feature with "status": "deprecated"." "Add .md to any documentation URL to read it as Markdown." "Do not fetch /docs/llms-full.txt unless you can stream it."
- Pages that fit our goal: `/docs/en-us/ui.md`, `.../ui/position-and-size.md`, `.../production/publishing/adaptive-design.md`, `.../production/publishing/console-guidelines.md`, `.../projects/cross-platform.md`, `.../input/mobile.md`, `.../input/gamepad.md`, `.../performance-optimization.md` and children.
- Facts I checked in those pages (2026-11-24): console guide says players sit "8-10 feet away", use `GuiService.ViewportDisplaySize` with `Enum.DisplaySize.Large`, keep UI inside the TV safe area (no numbers given), disable chat on console, use `InputActionLabel` or `UserInputService:GetImageForKeyCode()` for button icons. The adaptive design page gives no numeric touch size or safe area. Any numbers in other skills (for example 44 px) are therefore the skill authors' own.
- Licence: docs prose CC-BY-4.0, code samples MIT (https://github.com/Roblox/creator-docs README, 2026-11-24; I read it in the README summary, not the LICENSE file itself, so UNVERIFIED at file level). CC-BY needs credit if we copy prose. Linking is enough for us.
- Verdict: ADOPT as a link list in our `roblox-dev-skill` / `luau-conventions` notes: "start from llms.txt, check deprecated.md and latest-features.json".

### Roblox/studio-rust-mcp-server
- https://github.com/Roblox/studio-rust-mcp-server , read 2026-11-24. MIT, 503 stars. Archived and read-only since 2026-04-03. Maintainers recommend the built-in Studio MCP server. Setup ran a downloaded binary and edited MCP client configs.
- Verdict: SKIP.

## 2. MCP servers beyond the built-in one

The built-in server (docs 2026-11-24) already has: script read and edit, `execute_luau` in Edit, Client or Server context, `search_game_tree`, `inspect_instance`, playtest start and stop, console output, screenshots and video, simulated player input, `http_get` for Roblox docs, `skill`, `save_place`, asset search, insert, upload, and generation tools. Warning in docs: clients "can read and modify content in your open Roblox places." `submit_feedback` can send reports without asking, but tells you each time.

### Chrrxs/robloxstudio-mcp
- https://github.com/Chrrxs/robloxstudio-mcp . Read 2026-11-24. MIT. 360 stars (API) vs 382 (page), so numbers differ by cache. Pushed 2026-11-02. 204 commits. Footer: "Based on boshyxd/robloxstudio-mcp v2.7.0". One maintainer.
- Adds over built-in: `capture_screenshot` plus mouse and keyboard input, `capture_video` (needs Windows or WSL and FFmpeg 8+), multiplayer testing, per-peer server and client eval, profiling and memory tools.
- Device emulation: not mentioned on the page. It does NOT give us phone-size capture. The built-in simulator skill does.
- Safety: monetization and experience-settings tools need an Open Cloud key ("can use every permission the key grants"). Runs Luau in live and edit contexts. Downloads a plugin release from GitHub if missing. Our rule 13 says keys stay in env vars.
- Verdict: KEEP IN MIND. Multiplayer and per-peer testing could help later. Not needed now.

### boshyxd/robloxstudio-mcp
- API 2026-11-24: MIT, 497 stars, pushed 2026-06-06, archived true. Verdict: SKIP (archived; a fork exists above).

### princeofscale/bloxforge
- https://raw.githubusercontent.com/princeofscale/bloxforge/HEAD/README.md . MIT (API), 7 stars, created 2026-06-18, pushed 2026-10-15. One person.
- Local Node 20 server and Studio plugin on localhost. Profiles `core`, `builder`, `tester`, `full`, `inspector`. Plan and apply gates and dry runs. Wraps Rojo, Rokit, Wally CLIs. Optional Open Cloud key.
- Safety: installs a plugin via `npx`, needs Studio "Allow HTTP Requests". No device emulation found.
- Verdict: SKIP. Overlaps the built-in server, tiny user base. The plan and dry run idea is nice, though.

### Others seen in search results only (UNVERIFIED: licence, upkeep, safety not read)
kolvian/roblox-mcp-server, jadonbp/studioforge, majidmanzarpour/vibe-blocks-mcp, code-and-relax/robloxstudio-mcp (API: MIT, 0 stars, pushed 2026-02-11, not a fork), EL4CTEO rbx-studio-mcp (listed on mcpservers.org), nhattamgithub mcp-roblox-docs, zubeidhendricks/roblox-studio-mcp-claude-code. Verdict: SKIP; the built-in server and the official docs search cover their jobs.

### Rojo and Open Cloud MCP
I found no maintained, official Rojo MCP or Open Cloud MCP. Our repo already uses Rojo CLI and Open Cloud scripts in CI. UNVERIFIED that none exists.

## 3. Tools that keep agents current on the API

- luau-lsp (https://github.com/JohnnyMorganz/luau-lsp , 2026-11-24): MIT, 558 stars, 1,961 commits, last commit date not shown. Roblox type definitions and docs are preloaded by default. Needs a Rojo sourcemap. It does not itself warn about deprecated APIs in the text I read (UNVERIFIED). Already in our gate.
- `deprecated.md` and `latest-features.json` from Roblox llms.txt: the best deprecation source. See section 1.
- MaximumADHD/Roblox-Client-Tracker (API dump history): UNVERIFIED, fetch failed.
- MSayib `roblox-api-monitor.py` downloads the API dump (changelog, 2026-11-24). It is part of the MSayib skill.
- roblox/creator-docs: CC-BY-4.0 prose, MIT code samples. Useful offline, not needed given the `.md` URLs.

## 4. Skill repos we copied from: what we did not copy

Note on dates: the tool I used reads GitHub pages through a summariser and some commit lists were blank. Where I give a date it came from the GitHub API endpoints.

### MSayib/roblox-dev-skill
- https://github.com/MSayib/roblox-dev-skill . MIT. 36 stars, 27 commits, default branch `master`. Latest commit 2026-11-23: "feat(v2.23.0): engine 0.747/0.748, Luau 0.746-0.748, 39 MCP tools & auto rbx-* skill routing (#20)". We hold v2.19.0, so we are 4 minor releases behind. Changelog file I could read stops at 2.18.1 (2026-10-17), so what changed in 2.19 to 2.23 beyond that commit title is UNVERIFIED.
- Folders not in our copy: none, we took the whole skill. It has 14 references including `ui-systems`, `performance-optimization`, `mcp-integration`, `agent-safety`.
- Safety: installers `install.sh`, `install.ps1`, `install.cmd` fetch from GitHub. `roblox-api-monitor.py` downloads the API dump. `tests/e2e/run_evals.py` runs `claude -p`. We should not copy the tools or installers, only the skill and references.
- Wrong or outdated: its changelog says Upgraded UIGradients and UIShadow are betas "not for published games", which matters for UI work.
- Verdict: ADOPT (refresh to v2.23.0 after diffing).

### TabooHarmony/roblox-brain
- https://github.com/TabooHarmony/roblox-brain . MIT. 209 stars. Pushed 2026-10-15 (we copied 2026-10-14 commit, so about one newer commit). 29 skills under `skills/core`, `skills/design`, `skills/gameplay`, `skills/tools`. Each skill is a short SKILL.md (about 300 to 600 words) plus `references/full.md`. Each has `last_reviewed` and `sources` fields. None of the ones I read had install, network, key or "act without asking" lines.
- `roblox-input` (gameplay): UserInputService events, `ContextActionService:BindAction` Sink and Pass, Input Action System, gamepad focus (`GuiService.SelectedObject`, `Selectable`), touch gestures, DragDetector. Last reviewed 2026-10-02. Weak: BindAction example uses an undefined `humanoid`; gamepad and touch sections are thin and point to full.md. Says `UseFixedSimulation` must be enabled in Studio. Verdict ADOPT PART.
- `roblox-camera`: CameraType, FOV, CFrame table, a PreRender loop, `ScreenPointToRay` vs `ViewportPointToRay`. Last reviewed 2026-06-29. Claim that Heartbeat "adds 1-frame lag" is unexplained. ADOPT PART.
- `roblox-performance` (core): MicroProfiler, Developer Console, Script Profiler, a targets table, Parallel Luau, StreamingEnabled, mobile notes. Last reviewed 2026-10-02. The 45 FPS mobile target and 33 ms threshold are unsourced. ADOPT PART (but see EL4CTEO and the official rbx skills).
- `roblox-lighting`: Lighting properties, Atmosphere, Bloom, ColorCorrection, DepthOfField, SunRays, day and night loop, local light cost. Last reviewed 2026-07-26. Rules like "Max 2-3 post effects" are unsourced rules of thumb. Useful for the "looks good without lag" aim. ADOPT PART.
- `roblox-localization`: LocalizationTable, `AutoLocalize`, `GetTranslatorForPlayerAsync`, Localization Tools plugin. Its description promises text overflow and string audit help the body does not give. ADOPT PART, low priority.
- `roblox-animation-vfx`: Animator tracks, burst emitters, flipbooks, tweens, Server Authority notes. Last reviewed 2026-10-02. File starts with a doubled `---`. We already have our own `animation-vfx`; take only as cross-check. KEEP IN MIND.
- `roblox-player-psychology` and `roblox-growth-design`: persuasion tactics. Per the summary it has variable rewards, pity crates, countdown timers, streaks, and a price ladder up to 999 Robux, with no guidance for under-13 players. Conflicts with our rules 9 and 10. SKIP. Also contains a math error ("40% D1 is 3x the players of 25% D1 by day 30").
- `roblox-analytics`: built-in AnalyticsService only (Custom, Economy, Funnel events). Quotes a rate limit "120 + (20 x CCU) calls/minute" with no source, UNVERIFIED. Roblox now has an official `rbx-instrument-analytics`. KEEP IN MIND.
- Other folders not read: roblox-architecture, collaboration-mode, data, luau-core, luau-patterns, luau-types, networking, security, server-data, game-design, monetization, building, npc-ai, physics, cloud, publish-checklist, studio-mcp, tooling. UNVERIFIED.

### EL4CTEO/roblox-skills
- https://github.com/EL4CTEO/roblox-skills . MIT. API says 17 stars and pushed 2026-09-28 (v1.1.0, "Support 29 agent targets"). Page summary said 78 stars and 29 commits. The page-reported and API values disagree, and the pushed date is before the commit date you gave for our copy (a7538bc, 2026-10-17). UNVERIFIED which is right. Check the repo by hand.
- 23 skills. Not copied and relevant:
  - `roblox-ui`: about 1,400 words. Covers `ScreenGui.ScreenInsets = CoreUISafeInsets`, Scale vs Offset, `UIAspectRatioConstraint`, `UISizeConstraint`, `UITextSizeConstraint`, `UIListLayout` flex, `UIFlexItem`, `UIGridLayout`, StyleSheet and StyleRule, gamepad navigation, `InputBinding.UIButton`, 44x44 px touch target, RichText, `CanvasGroup`, `UIDragDetector`, world UI, and React, Fusion and Vide notes. Issues: it states a `ClipsDescendants` default change "since Sep 24, 2026" and an opt-out removal "November 2026" which I cannot verify; text filtering advice names `FilterStringAsync` without the broadcast path; BillboardGui "distance scaling" claim is doubtful. No install or network lines. Verdict ADOPT PART, after checking those dated claims against the docs.
  - `roblox-input`: about 1,100 words. Input Action System, `UserInputService.PreferredInput`, haptics, ContextActionService as legacy, custom cameras with `BindToRenderStep`. `Workspace.PlayerScriptsUseInputActionSystem` unverified. ADOPT PART.
  - `roblox-performance`: about 1,400 words. MicroProfiler, `debug.setmemorycategory`, `debug.profilebegin`, streaming, `ContentProvider:PreloadAsync`, `RenderFidelity`, `CollisionFidelity`, `BulkMoveTo`, Parallel Luau. Its `ConnectParallel` example writes a shared table from parallel code, which its own text warns against. Claims `--!optimize 2` "is how Roblox compiles live games already", unsourced. ADOPT PART.
  - `roblox-studio-mcp`: setup and tool loop for the built-in MCP. Says `execute_luau` and `multi_edit` are real edits, "Only connect clients you trust". Covered by Roblox docs. KEEP IN MIND.
  - Others not read: roblox-analytics-liveops, roblox-text-chat, roblox-world-building, roblox-npc-ai, roblox-physics, roblox-networking, roblox-security, roblox-data-stores, roblox-monetization, roblox-open-cloud. UNVERIFIED.

### EL4CTEO/blender-skills
- MIT. Page says 430 stars, 22 skills. Latest commit 2026-11-21, "Release 1.3.3: edge-case fixes from stress testing (#15)". Our copy is from 2026-10-16.
- Not copied and relevant to look: `blender-pbr-materials`, `blender-texture-baking`, `blender-lighting-lookdev`, `blender-time-of-day`, `blender-weather-fx`, `blender-character-rigging`, `blender-animation`. For UI work none apply; for "look good" some art tasks might. Safety not read. KEEP IN MIND.

### WojciechJelen/roblox-dev-kit
- MIT, page says 0 stars, 41 commits. Latest commit 2026-10-26 "Add isolated Roblox environments for parallel agents (#1)" (we copied 2026-10-24, so one change). Contains `roblox-setup` (installs the toolchain and registers MCP servers, so it runs installs: SKIP), `/roblox:*` commands, `.mcp.json`, bundled Blender MCP. Nothing on UI, mobile or performance. Verdict KEEP IN MIND (isolated environments for parallel agents might fit our multi-thread work).

### AshExplained/roblox-skills
- MIT, page: 18 stars, 6 commits, 40 skills (About says 34). Latest commit date and API read failed, UNVERIFIED. Content I read is short checklists (300 to 600 words), generic.
- `roblox-ui-implementation`: design gate (needs an approved brief), layout rules, Studio MCP tool order, a verify list. No numeric tap size. Says use `multi_edit` or `execute_luau` with no confirmation step. KEEP IN MIND for the brief gate idea only.
- `roblox-game-ux`: 10 to 30 second first-action goal, five-step first-session order, a design brief file with five states per screen. Generic; timings unsourced. KEEP IN MIND.
- `roblox-localization-accessibility`: about 300 words, no numbers, no mention of Roblox localization tables, colourblind or screen readers. SKIP.
- `roblox-performance-optimization`: no numeric budgets; relies on `rbx-scene-analysis` "when available". SKIP (official skill is better).
- `roblox-analytics-instrumentation`, `roblox-animation-audio-feedback`: generic. SKIP.

### JoCoding-Inc/roblox-skills
- MIT, 0 to 1 stars, 4 commits, pushed 2026-11-24. Four skills: `roblox-pitfalls`, `roblox-blender-export`, `roblox-store-art-pack`, `roblox-ui-genre-studs` (we copied the last). Nothing else on our goal. `roblox-pitfalls` may help with Open Cloud and Studio asset load errors. KEEP IN MIND.

### izzyfrm/roblox-ui-skill
- MIT, 0 stars, 14 commits, last commit 2026-10-04 "chore: add MIT license" (same as our copy). We took only anti-slop. Not taken:
  - `rules/responsive.md` (about 280 words): test tall and wide phones, narrow and wide desktop, tablet; Scale for structure, Offset for details; gamepad: Selectable, clear focus state, no hover-only. No pixel numbers, no safe area values. One sentence on tablet.
  - `rules/interaction-motion.md` (about 270 words): eight control states, small transitions 0.12 to 0.30 s, cancel old tweens, sparing Back, Elastic, Bounce, a "big moment" order (result, emphasis, VFX and SFX, details, next action). Sound.
  - `rules/debugging.md` (about 330 words): duplicate ScreenGuis, duplicate connections, DisplayOrder and ZIndex, stale tweens, hidden UI that still takes input, search scripts before renaming instances. Useful for our `ui-review`.
  - `rules/design.md`, `styles/presets.md`: not read. UNVERIFIED.
  - `bin/roblox-ui-skill.js` is an installer; do not copy.
- Verdict: ADOPT PART: the three rules above, as short additions to `ui-review`. Small files, no risky lines.

## 5. Other Roblox skill repos

- nonlooped/roblox-suite (https://github.com/nonlooped/roblox-suite): MIT, 36 stars, created 2026-06-16, pushed 2026-11-20. Skills with `references/` and `scripts/`, plus evals, SECURITY.md, PRIVACY.md, REVIEW_POLICY.md. Names deprecated patterns it targets (`Humanoid:LoadAnimation`, BodyMovers, bare `SetAsync`). Has `roblox-user-interfaces` (containers, responsive layouts, particles in UI), `roblox-animation`, `roblox-vfx`. Install is `npx skills add nonlooped/roblox-suite`, which we should not run. I did not read any skill body, so quality is UNVERIFIED. Its site says nothing about mobile or device support. KEEP IN MIND: a good second opinion on deprecations.
- brockmartin/roblox-game-skill: 431 stars, 217 per another read, last push 2026-03-04, 30,677 lines in 31 files. GitHub API says licence is null and I saw no LICENSE file. We cannot copy it into a public repo. Has `gui-systems.md` and a performance audit workflow. SKIP.
- JustineDevs/roblox-ai-os ("RCS"): 16 stars, pushed 2026-05-12, licence null. SKIP.
- Registry pages seen but not read: skills.sh and claudeskills.info entries for vasilyu1983/ai-agents-public gamedev-roblox, gamedev-skills/awesome-gamedev-agent-skills roblox-luau, greedychipmunk/agent-skills, kursku/skills luau-roblox, dig1t/skills luau-best-practices, christopher-buss/skills roblox-ts, flatbedj/roblox-skills, dnouri/roblox-pi-template. Licence, upkeep and safety UNVERIFIED for all. Note: roblox-ts is TypeScript, not our language.
- Rojo, Wally community: I found no skill pack from them. UNVERIFIED that none exists.
- anthropics/skills: Apache 2.0 for document skills and "many" others; I could not see the folder list, so whether a frontend-design or accessibility skill exists is UNVERIFIED. Our session already lists `design:accessibility-review` and `design:design-critique` skills, which transfer to Roblox UI (contrast, touch size, focus order).

## 6. Things that look wrong or risky across all repos

- Several skills tell agents to run `execute_luau` or `multi_edit` with no confirmation line (AshExplained ones, EL4CTEO studio-mcp). Our CLAUDE.md rule 2 and the Roblox MCP docs already cover this; keep our review step.
- Dated claims in EL4CTEO `roblox-ui` (Sep and Nov 2026 ClipsDescendants changes) and the roblox-brain "last_reviewed" fields should be checked against `latest-features.json` before copying.
- Persuasion or retention skills (`roblox-player-psychology`) conflict with our rule 10 for a young audience.
- Numbers in skills (44 px touch target, 45 FPS, 33 ms) have no Roblox source. Roblox's own adaptive-design and console pages give no numbers.

## 7. Suggested next steps (for the owner to decide)

1. Add `rbx-device-simulator-lua`, `rbx-perf-profiling`, `rbx-scene-analysis` to our UI review and mobile playtest skills as required steps.
2. Add Roblox llms.txt, `deprecated.md` and `latest-features.json` as the first lookup in our Roblox skills.
3. Diff and refresh MSayib from v2.19.0 to v2.23.0 (skill and references only).
4. Add izzyfrm `responsive`, `interaction-motion`, `debugging` and EL4CTEO `roblox-ui`, `roblox-input` after checking dated claims.
5. Add roblox-brain `roblox-lighting`, `roblox-camera`, `roblox-input` if lighting and camera tasks start.
