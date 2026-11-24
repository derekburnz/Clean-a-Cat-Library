# Clean a Cat memory

Standing rules live in the project instructions. This file holds only current facts. Keep it short: move detail into one topic file per subject and link it here. Never save secrets.

- [project-setup](project-setup.md): state of the template setup.
- Owner: Derek (GitHub derekburnz), Eastern time. Claude plan: Ultra, so every thread runs on its roster model with no downgrades. Answer first, plain words.
- GitHub: only derekburnz on this project. The 2573351 login is NOT a GitHub collaborator (Derek's call 2026-11-23); skip assigning or requesting review from it on PRs. 2573351 is tied to Derek's Roblox account that owns the Creampuff Games group.
- Repos (split by Derek 2026-11-23 ET): game derekburnz/Clean-a-Cat, library derekburnz/Clean-a-Cat-Library. Derek's call 2026-11-23: both stay PUBLIC until game release, then he makes them private. Never put secrets in them. Also attached: derekburnz/Roblox-Asset-Library, Derek's reusable assets from past games; check it before making new models, UI or sounds.
- Main branch rule: Derek added a ruleset on main 2026-11-24 ET (active, PR required, both test checks required, no force push or delete).
- Game name LOCKED 2026-11-23 ET: Clean a Cat (chosen over Clean the Cat), slug clean-a-cat. Cat Spaw dropped everywhere. Web name check found no conflicting game.
- Stage: planning plus build setup. Derek leans to a cat spa where customers bring dirty cats (not confirmed), with timed upgrades as the reason to return. The design stays a draft until Derek's playtests of animal spa games are in (see planning-status). Path in the game repo: docs/design/clean-a-cat/gdd.md. Model style picked by Model-Agent: Bubble Pastel (Derek can swap).
- Design-Agent pause PARTLY LIFTED by Derek 2026-11-23 ET: it may draft likely-needed UI screens (with Model-Agent drafting likely-needed models and Review-QA checking visual quality). Derek's words: focus on quality, QA and research of what looks good, don't worry about time or usage, use Fable 5.2 high for anything needed. Final gameplay design still waits on Derek's decision.
- Design goals (Derek): a fun first 5 minutes for a low bounce rate off home recommendations, and a strong reason to return on day 2. Day 7 retention he handles with events. He can playtest Roblox games for us. No ad numbers needed. Cat Cafe has no spa.
- Roblox (Derek 2026-11-23 ET): universe 10778773655, place 79301459457383, owned by the Roblox group Creampuff Games (group id 107520049; it already has players from Derek's other game). Derek also made a dev copy place, added to the group key's perms. Uploads must have the same owner. Owner key and group key (full access) are in GitHub secrets; auto publish variable set true. Derek wants no more keys. Server size undecided until after design.
- Studio PC: DESKTOP-DFOGFG7. Derek approved the Desktop and Downloads folders for management; the game folder goes under C:\Users\Derek\Downloads. Only Sync-Agent drives Studio there.
- Threads running (all 8 roles, started 2026-11-23 ET on Derek's OK): Planning-Agent, Gameplay-Engineer, Design-Agent, Review-QA-Agent, Motion-FX-Agent, Model-Agent, Growth-Agent, Sync-Agent. Roster with models and effort: library/Setup/setup-drafts-2026-11-23/threads.md in Clean-a-Cat-Library. Never write thread ids here.
- Owner preferences: confirmed 2026-11-22 (ET). Changes from the defaults in library/Setup/owner-preferences.md: (1) server restarts are allowed without asking until public release (ads running or real players on servers); after that, no restart without Derek's OK. AUTO_RESTART still stays unset. (2) PRs that pass the tests are always auto-merged, with the Review-QA pass still the gate. Publishing stays silent.
- Restarts: allowed until public release, then only on Derek's OK. Last: none yet.
- Switches (checked 2026-11-24 ET): main publishes live by itself (version 22 at 13:16 UTC), but the flags workflow has never run, so every LiveFlags switch on main (20) is still off. They are held off on purpose until Derek says whether the design pause covers turning features on.
- Open asks on the owner: playtests and the updated plan page (40 questions, published 2026-11-24 ET by Planning-Agent). Sounds: Derek listened 2026-11-23 ET and they are fine; tuning waits until the game is decided. Derek won't look at prototypes until spa playtests and hook research are done.
- Benchmark: sheet set up by Growth-Agent at Growth-Agent/benchmark-sheet.md.
- Topic files (add one line per file: [name](name.md), what it holds):
- [planning-status](planning-status.md): Derek's decisions, the Clean a Cat design state, files and what waits on Derek.
- [roblox-research-howto](roblox-research-howto.md): how to read Roblox game stats from a cloud thread.
- [roblox-age-rules](roblox-age-rules.md): maturity reading for the spa and the Kids and Select gate for reaching young players.
- [growth-voices-and-videos](growth-voices-and-videos.md): use the voice studio repo, not ElevenLabs; where the 2026-11-24 video notes are.
- [art-and-models](art-and-models.md): art style and model decisions.
- [derek-playtest-notes](derek-playtest-notes.md): what Derek liked and disliked in rival games and the game shape he leans toward.
- [growth-role-notes](growth-role-notes.md): Growth lane rules, playbook map and state.
- [model-qa-checks](model-qa-checks.md): Model-Agent's note on the Blender QA check for models.
