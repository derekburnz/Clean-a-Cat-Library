const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const ctx = await b.newContext({ viewport: { width: 420, height: 900 } });
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(String(e)));
  const fs = require('fs'); const seed = JSON.parse(fs.readFileSync(process.argv[3], 'utf8')); const ch = JSON.parse(fs.readFileSync(process.argv[4], 'utf8'));
  const st = {}; for (const src of [seed.q2, ch.q2]) for (const k in src) { const d = Object.assign({}, src[k]); delete d.at; st[k] = d; }
  await p.goto('file://' + process.argv[2]);
  await p.evaluate(s => localStorage.setItem('clean-a-cat-plan-v2', JSON.stringify(s)), st);
  await p.reload(); await p.waitForTimeout(500);
  await p.addStyleTag({ content: '.bar{position:static !important}' });
  const r = await p.evaluate(() => ({ left: document.getElementById('n-left').textContent, done: document.getElementById('n-done').textContent,
    first: [...document.querySelectorAll('#questions article.q')].slice(0, 9).map(a => a.id.slice(3)).join(' '), helpersTucked: !!document.querySelector('#answered-list #q2-helpers'),
    width: document.documentElement.scrollWidth }));
  console.log(JSON.stringify(r), 'errors', errs);
  const bb = await (await p.$('#q2-starterpack')).boundingBox();
  await p.screenshot({ path: 'f-pack.png', clip: { x: 0, y: bb.y - 130, width: 420, height: 1750 }, fullPage: true });
  await b.close();
})();
