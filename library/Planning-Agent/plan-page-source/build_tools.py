#!/usr/bin/env python3
"""Builds Derek's tool picks page and its Markdown copy from one list.
Run: python3 build_tools.py clean-a-cat-tool-picks.html tools-and-skills-deep-dive.md
Answers save in the page database, collection `picks`, doc id `s-<id>` with {pick, note}. pick is the option index, 0 is our pick."""
import html, json, sys

OUT_HTML, OUT_MD = sys.argv[1], sys.argv[2]
PAGE_LINK = "PAGE_LINK"

ADD = ["Yes, add it", "Not now", "No"]
TRY = ["Yes, try it", "Not now", "No"]

GROUPS = [
 dict(key="add", title="Add now", chip="Add now",
      lead="Five things that cost little and help every screen from the first one. None of them adds code to the game.",
      items=[
  dict(id="rbxskills", t="Use Roblox's own Studio skills for device checks and speed checks", opts=ADD, who="Sync-Agent and Review-QA-Agent",
   what="Roblox now ships its own skills inside Studio. Three matter here. One flips Studio's device preview through phone, tablet, console and PC and takes a picture of the UI at each. One reads Roblox's frame timing tool to find what makes a frame slow. One checks draw cost, memory and leaks in the place.",
   why="It is the closest we get to seeing the real game on every device. Our test gate checks sizes in a stand-in for Roblox. This checks the real thing in Studio.",
   lic="Part of Roblox Studio. Nothing to copy.",
   keep="Kept by Roblox. Their page was last updated on November 20, 2026.",
   cost="No install. One of our skills already says to use the device check when it is there. The change is to make it a must before any screen is signed off and to add the other two. Sync-Agent first confirms that the three show up in your Studio. That is not checked yet.",
   src="Roblox's skills page and Studio MCP page, read today. The three names are confirmed: rbx-device-simulator-lua, rbx-perf-profiling and rbx-scene-analysis."),
  dict(id="devskill", t="Update our main Roblox skill from 2.19.0 to 2.23.0", opts=ADD, who="the thread that owns the skills folder",
   what="roblox-dev-skill by MSayib is the skill every thread reads before it writes Roblox code. Our copy is from October 22. Four releases came out since then. The newest is from November 23.",
   why="The new version knows Roblox engine 0.748 and sends threads to Roblox's Studio skills by itself. Stale facts are how threads end up using retired APIs. In the same change we add Roblox's own list of retired APIs and its latest features file as the first place to look.",
   lic="MIT. License file read.",
   keep="Very active. One author, 36 stars.",
   cost="Someone reads the difference before it is copied. We take the skill and its reference files only and never its install scripts.",
   src="Change log and license read from the repo today."),
  dict(id="uirules", t="Add five small UI and input guides to our skills", opts=ADD, who="Design-Agent and Review-QA-Agent",
   what="Three short rule files from izzyfrm/roblox-ui-skill (screen sizes, button states and motion, UI bugs) go into our ui-review checklist. Two skills from EL4CTEO/roblox-skills (roblox-ui and roblox-input) are added whole.",
   why="They fill thin spots in what we have: controller focus, the eight states of a button, motion times of 0.12 to 0.30 seconds, the order of a big moment (result, emphasis, effects, details, next step), safe areas and bugs like a hidden window that still takes taps.",
   lic="MIT for both. License files read.",
   keep="Both are small one person repos. Their last changes were in September and October 2026.",
   cost="roblox-ui states two dated Roblox changes that we could not confirm. Whoever copies it checks them against Roblox's docs first. Our helpers read these files as summaries, so the full text gets a read before it goes in.",
   src="Helper summaries of the files plus license files read today."),
  dict(id="settings", t="Build Roblox's comfort and device settings into every screen", opts=ADD, who="Design-Agent and Gameplay-Engineer",
   what="Roblox has built-in settings a game can read: the player's text size choice, less see-through backgrounds, reduced motion, the kind of input in use, safe areas around notches and the top bar, controller button pictures and vibration.",
   why="This is most of what makes a game feel right on each device and it needs no library. Roblox's console guide asks that a TV player sitting 8 to 10 feet away can read everything and reach every button with four directions, select and back.",
   lic="Built into Roblox.",
   keep="Kept by Roblox. The old vibration service is retired. HapticEffect replaces it.",
   cost="It becomes lines in our ui-review checklist and, where it can be measured, in the test gate. Our effects code already honors reduced motion. Text size and see-through are not handled yet.",
   src="Roblox's accessibility, console and GuiService pages, read today. Our code searched."),
  dict(id="baseline", t="Pick one low end phone as the test device and make Roblox's speed rules our budget", opts=ADD, who="Review-QA-Agent",
   what="Roblox's own advice is to choose one weak device and test on it all the time, because Studio cannot show real phone memory. Roblox gives few numbers: 16.67 ms per frame for 60 frames a second, an example budget of under 1,000 draw calls, most images at 512 by 512 or smaller and a closer look once more than 2 to 3 percent of sessions crash. It gives no memory limit for phones.",
   why="Five causes cover most phone lag and crashes in a game like ours. Memory that grows through a session. Large or too many images. See-through layers and heavy particles. Scripts that run every frame and are never disconnected. Leftovers from players who left. A named phone and a short budget catch these early.",
   lic="Roblox's public docs. Nothing to copy.",
   keep="Kept by Roblox.",
   cost="None. It joins the open job on your plan page to name your test devices. Review-QA-Agent turns the numbers into a checklist.",
   src="Roblox's performance pages (design, identify, improve, memory), read today."),
 ]),
 dict(key="try", title="Try on one screen", chip="Try once",
      lead="Five small trials for when the first real screens are built. Each one is tried on a single screen and dropped if it adds nothing.",
      items=[
  dict(id="spr", t="spr, a one file spring library for bouncy UI", opts=TRY, who="Motion-FX-Agent",
   what="One call makes a window or button move like a spring: a pop in with a little bounce or a squash when pressed.",
   why="Springs are what make chunky cartoon UI feel alive and they stay smooth when a move is cut short. Roblox's built-in tweens do not handle that well.",
   lic="MIT. License file read.",
   keep="146 stars and 1 open issue. The last change we could see was in July 2024, so treat it as finished and not active. We would keep our own copy of the one file, as we do with ProfileStore. The backup is Spring from RbxUtil, which is MIT and was updated in August 2026.",
   cost="It must honor reduced motion and it has to run in our test gate's stand-in for Roblox. Try it on the recap card. If it adds nothing over tweens we drop it.",
   src="License file read today. Stars and dates from the repo page and a mirror."),
  dict(id="trove", t="Trove, a cleanup helper that stops memory leaks", opts=TRY, who="Gameplay-Engineer",
   what="A screen adds everything it makes to a Trove: connections, windows, running animations. One call cleans it all when the screen closes.",
   why="Memory that grows through a session is the top cause of phone crashes. One cleanup habit in every screen prevents most of it.",
   lic="MIT. License file read. It is part of Sleitnick's RbxUtil.",
   keep="About 475 stars, updated in August 2026. On Wally as sleitnick/trove 1.8.0.",
   cost="It would be the first outside package in the game code after ProfileStore. We either set up Wally packages or keep a copy of the one file.",
   src="License and package list read from the repo today."),
  dict(id="flipbook", t="Flipbook, a Studio plugin that shows one screen at a time", opts=TRY, who="Sync-Agent and Design-Agent",
   what="A storybook for Roblox. It shows a single screen or pop-up alone in Studio, in each of its states, without playing the game.",
   why="You and Design-Agent can flip through every window on the PC in seconds and compare it with the mockup.",
   lic="MIT wording in its license file. The other tool of this kind, UI Labs, is GPL-3.0, so Flipbook is our pick.",
   keep="Active. Version 2.5.0 came out in April 2026. The year is our reading of the releases page.",
   cost="A plugin install in Studio on your PC and a small story file per screen. It does not run in the test gate. Our HTML mockups and the gate already cover a lot, so this is low on the list.",
   src="License file read today. Release list read by a helper."),
  dict(id="asphalt", t="Asphalt, a tool that uploads images and sounds and writes their ids", opts=TRY, who="the thread that owns CI",
   what="Images and sounds stay as files in the repo. Asphalt uploads them under the group, writes a Luau file with every id and keeps a lock file so nothing is uploaded twice. It also turns SVG icons into PNG and fixes dark edges on see-through images.",
   why="Icons and UI art will soon arrive in batches. Ids typed by hand are a common cause of blank images and uploads under the wrong owner do not load in a group game.",
   lic="MIT. License file read.",
   keep="Version 2.0.2 from July 2026, 170 stars, one main author.",
   cost="It overlaps our own upload workflow, so we compare the two on the first batch of icons and keep one. It can use the group key that is already a GitHub secret, so no new key. Its guide says nothing about sprite sheets.",
   src="License and version read from the repo today. Features from its guide, read by a helper."),
  dict(id="icons", t="Icon and UI shape sources with clean licenses", opts=TRY, who="Design-Agent",
   what="Phosphor icons come in filled and two tone styles that suit chunky UI. Kenney's UI Pack has 430 files of plain buttons and panels to recolor. Lucide is a thin line set.",
   why="Drawn icons take time. These are free for commercial use with no credit line and can be recolored to our pastel set.",
   lic="Phosphor is MIT and Lucide is ISC, both license files read. Kenney's pack is CC0 by its own page.",
   keep="All three are widely used. The Roblox wrapper for Lucide was archived in July 2026 and leans on someone else's uploads. We skip the wrapper and upload our own copies under the group.",
   cost="Your Roblox-Asset-Library is checked first. Design-Agent takes an icon from these only where it fits the style.",
   src="License files read today. Kenney's page read by a helper."),
 ]),
 dict(key="later", title="Not now", chip="Later",
      lead="Four things that look tempting and that I would hold. The first two are the big ones.",
      items=[
  dict(id="framework", t="No UI framework for now", opts=["Agree, no framework now", "Trial Vide on one screen now", "Something else"], who="Gameplay-Engineer if it is trialled",
   what="Fusion, Vide and React Luau are libraries that redraw the UI by themselves when the data changes.",
   why="They save refresh code on screens with long lists. But our test gate builds every screen in a stand-in for Roblox and a framework would have to run there first. Nobody has published phone speed numbers for any of them. Fusion's package on Wally is stuck at 0.3.0 while its main branch is at 0.4.0. React is the heaviest to learn and to ship.",
   lic="All three are MIT. License files read.",
   keep="Vide is at 0.4.1 from July 2026 with changes in October. Fusion last changed in February 2026. React Luau is active.",
   cost="If a list screen such as the Cat Index gets painful in plain code we trial Vide on that one screen.",
   src="License and package files read today. Dates from GitHub, read by a helper."),
  dict(id="stylesheet", t="Roblox's built-in style sheets: not yet", opts=["Agree, not yet", "Try it on one screen now", "Something else"], who="Design-Agent if it is trialled",
   what="Roblox now has a system like CSS. One sheet holds colors, fonts and button looks, with hover and press changes that animate. The animated part was fully released on July 27, 2026.",
   why="It would give one place for our cream windows and three color buttons. Two of our four research helpers said to adopt it. I say wait. Our test gate's stand-in for Roblox does not know style sheets. The gate could no longer see the fonts and sizes a sheet sets and would pass screens it has not really checked.",
   lic="Built into Roblox.",
   keep="Kept by Roblox.",
   cost="We look again when the stand-in learns style sheets or when tests run in real Roblox.",
   src="Roblox's styling page and release post, read today. Our test tool searched for style sheet support and none was found."),
  dict(id="luauexec", t="Run tests inside real Roblox from GitHub", opts=["Agree, later", "Set it up now", "Something else"], who="the thread that owns CI",
   what="Roblox's Open Cloud can run Luau in the real engine from a GitHub workflow. A task runs up to 5 minutes and 10 can run at a time.",
   why="It would catch what the stand-in cannot, such as style sheets or engine changes. It cannot measure phone frame rate.",
   lic="A Roblox service.",
   keep="Marked stable in Roblox's docs.",
   cost="The key we have may need one more permission, which is your step. It is worth it the first time a bug slips past the stand-in.",
   src="Roblox's Luau Execution page, read by a helper today."),
  dict(id="moreskills", t="More skills for when that work starts", opts=["Agree, later", "Add lighting and camera now", "Something else"], who="the thread whose work it is",
   what="From TabooHarmony/roblox-brain: lighting, camera and localization. From EL4CTEO: performance. nonlooped/roblox-suite as a second opinion on retired APIs. The Chrrxs Studio MCP server for tests with several players.",
   why="None is needed for the first screens. Lighting and camera help once the spa room is dressed.",
   lic="All MIT. License files read.",
   keep="roblox-suite changed on November 20, 2026 and the Chrrxs server on November 2, 2026. The others last changed in September and October 2026.",
   cost="Each has small flaws our helpers noted, such as targets with no source. Each gets a full read when its turn comes.",
   src="Helper summaries plus license files read today."),
 ]),
]

