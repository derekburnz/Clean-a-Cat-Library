# Clean a Cat: UI research brief

Research for the Design-Agent, 2026-11-24. It covers what the UI should look like and how it must behave on a phone, where most Roblox sessions happen [48], so the screens listed in section 3 can be drafted.

**How to read the marks.** A number in brackets, such as [7], is a source in the list at the end. **[J]** is my judgment. **[P]** is a project file.

**Limit of this research.** Image and video hosts were blocked in this session, so I saw no screenshots or footage. Claims about a game's look come from written guides, Roblox's documents and Derek's playtest notes. Pull a reference frame before copying a pattern.

## 1. Conventions players expect

| Convention | Evidence | Use in Clean a Cat |
|---|---|---|
| Square menu buttons in a column on the left edge | Steal a Brainrot has four (Shop, Rebirth, Index, Codes) [23][24] | Build and Index, three at most [P4] |
| Money is an icon plus an outlined number with no plate | Bottom left in Steal a Brainrot, Grow a Garden and Capybara Onsen [24][25][P1] | Top right is fine [J]: a thumb covers the bottom left on a phone |
| Top centre holds the one current objective | Grow a Garden's "Talk to Sam!" banner [25], Roblox's layout course [4] | The goal line [P4] |
| Red square X at a window's top right, grey for unusable, a lock for locked, an unaffordable price in red | Roblox UI guide [1] | Use all four as they are |
| Green means buy with game money, and Robux buttons are a different colour | Grow a Garden: green coin button, purple Robux, blue Gift [25] | Robux actions never share the green |
| Rarity ladder grey, green, blue, purple, gold | The common order across games [29]; our swatches follow it [P2] | Show the rarity word with the colour [5][10] |
| A collection index with silhouettes, a counter, tabs and a progress bar to a reward | Steal a Brainrot's Index [23] | Section 3.5 |
| An "Odds" button in the shop header | Grow a Garden's seed shop [25]. Required for paid random items [7] | Section 3.10 |
| Floating world labels and a "Collect" amount over the thing itself | Steal a Brainrot [24] | Need icons, tip jar, chance board [P4] |
| Chunky rounded font with a dark outline | The repo's reference-frame comparison of three simulators [P3] | Section 2.4 |
| Praise words with a growing combo, then a star recap with coins and XP | My Pet Salon! [P1]. Dress To Impress pops stars with a sound per vote [28] | Sections 3.3 and 3.4 |
| Tutorial: dim the screen, outline the target, arrow, ground trail | Hello Kitty Cafe, in Roblox's onboarding guide [6]; My Pet Salon! [P1] | Section 3.13 |

Clarity beats decoration. Grow a Garden reached 3.2 million concurrent players while a reviewer wrote that it "didn't look particularly pretty" [27], and Roblox's course puts legibility ahead of looks [5].

## 2. Visual quality recipe

All sizes are for the smallest landscape phone, 667 x 375 [P3]. Roblox's top bar takes about 58 px (inferred from an example in [11], so measure it), which leaves about 317 px. Design windows to fit 290 px.

### 2.1 Shape [J]
- One radius scale: 8 (chips, badges), 12 (buttons, small cards), 16 (list rows, big cards), 22 (windows), full circle (HUD side buttons). A nested shape uses the outer radius minus the padding.
- Soft blocks to match the models [P2]: no sharp corners and no lines under 2 px.

