// Clean a Cat mockup harness (Design-Agent, 2026-11-24).
// Lays the screen out in design pixels and scales it like the asset library's Scale.luau: design 1280 x 720,
// scale = clamp(min(w / 1280, h / 720), 0.75, 1.3), and touch screens never below 0.75.
// URL options: ?touch=1 (phone or tablet), ?state=<name> (a screen's variant).
// Elements a player can press carry data-tap; check.mjs measures them.
(function () {
  const q = new URLSearchParams(location.search);
  const touch = q.get('touch') === '1';
  document.body.classList.toggle('touch', touch);
  if (q.get('state')) document.body.dataset.state = q.get('state');

  // ---------- icons: 64 x 64, ink outline 4 ----------
  const K = '#45226b';
  const S = `stroke="${K}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"`;
  const ICONS = {
    coin: `<circle cx="32" cy="34" r="24" fill="#d19e22" ${S}/><circle cx="32" cy="30" r="24" fill="#ffc94d" ${S}/><circle cx="32" cy="30" r="15" fill="#ffe08a" stroke="#d19e22" stroke-width="3"/><path d="M26 30c0-4 3-7 6-7m0 0v14" fill="none" stroke="#b8820f" stroke-width="4" stroke-linecap="round"/>`,
    star: `<path d="M32 5l8 17 18 2-13 13 4 19-17-9-17 9 4-19L6 24l18-2z" fill="#ffd84d" ${S}/><path d="M24 22l4-1" stroke="#fff" stroke-width="4" stroke-linecap="round"/>`,
    starEmpty: `<path d="M32 5l8 17 18 2-13 13 4 19-17-9-17 9 4-19L6 24l18-2z" fill="#eadfd3" ${S}/>`,
    xp: `<path d="M32 4l24 14v28L32 60 8 46V18z" fill="#c07cff" ${S}/><text x="32" y="41" text-anchor="middle" font-family="Fredoka One" font-size="22" fill="#fff" stroke="${K}" stroke-width="1.5">XP</text>`,
    sponge: `<path d="M6 26l10-12h42l-10 12z" fill="#c9f5e5" ${S}/><path d="M48 26l10-12v26l-10 12z" fill="#e0b640" ${S}/><rect x="6" y="26" width="42" height="26" rx="4" fill="#ffd84d" ${S}/><rect x="6" y="22" width="42" height="9" rx="3" fill="#a8e6cf" ${S}/><circle cx="16" cy="40" r="3.5" fill="#e0a92e"/><circle cx="28" cy="45" r="3" fill="#e0a92e"/><circle cx="38" cy="38" r="3.5" fill="#e0a92e"/><path d="M12 34h10" stroke="#fff6c2" stroke-width="3" stroke-linecap="round"/><circle cx="54" cy="8" r="5" fill="#e8f7ff" stroke="${K}" stroke-width="3"/>`,
    brush: `<path d="M30 40l24 14" stroke="${K}" stroke-width="12" stroke-linecap="round"/><path d="M30 40l24 14" stroke="#f08aa6" stroke-width="6" stroke-linecap="round"/><rect x="4" y="18" width="34" height="22" rx="10" fill="#ffb3c7" ${S}/><path d="M10 18V8M17 18V6M24 18V6M31 18V8" stroke="${K}" stroke-width="4" stroke-linecap="round"/><path d="M10 28h18" stroke="#ffe0ea" stroke-width="4" stroke-linecap="round"/>`,
    shower: `<path d="M12 60V22a12 12 0 0 1 12-12h12" fill="none" stroke="${K}" stroke-width="11" stroke-linecap="round"/><path d="M12 60V22a12 12 0 0 1 12-12h12" fill="none" stroke="#d6dee6" stroke-width="5" stroke-linecap="round"/><path d="M30 12h28l-5 13H35z" fill="#8fd3fe" ${S}/><path d="M36 32l-3 7M45 32v8M54 32l3 7M40 46l-2 7M50 46l2 7" stroke="#3faef2" stroke-width="5" stroke-linecap="round"/>`,
    dryer: `<path d="M8 22a16 16 0 0 1 16-14h18v28H24A16 16 0 0 1 8 22z" fill="#8fd3fe" ${S}/><rect x="42" y="14" width="12" height="16" rx="3" fill="#ffb3c7" ${S}/><path d="M22 36l-4 20h12l2-20" fill="#ffb3c7" ${S}/><circle cx="24" cy="22" r="6" fill="#fff" ${S} stroke-width="3"/><path d="M56 16h4M56 22h6M56 28h4" stroke="#8fd3fe" stroke-width="3" stroke-linecap="round"/>`,
    tweezers: `<path d="M10 6l26 44M22 4l20 44" fill="none" stroke="${K}" stroke-width="11" stroke-linecap="round"/><path d="M10 6l26 44M22 4l20 44" fill="none" stroke="#d9c7f5" stroke-width="5" stroke-linecap="round"/><circle cx="46" cy="52" r="10" fill="#b98a5c" ${S}/><path d="M46 38v6M46 60v4M32 52h6M54 52h6M37 43l4 4M51 57l4 4M55 43l-4 4M41 57l-4 4" stroke="${K}" stroke-width="3" stroke-linecap="round"/>`,
    clipper: `<g ${S}><path d="M5 47c0-5 5-8 13-9l32-4c4 0 8 2 9 5l-6 4 6 5c-2 3-5 5-10 5H15c-6 0-10-2-10-6z" fill="#e3e9f2"/><path d="M12 46l38-2.5" fill="none" stroke-width="3"/><rect x="-4" y="-6.5" width="46" height="13" rx="6.5" transform="translate(47 31) rotate(203)" fill="#ffb3c7"/><circle cx="45" cy="33" r="2.6" fill="${K}" stroke="none"/></g><path d="M13 16.5l13 5.5" stroke="#fff" stroke-width="2.6" stroke-linecap="round" opacity=".85"/>`,
    bath: `<path d="M6 30h52v8a14 14 0 0 1-14 14H20A14 14 0 0 1 6 38z" fill="#fff" ${S}/><rect x="4" y="26" width="56" height="8" rx="4" fill="#a8e6cf" ${S}/><circle cx="20" cy="18" r="7" fill="#bfe6ff" ${S} stroke-width="3"/><circle cx="34" cy="13" r="5" fill="#bfe6ff" ${S} stroke-width="3"/><circle cx="44" cy="20" r="6" fill="#bfe6ff" ${S} stroke-width="3"/><path d="M18 52l-3 6M46 52l3 6" ${S}/>`,
    paw: `<ellipse cx="32" cy="42" rx="14" ry="12" fill="#ffb3c7" ${S}/><ellipse cx="14" cy="28" rx="6" ry="8" fill="#ffb3c7" ${S}/><ellipse cx="25" cy="17" rx="6" ry="8" fill="#ffb3c7" ${S}/><ellipse cx="39" cy="17" rx="6" ry="8" fill="#ffb3c7" ${S}/><ellipse cx="50" cy="28" rx="6" ry="8" fill="#ffb3c7" ${S}/>`,
    book: `<path d="M32 14C24 8 14 8 6 10v40c8-2 18-2 26 4 8-6 18-6 26-4V10c-8-2-18-2-26 4z" fill="#fff" ${S}/><path d="M32 14v40" ${S}/><path d="M6 10c8-2 18-2 26 4V54c-8-6-18-6-26-4z" fill="#c9f5e5" ${S}/><path d="M14 22l3 6 6 1-4 4 1 6-6-3-6 3 1-6-4-4 6-1z" fill="#ffd84d" stroke="${K}" stroke-width="2" stroke-linejoin="round"/>`,
    hammer: `<path d="M30 26l-16 28" ${S} stroke-width="9"/><path d="M30 26l-16 28" stroke="#d9a46a" stroke-width="4" stroke-linecap="round"/><path d="M18 14l22-6 14 12-6 8-12-6-12 2z" fill="#8fd3fe" ${S}/>`,
    customer: `<circle cx="32" cy="20" r="12" fill="#ffd9b8" ${S}/><path d="M12 58c0-14 9-22 20-22s20 8 20 22z" fill="#ffb3c7" ${S}/><path d="M18 16c2-8 8-12 14-12s12 4 14 12c-6-2-22-2-28 0z" fill="#ffe27a" ${S} stroke-width="3"/>`,
    helper: `<rect x="14" y="20" width="36" height="28" rx="8" fill="#f2a65a" ${S}/><path d="M16 22l2-14 10 10M48 22l-2-14-10 10" fill="#f2a65a" ${S} stroke-width="3"/><rect x="12" y="10" width="40" height="10" rx="5" fill="#a8e6cf" ${S} stroke-width="3"/><circle cx="25" cy="33" r="3" fill="${K}"/><circle cx="39" cy="33" r="3" fill="${K}"/><path d="M28 40q4 3 8 0" fill="none" ${S} stroke-width="3"/><path d="M20 48v8h24v-8" fill="#fff" ${S} stroke-width="3"/>`,
    gear: `<path d="M28 4h8l2 8 6 3 7-4 6 6-4 7 3 6 8 2v8l-8 2-3 6 4 7-6 6-7-4-6 3-2 8h-8l-2-8-6-3-7 4-6-6 4-7-3-6-8-2v-8l8-2 3-6-4-7 6-6 7 4 6-3z" fill="#d9c7f5" ${S}/><circle cx="32" cy="32" r="9" fill="#fff" ${S}/>`,
    bell: `<path d="M14 44c4-4 4-10 4-18a14 14 0 0 1 28 0c0 8 0 14 4 18z" fill="#ffd84d" ${S}/><circle cx="32" cy="50" r="6" fill="#ffd84d" ${S}/><path d="M32 8v4" ${S}/>`,
    clock: `<circle cx="32" cy="32" r="24" fill="#fff" ${S}/><path d="M32 18v15l10 6" fill="none" ${S}/>`,
    heart: `<path d="M32 54S8 40 8 24a12 12 0 0 1 24-4 12 12 0 0 1 24 4c0 16-24 30-24 30z" fill="#ff86b0" ${S}/>`,
    lock: `<rect x="12" y="28" width="40" height="28" rx="7" fill="#ffd84d" ${S}/><path d="M20 28v-6a12 12 0 0 1 24 0v6" fill="none" ${S} stroke-width="6"/><circle cx="32" cy="41" r="4" fill="${K}"/>`,
    check: `<circle cx="32" cy="32" r="24" fill="#3fa868" ${S}/><path d="M20 33l8 8 16-18" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>`,
    x: `<path d="M16 16l32 32M48 16L16 48" stroke="#fff" stroke-width="9" stroke-linecap="round"/>`,
    sparkle: `<path d="M32 4c3 16 12 25 28 28-16 3-25 12-28 28-3-16-12-25-28-28 16-3 25-12 28-28z" fill="#fff4b8" ${S}/>`,
    gift: `<rect x="8" y="24" width="48" height="12" rx="3" fill="#ff86cf" ${S}/><rect x="12" y="36" width="40" height="20" rx="3" fill="#ffb3c7" ${S}/><path d="M32 24v32" stroke="#ffe14a" stroke-width="8"/><path d="M32 24v32" ${S} stroke-width="0"/><path d="M32 24c-6-12-18-10-14-2 2 3 8 2 14 2 6 0 12 1 14-2 4-8-8-10-14 2z" fill="#ffe14a" ${S} stroke-width="3"/>`,
    jar: `<rect x="14" y="16" width="36" height="42" rx="10" fill="#e8f7ff" ${S}/><rect x="18" y="8" width="28" height="10" rx="4" fill="#a8e6cf" ${S} stroke-width="3"/><circle cx="26" cy="44" r="7" fill="#ffc94d" ${S} stroke-width="3"/><circle cx="38" cy="40" r="7" fill="#ffc94d" ${S} stroke-width="3"/><circle cx="32" cy="50" r="6" fill="#ffc94d" ${S} stroke-width="3"/>`,
    queue: `<circle cx="16" cy="22" r="8" fill="#ffd9b8" ${S} stroke-width="3"/><circle cx="48" cy="22" r="8" fill="#ffd9b8" ${S} stroke-width="3"/><path d="M4 50c0-10 5-16 12-16s12 6 12 16zM36 50c0-10 5-16 12-16s12 6 12 16z" fill="#a8e6cf" ${S} stroke-width="3"/><circle cx="32" cy="26" r="10" fill="#ffd9b8" ${S}/><path d="M18 58c0-12 6-18 14-18s14 6 14 18z" fill="#ffb3c7" ${S}/>`,
    tools: `<rect x="6" y="24" width="52" height="30" rx="6" fill="#8fd3fe" ${S}/><path d="M22 24v-6a4 4 0 0 1 4-4h12a4 4 0 0 1 4 4v6" fill="none" ${S}/><rect x="6" y="32" width="52" height="6" fill="#4fb4f0" stroke="${K}" stroke-width="3"/><rect x="28" y="30" width="8" height="10" rx="2" fill="#ffd84d" ${S} stroke-width="3"/>`,
    dice: `<rect x="8" y="8" width="48" height="48" rx="12" fill="#fff" ${S}/><circle cx="22" cy="22" r="4" fill="${K}"/><circle cx="42" cy="22" r="4" fill="${K}"/><circle cx="32" cy="32" r="4" fill="${K}"/><circle cx="22" cy="42" r="4" fill="${K}"/><circle cx="42" cy="42" r="4" fill="${K}"/>`,
    arrow: `<path d="M20 6h24v26h12L32 58 8 32h12z" fill="#ffd84d" ${S}/>`,
    friends: `<circle cx="22" cy="22" r="10" fill="#ffd9b8" ${S}/><circle cx="44" cy="24" r="9" fill="#ffd9b8" ${S}/><path d="M4 56c0-12 8-20 18-20s18 8 18 20z" fill="#8fd3fe" ${S}/><path d="M34 56c0-10 4-18 12-18s14 6 14 18z" fill="#a8e6cf" ${S}/>`,
    music: `<path d="M24 46V14l28-6v32" fill="none" ${S} stroke-width="5"/><ellipse cx="18" cy="48" rx="8" ry="6" fill="#d9c7f5" ${S}/><ellipse cx="46" cy="42" rx="8" ry="6" fill="#d9c7f5" ${S}/>`,
    speaker: `<path d="M8 24h12l14-12v40L20 40H8z" fill="#d9c7f5" ${S}/><path d="M42 22q6 10 0 20M48 16q10 16 0 32" fill="none" ${S}/>`,
    hand: `<path d="M24 34V12a5 5 0 0 1 10 0v16-4a5 5 0 0 1 10 0v6a5 5 0 0 1 10 0v12c0 10-6 18-18 18-8 0-12-4-16-10l-8-12a5 5 0 0 1 8-6z" fill="#fff" ${S}/>`,
    crown: `<path d="M8 22l12 10 12-18 12 18 12-10-4 28H12z" fill="#ffd84d" ${S}/><rect x="12" y="48" width="40" height="8" rx="3" fill="#ffae1f" ${S}/>`,
    eye: `<path d="M4 32s10-16 28-16 28 16 28 16-10 16-28 16S4 32 4 32z" fill="#fff" ${S}/><circle cx="32" cy="32" r="9" fill="#8fd3fe" ${S}/><circle cx="32" cy="32" r="3" fill="${K}"/>`,
    burr: `<circle cx="32" cy="32" r="12" fill="#b98a5c" ${S}/><path d="M32 8v10M32 46v10M8 32h10M46 32h10M15 15l7 7M42 42l7 7M49 15l-7 7M22 42l-7 7" ${S} stroke-width="3"/>`,
    mud: `<path d="M8 40c0-10 8-14 14-12 2-8 12-12 18-6 8-2 16 4 14 12 6 4 2 14-6 14H16c-6 0-8-4-8-8z" fill="#7a5c40" ${S}/><circle cx="24" cy="38" r="3" fill="#9a7a58"/><circle cx="40" cy="34" r="4" fill="#9a7a58"/>`,
    water: `<path d="M32 6C24 20 14 30 14 40a18 18 0 0 0 36 0c0-10-10-20-18-34z" fill="#8fd3fe" ${S}/><path d="M24 40a8 8 0 0 0 8 8" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>`,
    nails: `<path d="M14 40c0-10 8-16 18-16s18 6 18 16-8 16-18 16-18-6-18-16z" fill="#ffb3c7" ${S}/><path d="M18 26l-4-12M28 22l-2-12M38 22l2-12M46 26l4-12" ${S} stroke-width="5"/><path d="M18 26l-4-12M28 22l-2-12M38 22l2-12M46 26l4-12" stroke="#fff" stroke-width="2" stroke-linecap="round"/>`,
    tangle: `<path d="M10 40c8-20 16 10 24-6s12 14 20-4M10 28c10-14 18 10 26-4s10 12 18 0" fill="none" ${S} stroke-width="5"/><path d="M10 40c8-20 16 10 24-6s12 14 20-4M10 28c10-14 18 10 26-4s10 12 18 0" fill="none" stroke="#c9a37b" stroke-width="2.5" stroke-linecap="round"/>`,
    smell: `<path d="M18 52c-8-8 8-14 0-24s6-16 0-22M34 52c-8-8 8-14 0-24s6-16 0-22M50 52c-8-8 8-14 0-24s6-16 0-22" fill="none" ${S} stroke-width="5"/><path d="M18 52c-8-8 8-14 0-24s6-16 0-22M34 52c-8-8 8-14 0-24s6-16 0-22M50 52c-8-8 8-14 0-24s6-16 0-22" fill="none" stroke="#a6d16a" stroke-width="2.5" stroke-linecap="round"/>`,
    wet: `<path d="M20 8c-6 10-10 16-10 22a10 10 0 0 0 20 0c0-6-4-12-10-22zM44 22c-6 10-10 16-10 22a10 10 0 0 0 20 0c0-6-4-12-10-22z" fill="#8fd3fe" ${S}/>`,
    bow: `<path d="M32 32L10 18c-6 4-6 24 0 28zM32 32l22-14c6 4 6 24 0 28z" fill="#ff86b0" ${S}/><circle cx="32" cy="32" r="7" fill="#ffb3c7" ${S}/>`,
    play: `<path d="M20 12l32 20-32 20z" fill="#7be85a" ${S}/>`,
    hourglass: `<path d="M16 6h32M16 58h32M20 6c0 16 24 16 24 26S20 42 20 58M44 6c0 16-24 16-24 26s24 10 24 26" fill="#fff4dd" ${S}/><path d="M24 52h16l-8-10z" fill="#ffc94d"/>`,
  };
  window.icon = function (name, extra = '') {
    const body = ICONS[name];
    if (!body) throw new Error('no icon ' + name);
    return `<svg class="ic ${extra}" viewBox="0 0 64 64" aria-hidden="true">${body}</svg>`;
  };
  // <i data-ic="coin"></i> becomes the icon
  function fillIcons(root) {
    root.querySelectorAll('[data-ic]').forEach((el) => {
      el.outerHTML = window.icon(el.dataset.ic, el.className || '');
    });
  }

  // ---------- scale ----------
  const DESIGN = { x: 1280, y: 720 };
  function layout() {
    const w = window.innerWidth, h = window.innerHeight;
    let s = Math.min(w / DESIGN.x, h / DESIGN.y);
    s = Math.min(Math.max(s, 0.75), 1.3);
    if (touch) s = Math.max(s, 0.75);
    const stage = document.getElementById('stage');
    stage.style.width = w / s + 'px';
    stage.style.height = h / s + 'px';
    stage.style.transform = `scale(${s})`;
    document.documentElement.style.setProperty('--s', s);
    document.body.dataset.scale = s.toFixed(3);
    // short screens (phones held sideways) get the compact layouts, like Scale.isShort
    document.body.classList.toggle('short', h / s < 560);
  }

  function chrome() {
    const stage = document.getElementById('stage');
    stage.insertAdjacentHTML('beforeend',
      '<div class="rbx-topbar" data-rbx><i></i><i></i></div><div class="rbx-stick" data-rbx></div><div class="rbx-jump" data-rbx></div>');
  }

  // <x data-only="a b"> stays only in states a and b
  function pickState() {
    const st = document.body.dataset.state || '';
    document.querySelectorAll('[data-only]').forEach((el) => {
      if (!el.dataset.only.split(/\s+/).includes(st)) el.remove();
    });
  }

  window.addEventListener('DOMContentLoaded', () => {
    pickState();
    fillIcons(document);
    chrome();
    layout();
  });
  window.addEventListener('resize', layout);
})();
