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
hooks_html = shared[shared.index('<div class="from">'):].strip().replace('Spoken hooks', 'Question').replace('Visual hooks', 'Bold claim').replace('Text only hooks', 'Storytime')

# hook pools for "3 new": only copy that already exists in the mockups
spoken_all = ["Watch what one coat does in daylight", "I keep this one in every bag", "This is the lip oil I reach for first",
              "Does this lip oil last from breakfast to dinner?", "How I get glossy lips that don't feel sticky.", "3 things I like about this lip oil."]
visual_all = ["Cap off, close to the mic", "Bare lips, then one swipe", "Swatch on the hand, then the lips",
              "Left side gloss, right side lip oil.", "Wand out, one slow swipe", "Press lips together, close up"]
text_all = ["POV: you found a lip oil that isn't sticky", "the only lip step I keep", "lip oil, one swipe, daylight",
            "glossy, not heavy", "no sticky feel", "nothing sticks"]

import sys
sys.path.insert(0, HERE)
from samples import SETS as _SETS, GENERIC as _GEN, LIP as _LIPX
_STRUCT = {'✎','SAY','Clip:','Shot:','Scene:','HOOK · SPOKEN','HOOK · VISUAL','HOOK · TEXT ONLY','Shorter','Punchier','More like me','Redo','Open in teleprompter','SETUP','VERDICT','VERDICT A','VERDICT B','HOOK','PROBLEM','PRODUCT','PROOF','CTA','BODY','END','COVER','✓','+ add it','must-say ✓','MUST-SAY (FROM THE BRIEF)'}
_PAT = re.compile(r'^(\d+|\d+ OF \d+|\d+ TO \d+ S|CHECK IN · .*|BEAT \d+|SLIDE \d+|[AB] · (AN HOUR LATER|AFTER LUNCH))$')
def _split_body(body):
    parts = re.split(r'(<[^>]+>)', body); out = []; content = []
    for part in parts:
        t = part.strip()
        if part.startswith('<') or not t or t in _STRUCT or _PAT.match(t):
            out.append(part); continue
        lead = part[:len(part) - len(part.lstrip())]; trail = part[len(part.rstrip()):]
        out.append(lead + '{{%d}}' % len(content) + trail); content.append(html.unescape(t))
    return ''.join(out), content
_lip = {}
for _n in range(1, 12):
    layouts[_n]['tpl'], _lip[_n] = _split_body(layouts[_n]['body'])
SETS_JS = {'lip oil': {'L': _lip, 'hooks': {'spoken': spoken_all, 'visual': visual_all, 'text': text_all}, 'h2': _LIPX['hooks2'], 'x': _LIPX['extra']}}
for _k, _v in _SETS.items():
    SETS_JS[_k] = {'L': _v['layouts'], 'hooks': _v['hooks'], 'h2': _v['hooks2'], 'x': _v['extra']}
