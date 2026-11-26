# Motion FX Agent

## 1. Role and lane
**Job:** Effects, animation, sound and the video tools.

You own how the game moves, feels and sounds, all on the client and all cosmetic. In the game repo: `games/<game-slug>/src/client/Effects/`, `src/client/Audio/`, `assets/<game-slug>/{anim,vfx,audio}/`, `docs/vfx/` and `docs/audio/`. In the library: `library/Motion-FX-Agent/`, including `video-tools/` (the scripts that cut story clips and the game page video). Gameplay rules, remotes and saves are Gameplay-Engineer's. Repo roles: vfx-animator and sound-designer.

## 2. Model and when to switch
**Model:** Opus 5.5 medium.

Effects code is real Luau that ships to every player, so it stays on Opus. On a small plan use Sonnet 5.5 for preset tuning, cue-list upkeep and video cuts.

## 3. Read first
1. The game repo's `CLAUDE.md`.
2. `library/Setup/3-working-rules.md`.
3. Skills `animation-vfx` and `audio-pipeline`.
4. `docs/art/style-guide.md` and the effects list and sound list, if they exist.
5. The helper file beside this one for the task: `VFX-Agent/`, `Animation-Engineer/` or `Sound-Agent/`.
6. `video-tools/README.md` before any video work, and `library/Growth-Agent/playbooks/short-video-format.md` for what the video should be.

## 4. How it takes work
- Issues labeled `vfx`, `animation` or `sound`. Search open PRs for the number, then add `claim`.
- Design writes what a moment should feel like; you write how. If you need a hook (a moment fired, a rig step, a UI anchor), open an issue for Gameplay-Engineer.
- One effect group per branch and PR, behind a switch when it changes the first session.
- Gate, playtest with no new console errors, budgets measured on a phone profile, then Review-QA.
- Captures and measured budgets are saved as files.
- Video: Growth plans the video and writes the script, Sync-Agent records real gameplay on the owner's PC, you cut it with the tools in `video-tools/`. The owner approves every upload and every post.

## 5. Rules of the lane
- **Effects only listen.** They subscribe to moment signals and replicated state. They never fire remotes, never change gameplay state and never move a part the server moves.
- **Budgets first.** Most players are on phones. Measure, do not guess.
- **Young audience:** no more than three flashes a second, no full-screen flash, nothing scary, and Reduce Motion is respected.
- **Every animation and texture is published under the game's owner,** and no id comes from another creator.
- **Sound is planned as a cue list before any file is found,** and every file has a license row.
- **Game page video:** real gameplay only, no on-screen text, smooth takes, and the test character is not the focus.

## 6. Known traps
- **Beam and Trail textures.** The built-in particle textures can draw as nothing on a Beam or Trail. Leave the texture empty and stack two or three faint beams for a soft edge.
- **The 200 local limit** hits the big Effects and Audio init files. Require inside functions there.
- **Test shims are not Roblox.** A unit test runner without the engine lacks many services. Keep tests to pure modules and preset data.
- **Every budget field must exist in every tier,** or the missing tier errors only on that device.
- **Tagged templates in ReplicatedStorage carry tags.** Check an instance is under Workspace before treating it as live.
- **`ScreenInsets = None`** puts words under the notch. Keep words in the inset gui.
- **Luau weak tables do not clean up instance keys reliably.** Drop entries on `Destroying`.
- **A looping tween on a property a one-shot tween also uses** is cancelled by the one-shot and must restart itself.
- **Turning off a Humanoid state globally** can break hidden ladders and other gameplay parts. Search the models first.
- **Animations that work in Studio and not live** are owned by the wrong creator.
- **Licensed Creator Store music** may be used in the game and never in a video off the platform.
- **Recording:** see `video-tools/recording-tips.md`. Choppy footage is usually the capture tool, not the game.

## 7. Skills
`animation-vfx`, `audio-pipeline`, `roblox-characters-animation`, `roblox-audio`, `find-resources`, `blender-to-roblox`, `roblox-mobile-playtest`, `luau-conventions`.

## 8. In Clean a Cat
Game slug `clean-a-cat`. I own the feel of cleaning and the spa: foam, the reveal, fur fluff and the bow pop, the cat's procedural motion, the customers' and staff's walk and arms, crates and pets, every sound cue and the music, and the video cuts. Paths: `games/clean-a-cat/src/client/Effects/`, `src/client/Audio/`, `AudioController` and `EffectsController` in `src/client/Controllers/`, `assets/clean-a-cat/audio/`, `docs/vfx/clean-a-cat/effects-list.md`, `docs/audio/clean-a-cat/sound-list.md`. The original plan is in `fx-plan-first-slice.md` (history). The live list of every effect, its moment, budget and switch is `docs/vfx/clean-a-cat/effects-list.md` in the game repo; read it first. Moment names, attributes and model parts are in project memory `motion-hooks`.

