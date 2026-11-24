#!/usr/bin/env python3
"""Builds script-writer-flow/index.html: a clickable prototype of
Home v5 > Write a script pop-up > writing > script output (11 layouts).
Layout markup is pulled as-is from script-output-2026-11-25/index.html,
so the prototype stays identical to the reviewed mockups."""
import re, json, os, html

SRC = os.path.expanduser('~/Documents/Agentic System/ugc-breakouts-handover-2026-10-16')
OUT_SRC = os.path.join(SRC, 'script-output-2026-11-25/index.html')
HERE = os.path.dirname(os.path.abspath(__file__))

src = open(OUT_SRC).read()
css_out = re.search(r'<style>(.*?)</style>', src, re.S).group(1)

# --- pull every layout: label, scr inner, bar ---
blocks = re.findall(r'<div><div class="label">(\d+)\. ([^<]+)</div>\s*<div class="phone"><div class="scr"[^>]*>(.*?)</div><div class="bar">(.*?)</div></div>\s*<div class="note">', src, re.S)
layouts = {}
for num, label, inner, bar in blocks:
    n = int(num)
    if n == 0:
        shared = inner
        continue
    # drop the per-layout top/title/meta (the prototype renders one shared header)
    body = re.split(r'</div></div>\s*\n', inner, maxsplit=0)
    m = re.search(r'<div class="meta">.*?</div></div>\n', inner, re.S)
    head_end = m.end()
    meta = m.group(0)
    lay = re.search(r'<div class="tag lay">([^<]+)</div>', meta).group(1)
    fixed = re.search(r'<div class="tag len">([^<]+)</div>', meta)
    layouts[n] = {
        'label': label.strip(),
        'tag': lay,
        'fixedLen': fixed.group(1) if fixed else None,
        'body': inner[head_end:].strip(),
        'bar': bar.strip(),
    }
assert sorted(layouts) == list(range(1, 12)), sorted(layouts)

# shared top part (screen 0): Built from + 3 hook groups
hooks_html = shared[shared.index('<div class="from">'):].strip()

# hook pools for "3 new": only copy that already exists in the mockups
spoken_all = ["Watch what one coat does in daylight", "I keep this one in every bag", "This is the lip oil I reach for first",
              "Does this lip oil last from breakfast to dinner?", "How I get glossy lips that don't feel sticky.", "3 things I like about this lip oil."]
visual_all = ["Cap off, close to the mic", "Bare lips, then one swipe", "Swatch on the hand, then the lips",
              "Left side gloss, right side lip oil.", "Wand out, one slow swipe", "Press lips together, close up"]
text_all = ["POV: you found a lip oil that isn't sticky", "the only lip step I keep", "lip oil, one swipe, daylight",
            "glossy, not heavy", "no sticky feel", "nothing sticks"]

def scope(css, prefix):
    out = []
    for rule in re.findall(r'([^{}]+)\{([^{}]*)\}', css):
        sel, body = rule
        sel = sel.strip()
        if sel.startswith(':root') or sel == '*' or sel == 'body':
            continue
        sels = ','.join(prefix + ' ' + s.strip() for s in sel.split(','))
        out.append(sels + '{' + body + '}')
    return '\n'.join(out)