### 2.2 Outline and depth [J]
- **Ink, not black.** Use one dark plum (about #3B2D45, the tone in the 11-23 mockup) for every outline and all dark text. Pure black looks harsh on pastel. Mud brown stays reserved for dirt [P2].
- Outline width: 3 px on buttons and cards, 4 px on windows, 2 px on chips.
- Bottom lip: 4 px on buttons, 6 px on windows, the fill colour darkened by about 25%. When pressed, the face moves down 3 px and scales to 0.96.
- Window shadow: ink at 25% opacity, offset 0 and 6 px, no blur. A soft shadow needs a 9-slice image [18].
- Outline only what can be pressed, plus the window itself [P3].

### 2.3 Colour and contrast
Ratios below are computed from the style guide's hex values [P2]. The targets are 4.5:1 for normal text and 3:1 for text of 24 px or more, or 18.5 px bold [44].

| Pair | Ratio | Rule |
|---|---|---|
| Ink on cream, mint, bubblegum, sky | 11.9, 9.0, 7.6, 7.8 | Ink text is safe on every pastel |
| White on mint, bubblegum, sky | 1.4, 1.7, 1.6 | White text always carries an ink outline. A wide outline counts as the background [44], so it reads as white on ink (12.8:1) |
| Gold #FFC94D on cream | 1.4 | Coin numbers are gold with an ink outline, never bare |
| Rarity colours as text on cream | 1.4 to 2.8 | Never use a rarity colour as text. Use a filled chip with ink text (4.3 to 8.3:1) |
| White on a pastel green button | 1.9 to 2.4 | Button labels are white with an ink outline, or ink with none |

- Mute the background and keep saturation for things that can be pressed [34].
- One accent per window (its header colour) plus the button meanings: green buy, red close, gold rare, grey disabled [P3][39].
- About 5% of people are colour-blind, so every colour meaning also has an icon or a word [10][5].

### 2.4 Type scale (px at 375 tall)
Apple's default is 17 pt with an 11 pt floor [35], Epic says text under 18 pt "reads poorly on a phone" [37], and Roblox says never under 9 [12]. The sizes below are my choice inside those limits [J].

| Role | Size | Outline when over the 3D world |
|---|---|---|
| Caption, badge count, "x2" | 14 | 2 |
| Body, descriptions | 18 | none (ink on a plate) |
| Button label, HUD number, row title | 22 | 2.5 |
| Goal line, card title | 24 | 2.5 |
| Window title | 28 | 3 |
| Praise word (combo number 44) | 36 | 4 |
| Hero: reveal name, star total | 44 to 48 | 4 |

Fonts: FredokaOne for titles, buttons and praise, and Builder Sans Bold for numbers and body [P4][J]. The current `client/UI/init.luau` uses GothamMedium and GothamBold, which Roblox deprecated [22].

### 2.5 Touch sizes
- 44 px is the floor [35]. Android says 48 with 8 between targets [45] and Roblox's course says 9 mm [5]. NN/g asks for 1 cm for adults and 2 cm for young children [32][30], and a centimetre is about 64 px on a phone.
- So: HUD and list buttons are 56 to 64 px. The main action on a card is at least 64 tall and 128 wide. The close X is 48 [J].
- Gaps of 12 px or more. No more than 5 or 6 live controls on screen at once [37].

### 2.6 Icons
- Simple shapes that read at 32 px, one family, one outline weight [5][P3]. No emoji or letters as icons [P3].
- Pair an icon with a word wherever there is room. Icons alone are ambiguous [39], and text alone fails non-readers [33].

### 2.7 Motion
- Things that appear ease out [40]. Windows open in 0.2 to 0.3 s and close in under 0.2 s [P3].
- "The more common an action, the simpler the juice" [40]: a scrub stroke gets a tiny effect and a rare cat the big one.
- Follow `GuiService.ReducedMotionEnabled`: snap, or fade instead of moving [10].

## 3. Per-screen notes

Every window is centred, at most 290 px tall, has one scroll list and an X at the top right, and is opened by the player [P3][P4].

**3.1 Main HUD.** Top left is Roblox's. Goal line top centre. Coins and stars top right. Up to three round 60 px buttons on the left edge with a label under each. Tool bar bottom centre [P4]. The centre stays empty [P3][4]. To win back the 58 px strip, put the coins and goal line in a second ScreenGui that uses `TopbarSafeInsets` [2][J], and test it on console, where a bug was reported [50]. Keep the left buttons in the upper half, clear of the thumbstick's touch area [P3]. References: Steal a Brainrot [24], Grow a Garden [25].

**3.2 Customer queue picker.** No source showed a multi-customer picker in a Roblox game, so this is [J]. Put it in the world first: a bubble over each waiting customer with the cat's face, a rarity chip and its dirt icons. Tapping the customer picks them, as My Pet Salon! allows [P1]. Small 3D targets are hard for children [30], so add a tray of up to four 72 px cards above the tool bar that mirrors the bubbles. If customers can leave, show patience as a ring that empties calmly, with no red flashing or countdown numbers (section 5). Reference: Animal Crossing Pocket Camp marks which visitors are ready [43].

**3.3 Wash step HUD.**
- Step counter top centre: "Step 1 of 3" at 24 px plus three pips and the step's icon. A bare number is not enough: seven-year-olds in testing did not link a "2" to the goal [31].
- Tool picker bottom centre, 60 px slots. The needed tool glows and locked ones are grey with a lock [P4][1].
- Praise pop-up: one at a time, upper centre, never under the finger. Word at 36 px and "x5" in its own label at 44 px. It pops in over 0.2 s, holds 0.5 s, fades, and takes no input. Short words only (Nice!, Great!, Awesome!) [J]. Reference: My Pet Salon! [P1].
- Gestures: a ghost hand shows the swipe, aim, pick or hold once per new step kind [P1]. Wrong moves get a visual hint, not an error message [33]. Swipes and taps are easy for under-nines and precise drags are not [30], so hit areas are generous. Lift a picked item, and the hold step's filling ring, above the finger so they stay visible [38].

**3.4 Recap card.** A centred card about 360 x 260. Three stars pop in 0.25 s apart with a rising sound, as Dress To Impress does per vote [28]. Under each star is a small icon for what earned it [J][31]. Then one row each for coins and XP, counting up over about 0.45 s [P3], with rows of zero hidden [P3]. Coins fly to the HUD counter [6]. One green "Next cat" button, 64 px tall, and a smaller Photo button. No countdown and no auto-advance: this is the natural place to stop [46]. Reference: My Pet Salon! [P1].

**3.5 Cat Index.** Use the widest window, about 570 px. Tabs down the left for sets. A grid of five 92 px cards. Unseen cats are silhouettes. A counter such as "12 / 40" at the top right. A progress bar along the bottom names the set reward [23]. Each card has a rarity frame and a chip with the rarity word. Show half of the next row so players see that it scrolls [33]. Reference: Steal a Brainrot [23].

**3.6 Rare cat reveal.** A short full-screen moment: silhouette, flash, then the cat on a sunburst with a name banner, a rarity chip and a "New!" stamp [J][P3]. Control returns in 2.5 s or on a tap. It is the brightest moment in the game [P2], so nothing else animates. With reduced motion it is a fade [10].

**3.7 Tool upgrade shop.** A list of 60 px rows: icon, name, level pips, one line with real numbers ("Scrubs 20% faster"), and a green price button of 96 x 48 on the right. Unaffordable is a grey button with the price in red [1], and a tap says how many coins are missing [P3]. Locked rows show the requirement in place of the button [24]. A maxed tool shows a grey "MAX" chip. References: Steal a Brainrot's tool shop [24], Grow a Garden's seed cards [25][26].

**3.8 Helper hire.** Three cards across, 150 px wide: portrait, one line on what the helper does, speed as pips, a price button. A hired helper shows a tick and "Working" [J]. Reuse one card component for helpers, tools and builds: consistency is what reads as polish [39][42]. Reference: My Pet Salon! [P1].

**3.9 Builder.** As planned [P4]: two sections with rows, a countdown on the running build, and grey rows that say why they wait. Timers are plain text with no pulsing, since timers already make players impatient [43]. A pay-to-skip button, if one ever exists, is never the largest [J]. Reference: Cats & Soup's upgrade menu [42].

**3.10 Odds board.** Section 5 has the rules. One row per rarity: colour chip, word, and a percentage right-aligned in Builder Sans at 22 px. Rows must total exactly 100% [7]. A "Details" button with the word on it opens every cat's chance; a bare (i) icon does not meet the rule [7]. A "Your luck now" line updates when stars change the chances [7]. Reference: Grow a Garden's Odds button [25].

**3.11 Settings.** One short list with the most-used items first [41]: music and sound sliders kept separate [10], then toggles with an icon, a word and an obvious on or off state [41]. Rows are 56 px. Nothing destructive.

**3.12 Toasts.** One at a time, under the goal line, with an icon and five words or fewer, for 2.5 s. They queue. None show while a window is open, apart from warnings [P3]. For rewards, prefer flying coins and a badge on the button over a banner [6].

**3.13 Tutorial pointer.** Dim to about 55% with a rounded hole 8 px larger than the target, an ink-and-white outline, and a 52 px arrow that bobs 8 px once a second [J]. The player taps the real button [P3]. Captions are six words or fewer at 22 px, one step at a time, because text-only prompts get skipped [6][36]. The ground trail is chevrons flowing to the goal with a bobbing arrow over it [P1]; it suggests and never forces [6]. Show extra hints only to players who stall (Roblox's example waits 11 seconds) [6].

## 4. Roblox technical rules

- **Insets.** Interactive UI goes in a ScreenGui with `CoreUISafeInsets`. Use `None` only for backdrops, because text there can sit under the notch [2][P3]. Read `GuiService.TopbarInset` and listen for changes; never hard-code it [11][21].
- **Touch zones.** The default thumbstick and jump button take the bottom corners [3]. Measure `TouchGui` at runtime [P3].
- **TextScaled.** It ignores TextSize, stops at 100, and can shrink text until it is unreadable. Roblox prefers `AutomaticSize` [12]. If you use it, add a `UITextSizeConstraint` [P3]. TextScaled labels do not follow the player's text size setting [11][10].
- **UIStroke.** On a label it outlines the letters. Set `ApplyStrokeMode = Border` to outline the box instead [13]. `StrokeSizingMode.ScaledSize` makes thickness follow the font size or the parent, and it has been live since December 2025 [14][15]. Keep under about 300 strokes on screen for weak phones [15]. Strokes do not affect layout, so leave room [15]. Never tween a text stroke's thickness [13]. Test ScaledSize under UIScale and in BillboardGuis, where bugs were reported [49].
- **UIGradient.** On a TextLabel or TextButton it tints the text too, so put the label on a child [P3]. Animate Offset or Rotation, not the colours [16]. Avoid it on labels that use the old TextStroke properties [16].
- **Frames or images.** Start with Frame, UICorner, UIStroke and a lip frame, which need no uploads [J]. Move to 9-slice sprites for soft shadows later [18]. Put small images on one sheet; most need 256 px or less [19].
- **CanvasGroup.** It costs texture memory, clips its children (outlines included) and turns blank past the memory cap. Use it for fades on fixed-size windows only [17][P3].
- **Gamepad.** Every control is reachable with four directions, select and back, focus stays inside the open window and returns on close [20][P3]. Use `ViewportDisplaySize` for TV sizing [11][20].

## 5. Kid and policy rules

- **Odds.** If a random item can be bought with Robux, or with currency Robux can buy, every outcome and its numerical chance is shown before purchase. Percentages total exactly 100%, luck changes update the display, and the "Details" control is visible with a word on it [7][8]. Check `ArePaidRandomItemsRestricted` per player [7]. Free random rewards are exempt [7], but the house rule (CLAUDE.md rule 9) shows chances anyway.
- **No fake urgency.** Roblox bans false time pressure, disguised ads and tricking users into purchases in notifications [9]. Apply the same to every screen [J]: no "limited" tags, no nagging timers, no discount strikes [P4].
- **Notifications.** The opt-in prompt never appears for under-13s [9]. The Builder's "Notify me" bell must hide when `CanPromptOptInAsync` is false, and play must never require opting in [9].
- **Tip jar.** Roblox allows Robux tip jars only when the user understands they get nothing back [8]. Ours holds game coins from customers, so it must never show a Robux prompt [J].
- **Low reading age.** Icon first, then words and sound [33]. Children take instructions literally and hold little in mind, so give one at a time [31].
- **Stopping points and links.** Give natural places to pause [46]; the recap card is ours. No outside links on any screen [8].

## 6. Pitfalls to avoid

1. Shrinking a desktop window to the phone. A 0.6 scale turns a 58 px X into 34 px [P3]. Reflow instead.
2. White, gold or rarity-coloured text on pastel with no outline (section 2.3).
3. Buttons in the lower corners, or anything under the top bar.
4. A plate behind every number, cards inside cards, outlines on things that cannot be pressed [P3].
5. A pop-up for every event. Children want feedback on every action [34], so give it in the world and on the counter.
6. Precise drags and two-hand moves in wash steps [30].
7. Uploading UI art under a personal account [P3].
8. Signing off from the Studio canvas alone. Test over bright and dark scenes on a real small phone [5][P3].

## Sources

1. https://create.roblox.com/docs/production/game-design/ui-ux-design
2. https://create.roblox.com/docs/reference/engine/enums/ScreenInsets.md
3. https://create.roblox.com/docs/ui/position-and-size
4. https://create.roblox.com/docs/en-us/tutorials/curriculums/user-interface-design/wireframe-your-layouts
5. https://create.roblox.com/docs/tutorials/curriculums/user-interface-design/choose-an-art-style
6. https://create.roblox.com/docs/production/game-design/onboarding-techniques
7. https://create.roblox.com/docs/production/monetization/paid-random-items
8. https://about.roblox.com/en-au/community-standards
9. https://create.roblox.com/docs/production/promotion/experience-notifications
10. https://create.roblox.com/docs/production/publishing/accessibility.md
11. https://create.roblox.com/docs/reference/engine/classes/GuiService.md
12. https://create.roblox.com/docs/reference/engine/classes/TextLabel.md
13. https://create.roblox.com/docs/reference/engine/classes/UIStroke.md
14. https://create.roblox.com/docs/reference/engine/enums/StrokeSizingMode.md
15. https://devforum.roblox.com/t/studio-beta-uistroke-improvements-scaling-offsets-and-more/3958036
16. https://create.roblox.com/docs/reference/engine/classes/UIGradient.md
17. https://create.roblox.com/docs/reference/engine/classes/CanvasGroup.md
18. https://create.roblox.com/docs/ui/9-slice.md
19. https://create.roblox.com/docs/performance-optimization/improve.md
20. https://create.roblox.com/docs/production/publishing/console-guidelines
21. https://devforum.roblox.com/t/get-ready-for-updated-experience-controls/3163001
22. https://devforum.roblox.com/t/introducing-builder-font-deprecating-gotham-and-arial/2868222 (title only; the page body would not load)
23. https://allthings.how/?p=329377 (Steal a Brainrot Index)
24. https://allthings.how/?p=328991 (Steal a Brainrot beginner guide)
25. https://allthings.how/?p=330478 (Grow a Garden beginner guide)
26. https://beebom.com/grow-a-garden-seed-shop-guide
27. https://www.pcgamer.com/games/survival-crafting/i-played-the-roblox-hit-thats-pulled-in-10-billion-visits-and-while-im-not-sold-on-it-i-can-see-how-its-cultivated-a-mass-following
28. https://roonby.com/2024/10/30/dress-to-impress-dti-voting-system-guide-all-you-need-to-know/
29. https://tvtropes.org/pmwiki/pmwiki.php/Main/ColorCodedItemTiers
30. https://www.nngroup.com/articles/children-ux-physical-development/
31. https://www.nngroup.com/articles/kids-cognition/
32. https://www.nngroup.com/articles/touch-target-size/
33. https://developers.google.com/building-for-kids/designing-engaging-apps
34. https://www.smashingmagazine.com/2016/01/designing-apps-for-kids-is-not-childs-play/
35. https://developer.apple.com/design/human-interface-guidelines/designing-for-games
36. https://developer.apple.com/app-store/onboarding-for-games/
37. https://dev.epicgames.com/documentation/fortnite/designing-for-mobile-in-fortnite
38. https://blog.unity.com/en/games/mobile-ui-design-best-practices-part-1
39. https://www.gameanalytics.com/blog/how-to-make-your-game-ui-shine-and-increase-conversions
40. https://www.gameanalytics.com/blog/squeezing-more-juice-out-of-your-game-design
41. https://gdevelop.io/blog/borrowing-without-copying-ui
42. https://dev.to/jpdengler/exploring-the-charming-uiux-design-of-catssoup-3l9a
43. https://www.gamedeveloper.com/business/animal-crossing-pocket-camp-can-an-old-dog-learn-new-tricks-
44. https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
45. https://support.google.com/accessibility/android/answer/7101858
46. https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/age-appropriate-design-a-code-of-practice-for-online-services/13-nudge-techniques/
47. https://create.roblox.com/docs/en-us/tutorials/curriculums/user-interface-design/implement-designs-in-studio (background reading)
48. https://create.roblox.com/docs/input/mobile.md (most Roblox sessions are on mobile)
49. https://devforum.roblox.com/t/uiscale-scaling-a-text-with-scaled-size-uistroke-bug/4238464 and https://devforum.roblox.com/t/incorrect-behavior-of-scaledsize-mode-uistroke-in-billboardgui/4050010 (titles only)
50. https://devforum.roblox.com/t/screenguiscreeninsets-topbarsafeinsets-is-incorrect-on-consoles/4111410 (title only)

Project files:
- [P1] `/mnt/project-files/Planning-Agent/playtest-notes.md` (Derek's notes on My Pet Salon! and Capybara Onsen)
- [P2] `docs/art/style-guide.md` and `assets/clean-a-cat/blender/palette.py`
- [P3] repo skills `ui-review`, `roblox-gui` and `roblox-ui-genre-studs`
- [P4] `/mnt/project-files/Design-Agent/first-session-2026-11-23/ui-layout-plan.md`

**Not found or not checked.** No written source described the HUDs of Adopt Me, Pet Simulator 99, Fisch, Bee Swarm Simulator, Clean Everything, Toca Boca games, Project Makeover, Hay Day, Unpacking or Good Pizza, Great Pizza in usable detail, so none is cited as evidence. Whether UICorner costs more than a 9-slice image could not be checked: the DevForum threads would not load.
