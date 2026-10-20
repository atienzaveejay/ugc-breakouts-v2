# Builds live-fixes/index.html (one table for Lester) and live-fixes/fixes.csv (paste into a Sheet tab).
# Rechecked on ugcbreakouts.com 20 Oct 2026. Old 19 Oct page: index.html.bak-1020 / build.py.bak-1020.
# Run: python3 -I build.py
import csv, html, os

HERE = os.path.dirname(os.path.abspath(__file__))
IMG_URL = "https://atienzaveejay.github.io/ugc-breakouts-v2/live-fixes/img/"
CHECKED = "20 Oct 2026"

# (area, what's wrong + steps, expected, [screenshots], priority, old item no. or "New")
FIXES = [
 ("Video analysis",
  "Analysis never finishes. Run a search, open a video that isn't analyzed, tap Analyze video. Today @byharleen (rhode holiday set) sat on “Building your creative strategy…” for 11+ minutes. The 11 Oct one (@.xoxogabby) now reads Failed in history, but its page just shows Analyze video again with no message, and the analysis was still taken from the count.",
  "Analysis finishes in about 30 seconds. If it fails: say so on the page, offer Retry, and give the analysis back.",
  ["oct20-in-analyzing.jpg", "oct20-in-analysis-failed.jpg"], "Blocker", "26"),
 ("Share",
  "Copied link 404s. Open any analyzed video, tap Share, add a note, tap Copy, paste into a new tab. The clipboard gets the link, two line breaks, then the note, so the pasted address is wrong.",
  "Copy puts only the link on the clipboard. The note already shows on the shared page.",
  ["oct20-in-share-copy.jpg", "oct20-in-share-pasted-404.jpg"], "Blocker", "1"),
 ("Shared page",
  "Shared page shows the sender's full email. Share any video and open the /s/ link. It reads “First name (email) sent you a breakout”, to anyone with the link.",
  "First name and last initial only, e.g. “Alex R. sent you a breakout”. Never the email.",
  ["oct20-in-shared-email.jpg"], "Blocker", "27"),
 ("Breakout Score",
  "Score is still based on follower count. Tap “What is Breakout Score?” on any analysis: “views relative to follower count, engagement, and how recently the video was posted”. Same text on the sales page, /top-breakouts and /find-breakouts.",
  "Score against the account's own usual views (median of its 15 latest non-pinned posts, leaving this one out). Example scale: 25 × log10(views ÷ usual views), capped at 100. Copy: “A score from 0 to 100. It shows how much a video beat the average of what that account usually gets.”",
  ["oct20-in-score-info.jpg"], "High", "25"),
 ("Top Breakouts",
  "Every score reads 100. Signed in, open /top: 60 of 60 cards show 100. Signed out /top-breakouts: 12 of 12. Search results look right (95 down to 69).",
  "Scores spread out like they do in search results. Likely fixed by the score change above. Check after it.",
  ["oct20-in-top-app.jpg"], "High", "22"),
 ("Top Breakouts (public page)",
  "“No preview” on every card. Signed out, open ugcbreakouts.com/top-breakouts: all 12 cards have no thumbnail (the page data sends no image). The signed-in /top feed shows its thumbnails fine.",
  "Public strip uses the same thumbnails as /top, with a saved frame as fallback.",
  ["oct20-out-top-breakouts.jpg"], "High", "24"),
 ("Old library pages",
  "Old Viral Video Finder library is still live. Signed out, /bookmarks and /my-library open an empty library instead of Sign in. Signed in, /my-library and /my-library/analysis-history show the old app: “Outlier score 2518x”, “Ask Sparky”, a Custom Search tab bar, and “Saved videos 0” above 9 videos. The 404 page's “Open Bookmarks” button goes here.",
  "Redirect /bookmarks, /my-library and its sub-pages to /library (signed in) or Sign in (signed out). No “Outlier” anywhere.",
  ["oct20-in-oldlibrary.jpg", "oct20-out-bookmarks.jpg"], "High", "29"),
 ("Account",
  "Renewal date is in the past. Account on 20 Oct, still on Pro, says “Renews Oct 5, 2026”.",
  "Show the real next renewal date from Stripe. If the plan didn't renew, Pro should end.",
  ["oct20-in-account.jpg"], "High", "New"),
 ("Processing",
  "Logo does nothing. Start a search. While it runs, tap “UGC Breakouts” in the top bar. Nothing happens (the logo is set with no link on this screen).",
  "Logo goes Home.",
  ["oct20-in-processing.jpg"], "Normal", "2"),
 ("Processing",
  "Wait time copy is wrong. The screen says “Usually 15 seconds to a minute.” Today's search took 2:34. The 9 searches before it took 1:10 to 4:52.",
  "“Usually 1 to 3 minutes.” Or make searches faster.",
  ["oct20-in-processing.jpg"], "Normal", "New"),
 ("Video analysis",
  "Top bar search box sends you Home. Open any analysis (or Share) and tap Search in the top bar. It links to /?focus=1.",
  "UGC Breakouts logo in its place, linked Home.",
  ["oct20-in-analysis-top.jpg"], "Normal", "3"),
 ("Library vs Results",
  "Search counts don't match. Library and Home say “heatless curls · 140 breakouts” and “costco finds · 98 breakouts”, but Results stops at 60.",
  "Same number in both places: count what Results can show, or let Results go past 60.",
  ["oct20-in-library.jpg"], "Normal", "New"),
 ("404 page",
  "Old 404. Open any wrong address: “This page slipped off the radar”, buttons to Dashboard and the old Bookmarks, then a redirect after 7 seconds.",
  "UGC Breakouts 404: one line, the search box, a Home link. No auto redirect, no Bookmarks link.",
  ["oct20-out-this-does-not-exist.jpg"], "Normal", "19"),
 ("Footer pages",
  "Old name and other platforms. Terms, Privacy and Suggestions say “Viral Video Finder”. Contact, Suggestions and Blog have it in the tab title. Blog mentions YouTube Shorts, Instagram Reels, “outlier” and VVF. Footer Pricing links to /#vvf-pricing (and /pricing is a 404).",
  "“UGC Breakouts” everywhere, titles included. TikTok only, “breakout” not “outlier”. Pricing link goes to the pricing section.",
  ["oct20-out-terms.jpg", "oct20-out-blog.jpg"], "Normal", "28"),
 ("Legal pages",
  "Effective date is always today. Terms, Privacy, DPA and Security read “Effective date: Oct 20, 2026” today and read Oct 19 yesterday. DPA and Security also say they're drafts pending legal review.",
  "A fixed effective date per page. Ivan decides if the DPA and Security drafts stay public.",
  ["oct20-out-dpa.jpg"], "Normal", "30"),
 ("Sign up / Log in",
  "Old product copy. /register: “Search trending creators, preview viral videos, and track what's working in your niche - all in one place.” /login: “unlock creator search, playback, and exports from the dashboard.” Neither page has a tab title.",
  "Both use “Find Viral Breakouts. Get the creative strategy to make your own.” Titles “Sign up · UGC Breakouts” and “Log in · UGC Breakouts”.",
  ["oct20-out-register.jpg", "oct20-out-login.jpg"], "Normal", "31"),
 ("Contact",
  "“Unlimited” line. /contact says “If you're asking about AI Analysis, tell us what unlimited access would help you do.” Pro is 100 analyses.",
  "Cut the line, or “If you're asking about video analyses, tell us what you'd use more of.”",
  ["oct20-out-contact.jpg"], "Normal", "32"),
 ("Sales pages (phone)",
  "Page scrolls sideways. At phone width the header “Try for free” button runs about 18px past the right edge on /, /top-breakouts and /find-breakouts.",
  "Header fits the screen at 360px and up. No sideways scroll.",
  ["oct20-out-home.jpg"], "Normal", "New"),
]