home_css = r'''
.logo{font-weight:800;font-size:17px}.logo b{color:#1FB2C2;font-weight:800}
.hi{font-size:14px;color:var(--mute);margin-top:10px}
h1{font-size:30px;font-weight:800;letter-spacing:-.8px;line-height:1.08;margin:4px 0 22px}
.card{border-radius:20px;padding:20px;margin-bottom:20px}
.card.p{background:var(--pink);border:1.5px solid var(--pinkb)}
.card.t{background:var(--teal);border:1.5px solid var(--tealb)}
.ct{font-size:20px;font-weight:800;letter-spacing:-.4px}
.cs{font-size:13px;color:var(--mute);margin:4px 0 14px}
.box{background:#fff;border-radius:14px;display:flex;align-items:center;padding:6px 6px 6px 14px;gap:10px;border:1.5px solid #fff}
.box.ton{border-color:var(--tealx)}
.box input{flex:1;min-width:0;font:inherit;font-size:15px;border:0;outline:0;background:transparent;color:var(--ink);font-weight:600}
.box input::placeholder{color:#9A918C;font-weight:400}
.go{width:38px;height:38px;border-radius:10px;display:grid;place-items:center;color:#fff;font-weight:800;flex:none;cursor:pointer}
.go.r{background:var(--red)}.go.g{background:var(--tealx)}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
.chip{background:#fff;border:1px solid var(--line);font-size:13px;font-weight:600;padding:6px 10px;border-radius:9px}
.chip.on{background:var(--tealx);color:#fff;border-color:var(--tealx)}
.alt{font-size:12.5px;color:var(--mute);margin-top:12px}.alt a{color:var(--ink);font-weight:700;text-decoration:underline;text-underline-offset:2px}
.sec{margin-top:2px}
.sh{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:8px}
.sh h2{font-size:18px;font-weight:800;letter-spacing:-.3px}.sh span{font-size:12px;color:var(--mute)}
.list{background:#fff;border-radius:16px;border:1px solid var(--line)}
.li{display:flex;align-items:center;gap:10px;padding:11px 14px;border-top:1px solid var(--line)}.li:first-child{border-top:0}
.n{width:18px;font-size:13px;font-weight:800;color:var(--mute)}
.lt{flex:1;font-size:15px;font-weight:700}.lm{font-size:12px;color:var(--mute);font-weight:500}
.up{font-size:12px;font-weight:700;color:#178A4C}
.nav{position:absolute;bottom:0;left:0;right:0;height:72px;background:#fff;border-top:1px solid var(--line);display:flex;justify-content:space-around;align-items:center;font-size:11px;font-weight:600;color:var(--mute);z-index:1}
.nav b{color:var(--ink)}
.sml{font-size:12.5px;font-weight:700;color:var(--mute);margin:14px 2px 6px}
.sml.s{font-size:11px;font-weight:600;color:#8C827D;letter-spacing:.1px}
.box.on{border-color:var(--red)}
.chip.add{border-style:dashed;color:var(--mute)}
.lift{position:relative;z-index:3}
.fhead{display:flex;justify-content:space-between;align-items:center}
.sug{background:#fff;border-radius:14px;border:1px solid var(--line);margin-top:10px}
.sg{display:flex;gap:10px;align-items:center;padding:11px 14px;border-top:1px solid var(--line);font-size:15px;cursor:pointer}.sg:first-child{border-top:0}
.sg em{font-style:normal;font-weight:800}.sg small{margin-left:auto;font-size:12px;color:var(--mute)}
.thumbs{display:flex;gap:8px;margin-top:8px}
.th{flex:1;height:128px;border-radius:12px;position:relative;overflow:hidden;cursor:pointer}
.th span{position:absolute;left:6px;bottom:6px;font-size:11px;font-weight:700;color:#fff;background:rgba(0,0,0,.55);padding:2px 6px;border-radius:6px}
.hnote{font-size:13px;color:var(--mute);margin:8px 2px 0;line-height:1.45}
.sec2{margin-top:26px}
.li,.chip{cursor:pointer}
.nav span{cursor:pointer}
.q2{background:#fff;border-radius:16px;border:1px solid var(--line);padding:14px;margin-bottom:10px}
.qt{font-size:14.5px;font-weight:800;margin-bottom:8px}.qt i{font-style:normal;font-weight:500;color:var(--mute);font-size:12.5px;margin-left:4px}
.q2 .chips{margin-top:0;gap:6px}
.q2 textarea,.q2 input.tx{width:100%;font:inherit;font-size:14px;border:1px solid var(--line);border-radius:10px;padding:8px 10px;resize:none;background:#FBF9F7}
.more{display:flex;justify-content:space-between;font-size:14px;font-weight:700;padding:13px 14px;background:#fff;border-radius:14px;border:1px dashed #CFC6BF;margin-bottom:10px;cursor:pointer}
.btn{flex:1;text-align:center;font-weight:800;font-size:15px;padding:14px;border-radius:14px;cursor:pointer}
.btn.g{background:var(--tealx);color:#fff}.btn.o{background:#fff;border:1.5px solid var(--ink)}
.dim{position:absolute;inset:0;background:rgba(23,19,18,.42);z-index:2}
.x{font-size:13px;font-weight:700;color:var(--mute);background:#fff;border:1px solid var(--line);border-radius:999px;padding:4px 10px;cursor:pointer}
.sheet{position:absolute;left:0;right:0;bottom:0;top:96px;background:var(--bg);border-radius:26px 26px 0 0;z-index:4;padding:10px 18px 0;box-shadow:0 -8px 30px rgba(0,0,0,.18);display:flex;flex-direction:column}
.sbody{flex:1;overflow-y:auto;padding-bottom:12px}
.grab{width:44px;height:5px;border-radius:9px;background:#CFC6BF;margin:0 auto 12px}
.shead{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px}
.shead h1{font-size:26px;margin:0}
.scta{display:flex;gap:8px;padding:10px 0 22px}
'''

