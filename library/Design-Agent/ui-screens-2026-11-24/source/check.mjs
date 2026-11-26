// Screen check for the HTML mockups (Design-Agent, 2026-11-24). The same limits as the game's UI gate
// (games/clean-a-cat/tools/cloudcheck/uigate-checks.mjs): 44 px taps on touch and 36 with a mouse, no text under 9 px
// (14 px is flagged as small, the ui-review body text rule), nothing off screen or under Roblox's menu buttons (184 x 58 at the top left), two
// fonts, plus overlapping buttons, buttons under the thumbstick or jump button, and words cut off.
//
//   node check.mjs [--out dir] [--screen name] [--profile name]
// Writes <out>/<screen>[-<state>]-<profile>.png, report.json and index.html. Exit code 1 on any failure.
import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const PROFILES = [
  { name: 'smallphone', width: 667, height: 375, touch: true },
  { name: 'phone', width: 844, height: 390, touch: true },
  { name: 'a06', width: 705, height: 338, touch: true },
  { name: 'tablet', width: 1180, height: 820, touch: true },
  { name: 'ipad43', width: 1024, height: 768, touch: true },
  { name: 'desktop', width: 1280, height: 720, touch: false },
  { name: 'console', width: 1920, height: 1080, touch: false },
];
const LIMITS = { tapTouch: 44, tapMouse: 36, textMin: 9, textSmall: 14, topbarLeft: 184, inset: 58, fonts: ['Fredoka One', 'Nunito'] };

const args = { out: path.join(HERE, 'shots'), screen: null, profile: null };
for (let i = 2; i < process.argv.length; i++) {
  const a = process.argv[i];
  if (a === '--out') args.out = process.argv[++i];
  else if (a === '--screen') args.screen = process.argv[++i];
  else if (a === '--profile') args.profile = process.argv[++i];
}
fs.mkdirSync(args.out, { recursive: true });

const screens = fs.readdirSync(HERE).filter((f) => f.endsWith('.html') && f !== 'index.html' && !f.startsWith('_'))
  .map((f) => f.replace(/\.html$/, '')).filter((n) => !args.screen || n === args.screen).sort();

