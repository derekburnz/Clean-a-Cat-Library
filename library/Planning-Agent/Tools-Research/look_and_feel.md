# Look and feel research: tools, packs and libraries for a Roblox cat spa game

Read on 2026-11-24. Research only. Nothing was cloned or run.

Method notes (read this first):
- GitHub API and the GitHub tool were blocked for repos outside our own, and GitHub atom and commit-history pages are blocked by robots rules. So many "last commit" dates are UNVERIFIED. Where a date comes from a mirror site (relatedrepos, awesome.ecosyste.ms, crates.io) I say so.
- Licences were read from the repo page or the project's own page, not from memory. I could not open raw LICENSE files (blocked), so the "MIT license" label on the repo page is the source.
- Some DevForum threads redirect to a maintenance page, so a few items rest on search snippets only. Marked UNVERIFIED.
- Dates with no year in the source are marked "year inferred".

## Summary table

| Name | Licence | Last release or commit | Verdict |
|---|---|---|---|
| Asphalt (jackTabsCode) | MIT | v2.0.2, 07 Jul 2026 (year inferred) | ADOPT |
| Tarmac (Roblox/tarmac) | MIT | mirror shows update 23 Jul 2025; nothing newer seen | SKIP |
| Tungsten (pwnwrkz) | GPL-3.0 | UNVERIFIED | SKIP (licence) |
| Rojo | not read (MIT, UNVERIFIED) | v7.7.1, 02 Oct (year inferred 2026) | KEEP IN MIND (already in use) |
| Open Cloud Assets API | Roblox terms | docs read 2026-11-24 | ADOPT (via Asphalt) |
| Codify plugin (cxmeel/codify-plugin) | none stated | repo archived 25 Apr 2026; plugin is paid | SKIP |
| Figma Importer Assistant | not stated | UNVERIFIED | KEEP IN MIND |
| RoImport (Figma to Roblox) | plugin not stated; bridge open source | v1.3 21 Jul 2026, update 19 Sep 2026 | KEEP IN MIND |
| Roblox UI Styling (StyleSheet) | built in to engine | docs read 2026-11-24 | ADOPT |
| react-luau (Roblox) | MIT | read-only mirror, date UNVERIFIED | SKIP |
| Fusion (dphfox) | MIT | UNVERIFIED | KEEP IN MIND |
| Vide (centau) | MIT | UNVERIFIED | KEEP IN MIND |
| Sculpt (ImAvafe) | none stated | UNVERIFIED, 1 star | SKIP |
| rbxts-react-clean-ui | not stated | v1.3.0, 14 Sep 2026 | SKIP (TypeScript, modern look) |
| UIKit (dig1t) | Apache-2.0 | archived 7 Mar 2024 | SKIP |
| Kenney UI Pack | CC0 | version 2.0, date not shown | TRY |
| Kenney Interface Sounds | CC0 | v1.0, 11/02/2020 | TRY |
| game-icons.net | CC BY 3.0 | not applicable | KEEP IN MIND (credit needed, style mismatch) |
| Lucide | ISC | lucide-roblox wrapper archived 21 Jul 2026 | KEEP IN MIND (use SVG, not wrapper) |
| lucide-roblox (latte-soft) | MIT | archived 21 Jul 2026 | SKIP |
| Phosphor icons | MIT | UNVERIFIED | TRY |
| Tabler icons | MIT | UNVERIFIED | KEEP IN MIND |
| OpenMoji | graphics CC BY-SA 4.0 | UNVERIFIED | SKIP (share-alike) |
| Twemoji (jdecked) | graphics CC-BY 4.0, code MIT | v17.0.3 mentioned, date UNVERIFIED | KEEP IN MIND (credit) |
| Roblox built-in fonts (FredokaOne, Nunito) | Roblox platform fonts | Enum page read 2026-11-24 | ADOPT |
| Sleitnick RbxUtil (Shake, Spring, Signal, Trove, Timer) | MIT | UNVERIFIED | ADOPT (Shake, Spring) |
| EZ Camera Shake (RbxCameraShaker) | MIT | last push 6 Jul 2023 (mirror) | SKIP (use Shake) |
| GG Camera Shake | port licence not stated; Unity original MIT | v1.1.3, 12 Jul 2026 | KEEP IN MIND |
| Fraktality spr | MIT | mirror: 31 Jul 2024 | TRY |
| Flipper (Reselim) | MIT | UNVERIFIED | KEEP IN MIND |
| UIEmitter | not stated, closed source, sold | v2-ab 6 Jun 2025 | SKIP |
| Roblox HapticService / HapticEffect | built in | docs read 2026-11-24 | ADOPT |
| Quenty NevermoreEngine | MIT | UNVERIFIED | KEEP IN MIND |
| Roblox Lighting (LightingStyle Soft) | built in | docs read 2026-11-24 | ADOPT |
| Roblox accessibility properties | built in | docs read 2026-11-24 | ADOPT |
| Roblox creator templates | not stated | page read 2026-11-24 | KEEP IN MIND |

