const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  for (const [w, name] of [[420, 'phone'], [1200, 'desk']]) {
    const ctx = await b.newContext({ viewport: { width: w, height: 900 }, deviceScaleFactor: 1 });
    const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(String(e)));
    const fs = require('fs'); const seed = JSON.parse(fs.readFileSync(process.argv[3], 'utf8'));
    const st = {}; for (const k in seed.q2) { const d = Object.assign({}, seed.q2[k]); delete d.at; st[k] = d; }
    await p.goto('file://' + process.argv[2]);
    await p.evaluate(s => localStorage.setItem('clean-a-cat-plan-v2', JSON.stringify(s)), st);
    await p.reload(); await p.waitForTimeout(700);
    const r = await p.evaluate(() => ({ left: document.getElementById('n-left').textContent, done: document.getElementById('n-done').textContent,
      open: [...document.querySelectorAll('#questions article.q')].length, alldone: !document.getElementById('alldone').hidden,
      setup: [...document.querySelectorAll('#setup li.todo input[type=checkbox]')].map(i => i.id + '=' + i.checked).join(' '),
      notes: [...document.querySelectorAll('#setup li.todo textarea, #setup li.todo input[type=text]')].map(i => i.id + ':' + i.value).join(' | '),
      tonight: document.querySelectorAll('#saved dl.decided > div').length, notes: document.querySelectorAll('#notes dl.decided > div').length, leftrows: document.querySelectorAll('#setup dl.decided > div').length,
      done2: document.getElementById('c-done2__done').checked, width: document.documentElement.scrollWidth, vw: window.innerWidth }));
    console.log(name, JSON.stringify(r), 'errors', errs);
    await p.addStyleTag({ content: '.bar{position:static !important}' });
    await p.screenshot({ path: 'v57-' + name + '-top.png' });
    await p.locator('#saved').screenshot({ path: 'v57-' + name + '-saved.png' });
    await p.locator('#notes').screenshot({ path: 'v57-' + name + '-notes.png' }); await p.locator('#setup').screenshot({ path: 'v57-' + name + '-setup.png' });
    await ctx.close();
  }
  await b.close();
})();