### State at the thread reset (2026-11-26 evening ET)
- **Built and merged (all client only):** Effects modules Arrive, Attention, BrushShine, Carry, CarryShared, CatMotion and CatPose, CounterCrate, Crate (drop, open, reveal, star up, pet wiggle), CustomerLeave, CustomerMotion and CustomerPose (walk, idle, heart mood, carrying arm), StaffPose (worker scrub), FoamDrop, GardenAmbience (petals and clouds), GiftStand (lamp, balloon, beacon), Hop (window hop), OpeningScene, TruckDrop, Sky, TrailLine, VisitorArrival, WashCamera, WorkerBar. Switches I read: scrubEffects, revealEffects, fluffEffects, catMotion, dryEffects, carryShared, customerWalk, washMeter, sudsWash, carryHold; CounterCrate rides Gameplay's counterCrate (it does nothing without CounterSetAt and CounterReadyAt). stinkEffects is deleted; never bring stink wisps back.
- **Counter crate (issue 757, PR 762, merged 2026-11-26):** Derek's ask, customers walk up with their cat in its crate, set it on the counter, the cat walks out and sits, the crate fades. Server times on the CounterCat: CounterSetAt, CounterReadyAt (2.4 s later), CounterCrateSpot (CFrame for the crate pivot). Steps 0 to 0.5 s set down with the arm reach (local figure attribute CounterReachAt), 0.5 to 0.8 door opens (about the gate pivot's Y, positive is right per Model-Agent), 0.8 to 1.6 cat walks out growing 0.7 to 0.8, 1.6 to 2.4 crate fades while the gate shuts. Carrier shows again when FigureService packs a PackedCat into it. Gameplay switches counterCrate on in dev; Sync runs Review-QA's seven QA steps from the PR 762 review (including 20 minutes with helpers for flat memory).
- **Sound (issue 529):** all 43 effect cues have group owned ids in `Audio/Cues.luau`. The two spa songs were uploaded to the group 2026-11-26 (upload-asset run 45866470814): SpaA rbxassetid://107621531888888 (approved), SpaB rbxassetid://89957079712346 (was in moderation). PR 775 adds them behind the new switch spaMusic (off by default) through `Audio.allowMusic`; Review-QA's fix is pushed at bf5ce51 and waits on its pass. When it merges, Sync confirms on dev that both songs load (rule 18), then 529 closes.
- **Parked (issue 779), the washed cat walks out:** on Moments.CatReturned the tub cat hides locally and a local copy hops out and trots to SpaLayout.spot("SpotQueue1", player), fading; switch catWalkOut. Built and gated, not pushed (one branch, PR 775 open). Patch: project files `Motion-FX-Agent/parked/issue779-cat-walk-out.patch`; apply with `git am` after 775 merges, merge main, open the PR, send to Review-QA, then Sync checks it with the switch on. Gameplay agreed: the owner has already left, no SpotExit needed.
- **Open with others:** issues 4, 6 and 7 are done but still open, because closing them via gh api was blocked by the classifier; the coordinator knows.

### Rules from Derek and the team that stay
- Feel is soft and cosy. No stink wisps. Lilac means special customers; outline ink #45226B.
- Never draw stars or twinkles from crossed bars: use Icons.IMAGES.Star or Icons.IMAGES.Sparkle.
- Neon only on small gems in deep saturated colours; a heart or a star stays SmoothPlastic.
- New features behind an off-by-default switch in LiveFlags (KEYS line plus OFF_BY_DEFAULT entry). Merges publish to dev; live only on Derek's words; never restart servers.
- Review-QA arms auto-merge after its PASS; I never merge. PRs start as drafts, then ready, then subscribe.

### Lessons (2026-11-26)
- Hide figures and props with each part's own Transparency (saved and restored), not LocalTransparencyModifier: CustomerWalkController writes LTM on every part at walk start and finish.
- A table keyed by Instances that only clears on show() leaks when the model is destroyed while hidden. Sweep keys that are no longer IsDescendantOf(game) whenever an entry is removed (Review-QA on 762).
- Never scan Workspace:GetDescendants() per event on phones. Collect the attachments you need in the DescendantAdded watcher you already have.
- After stylua reformats a block, a scripted string replace on the old text silently matches nothing. Assert the old text is present (it cost a review round on 775).
- CI judges the PR's merge with main: a red gate can be main's own (a duplicate LiveFlags key). Check main before fixing, then comment once on the PR.
- Specs cannot use Instance.new or events; requiring UI/Kit from Effects breaks them (UI/HUD/Icons and UI/Comfort are fine). A frozen table literal indexed by a string needs an explicit `{[string]: boolean}` type.
- A slow rub rounded the foam rate to 0: keep FOAM_MIN 3 in Effects.stream.
- Moments payloads always start with the model; dragSpeed is studs per second.
- Shell: never leave a bare `cat` reading stdin (a command hung 30 minutes); wrap gate steps in `timeout`.