FIXED = [
 ("Videos play with sound on", "4", "every player (Results, Top, analysis, Library) now loads with sound on (muted=0)."),
]

V31_LINE = "17 more items (menu, top bar, Home sections, how-to video, Top Breakouts cards, sales page refresh and the rest of Ivan's 1 Oct list) wait for the UB 3.1 build. No live work on those."

ORDER = {"Blocker": 0, "High": 1, "Normal": 2}
FIXES.sort(key=lambda f: ORDER[f[4]])  # stable: keeps the order above inside each priority
counts = {p: sum(1 for f in FIXES if f[4] == p) for p in ORDER}
n_new = sum(1 for f in FIXES if f[5] == "New")

# CSV for a Sheet tab
with open(os.path.join(HERE, "fixes.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["No.", "Area", "What's wrong (steps to reproduce)", "Expected", "Screenshot", "Priority", "Status", "Ref"])
    for i, (area, wrong, exp, shots, pri, ref) in enumerate(FIXES, 1):
        w.writerow([i, area, wrong, exp, "\n".join(IMG_URL + s for s in shots), pri, "Open", "New" if ref == "New" else "Old #" + ref])
    w.writerow([])
    w.writerow(["", "Already fixed", "; ".join(f"{t} (old #{r}): {n}" for t, r, n in FIXED)])
    w.writerow(["", "Waiting for 3.1", V31_LINE])

e = html.escape
rows = ""
for i, (area, wrong, exp, shots, pri, ref) in enumerate(FIXES, 1):
    title, _, rest = wrong.partition(". ")
    pics = "".join(f'<a href="img/{s}" target="_blank"><img src="img/{s}" alt="" loading="lazy"></a>' for s in shots)
    refl = "new" if ref == "New" else f"#{ref}"
    rows += (f'<tr class="p-{pri.lower()}"><td class="no">{i}</td><td class="pri"><span>{pri}</span></td>'
             f'<td class="area">{e(area)}<small>{refl}</small></td>'
             f'<td><b>{e(title)}.</b> {e(rest)}</td><td class="exp">{e(exp)}</td><td class="shots">{pics}</td></tr>')
fixed_li = "".join(f"<li><b>{e(t)}</b> (old #{r}): {e(n)}</li>" for t, r, n in FIXED)

page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>UB Live Site Fixes</title>
<style>
:root{{--bg:#fff;--ink:#16181A;--mid:#5F6368;--hair:#E3E5E8;--head:#F5F6F7;--blk:#B3261E;--blk-bg:#FDECEA;--hi:#8A5300;--hi-bg:#FFF3DC;--nm:#3C4043;--nm-bg:#EEF0F2}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#151719;--ink:#ECEDEE;--mid:#A3A8AD;--hair:#2C3034;--head:#1D2023;--blk:#FF8A80;--blk-bg:#3A1A18;--hi:#F2C46D;--hi-bg:#352812;--nm:#C9CDD1;--nm-bg:#24282C}}}}
:root[data-theme="dark"]{{--bg:#151719;--ink:#ECEDEE;--mid:#A3A8AD;--hair:#2C3034;--head:#1D2023;--blk:#FF8A80;--blk-bg:#3A1A18;--hi:#F2C46D;--hi-bg:#352812;--nm:#C9CDD1;--nm-bg:#24282C}}
*{{box-sizing:border-box}}html,body{{margin:0}}
body{{background:var(--bg);color:var(--ink);font:14px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}}
.wrap{{max-width:1240px;margin:0 auto;padding:32px 16px 64px}}
h1{{font-size:24px;margin:0 0 8px}}
.sum{{max-width:760px;margin:0 0 6px;font-size:15px}}
.meta{{color:var(--mid);margin:0 0 20px;font-size:13px}}
table{{width:100%;border-collapse:collapse;border:1px solid var(--hair)}}
th{{background:var(--head);text-align:left;font-size:12px;color:var(--mid);font-weight:600;padding:8px 10px;border-bottom:1px solid var(--hair)}}
td{{padding:10px;border-bottom:1px solid var(--hair);vertical-align:top}}
td.no{{font-variant-numeric:tabular-nums;color:var(--mid);width:36px}}
td.pri span{{display:inline-block;font-size:12px;font-weight:600;padding:2px 8px;border-radius:4px}}
.p-blocker td.pri span{{background:var(--blk-bg);color:var(--blk)}}
.p-high td.pri span{{background:var(--hi-bg);color:var(--hi)}}
.p-normal td.pri span{{background:var(--nm-bg);color:var(--nm)}}
td.area{{width:130px;font-weight:600}}td.area small{{display:block;font-weight:400;color:var(--mid)}}
td.shots{{width:150px;white-space:nowrap}}
td.shots img{{height:110px;width:auto;border:1px solid var(--hair);border-radius:4px;margin:0 4px 4px 0}}
h2{{font-size:16px;margin:28px 0 6px}}
ul{{margin:0;padding-left:18px}}
p.v31{{margin:0;color:var(--mid)}}
@media (max-width:820px){{
 table,thead,tbody,tr,td{{display:block;width:auto}}thead{{display:none}}
 tr{{border-bottom:1px solid var(--hair);padding:10px 4px}}td{{border:0;padding:3px 6px}}
 td.no,td.pri,td.area{{display:inline-block;width:auto}}td.shots{{white-space:normal}}
 td.exp::before{{content:"Expected: ";font-weight:600}}
 td.shots img{{height:150px}}td.shots a{{display:inline-block}}
}}
</style></head><body><div class="wrap">
<h1>UGC Breakouts: live site fixes</h1>
<p class="sum">{len(FIXES)} fixes for the live site, rechecked on ugcbreakouts.com on {CHECKED}, blockers first. Analysis not finishing, the broken share link and the email on the shared page come first. The rest are scoring, old pages and copy.</p>
<p class="meta">{counts["Blocker"]} Blocker · {counts["High"]} High · {counts["Normal"]} Normal · {n_new} new today. Checked signed in (Pro) and signed out, at phone width. Ref is the item number in the earlier list. Click a screenshot to open it full size.</p>
<table><thead><tr><th>No.</th><th>Priority</th><th>Area</th><th>What's wrong (steps to reproduce)</th><th>Expected</th><th>Screenshot</th></tr></thead>
<tbody>{rows}</tbody></table>
<h2>Waiting for UB 3.1</h2><p class="v31">{e(V31_LINE)}</p>
<h2>Already fixed</h2><ul>{fixed_li}</ul>
</div></body></html>'''

open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
print("wrote index.html + fixes.csv:", len(FIXES), "fixes", counts, "new", n_new)