FACTS = [
 ("Fonts", "FredokaOne and Nunito are both built into Roblox, so nothing needs an upload. Uploading a custom font is not confirmed to be possible. Nunito comes in one weight only. The starter HUD still uses Gotham in two places."),
 ("Lighting", "Roblox's Soft lighting style fits a flat pastel look. The older Technology setting is retired. Roblox gives no cost numbers for screen effects on phones, so we keep to color correction and a light bloom and test on the phone."),
 ("A 3D cat inside a menu", "The window type that shows 3D inside UI is costly on phones when it moves or resizes. Use one at a fixed size or a picture made ahead of time."),
 ("Tap sizes", "Roblox gives no numbers for tap size or safe areas. Our 44 pixel rule is our own and matches the common phone app standard."),
 ("What nobody offers", "We found no open source library worth taking for confetti, counting numbers, tutorial arrows or toasts and no open source cartoon UI kit with a clear license. We build small ones of our own on our theme. For a long list such as the Cat Index we write our own list that reuses its rows."),
 ("Controller button pictures", "Roblox has its own way to show the right button picture for the player's controller. No library is needed."),
]

SKIP = [
 ("React Luau, Roact", "UI frameworks", "MIT, Apache-2.0", "React is heavy for our needs. Roact was archived in December 2023."),
 ("UI Labs", "Studio screen preview plugin", "GPL-3.0", "Flipbook does the same job under MIT."),
 ("TopbarPlus", "Buttons in Roblox's top bar", "MPL-2.0 plus a credit rule", "We keep out of the top bar. Using it means crediting it in the game description."),
 ("lucide-roblox", "Roblox wrapper for Lucide icons", "MIT", "Archived in July 2026 and leans on someone else's uploads."),
 ("Zap, Blink, ByteNet", "Libraries that shrink network traffic", "MIT (ByteNet by its readme)", "Not needed with 6 players per server."),
 ("CullThrottle", "Pauses effects the camera cannot see", "MPL-2.0", "Built for thousands of moving objects. A spa plot has few."),
 ("ObjectCache, PartCache", "Part reuse pools", "MIT, none stated", "A 20 line pool of our own is safer. PartCache has no license."),
 ("Lune, Jest Roblox", "Test runners outside Studio", "MPL-2.0, MIT", "Our CI already has its own runner."),
 ("run-in-roblox, Tarmac", "Older build tools", "MIT", "Both are stale. run-in-roblox last changed in 2020."),
 ("Tungsten", "Asset tool with sprite sheets", "GPL-3.0", "Copyleft license and 17 stars."),
 ("darklua, Mantle", "Code and settings tools", "MIT", "We have no need for them."),
 ("Sentry for Lua", "Crash reports to an outside service", "MIT", "A hack week project that sends data off Roblox. Not for a young audience. Roblox's own dashboard shows crash rate."),
 ("Benchmarker", "Speed test plugin", "Paid, no license shown", "Not open source."),
 ("Figma importers, Codify", "Design to Roblox tools", "Mostly closed or none", "We design in HTML and build in code. Codify was archived with no license."),
 ("brockmartin/roblox-game-skill, JustineDevs/roblox-ai-os", "Skill packs", "No license", "We cannot copy unlicensed files into a public repo."),
 ("roblox-brain player psychology skill", "Retention tactics", "MIT", "Pity crates, countdown timers and streaks. It breaks our young audience rules."),
 ("AshExplained, 35 other checklists", "Short skill checklists", "MIT", "Generic. We already took the five useful ones."),
 ("Other Studio MCP servers", "Ways for Claude to drive Studio", "MIT", "Roblox's old one and the best known community one are archived. The built-in server covers the job."),
 ("UltimateList, virtualized-list", "Long list helpers", "MPL-2.0, not shown", "Both need React."),
 ("OpenMoji, game-icons.net", "Icon art", "CC BY-SA, CC BY", "Share-alike art is a no. game-icons needs a credit per icon and is not our style."),
 ("UIEmitter", "2D UI particles", "Closed, sold", "Not open source."),
 ("EZ Camera Shake", "Camera shake", "MIT", "Last changed in 2023. Our effects use no camera shake by default."),
 ("NevermoreEngine", "Very large module collection", "MIT", "Too big to take on. Good for ideas only."),
 ("SimpleToasts", "Toast pop-ups", "MIT", "2 stars and four months old. We build toasts on our theme."),
]

