const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport:{width:1720,height:1000}, deviceScaleFactor: +process.argv[2]||1 });
await p.goto('file://' + __dirname + '/storyboard.html'); await p.waitForTimeout(1500); await p.evaluate(()=>document.fonts.ready);
await p.screenshot({ path: process.argv[3]||'sb.png', fullPage:true }); await b.close(); })();
