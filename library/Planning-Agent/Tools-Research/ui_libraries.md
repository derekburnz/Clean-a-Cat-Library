# Roblox UI libraries and tools: research notes

Read on 2026-11-24. Method note: the GitHub API, commit pages and release feeds were blocked for this session (robots rules and a repo allow list). So most "last commit" dates and some release dates could not be read. Those are marked UNVERIFIED. Star counts and issue counts come from each repo front page on 2026-11-24. Licenses were read from the repo page or the LICENSE file unless stated.

## Summary table

| Name | License | Last release or commit date | Verdict |
|---|---|---|---|
| Fusion (dphfox/Fusion) | MIT | wally 0.3.0 latest on index; main branch is 0.4.x; dates UNVERIFIED | KEEP IN MIND |
| Vide (centau/vide) | MIT | v0.4.1 changelog 2026-07-11; 0.4.0 2026-01-17 | TRY ON ONE SCREEN |
| React Luau (jsdotlua/react-lua) | MIT | UNVERIFIED | KEEP IN MIND |
| Roblox/react-luau | MIT | read-only mirror; UNVERIFIED | SKIP (use jsdotlua fork if React) |
| Roact (Roblox/roact) | Apache-2.0 | archived 2023-12-13 | SKIP |
| Roblox StyleSheet (built in) | Roblox engine feature | Transitions full release 2026-07-27 | TRY ON ONE SCREEN |
| Foundation (Roblox's UI lib) | UNVERIFIED | Fusion port v0.7.0 on 2026-10-13 | KEEP IN MIND |
| FusionFoundation (TenebrisNoctua) | MIT | 0.7.0 2026-10-13 | SKIP |
| UI Labs (PepeElToro41/ui-labs) | GPL-3.0 (dev plugin only) | UNVERIFIED | TRY ON ONE SCREEN |
| Flipbook (flipbook-labs/flipbook) | UNVERIFIED (not shown) | v2.5.0 "April 10", year inferred 2026 | TRY ON ONE SCREEN |
| Hoarcekat (Kampfkarren) | not read (rate limit) | UNVERIFIED | SKIP (legacy) |
| spr (Fraktality/spr) | MIT | UNVERIFIED | ADOPT-candidate, see text |
| Flipper (Reselim/Flipper) | MIT | UNVERIFIED | SKIP (spr or ripple cover it) |
| ripple (littensy/ripple) | MIT | UNVERIFIED | KEEP IN MIND |
| Otter | not checked | not checked | UNVERIFIED |
| TopbarPlus (1ForeverHD) | MPL-2.0 (plus a credit request) | UNVERIFIED | SKIP for now |
| SimpleToasts (rvila94) | MIT | July 2026 post; 2 stars | KEEP IN MIND (too new) |
| UltimateList (Kampfkarren) | not stated | UNVERIFIED | SKIP (needs React) |
| virtualized-list-lua (jsdotlua) | not shown | UNVERIFIED | SKIP (needs React) |
| VirtualScroller (richmensch) | MIT (per forum post) | v1.0.0 2025-10-12 | KEEP IN MIND |
| lucide-roblox (latte-soft) | MIT (Lucide itself ISC) | ARCHIVED 2026-07-21 | SKIP |
| RbxUtil (Sleitnick: Trove, Signal) | MIT | UNVERIFIED | ADOPT Trove only if needed |
| Janitor (howmanysmall) | MIT | UNVERIFIED | KEEP IN MIND |
| Rex (Tiago Mouta) | n/a | ARCHIVED 2025-08-09 | SKIP |

## The direct question: framework before first screens?

Short answer: not required. If you want one later, the evidence leans to Vide, with Fusion as the safer-known choice. Do a one-screen trial first.

Evidence for moving now:
- Cheapest moment to switch. No screens exist to rewrite.
- Reactive state means a count-up, a coin total or a toast list updates by itself. In plain code, every screen needs hand-written refresh code and cleanup.
- Fusion and Vide are tiny pure-Luau packages (Fusion API listed on deepwiki; Vide manifest shows only src and LICENSE shipped). Both are MIT.
- Previewing tools (UI Labs, Flipbook) have first-class renderers for them.
- Roblox's own Foundation library is React, so the engine team's direction is React-like, and the Fusion port exists.

Evidence against:
- You have a custom UI gate in CI that builds every screen at four sizes in a fake Roblox. A framework adds a layer your fake Roblox must support. UNVERIFIED whether Fusion or Vide run on your fake Roblox. Needs a test.
- Fusion on the Wally index is still 0.3.0 (index lists 0.3.0, 0.3.0-dev.1, 0.2.0, 0.1.1-beta, 0.0.1-beta, read 2026-11-24). The 0.4 line exists on GitHub main (wally.toml says 0.4.0-dev1; deepwiki says 0.4.0) but is not on Wally. That is a version risk.
- Vide has no GitHub release entries and its wally package name is not shown on the repo page. UNVERIFIED how you install it. The manifest (v0.4.1) is for wally.
- No measured low-end phone numbers found for any framework. The only benchmark repo found (jsdotlua/react-performance-benchmarks) lists benchmarks but publishes no results. So "no lag" cannot be promised either way.
- Frameworks are a long-term promise. The author of Rex archived his own framework in Aug 2025 saying reactive list rendering needs heavy testing and a framework needs a reason to exist (mouta.me, read 2026-11-24). He still recommends Fusion for production and Vide as modern.
- Roblox now ships native styling (StyleSheet, tokens, themes, hover and pressed transitions). That covers theme and hover feel without any package. See below.
- Your rules (strict, Rojo, public repo, tiny team) favour few dependencies.

Practical call: keep plain Luau for the first screens. Use Roblox StyleSheet for theme and hover feel on one screen. Trial Vide or Fusion on one list-heavy screen (shop or collection) with UI Labs. Decide after the UI gate passes on it.

## Roblox StyleSheet (built in)
- URL: https://create.roblox.com/docs/ui/styling (read 2026-11-24).
- What: StyleSheet holds rules, tokens (named values like CSS variables) and themes (swappable token sets). StyleRule applies properties by selector (class, tag, name, state like Hover, @query for screen conditions). StyleLink attaches a sheet to a ScreenGui. Only one sheet per tree. Can be built in Luau.
- Transitions: https://devforum.roblox.com/t/full-release-styling-transitions/4646870. Beta 2026-05-21, full release 2026-07-27. Run natively, "generally faster than manual Luau tweening", problems possible with hundreds at once. Only fire for style changes (tag or GuiState), not layout changes. Needs higher rule priority.
- Fit: no dependency, no license issue, works with plain Instance code. Cannot be tested in your fake Roblox unless your fake models these classes (UNVERIFIED, likely not).
- Cost: another place for theme to live next to your Theme module.
- Verdict: TRY ON ONE SCREEN. Docs page did not state platform or performance limits, so check on a real phone.

## Fusion
- https://github.com/dphfox/Fusion. Reactive UI library by dphfox. License MIT (repo page). 810 stars, 62 issues, not archived (page, 2026-11-24).
- Releases page shows v0.3 (30 Aug, year not shown), v0.2 (31 Jan), v0.1 (20 Aug). Wally: elttob/fusion, latest 0.3.0. Also npm @dphfox/fusion.
- Strict types: deepwiki says exported Luau types and frozen API. Whether it passes your strict luau-lsp: UNVERIFIED.
- Features: Value, Computed, ForValues, Spring, Tween, scopes for cleanup (deepwiki).
- Risk: 0.3 to 0.4 had API breaks (v0.3 replaced :get() with functions). Wally lags main.
- Verdict: KEEP IN MIND (safe known name, but version split).

## Vide
- https://github.com/centau/vide. "A reactive Luau library for creating UI", inspired by Solid. MIT. 320 stars, 6 issues. Changelog: 0.4.1 2026-07-11, 0.4.0 2026-01-17, 0.3.1 2024-10-09 (raw CHANGELOG.md). Active in 2026.
- Fully Luau typecheckable (README). Manifest: wally, shared realm. Package name UNVERIFIED (not read).
- Fit: small, closest to plain Instance code (Storyteller says Vide stories can be a function returning an Instance).
- Cost: smaller community than Fusion; no performance claims in README.
- Verdict: TRY ON ONE SCREEN.

## React Luau
- Community: https://github.com/jsdotlua/react-lua. MIT, 570 stars, 16 issues. Translation of React 17.x. Fork of the Roblox one, meant as the community version. No release listed. UNVERIFIED last commit.
- Roblox: https://github.com/Roblox/react-luau. MIT, 584 stars, read-only mirror, Wally roblox/react, also Creator Store (page, 2026-11-24).
- Big: most virtual list helpers need it. Heaviest to learn and ship. Engine team uses it for Foundation.
- Verdict: KEEP IN MIND; only if you want Foundation or UltimateList.

## Roact
- https://github.com/Roblox/roact. Apache-2.0. Archived 2023-12-13, "deprecated and no longer maintained". SKIP.

## Foundation and FusionFoundation
- Foundation is Roblox's own UI library used in the client, Studio and website (forum post 2026-06-27). License not found. UNVERIFIED.
- Port: https://github.com/TenebrisNoctua/FusionFoundation. MIT, 6 stars. 0.7.0 on 2026-10-13. Docs "will come eventually". Too small a community. SKIP; but its component list (Popover, Dropdown, Toggle, Slider, Loading) is a useful checklist.

## UI Labs
- https://github.com/PepeElToro41/ui-labs. Storybook-like plugin. License GPL-3.0 (repo page). 198 stars, 22 issues. Last release or commit UNVERIFIED.
- Works with plain Instance UI: "generic stories" use a `render(props)` function that builds into props.target and returns a cleanup function (docs, ui-labs.luau.page, 2026-11-24). Also React, Roact, Fusion, Vide, Iris.
- License note: it is a Studio plugin, not shipped in your game or repo. Stories you write for it are your own code. A story file does not need to copy UI Labs code. Confirm with the owner before adding it as a repo dependency. Studio only; cannot run in CI.
- Verdict: TRY ON ONE SCREEN.

## Flipbook
- https://github.com/flipbook-labs/flipbook. Storybook plugin; stars, license and issues were not shown on the page read, so UNVERIFIED. Releases page: v2.5.0 "April 10", v2.4.0 "December 21", v2.3.0 "October 9"; years inferred (2026, 2025, 2025). Active.
- Storyteller renderers (flipbook-labs.github.io/storyteller): React, Roact, Fusion, Iris, Vide, and "Manual" (function takes props and returns an Instance). So plain Instance UI works.
- Verdict: TRY ON ONE SCREEN (pick one of UI Labs or Flipbook).

## Hoarcekat
- https://github.com/Kampfkarren/hoarcekat. Page fetch was rate limited, nothing read. Storyteller lists "Hoarcekat (Legacy)". SKIP, UNVERIFIED.

## Motion: spr, Flipper, ripple
- spr https://github.com/Fraktality/spr. MIT, 146 stars, 1 issue, "Small and fast motion library". Spring-based, single module. No release listing. UNVERIFIED last commit.
- Flipper https://github.com/Reselim/Flipper. MIT, 144 stars, 1 issue, has wally.toml. Skip, older.
- ripple https://github.com/littensy/ripple. MIT, 128 stars, 3 issues, Wally littensy/ripple. Verdict KEEP IN MIND.
- Note: Roblox Styling Transitions and TweenService cover simple hover and pop. Springs help for bouncy panels and drag. Verdict for spr: TRY ON ONE SCREEN (single file, MIT, no framework).
- Otter, count-up, confetti, shine: not checked, UNVERIFIED. Nothing solid found.

## TopbarPlus
- https://github.com/1ForeverHD/TopbarPlus. License file reads Mozilla Public License 2.0, plus a "credit" section asking to keep attribution or credit it in the game description. 236 stars, 29 issues. No releases. UNVERIFIED last commit.
- Fit: builds topbar icons. Your UI gate treats the Roblox top bar as a no-go zone, so you may not need it. SKIP for now.
- MPL-2.0 is on your allowed list. Credit request needs an owner decision.

## SimpleToasts
- https://github.com/rvila94/SimpleToasts. MIT, 2 stars. Zero dependency, plain Instances. Wally r94vi/simpletoasts (README). Posted 2026-07-22. Stacked toasts, 5 severities, 6 positions, server to client bridge.
- Too new and tiny. Read the code for ideas, or build your own on your Theme. KEEP IN MIND.

## Lists
- UltimateList (kampfkarren.github.io/ultimate-list): virtualized lists and grids, built on React. License not stated. SKIP.
- virtualized-list-lua (jsdotlua): FlatList for react-lua. SKIP.
- VirtualScroller (forum post 2025-10-12): MIT, v1.0.0, no dependencies, claims huge lists. Docs link reported 404 in June 2026; no repo link in the post. KEEP IN MIND; probably write your own recycling list for plain Luau.

## Icons
- lucide-roblox (latte-soft): MIT, Lucide is ISC, 31 stars, ARCHIVED 2026-07-21. Maps names to Roblox asset ids, so it relies on uploads by someone else (your rule 18 about group-owned uploads makes that a risk). SKIP.
- Upload Lucide yourself under your group (ISC licence, free). Not verified in this pass. Material, Phosphor ports: not checked.

## Input glyphs
- Found only: ControllerIconMapping and Control Hints forum posts, an Xbox icon pack post. Pages returned empty or unread. UNVERIFIED. InputGlyphs (eviltwo) is Unity only. Nothing adoptable confirmed.

## Cleanup helpers
- Trove (in Sleitnick/RbxUtil): https://github.com/Sleitnick/RbxUtil, MIT, 480 stars, 23 issues, 31 modules including Trove and Signal.
- Janitor: https://github.com/howmanysmall/Janitor, MIT, 151 stars, 191 commits.
- Maid (Nevermore): not read, UNVERIFIED.
- Short note: pick one, Trove has a smaller wally footprint if you already use RbxUtil. You have your own Signal.

## Other
- afrxo/roblox-agent-skills (roblox-ui skill): a skill file, recommends Fusion 0.3, UI Labs, 44 px targets. Licence not stated. You already have similar skills, so SKIP.
- Rex: archived 2025-08-09 by its author. SKIP.
- Search hits like "WindUI" and "Fyy-Luau-Vault" are exploit-script interface hubs, not game dev libraries. Ignore.

## Could not verify
- Latest commit date for almost every repo (blocked pages).
- Low end phone performance of any framework (no measured data found).
- Whether Fusion or Vide run on your fake Roblox in CI.
- Licence of Flipbook, Foundation, UltimateList, virtualized-list-lua.
