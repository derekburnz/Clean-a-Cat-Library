#!/bin/bash
# usage: pr_qa.sh <pr number>  — independent Blender QA (roblox profile, UVs off) on every FBX the PR adds or changes
cd "${GAME_REPO:-/home/claude/Clean-a-Cat}" || exit 1
git fetch -q origin main "pull/$1/head:pr$1" || exit 1
echo "head $(git rev-parse pr$1)"
for f in $(git diff --name-only --diff-filter=AM origin/main...pr$1 -- 'assets/clean-a-cat/exports/*.fbx'); do
  git show "pr$1:$f" > /tmp/qa_cur.fbx
  r=$(python3 $(dirname "$0")/run_qa.py /tmp/qa_cur.fbx --profile roblox --no-uv 2>&1 | grep '@@JSON' | sed 's/@@JSON@@//')
  echo "$r" | python3 -c "
import json,sys
d=json.load(sys.stdin); o=d['objects']
print('$(basename $f .fbx)', 'PASS' if d['pass'] else 'FAIL', 'tris', sum(v['tris'] for v in o.values()), 'objs', len(o))
for e in d['errors']: print('  ERR', e)
for w in d['warnings']: print('  warn', w)"
done
