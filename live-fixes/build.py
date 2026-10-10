# Builds live-fixes/index.html: the Live Site Fixes Doc (items 1-25, rechecked 11 Oct)
# plus new findings and the 9 Oct polish review. Run: python3 -I build.py
import html, os

V2 = "https://atienzaveejay.github.io/ugc-breakouts-v2/"
U3 = V2 + "ub-3/app.html"
DOC = "https://docs.google.com/document/d/1Be5sm_H_oVBx_5a__ytGc9H6-RlKbzsbAzo7jrgCoPY/edit"
HOWTO = "https://docs.google.com/document/d/1Gkhq7KIne1rpBlTxj9PtsrFIsCj4gX5qtotu7rs_B-c/edit"

LIVE, PART, FIXED, NOT, NEW = "live", "part", "fixed", "notchecked", "new"
LABEL = {LIVE: "Still live 11 Oct", PART: "Partly done", FIXED: "Fixed", NOT: "Not rechecked", NEW: "New 11 Oct"}

# (no, title, status, check note, reproduce, build, type, links[(label,url)], images[file])
ITEMS = {
"bugs": ("Bugs, fix first", [
 (1, "Share: Copy gives a link that 404s", LIVE,
  "Checked 11 Oct: with the note “Check out this hook”, Copy put the link, two line breaks and the note on the clipboard.",
  "Signed in. Open any analyzed video, tap Share, type a note, tap Copy new link, paste into a new tab. The page 404s because the note is part of the address.",
  "Copy puts the URL only on the clipboard. The note already shows on the shared page. (Share screen copy handler: url + \"\\n\\n\" + note.)",
  "BUG", [], ["bug1-1-share-with-note.jpg", "bug1-3-pasted-link-404.jpg"]),
 (2, "Processing: UGC Breakouts in the top bar does nothing", LIVE,
  "Checked 11 Oct: tapped the logo during a search, nothing happened. In the code the Processing screen sets the logo with no link.",
  "Signed in. Run a search. While Processing shows, tap “UGC Breakouts” in the top bar.",
  "Tapping it goes to Home (/).", "BUG", [], ["today-processing.jpg"]),
 (3, "Video analysis: the search bar sends you Home", LIVE,
  "Checked 11 Oct: the top bar “Search” on an analysis links to /?focus=1.",
  "Signed in. Open any video analysis and tap the search bar in its top bar.",
  "Replace it with the UGC Breakouts logo, linked to Home.", "BUG", [], ["bug3-1-analysis-topbar.jpg"]),
 (26, "Video analysis stuck on “Building your creative strategy…”", NEW,
  "Found 11 Oct: Analyze video on @.xoxogabby (rhode holiday set) was still on this message 10 minutes later, also after reloads.",
  "Signed in. Run a search, open a video that isn't analyzed yet, tap Analyze video, wait.",
  "Check the analysis job for this video. If it fails, show an error and give the analysis back, so a user isn't charged for nothing.", "BUG", [], []),
 (27, "Shared page shows the sender's full email", NEW,
  "Found 11 Oct: the shared page shows the sender's first name followed by their full email address in brackets, then “sent you a breakout”.",
  "Signed in. Share any analyzed video and open the link.",
  "Show first name and last initial only (agreed 15 Sept), e.g. “Veejay A. sent you a breakout”. Never the email.", "BUG", [], []),
]),
"build": ("Ready to build", [
 (4, "Videos play with sound on", PART,
  "11 Oct: Processing examples now play with sound (muted=0). Results, Top Breakouts and analysis players not rechecked.",
  "Signed in. Tap any video to play it.", "Everywhere a video plays. A video started by a tap plays with sound.", "DEV", [], []),
 (5, "Same top bar on every screen", LIVE,
  "11 Oct: still differs. Processing has Back, logo and Pro; an analysis has Search, nav and Pro; Results cuts the logo to “UGC B” and adds the search term.",
  "Signed in. Go through Home, Processing, Results, an analysis and Library.",
  "Logo top left (goes Home), menu top right, no “Pro” tag. On UB 3.0 the menu is the bottom bar.", "DEV",
  [("UB 3.0 bottom bar", U3 + "#home-new")], []),
 (6, "Breakout Score info icon", PART,
  "11 Oct: an analysis now has a “What is Breakout Score?” button, but its text still uses the follower count definition (item 25). Results cards not rechecked.",
  "Signed in. Open Results or an analysis and look at the Breakout Score.",
  "An (i) next to every score with the one line definition. Lester sends the formula in plain words, Veejay writes the copy.", "DEV + COPY", [], []),
 (7, "Processing: example videos open full screen", LIVE,
  "Checked 11 Oct: the example plays inside its small tile (96 by 160), not full screen.",
  "Signed in. Start a search and tap an example video.", "Tapping an example opens it full screen with sound on.", "DEV", [], ["today-processing.jpg"]),
 (8, "Home: no dropdown on the search box", NOT, "",
  "Signed in. On Home, tap the search box.", "No suggestions dropdown when the box is selected.", "DEV", [], []),
 (9, "Home: recent searches vs suggestions", PART,
  "11 Oct: they are two rows now. The labels are “Try a product, style, or tag” and “Recent · opens results”.",
  "Signed in, with past searches. Look under the search box on Home.",
  "Label the recent row “Recent search terms”.", "DEV", [("UB 3.0 Home", U3 + "#home-busy")], []),
 (10, "Home: rename Library", LIVE, "11 Oct: the Home section is still “Library” with 2 videos.",
  "Signed in. Scroll Home to the Library section.", "“Library” becomes “Recent videos analyzed” and shows more videos.", "DEV",
  [("UB 3.0 Home", U3 + "#home-busy")], []),
 (11, "Home: more suggested terms", NOT, "",
  "Signed in. On Home, tap More suggestions.", "Brings more terms, based on the user's past searches where possible.", "DEV", [], []),
 (12, "Top Breakouts: confirm before analyzing", LIVE,
  "11 Oct: the confirm text isn't in the live code. Not tapped, since a tap uses an analysis.",
  "Signed in. Open Top Breakouts and tap a video.", "Ask first: “Analyze this video? Uses 1 analysis.”", "DEV",
  [("Design (v2)", V2 + "#top-confirm")], []),
 (13, "Sales page: hero copy", LIVE, "11 Oct: still “Find Viral Breakouts.” with “An app for TikTok creators”.",
  "Signed out. Open ugcbreakouts.com.", "“Find Viral TikTok Breakouts”. Remove “An app for TikTok creators”.", "COPY", [], ["m-out-home.jpg"]),
]),
"design": ("Designed, then to Lester", [
 (14, "Menu and quick access", LIVE, "11 Oct: not on the live site.",
  "Signed in. Open the menu.", "A bottom bar on phone: Home, Top, Library (Searches, Bookmarked, Analyzed inside), Account.", "DESIGN",
  [("UB 3.0 bottom bar", U3 + "#home-new"), ("Hamburger, not chosen", U3 + "#nav-alt")], []),
 (15, "Several searches and analyses at once", PART,
  "11 Oct: Library now shows “In progress… 4 more searches running” and a “breakouts are ready” banner. Home has no running list yet.",
  "Signed in. Start two searches and analyze a video, then go to Home and Library.",
  "Home lists Ready first, then running ones with progress. Analyzing shows in Library. A bar follows the user while a search runs.", "DESIGN",
  [("UB 3.0 Home", U3 + "#home-busy"), ("Search follows", U3 + "#browsing"), ("Library", U3 + "#library")], []),
 (16, "Processing: how-to video", LIVE, "11 Oct: not on the live site.",
  "Signed in, new account. Run the first search.", "A short how-to video on the first search screen, in place of Browse while you wait.", "DESIGN + VIDEO",
  [("UB 3.0 first search", U3 + "#first-wait"), ("How-To Video Doc", HOWTO)], []),
 (17, "Processing: what an analysis looks like", LIVE, "11 Oct: tapping an example only plays it.",
  "Signed in. On Processing, tap an example video.", "Show a sample analysis so users see what they'll get.", "DESIGN", [], []),
 (18, "Video analysis: shot list and Try these", LIVE,
  "11 Oct: Try these are still labels with reasons, not lines a creator can say.",
  "Signed in. Open a few analyses and scroll to Try these and the shot list.", "Real hook lines, and a richer shot list (design plus the prompt behind it).", "DESIGN + DEV", [], ["m-detail.jpg"]),
 (19, "Better 404 page", LIVE,
  "Checked 11 Oct, signed in: still “This page slipped off the radar”, then a redirect after 7 seconds.",
  "Open any wrong address.", "UGC Breakouts branded: one headline, the search box, the bar to get anywhere.", "DESIGN",
  [("UB 3.0 404", U3 + "#notfound")], []),
 (20, "Top Breakouts: cards, categories, filters", LIVE, "11 Oct: cards still differ from Results.",
  "Open Top Breakouts.", "Cards match Results. More categories. The agreed sorts and filters.", "DESIGN",
  [("Design (v2)", V2 + "#top")], ["m-top.jpg"]),
 (21, "Sales page refresh", LIVE, "11 Oct: The real problem, One search one video and You pitch brands are unchanged.",
  "Signed out. Scroll the sales page.", "New background, better visuals for The real problem and How it works, rewrite One search one video, rewrite or drop You pitch brands.", "DESIGN + COPY", [], ["m-out-example.jpg"]),
]),
"found": ("Found by Veejay", [
 (22, "Top Breakouts: nearly every score reads 100", LIVE,
  "11 Oct: 50 of the first 60 show 100, the other 10 show 99. Search results look right (100 down to 26).",
  "Open Top Breakouts and look at the scores.", "Check whether the score caps out in this feed.", "BUG", [], ["item22-top-scores.jpg"]),
 (23, "Sales page: example searches repeat the same reasons", NOT, "",
  "Signed out. Tap each example search in One search, one video.", "Each example gets its own reasons.", "COPY", [], []),
 (24, "Top Breakouts: “No preview” on every card", FIXED,
  "Checked 11 Oct: every card shows its thumbnail. Nothing to build.", "", "", "BUG", [], []),
 (25, "Breakout Score: the formula and its copy still use follower count", LIVE,
  "11 Oct: the info text still reads “views relative to follower count, engagement, and how recently the video was posted”, and the numbers follow it. A mousepad video at 730 times its creator's usual views scores 62, while a dog video at 260 times scores 91, because the score leans on followers.",
  "Compare any result's score with the creator's usual views on their TikTok profile. Test cases: @tulip6942 (desk essentials) 730x, score 62; @winston.cavapoo (dog car seat) 260x, score 91; @kenyewest (costco finds) 3,700x, score 79.",
  "Score the video against its own account, as agreed: usual views = median views of the creator's 15 latest non-pinned posts, leaving this one out. Then a 0 to 100 scale, for example 25 × log10(views ÷ usual views), capped at 100, so 10x = 25, 100x = 50, 1,000x = 75 and 10,000x = 100. On the test cases above that gives 72, 60 and 89, in the same order as the multiples, and it spreads the Top Breakouts scores out (item 22). The 60+ breakout line (5 Oct) needs a recheck on the new scale. Then use the agreed line wherever the score is explained.", "BUG + COPY", [], []),
]),
}

