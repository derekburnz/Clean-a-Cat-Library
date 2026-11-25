const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const ctx = await b.newContext({ viewport: { width: 420, height: 900 } });
  const p = await ctx.newPage();
  const errs = []; p.on('pageerror', e => errs.push(String(e)));
  const url = 'file://' + process.argv[2];
  const seed = JSON.parse(require('fs').readFileSync(process.argv[3], 'utf8'));
  const st = {}; for (const k in seed.q2) { const d = Object.assign({}, seed.q2[k]); delete d.at; st[k] = d; }
  for (const k in seed.todo_notes_linked) st[k] = seed.todo_notes_linked[k];
  await p.goto(url);
  await p.evaluate(s => localStorage.setItem('clean-a-cat-plan-v2', JSON.stringify(s)), st);
  await p.reload(); await p.waitForTimeout(500);
  const info = async () => p.evaluate(() => ({
    left: document.getElementById('n-left').textContent, done: document.getElementById('n-done').textContent,
    visible: document.querySelectorAll('#questions article.q').length, tucked: document.querySelectorAll('#answered-list article.q').length,
    helpersVisible: !!document.querySelector('#questions #q2-helpers'), groupsShown: [...document.querySelectorAll('#questions .qgroup')].filter(g => !g.hidden).length,
    firstNums: [...document.querySelectorAll('#questions article.q .qn')].slice(0, 3).map(e => e.textContent).join(','),
    width: document.documentElement.scrollWidth, status: document.getElementById('status').textContent }));
  console.log('seeded', JSON.stringify(await info()));
  await p.addStyleTag({ content: '.bar{position:static !important}' });
  await p.screenshot({ path: 'd-top.png' });
  const q = await p.$('#q2-helpers'); const qb = await q.boundingBox();
  await p.screenshot({ path: 'd-helpers.png', clip: { x: 0, y: qb.y - 120, width: 420, height: 1500 }, fullPage: true });
  // type helper words, pick an open question, then reload at once: words must survive and stay marked unsent
  await p.fill('#q2-helpers__note', 'helpers test words');
  await p.click('#q2-stations__pick0');
  const before = await p.evaluate(() => !!document.querySelector('#questions #q2-stations'));
  await p.reload(); await p.waitForTimeout(500);
  const after = await p.evaluate(() => ({ note: (document.getElementById('q2-helpers__note') || {}).value, unsent: localStorage.getItem('clean-a-cat-plan-v2-unsent'),
    helpersTucked: !!document.querySelector('#answered-list #q2-helpers'), stationsTucked: !!document.querySelector('#answered-list #q2-stations') }));
  console.log('stays in place after a pick', before, 'after reload', JSON.stringify(after), JSON.stringify(await info()));
  await p.click('#answered > summary'); await p.waitForTimeout(200);
  const ab = await (await p.$('#answered')).boundingBox();
  await p.screenshot({ path: 'd-answered.png', clip: { x: 0, y: ab.y, width: 420, height: 1600 }, fullPage: true });
  await p.click('#acceptall'); await p.waitForTimeout(300);
  console.log('after take all', JSON.stringify(await info()), 'errors', errs.slice(0, 3));
  await b.close();
})();
