const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const ctx = await b.newContext({ viewport: { width: 420, height: 900 } });
  const seed = JSON.parse(require('fs').readFileSync(process.argv[3], 'utf8'));
  await ctx.addInitScript(seed => {
    const store = {}; for (const k in seed.q2) store[k] = Object.assign({}, seed.q2[k]);
    window.__store = store; window.__sets = [];
    let cb = null;
    const fire = () => cb && cb({ docs: Object.keys(store).map(id => ({ id, data: () => store[id] })), metadata: { fromCache: false } });
    const db = { collection: () => ({ onSnapshot: (f) => { cb = f; setTimeout(fire, 100); } }),
      doc: (path) => ({ set: (body) => new Promise(res => setTimeout(() => { const id = path.split('/')[1]; store[id] = body; window.__sets.push(id); res(); fire(); }, 200)) }) };
    window.claude = { use: () => new Promise(r => setTimeout(() => r(db), 2500)) };
  }, seed);
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(String(e)));
  await p.goto('file://' + process.argv[2]);
  // type before the database is connected (the case that lost his words)
  await p.fill('#q2-helpers__note', 'typed before the connection was up');
  await p.waitForTimeout(1500);
  await p.fill('#q2-impatience__note', 'second note'); await p.click('body');
  await p.waitForTimeout(3000);
  const r = await p.evaluate(() => ({ helpersNote: document.getElementById('q2-helpers__note').value, stored: (window.__store['q2-helpers'] || {}).note, storedPick: String((window.__store['q2-helpers'] || {}).pick),
    imp: (window.__store['q2-impatience'] || {}).note, sets: window.__sets, pickNow: document.getElementById('q2-helpers__pick0').checked, status: document.getElementById('status').textContent,
    left: document.getElementById('n-left').textContent, tucked: document.querySelectorAll('#answered-list article.q').length, helpersVisible: !!document.querySelector('#questions #q2-helpers'),
    unsent: localStorage.getItem('clean-a-cat-plan-v2-unsent') }));
  console.log(JSON.stringify(r), 'errors', errs);
  await p.reload(); await p.waitForTimeout(3200);
  console.log('after reload', JSON.stringify(await p.evaluate(() => ({ left: document.getElementById('n-left').textContent, tucked: document.querySelectorAll('#answered-list article.q').length, helpersTucked: !!document.querySelector('#answered-list #q2-helpers'), note: document.getElementById('q2-helpers__note').value, status: document.getElementById('status').textContent }))));
  await b.close();
})();