NCARDS = sum(len(g["items"]) for g in GROUPS)
NSKIP = len(SKIP)

LIMITS = [
 "License files were read directly from the repo for 34 projects. Where a license came from a project's page and not its file, the card says so.",
 "This thread cannot open GitHub's commit pages for other people's repos. Last change dates come from research helpers and a few come from mirror sites. Treat them as close, not exact.",
 "Nobody has published phone speed numbers for any UI library. Any claim that one is fast on a weak phone is untested.",
 "Helpers read skill files as summaries. Anything we copy gets a full read first.",
]

def esc(s): return html.escape(s, quote=True)

# ----------------------------------------------------------------- HTML
def card(it, chip, n):
    doc = "s-" + it["id"]
    rows = [("What it is", it["what"]), ("Why", it["why"]), ("License", it["lic"]), ("Upkeep", it["keep"]), ("Cost and risk", it["cost"]), ("How it was checked", it["src"]), ("Who would do it", it["who"][0].upper() + it["who"][1:] + ".")]
    dl = "".join(f"<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>" for k, v in rows)
    opts = "".join(
        f'<label class="opt{" ours" if i == 0 else ""}"><input type="radio" name="{doc}" id="{doc}-{i}" value="{i}" data-doc="{doc}" data-key="pick"><span>{esc(o)}{"<em>our pick</em>" if i == 0 else ""}</span></label>'
        for i, o in enumerate(it["opts"]))
    return f'''<article class="card" id="{doc}">
  <header><span class="num">{n}</span><h3>{esc(it["t"])}</h3><span class="chip chip-{chip[1]}">{esc(chip[0])}</span></header>
  <dl>{dl}</dl>
  <div class="choose"><div class="opts" role="radiogroup" aria-label="Your pick">{opts}</div>
  <label class="note"><span class="sr">Note</span><input type="text" id="{doc}-note" data-doc="{doc}" data-key="note" placeholder="Note, if you want to add one"></label></div>
</article>'''

