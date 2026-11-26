---
name: model-qa-checks
description: Which checks every Clean a Cat model must pass, the EL4CTEO Blender skills Derek asked about on 2026-11-24, and the gap that was found
metadata:
  type: feedback
  modified: 2026-11-24T16:15:00.000Z
---

Every model batch runs three checks before it goes to Review-QA: the build's gates (`gates.md`), `rbx_zfight.py` on the Part models, and the `blender-asset-qa` skill's `qa_check.py` (roblox profile, uv off) on the Blender meshes. The Blender skills are the EL4CTEO/blender-skills pack copied into the game repo's `.claude/skills/` (blender-core, blender-asset-qa, blender-game-optimization, blender-export-pipelines, blender-retopology-uv).

**Why:** Derek asked twice on 2026-11-24 (8 AM ET) whether the EL4CTEO Blender skills are in use for models. Model-Agent had read them but had not run `qa_check.py` since 2026-11-23, and a sweep found 59 of 100 models with findings (n-gons, flipped faces, faces in one plane). None showed in the game because the game loads the Part models, but the gap was real. Issue #160 fixes the findings and makes the check part of `build_all.py`.

**How to apply:** Never call a model done on `gates.md` and `rbx_zfight.py` alone. If `qa_check` is not yet a column in `gates.md`, run it by hand on every changed model. An accepted warning needs a written reason. The Model-Agent role file's skill list (section 7) is the list to check against, and Review-QA signs off, never Model-Agent. See [[art-and-models]].

**What only Studio catches (2026-11-24, issue #176):** the three checks and the renders all passed the new wash tub, but Sync-Agent's Studio look from above showed a seam and a darker wedge in the water. Cause: overlapping see-through parts (two layers look darker) in Roblox's Glass material. Rule since then: no Glass material on any model, a bath's `_Water` exports solid, and see-through parts must never overlap each other. A model with see-through parts is not done until Sync-Agent has looked at it in Studio from above and from the play camera.

**Gate since 2026-11-24 (issue #235, PR #241):** the export stops the build when two see-through parts of one model overlap, and `rbx_zfight.py` prints `glass N` beside `zfight N`. A clean run is every line ending `zfight 0 area 0.000 glass 0`. It cannot see two curved sides that barely cross or overlaps between two models, so the Studio look still applies.
