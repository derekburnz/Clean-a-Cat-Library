---
name: prepush-chain
description: Never pipe prepush.sh into tail inside a && push chain: the pipe hides its failure and the push still runs.
metadata:
  type: feedback
  modified: 2026-11-27T15:35:30.192Z
---

On 2026-11-27 Design-Agent ran `bash games/clean-a-cat/tools/prepush.sh 2>&1 | tail -2 && git push`. StyLua failed, but `tail` returned 0, so the branch was pushed anyway. Review-QA asked for the chain to stop when prepush fails.

**Why:** a red or unchecked push can reach CI and email Derek. The rule is to push only after "Pre-push check passed".

**How to apply:** write the log to a file and push only if it holds the pass line, for example `bash games/clean-a-cat/tools/prepush.sh > log 2>&1; grep -q "Pre-push check passed" log && git push`. Run StyLua from games/clean-a-cat on the changed files only. Running it on tools/ also reformats the cloudcheck shims. The pinned binary on a cloud thread is /root/.cache/cleanacat-tools/stylua-<version>/stylua.

Related: [[review-qa-working-notes]]
