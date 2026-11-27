# Sync-Agent overnight Studio results, 2026-11-27 (local Studio, iphone_13 or desktop frame, unsaved places)
Pictures: draft docs PRs 1012 (qa/night3-2026-11-27) and 1014 (qa/carrier-float-871); copies in shared Gameplay-Engineer/dropoff-2026-11-27 and Motion-FX-Agent/carrier-float-871.

- 991 recap, 844315b: PASS. 9 rows, Next cat 109x45 px, bottom y 304.5 of 330.
- 871 walk-in, 208dc9d (PR 1008): PASS. All counter places N of N parts, 0 off mats; StreamingEnabled false (not a cause).
- 871 leave, 208dc9d: FAIL (PackedCat 16.4 studs off at the pavement). 7e033d1 (PR 1010): PASS, 1.47 studs, N of N.
- 871 carrier float, c2eeb78: PASS. Hand Grip to Carrier Grip 0.00 at 22 samples.
- 884 helpers fetch: 844315b FAIL (all walks to the pavement spot, Jo crossed ThirdTub); 49f4f89 (PR 1009) lane crossed the Tools board; c2eeb78 (PR 1011) PASS: stop 2.6 behind the cat, 1.3 from counter edge, nothing solid crossed.
- 948 Stardust bows, 208dc9d: PASS (24 fits, no overlap with the wand).
- 883 Clover and Glitch portraits, c2eeb78: PASS (Success, drawn, silhouettes when unowned).
- 869 like how-to, fb23dab (PR 1013): PASS loop (grey ~0.9 s, pink ~1.2 s per 2.1 s), frame named Tap, Reduced Motion still and pink. Asset preload 403 under the moderation hold is not conclusive.
- 773 dev look, fb23dab: PASS bows (overhang of Golden/Royal wanted per Design), faces, window bow. Walk-out bow NOT CONCLUSIVE (served cats leave via going-home effect). 235 fps avg on desktop; real phone not tested.
- 40 first loop, fb23dab: PASS to the third customer at 6:11. Not reachable locally: brush table and dryer, VIP Room, rejoin and timers. Small note: after closing a recap one Take found no prompt; retry worked.
- 531 console: no errors from our scripts. Only local limits (ProfileStore, DataStore, MemoryStoreService publish) and rbxassetid://203785492 type mismatch x3 (not in repo, likely Studio test avatar).
- Seen: starter pack side ad shows a large sparkle picture filling the panel above "See the pack" (Design).
- Open: E on "Put in tub" did nothing 3x once (client RequestPlaceCat worked), not reproduced.
- Not testable from here: real phone, music, notifications, Finish now, likes, saves, rejoin, two players.