## 1. Asset pipeline

### Asphalt
- URL: https://github.com/jackTabsCode/asphalt (read 2026-11-24). "An assets-as-files tool for Roblox".
- Licence: MIT (repo page and crates.io, 2026-11-24).
- Upkeep: releases page shows v2.0.2 (07 Jul), v2.0.1 (01 Jun), v2.0.0 (30 Apr); no year shown, but crates.io lists 2.0.1 updated 2026-06-01, so these are 2026. 169 stars. 40,422 crate downloads. Maintainer jackTabsCode. Not archived.
- Features read from the README (raw.githubusercontent, 2026-11-24): config in `asphalt.toml`; can target a user or a group (creator `type` = `"group"`); generates Luau or TypeScript code, `flat` style indexes assets like paths; images, audio (mp3, ogg, wav, flac), models and animations (.rbxm, .rbxmx); converts SVG to PNG and alpha bleeds images; writes `asphalt.lock.toml` to commit; a dry run exits non-zero if hashes changed (usable in CI).
- Gaps: README says nothing on 2x or high DPI images and nothing on sprite packing (UNVERIFIED beyond the README). Says 3D formats (fbx, gltf) should use the 3D Importer, not the web API.
- Fit: very good. Group uploads match our rule. Codegen gives typed id tables instead of hand-typed ids. Lockfile makes uploads repeatable and reviewable in a public repo. Key needs `asset:read` and `asset:write`.
- Risk: API key must stay in env or GitHub secret. Per CLAUDE.md rule 18, check each upload loads in the live game.
- Verdict: ADOPT. It is the maintained successor to Tarmac and does group upload plus codegen.

### Tarmac
- URL: https://github.com/Roblox/tarmac (read 2026-11-24). MIT. 140 stars. README says only that the repo moved from rojo-rbx to the Roblox org. A mirror (relatedrepos.com) shows Roblox/tarmac updated 23 Jul 2025 and the old rojo-rbx copy 5 Mar 2024. I could not read a release list. README fetch failed, so features are UNVERIFIED.
- Verdict: SKIP. Nothing newer than mid-2025 seen, and Asphalt covers the same job with group support and a lockfile. Tarmac was the one that packed sprite sheets; that is its one advantage (UNVERIFIED this session).

### Tungsten
- URL: https://github.com/pwnwrkz/tungsten and https://pwnwrkz.github.io/tungsten/getting-started/introduction/ (2026-11-24). Created during LucideRoblox work. Docs say it has "spritesheet packing that Asphalt lacks", group or user targets, Luau codegen, Open Cloud sync, watch mode. 17 stars, no releases listed, labelled "Active".
- Licence: GPL-3.0 (repo page). A GPL tool run as a build step does not make our game GPL, but it is copyleft and adds friction in a public repo. Small, young, one-person project.
- Verdict: SKIP for now. Worth a look only if sprite packing becomes needed. Revisit if the licence changes.

### Rojo asset handling
- URL: https://github.com/rojo-rbx/rojo/releases (read 2026-11-24): latest v7.7.1 (02 Oct, year inferred 2026), v7.7.0 (02 Jul). Licence UNVERIFIED this session (widely known as MIT; not confirmed).
- Rojo syncs files into instances. It does not upload images to Roblox. Asphalt's README says to sync model files with Rojo. UNVERIFIED how Rojo treats .png in 7.7.
- Verdict: KEEP IN MIND, already used.

### Open Cloud Assets API
- URL: https://create.roblox.com/docs/cloud/guides/usage-assets.md (2026-11-24).
- Facts: one asset per call, up to 20 MB. Images .png .jpeg .bmp .tga, under 8000x8000. Audio mp3 ogg wav flac, up to 7 minutes, 100 uploads a month if ID-verified (10 if not). Models fbx gltf glb rbxm rbxmx. To upload as a group, put the group ID in `creationContext.creator`; the account needs group permission. Images, audio, meshes and videos cannot be updated in place; only fbx content can. Fonts are not listed as an upload type.
- Cost: the audio cap of 100 a month matters if sounds are uploaded in many small files.
- Verdict: ADOPT, through Asphalt.