sections, n = [], 0
for g in GROUPS:
    cards = []
    for it in g["items"]:
        n += 1
        cards.append(card(it, (g["chip"], g["key"]), n))
    sections.append(f'''<section id="{g["key"]}">
  <header><h2>{esc(g["title"])}</h2><p>{esc(g["lead"])}</p></header>
  {"".join(cards)}
</section>''')

facts_html = "".join(f"<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>" for k, v in FACTS)
skip_html = "".join(f"<tr><th scope=\"row\">{esc(a)}</th><td>{esc(b)}</td><td>{esc(c)}</td><td>{esc(d)}</td></tr>" for a, b, c, d in SKIP)
limits_html = "".join(f"<li>{esc(x)}</li>" for x in LIMITS)

DATA = dict(items=[dict(id="s-" + it["id"], t=it["t"], opts=it["opts"]) for g in GROUPS for it in g["items"]])

PAGE = r'''<title>Clean a Cat Tool Picks</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600&family=Nunito+Sans:opsz,wght@6..12,400;6..12,600;6..12,700&display=swap">
<style>
/* Layout: one reading column, same spa palette as the launch plan. Each find is a spec card: a fact list on the left rail of labels, the pick buttons at the foot. Mint is add, sky is try, mud is later. */
:root{
  --bg:#FFF6EC; --surface:#FFFFFF; --ink:#3A2C20; --soft:#7A6656; --line:#EBDCCB;
  --mint:#23805F; --mint-bg:#DDF5EA; --gum:#C8436E; --gum-bg:#FFE3EC; --sky:#1F6FA8; --sky-bg:#E2F2FE; --mud:#5A4632; --mud-bg:#F1E4D4;
  --display:"Fredoka","Trebuchet MS",system-ui,sans-serif; --body:"Nunito Sans","Segoe UI",system-ui,sans-serif;
}
@media (prefers-color-scheme: dark){ :root:not([data-theme="light"]){
  --bg:#211912; --surface:#2C2219; --ink:#FBEFE2; --soft:#C4AF9C; --line:#46372A;
  --mint:#7FDDB8; --mint-bg:#1F3B30; --gum:#FF9DBA; --gum-bg:#4A2330; --sky:#8FD3FE; --sky-bg:#1C3447; --mud:#C9A988; --mud-bg:#3A2D21; color-scheme:dark } }
:root[data-theme="dark"]{
  --bg:#211912; --surface:#2C2219; --ink:#FBEFE2; --soft:#C4AF9C; --line:#46372A;
  --mint:#7FDDB8; --mint-bg:#1F3B30; --gum:#FF9DBA; --gum-bg:#4A2330; --sky:#8FD3FE; --sky-bg:#1C3447; --mud:#C9A988; --mud-bg:#3A2D21; color-scheme:dark }
*{box-sizing:border-box}
body{background:var(--bg);color:var(--ink);font-family:var(--body);font-size:16px;line-height:1.55}
.wrap{max-width:820px;margin:0 auto;padding-block:28px 72px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:flex;flex-direction:column;gap:36px}
h1,h2,h3{font-family:var(--display);font-weight:600;text-wrap:balance;margin:0;line-height:1.2}
h1{font-size:clamp(1.9rem,6vw,2.6rem)}
h2{font-size:1.5rem}
h3{font-size:1.1rem}
p{margin:0}
a{color:var(--sky);text-underline-offset:2px}
a:focus-visible,input:focus-visible,button:focus-visible,textarea:focus-visible{outline:3px solid var(--sky);outline-offset:2px}
.eyebrow{font-size:.78rem;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--gum)}
.intro{display:flex;flex-direction:column;gap:12px}
.lede{font-size:1.08rem;max-width:62ch}
.soft{color:var(--soft);max-width:65ch}
.tally{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin:6px 0 0;padding:0;list-style:none}
.tally a{display:flex;flex-direction:column;gap:2px;padding:12px 14px;border-radius:14px;text-decoration:none;color:var(--ink);border:1px solid var(--line);background:var(--surface)}
.tally b{font-family:var(--display);font-size:1.6rem;line-height:1;font-variant-numeric:tabular-nums}
.tally span{font-size:.88rem;color:var(--soft)}
.tally .t-add b{color:var(--mint)} .tally .t-try b{color:var(--sky)} .tally .t-later b{color:var(--mud)} .tally .t-skip b{color:var(--soft)}

.bar{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--bg);border-bottom:1px solid var(--line);margin-inline:-4px;padding:10px 4px;display:flex;flex-wrap:wrap;gap:8px 10px;align-items:center}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:10;background:var(--bg)}
.pill{display:inline-flex;gap:6px;align-items:baseline;padding:5px 12px;border-radius:999px;background:var(--surface);border:1px solid var(--line);font-size:.86rem;font-variant-numeric:tabular-nums}
.pill b{font-family:var(--display);font-weight:600}
.pill.full{background:var(--mint-bg);border-color:var(--mint)}
.btn{font:inherit;font-weight:700;font-size:.88rem;color:var(--ink);background:var(--surface);border:1px solid var(--mud);border-radius:999px;padding:6px 14px;cursor:pointer}
.btn:hover{background:var(--mud-bg)}
.status{margin-left:auto;font-size:.8rem;color:var(--soft)}
.status.warn{color:var(--gum)}

section{display:flex;flex-direction:column;gap:16px;scroll-margin-top:90px}
section>header{display:flex;flex-direction:column;gap:6px}
section>header p{color:var(--soft);max-width:65ch}

.card{background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:18px;display:flex;flex-direction:column;gap:14px;scroll-margin-top:90px}
.card>header{display:flex;gap:12px;align-items:flex-start;flex-wrap:wrap}
.card h3{flex:1;min-width:12rem}
.num{flex:none;display:grid;place-items:center;width:30px;height:30px;border-radius:50%;background:var(--mud);color:var(--bg);font-family:var(--display);font-weight:600;font-size:.95rem;font-variant-numeric:tabular-nums}
.chip{flex:none;font-size:.74rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;padding:4px 10px;border-radius:999px}
.chip-add{background:var(--mint-bg);color:var(--mint)}
.chip-try{background:var(--sky-bg);color:var(--sky)}
.chip-later{background:var(--mud-bg);color:var(--mud)}
dl{margin:0;display:flex;flex-direction:column}
dl>div{display:grid;grid-template-columns:9.5rem minmax(0,1fr);gap:4px 14px;padding:8px 0;border-top:1px dashed var(--line)}
dt{font-size:.8rem;font-weight:700;color:var(--soft);padding-top:2px}
dd{margin:0;font-size:.95rem}
@media (max-width:560px){ dl>div{grid-template-columns:1fr} }
.choose{display:flex;flex-direction:column;gap:10px;padding-top:12px;border-top:2px solid var(--line)}
.opts{display:flex;flex-wrap:wrap;gap:8px}
.opt{position:relative;cursor:pointer}
.opt input{position:absolute;opacity:0;inset:0;width:100%;height:100%;cursor:pointer;margin:0}
.opt span{display:inline-flex;gap:8px;align-items:baseline;padding:9px 14px;min-height:44px;border-radius:12px;border:1px solid var(--line);background:var(--bg);font-weight:600;font-size:.93rem}
.opt em{font-style:normal;font-size:.7rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--gum)}
.opt.ours span{border-color:var(--gum)}
.opt input:checked+span{background:var(--mint-bg);border-color:var(--mint);box-shadow:inset 0 0 0 1px var(--mint)}
.opt input:focus-visible+span{outline:3px solid var(--sky);outline-offset:2px}
input[type=text],textarea{font:inherit;color:var(--ink);background:var(--bg);border:1px solid var(--line);border-radius:10px;padding:9px 11px;width:100%;min-width:0}
textarea{resize:vertical}
.note{display:block}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%)}

.facts{background:var(--sky-bg);border-radius:14px;padding:6px 18px}
.facts>div:first-child{border-top:0}
.scroll{overflow-x:auto;border:1px solid var(--line);border-radius:14px;background:var(--surface)}
table{border-collapse:collapse;width:100%;min-width:640px;font-size:.9rem}
th,td{text-align:left;vertical-align:top;padding:9px 12px;border-bottom:1px solid var(--line)}
thead th{font-size:.76rem;letter-spacing:.06em;text-transform:uppercase;color:var(--soft)}
tbody th{font-weight:700}
tbody tr:last-child th,tbody tr:last-child td{border-bottom:0}
@media (max-width:560px){
  table{min-width:0} thead{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%)}
  tbody tr{display:flex;flex-direction:column;gap:2px;padding:12px 14px;border-bottom:1px solid var(--line)}
  tbody tr:last-child{border-bottom:0}
  tbody th,tbody td{display:block;padding:0;border:0}
  tbody td:nth-child(2),tbody td:nth-child(3){color:var(--soft);font-size:.84rem}
  tbody td:nth-child(3)::before{content:"License: "}
}
.limits{margin:0;padding-left:20px;display:flex;flex-direction:column;gap:6px;color:var(--soft);font-size:.93rem;max-width:68ch}
.send{display:flex;flex-direction:column;gap:10px;align-items:flex-start}
#copyout{min-height:160px}
</style>

<div class="wrap">
  <div class="intro">
    <span class="eyebrow">Deep dive, November 24, 2026</span>
    <h1>Tools and skills worth adding</h1>
    <p class="lede">Short answer: no outside library beats what we already have for UI. The best finds are free tools that Roblox itself now ships and a few small pieces to fold into our own skills.</p>
    <p class="soft">I recommend 5 additions now, 5 small trials once the first real screens are built and no UI framework yet. Another __NSKIP__ finds are on the skip list with the reason for each. Nothing is added to the repo until you pick. For each yes I open a task for the thread that owns it.</p>
    <ul class="tally">
      <li><a class="t-add" href="#add"><b>5</b><span>to add now</span></a></li>
      <li><a class="t-try" href="#try"><b>5</b><span>to try on one screen</span></a></li>
      <li><a class="t-later" href="#later"><b>4</b><span>to hold for later</span></a></li>
      <li><a class="t-skip" href="#skip"><b>__NSKIP__</b><span>looked at and skipped</span></a></li>
    </ul>
  </div>

  <div class="bar">
    <span class="pill" id="pill"><b id="n-done">0</b> of __NCARDS__ picked</span>
    <button class="btn" id="acceptall" type="button">Take all our picks</button>
    <span class="status" id="status" role="status">Loading your picks</span>
  </div>

  __SECTIONS__

  <section id="facts">
    <header><h2>Good to know</h2><p>Facts the research turned up that need no pick from you.</p></header>
    <dl class="facts">__FACTS__</dl>
  </section>

  <section id="skip">
    <header><h2>Looked at and skipped</h2><p>Each of these was checked and left out. If you want one of them anyway, name it in the box under the table.</p></header>
    <div class="scroll"><table>
      <thead><tr><th scope="col">Find</th><th scope="col">What it is</th><th scope="col">License</th><th scope="col">Why we skip it</th></tr></thead>
      <tbody>__SKIP__</tbody>
    </table></div>
    <label class="note"><span class="sr">Anything from the skip list you want</span><input type="text" id="s-skip-note" data-doc="s-skip" data-key="note" placeholder="Anything from this list you want anyway"></label>
  </section>

  <section id="limits">
    <header><h2>How sure this is</h2></header>
    <ul class="limits">__LIMITS__</ul>
  </section>

  <section id="send">
    <header><h2>Your picks</h2><p>Picks save by themselves as you tap. If the page says it could not save, use the button and paste the text in the project chat.</p></header>
    <div class="send">
      <button class="btn" id="copy" type="button">Copy my picks</button>
      <span class="soft" id="copied" role="status"></span>
      <textarea id="copyout" hidden readonly aria-label="Your picks as text"></textarea>
    </div>
  </section>
</div>

<script>
(function(){
  var DATA = __DATA__;
  var LS = "clean-a-cat-tool-picks-v1";
  var state = {}, dirty = {}, timers = {}, writing = {}, again = {};
  var db = null, online = false;
  var statusEl = document.getElementById("status");

  function setStatus(t, warn){ statusEl.textContent = t; statusEl.classList.toggle("warn", !!warn); }
  function controls(doc){ return document.querySelectorAll('[data-doc="' + doc + '"]'); }
  function has(v){ return v !== undefined && v !== null && v !== ""; }
  function applyDoc(doc){
    var d = state[doc] || {};
    controls(doc).forEach(function(el){
      var v = d[el.dataset.key];
      if (el === document.activeElement && dirty[doc]) return;
      if (el.type === "radio") el.checked = (has(v) && String(v) === el.value);
      else el.value = v == null ? "" : String(v);
    });
  }
  function counts(){
    var n = 0;
    DATA.items.forEach(function(x){ if (has((state[x.id] || {}).pick)) n++; });
    document.getElementById("n-done").textContent = n;
    document.getElementById("pill").classList.toggle("full", n === DATA.items.length);
  }
  function saveLocal(){ try { localStorage.setItem(LS, JSON.stringify(state)); } catch (e) {} }
  function loadLocal(){ try { var s = JSON.parse(localStorage.getItem(LS) || "{}"); if (s && typeof s === "object") state = s; } catch (e) {} }

  function flush(doc){
    if (!db) { dirty[doc] = false; return; }
    if (writing[doc]) { again[doc] = true; return; }
    writing[doc] = true;
    setStatus("Saving");
    var body = Object.assign({}, state[doc] || {}, { at: new Date().toISOString() });
    db.doc("picks/" + doc).set(body).then(function(){
      writing[doc] = false;
      if (again[doc]) { again[doc] = false; flush(doc); return; }
      dirty[doc] = false;
      setStatus("All picks saved");
    }, function(){
      writing[doc] = false; again[doc] = false;
      setStatus("Could not save online. Use Copy my picks below.", true);
    });
  }
  function changed(doc, delay){
    dirty[doc] = true; saveLocal(); counts();
    clearTimeout(timers[doc]);
    timers[doc] = setTimeout(function(){ flush(doc); }, delay);
  }
  function onInput(ev){
    var el = ev.target; if (!el.dataset || !el.dataset.doc) return;
    if (el.type === "radio" && !el.checked) return;
    var doc = el.dataset.doc;
    state[doc] = Object.assign({}, state[doc] || {});
    state[doc][el.dataset.key] = el.value;
    changed(doc, el.type === "text" ? 900 : 150);
  }
  document.addEventListener("input", onInput);
  document.addEventListener("change", onInput);

  document.getElementById("acceptall").addEventListener("click", function(){
    DATA.items.forEach(function(x){
      if (!has((state[x.id] || {}).pick)) {
        state[x.id] = Object.assign({}, state[x.id] || {}, { pick: "0" });
        applyDoc(x.id); changed(x.id, 150);
      }
    });
  });

  function summary(){
    var L = ["Clean a Cat: my tool picks", ""];
    DATA.items.forEach(function(x, i){
      var d = state[x.id] || {};
      L.push((i + 1) + ". " + x.t + ": " + (has(d.pick) ? x.opts[Number(d.pick)] : "not picked") + (d.note ? " (" + d.note + ")" : ""));
    });
    var s = (state["s-skip"] || {}).note;
    if (s) L.push("", "From the skip list: " + s);
    return L.join("\n");
  }
  document.getElementById("copy").addEventListener("click", function(){
    var text = summary(), out = document.getElementById("copyout"), msg = document.getElementById("copied");
    function fallback(){ out.hidden = false; out.value = text; out.focus(); out.select(); msg.textContent = "Select all and copy the text below."; }
    try { navigator.clipboard.writeText(text).then(function(){ msg.textContent = "Copied. Paste it in the project chat."; }, fallback); }
    catch (e) { fallback(); }
  });

  function renderAll(){
    var ids = {};
    document.querySelectorAll("[data-doc]").forEach(function(el){ ids[el.dataset.doc] = 1; });
    Object.keys(ids).forEach(applyDoc);
    counts();
  }
  loadLocal(); renderAll();

  var gave = setTimeout(function(){ if (!online) setStatus("Picks are kept in this browser for now. Use Copy my picks to send them.", true); }, 10000);
  var use = window.claude && window.claude.use ? window.claude.use("db") : Promise.resolve(null);
  use.then(function(d){
    if (!d) { clearTimeout(gave); setStatus("Picks are kept in this browser. Use Copy my picks to send them.", true); return; }
    db = d;
    db.collection("picks").onSnapshot(function(snap){
      snap.docs.forEach(function(doc){
        if (dirty[doc.id] || writing[doc.id]) return;
        var body = Object.assign({}, doc.data() || {}); delete body.at;
        state[doc.id] = body; applyDoc(doc.id);
      });
      counts(); saveLocal();
      if (!snap.metadata.fromCache) {
        clearTimeout(gave);
        if (!online) { online = true; Object.keys(dirty).forEach(function(k){ if (dirty[k]) flush(k); }); }
        var busy = Object.keys(writing).some(function(k){ return writing[k]; });
        if (!busy) setStatus("All picks saved");
      }
    }, function(){
      clearTimeout(gave);
      setStatus("Could not reach your saved picks. Use Copy my picks below.", true);
    });
  }, function(){ clearTimeout(gave); setStatus("Picks are kept in this browser. Use Copy my picks to send them.", true); });
})();
</script>
'''
page = (PAGE.replace("__SECTIONS__", "\n".join(sections)).replace("__FACTS__", facts_html).replace("__SKIP__", skip_html)
        .replace("__LIMITS__", limits_html).replace("__NSKIP__", str(NSKIP)).replace("__NCARDS__", str(NCARDS))
        .replace("__DATA__", json.dumps(DATA).replace("<", "\\u003c")))