page = r'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>UGCB Script Writer flow</title>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{--bg:#F4F0EC;--ink:#171312;--mute:#6B625E;--line:#E6DFD9;--pink:#FFE6E8;--pinkb:#F7C3C9;--red:#D92D48;--teal:#E1F1F2;--tealb:#B7DCDF;--tealx:#0F7A7C;--ok:#178A4C}
*{box-sizing:border-box;margin:0;padding:0}
html,body{overflow-x:hidden}
body{background:#E9E3DD;font-family:"Plus Jakarta Sans",system-ui,sans-serif;color:var(--ink);padding:24px 16px}
.wrap{display:flex;gap:28px;justify-content:center;align-items:flex-start;flex-wrap:wrap}
.side{max-width:330px;font-size:13.5px;line-height:1.5;color:var(--mute)}
.side h3{font-size:20px;font-weight:800;color:var(--ink);letter-spacing:-.3px;margin-bottom:6px}
.side p{margin-bottom:10px}
.side .lbl{font-size:12px;font-weight:800;color:var(--ink);margin:14px 0 6px}
.lays{display:flex;flex-wrap:wrap;gap:6px}
.lays button{font:inherit;font-size:12.5px;font-weight:700;background:#fff;border:1px solid var(--line);border-radius:8px;padding:5px 8px;cursor:pointer;color:var(--ink)}
.lays button.on{background:var(--ink);color:#fff;border-color:var(--ink)}
.restart{font:inherit;font-size:12.5px;font-weight:700;background:none;border:0;text-decoration:underline;cursor:pointer;color:var(--ink);margin-top:12px}
.phone{width:390px;max-width:100%;height:min(844px,calc(100dvh - 48px));background:var(--bg);border-radius:36px;border:10px solid #171312;overflow:hidden;position:relative}
.view{position:absolute;inset:0;display:none}
.view.on{display:block}
.scr{height:100%;overflow-y:auto;padding:20px 18px 96px}
.home .scr{padding-bottom:90px}
.top{display:flex;justify-content:space-between;align-items:center;margin-bottom:6px}
.pro{background:var(--ink);color:#fff;font-size:12px;font-weight:700;padding:5px 10px;border-radius:999px}
.tap{cursor:pointer}
.writing{height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;padding:30px;text-align:center}
.spin{width:34px;height:34px;border-radius:50%;border:4px solid var(--tealb);border-top-color:var(--tealx);animation:sp .8s linear infinite}
@keyframes sp{to{transform:rotate(360deg)}}
.writing b{font-size:18px}.writing span{font-size:13px;color:var(--mute)}
.toast{position:absolute;left:50%;bottom:86px;transform:translateX(-50%);background:var(--ink);color:#fff;font-size:13px;font-weight:700;padding:8px 14px;border-radius:999px;z-index:9;white-space:nowrap;opacity:0;transition:opacity .2s;pointer-events:none}
.toast.on{opacity:1}
@media (max-width:520px){
 body{padding:0}
 .wrap{gap:0}
 .side{order:2;padding:18px 16px 28px;max-width:none}
 .phone{width:100%;height:100dvh;border:0;border-radius:0}
}
/* home */
''' + scope(home_css, '.home') + '\n/* output */\n' + scope(css_out, '.out') + r'''
.out .blk{cursor:pointer}
.out .ho{cursor:pointer}
.out .gh span{cursor:pointer}
.out .menu div{cursor:pointer}
.out .menu div.picked{background:var(--tealx)}
.out .mi .add{cursor:pointer}
.out .btn{cursor:pointer}
.out .back{cursor:pointer}
.out .hooks{margin-bottom:4px}
.out .hk-toggle{font-size:12.5px;font-weight:800;color:var(--tealx);margin:0 2px 10px;cursor:pointer}
</style></head><body>
<div class="wrap">
<div class="phone">

<!-- HOME (v5) -->
<div class="view home on" id="v-home"><div class="scr">
 <div class="top"><div class="logo">UGC<b>Breakouts</b></div><div class="pro">Pro</div></div>
 <div class="hi">Hi Veejay</div><h1>What are you filming next?</h1>
 <div class="card p" id="fcard"><div class="fhead"><div class="ct">Breakout Finder</div><div class="x" id="fclose" style="display:none">Close</div></div><div class="cs" id="fcs">High views from small accounts, in your niche</div>
  <div class="box" id="fbox"><input id="fq" placeholder="Search a product or #hashtag" autocomplete="off"><div class="go r" id="fgo">→</div></div>
  <div id="fdef"><div class="sml s" style="margin-top:14px">Suggested searches</div><div class="chips srch" style="margin-top:8px"><div class="chip">Lip liner</div><div class="chip">Self tanner</div><div class="chip">Heatless curls</div><div class="chip">Fridge restock</div></div></div>
  <div id="fopen" style="display:none"><div class="sug" id="fsug" style="display:none"></div>
   <div class="sml">Popular this week</div>
   <div class="chips srch" id="fpop" style="margin-top:0"></div></div></div>
 <div class="card t"><div class="ct">Write a script</div><div class="cs">Built from your profile</div>
  <div class="box" id="pbox"><input id="prod" placeholder="What's the product?" autocomplete="off"><div class="go g" id="pgo">→</div></div>
  <div class="sml s" style="margin-top:14px">Suggested products</div><div class="chips" style="margin-top:8px" id="pchips"><div class="chip tap">Moisturizer</div><div class="chip tap">Lip oil</div><div class="chip tap">Water bottle</div><div class="chip tap">Get ready with me</div></div>
  <div class="alt">Or start from <a>a brand brief</a></div></div>
 <div class="sec2"><div class="sh"><h2>What creators are searching</h2><span>this week</span></div>
  <div class="list srchl">
   <div class="li"><div class="n">1</div><div class="lt">lip liner<div class="lm">214 searches</div></div><div class="up">▲ 38%</div></div>
   <div class="li"><div class="n">2</div><div class="lt">get ready with me<div class="lm">171 searches</div></div><div class="up">▲ 12%</div></div>
   <div class="li"><div class="n">3</div><div class="lt">self tanner<div class="lm">96 searches</div></div><div class="up">new</div></div>
   <div class="li"><div class="n">4</div><div class="lt">fridge restock<div class="lm">88 searches</div></div><div class="up">▲ 20%</div></div>
   <div class="li"><div class="n">5</div><div class="lt">heatless curls<div class="lm">61 searches</div></div><div class="up">▲ 5%</div></div>
  </div></div>
 <div class="sec2"><div class="sh"><h2>Most saved videos this week</h2><span>see all</span></div>
  <div class="thumbs" id="thumbs">
   <div class="th" style="background:#C9B8AE"><span>▶ lip liner</span></div>
   <div class="th" style="background:#B9C7C2"><span>▶ skincare</span></div>
   <div class="th" style="background:#C7B9CF"><span>▶ GRWM</span></div>
  </div>
  <div class="hnote">Tap a video to open its breakout. The tag is its search. Handles stay hidden.</div></div>
 <div class="sec2"><div class="sh"><h2>Searched by creators like you</h2></div>
  <div class="chips srch" style="margin-top:0"><div class="chip">Lip oil</div><div class="chip">Concealer</div><div class="chip">Water bottle</div><div class="chip">Mini fridge</div><div class="chip">Day in my life</div></div>
  <div class="hnote">"Like you" = same niche and a similar follower count. Each chip starts a search.</div></div>
</div>
<div class="dim" id="fdim" style="display:none"></div>
<div class="nav" id="hnav"><b>Home</b><span>Breakouts</span><span>Script</span><span>Library</span></div>
<div class="dim" id="dim" style="display:none"></div>
<div class="sheet" id="sheet" style="display:none">
 <div class="grab"></div>
 <div class="shead"><h1><span id="stitle">Lip oil</span> script <span style="font-size:15px;color:var(--mute);font-weight:600">✎</span></h1><div class="x" id="sclose">Close</div></div>
 <div class="sbody">
  <div class="q2"><div class="qt">How long?</div><div class="chips one" data-q="len"><div class="chip tap">15 s</div><div class="chip tap on">30 s</div><div class="chip tap">45 s</div><div class="chip tap">60 s+</div></div></div>
  <div class="q2"><div class="qt">How will you film it?<i>pick all that fit</i></div><div class="chips multi" data-q="film"><div class="chip tap on">Hands and product</div><div class="chip tap">Talking to camera</div><div class="chip tap">Voiceover</div><div class="chip tap">Text on screen</div></div></div>
  <div class="q2"><div class="qt">Is this for a brand deal?</div><div class="chips one" data-q="deal"><div class="chip tap on">No</div><div class="chip tap">Yes, add the brief</div></div>
   <textarea id="brief" rows="2" placeholder="Paste or upload the brief" style="display:none;margin-top:8px"></textarea></div>
  <div class="more" id="more"><span>Add more detail</span><span id="moreic">+</span></div>
  <div id="detail" style="display:none">
   <div class="q2"><div class="qt">Who is it for?<i>optional</i></div><div class="chips one" data-q="who"><div class="chip tap">Beginners</div><div class="chip tap">Busy moms</div><div class="chip tap">Students</div><div class="chip tap">Type your own</div></div></div>
   <div class="q2"><div class="qt">Got a hook that works?<i>stays word for word</i></div><input class="tx" placeholder="Paste it here"></div>
   <div class="q2"><div class="qt">Tone</div><div class="chips one" data-q="tone"><div class="chip tap">Funny</div><div class="chip tap">Calm</div><div class="chip tap">Blunt</div><div class="chip tap">Bubbly</div><div class="chip tap">Expert</div></div></div>
   <div class="q2"><div class="qt">Opening style the brand wants</div><input class="tx" placeholder="For example, a relatable problem story"></div>
   <div class="q2"><div class="qt">How does it end?</div><div class="chips one" data-q="end"><div class="chip tap">Link in bio</div><div class="chip tap">TikTok Shop</div><div class="chip tap">"Comment X"</div><div class="chip tap">No CTA</div></div></div>
   <div class="q2"><div class="qt">Anything from your own experience to add?<i>optional</i></div><textarea rows="2"></textarea></div>
  </div>
 </div>
 <div class="scta"><div class="btn o" id="skip">Skip</div><div class="btn g" style="flex:2" id="write">Write my script</div></div>
</div>
</div>

<!-- SEARCH RESULTS PLACEHOLDER -->
<div class="view home" id="v-res"><div class="scr">
 <div class="top"><div class="x" id="rback">← Home</div><div class="pro">Pro</div></div>
 <h1 id="rtitle">Breakouts for "lip oil"</h1>
 <div class="hnote">Results open on the Breakouts page, like today. That page is not part of this mock.</div>
</div></div>

<!-- WRITING -->
<div class="view" id="v-writing"><div class="writing"><div class="spin"></div><b>Writing your <span id="wprod">lip oil</span> script</b><span id="wsub"></span></div></div>

<!-- OUTPUT -->
<div class="view out" id="v-out"><div class="scr" id="oscr">
 <div class="top"><div class="back" id="oback">← Home</div><div class="pro">Pro</div></div>
 <h1>Lip oil script <span>✎</span></h1>
 <div class="meta"><div class="tag lay" id="otag"></div><div class="tag len" id="olen"></div></div>
 <div class="hooks" id="hooks">__HOOKS__</div>
 <div id="obody"></div>
</div><div class="bar" id="obar"></div></div>

<div class="toast" id="toast"></div>
</div>

<div class="side">
 <h3>Script Writer flow (clickable)</h3>
 <p>Tap through it like the user would. Home: tap the Breakout Finder box or a suggested search to open it in place, scroll down for what creators are searching, most saved videos and searches by creators like you. Write a script: type a product (or tap a suggested product), answer the pop-up ("Add more detail" opens 6 more questions), then Write my script.</p>
 <p>The script layout follows "How will you film it?": Talking to camera opens layout 1, Voiceover and Hands and product open layout 2 (voiceover over clips), Text on screen opens layout 3 (silent). A brand deal opens layout 10 with the must-say checklist. If more than one is picked, the first in that list wins.</p>
 <p>On the script: tap a hook to use it, "3 new" swaps a group, tap any line for edit one line. Sample copy only, so the rewrite itself isn't simulated.</p>
 <div class="lbl">See every layout</div>
 <div class="lays" id="lays"></div>
 <button class="restart" id="restart">Start over</button>
</div>
</div>

<script>
const L=__LAYOUTS__;
const POOL={spoken:__SPOKEN__,visual:__VISUAL__,text:__TEXT__};
const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
let product='lip oil',cur=2;
function show(id){$$('.view').forEach(v=>v.classList.toggle('on',v.id===id))}
function toast(t){const e=$('#toast');e.textContent=t;e.classList.add('on');clearTimeout(e._t);e._t=setTimeout(()=>e.classList.remove('on'),1400)}
function cap(s){return s.charAt(0).toUpperCase()+s.slice(1)}
// home
function openSheet(p){product=(p||'lip oil').trim().toLowerCase()||'lip oil';$('#stitle').textContent=cap(product);$('#dim').style.display='block';$('#sheet').style.display='flex'}
function closeSheet(){$('#dim').style.display='none';$('#sheet').style.display='none'}
$('#pgo').onclick=()=>openSheet($('#prod').value);
$('#prod').addEventListener('keydown',e=>{if(e.key==='Enter')openSheet($('#prod').value)});
$('#prod').addEventListener('focus',()=>$('#pbox').classList.add('ton'));
$('#prod').addEventListener('blur',()=>$('#pbox').classList.remove('ton'));
$$('#pchips .chip').forEach(c=>c.onclick=()=>{$('#prod').value=c.textContent;openSheet(c.textContent)});
$('#sclose').onclick=closeSheet;$('#dim').onclick=closeSheet;
$$('.chips.one').forEach(g=>g.querySelectorAll('.chip').forEach(c=>c.onclick=()=>{const was=c.classList.contains('on');g.querySelectorAll('.chip').forEach(x=>x.classList.remove('on'));if(!(was&&g.dataset.q!=='len'&&g.dataset.q!=='deal'))c.classList.add('on');if(g.dataset.q==='deal')$('#brief').style.display=c.textContent.startsWith('Yes')?'block':'none'}));
$$('.chips.multi .chip').forEach(c=>c.onclick=()=>c.classList.toggle('on'));
$('#more').onclick=()=>{const d=$('#detail'),o=d.style.display==='none';d.style.display=o?'block':'none';$('#moreic').textContent=o?'−':'+'};
function pickLayout(){
 if($('[data-q=deal] .chip.on')?.textContent.startsWith('Yes'))return 10;
 const f=$$('[data-q=film] .chip.on').map(c=>c.textContent);
 if(f.includes('Talking to camera'))return 1;
 if(f.includes('Voiceover')||f.includes('Hands and product'))return 2;
 if(f.includes('Text on screen'))return 3;
 return 11}
function write(){closeSheet();$('#wprod').textContent=product;show('v-writing');setTimeout(()=>{render(pickLayout());show('v-out')},1600)}
$('#write').onclick=write;$('#skip').onclick=write;
// output
function words(t){return t.replace(/must-say ✓/,'').trim().split(/\s+/).length}
function lenOf(){const el=$('#obody');let n=0;const says=[...el.querySelectorAll('.blk .say,.verdict .say')].map(s=>s.textContent.trim());says.forEach(t=>n+=words(t));const h=el.querySelector('.hook');if(h&&/SPOKEN/.test(h.querySelector('small').textContent)){const ht=h.querySelector('b').textContent.trim();if(!says.includes(ht))n+=words(ht)}return n}
function setLen(l){$('#olen').textContent=l.fixedLen||(()=>{const n=lenOf();return n+' words · about '+Math.round(n/2.5)+' s of 30 s'})()}
function render(n){cur=n;const l=L[n];$('#otag').textContent=l.tag;$('#obody').innerHTML=l.body;$('#obar').innerHTML=l.bar;setLen(l);
 const p=$('#oscr h1');p.innerHTML=cap(product)+' script <span>✎</span>';
 const f=$$('[data-q=film] .chip.on').map(c=>c.textContent.toLowerCase());const deal=$('[data-q=deal] .chip.on')?.textContent.startsWith('Yes');
 $('#hooks .from').innerHTML='Built from: <b>your answers</b> · <b>'+product+'</b>'+(f.length?' · <b>'+f.join(', ')+'</b>':'')+(deal?' · <b>the brief</b>':'');
 resetHooks();
 $('#oscr').scrollTop=0;wireOut();$$('#lays button').forEach(b=>b.classList.toggle('on',+b.dataset.n===n))}
function wireOut(){
 function pick(m){m.querySelectorAll('div').forEach(o=>o.onclick=()=>{m.querySelectorAll('div').forEach(x=>x.classList.remove('picked'));o.classList.add('picked');toast(o.textContent+': rewrites only this line')})}
 $$('#obody .menu').forEach(pick);
 $$('#obody .blk').forEach(b=>b.onclick=e=>{if(e.target.closest('.menu'))return;const open=b.querySelector('.menu');$$('#obody .menu').forEach(m=>m.remove());$$('#obody .blk.sel').forEach(x=>x.classList.remove('sel'));$$('#obody .pen').forEach(x=>x.style.display='');if(open)return;b.classList.add('sel');const pen=b.querySelector('.pen');if(pen)pen.style.display='none';const m=document.createElement('div');m.className='menu';m.innerHTML='<div>Shorter</div><div>Punchier</div><div>More like me</div><div>Redo</div>';(b.classList.contains('num')?b.lastElementChild:b).appendChild(m);pick(m)});
 $$('#obody .mi .add').forEach(a=>a.onclick=()=>{a.outerHTML='<span class="y">✓</span>';toast('Added to the script')});
 $$('#obar .btn').forEach(b=>b.onclick=()=>toast('Copied'));
}
// hooks
const groups=$$('#hooks .hg');const keys=['spoken','visual','text'];const off=[0,0,0];
groups.forEach((g,i)=>{g.querySelector('.gh span').onclick=()=>{off[i]=(off[i]+3)%POOL[keys[i]].length;const hs=g.querySelectorAll('.ho');hs.forEach((h,j)=>{h.textContent=POOL[keys[i]][(off[i]+j)%POOL[keys[i]].length];h.classList.remove('on')})};
 g.addEventListener('click',e=>{const h=e.target.closest('.ho');if(!h)return;$$('#hooks .ho').forEach(x=>x.classList.remove('on'));h.classList.add('on');const hk=$('#obody .hook');if(hk){hk.querySelector('small').textContent='HOOK · '+['SPOKEN','VISUAL','TEXT ONLY'][i];hk.querySelector('b').textContent=h.textContent;setLen(L[cur])}else{toast('Hook goes to the top of the script')}})});
function norm(t){return t.trim().replace(/\.$/,'').toLowerCase()}
function resetHooks(){const hk=$('#obody .hook b');const cur_=hk?norm(hk.textContent):'';groups.forEach((g,i)=>{off[i]=0;g.querySelectorAll('.ho').forEach((h,j)=>{h.textContent=POOL[keys[i]][j];h.classList.toggle('on',!!cur_&&norm(h.textContent)===cur_)})})}
$('#oback').onclick=()=>{show('v-home')};
// layout switcher
const lays=$('#lays');Object.keys(L).forEach(k=>{const b=document.createElement('button');b.dataset.n=k;b.textContent=k+'. '+L[k].label;b.onclick=()=>{render(+k);show('v-out')};lays.appendChild(b)});
$('#restart').onclick=()=>{closeSheet();closeFinder();$('#prod').value='';show('v-home')};
// finder (in place)
const POP=[["Lip liner","Get ready with me","Self tanner","Fridge restock","Heatless curls","Advent calendar","Skincare routine"],["Lip oil","Concealer","Water bottle","Mini fridge","Day in my life","Moisturizer"]];let popi=0;
function drawPop(){const f=$('#fpop');f.innerHTML=POP[popi].map(t=>'<div class="chip">'+t+'</div>').join('')+'<div class="chip add" id="fmore">↻ More</div>';
 f.querySelectorAll('.chip:not(.add)').forEach(c=>c.onclick=()=>openRes(c.textContent));$('#fmore').onclick=()=>{popi=(popi+1)%POP.length;drawPop()}}
function openFinder(){if($('#fopen').style.display==='block')return;$('#fcard').classList.add('lift');$('#fclose').style.display='';$('#fcs').style.display='none';$('#fdef').style.display='none';$('#fopen').style.display='block';$('#fbox').classList.add('on');$('#fdim').style.display='block';$('#v-home .scr').scrollTop=0;drawPop();drawSug()}
function closeFinder(){$('#fcard').classList.remove('lift');$('#fclose').style.display='none';$('#fcs').style.display='';$('#fdef').style.display='';$('#fopen').style.display='none';$('#fbox').classList.remove('on');$('#fdim').style.display='none';$('#fq').value='';$('#fq').blur()}
function esc(t){return t.replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]))}
function drawSug(){const q=$('#fq').value.trim().toLowerCase(),b=$('#fsug');if(!q){b.style.display='none';b.innerHTML='';return}
 const TERMS=['lip oil','lip liner','self tanner','fridge restock','heatless curls','advent calendar','skincare routine','get ready with me','concealer','water bottle','mini fridge','day in my life','moisturizer'];const base=TERMS.find(t=>t.startsWith(q))||q;const items=[base,base+' swatch',base+' review'];
 b.innerHTML=items.map((t,i)=>'<div class="sg" data-t="'+esc(t)+'"><span><em>'+esc(q)+'</em>'+esc(t.slice(q.length))+'</span><small>'+(i===0?'breakouts ready':'')+'</small></div>').join('');b.style.display='block';
 b.querySelectorAll('.sg').forEach(r=>r.onclick=()=>openRes(r.dataset.t))}
function openRes(t){t=t.trim();if(!t)return;$('#rtitle').textContent='Breakouts for "'+t.toLowerCase()+'"';closeFinder();show('v-res')}
$('#fq').addEventListener('focus',openFinder);$('#fbox').onclick=openFinder;$('#fq').addEventListener('input',drawSug);
$('#fq').addEventListener('keydown',e=>{if(e.key==='Enter')openRes($('#fq').value)});
$('#fgo').onclick=e=>{e.stopPropagation();if($('#fopen').style.display==='block'&&$('#fq').value.trim())openRes($('#fq').value);else{openFinder();$('#fq').focus()}};
$('#fclose').onclick=e=>{e.stopPropagation();closeFinder()};$('#fdim').onclick=closeFinder;
$$('#fdef .chip').forEach(c=>c.onclick=()=>openRes(c.textContent));
$$('.srchl .li').forEach(r=>r.onclick=()=>openRes(r.querySelector('.lt').firstChild.textContent));
$$('#v-home .sec2 .chips.srch .chip').forEach(c=>c.onclick=()=>openRes(c.textContent));
$$('#thumbs .th').forEach(t=>t.onclick=()=>toast('Opens that video\'s breakout (not part of this mock)'));
$('#rback').onclick=()=>show('v-home');
$$('#hnav span').forEach(s=>s.onclick=()=>toast(s.textContent+': not part of this mock'));
</script>
</body></html>'''

page = (page.replace('__HOOKS__', hooks_html)
            .replace('__LAYOUTS__', json.dumps(layouts, ensure_ascii=False))
            .replace('__SPOKEN__', json.dumps(spoken_all))
            .replace('__VISUAL__', json.dumps(visual_all))
            .replace('__TEXT__', json.dumps(text_all)))
open(os.path.join(HERE, 'index.html'), 'w').write(page)
print('ok', len(page), 'layouts', len(layouts))