## 2. Design to Roblox

### Roblox UI Styling (StyleSheet, StyleRule, tokens, themes)
- URL: https://create.roblox.com/docs/ui/styling.md (2026-11-24). A DevForum post "UI Styling is officially released" exists (title seen in search; page itself redirected, so release date UNVERIFIED).
- What: CSS-like. StyleSheet holds rules, tokens and themes. A StyleRule with a tag selector such as `.ButtonPrimary` styles every tagged button. Tokens work like CSS variables. Themes swap token sets. StyleLink attaches a sheet to a ScreenGui.
- Licence: part of the engine.
- Fit: fits code-built UI. One style sheet could hold the cream window, ink outline, three-colour button tokens. Cuts repeated property code and gives one place to change a colour.
- Risk: newer system; check Studio version and mobile behaviour in a smoke test.
- Verdict: ADOPT (try on one screen first).

### Codify
- Repo https://github.com/cxmeel/codify-plugin (2026-11-24): no licence stated, 10 stars, "archived by the owner on Apr 25, 2026". It is the decoupled conversion module of the paid Codify plugin (sold on Roblox and Itch.io). Outputs Luau (`Instance.new`), Fusion, React, roblox-ts JSX. The csqrl URL in the brief failed to load; search shows forks (zeroglzk, cxmeel).
- Verdict: SKIP. Archived, no licence, and the plugin is paid. We already build UI in code.

### Figma to Roblox plugins
- Figma Importer Assistant: https://miagobble.github.io/Figma-Import-Assistant/posts/gettingstarted (2026-11-24). Studio plugin plus Figma plugin. Licence and price not stated; Patreon at 1 dollar a month exists. 9-slice and fonts not covered.
- RoImport: https://devforum.roblox.com/t/free-figma-to-roblox-plugin-roimport/4731967 (2026-11-24). Free. Only the bridge app is confirmed open source. Launched 11 Jul 2026, v1.3 21 Jul 2026 with 9-slice settings, last major update 19 Sep 2026. Layer-name tags, `_2x` `_3x` `_x4` size tags. Auto-upload needs a Creator Hub API key and a local bridge. Group upload not mentioned.
- Others seen in search only (UNVERIFIED): UILint v2, GuiForge, Framewisp, Figblox, MonkeyPTR, Bloxporter (PAID), UI Designer Pro.
- Fit: we make mockups in HTML, not Figma, and build UI in code. These would add a second source of truth. Closed-source plugins in the loop are a risk for a public repo.
- Verdict: KEEP IN MIND. Do not adopt unless the designer moves to Figma.

### HTML or SVG to Roblox UI converters
- Nothing mature found. I did not find a maintained open source HTML-to-Roblox converter. UNVERIFIED that none exists.