open(OUT_HTML, "w", encoding="utf-8").write(page)

# ----------------------------------------------------------------- Markdown copy
M = ["# Clean a Cat: tools and skills worth adding (2026-11-24 ET, Planning-Agent)", "",
     f"This is the file copy of Derek's tool picks page. {PAGE_LINK}", "",
     "Derek asked for a deep dive into open source repos and skills that could help before development goes further, with a focus on quality UI, menus and pop ups and on a game that looks and feels good on PC, phone, tablet and console without lag or crashes.", "",
     "**Short answer:** no outside library beats what we already have for UI. The best finds are free tools that Roblox itself now ships and a few small pieces to fold into our own skills. We recommend 5 additions now, 5 small trials once the first real screens are built and no UI framework yet. "
     f"Another {NSKIP} finds are on the skip list. **Nothing is added to the repo until Derek picks.** For each yes Planning-Agent opens a task for the thread that owns it.", "",
     "Derek's picks save in the page database, collection `picks`, doc id `s-<id>` with `pick` (the option index, 0 is our pick) and `note`. The skip list note is `s-skip`. Read them with the ArtifactData tool.", "",
     "Research notes behind this list: `Tools-Research/ui_libraries.md`, `performance_and_devices.md`, `skills_and_mcp.md` and `look_and_feel.md`.", ""]
