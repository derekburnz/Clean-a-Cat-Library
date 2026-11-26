const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  for (const [w, name, dsf] of [[420, 'phone', 1], [1200, 'desk', 1]]) {
    const ctx = await b.newContext({ viewport: { width: w, height: 900 }, deviceScaleFactor: dsf });
    const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(String(e)));
    const fs = require('fs'); const seed = JSON.parse(fs.readFileSync(process.argv[3], 'utf8'));
    const st = {}; for (const k in seed.q2) { const d = Object.assign({}, seed.q2[k]); delete d.at; st[k] = d; }
    await p.goto('file://' + process.argv[2]);
    await p.evaluate(s => localStorage.setItem('clean-a-cat-plan-v2', JSON.stringify(s)), st);
    await p.reload(); await p.waitForTimeout(700);
    const r = await p.evaluate(() => ({ left: document.getElementById('n-left').textContent, done: document.getElementById('n-done').textContent,
      first: [...document.querySelectorAll('#questions article.q')].map(a => a.id.slice(3) + ':' + a.querySelector('.qn').textContent).join(' '),
      setup: [...document.querySelectorAll('#setup li.todo input[type=checkbox]')].map(i => i.id + '=' + i.checked).join(' '),
      done2: document.getElementById('c-done2__done').checked, lockIn: !!document.querySelector('#answered #c-lock__done') && document.getElementById('c-lock__done').checked,
      img: [...document.querySelectorAll('#q2-icons2 img')].map(i => i.naturalWidth), width: document.documentElement.scrollWidth, vw: window.innerWidth }));
    console.log(name, JSON.stringify(r), 'errors', errs);
    await p.addStyleTag({ content: '.bar{position:static !important}' });
    await p.screenshot({ path: 'n-' + name + '-top.png' });
    
    await p.locator('#setup').screenshot({ path: 'n-' + name + '-setup.png' });
    if (name === 'phone') { await p.locator('#q2-headbows').scrollIntoViewIfNeeded(); await p.waitForTimeout(500); await p.locator('#q2-headbows').screenshot({ path: 'n-phone-newq.png' }); await p.locator('#q2-headbows').screenshot({ path: 'n-phone-newq4.png' }); await p.locator('li.todo:has(#c-s2-devtest__done)').screenshot({ path: 'n-phone-notify.png' }); console.log('imgs', JSON.stringify(await p.evaluate(() => [...document.querySelectorAll('#q2-headbows img')].map(i => i.naturalWidth)))); }
    if (name === 'phone') {
      // answer one question and tick a setup step; check counts and local state
      await p.fill('#c-s2-passes__note', 'test 123'); await p.check('#c-s2-passes__done'); await p.waitForTimeout(400);
      const r2 = await p.evaluate(() => ({ left: document.getElementById('n-left').textContent, ls: JSON.parse(localStorage.getItem('clean-a-cat-plan-v2'))['c-s2-passes'], pv: 1 }));
      console.log('after', JSON.stringify(r2));
      await p.click('#copy'); await p.waitForTimeout(200);
      const txt = await p.inputValue('#copyout'); console.log(txt.split('\n').filter(l => /Setup|passes|starter pack ad|Make the/i.test(l)).slice(0, 6).join('\n'));
    }
    await ctx.close();
  }
  await b.close();
})();
