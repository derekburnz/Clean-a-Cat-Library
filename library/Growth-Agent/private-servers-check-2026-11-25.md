# Private servers: what Roblox's setting allows (2026-11-25 ET, Growth-Agent)

For issue #530. Derek: "6 and make private servers free with roblox plus or 100 robux to purchase". OFFICIAL = Roblox Creator Hub pages (create.roblox.com/docs/production/monetization/private-servers and .../roblox-plus), the Roblox Plus DevForum announcement (2026-04-10, updated 2026-04-30) and the Roblox newsroom post (2026-04-10). JUDGMENT = my call. The setting itself is Derek's to change.

## Short answer
Derek's wish is how Roblox already works. Set private servers to Requires Robux at 100 Robux. Roblox Plus subscribers then get paid private servers at no cost as a platform benefit. The game cannot set a price of 0 for some players only.

## What the pages say (OFFICIAL)
- Where: Creator Dashboard > Audience > Access Settings. "Enable Requires Robux" and enter an amount, or turn it off to make private servers free for everyone.
- One price per game, not per player. No option for "free for subscribers" as a creator price.
- Roblox Plus: "Roblox Plus subscribers get access to paid private servers at no cost." So a Plus player gets into our 100 Robux private server for free without us doing anything.
- Price is a monthly Robux fee (recurring), not a one time purchase. Changing the price cancels all active private server subscriptions and players are told by message.
- The game must be public first. Paid private servers cannot be on at the same time as paid access.
- No minimum or maximum price is stated on the pages I read.
- Under 13: "Players under the age of 13 may not be able to join private servers depending on their privacy and parental control settings."
- Creators can earn up to 100 Robux per Plus subscriber who spends at least 60 minutes a month in a paid private server that subscriber owns. Free private servers do not earn this.
- Plus has sign up rewards through MarketplaceService:PromptRobloxSubscriptionPurchase (up to 750 Robux per new subscriber, paid over three months), and `Player.HasRobloxSubscription` can read Plus status.

## What I recommend (JUDGMENT)
1. Set Requires Robux at 100 Robux. It matches what Derek asked and Plus players still play free. A free private server would earn nothing from Plus players.
2. Tell Derek it renews monthly. "100 Robux to purchase" is 100 Robux a month for non Plus players. If he wants a lower or one time cost, there is no such option in the setting.
3. Do not change the price after launch unless needed, since a change cancels every active private server.
4. Do not add a Plus sign up prompt for now. Many of our players are young and Roblox's rules for under 13 apply; revisit only if Derek asks.
5. Private servers are one player's friends in six spa slots; the visiting setting and the friend bonus work as in a public server.
6. Players under 13 who cannot join private servers should not be told they are missing anything; no prompts in the game about private servers.

Settings Derek changes himself: Access Settings > Requires Robux = on, 100; max players per server = 6 (his earlier answer).

## Update 2026-11-26 evening: Derek now says 25 (or 50)
Derek (plan page, 2026-11-26 5:20 PM ET): "Honestly 50, or 25 since there is no real benefit to being alone in your own server, give it free with robux plus". Planning-Agent is writing 25 a month into the design. Re-read of the two Creator Hub pages (private-servers, roblox-plus):
- OFFICIAL: no minimum or maximum price is stated, so 25 is not ruled out, but the pages also do not confirm it is allowed. The Access Settings field in the Creator Dashboard is the only proof; Derek sees it when he types the number. Plus page examples use 50, 60, 70, 100 and 200.
- OFFICIAL: the Plus free access does not depend on the price ("Subscribers get access to paid private servers at no cost").
- OFFICIAL: changing the price cancels every active private server subscription, with a message to each player. So pick once.
- OFFICIAL: the Plus payout depends on the price: 70 percent of the server price, up to 100 Robux per Plus subscriber who spends 60 minutes in their own paid private server in 30 days. At 25 that is about 17 Robux, at 50 about 35, at 100 the 70 percent share is 70. JUDGMENT: this is the cost of the lower price, small next to Derek's reason, so his 25 stands; say it once and do not reopen it.
- Group wall: Roblox retired community walls (Planning-Agent, 2026-11-26), so the wall lines in like-group-rewards-check, monetization-calls and owner-settings-list are void. Moderation of the group's forums, if he turns them on, is his.