### Open source UI kits and design systems
- react-luau (Roblox): https://github.com/Roblox/react-luau. MIT, 584 stars, "read-only mirror" (2026-11-24). Adds a React runtime. Heavy for our needs. SKIP.
- Fusion: https://github.com/dphfox/Fusion. MIT, 810 stars, 933 commits. Release date UNVERIFIED. Reactive UI library. KEEP IN MIND if code-built UI grows.
- Vide: https://github.com/centau/vide. MIT, 320 stars. Date UNVERIFIED. Similar. KEEP IN MIND.
- Sculpt: https://github.com/ImAvafe/sculpt. Styling and theming toolkit, 1 star, no licence stated. SKIP.
- rbxts-react-clean-ui: https://github.com/Shadercloud/rbxts-react-clean-ui, from DevForum post (2026-11-24): roblox-ts, v1.3.0 on 14 Sep 2026, licence not stated, modern light and dark themes. Not our style or language. SKIP.
- dig1t/UIKit: Apache-2.0, 1 star, archived 7 Mar 2024. SKIP.
- General UI Kit (itch.io, rblx-essentials), Vault UI System (BuiltByBit): paid or tag-based Studio kits seen in search. UNVERIFIED licences. SKIP for a public repo.
- I did not find an open source Roblox kit in a chunky cartoon style with a clear licence. The best path is our own kit on UI Styling.
- Other helpers listed by Loominagit/useful-roblox-resources (https://github.com/Loominagit/useful-roblox-resources, 2026-11-24): UIStrokeAdjuster (scales UIStroke), LayoutUtil, Iris (immediate-mode, for tools). Each licence UNVERIFIED.

## 3. Icon and UI art packs

### Kenney UI Pack
- https://kenney.nl/assets/ui-pack (2026-11-24). CC0. 430 files, version 2.0 "completely remade". Tags button, panel, slider, interface. Date not shown.
- Fit: Kenney art is flat and clean, close to our flat pastel look, and CC0 means no credit. Needs recolour to our palette. The page did not list 9-slice, so check the pack. Upload under the group via Asphalt.
- Verdict: TRY as base shapes.

### Kenney Game Icons
- https://kenney.nl/assets/game-icons: licence not stated on the page I read (UNVERIFIED). Kenney assets are normally CC0 but confirm on the download page before use.

### Kenney Interface Sounds
- https://kenney.nl/assets/interface-sounds (2026-11-24). CC0, 100 files, v1.0 dated 11/02/2020. Clicks and buttons. Note our sounds are synthesized, so this is a reference or fallback set. Audio upload cap is 100 a month.
- Verdict: TRY.

### game-icons.net
- https://game-icons.net/about.html (2026-11-24): CC BY 3.0, credit author. Example credit line given by the site. Black and white fantasy style; mismatch with a cute pastel look and each icon needs the right author credited. Verdict: KEEP IN MIND.

### Lucide
- Lucide is ISC (stated on lucide-roblox page, 2026-11-24). Clean outline icons. Roblox wrapper latte-soft/lucide-roblox: MIT, 31 stars, archived 21 Jul 2026. Do not depend on the wrapper. Use the SVGs through Asphalt (it converts SVG to PNG). Thin outline style may clash with chunky UI. KEEP IN MIND.

### Phosphor
- https://github.com/phosphor-icons/core. MIT, 399 stars (core repo), date UNVERIFIED. Has weights including a fill and duotone style that fit chunky UI better than thin lines. Verdict: TRY.

### Tabler
- https://github.com/tabler/tabler-icons. MIT, 21.6k stars. Release date UNVERIFIED. Outline style. KEEP IN MIND.

### Material Symbols
- Not read this session. UNVERIFIED (Google states Apache-2.0, not confirmed here). Skip unless needed.

### OpenMoji
- https://github.com/hfg-gmuend/openmoji (2026-11-24). Graphics CC BY-SA 4.0, code LGPL-3.0. 4.5k stars. Share-alike on art. Verdict: SKIP per our rule.

### Twemoji
- https://github.com/jdecked/twemoji (2026-11-24). Code MIT, graphics CC-BY 4.0 (credit needed). Mentions v17.0 and a v17.0.3 CDN example. Maintainer not named. Cute flat emoji (cat, fish, sparkle) usable in UI with a credit line. Verdict: KEEP IN MIND.

Note: Roblox itself can show emoji in TextLabels as text, which costs no upload. UNVERIFIED how emoji render on every device.

## 4. Fonts

- Source: https://create.roblox.com/docs/reference/engine/enums/Font (2026-11-24). The Enum.Font list includes FredokaOne and Nunito (plus BuilderSans, Gotham, Bangers, LuckiestGuy, PatrickHand, Cartoon and others).
- So both mockup fonts exist in Roblox with no upload. Use `Font.fromEnum(Enum.Font.FredokaOne)` or `Font.fromName`. Source: Font datatype page (https://create.roblox.com/docs/reference/engine/datatypes/Font, 2026-11-24) lists `fromName`, `fromId`, `fromEnum` but does not list valid names. Which names `fromName` accepts is UNVERIFIED.
- Enum.Font entries have no weight or style options (the page says `fromEnum` takes no weight or style). Nunito from the enum is one weight only. Check Nunito Bold look in Studio.
- Creator Store fonts: a 2023 DevForum post (https://devforum.roblox.com/t/fonts-in-creator-marketplace-81-new-fonts/2164977, read 2026-11-24) says 81 fonts were added and the goal was the whole Google Fonts catalog, and its list has "Nunito Sans", not Nunito, and no Fredoka. Custom font upload was asked about with no Roblox reply there. A Dec 2025 DevForum request (https://devforum.roblox.com/t/bring-the-full-google-fonts-catalog-to-roblox/4128957) says no expansion had been announced as of 24 Dec 2025. The Open Cloud guide does not list font upload either. So custom font upload in 2026: not confirmed. UNVERIFIED for 2026 beyond Dec 2025.
- Licence position of catalog fonts in a game: not stated on any page I read. UNVERIFIED. Google Fredoka and Nunito are SIL OFL (not opened this session; the Fredoka page on fonts.google.com appeared in search but I did not read it).
- Verdict: ADOPT built-in FredokaOne and Nunito. Do not plan custom fonts.

## 5. Feel and juice libraries

### Sleitnick RbxUtil
- https://github.com/Sleitnick/RbxUtil (2026-11-24). MIT. 480 stars, 546 commits. 31 modules incl. Shake, Spring, Signal, Trove, Timer, TaskQueue, Input, Streamable. No Tween module. Last commit date UNVERIFIED.
- Fit: Wally or Rojo friendly, typed, small. Shake gives camera or UI shake; Spring gives squash and stretch.
- Verdict: ADOPT Shake and Spring (check the repo is still maintained before pinning).

### EZ Camera Shake (RbxCameraShaker)
- https://github.com/Sleitnick/RbxCameraShaker. MIT, 123 stars, 9 commits. Mirror shows last push 6 Jul 2023. SKIP; Shake in RbxUtil is the newer tool by the same author (assumed, UNVERIFIED).

### GG Camera Shake
- Post: https://devforum.roblox.com/t/gg-camera-shake-screenshake-that-doesnt-suck/4731267 (2026-11-24). Kick, Perlin and Bounce algorithms, 2D and 3D presets, accessibility strength multiplier, typed. Posted 11 Jul 2026, v1.1.3 on 12 Jul 2026, on Wally 14 Jul 2026. Port licence not stated; Unity original MIT. Young, one author. KEEP IN MIND.

### spr and Flipper (springs)
- spr: https://github.com/Fraktality/spr. MIT, 146 stars, 84 commits. A mirror shows a 31 Jul 2024 update. Small and fast. TRY for button press and pop-in.
- Flipper: https://github.com/Reselim/Flipper. MIT, 144 stars, 106 commits. Date UNVERIFIED. KEEP IN MIND.
- Roblox TweenService may already be enough for most pops. Do not add a library until a tween looks wrong.

### UI particles and confetti
- UIEmitter (DevForum, 2026-11-24): sold on Creator Store, no licence, no public source (author says git suspended), v2-ab 6 Jun 2025. SKIP. A small module of our own using ImageLabels and a Heartbeat loop with a cap on particle count is easy and safe.

### Haptics
- HapticService: https://create.roblox.com/docs/reference/engine/classes/HapticService.md (2026-11-24). Client only. `IsVibrationSupported`, `SetMotor`, `IsMotorSupported`. Output scaled by the player's haptic setting. The page says HapticEffect supersedes it for new work (check HapticEffect doc before coding; not read). MasVibrate on DevForum is marked deprecated. Verdict: ADOPT the built-in.

### Sound managers
- Several seen in search (UNVERIFIED licences and dates): Open Source Audio Manager, SoundController, EasySFX, SoundProvider, AudioEngine, Magic Audio Manager. None read. Our audio-pipeline skill exists; a 50 line pooled play function is likely enough. KEEP IN MIND.

### Quenty NevermoreEngine
- https://github.com/Quenty/NevermoreEngine. MIT, 609 stars, 5,887 commits (2026-11-24). Many packages (Blend, ButtonHighlightModel, ColorPalette, Spring, AccelTween). Big and its own loader. Take ideas, not the whole thing. KEEP IN MIND.

### Highlights, viewport frames, dialog
- Highlight is a built-in instance (our animation-vfx skill covers it).
- ViewportFrame cost: DevForum thread May 2022 (https://devforum.roblox.com/t/viewportframe-performance-issues-for-displaying-items/1798310, 2026-11-24): resizing or changing visibility triggers a re-bake; more than one animated ViewportFrame is not advised; fixes were show fewer, avoid animating size, cache, or pre-render images. Old thread, still the clearest source. Other threads about low-end devices seen in search, not read. For showing a cat in a menu: use one ViewportFrame at a fixed size, or a pre-rendered image.
- No dialog or speech bubble module was read. UNVERIFIED.

## 6. Lighting and post-processing

- Source: https://create.roblox.com/docs/reference/engine/classes/Lighting.md (2026-11-24). `Lighting.LightingStyle` has `Soft` (stylised) and `Realistic`. `PrioritizeLightingQuality` (bool) decides what scales down first, lighting quality or view distance. `Technology` (incl. ShadowMap, Future) is deprecated and superseded by those two. `ShadowSoftness` applies only on devices that can render shadow maps.
- Technology enum page (https://create.roblox.com/docs/reference/engine/enums/Technology.md): Voxel is a 4x4x4 voxel map; Compatibility is deprecated; no cost numbers given. For a Voxel-like look: use Voxel with a ColorGradingEffect set to the Retro preset (the page says this for imitating the old system).
- Performance guide (https://create.roblox.com/docs/performance-optimization/design.md, 2026-11-24): pick a baseline device; example budget under 1,000 draw calls and 1,000,000 triangles; low-end devices can crash from out-of-memory; Studio emulator does not show memory use; avoid reading `SavedQualityLevel` to change effects; built-in materials use less memory than custom textures; use only 0 or 1 transparency where possible since partial transparency causes overdraw; instance streaming helps memory and frame rate. The page does not cover post-effects or UI.
- Which post effects are safe on phones: not stated in any official page I read. UNVERIFIED. Practical advice: keep to ColorCorrection and a light Bloom, test each on the baseline phone.
- Open source lighting preset collections: none found. UNVERIFIED.
- Our no-texture Part art is cheap on memory, which suits this guide.
- Verdict: ADOPT Soft lighting style, test PrioritizeLightingQuality on a low-end phone.

## 7. Study references

- Roblox templates page (https://create.roblox.com/docs/resources/templates.md, 2026-11-24): lists uncopylocked games (Platformer, UGC Homestore, Obby, Move It Simulator and others). Page gives no licence and no mention of open source. Use for study only; do not copy assets. KEEP IN MIND.
- Roblox GitHub org (https://github.com/Roblox, 2026-11-24): 110 repos; I saw react-luau, rodux, gear, signals (MIT, updated 10 Sep 2026). No open sample game with polished UI seen on the first page. UNVERIFIED for the other 100.
- No open source polished cartoon game with a clear licence was found.

## 8. Accessibility

- Source: https://create.roblox.com/docs/production/publishing/accessibility.md (2026-11-24).
- `GuiService.PreferredTextSize` (Medium default; Large, Larger, Largest). `UITextSizeConstraint` limits are respected, `TextScaled` text is not affected, `AutomaticSize` and `TextWrapped` adapt.
- `GuiService.ReducedMotionEnabled`: set TweenInfo time to 0 or fade a CanvasGroup's `GroupTransparency` instead of moving.
- `GuiService.PreferredTransparency`: 1 default, 0 fully opaque; multiply each BackgroundTransparency.
- Pair colours with symbols (over 5% of people have colour blindness), do not signal by sound only, give separate volume controls for sfx, music and speech.
- The page gives no touch target size. The adaptive design page (https://create.roblox.com/docs/production/publishing/adaptive-design.md) also gives no numbers for touch targets or safe zones; it asks for focusable gamepad controls and legible text on a small phone and a far-away TV. The cross-platform guide may hold numbers (not read). UNVERIFIED.
- GG Camera Shake has a strength multiplier for reduced motion (DevForum post).
- Helper modules for these settings: none found. A 30 line module is enough.
- Contrast and colour-blind checkers for HTML mockups: I did not research specific tools, so none are named here. UNVERIFIED.
- Verdict: ADOPT all properties above. Add a settings check to the ui-review skill.

## Surprises
1. lucide-roblox was archived 21 Jul 2026 and Codify's open module was archived 25 Apr 2026.
2. FredokaOne and Nunito are already in Enum.Font; no upload needed.
3. UI Styling (StyleSheet and tokens) is now a built-in, CSS-like system that matches a themed button kit.
4. Lighting.Technology is deprecated; use LightingStyle plus PrioritizeLightingQuality.
5. Fonts are not an Open Cloud upload type in the guide.

## Could not verify
Last commit dates for RbxUtil, Fusion, Vide, Flipper, Phosphor, Tabler, Tungsten; Kenney Game Icons licence; Rojo licence; tarmac features; HapticEffect details; touch target numbers; post effect cost on phones; any HTML-to-Roblox converter; sound manager licences.
