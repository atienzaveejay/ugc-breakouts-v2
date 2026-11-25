# Clickable script page options for Ivan (25 Nov). Same 15s lip oil script as the prototype default
# (script-writer-flow: Lip oil, 15s, Sell it, Talking to camera, Calm and real).
import html as H
E=H.escape
S={
 "src":"From your idea · Talking to camera · 15s",
 "title":"Lip oil script",
 "idea_t":"One coat in daylight",
 "idea":"Show one coat of lip oil by the window, and why it beats sticky gloss.",
 "answers":"Sell it · Talking to camera · Calm and real",
 "hook":("0–2s","Watch what one coat of this lip oil does.","Close up, the lip oil by your face"),
 "body_t":"3–11s",
 "beats":[("Talking","3–7s","My lips get dry by lunch, and most glosses just sit on top.","Talking, bare lips"),
          ("Lips by the window","8–11s","The shine looks natural in daylight, not wet.","Lips by the window")],
 "cta":("12–15s","It's on TikTok Shop, linked below.","Product to camera"),
}
# hooks exactly as the prototype shows them for lip oil (Question / Bold claim / Storytime)
HOOKS={"Question":["Does this lip oil last from breakfast to dinner?","Why does every gloss feel sticky by noon?","Is this the only lip step you need?"],
       "Bold claim":["Watch what one coat of this lip oil does.","This is the lip oil I reach for first","I stopped wearing gloss because of this lip oil"],
       "Storytime":["POV: you found a lip oil that isn't sticky","I almost gave up on lip products until this","My hair kept sticking to my gloss, so I switched"]}