function inPage(limits, touch) {
  const vw = innerWidth, vh = innerHeight;
  const findings = [];
  const add = (check, el, msg, fail = true) => findings.push({ check, fail, msg, where: describe(el) });
  function describe(el) {
    if (!el) return '';
    const id = el.id ? '#' + el.id : '';
    const cls = el.classList && el.classList.length ? '.' + [...el.classList].slice(0, 3).join('.') : '';
    const t = (el.innerText || el.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 30);
    return `${el.tagName.toLowerCase()}${id}${cls}${t ? ` "${t}"` : ''}`;
  }
  const visible = (el) => {
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden' || Number(cs.opacity) === 0) return false;
    const r = el.getBoundingClientRect();
    return r.width > 0 && r.height > 0;
  };
  const inter = (a, b) => !(a.right <= b.left || b.right <= a.left || a.bottom <= b.top || b.bottom <= a.top);
  const area = (a, b) => Math.max(0, Math.min(a.right, b.right) - Math.max(a.left, b.left)) * Math.max(0, Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top));
  const scroller = (el) => el.closest('.scroll');
  const rbx = (el) => el.closest('[data-rbx]') || el.closest('.world') || el.closest('.backdrop');

  // taps
  const taps = [...document.querySelectorAll('[data-tap]')].filter(visible);
  const min = touch ? limits.tapTouch : limits.tapMouse;
  for (const el of taps) {
    const r = el.getBoundingClientRect();
    if (Math.min(r.width, r.height) < min - 0.5) add('tap', el, `${Math.round(r.width)} x ${Math.round(r.height)} px, under ${min}`);
  }
  for (let i = 0; i < taps.length; i++) for (let j = i + 1; j < taps.length; j++) {
    const a = taps[i], b = taps[j];
    if (a.contains(b) || b.contains(a)) continue;
    const ra = a.getBoundingClientRect(), rb = b.getBoundingClientRect();
    if (area(ra, rb) > 4) add('overlap', a, `overlaps ${describe(b)}`);
  }

  // text: every element with its own words
  const fonts = new Set();
  const all = [...document.querySelectorAll('#stage *')].filter((el) => !rbx(el) && visible(el));
  const scale = Number(document.body.dataset.scale || 1);
  for (const el of all) {
    const own = [...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim());
    if (!own) continue;
    const cs = getComputedStyle(el);
    const px = parseFloat(cs.fontSize) * scale;
    if (px < limits.textMin - 0.01) add('text', el, `${px.toFixed(1)} px words, under ${limits.textMin}`);
    else if (px < limits.textSmall - 0.01) add('small', el, `${px.toFixed(1)} px words`, false);
    fonts.add(cs.fontFamily.split(',')[0].replace(/["']/g, '').trim());
    if ((cs.overflow === 'hidden' || cs.textOverflow === 'ellipsis') && el.scrollWidth > el.clientWidth + 1)
      add('cut', el, `words cut off (${el.scrollWidth} > ${el.clientWidth})`);
  }
  for (const f of fonts) if (!limits.fonts.includes(f)) add('fonts', null, `font ${f} besides ${limits.fonts.join(' and ')}`);
  document.fonts.forEach((f) => { if (f.status === 'error') add('fonts', null, `font ${f.family} failed to load`); });

  // off screen and under Roblox's menu buttons
  const bar = { left: 0, top: 0, right: limits.topbarLeft, bottom: limits.inset };
  for (const el of all) {
    const own = [...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim());
    const isThing = own || el.hasAttribute('data-tap') || el.matches('.win,.card,.rbtn,.btn,.tile,img,svg.ic');
    if (!isThing) continue;
    if (el.closest('svg') && el.tagName.toLowerCase() !== 'svg') continue;
    const r = el.getBoundingClientRect();
    const sc = scroller(el);
    if (!sc && (r.left < -1 || r.top < -1 || r.right > vw + 1 || r.bottom > vh + 1)) add('offscreen', el, `at ${Math.round(r.left)},${Math.round(r.top)} to ${Math.round(r.right)},${Math.round(r.bottom)} on ${vw} x ${vh}`);
    if (!el.closest('.allow-topbar') && inter(r, bar) && area(r, bar) > 6) add('topbar', el, `under Roblox's menu buttons (${limits.topbarLeft} x ${limits.inset})`);
  }

  // words that are not part of a button keep 4 px clear of every button
  const gap = (a, b) => Math.max(b.left - a.right, a.left - b.right, b.top - a.bottom, a.top - b.bottom);
  for (const el of all) {
    if (el.closest('[data-tap]') || el.closest('.scroll')) continue;
    if (![...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim())) continue;
    const r = el.getBoundingClientRect();
    for (const t of taps) {
      if (t.contains(el) || el.contains(t) || t.closest('.scroll')) continue;
      if (gap(r, t.getBoundingClientRect()) < 4) { add('crowd', el, `words within 4 px of ${describe(t)}`); break; }
    }
  }

  // thumbstick and jump button on touch: HUD buttons must stay clear
  if (touch && !document.body.classList.contains('no-move')) {
    for (const c of document.querySelectorAll('.rbx-stick,.rbx-jump')) {
      const rc = c.getBoundingClientRect();
      for (const el of taps) if (inter(el.getBoundingClientRect(), rc)) add('controls', el, `under the ${c.className.includes('jump') ? 'jump button' : 'thumbstick'}`);
    }
  }
  return { findings, scale, fonts: [...fonts] };
}

const browser = await chromium.launch();
const report = [];
for (const screen of screens) {
  const file = path.join(HERE, screen + '.html');
  const html = fs.readFileSync(file, 'utf8');
  const states = (html.match(/<meta name="states" content="([^"]*)"/) || [, ''])[1].split(',').map((s) => s.trim()).filter(Boolean);
  for (const state of states.length ? states : ['']) {
    for (const p of PROFILES.filter((p) => !args.profile || p.name === args.profile)) {
      const ctx = await browser.newContext({ viewport: { width: p.width, height: p.height }, deviceScaleFactor: 1, hasTouch: p.touch });
      const page = await ctx.newPage();
      const errors = [];
      page.on('pageerror', (e) => errors.push(String(e)));
      const url = pathToFileURL(file).href + `?touch=${p.touch ? 1 : 0}` + (state ? `&state=${state}` : '');
      await page.goto(url);
      await page.evaluate(() => document.fonts.ready);
      await page.waitForTimeout(250);
      const r = await page.evaluate(`(${inPage.toString()})(${JSON.stringify(LIMITS)}, ${p.touch})`)
        .catch((e) => ({ findings: [{ check: 'error', fail: true, msg: String(e) }] }));
      const shot = `${screen}${state ? '-' + state : ''}-${p.name}.png`;
      await page.screenshot({ path: path.join(args.out, shot) });
      for (const e of errors) r.findings.push({ check: 'error', fail: true, msg: e });
      report.push({ screen, state, profile: p.name, shot, ...r });
      await ctx.close();
    }
  }
}
await browser.close();

const fails = report.flatMap((r) => r.findings.filter((f) => f.fail).map((f) => ({ ...f, screen: r.screen, state: r.state, profile: r.profile })));
const notes = report.flatMap((r) => r.findings.filter((f) => !f.fail).map((f) => ({ ...f, screen: r.screen, state: r.state, profile: r.profile })));
fs.writeFileSync(path.join(args.out, 'report.json'), JSON.stringify(report, null, 1));
const rows = report.map((r) => `<figure><img src="${r.shot}" loading="lazy"><figcaption>${r.screen}${r.state ? ' (' + r.state + ')' : ''} · ${r.profile} · ${r.findings.filter((f) => f.fail).length} fails</figcaption></figure>`).join('\n');
fs.writeFileSync(path.join(args.out, 'index.html'), `<!doctype html><meta charset="utf-8"><title>Clean a Cat screens</title><style>body{font-family:sans-serif;background:#222;color:#eee;margin:16px}figure{display:inline-block;margin:8px;vertical-align:top}img{max-width:420px;display:block;border:1px solid #555}</style>${rows}`);
console.log(`${report.length} pictures, ${fails.length} failures, ${notes.length} notes`);
for (const f of fails.slice(0, 80)) console.log(`FAIL ${f.screen}${f.state ? '/' + f.state : ''} ${f.profile} ${f.check}: ${f.msg} ${f.where || ''}`);
const small = new Map();
for (const n of notes) { const k = `${n.screen}${n.state ? '/' + n.state : ''} ${n.check}`; small.set(k, (small.get(k) || 0) + 1); }
for (const [k, v] of small) console.log(`note ${k}: ${v}`);
process.exit(fails.length ? 1 : 0);
