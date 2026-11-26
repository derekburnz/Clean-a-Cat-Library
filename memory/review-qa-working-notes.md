---
name: review-qa-working-notes
description: How Review-QA-Agent works in this project: verdict format, merge duty, visual QA rubric, where its files live
metadata:
  type: project
  modified: 2026-11-25T23:27:05.641Z
---
Review-QA-Agent's standing way of working (checked against its role file library/Review-QA-Agent/Review QA Agent.md on 2026-11-24):
- Every verdict is PASS, CHANGES NEEDED or SAME_CODE, names the exact head, says whether a restart is needed, and carries a QoL line on UI or gameplay PRs (the five checks in role file section 5) plus a QA line for the test plan.
- Review files go in docs/reviews/<date>-<topic>.md in the game repo; send the verdict to the author thread too.
- Model-Agent and Motion-FX cannot merge, so Review-QA merges their PRs after checking CI itself on GitHub (merge commit, full 40-char expectedHeadSha). Never arm on-hold PRs.
- Visual QA of draft models and screens uses section 8 of /mnt/project-files/Review-QA-Agent/qa-plan-first-5-minutes.md (phone-size renders, KEEP / FIX / DROP per item).
- Studio checks go through Sync-Agent with exact steps and a pass rule; it captures on an iPhone 14 emulator (844 x 390) and keeps images on Derek's PC.
- Skills to use: remote-security-checklist, luau-conventions, monetization-policy, ui-review, playtest-report, merge-and-publish, roblox-testing, roblox-mobile-playtest, roblox-creator-store-security-audit, roblox-policy-compliance.

- Speed budget (2026-11-25, #182, PR #423): docs/playtests/speed-budget.md in the game repo, test phone iPhone 12. #182 closes only after one playtest report uses the page. For the first iPhone 12 run, also use Motion-FX's effects list at Motion-FX-Agent/speed-budget-effects.md in the shared files (wash blur, 3 carriers in view, the opening, 20 min memory).

- Independent Blender QA (Derek 2026-11-25: every drafted model QA checked with the proper skills, everything clean): a cloud thread has no Blender, but `pip install bpy` (5.3) works. Import the PR's FBX, scale it x100 and apply (the FBX comes in at 0.01, which makes the z-fight check fire falsely), then run the blender-asset-qa skill's qa_check.py with `--profile roblox --no-uv` (the models are flat colour). The pivot and back-to-back warnings are accepted, as in gates.md. Also read the rbx model.json for Anchored and CanCollide/Query/Touch.
- Sync-Agent's Studio picture PRs (captures from Derek's PC, e.g. #409, #418, #420, #455) stay DRAFTS and are never merged into the public repo; give the verdict as a comment only. (#490 was merged by mistake 2026-11-25; checked, it held only our own art and a test name.)
- Owner rule: no decision cards. Park a question for Derek with the coordinator in one plain line instead.

**Why:** Derek asked on 2026-11-24 that every thread follows its role file and skills and saves the key points.
**How to apply:** a new Review-QA thread starts from this note plus the role file. See [[planning-status]] and [[art-and-models]].