n = 0
for g in GROUPS:
    M += [f"## {g['title']}", g["lead"], ""]
    for it in g["items"]:
        n += 1
        M += [f"### {n}. {it['t']} (`s-{it['id']}`)",
              f"- **What it is:** {it['what']}", f"- **Why:** {it['why']}", f"- **License:** {it['lic']}",
              f"- **Upkeep:** {it['keep']}", f"- **Cost and risk:** {it['cost']}", f"- **How it was checked:** {it['src']}",
              f"- **Who would do it:** {it['who'][0].upper() + it['who'][1:]}.",
              "- **Options:** " + " / ".join(f"{i}: {o}" for i, o in enumerate(it["opts"])) + ". Our pick is 0.", ""]
M += ["## Good to know", ""]
M += [f"- **{k}:** {v}" for k, v in FACTS]
M += ["", "## Looked at and skipped", "", "| Find | What it is | License | Why we skip it |", "|---|---|---|---|"]
M += [f"| {a} | {b} | {c} | {d} |" for a, b, c, d in SKIP]
M += ["", "## How sure this is", ""]
M += [f"- {x}" for x in LIMITS]
M += [""]
open(OUT_MD, "w", encoding="utf-8").write("\n".join(M))
print("cards", NCARDS, "skip", NSKIP)
