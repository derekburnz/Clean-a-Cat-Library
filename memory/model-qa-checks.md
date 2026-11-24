---
name: model-qa-checks
description: Which checks every Clean a Cat model must pass, the EL4CTEO Blender skills Derek asked about on 2026-11-24, and the gap that was found
metadata:
  type: feedback
  modified: 2026-11-24T13:28:01.472Z
---

Every model batch runs three checks before it goes to Review-QA: the build's gates (`gates.md`), `rbx_zfight.py` on the Part models, and the `blender-asset-qa` skill's `qa_check.py` (roblox profile, uv off) on the Blender meshes. The Blender skills are the EL4CTEO/blender-skills pack copied into the game repo's `.claude/skills/` (blender-core, blender-asset-qa, blender-game-optimization, blender-export-pipelines, blender-retopology-uv).

**Why:** Derek asked twice on 2026-11-24 (8 AM ET) whether the EL4CTEO Blender skills are in use for models. Model-Agent had read them but had not run `qa_check.py` since 2026-11-23, and a sweep found 59 of 100 models with findings (n-gons, flipped faces, faces in one plane). None showed in the game because the game loads the Part models, but the gap was real. Issue #160 fixes the findings and makes the check part of `build_all.py`.

**How to apply:** Never call a model done on `gates.md` and `rbx_zfight.py` alone. If `qa_check` is not yet a column in `gates.md`, run it by hand on every changed model. An accepted warning needs a written reason. The Model-Agent role file's skill list (section 7) is the list to check against, and Review-QA signs off, never Model-Agent. See [[art-and-models]].