PICK=[HOOKS["Bold claim"][0],HOOKS["Question"][0],HOOKS["Storytime"][0]]
MORE=[HOOKS["Bold claim"][1],HOOKS["Question"][1],HOOKS["Storytime"][1]]
CAM='<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 8h3l2-3h6l2 3h3v11H4z"/><circle cx="12" cy="13" r="3.5"/></svg>'
PEN='<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 20h4L19 9l-4-4L4 16z"/></svg>'
NAV='<div class="nav"><span>Home</span><span>Breakouts</span><b>Script</b><span>Library</span></div>'
q=lambda s:'“'+E(s)+'”'
def say(cls,s): return f'<p class="{cls} say" tabindex="0">{q(s)}</p>'
TOP='<div class="top"><span class="back">← Home</span><span class="tr"><span class="pro">Pro</span><span class="acct">Account</span></span></div>'
HEAD=f'{TOP}<div class="srcl">{E(S["src"])}</div><h2 class="ttl">{E(S["title"])} <span class="pen">{PEN}</span></h2>'
PRACTICE='<button class="btn-o prac">▶ Practice full screen</button>'
REWRITE='<div class="rw"><b>Not quite right?</b><button class="btn-o sm rew">Rewrite the whole script</button><small>3 of 3 rewrites left</small></div>'
BAR3='<div class="dock bar3"><button class="b-o save">Save script</button><button class="b-o share">Share</button><button class="b-t copy">Copy</button></div>'
def o1():
    b=''.join(f'<div class="l-beat"><div class="l-bh"><span class="l-n">{i+1}</span><span class="l-bn">{E(n.lower())}</span><span class="l-t">{t}</span></div>{say("l-say",s)}<p class="l-shot">{CAM}{E(f)}</p></div>' for i,(n,t,s,f) in enumerate(S["beats"]))
    return f'''{HEAD}
<div class="l-sec"><div class="l-sh"><b>HOOK</b><span>{S["hook"][0]}</span></div><p class="l-say big say hk" tabindex="0">{q(S["hook"][1])}</p><p class="l-shot">{CAM}{E(S["hook"][2])}</p></div>
<div class="l-sec"><div class="l-sh"><b>BODY</b><span>{S["body_t"]}</span></div>{b}</div>
<div class="l-sec"><div class="l-sh"><b>CTA</b><span>{S["cta"][0]}</span></div>{say("l-say",S["cta"][1])}<p class="l-shot">{CAM}{E(S["cta"][2])}</p></div>
{PRACTICE}{REWRITE}''', BAR3
def o2():
    b=''.join(f'<div class="v-step"><div class="v-sh"><span class="v-n">{i+1}</span><b>{E(n)}</b><span class="v-t">{t}</span><i class="pen ed">{PEN}</i></div>{say("v-say",s)}<p class="v-shot">{CAM}{E(f)}</p></div>' for i,(n,t,s,f) in enumerate(S["beats"]))
    bulb='<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#0F7A7C" stroke-width="2"><path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/></svg>'
    return f'''<div class="v-top"><span class="v-back">‹</span><b>Your script</b><span></span></div>
<div class="v-src"><div class="v-ic">✎</div><div><small>From your idea</small><b>Lip oil</b><span>{E(S["answers"])}</span></div></div>
<div class="v-idea"><div class="v-ih"><span class="v-bulb">{bulb}</span><b>IDEA</b><span>15s</span></div><h2>{E(S["idea_t"])}</h2><p>{E(S["idea"])}</p></div>
<div class="v-hook"><div class="v-sh"><b class="tl">HOOK</b><span class="v-t">{S["hook"][0]}</span><i class="pen ed">{PEN}</i></div><p class="v-say xl say hk" tabindex="0">{q(S["hook"][1])}</p><p class="v-shot">{CAM}{E(S["hook"][2])}</p></div>
<div class="v-body"><div class="v-bh"><b class="tl">BODY</b><span class="v-t">{S["body_t"]}</span></div>{b}</div>
<div class="v-cta"><div class="v-sh"><b class="tl">CTA</b><span class="v-t">{S["cta"][0]}</span><i class="pen ed">{PEN}</i></div>{say("v-say",S["cta"][1])}<p class="v-shot">{CAM}{E(S["cta"][2])}</p></div>
{PRACTICE}{REWRITE}''', '<div class="dock v-bar"><button class="v-save save">Save script</button><button class="v-ib share" aria-label="Share">⤴</button><button class="v-ib copy" aria-label="Copy">⧉</button></div>'
def o3():
    hk=''.join(f'<div class="s-hk{" on" if i==0 else ""}" data-i="{i}" tabindex="0"><span class="dot"></span><span class="hkt">{E(h)}</span></div>' for i,h in enumerate(PICK))
    shots=[("Hook",S["hook"][0],S["hook"][1],S["hook"][2])]+list(S["beats"])+[("CTA",S["cta"][0],S["cta"][1],S["cta"][2])]
    cards=''.join(f'<div class="s-card"><div class="s-ch"><span class="s-k">Shot {i+1} of {len(shots)}</span><b>{E(n)}</b><span class="s-t">{t}</span></div><p class="s-say say{" hk" if i==0 else ""}" tabindex="0">{q(s)}</p><div class="s-film">{CAM}<span>{E(f)}</span></div></div>' for i,(n,t,s,f) in enumerate(shots))
    return f'''{HEAD}<div class="s-lab">Pick your hook</div><div class="s-hks">{hk}</div><button class="s-more">↻ 3 new hooks</button>
<div class="s-lab">Your shots</div>{cards}{PRACTICE}{REWRITE}''', BAR3
def o4():
    b=''.join(f'<p class="d-p"><span class="d-tm">{t}</span><span class="say" tabindex="0">{E(s)}</span><em>{E(f)}</em></p>' for (n,t,s,f) in S["beats"])
    sheet=''.join(f'<div class="d-opt" data-h="{E(h)}" tabindex="0">{E(h)}</div>' for g in HOOKS for h in HOOKS[g][:1])+''.join(f'<div class="d-opt" data-h="{E(h)}" tabindex="0">{E(h)}</div>' for g in HOOKS for h in HOOKS[g][1:2])
    return f'''{HEAD}
<div class="d-h">Hook</div><p class="d-p hook"><span class="d-tm">{S["hook"][0]}</span><span class="say hk" tabindex="0">{E(S["hook"][1])}</span><em>{E(S["hook"][2])}</em></p>
<div class="d-h">Body</div>{b}
<div class="d-h">CTA</div><p class="d-p"><span class="d-tm">{S["cta"][0]}</span><span class="say" tabindex="0">{E(S["cta"][1])}</span><em>{E(S["cta"][2])}</em></p>''', f'''<div class="dock d-dock"><button class="d-go prac">▶ Practice full screen</button><div class="d-tools"><button class="tb hooks">Hooks</button><button class="tb rew">Rewrite</button><button class="tb save">Save</button><button class="tb share">Share</button><button class="tb copy">Copy</button></div></div>
<div class="hsheet"><div class="hs-in"><div class="hs-h"><b>Pick a hook</b><button class="hs-x">Close</button></div>{sheet}</div></div>'''
OPTS=[("1","Live, cleaned up",o1,"The live page with the smallest changes: clear Hook / Body / CTA sections with times, bigger spoken lines, and what to film under each.","Better: closest to what Lester already built, so it ships fastest.","Trade-off: still reads like a document, and the hook can't be swapped on the page."),
      ("2","Your Script page v7",o2,"Your 11 Nov design: source card, Idea card, Hook card, Body with numbered steps, CTA, and a big Save script. Bottom bar kept as live.","Better: clearest structure, every part has its time and a pencil to change it.","Trade-off: the longest page to scroll."),
      ("3","Shoot list",o3,"Pick a hook at the top, then one card per shot in filming order: what to say (big), what to film (small), and the time.","Better: easiest to film from, one card at a time, and it looks good screen recorded.","Trade-off: the full script isn't one block, so it's harder to read top to bottom."),
      ("4","Simple script",o4,"A plain script like a notes doc, times inline and what to film in grey. One big Practice button; hooks, rewrite, save, share and copy sit in a small bar.","Better: least to understand, the user reads it in one go.","Trade-off: hooks and rewrite are one tap away instead of on the page.")]