# polish review, 9 Oct, grouped by screen: (screen, before img, after img, [(text, tag, live11)])
POLISH = [
 ("Processing and Ready", "today-ready.jpg", None, [
  ("Ready is a full screen stop with one button before the results. UB 3.0 replaces it with a toast and keeps people where they are.", "POLISH", True),
  ("The “See breakouts” label is dark text on the coral button. Every other filled button uses white.", "POLISH", True),
  ("Example breakouts all show 100 (item 22).", "REPEAT", True)]),
 ("Video detail", "m-detail-unanalyzed.jpg", "after-1-detail.jpg", [
  ("Analyze video is the one filled button, in the bottom bar. Save and Share become icons.", "POLISH", False),
  ("Cut “See why this video broke out” and its line. The button carries the action.", "SUBTEXT", True)]),
 ("Video analysis", "m-detail.jpg", "after-2-analysis.jpg", [
  ("Cut “What worked in this clip, plus lines you can try.”", "SUBTEXT", True),
  ("Cut the gray note under the Shot list. It repeats What you can do next.", "REPEAT", True),
  ("What you can do next becomes a white card with numbered badges, not a red block.", "POLISH", True),
  ("Shot list times in the app font.", "POLISH", False),
  ("Shot list stops at 0:30 on a 1:29 video.", "ASK", False)]),
 ("Results", "m-results.jpg", "after-3-results.jpg", [
  ("Cut the search term chip on every thumbnail.", "REPEAT", True),
  ("Logo cuts to “UGC B” on phone.", "POLISH", True),
  ("Filter row cuts “Past 7 days” mid word. Fade the last chip.", "POLISH", False),
  ("Blank beige thumbnails while loading. Add a loading state.", "POLISH", False),
  ("Desktop: tall gap between stats and buttons.", "POLISH", False)]),
 ("Home, signed in", "m-home-in.jpg", None, [
  ("Cut “Search a product or format to remake”. The placeholder says it.", "SUBTEXT", True),
  ("Cut “· opens results” and “Open ›”.", "REPEAT", True),
  ("“GRWM” and “get ready with me” both suggested.", "REPEAT", True)]),
 ("Library", "m-library.jpg", None, [
  ("Cut the “RECENT” label over the only list.", "REPEAT", True),
  ("Videos tab repeats the Analyzed tab. UB 3.0 has one Library with Searches, Bookmarked and Analyzed.", "REPEAT", False),
  ("Each search row has a chevron and a bookmark. Keep the bookmark.", "POLISH", False)]),
 ("Account", "m-account.jpg", None, [
  ("Logout becomes a quiet “Log out” text link.", "POLISH", True),
  ("“Renews Oct 5, 2026” shows after that date. Check the renewal.", "DEV", False)]),
 ("Affiliate", "m-affiliate.jpg", None, [
  ("Cut the three step tiles. The button and card already say it.", "REPEAT", True),
  ("Shorten to “Bring TikTok UGC creators to Breakouts.”", "SUBTEXT", False)]),
 ("Top Breakouts", "m-top.jpg", None, [
  ("Category label on some cards only. All or none.", "POLISH", False),
  ("The All feed leads with pranks and storytime, not product videos.", "ASK", False)]),
 ("Sales page, signed out", "m-out-signup.jpg", None, [
  ("Free terms said four times. Say them once, in pricing.", "REPEAT", False),
  ("Two email forms at the bottom. Drop the “Weekly viral digest” box (its placeholder is you@brand.com).", "POLISH", True),
  ("Lip oil example shows the wrong thumbnail. Use the @softfocus.kai frame.", "POLISH", False),
  ("Header “Try for free” touches the right edge on phone.", "POLISH", False),
  ("Three labels for one action: Try for free, Start free, Continue with Google.", "ASK", False)]),
 ("Sign in", "m-out-auth.jpg", None, [
  ("Example card reads “1 followers”.", "POLISH", False),
  ("“beat its account size” frames the score by size. Same fix as item 25.", "LOCK", False)]),
 ("Footer pages", "m-out-contact.jpg", None, [
  ("Terms and Privacy say “Viral Video Finder” in the body.", "LOCK", True),
  ("Contact: tab title “Contact Viral Video Finder”, and the AI Analysis “unlimited access” line.", "LOCK", True),
  ("Blog: VVF, YouTube Shorts, Instagram Reels and outlier in the intro and byline.", "LOCK", False),
  ("Footer Pricing links to “#vvf-pricing”, and /pricing is a 404.", "POLISH", True)]),
]

