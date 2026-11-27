# Can the store art be uploaded by key? (2026-11-26 ET, Growth-Agent)
Derek, plan page 5:20 PM ET: "You should be able to do this with keys or use claude in chrome". Source: Roblox Creator Hub page "Manage experience icons and thumbnails" (create.roblox.com/docs/cloud/guides/experience-icons-and-thumbnails), read today. OFFICIAL unless marked.

## CORRECTION 2026-11-26 evening: the key route does NOT work for the page art (see the end of this file). The section below is what the docs page says; it was wrong for our experience pages.
## Answer (as the docs page reads): an Open Cloud key can do it
1. Upload each PNG: POST https://apis.roblox.com/assets/v1/assets, assetType Image, `groupId` for a group owned game (Creampuff Games), assetPrivacy OpenUse. Poll the operation until done and read the asset id. Moderation runs and the image shows only once approved.
2. Icon: PATCH https://apis.roblox.com/assets/v1/assets/{PlaceId}?updateMask=icon, body icon "assets/{id}". The icon must be square (a non square file is rejected); the 512 files are square.
3. Detail page thumbnails: PATCH .../assets/{PlaceId}?updateMask=previews, body previews list of {asset, altText}. Array order is the page order, and the call replaces the whole list, so send all four in Derek's order: 2, 1, 3, 5.
4. Home page thumbnails are a separate API (thumbnail-personalization-api, scopes universe.thumbnail:read and write). Order does not matter there, up to five. Roblox takes one main icon; the page I read has no alternate icon endpoint, so icon E (the alternate for Home tests) may only be settable in Creator Hub. NOT confirmed: say so rather than guess.
Key scopes: asset:read and asset:write on the game for icon and detail thumbnails.
Not read: size and format limits (they are on the Icons and Thumbnails best practice pages).

## Who does it
Our rule: Growth never dispatches upload workflows, and uploads go through Gameplay-Engineer's upload-asset workflow or a script run with the group key. Rule 18 in CLAUDE.md applies: after upload, check it loads on dev. Derek already allowed uploads to the group (2026-11-24) and now asks for this one; the coordinator decides the owner. Order for the PATCH: previews 2, 1, 3, 5, then icon A. Icon E waits on the alternate route. Record the minute of the change for the stats reads.
Also check the old Chrome blocker: it could only upload a screenshot, so the key route is the better one.

## Result of the live upload (Gameplay-Engineer, 5:44 PM ET, 22:44 UTC) and my first check
Icon A asset 92729298316581; thumbnails in order 2, 1, 3, 5: 105795079697238, 112653869263896, 79981284321647, 120549383496799. Both PATCH calls returned 200. Public read at about 5:50 PM ET (universe 10778773655): games media list empty, icon state Completed (cannot tell old from new, no asset id shown), thumbnail list shows one thumbnail only. So the four thumbnails are NOT visible yet: probably still in moderation or the previews write did not apply. Recheck in 30 to 60 minutes; if still one thumbnail, read previews back with readMask and ask Derek to look at the Thumbnails page. Icon E has no route.

## Chrome look, 2026-11-26 about 6:25 PM ET (Derek's signed in Creator Hub as Creampuff Games; no password or code touched)
- Place 79301459457383 (universe 10778773655), Thumbnails, Experience Detail Page tab: only "Auto-generated image". The four thumbnails are not listed there. Home Page tab: empty list. So the 5:44 PM PATCH either did not apply or the images are still pending and hidden. Public data agrees (one thumbnail).
- Icon page text did not render (the tab froze on screenshots); icon A not confirmed. Overview shows a grey placeholder icon.
- Game details: Description is 0/1000, empty. So "cat spa" text is not set on this game (issue 892).
- Icon E: Claude in Chrome's upload tool takes screenshots only, so it cannot pick icon-alternate-e-512.png (164 KB). Pasting the file through script would cost about 100k tokens. Not done. Issue 901.

## Key route failed (Gameplay-Engineer, 6:17 PM ET)
store-setup wrote to live place 79301459457383 and dev place 111265803618777; both PATCHes returned 200 but readMask previews,icon reads back empty (run 45910001445). The assets API fields seem to apply to Creator Store listings, not the experience page. So the page's icon and thumbnails need Creator Hub with a real file upload: Sync-Agent's PC session is doing it (live place, icon A, icon E if there is an alternate slot, four thumbnails in order). Group images already uploaded: icon 92729298316581, thumbnails 105795079697238, 112653869263896, 79981284321647, 120549383496799. Lesson: a docs page that says an API can do something is not proof; read it back.