GEN_JS = {'L': _GEN['layouts'], 'hooks': _GEN['hooks'], 'h2': _GEN['hooks2'], 'x': _GEN['extra']}
for _k, _v in list(SETS_JS.items()) + [('generic', GEN_JS)]:
    for _n in range(1, 12):
        assert len(_v['L'][_n]) == len(_lip[_n]), (_k, _n, len(_v['L'][_n]), len(_lip[_n]))
    for _g in ('spoken', 'visual', 'text'):
        assert len(_v['hooks'][_g]) == 6, (_k, _g)

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
.chip,.btn,.go,.x,.li,.sg,.more,.th{transition:transform .15s var(--ease),background .2s,box-shadow .2s,border-color .2s}
.chip:active,.btn:active,.go:active,.x:active,.more:active,.th:active{transform:scale(.98)}
.li:active,.sg:active{transform:scale(.99)}
.card.p{transition:box-shadow .3s var(--ease)}
.card.p.lift{box-shadow:var(--sh-2)}
.pin{animation:s3pop .35s ease both;animation-delay:calc(var(--k,0)*40ms)}
.ris{animation:rise .3s var(--ease) both}
.tabnav span{cursor:pointer;padding:8px 6px}.tabnav span.on{color:var(--ink);font-weight:800}
.bbrief{display:flex;align-items:center;gap:12px;margin-top:12px;background:#fff;border:1.5px solid var(--ink);border-radius:14px;padding:11px 12px;cursor:pointer}
.bbrief .bi{width:36px;height:36px;border-radius:8px;background:var(--tsoft);color:var(--tealx);display:grid;place-items:center;font-size:11px;font-weight:800;flex:none}
.bbrief b{display:block;font-size:15px}.bbrief small{display:block;font-size:12.5px;color:var(--mute);font-weight:600;margin-top:1px}.bbrief .chev{margin-left:auto;font-weight:800;color:var(--mute)}
.bbrief:active{transform:scale(.98)}
.bblock{background:var(--tsoft);border-radius:12px;padding:12px;margin-bottom:12px}
.bblock textarea{width:100%;box-sizing:border-box}
.bup{display:inline-block;margin-top:8px;font-size:13px;font-weight:700;text-decoration:underline;cursor:pointer;position:relative}.bup input{position:absolute;inset:0;opacity:0;cursor:pointer}
.bfile{display:none;margin-top:8px;align-items:center;gap:8px;background:#fff;border:1px solid var(--line);border-radius:9px;padding:6px 10px;font-size:13px;font-weight:600}
.bfile.on{display:inline-flex}.bfile .rm{color:var(--mute);cursor:pointer;font-weight:700}
.ctax{display:none;margin-top:8px}
.same{margin-top:18px;background:#fff;border:1px solid var(--line);border-radius:14px;padding:18px}
.same b{display:block;font-size:18px;font-weight:800}.same span{display:block;margin-top:6px;font-size:14px;color:var(--mute);line-height:1.45}
.qrow{display:flex;align-items:center;gap:8px;margin-top:6px;font-size:14px;color:var(--mute);font-weight:600}.qrow b{color:var(--ink)}.qrow .qel{margin-left:auto;font-variant-numeric:tabular-nums}
.qh{font-size:28px;line-height:1.12;letter-spacing:-.025em;font-weight:800;margin:10px 0 12px}
.qsteps{list-style:none;margin:0 0 14px;padding:0;display:grid;gap:8px}
.qsteps li{display:flex;align-items:center;gap:10px;font-size:14px;font-weight:700;color:var(--soft)}
.qsteps li .d{width:18px;height:18px;border-radius:50%;border:2px solid #D6CDC5;display:grid;place-items:center;font-size:10px;color:#fff;flex:none;transition:all .2s var(--ease)}
.qsteps li.qon{color:var(--ink)}.qsteps li.qon .d{border-color:var(--tealx)}
.qsteps li.qok{color:var(--ink)}.qsteps li.qok .d{background:var(--tealx);border-color:var(--tealx)}
.qstats{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px}
.qstats div{background:#fff;border:1px solid var(--hair);border-radius:10px;padding:10px}
.qstats b{display:block;font-size:24px;font-weight:800;font-variant-numeric:tabular-nums;letter-spacing:-.02em}.qstats small{font-size:12.5px;color:var(--mute);font-weight:600}
.qfeedw{position:relative;height:250px;overflow:hidden;border-radius:12px;background:#fff;border:1px solid var(--hair)}
.qfeedw:after{content:"";position:absolute;left:0;right:0;bottom:0;height:60px;background:linear-gradient(transparent,#fff);pointer-events:none}
.qfeed{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;padding:8px;animation:qscroll 6s linear infinite}
@keyframes qscroll{from{transform:translateY(0)}to{transform:translateY(-50%)}}
.qtile{position:relative;height:96px;border-radius:8px;transition:opacity .3s var(--ease),box-shadow .3s var(--ease)}
.qtile i{position:absolute;left:6px;bottom:6px;right:22px;height:5px;border-radius:3px;background:rgba(255,255,255,.7)}
.qtile.no{opacity:.28}
.qtile.hit{box-shadow:0 0 0 3px var(--tealx)}
.qtile .ok{position:absolute;top:5px;right:5px;width:18px;height:18px;border-radius:50%;background:var(--tealx);color:#fff;font-size:10px;font-weight:800;display:grid;place-items:center;opacity:0;transform:scale(.6)}
.qtile.hit .ok{animation:settle .16s var(--out) both}
.qscan{position:absolute;left:0;right:0;height:2px;background:var(--tealx);box-shadow:0 0 10px 2px rgba(11,123,127,.35);z-index:3;animation:qline 1.4s cubic-bezier(.4,0,.2,1) infinite}
@keyframes qline{0%{top:0;opacity:1}90%{opacity:1}100%{top:100%;opacity:0}}
.qdone{display:none;margin-top:14px}.qdone.on{display:block;animation:rise .3s var(--ease) both}
.qdone h3{margin:0 0 10px;font-size:22px;font-weight:800}
#detail .q2{animation:rise .35s var(--ease) both;animation-delay:calc(var(--k,0)*40ms)}
#brief{animation:rise .3s var(--ease) both}
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
.sheet{position:absolute;left:0;right:0;bottom:0;top:96px;background:var(--bg);border-radius:26px 26px 0 0;z-index:4;padding:10px 18px 0;box-shadow:0 -8px 30px rgba(0,0,0,.18);display:flex;flex-direction:column;animation:up .38s var(--ease) both}
.sheet.closing{animation:down .26s var(--ease) both}
.dim{animation:fade .25s both}
.dim.closing{animation:fadeout .22s both}
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
:root{--bg:#F4F0EC;--ink:#171312;--mute:#6B625E;--line:#E6DFD9;--pink:#FFE6E8;--pinkb:#F7C3C9;--red:#D92D48;--teal:#E1F1F2;--tealb:#B7DCDF;--tealx:#0F7A7C;--ok:#178A4C;
 --ease:cubic-bezier(.2,.8,.2,1);--out:cubic-bezier(.2,.7,.2,1);--snap:cubic-bezier(.3,0,.15,1);--sh-2:0 6px 24px rgba(23,19,18,.12);--track:#ECE5DF;--hair:#E8E0D9;--soft:#9A908A;--tsoft:#E2F3F3}
/* motion: UB 3.1 (--ease, up, fade, rise, slidein, s3pop, press, toast) + magic-moments-v2 (--out, --snap, processing beat, rv, unroll, settle). See handover notes script-writer-flow-motion-notes-2026-11-25.md */
@keyframes up{from{transform:translateY(100%)}}
@keyframes down{to{transform:translateY(100%)}}
@keyframes fade{from{opacity:0}}
@keyframes fadeout{to{opacity:0}}
@keyframes rise{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
@keyframes slidein{from{opacity:0;transform:translateX(28px)}to{opacity:1;transform:none}}
@keyframes s3pop{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:none}}
@keyframes rv{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
@keyframes unroll{from{clip-path:inset(0 0 100% 0)}to{clip-path:inset(0 0 0 0)}}
@keyframes settle{from{opacity:0;transform:scale(.6)}to{opacity:1;transform:none}}
@keyframes fill{from{transform:scaleX(0)}to{transform:none}}
@keyframes on{from{opacity:0}to{opacity:1}}
@keyframes ink{from{color:var(--soft)}to{color:var(--ink)}}
@keyframes read{from{opacity:.4;filter:grayscale(1)}to{opacity:1;filter:none}}
@keyframes scan{0%{opacity:1;top:0}92%{opacity:1}100%{opacity:0;top:100%}}
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
.view.enter>.scr,.view.enter>.proc{animation:slidein .4s var(--ease) backwards}
.view.back>.scr{animation:fade .2s backwards}
.scr{height:100%;overflow-y:auto;padding:20px 18px 96px}
.home .scr{padding-bottom:90px}
.top{display:flex;justify-content:space-between;align-items:center;margin-bottom:6px}
.pro{background:var(--ink);color:#fff;font-size:12px;font-weight:700;padding:5px 10px;border-radius:999px}
.tap{cursor:pointer}
.proc{height:100%;overflow:hidden;padding:20px 20px 0}
.proc .top{margin-bottom:10px}
.ptok{display:flex;align-items:center;gap:10px;height:44px;font-size:15px;color:var(--mute);font-weight:600;white-space:nowrap;overflow:hidden}
.ptok .ti{width:36px;height:36px;border-radius:6px;background:#fff;border:1px solid var(--hair);display:grid;place-items:center;color:var(--ink);flex:none;font-size:16px}
.ptok b{color:var(--ink);font-size:16px}
.pline{display:flex;align-items:center;gap:10px;margin:14px 0 14px;min-height:40px}
.pline h2{margin:0;font-size:30px;line-height:1.12;letter-spacing:-.025em;font-weight:800}
.pdone{width:32px;height:32px;border-radius:50%;background:var(--tealx);color:#fff;display:grid;place-items:center;flex:none;opacity:0;transform:scale(.6);font-weight:800}
.go2 .pdone{animation:settle .22s cubic-bezier(.2,.9,.3,1) 1780ms both}
.pbar{display:grid;grid-template-columns:repeat(3,1fr);gap:5px;height:12px}
.pbar span{background:var(--track);border-radius:3px;overflow:hidden}
.pbar i{display:block;height:100%;background:var(--tealx);transform:scaleX(0);transform-origin:0 50%}
.go2 .pbar i{animation:fill .48s cubic-bezier(.45,0,.25,1) var(--d) both}
.plab{display:grid;grid-template-columns:repeat(3,1fr);gap:5px;margin:10px 0 0;padding:0;list-style:none}
.plab li{display:flex;flex-direction:column;gap:5px;min-width:0}
.plab .dot{position:relative;width:18px;height:18px;border-radius:50%;border:2px solid #D6CDC5}
.plab .dot i{position:absolute;inset:-2px;border-radius:50%;opacity:0}
.plab .dot .rg{border:2px solid var(--tealx)}
.plab .dot .ok{background:var(--tealx);display:grid;place-items:center;transform:scale(.5);color:#fff;font-size:10px;font-weight:800;font-style:normal}
.go2 .plab .rg{animation:on 1ms linear var(--d) both}
.go2 .plab .ok{animation:settle .16s var(--out) var(--e) both}
.plab .t{font-size:14px;line-height:1.25;font-weight:700;color:var(--soft)}
.go2 .plab .t{animation:ink 1ms linear var(--d) both}
.pmat{position:relative;margin-top:14px;background:#fff;border:1px solid var(--hair);border-radius:8px;padding:10px;overflow:hidden}
.pscan{position:absolute;left:0;right:0;top:0;height:2px;background:var(--tealx);box-shadow:0 0 10px 2px rgba(11,123,127,.35);opacity:0;z-index:4}
.go2 .pscan{animation:scan 1.55s cubic-bezier(.4,0,.2,1) 150ms both}
.ing{display:grid;grid-template-columns:36px 1fr 24px;gap:10px;align-items:center;padding:8px 0;border-top:1px solid var(--hair);opacity:.4;filter:grayscale(1)}
.ing:first-child{border-top:0}
.go2 .ing{animation:read .2s linear var(--d) both}
.ing .oi{width:36px;height:36px;border-radius:6px;background:var(--tsoft);color:var(--tealx);display:grid;place-items:center;font-weight:800}
.ing small{display:block;font-size:12.5px;color:var(--mute);font-weight:600}
.ing b{display:block;font-size:16px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ing .ck{width:22px;height:22px;border-radius:50%;background:var(--tealx);color:#fff;display:grid;place-items:center;opacity:0;transform:scale(.5);font-size:12px;font-weight:800}
.go2 .ing .ck{animation:settle .16s var(--out) var(--e) both}
.pdraft{margin-top:12px;background:#fff;border:1px solid var(--hair);border-radius:8px;padding:10px 12px;display:grid;gap:10px}
.pdraft small{display:block;font-size:11px;font-weight:800;letter-spacing:.06em;color:var(--mute)}
.pdraft .dh b{font-size:16px;font-weight:800}.pdraft .cur{display:inline-block;width:2px;height:16px;background:var(--tealx);vertical-align:-2px;margin-left:1px;animation:blink .8s steps(1) infinite}
@keyframes blink{50%{opacity:0}}
.pdraft .sk i{display:block;height:8px;border-radius:4px;background:var(--track);margin-top:6px;transform-origin:0 50%;transform:scaleX(0)}
.go2 .pdraft .sk i{animation:fill .5s cubic-bezier(.45,0,.25,1) var(--d) both}
.go2 .pdone{animation-delay:2700ms!important}
.toast{position:absolute;left:16px;right:16px;bottom:86px;justify-content:center;text-align:center;z-index:60;background:var(--ink);color:#fff;border-radius:12px;padding:11px 16px;font-size:14px;font-weight:650;display:none;gap:8px;align-items:center;box-shadow:var(--sh-2);pointer-events:none}
.toast.on{display:flex;animation:rise .3s var(--ease) both}
.rv{animation:rv .3s var(--out) var(--d,0ms) both}
@media (prefers-reduced-motion:reduce){*,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}}
@media (max-width:520px){
 body{padding:0}
 .wrap{gap:0}
 .side{order:2;padding:18px 16px 28px;max-width:none}
 .phone{width:100%;height:100dvh;border:0;border-radius:0}
}
/* home */
''' + scope(home_css, '.home') + '\n/* output */\n' + scope(css_out, '.out') + r'''
.out .scr{overflow-y:auto;overflow-x:hidden}
.scr,.sbody{overscroll-behavior:contain}
.dim{touch-action:none}
.scr.flock{overflow:hidden;touch-action:none}
.tr{display:flex;align-items:center;gap:10px}.acct{font-size:13px;font-weight:700;color:var(--mute);cursor:pointer}
.ptag,.stag{display:inline-block;font-size:10px;font-weight:800;letter-spacing:.04em;text-transform:uppercase;color:var(--soft);border:1px solid var(--line);border-radius:6px;padding:1px 5px;margin-left:6px;vertical-align:middle;font-style:normal}
.stag{color:var(--tealx);border-color:var(--tealb)}
.meta{display:flex;flex-wrap:wrap;align-items:center;gap:4px}
.out .idea,.out .meta,#hooks .from{display:none}
#v-out #hooks{display:none}
.oing{background:#EDE6E0;border-radius:14px;padding:14px;margin:0 0 4px}.oing .oh{font-size:11.5px;font-weight:800;letter-spacing:.5px;color:var(--mute);text-transform:uppercase;margin-bottom:8px}.oing .oc{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:12px}.oing .oc span{background:#fff;border-radius:7px;padding:4px 8px;font-size:12.5px;font-weight:600}.oing .oi{border-top:1px solid #DCD3CC;padding-top:10px}.oing .oi p{font-size:15px;font-weight:700;line-height:1.35;margin-top:4px}.ostart{display:flex;align-items:center;gap:10px;margin:18px 0 14px}.ostart::before,.ostart::after{content:'';flex:1;height:2px;background:var(--ink)}.ostart span{font-size:12.5px;font-weight:800}
.ownx{display:none;margin-top:8px}
.srcl{font-size:12.5px;font-weight:600;color:var(--mute);margin:6px 0 2px}
/* spacing pass 25 Nov (Veejay): more air on the script page */
#v-out .srcl{margin:12px 0 6px}
#v-out h1{margin:0 0 20px}
#v-out #hooks .hg{padding:16px 16px 14px;margin:0 0 16px}
#v-out #hooks .gh{margin:0 0 12px}
#v-out #hooks .ho{padding:12px 14px;margin:0 0 10px}
#v-out #hooks .ho:last-child{margin-bottom:0}
#v-out .tele{margin:8px 0 8px}
#v-out .sech{margin:28px 2px 12px}
#v-out #obody .blk,#v-out #obody .verdict{margin-bottom:14px}
#v-out #obody .hook{margin-bottom:16px;position:relative;padding-right:44px}#obody .hook .hpen{position:absolute;top:10px;right:10px;width:30px;height:30px;border-radius:8px;display:grid;place-items:center;cursor:pointer;color:inherit;opacity:.85}#obody .hook .hpen:hover{background:rgba(255,255,255,.14)}.chm{position:absolute;inset:0;background:rgba(23,19,18,.45);z-index:50;display:flex;align-items:center;justify-content:center;padding:18px;animation:fade .2s both}.chm .in{background:#F4F0EC;border-radius:16px;padding:18px;width:100%;box-shadow:0 10px 30px rgba(23,19,18,.2)}.chm h3{font-size:19px;font-weight:800;margin-bottom:4px}.chm .sub{font-size:12.5px;color:var(--mute);line-height:1.4;margin-bottom:12px}.chm .op{display:flex;gap:10px;align-items:center;background:#fff;border:1.5px solid var(--line);border-left:4px solid var(--c,#999);border-radius:11px;padding:10px 12px;margin-bottom:8px;cursor:pointer}.chm .op.on{border-color:var(--tealx);border-left-color:var(--tealx);background:#E1F1F2}.chm .op small{display:block;font-size:10.5px;font-weight:800;letter-spacing:.5px;color:var(--c,#999)}.chm .op b{font-size:14px;line-height:1.3}.chm .op .rd{margin-left:auto;flex:none;width:16px;height:16px;border-radius:50%;border:2px solid var(--line)}.chm .op.on .rd{border:5px solid var(--tealx)}.chm .go2{width:100%;margin-top:6px;background:var(--red,#D92D48);color:#fff;border:0;border-radius:11px;padding:12px;font-size:14.5px;font-weight:700;cursor:pointer}.chm .go2.off{opacity:.45;cursor:default}
.idea{display:flex;align-items:center;gap:8px;margin:4px 0 2px}.idea small{font-size:11px;font-weight:800;letter-spacing:.06em;color:var(--mute)}.idea b{font-size:12px;font-weight:800;background:var(--ink);color:#fff;border-radius:6px;padding:1px 6px}
.from2{font-size:13px;color:var(--mute);margin:6px 0}.from2 b{color:var(--ink)}
.sech{display:flex;align-items:baseline;gap:8px;margin:16px 2px 6px}.sech b{font-size:12px;font-weight:800;letter-spacing:.06em}.sech em{font-style:normal;font-size:12px;font-weight:700;color:var(--mute)}
.beat{display:flex;align-items:baseline;gap:6px;font-size:12px;font-weight:700;color:var(--mute);margin:0 0 4px}.beat b{color:var(--ink);font-size:12.5px}.beat span{color:var(--ink);text-transform:lowercase}.beat em{font-style:normal;margin-left:auto}
.cols+.cols .beat,.beatw{margin-top:6px}
.tele{cursor:pointer}
.rew{text-align:center;margin:22px 0 8px}.rew b{display:block;font-size:15px;margin-bottom:8px}.rew small{display:block;font-size:12px;color:var(--mute);margin-top:6px}.rew .btn{display:block}
.rew .btn.off{opacity:.45;pointer-events:none}
.obar3{display:flex;gap:8px;width:100%}.obar3 .btn{flex:1}
.cpm{position:absolute;right:16px;bottom:84px;background:#fff;border:1px solid var(--line);border-radius:12px;box-shadow:var(--sh-2);z-index:30;overflow:hidden;animation:rise .25s var(--ease) both}
.cpm div{padding:11px 16px;font-size:14px;font-weight:700;cursor:pointer}.cpm div+div{border-top:1px solid var(--hair)}
.tp{position:absolute;inset:0;background:#141110;color:#fff;z-index:40;display:flex;flex-direction:column;animation:fade .25s both}
.tp .tph{display:flex;justify-content:space-between;align-items:center;padding:18px 18px 8px}
.tp .tph span{font-size:13px;font-weight:800;cursor:pointer;background:rgba(255,255,255,.12);border-radius:999px;padding:6px 12px}
.tp .tpb{flex:1;overflow-y:auto;padding:30vh 24px 50vh;scroll-behavior:auto}
.tp .tpb p{font-size:26px;line-height:1.35;font-weight:800;margin:0 0 22px}
.multi3 .chip.off{opacity:.45}
.phone{overscroll-behavior:contain}
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
.out .menu{animation:unroll .34s var(--snap) both}
.out .blk,.out .btn,.out .ho,.out .gh span,.out .back{transition:transform .15s var(--ease),background .2s,box-shadow .2s,border-color .2s}
.out .btn:active,.out .ho:active,.out .back:active{transform:scale(.98)}
.out .blk:active{transform:scale(.99)}
.out .ho.sw{animation:rv .3s var(--out) var(--d,0ms) both}
</style></head><body>
<div class="wrap">
<div class="phone">

<!-- HOME (v5) -->
<div class="view home on" id="v-home"><div class="scr">
 <div class="top"><div class="logo">UGC<b>Breakouts</b></div><div class="tr"><div class="pro">Pro</div><span class="acct">Account</span></div></div>
 <div class="hi">Hi Veejay</div><h1>What are you filming next?</h1>
 <div class="card p" id="fcard"><div class="fhead"><div class="ct">Breakout Finder</div><div class="x" id="fclose" style="display:none">Close</div></div><div class="cs" id="fcs">High views from small accounts, in your niche</div>
  <div class="box" id="fbox"><input id="fq" placeholder="Search a product or #hashtag" autocomplete="off"><div class="go r" id="fgo">→</div></div>
  <div id="fdef"><div class="sml s" style="margin-top:14px">Suggested searches</div><div class="chips srch" style="margin-top:8px"><div class="chip">Lip liner</div><div class="chip">Self tanner</div><div class="chip">Heatless curls</div><div class="chip">Fridge restock</div></div></div>
  <div id="fopen" style="display:none"><div class="sug" id="fsug" style="display:none"></div>
   <div class="sml">Popular this week</div>
   <div class="chips srch" id="fpop" style="margin-top:0"></div></div></div>
 <div class="card t"><div class="ct">Write a script</div><div class="cs">Built from your profile</div>
  <div class="box" id="pbox"><input id="prod" placeholder="What's the product?" autocomplete="off"><div class="go g" id="pgo">→</div></div>
  <div class="sml s" style="margin-top:14px">Suggested products <span class="ptag">Proposal</span></div><div class="chips" style="margin-top:8px" id="pchips"><div class="chip tap">Moisturizer</div><div class="chip tap">Lip oil</div><div class="chip tap">Water bottle</div><div class="chip tap">Get ready with me</div></div>
  <div class="bbrief" id="bbrief"><span class="bi">PDF</span><span><b>Start from a brand brief</b><small>Paste it or upload a PDF</small></span><span class="chev">›</span></div></div>
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
<div class="nav tabnav" id="hnav"><span data-t="home" class="on">Home</span><span data-t="top">Breakouts</span><span data-t="script">Script</span><span data-t="lib">Library</span></div>
<div class="dim" id="dim" style="display:none"></div>
<div class="sheet" id="sheet" style="display:none">
 <div class="grab"></div>
 <div class="shead"><h1><span id="stitle">Lip oil</span> script <span style="font-size:15px;color:var(--mute);font-weight:600">✎</span></h1><div class="x" id="sclose">Close</div></div>
 <div class="sbody">
  <div class="bblock" id="bblock" style="display:none"><div class="qt">Brand brief</div>
   <textarea class="tx" id="btext" rows="3" placeholder="Paste the brand&rsquo;s brief"></textarea>
   <label class="bup">Upload a PDF<input type="file" id="bpdf" accept=".pdf,application/pdf"></label>
   <div class="bfile" id="bfile"><span id="bfname">brief.pdf</span><span class="rm" id="brm">Remove</span></div></div>
  <div class="q2"><div class="qt">How long?</div><div class="chips one" data-q="len"><div class="chip tap on">15s</div><div class="chip tap">30s</div><div class="chip tap">45s</div><div class="chip tap">60s</div><div class="chip tap">90s</div><div class="chip tap">120s+</div></div></div>
  <div class="q2"><div class="qt">How will you film it?</div><div class="chips one" data-q="film"><div class="chip tap on">Talking to camera</div><div class="chip tap">Voiceover + b-roll</div><div class="chip tap">Text on screen</div><div class="chip tap">Hands only</div><div class="chip tap">Day in my life</div><div class="chip tap">Get ready with me</div><div class="chip tap">Green screen</div><div class="chip tap">Skit</div><div class="chip tap">Street interview</div><div class="chip tap">Car talk</div><div class="chip tap own">+ Add your own</div></div><input class="tx ownx" maxlength="60" placeholder="How will you film it?"></div>
  <div class="q2"><div class="qt">What tone?</div><div class="chips one" data-q="tone"><div class="chip tap">Funny</div><div class="chip tap on">Calm and real</div><div class="chip tap">Hype</div><div class="chip tap">Story</div><div class="chip tap">Bestie chat</div><div class="chip tap">Teacher</div><div class="chip tap">Shocked</div><div class="chip tap">Honest review</div><div class="chip tap">Cozy</div><div class="chip tap">Dramatic</div><div class="chip tap own">+ Add your own</div></div><input class="tx ownx" maxlength="60" placeholder="Describe the tone"></div>
  <div class="more" id="more"><span>Add more detail<i style="font-style:normal;font-weight:600;color:var(--mute);font-size:12.5px;margin-left:6px">optional</i></span><span id="moreic">+</span></div>
  <div id="detail" style="display:none">
   <div class="q2"><div class="qt">What should the video do?</div><div class="chips one" data-q="do"><div class="chip tap">Sell it</div><div class="chip tap">Review it</div><div class="chip tap">How to use it</div><div class="chip tap">Before and after</div><div class="chip tap">Unboxing</div><div class="chip tap">Compare it</div><div class="chip tap own">+ Add your own</div></div><input class="tx ownx" maxlength="60" placeholder="What should it do?"></div>
   <div class="q2"><div class="qt">Hook that works</div><input class="tx" id="dhookin" placeholder="Paste a hook you know works"></div>
   <div class="q2"><div class="qt">Problem it solves</div><input class="tx" placeholder="What problem does it fix?"></div>
   <div class="q2"><div class="qt">Solution it gives</div><input class="tx" placeholder="How does it fix it?"></div>
   <div class="q2"><div class="qt">Must say</div><input class="tx" placeholder="Anything the video has to say"></div>
   <div class="q2"><div class="qt">Avoid saying</div><input class="tx" placeholder="Anything to leave out"></div>
   <div class="q2"><div class="qt">CTA</div><div class="chips one opt" data-q="cta"><div class="chip tap">Link in bio</div><div class="chip tap">Tap the orange cart</div><div class="chip tap">Comment for link</div><div class="chip tap">Follow for more</div><div class="chip tap own">+ Add your own</div></div><input class="tx ownx" maxlength="60" placeholder="Your CTA"></div>
  </div>
 </div>
 <div class="scta"><div class="btn o" id="skip">Skip</div><div class="btn g" style="flex:2" id="write">Write my script</div></div>
</div>
</div>

<!-- SEARCH PROCESSING (Ivan 6:18 AM: more entertaining) -->
<div class="view home" id="v-srch"><div class="scr">
 <div class="top"><div class="x" id="qback">← Home</div><div class="tr"><div class="pro">Pro</div><span class="acct">Account</span></div></div>
 <div class="qrow"><span>Searching</span><b id="qterm">lip oil</b><span class="qel" id="qel">0:00</span></div>
 <h2 class="qh" id="qh">Finding your Viral Breakouts</h2>
 <ol class="qsteps" id="qsteps"><li><span class="d">✓</span>Finding your Viral Breakouts</li><li><span class="d">✓</span>Calculating Breakout Score</li><li><span class="d">✓</span>Building strategy</li></ol>
 <div class="qstats"><div><b id="qn">0</b><small>videos checked</small></div><div><b id="qk">0</b><small>breakouts found</small></div></div>
 <div class="qfeedw"><div class="qscan"></div><div class="qfeed" id="qfeed"></div></div>
 <div class="qdone" id="qdone"><h3>Breakouts ready</h3><div class="btn g" id="qsee">See breakouts</div></div>
 <div class="hnote">Usually ~1-2 mins. Shortened in this mock.</div>
</div><div class="nav tabnav"><span data-t="home">Home</span><span data-t="top" class="on">Breakouts</span><span data-t="script">Script</span><span data-t="lib">Library</span></div></div>

<!-- SCREENS WE ARE NOT CHANGING (Ivan 6:18 AM) -->
<div class="view home" id="v-same"><div class="scr">
 <div class="top"><div class="x" id="sback">← Back</div><div class="tr"><div class="pro">Pro</div><span class="acct">Account</span></div></div>
 <h1 id="sametitle">Breakouts for "lip oil"</h1>
 <div class="same"><b>Same as live, not changing</b><span>This screen stays exactly as it is in the app today. Only Home, the Breakout Finder, Write a script and the script page change in this round.</span></div>
</div><div class="nav tabnav" id="samenav"><span data-t="home">Home</span><span data-t="top" class="on">Breakouts</span><span data-t="script">Script</span><span data-t="lib">Library</span></div></div>

<!-- WRITING -->
<div class="view" id="v-writing"><div class="proc" id="proc"><div class="top"><div class="logo" style="font-weight:800;font-size:17px">UGC<b style="color:#1FB2C2">Breakouts</b></div><div class="tr"><div class="pro">Pro</div><span class="acct">Account</span></div></div><div class="ptok"><span class="ti">✎</span><b id="wprod">Lip oil</b> · <span id="wsub">your own idea</span></div><div class="pline"><h2>Writing your script</h2><span class="ptag">Proposal</span><span class="pdone">✓</span></div><div class="pbar"><span><i style="--d:150ms"></i></span><span><i style="--d:700ms"></i></span><span><i style="--d:1250ms"></i></span></div><ol class="plab"><li><span class="dot"><i class="rg" style="--d:150ms"></i><i class="ok" style="--e:630ms">✓</i></span><span class="t" style="--d:150ms">Reading breakouts</span></li><li><span class="dot"><i class="rg" style="--d:700ms"></i><i class="ok" style="--e:1180ms">✓</i></span><span class="t" style="--d:700ms">Matching your answers</span></li><li><span class="dot"><i class="rg" style="--d:1250ms"></i><i class="ok" style="--e:1730ms">✓</i></span><span class="t" style="--d:1250ms">Writing each part</span></li></ol><div class="pmat"><div class="pscan"></div><div id="ings"></div></div><div class="pdraft" id="pdraft"><div class="dh"><small>HOOK</small><b id="dtype"></b><span class="cur"></span></div><div class="sk"><small>BODY</small><i style="--d:1500ms;width:92%"></i><i style="--d:1750ms;width:78%"></i><i style="--d:2000ms;width:85%"></i></div><div class="sk"><small>CTA</small><i style="--d:2300ms;width:60%"></i></div></div></div></div>

<!-- OUTPUT -->
<div class="view out" id="v-out"><div class="scr" id="oscr">
 <div class="top"><div class="back" id="oback">← Home</div><div class="tr"><div class="pro">Pro</div><span class="acct">Account</span></div></div>
 <div class="idea"><small>IDEA</small><b id="oidea">30s</b></div>
 <div class="srcl" id="osrc">From your idea</div>
 <h1>Lip oil script <span>✎</span></h1>
 <div class="meta"><div class="tag lay" id="otag"></div><span class="ptag">Proposal</span><div class="tag len" id="olen"></div><span class="stag">Sample script</span></div>
 <div class="from2" id="ofrom" style="display:none"></div>
 <div class="oing" id="oing"></div>
 <div class="ostart"><span>Your script starts here</span></div>
 <div class="hooks" id="hooks">__HOOKS__</div>
 <div id="obody"></div>
</div><div class="bar" id="obar"></div></div>

<div class="toast" id="toast"></div>
</div>

<div class="side">
 <h3>Script Writer flow (clickable)</h3>
 <p>Only the screens changing in this round are designed: Home, the Breakout Finder (with the search animation), Write a script (pop-up questions) and the script page. Everything else (search results, a breakout video, the Breakouts, Script and Library tabs, Account) shows a "Same as live, not changing" note with the live bottom bar.</p>
 <p>Questions follow Ivan&rsquo;s 25 Nov notes. Page 1 answers start preselected (15s, Talking to camera, Calm and real). Tap a picked chip again to clear it; any question can be left blank. &ldquo;What should the video do?&rdquo; now sits in Add more detail with nothing picked; left blank, the script is written as Sell it.</p><p>&ldquo;+ Add your own&rdquo; on filming, tone, what it should do and CTA opens a 60-character box. <span class="ptag">For Lester</span> Safety: the typed text only fills that one answer in the prompt, and the writer never repeats or explains its own instructions (for example &ldquo;give me your script making prompts&rdquo;).</p><p>Script page: what she picked and the idea sit in their own section at the top, then a line marks where the script starts. The hook choices at the top are gone. Like live, the script opens with 1 hook, and its pencil opens Change the hook (current hook, 1 Question, 1 Storytime; Rewrite my script uses 1 of 3 rewrites). More options in that pop-up: waiting on Ivan.</p>
 <p>Which script layout opens: Talking to camera, Get ready with me, Green screen and Car talk open 1; Voiceover + b-roll 2; Hands only 3; Text on screen 9; Day in my life and Skit 8; Street interview 11. With a talking, voiceover or hands-only video, Compare it (from Add more detail) opens 5, How to use it 6, Before and after 4. A brand brief opens 10.</p>
 <p>Handles, numbers and scripts are sample data; the search wait is shortened, and uploaded PDFs aren&rsquo;t read. Tagged Proposal: still open with Ivan.</p>
 <div class="lbl">Mock tools: see every layout</div>
 <div class="lays" id="lays"></div>
 <button class="restart" id="restart">Start over</button>
</div>
</div>

<script>
const L=__LAYOUTS__;
const SETS=__SETS__,GEN=__GEN__;let S=SETS['lip oil'],POOL=S.h2;
function setFor(p){const k=p.trim().toLowerCase();if(SETS[k])return SETS[k];const f=t=>t.split('{p}').join(k);const Lx={};for(const n in GEN.L)Lx[n]=GEN.L[n].map(f);return {L:Lx,hooks:{spoken:GEN.hooks.spoken.map(f),visual:GEN.hooks.visual.map(f),text:GEN.hooks.text.map(f)},h2:{question:GEN.h2.question.map(f),bold:GEN.h2.bold.map(f),story:GEN.h2.story.map(f)},x:GEN.x.map(e=>e.map(f)),generic:true}}
function titleCase(s){return s.replace(/\b([a-z])/g,c=>c.toUpperCase())}
function ans(q){const c=$('[data-q='+q+'] .chip.on');if(!c)return '';if(c.classList.contains('own'))return (c.closest('.q2').querySelector('.ownx').value||'').trim();return c.textContent}
function chosenLen(){const t=$('[data-q=len] .chip.on')?.textContent||'15s';return parseInt(t,10)||15}
let BRIEF=false;
const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
let product='lip oil',cur=2;
function show(id,dir){$$('.view').forEach(v=>{const on=v.id===id;v.classList.toggle('on',on);v.classList.remove('enter','back');if(on){void v.offsetWidth;v.classList.add(dir==='back'?'back':'enter')}})}
function toast(t){const e=$('#toast');e.textContent=t;e.classList.remove('on');void e.offsetWidth;e.classList.add('on');clearTimeout(e._t);e._t=setTimeout(()=>e.classList.remove('on'),1600)}
function stagger(list){[...list].forEach((el,i)=>{el.style.setProperty('--k',i);el.classList.remove('pin');void el.offsetWidth;el.classList.add('pin')})}
function cap(s){return s.charAt(0).toUpperCase()+s.slice(1)}
// home
function openSheet(p,brief){BRIEF=!!brief;$('#bblock').style.display=BRIEF?'block':'none';product=(p||'lip oil').trim().toLowerCase()||'lip oil';$('#stitle').textContent=BRIEF&&!(p||'').trim()?'Brand brief':cap(product);if(BRIEF&&!(p||'').trim())product='lip oil';const d=$('#dim'),s=$('#sheet');d.classList.remove('closing');s.classList.remove('closing');d.style.display='block';s.style.display='flex';s.querySelector('.sbody').scrollTop=0}
function closeSheet(now){const d=$('#dim'),s=$('#sheet');if(s.style.display==='none')return;if(now===true){d.style.display='none';s.style.display='none';return}d.classList.add('closing');s.classList.add('closing');clearTimeout(s._t);s._t=setTimeout(()=>{d.style.display='none';s.style.display='none';d.classList.remove('closing');s.classList.remove('closing')},260)}
$('#pgo').onclick=()=>openSheet($('#prod').value);
$('#prod').addEventListener('keydown',e=>{if(e.key==='Enter')openSheet($('#prod').value)});
$('#prod').addEventListener('focus',()=>$('#pbox').classList.add('ton'));
$('#prod').addEventListener('blur',()=>$('#pbox').classList.remove('ton'));
$$('#pchips .chip').forEach(c=>c.onclick=()=>{$('#prod').value=c.textContent;openSheet(c.textContent)});
$('#sclose').onclick=closeSheet;$('#dim').onclick=closeSheet;
$$('.chips.one').forEach(g=>g.querySelectorAll('.chip').forEach(c=>c.onclick=()=>{const was=c.classList.contains('on');g.querySelectorAll('.chip').forEach(x=>x.classList.remove('on'));if(!was)c.classList.add('on');const ox=g.parentNode.querySelector('.ownx');if(ox){const own=c.classList.contains('own')&&c.classList.contains('on');ox.style.display=own?'block':'none';if(own)ox.focus()}}));
$('#bbrief').onclick=()=>openSheet($('#prod').value,true);
$('#bpdf').onchange=e=>{const f=e.target.files[0];if(!f)return;$('#bfname').textContent=f.name;$('#bfile').classList.add('on')};
$('#brm').onclick=()=>{$('#bpdf').value='';$('#bfile').classList.remove('on')};
$$('.chips.multi .chip').forEach(c=>c.onclick=()=>c.classList.toggle('on'));
$$('.chips.multi3').forEach(g=>g.querySelectorAll('.chip').forEach(c=>c.onclick=()=>{if(!c.classList.contains('on')&&g.querySelectorAll('.chip.on').length>=3)return;c.classList.toggle('on');const full=g.querySelectorAll('.chip.on').length>=3;g.querySelectorAll('.chip').forEach(x=>x.classList.toggle('off',full&&!x.classList.contains('on')))}));
$('#more').onclick=()=>{const d=$('#detail'),o=d.style.display==='none';d.style.display=o?'block':'none';$('#moreic').textContent=o?'−':'+';if(o){[...d.children].forEach((q,i)=>{q.style.setProperty('--k',i);q.style.animation='none';void q.offsetWidth;q.style.animation=''});setTimeout(()=>{const sb=$('#sheet .sbody'),m=$('#more');sb.scrollTo({top:m.offsetTop-sb.offsetTop-8,behavior:'smooth'})},60)}};
// film / video-do -> layout (sample mapping, noted in the side panel)
const FILM2L={'Talking to camera':1,'Voiceover + b-roll':2,'Text on screen':9,'Hands only':3,'Day in my life':8,'Get ready with me':1,'Green screen':1,'Skit':8,'Street interview':11,'Car talk':1};
const DO2L={'Compare it':5,'How to use it':6,'Before and after':4};
function pickLayout(){
 if(BRIEF)return 10;
 const f=ans('film')||'Talking to camera',d=ans('do')||'Sell it';
 const fl=FILM2L[f]||11;
 if(DO2L[d]&&[1,2,3].includes(fl))return DO2L[d];
 return fl}
function write(){closeSheet(true);$('#wprod').textContent=BRIEF&&$('#stitle').textContent==='Brand brief'?'Brand brief':cap(product);
 const v=ans;
 $('#wsub').textContent=BRIEF?'brand brief':'your own idea';
 const ing=[['↗','Breaking out',cap(product)+' breakouts'],['▶','Video and filming',[v('do'),v('film').toLowerCase()].filter(Boolean).join(', ')||'Any'],['◷','Tone and length',[v('tone'),v('len')].filter(Boolean).join(', ')||'Any']];
 const D=[343,860,1377],E=[630,1180,1730];
 $('#ings').innerHTML=ing.map((x,i)=>'<div class="ing" style="--d:'+D[i]+'ms"><span class="oi">'+x[0]+'</span><span><small>'+x[1]+'</small><b>'+esc(x[2])+'</b></span><span class="ck" style="--e:'+E[i]+'ms">✓</span></div>').join('');
 const S0=setFor(product);const hk=($('#dhookin')?.value.trim())||(S0.h2&&S0.h2.question&&S0.h2.question[0])||'';
 const dt=$('#dtype');dt.textContent='';clearInterval(write._ti);clearTimeout(write._ts);
 write._ts=setTimeout(()=>{let i=0;write._ti=setInterval(()=>{dt.textContent=hk.slice(0,++i);if(i>=hk.length)clearInterval(write._ti)},Math.max(14,Math.min(32,1300/Math.max(1,hk.length))))},500);
 const pr=$('#proc');pr.classList.remove('go2');show('v-writing');void pr.offsetWidth;pr.classList.add('go2');
 clearTimeout(write._t);write._t=setTimeout(()=>{clearInterval(write._ti);render(pickLayout());show('v-out')},3200)}
$('#write').onclick=write;$('#skip').onclick=write;
// output
function words(t){return t.replace(/must-say ✓/,'').trim().split(/\s+/).length}
function lenOf(){const el=$('#obody');let n=0;const says=[...el.querySelectorAll('.blk .say,.verdict .say')].map(s=>s.textContent.trim());says.forEach(t=>n+=words(t));const h=el.querySelector('.hook');if(h&&/SPOKEN/.test(h.querySelector('small').textContent)){const ht=h.querySelector('b').textContent.trim();if(!says.includes(ht))n+=words(ht)}return n}
function setLen(l){const Y=chosenLen();$('#oidea').textContent=Y+'s';$('#olen').textContent=l.fixedLen?l.fixedLen.replace(/\b30 s\b/,Y+' s'):(()=>{const n=lenOf();return n+' words · about '+Math.round(n/2.5)+' s of '+Y+' s'})()}
let PENDING_HOOK=null,FROMV=null,REW={};
// ---- length: trim or extend so the spoken words fit the chosen length (about 2.5 words a second)
function wordsIn(el){return el?el.textContent.replace(/must-say ✓/,'').trim().split(/\s+/).filter(Boolean).length:0}
function spokenWords(){const b=$('#obody');let n=0;b.querySelectorAll('.blk .say,.verdict .say').forEach(x=>n+=wordsIn(x));const h=b.querySelector('.hook');if(h&&/SPOKEN|QUESTION|BOLD|STORY/.test(h.querySelector('small').textContent))n+=wordsIn(h.querySelector('b'));return n}
function parts(){const b=$('#obody');const kids=[...b.children].filter(e=>!e.matches('.tele,.must,.sech,.rew'));return {hook:kids[0],cta:kids[kids.length-1],body:kids.slice(1,-1)}}
function fitLength(n,spoken){if(!spoken)return;const Y=chosenLen(),max=Y*2.5,lo=max*0.82;
 let w=spokenWords();
 // trim: drop body beats from the end (never the must-say line), then shorten the longest line by sentences
 let guard=0;while(w>max&&guard++<20){const p=parts();if(p.body.length<2)break;const cand=p.body.slice().reverse().find(e=>!e.querySelector('.mk'));if(!cand)break;cand.remove();w=spokenWords()}
 guard=0;while(w>max&&guard++<20){const says=[...$('#obody').querySelectorAll('.blk .say,.verdict .say')];const long=says.sort((a,b)=>wordsIn(b)-wordsIn(a))[0];if(!long)break;const sent=long.textContent.match(/[^.!?]+[.!?]+/g)||[];if(sent.length<2)break;long.textContent=sent.slice(0,-1).join('').trim();w=spokenWords()}
 // extend: add product lines as extra body beats before the CTA
 const X=S.x||[];let xi=0;guard=0;
 while(w<lo&&xi<X.length&&guard++<20){const ex=X[xi++];const add=ex[0].split(/\s+/).length;if(w+add>max)continue;const p=parts();const tplEl=[...p.body].reverse().find(e=>e.matches('.blk')&&e.querySelector('.say'))||p.body[p.body.length-1];if(!tplEl)break;
  const c=tplEl.cloneNode(true);c.classList.remove('sel');c.querySelector('.menu')?.remove();const sy=c.querySelector('.say');sy.textContent=ex[0];const sh=c.querySelector('.shot');if(sh){const pre=sh.querySelector('b');sh.textContent=' '+ex[1];if(pre)sh.prepend(pre);}
  c.dataset.extra='1';const t=c.querySelector('.t');if(t&&!/^\d+ OF \d+$/.test(t.textContent))t.textContent='';c.querySelector('.mk')?.remove();
  p.cta.before(c);w=spokenWords()}
 // keep numbering honest after trimming or extending
 const p=parts();let k=0;p.body.forEach(e=>{const kk=e.querySelector('.num .k,.k');if(e.matches('.num')&&kk)kk.textContent=++k});
 const items=p.body.filter(e=>{const t=e.querySelector('.t');return t&&/^\d+ OF \d+$/.test(t.textContent)});items.forEach((e,i)=>e.querySelector('.t').textContent=(i+1)+' OF '+items.length);
 const hb=p.hook&&p.hook.querySelector('b');if(items.length&&hb&&/^\d+ things/.test(hb.textContent))hb.textContent=hb.textContent.replace(/^\d+/,items.length)}
// ---- live Hook / Body / CTA sections with time ranges, numbered and named beats
function clause(x){return (x||'').replace(/✎/g,'').replace(/^\s*(SAY|Clip:|Shot:|Any shots:)\s*/i,'').split(/[,.;!?]/)[0].trim().split(/\s+/).slice(0,5).join(' ').toLowerCase()}
function beatName(e){if(e.dataset&&e.dataset.extra){const sh=e.querySelector('.shot');const t0=e.querySelector('.t');if(t0&&/^\d+ OF \d+$/.test(t0.textContent.trim())){t0.style.display='none';return t0.textContent.trim().toLowerCase()}if(t0&&!t0.textContent.trim())t0.style.display='none';return sh?clause(sh.textContent):'closing line'}
 const t=e.querySelector(':scope > .t')||e.querySelector('.t');const raw=t?t.textContent.trim():'';
 if(e.matches('.cols')){const a=e.querySelector('.t');return a?a.textContent.replace(/^A · /,'').toLowerCase():'side by side'}
 if(raw&&!/^(SAY|BODY|\d+ TO \d+ S)$/.test(raw)){if(t)t.style.display='none';return raw.toLowerCase()}
 if(t&&/^\d+ TO \d+ S$/.test(raw))t.style.display='none';
 const k=e.querySelector('.k');if(e.matches('.slide')&&k){k.style.display='none';return k.textContent.toLowerCase()}
 if(t&&/^SAY$/i.test(raw))t.style.display='none';const sh=e.querySelector('.shot');return clause(sh?sh.textContent:(e.querySelector('.say')||e).textContent)}
function sectionize(n){const Y=chosenLen(),p=parts();if(!p.hook||!p.cta||p.hook===p.cta)return;
 const h=Y<=15?2:3,c=Y-Math.max(3,Math.round(Y*0.23)),bs=h+1,be=c-1;
 const sec=(lab,a,b)=>{const d=document.createElement('div');d.className='sech';d.innerHTML='<b>'+lab+'</b><em>'+a+'–'+b+'s</em>';return d};
 p.hook.before(sec('HOOK',0,h));if(p.body.length)p.body[0].before(sec('BODY',bs,be));p.cta.before(sec('CTA',c,Y));
 const wts=p.body.map(e=>Math.max(3,wordsIn([...e.querySelectorAll('.say')].map(x=>x.textContent).join(' ')?e:null)||3));
 const tot=wts.reduce((a,b)=>a+b,0)||1;let t0=bs;
 p.body.forEach((e,i)=>{const span=(be-bs+1)*wts[i]/tot;const a=Math.round(t0),b=i===p.body.length-1?be:Math.max(a,Math.round(t0+span)-1);t0+=span;
  const lab=document.createElement('div');lab.className='beat';lab.innerHTML='<b>'+(i+1)+'</b><span>'+esc(beatName(e))+'</span><em>'+a+'–'+b+'s</em>';
  if(e.matches('.cols'))e.before(lab);else e.prepend(lab)})}
// ---- live Practice full screen, Save script / Share / Copy, Rewrite the whole script
function decorate(n,spoken){const b=$('#obody');let t=b.querySelector('.tele');
 if(spoken){if(!t){t=document.createElement('div');t.className='tele';b.prepend(t)}t.textContent='Practice full screen';t.onclick=openTP}else if(t)t.remove();
 const key=product+'|'+n;if(REW[key]==null)REW[key]=3;
 const r=document.createElement('div');r.className='rew';r.innerHTML='<b>Not quite right?</b><div class="btn o'+(REW[key]?'':' off')+'" id="rewb">Rewrite the whole script</div><small id="rewn">'+REW[key]+' of 3 rewrites left</small>';b.append(r);
 r.querySelector('#rewb').onclick=()=>{if(!REW[key])return;REW[key]--;const sc=$('#oscr');const y=sc.scrollTop;render(n);sc.scrollTop=y;toast('Rewritten (sample script)')};
 const bar=$('#obar');bar.innerHTML='<div class="obar3"><div class="btn o" id="bsave">Save script</div><div class="btn o" id="bshare">Share</div><div class="btn g" id="bcopy">Copy</div></div>';
 $('#bsave').onclick=()=>{saveScript(n);toast('Saved to your Library')};
 $('#bshare').onclick=()=>toast("Opens the phone's share sheet (mock)");
 $('#bcopy').onclick=e=>{e.stopPropagation();$$('.cpm').forEach(m=>m.remove());const m=document.createElement('div');m.className='cpm';m.innerHTML='<div data-c="all">Copy script</div>'+(spoken?'<div data-c="say">Copy spoken lines</div>':'');$('#v-out').append(m);
  m.querySelectorAll('div').forEach(o=>o.onclick=()=>{m.remove();toast(o.dataset.c==='say'?'Spoken lines copied':'Script copied')});setTimeout(()=>document.addEventListener('click',()=>m.remove(),{once:true}),0)};
 const fr=$('#ofrom');if(FROMV){fr.style.display='';fr.innerHTML='From a breakout · <b>'+esc(FROMV.h)+'</b> · '+esc(FROMV.x.split(' ')[0])+' their usual views'}else fr.style.display='none'}
function saveScript(n){if(typeof SCRIPTS!=='undefined'&&!SCRIPTS.find(x=>x.p===product&&x.n===n&&x.saved)){SCRIPTS.unshift({p:product,n,when:'Just now',saved:true,src:FROMV?'Breakout':'Your idea',status:'Ready'})}}
function openTP(){const lines=[];const b=$('#obody');const h=b.querySelector('.hook b');if(h&&/SPOKEN|QUESTION|BOLD|STORY/.test(b.querySelector('.hook small')?.textContent||''))lines.push(h.textContent);
 b.querySelectorAll('.blk .say,.verdict .say').forEach(x=>lines.push(x.textContent.replace(/must-say ✓/,'').trim()));
 const tp=document.createElement('div');tp.className='tp';tp.innerHTML='<div class="tph"><span id="tpp">Pause</span><span id="tpx">Close</span></div><div class="tpb">'+lines.map(t=>'<p>'+esc(t)+'</p>').join('')+'</div>';$('#v-out').append(tp);
 const body=tp.querySelector('.tpb');let run=true;const step=()=>{if(!tp.isConnected)return;if(run)body.scrollTop+=0.6;requestAnimationFrame(step)};requestAnimationFrame(step);
 tp.querySelector('#tpp').onclick=()=>{run=!run;tp.querySelector('#tpp').textContent=run?'Pause':'Play'};tp.querySelector('#tpx').onclick=()=>tp.remove()}
const IDEA={'Sell it':'Show {p} fixing one everyday problem, then where to get it.','Review it':'An honest first take on {p}: what works and what doesn\'t.','How to use it':'Walk through using {p}, step by step.','Before and after':'Show the before, use {p}, then the after.','Unboxing':'Open {p} on camera and try it for the first time.','Compare it':'Put {p} next to what people use now and pick a winner.'};
function fillIng(){const pr=cap(product),d=ans('do');const chips=[BRIEF?'Brand brief':'',pr,ans('len'),ans('film'),ans('tone'),d,ans('cta'),($('#dhookin')?.value.trim())?'Your hook':''].filter(Boolean);
 const idea=BRIEF?'Turn the brand brief into a '+chosenLen()+'s script that covers every must-say.':(IDEA[d]||('A '+chosenLen()+'s video about '+product+(d?': '+d.toLowerCase():'')+'.')).replace('{p}',product);
 $('#oing').innerHTML='<div class="oh">What you picked</div><div class="oc">'+chips.map(c=>'<span>'+esc(c)+'</span>').join('')+'</div><div class="oi"><div class="oh" style="margin:0">The idea</div><p>'+esc(idea)+'</p></div>'}

// live (checked 25 Nov): pencil on the hook opens "Change the hook": current hook + 1 Question + 1 Storytime, Rewrite my script uses 1 of 3 rewrites
const PEN='<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 20h4L19 9l-4-4L4 16z"/></svg>';
function hookPen(n){const hk=$('#obody .hook');if(!hk)return;const p=document.createElement('span');p.className='hpen';p.innerHTML=PEN;p.title='Change the hook';p.onclick=e=>{e.stopPropagation();openCH(n)};hk.append(p)}
function openCH(n){const hk=$('#obody .hook');const curH=hk.querySelector('b').textContent;const key=product+'|'+n;const left=REW[key]==null?3:REW[key];
 const q=(POOL.question||[]).find(h=>norm(h)!==norm(curH))||'',st=(POOL.story||[]).find(h=>norm(h)!==norm(curH))||'';
 const ops=[['YOUR CURRENT HOOK',curH,'var(--tealx)',1],['QUESTION',q,'#5B4FD6'],['STORYTIME',st,'#C2410C']].filter(o=>o[1]);
 const m=document.createElement('div');m.className='chm';
 m.innerHTML='<div class="in"><h3>Change the hook</h3><div class="sub">A new hook rewrites the whole script. It uses 1 of your 3 rewrites ('+left+' left).</div>'+ops.map((o,i)=>'<div class="op'+(o[3]?' on':'')+'" style="--c:'+o[2]+'" data-i="'+i+'"><div><small>'+o[0]+'</small><b>'+esc(o[1])+'</b></div><span class="rd"></span></div>').join('')+'<button class="go2 off">Rewrite my script</button></div>';
 $('#v-out').append(m);let pick=0;const go=m.querySelector('.go2');
 m.onclick=e=>{if(e.target===m)m.remove()};
 m.querySelectorAll('.op').forEach(o=>o.onclick=()=>{pick=+o.dataset.i;m.querySelectorAll('.op').forEach(x=>x.classList.toggle('on',x===o));go.classList.toggle('off',pick===0||!left)});
 go.onclick=()=>{if(pick===0||!left)return;const o=ops[pick];REW[key]=left-1;hk.querySelector('small').textContent='HOOK · '+o[0];hk.querySelector('b').textContent=o[1];const rn=$('#rewn');if(rn)rn.textContent=REW[key]+' of 3 rewrites left';m.remove();setLen(L[cur]);toast('Rewritten with the new hook (sample: only the hook changes in this mock)')}}
function render(n){cur=n;fillIng();const l=L[n];S=setFor(product);POOL=S.h2;$('#otag').textContent=l.tag;$('#obody').innerHTML=l.tpl.replace(/\{\{(\d+)\}\}/g,(m,i)=>esc(S.L[n][+i]));const spoken=/Copy spoken lines/.test(l.bar);fitLength(n,spoken);sectionize(n);decorate(n,spoken);hookPen(n);setLen(l);
 const p=$('#oscr h1');p.innerHTML=esc(S.generic?titleCase(product):cap(product))+' script <span>✎</span>';
 const fv=ans('film').toLowerCase();
 $('#hooks .from').innerHTML='Built from: <b>your answers</b> · <b>'+product+'</b>'+(fv?' · <b>'+esc(fv)+'</b>':'')+(BRIEF?' · <b>the brief</b>':'');
 $('#osrc').textContent=BRIEF?'From a brief':'From your idea';
 resetHooks();
 $('#oscr').scrollTop=0;wireOut();$$('#lays button').forEach(b=>b.classList.toggle('on',+b.dataset.n===n));
 [...$('#hooks').children,...$('#obody').children].forEach((el,i)=>{el.classList.remove('rv');el.style.setProperty('--d',Math.min(120+i*60,700)+'ms');void el.offsetWidth;el.classList.add('rv')})}
function wireOut(){
 function pick(m){m.querySelectorAll('div').forEach(o=>o.onclick=()=>{m.querySelectorAll('div').forEach(x=>x.classList.remove('picked'));o.classList.add('picked');toast(o.textContent+': rewrites only this line')})}
 $$('#obody .menu').forEach(pick);
 $$('#obody .blk').forEach(b=>b.onclick=e=>{if(e.target.closest('.menu'))return;const open=b.querySelector('.menu');$$('#obody .menu').forEach(m=>m.remove());$$('#obody .blk.sel').forEach(x=>x.classList.remove('sel'));$$('#obody .pen').forEach(x=>x.style.display='');if(open)return;b.classList.add('sel');const pen=b.querySelector('.pen');if(pen)pen.style.display='none';const m=document.createElement('div');m.className='menu';m.innerHTML='<div>Shorter</div><div>Punchier</div><div>More like me</div><div>Redo</div>';(b.classList.contains('num')?b.lastElementChild:b).appendChild(m);pick(m)});
 $$('#obody .mi .add').forEach(a=>a.onclick=()=>{a.outerHTML='<span class="y">✓</span>';toast('Added to the script')});
 $$('#obar .btn').forEach(b=>b.onclick=()=>toast('Copied'));
}
// hooks
const groups=$$('#hooks .hg');const keys=['question','bold','story'];const off=[0,0,0];
groups.forEach((g,i)=>{g.querySelector('.gh span').onclick=()=>{off[i]=(off[i]+3)%POOL[keys[i]].length;const hs=g.querySelectorAll('.ho');hs.forEach((h,j)=>{h.textContent=POOL[keys[i]][(off[i]+j)%POOL[keys[i]].length];h.classList.remove('on','sw');h.style.setProperty('--d',(j*60)+'ms');void h.offsetWidth;h.classList.add('sw')})};
 g.addEventListener('click',e=>{const h=e.target.closest('.ho');if(!h)return;$$('#hooks .ho').forEach(x=>x.classList.remove('on'));h.classList.add('on');const hk=$('#obody .hook');if(hk){hk.querySelector('small').textContent='HOOK · '+['QUESTION','BOLD CLAIM','STORYTIME'][i];hk.querySelector('b').textContent=h.textContent;setLen(L[cur])}else{toast('Hook goes to the top of the script')}})});
function norm(t){return t.trim().replace(/\.$/,'').toLowerCase()}
function resetHooks(){const hk=$('#obody .hook b');const cur_=hk?norm(hk.textContent):'';groups.forEach((g,i)=>{off[i]=0;g.querySelectorAll('.ho').forEach((h,j)=>{h.textContent=POOL[keys[i]][j];h.classList.toggle('on',!!cur_&&norm(h.textContent)===cur_)})})}
$('#oback').onclick=()=>{show('v-home','back')};
// layout switcher
const lays=$('#lays');Object.keys(L).forEach(k=>{const b=document.createElement('button');b.dataset.n=k;b.textContent=k+'. '+L[k].label;b.onclick=()=>{render(+k);show('v-out')};lays.appendChild(b)});
$('#restart').onclick=()=>{clearTimeout(write._t);clearInterval(SRCH.i);clearInterval(SRCH.c);clearTimeout(SRCH.t);closeSheet(true);closeFinder();$('#prod').value='';show('v-home','back')};
// finder (in place)
const POP=[["Lip liner","Get ready with me","Self tanner","Fridge restock","Heatless curls","Advent calendar","Skincare routine"],["Lip oil","Concealer","Water bottle","Mini fridge","Day in my life","Moisturizer"]];let popi=0;
function drawPop(){const f=$('#fpop');f.innerHTML=POP[popi].map(t=>'<div class="chip">'+t+'</div>').join('')+'<div class="chip add" id="fmore">↻ More</div>';
 f.querySelectorAll('.chip:not(.add)').forEach(c=>c.onclick=()=>openRes(c.textContent));$('#fmore').onclick=()=>{popi=(popi+1)%POP.length;drawPop()};stagger(f.children)}
function openFinder(){if($('#fopen').style.display==='block')return;$('#fcard').classList.add('lift');$('#fclose').style.display='';$('#fcs').style.display='none';$('#fdef').style.display='none';$('#fopen').style.display='block';$('#fbox').classList.add('on');$('#fdim').style.display='block';$('#v-home .scr').scrollTop=0;$('#v-home .scr').classList.add('flock');const fo=$('#fopen');fo.classList.remove('ris');void fo.offsetWidth;fo.classList.add('ris');drawPop();drawSug()}
function closeFinder(){$('#fcard').classList.remove('lift');$('#fclose').style.display='none';$('#fcs').style.display='';$('#fdef').style.display='';$('#fopen').style.display='none';$('#fbox').classList.remove('on');$('#fdim').style.display='none';$('#v-home .scr').classList.remove('flock');$('#fq').value='';$('#fq').blur()}
function esc(t){return t.replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]))}
function drawSug(){const q=$('#fq').value.trim().toLowerCase(),b=$('#fsug');if(!q){b.style.display='none';b.innerHTML='';b._shown=0;return}
 const TERMS=['lip oil','lip liner','self tanner','fridge restock','heatless curls','advent calendar','skincare routine','get ready with me','concealer','water bottle','mini fridge','day in my life','moisturizer'];const base=TERMS.find(t=>t.startsWith(q))||q;const items=[base,base+' swatch',base+' review'];
 b.innerHTML=items.map((t,i)=>'<div class="sg" data-t="'+esc(t)+'"><span><em>'+esc(q)+'</em>'+esc(t.slice(q.length))+'</span><small>'+(i===0?'breakouts ready':'')+'</small></div>').join('');b.style.display='block';
 b.querySelectorAll('.sg').forEach(r=>r.onclick=()=>openRes(r.dataset.t));if(!b._shown){b._shown=1;b.classList.remove('ris');void b.offsetWidth;b.classList.add('ris')}}
let PREV='v-home';
function curView(){return ($$('.view').find(v=>v.classList.contains('on'))||{}).id||'v-home'}
function setNav(nav,t){nav.querySelectorAll('span').forEach(x=>x.classList.toggle('on',x.dataset.t===t))}
function openSame(title,tab){const c=curView();if(c!=='v-same')PREV=c==='v-srch'?'v-home':c;$('#sametitle').textContent=title;setNav($('#samenav'),tab||'');show('v-same')}
const TABT={top:'Breakouts',script:'Script',lib:'Library'};
let SRCH={};
function openRes(t){t=t.trim();if(!t)return;closeFinder();clearInterval(SRCH.i);clearInterval(SRCH.c);clearTimeout(SRCH.t);
 $('#qterm').textContent=t.toLowerCase();$('#qdone').classList.remove('on');$('#qn').textContent='0';$('#qk').textContent='0';$('#qel').textContent='0:00';$('#qh').textContent='Finding your Viral Breakouts';
 const st=$$('#qsteps li');st.forEach(x=>x.classList.remove('qon','qok'));st[0].classList.add('qon');
 const C=['#C9B8AE','#B9C7C2','#C7B9CF','#D6C6B0','#BCC8D6','#CBBFB3','#B7C4B5','#D2BCC2','#C4C0D4'];
 const tiles=[];for(let i=0;i<18;i++)tiles.push('<div class="qtile" style="background:'+C[i%9]+'"><i></i><span class="ok">✓</span></div>');
 const fd=$('#qfeed');fd.innerHTML=tiles.join('')+tiles.join('');
 const T=[...fd.children];let k=0,n=0,hits=0;const t0=Date.now();
 SRCH.c=setInterval(()=>{const sec=Math.floor((Date.now()-t0)/1000);$('#qel').textContent='0:'+String(sec).padStart(2,'0')},250);
 SRCH.i=setInterval(()=>{const el=T[k%18],el2=T[k%18+18];const hit=[2,7,11,16].includes(k%18);[el,el2].forEach(e=>e.classList.add(hit?'hit':'no'));if(hit)hits++;n+=37+((k*53)%41);$('#qn').textContent=n.toLocaleString();$('#qk').textContent=hits;k++;
  const el_=Date.now()-t0;if(el_>1300&&!st[1].classList.contains('qon')&&!st[1].classList.contains('qok')){st[0].classList.replace('qon','qok');st[1].classList.add('qon');$('#qh').textContent='Calculating Breakout Score'}
  if(el_>2600&&!st[2].classList.contains('qon')&&!st[2].classList.contains('qok')){st[1].classList.replace('qon','qok');st[2].classList.add('qon');$('#qh').textContent='Building strategy'}},150);
 SRCH.t=setTimeout(()=>{clearInterval(SRCH.i);clearInterval(SRCH.c);st.forEach(x=>{x.classList.remove('qon');x.classList.add('qok')});$('#qh').textContent='Breakouts ready';$('#qdone').classList.add('on')},3800);
 $('#qsee').onclick=()=>{PREV='v-home';openSame('Breakouts for "'+t.toLowerCase()+'"','top')};
 show('v-srch')}
$('#qback').onclick=()=>{clearInterval(SRCH.i);clearInterval(SRCH.c);clearTimeout(SRCH.t);show('v-home','back')};
$('#sback').onclick=()=>show(PREV||'v-home','back');
$$('.tabnav').forEach(nv=>nv.querySelectorAll('span').forEach(sp=>sp.onclick=()=>{const t=sp.dataset.t;if(t==='home'){clearInterval(SRCH.i);clearInterval(SRCH.c);clearTimeout(SRCH.t);show('v-home','back');return}PREV='v-home';openSame(TABT[t],t)}));
$$('.acct').forEach(a=>a.onclick=()=>openSame('Account',''));
$('#fq').addEventListener('focus',openFinder);$('#fbox').onclick=openFinder;$('#fq').addEventListener('input',drawSug);
$('#fq').addEventListener('keydown',e=>{if(e.key==='Enter')openRes($('#fq').value)});
$('#fgo').onclick=e=>{e.stopPropagation();if($('#fopen').style.display==='block'&&$('#fq').value.trim())openRes($('#fq').value);else{openFinder();$('#fq').focus()}};
$('#fclose').onclick=e=>{e.stopPropagation();closeFinder()};$('#fdim').onclick=closeFinder;
$$('#fdef .chip').forEach(c=>c.onclick=()=>openRes(c.textContent));
$$('.srchl .li').forEach(r=>r.onclick=()=>openRes(r.querySelector('.lt').firstChild.textContent));
$$('#v-home .sec2 .chips.srch .chip').forEach(c=>c.onclick=()=>openRes(c.textContent));
$$('#thumbs .th').forEach(t=>t.onclick=()=>openSame('Breakout video','top'));
(function(){const ph=document.querySelector('.phone');if(!ph)return;
 function activeScroller(){const sh=$('#sheet');if(sh&&getComputedStyle(sh).display!=='none')return sh.querySelector('.sbody');
  const v=[...document.querySelectorAll('.view')].find(v=>getComputedStyle(v).display!=='none');return v?v.querySelector('.scr'):null}
 function canScroll(el,dy){return el&&el.scrollHeight>el.clientHeight+1&&(dy>0?el.scrollTop<el.scrollHeight-el.clientHeight-1:el.scrollTop>0)}
 ph.addEventListener('wheel',e=>{const tgt=activeScroller();if(!tgt)return;if(tgt.classList.contains('flock')){e.preventDefault();return}
  let n=e.target;while(n&&n!==ph){if(n!==tgt&&canScroll(n,e.deltaY)&&/(auto|scroll)/.test(getComputedStyle(n).overflowY))return;if(n===tgt){if(!canScroll(tgt,e.deltaY)&&modalOpen())e.preventDefault();return}n=n.parentElement}
  e.preventDefault();tgt.scrollTop+=e.deltaMode===1?e.deltaY*16:e.deltaY},{passive:false});
 function modalOpen(){return getComputedStyle($('#sheet')).display!=='none'||!!document.querySelector('.tp')||$('#fopen').style.display==='block'}
 let ty=0;ph.addEventListener('touchstart',e=>{ty=e.touches[0].clientY},{passive:true});
 ph.addEventListener('touchmove',e=>{if(!modalOpen())return;const dy=ty-e.touches[0].clientY;let n=e.target;while(n&&n!==ph){if(canScroll(n,dy)&&/(auto|scroll)/.test(getComputedStyle(n).overflowY))return;n=n.parentElement}e.preventDefault()},{passive:false});
})();

</script>
</body></html>'''

page = (page.replace('__HOOKS__', hooks_html)
            .replace('__LAYOUTS__', json.dumps(layouts, ensure_ascii=False))
            .replace('__SETS__', json.dumps(SETS_JS, ensure_ascii=False))
            .replace('__GEN__', json.dumps(GEN_JS, ensure_ascii=False)))
open(os.path.join(HERE, 'index.html'), 'w').write(page)
print('ok', len(page), 'layouts', len(layouts))
