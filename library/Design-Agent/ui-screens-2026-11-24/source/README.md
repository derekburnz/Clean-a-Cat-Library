# Clean a Cat screen mockups

HTML mockups of the screens the game will very likely need, whichever loop Derek picks. They are drafts for looks and
layout, not a locked design. Owner: Design-Agent. Plans: issues #5 (first session) and #9 (UI layout).

## How a screen is built
- One HTML file per screen, using `kit.css` (tokens and parts) and `kit.js` (scaling, icons, Roblox's own UI drawn on top).
- Lay out in **design pixels on a 1280 x 720 canvas**. `kit.js` scales the stage like the asset library's `Scale.luau`:
  `scale = clamp(min(w / 1280, h / 720), 0.75, 1.3)`, touch screens never under 0.75. A small phone (667 x 375) is
  therefore 889 x 500 design pixels; `body.short` is set when the design height is under 560 (phones held sideways).
- Roblox's own UI is drawn for you: the menu buttons at the top left (184 x 58 real px) and on touch the thumbstick
  and jump button. Never put anything under them. Use `calc(58px / var(--s))` for the top bar's height in design pixels.
- `<meta name="states" content="a,b">` lists a screen's variants; `?state=a` sets `body[data-state="a"]`.
- Mark everything a player can press with `data-tap`. Put scrolling lists in `.scroll`.
- Icons: `<i data-ic="coin"></i>` (the list is in `kit.js`). Pictures: `img/` (Model-Agent's see-through cat portraits and tool icons, the `_ink`
  outlined versions and helper portraits).
- Fonts: Fredoka One for titles, buttons and numbers, Nunito for body words. No third font (the UI gate allows two).

## The look
- Words on the world (HUD numbers, praise) are white with an ink outline (`.outlined`), never in a box. Only things you
  can press look like buttons.
- Windows: cream body, ink outline, a lilac-to-pink title band with a round badge, a red X at the top right. Only the X
  (or the window's own action button) closes a window. No window opens by itself.
- Buttons: the asset library's three-colour chunky buttons (`.btn.green`, `.sky`, `.gold`, `.berry`, `.purple`,
  `.ghost`, `.off`). Green is the main action; grey `.off` is anything you cannot afford or use yet.
- Rarity: Common grey, Uncommon green, Rare blue, Epic purple, Legendary gold. Odds are always shown on anything random.
- Notifications: any "Notify me" bell (the Builder's) and its "Bell is on" state stay hidden unless the server says
  the player may get experience notifications. Players under 13 never see the opt-in prompt, so they never see the bell.
- Young audience: no fake timers, no fake discounts, no pressure words, nothing "limited".
- Words: never under 14 real px. `kit.js` raises any label that would scale under 14, like a UITextSizeConstraint with
  MinTextSize 14 on every label in the build. Cat names fit at up to 11 letters; coin counts over 999,999 show short
  (1.2M, 3.4B).

## Check
```
node check.mjs [--screen name] [--profile smallphone] [--out dir]
```
Opens every screen and state at small phone, phone, Galaxy A06, tablet, 4:3 iPad, desktop and console sizes, saves a
picture of each and fails on: taps under 44 px on touch (36 with a mouse), words under 9 px, anything off screen or
under Roblox's menu buttons, buttons under the thumbstick or jump button, buttons on top of each other, words cut off,
a third font. Words under 14 px are listed as notes. Default output: `shots/` (not committed). Phone and desktop
pictures of the 2026-11-24 drafts are in `docs/concepts/clean-a-cat/ui-2026-11-24/`.
