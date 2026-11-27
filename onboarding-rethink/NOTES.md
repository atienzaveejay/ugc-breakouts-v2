# Onboarding rethink: notes for Ivan's 27 Nov DM

Prototype: `index.html` (review page with a jump bar and notes) wraps `app.html` (the clickable app at phone width). `data.js` holds the live onboarding props plus the sample breakouts. `live.css` is the live stylesheet as captured on 25 Nov, untouched.

Built only from Ivan's 27 Nov notes. Steps 2 to 7 run the live flow code from the 25 Nov capture unchanged. Analysis and the Script Writer are stand-ins marked "same as live".

## Each of Ivan's points, and what the prototype does

| Ivan wrote | Prototype |
|---|---|
| Q1: page 1 chips should be better thought out, each with an amazing top 5 | Same live page 1. The chips are now 6 formats and 4 products, each with its own hand-picked top 5 (sample data). The Hashtags row is dropped for now (see the chip list below). |
| "product review": the 5 videos given aren't the very best | Tapping Product review ends on a results page whose first 5 are the strongest for that topic, with the rest of the search after them ("See all 48"). |
| User has nothing to do while the first search runs: make top 5 to 10 breakouts available and prompt them to go there | After the questions, Home shows the running search with one button: "Watch top breakouts while you wait". It opens Breakouts with the top 6 for the same topic, ready right away. |
| (same point) make sure those videos are extremely relevant | The 6 shown match the topic of her search, not the general Top Breakouts list. |
| Return to results when the search is done | A bar at the top of Breakouts shows the search time. When it finishes it turns dark with "See results". Home shows the same "Your results are ready" block. |
| Library: move Searches to the left, unlock Searches only | Library tabs are now Searches, Analyzed, Saved, Scripts. Searches opens first and works on the free plan. The other three keep a small lock and show the live lock card. |
| Not a clear path from start to all features: each screen needs one clear next step | Each screen has one primary action: Start my search, then Watch top breakouts, then See results, then Analyze #1 (bar at the bottom of results), then Write a script, then the checklist's next task. |
| Task checklist: search, create script, analyze video, connect account, plus a few already-done steps | "Get started" on Home: Create your account (ticked), Tell us what you film (ticked after the questions), Search for breakouts, Write your first script, Analyze a video, Connect your TikTok. Count and segment bar at the top. The next task gets the one Start button. |
| Glowing button on features they haven't tried? | A soft pulsing ring (no neon, no bounce) on the Write a script card, the Script tab, the Analyze button on result #1, and the avatar (Connect). It goes away once the feature is used. Reduced motion shows a still ring. |

## Open questions (options only, not built)

**"Should we unlock all Library?"**
1. Unlock Searches only (what the prototype shows). Free users keep the searches they paid for with their 3 free credits. Analyzed, Saved and Scripts stay as reasons to upgrade.
2. Unlock all four tabs and keep the paywall on actions (searches, scripts, analyses). The Library then only holds what the free plan already let her make, so nothing is given away, and she never meets a locked screen in her own stuff.
3. Unlock Searches and Analyzed (both come out of free actions she already took), keep Saved and Scripts locked.

**"What other free features can we add? (light dev lift)"**
1. Hooks only, free: from any breakout, show the 3 hook options from the Script Writer's Choose a Hook step without writing the full script. Reuses an existing step.
2. Weekly Top Breakouts for her niche, free: the Breakouts page already ranks videos; filter it by the topics from onboarding step 2.
3. One free analysis per search: let her analyze the #1 result of each free search, so the checklist's Analyze step never hits a paywall.

Not checked: what the free plan includes today for analysis, saving and scripts. Please confirm before choosing.

## The chips, and why each one

Rule used: a chip stays only if it is something a UGC creator can film this week, and if it can have a hand-picked top 5. Sources are files already in the repo or the handover folder.

| Chip | Group | Why | Source |
|---|---|---|---|
| Product review | Formats | Ivan's own example. The most common paid UGC ask. | Live chip (`onboarding-live-2026-11-25/data.json`); "Honest review" format #6 in `research/hooks-formats-2026-11-02.md` |
| Unboxing | Formats | Easy to film with no talking, and named in TikTok Shop's own guide. | Live step 3 style option; format #9 in hooks-formats |
| GRWM | Formats | Live chip and a live style option. Fits beauty, the biggest niche in step 2. | Live chip; format #12 in hooks-formats; sample set in `top-breakouts/app-data.json` |
| Before and after | Formats | Clear payoff, works for home and beauty. Note the claim risk flagged in hooks-formats. | Live step 3 style option; format #10 in hooks-formats |
| Day in my life | Formats | Live chip. Works for any niche, so it suits creators who don't have a product yet. | Live chip ("Day in my life"); format #13 in hooks-formats |
| Storytime | Formats | Live chip and live style option. Talking head, no product needed. | Live chip; live step 3 option |
| Lip liner | Products | Kept from the live product chips; beauty is the largest niche. | Live chip |
| Self-tanner | Products | Kept from the live product chips; strong before-and-after visuals. | Live chip |
| Resistance bands | Products | Adds a fitness product so the products aren't all beauty. | `top-breakouts/app-data.json` (Fitness sample) |
| Closet organizer | Products | Adds a home product; "My closet is 4 feet wide" is already in the sample set. | `top-breakouts/app-data.json` (Home sample) |

Dropped from live: Moisturizer, Collagen powder, Shoes, Green screen, POV, and the whole Hashtags row (#UGCcreator, #TikTokMadeMeBuyIt, #TikTokShop, #SkinTok, #CleanTok, #MomTok, #FoodTok, #GymTok). Reason: they are broad, and broad tags like #UGCcreator mostly return videos about doing UGC, which makes a strong top 5 hard to pick. This is my call, not Ivan's. Two hashtags (for example #TikTokMadeMeBuyIt and #CleanTok) can come back if he wants them.

How the real top 5 could work (for Lester, not built): for each chip, someone runs the search, picks the 5 with the highest multiple over usual views that are clearly filmable, and pins them. Refresh weekly.

## Things to know before sharing

- All videos, view counts, usual views and handles are sample data written for the prototype (see the header of `data.js`). Handles are blurred on screen. No Score badges are shown. Thumbnails are the stock photos from `top-breakouts/assets/`.
- A typed search that doesn't match a chip falls back to a sample set in the prototype. In the app, typed searches can't have a hand-picked top 5.
- The prototype search takes 90 seconds (the live note says 1 to 2 minutes), but finishes 15 seconds after she opens Breakouts so the hand-back can be seen.
- I didn't add a "Write a script" button to breakout cards. The script step is reached from Analyze, Home and the Script tab, which already exist.
- Lock card copy: the live card says "Save breakouts and searches...". Since Searches is now free, the prototype drops "and searches". I'm not sure the lock card copy I used is current live copy (it comes from a 28 Oct audit screenshot).
- The Home layout is the live Home (pink Breakout Finder and teal Write a script cards, from the live CSS). The search block and the checklist sit above them.
- Desktop: the review page shows the phone-width app with notes beside it. The desktop app layout (sidebar) was not designed in this round.