CSS=open(__file__.replace('build.py','style.css')).read()
JS=open(__file__.replace('build.py','app.js')).read()
cards=''; tabs=''
for k,t,fn,what,better,trade in OPTS:
    inner,dock=fn()
    tabs+=f'<button class="tab{" on" if k=="1" else ""}" data-k="{k}">{k}. {E(t)}</button>'
    cards+=f'''<section class="card{" on" if k=="1" else ""}" id="opt{k}" data-k="{k}"><h3>{k}. {E(t)}</h3>
<div class="phone" data-opt="{k}"><div class="scr"><div class="pad">{inner}<div class="sp"></div></div></div>{dock}{NAV}
<div class="tp"><div class="tph"><span>Practice</span><span><button class="tp-pp">Pause</button><button class="tp-x">Close</button></span></div><div class="tpb"></div></div><div class="toast"></div></div>
<div class="txt"><p>{E(what)}</p><p>{E(better)}</p><p class="m">{E(trade)}</p></div></section>'''
html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Script page options</title>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet"><style>{CSS}</style></head><body>
<header class="hd"><h1>Script page: 4 options</h1><p class="sub">Same 15s lip oil script in each (Sell it, Talking to camera, Calm and real), the one the <a href="../script-writer-flow/">prototype</a> writes by default. Scroll and tap inside each phone: pick a hook, tap a line to edit it, Practice full screen, Save, Share, Copy. Sample copy; rewrites aren't simulated.</p>
<p class="subm">Scroll and tap inside the phone. Sample copy.</p><nav class="tabs">{tabs}</nav></header><main class="grid">{cards}</main>
<script>const HOOKS={__import__("json").dumps(PICK)};const MORE={__import__("json").dumps(MORE)};{JS}</script></body></html>'''
open(__file__.replace('build.py','index.html'),'w').write(html)
print('ok')