e = html.escape
def links(ls): return "".join(f'<a class="lk" href="{e(u)}" target="_blank" rel="noopener">{e(l)} ↗</a>' for l, u in ls)
def imgs(fs): return "".join(f'<a href="img/{f}" target="_blank"><img src="img/{f}" alt="" loading="lazy"></a>' for f in fs)

def item(it):
    no, title, st, check, rep, build, typ, ls, ims = it
    body = ""
    if check: body += f'<p class="chk">{e(check)}</p>'
    if rep or build:
        body += '<div class="two">'
        if rep: body += f'<div><h4>How to reproduce</h4><p>{e(rep)}</p></div>'
        if build: body += f'<div><h4>What to build</h4><p>{e(build)}</p></div>'
        body += '</div>'
    if ls: body += f'<div class="lks">{links(ls)}</div>'
    if ims: body += f'<div class="shots">{imgs(ims)}</div>'
    return (f'<article class="it {st}" id="item-{no}"><header><span class="no">{no}</span><h3>{e(title)}</h3>'
            f'<span class="ty">{e(typ)}</span><span class="pill {st}">{LABEL[st]}</span></header>{body}</article>')

counts = {k: 0 for k in LABEL}
for _, (_, its) in ITEMS.items():
    for it in its: counts[it[2]] += 1

sections = ""
for key, (name, its) in ITEMS.items():
    sections += f'<section id="{key}"><h2>{e(name)} <small>{len(its)}</small></h2>' + "".join(item(i) for i in its) + "</section>"

pol = ""
for screen, before, after, rows in POLISH:
    li = "".join(f'<li><span class="tg">{t}</span><span>{e(x)}</span>{"<em>still live 11 Oct</em>" if lv else ""}</li>' for x, t, lv in rows)
    pics = imgs([before] + ([after] if after else []))
    cap = '<p class="cap">Before' + (', then our mock' if after else '') + '</p>'
    pol += f'<article class="ps"><div><h3>{e(screen)}</h3><ul>{li}</ul></div><div class="shots sm">{pics}{cap}</div></article>'

npol = sum(len(r) for *_, r in POLISH)

page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>UB Live Site Fixes</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600&display=swap">
<style>
:root{{--bg:#F4F0EC;--card:#fff;--ink:#171312;--mid:#6E6460;--hair:#E4DCD5;--coral:#E2384D;--teal:#0B7B7F;--teal-bg:#E4F4F4;--gold:#8A6D10;--gold-bg:#F7F1DE;--red-bg:#FBE3E6;--gray-bg:#EEE9E4;--mono:"JetBrains Mono",ui-monospace,Menlo,monospace}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#141110;--card:#1E1A18;--ink:#F1ECE8;--mid:#A89E99;--hair:#332C29;--coral:#FF6B7C;--teal:#5ED6D9;--teal-bg:#173233;--gold:#E8C766;--gold-bg:#352B12;--red-bg:#3D1C22;--gray-bg:#2A2421}}}}
:root[data-theme="dark"]{{--bg:#141110;--card:#1E1A18;--ink:#F1ECE8;--mid:#A89E99;--hair:#332C29;--coral:#FF6B7C;--teal:#5ED6D9;--teal-bg:#173233;--gold:#E8C766;--gold-bg:#352B12;--red-bg:#3D1C22;--gray-bg:#2A2421}}
*{{box-sizing:border-box}}html,body{{margin:0}}
body{{background:var(--bg);color:var(--ink);font:15px/1.55 "Plus Jakarta Sans",system-ui,sans-serif;-webkit-font-smoothing:antialiased}}
.wrap{{max-width:980px;margin:0 auto;padding:40px 16px 80px}}
h1{{font-size:34px;letter-spacing:-.035em;line-height:1.1;margin:0 0 10px}}
.lead{{color:var(--mid);max-width:680px;margin:0 0 22px}}
.lead a,.lk{{color:var(--teal);font-weight:700;text-decoration:none}}
nav.toc{{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 14px}}
nav.toc a{{background:var(--card);border:1px solid var(--hair);border-radius:999px;padding:6px 14px;color:var(--ink);text-decoration:none;font-weight:700;font-size:14px}}
.tally{{display:flex;flex-wrap:wrap;gap:6px 18px;color:var(--mid);font-size:13.5px;margin:0 0 30px}}
.tally b{{color:var(--ink)}}
h2{{font-size:22px;letter-spacing:-.025em;margin:42px 0 14px;display:flex;align-items:baseline;gap:10px}}
h2 small{{font:600 13px var(--mono);color:var(--mid)}}
.it{{background:var(--card);border:1px solid var(--hair);border-radius:16px;padding:16px 18px;margin:0 0 12px}}
.it.fixed{{opacity:.72}}
.it header{{display:flex;flex-wrap:wrap;align-items:center;gap:8px 10px}}
.no{{font:600 13px var(--mono);background:var(--gray-bg);border-radius:7px;padding:2px 8px}}
.it h3{{margin:0;font-size:16.5px;letter-spacing:-.01em;flex:1 1 260px}}
.ty{{font:600 11px var(--mono);color:var(--mid)}}
.pill{{font-size:12px;font-weight:700;border-radius:999px;padding:3px 10px;white-space:nowrap}}
.pill.live{{background:var(--red-bg);color:var(--coral)}}.pill.part{{background:var(--gold-bg);color:var(--gold)}}
.pill.fixed{{background:var(--teal-bg);color:var(--teal)}}.pill.notchecked{{background:var(--gray-bg);color:var(--mid)}}
.pill.new{{background:var(--coral);color:#fff}}
.chk{{margin:10px 0 0;font-size:14px;color:var(--mid)}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:12px}}
.two h4{{margin:0 0 3px;font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--mid)}}
.two p{{margin:0;font-size:14.5px}}
.lks{{display:flex;flex-wrap:wrap;gap:6px 16px;margin-top:10px;font-size:14px}}
.shots{{display:flex;gap:10px;margin-top:12px;overflow-x:auto}}
.shots img{{height:260px;width:auto;border-radius:10px;border:1px solid var(--hair);display:block}}
.ps{{background:var(--card);border:1px solid var(--hair);border-radius:16px;padding:16px 18px;margin:0 0 12px;display:grid;grid-template-columns:1fr auto;gap:18px}}
.ps h3{{margin:0 0 8px;font-size:16.5px}}
.ps ul{{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:7px}}
.ps li{{display:grid;grid-template-columns:72px 1fr;gap:4px 10px;font-size:14.5px}}
.ps li em{{grid-column:2;font-style:normal;font-size:12px;font-weight:700;color:var(--coral)}}
.tg{{font:600 10.5px var(--mono);color:var(--mid);padding-top:3px}}
.shots.sm{{flex-wrap:wrap;align-content:flex-start;max-width:300px;margin-top:0}}
.shots.sm img{{height:220px}}
.cap{{flex-basis:100%;margin:2px 0 0;font-size:12px;color:var(--mid)}}
img.tall{{width:150px!important;object-fit:cover;object-position:top}}
footer{{margin-top:40px;color:var(--mid);font-size:13px}}
@media (max-width:700px){{h1{{font-size:28px}}.two{{grid-template-columns:1fr}}.ps{{grid-template-columns:1fr}}.shots.sm{{max-width:none}}.shots img{{height:220px}}}}
</style></head><body><div class="wrap">
<h1>UGC Breakouts: live site fixes</h1>
<p class="lead">For Lester. Items 1 to 25 are from Ivan's 1 Oct review of ugcbreakouts.com plus four found while checking. Every item was rechecked on the live site on 11 Oct, signed in on a Pro account, and two new bugs came out of that. The polish review at the bottom is the smaller copy and layout list. The <a href="{DOC}" target="_blank" rel="noopener">Doc version ↗</a> has the same items 1 to 25.</p>
<nav class="toc"><a href="#bugs">Bugs</a><a href="#build">Ready to build</a><a href="#design">Designed</a><a href="#found">Found by Veejay</a><a href="#polish">Polish review</a></nav>
<p class="tally"><span><b>{counts[LIVE]}</b> still live</span><span><b>{counts[PART]}</b> partly done</span><span><b>{counts[FIXED]}</b> fixed</span><span><b>{counts[NEW]}</b> new</span><span><b>{counts[NOT]}</b> not rechecked</span></p>
{sections}
<section id="polish"><h2>Polish review <small>{npol}</small></h2>
<p class="lead">Veejay, 9 Oct, rechecked 11 Oct where marked. Ivan's two notes: “there seems to be something missing, more polish?” and “too many subtext and repeating elements on some pages.” Tags: SUBTEXT and REPEAT are cuts, POLISH is a layout or style change, LOCK breaks a product rule, ASK needs a call.</p>
{pol}</section>
<footer>Live site checked 11 Oct 2026 at 390 by 844, signed in on Pro, plus signed out for the sales page. Price is $49 a month.</footer>
</div><script>document.querySelectorAll(".shots img").forEach(function(i){{function f(){{if(i.naturalHeight>2.1*i.naturalWidth)i.classList.add("tall");}}if(i.complete)f();else i.addEventListener("load",f);}});</script></body></html>'''

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
open(out, "w", encoding="utf-8").write(page)
print("wrote", out, len(page)//1024, "KB", counts, "polish", npol)
