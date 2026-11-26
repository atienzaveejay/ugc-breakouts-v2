# Script output: 2 options for Ivan (26 Nov), drawn with the live script page's own CSS
# (copied from ugcbreakouts.com into ../script-writer-flow/live-script.css). Same lip oil product throughout.
import html as H, json
E=H.escape
D=__file__.replace('build.py','')
LIVE=open(D+'../script-writer-flow/live-script.css').read().replace(':is(#v-out,#v-hook) .bk','.lvp .bk')
IC={'back':'<svg class="i" viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7"></path></svg>',
 'bulb':'<svg viewBox="0 0 24 24"><path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"></path></svg>',
 'save':'<svg viewBox="0 0 24 24"><path d="M7 4h10v16l-5-3.6L7 20z"></path></svg>',
 'share':'<svg viewBox="0 0 24 24"><circle cx="18" cy="5" r="2.5"></circle><circle cx="6" cy="12" r="2.5"></circle><circle cx="18" cy="19" r="2.5"></circle><path d="M8.2 10.8l7.6-4.4M8.2 13.2l7.6 4.4"></path></svg>',
 'copy':'<svg viewBox="0 0 24 24"><rect x="8" y="8" width="12" height="12" rx="2"></rect><path d="M16 8V5a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v10a1 1 0 0 0 1 1h3"></path></svg>',
 'pen':'<svg viewBox="0 0 24 24"><path d="M4 20h4L19 9l-4-4L4 16z"></path></svg>',
 'cam':'<svg viewBox="0 0 24 24"><path d="M4 8h3l1.5-2h7L17 8h3v11H4z"></path><circle cx="12" cy="13" r="3.5"></circle></svg>',
 'prac':'<svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"></path></svg>'}
q=lambda s:'“'+E(s)+'”'
def dirn(s): return f'<p class="sc-dir">{IC["cam"]}{E(s)}</p>' if s else ''
def ph(label,t,pen=True): return f'<div class="sc-ph"><b>{E(label)}</b><span class="tm">{E(t)}</span>'+(f'<button class="sc-ed" aria-label="Edit">{IC["pen"]}</button>' if pen else '')+'</div>'
def line(s,kind='say'):
    if kind=='screen': return f'<p class="sc-q2 os-line"><span class="ostag">On screen</span>{E(s)}</p>'
    return f'<p class="sc-q2">{q(s)}</p>'
def head(idea,secs,picked):
    chips=''.join(f'<span>{E(c)}</span>' for c in picked)
    return (f'<div class="sc-tb2"><button class="ib">{IC["back"]}</button><span class="tt">Your script</span></div><div class="sc-pad sc-out">'
     f'<section class="sc-ideac"><div class="sc-ih"><span class="bulb">{IC["bulb"]}</span><b>IDEA</b><span class="len">{E(secs)}</span></div><h1>{E(idea)}</h1>'
     f'<div class="lv-ing"><small>What you picked</small><div>{chips}</div></div></section><div class="lv-start"><span>Your script starts here</span></div><div class="sc-pts">')
def hook(t,s,shot,kind='say'):
    body=f'<p class="sc-q1">{q(s)}</p>' if kind=='say' else f'<p class="sc-q1 os-line"><span class="ostag">On screen</span>{E(s)}</p>'
    return f'<section class="sc-hookc">{ph("Hook",t)}{body}{dirn(shot)}</section>'
def step(n,name,t,s,shot='',kind='say',shot_first=False):
    L=line(s,kind);S=dirn(shot)
    return f'<div class="sc-step"><div class="sc-sp"><span class="sn">{n}</span><b>{E(name)}</b><span class="tm">{E(t)}</span><button class="sc-ed">{IC["pen"]}</button></div>'+(S+L if shot_first else L+S)+'</div>'
def body(t,steps,top_shot='',label='Body'):
    return f'<section class="sc-bodyc">{ph(label,t,False)}{dirn(top_shot)}{"".join(steps)}</section>'
def part(title): return f'<div class="lv-part">{E(title)}</div>'
def cta(t,s,shot,kind='say'):
    b=f'<p class="sc-q1">{q(s)}</p>' if kind=='say' else f'<p class="sc-q1 os-line"><span class="ostag">On screen</span>{E(s)}</p>'
    return f'<section class="sc-ctac">{ph("CTA",t)}{b}{dirn(shot)}</section>'
def tail(spoken=True,note=''):
    n=f'<p class="lv-note">{E(note)}</p>' if note else ''
    pr=f'<button class="b b2 full-w sc-prac-btn">{IC["prac"]}Practice full screen</button>' if spoken else ''
    return f'</div>{n}{pr}<div class="sc-rw"><b>Not quite right?</b><button class="b b2">Rewrite the whole script</button><small>3 of 3 rewrites left</small></div></div>'
SELL_IDEA='why I switched to lip oil'
def s15_sell():
    return head(SELL_IDEA,'15 s',['Lip oil','15s','Talking to camera','Calm and real'])+hook('0–2s','Watch what one coat of this lip oil does.','Close up, the lip oil by your face')+\
     body('3–11s',[step(1,'the problem','3–7s','My lips get dry by lunch, and most glosses just sit on top.','Talking, bare lips'),step(2,'show it','8–11s','The shine looks natural in daylight, not wet.','Lips by the window')])+\
     cta('12–15s',"It's on TikTok Shop. Tap the orange cart.",'Product to camera')+tail()
def s60_sell(grouped=True):
    P=[('Part 1 · The problem',[('talking','3–9s','My lips get dry by lunch, and every gloss I own just sits on top and gets sticky.','Talking, bare lips'),('the old stuff','9–15s','I tried balms too, but they look flat on camera, and I end up putting gloss on top anyway.','Hold up an old gloss and a balm')]),
       ('Part 2 · Show it',[('apply','15–24s',"One coat, straight from the wand. It goes on clear with a little tint, and it doesn't smell like candy.",'Close up, applying'),('finish','24–32s',"Press your lips together, and that's it. No liner, no top coat.",'Close up, pressing lips'),('daylight','32–38s','Here it is by the window. It looks like my lips, just healthier.','Lips by the window')]),
       ('Part 3 · Proof',[('hours later','38–46s',"I put this on at 9 this morning. It's now 1.",'Phone clock on screen, then lips'),('proof','46–52s',"Still shiny, and I've had two coffees and a sandwich. No reapplying.",'Mug in frame, lips close up')])]
    st=[];n=0
    for title,items in P:
        if grouped: st.append(part(title))
        for nm,t,s,sh in items: n+=1;st.append(step(n,nm,t,s,sh))
    return head('one coat, four hours','60 s',['Lip oil','60s','Talking to camera','Calm and real'])+hook('0–3s','Watch what one coat of this lip oil does.','Close up, the lip oil by your face')+\
     body('3–52s',st)+cta('52–60s',"If your gloss gets sticky too, this is the one. It's on TikTok Shop, tap the orange cart.",'Product to camera')+tail()
def s15_compare():
    return head('lip oil vs gloss','15 s',['Lip oil','15s','Talking to camera','Compare it'])+hook('0–2s','Lip oil or gloss? I wore both for a day.','Hold one in each hand')+\
     body('3–12s',[step('A','gloss','3–6s','Looked great at 9. By 11 my hair was stuck to it.','Gloss on, hair in the wind'),step('B','lip oil','7–10s','Still shiny at lunch, never sticky.','Lips by the window at noon'),step('✓','verdict','10–12s','Oil wins for me.','You, to camera')])+\
     cta('13–15s','The one I use is in my TikTok Shop.','Product to camera')+tail()
def s_hands():
    return head('how I put on lip oil','15 s',['Lip oil','15s','Hands only','How to use it'])+hook('0–2s','The only lip step I do now.','Hand pulls the wand out, slow, gloss catches the light')+\
     body('3–12s',[step(1,'step 1','3–6s','One swipe on the bottom lip.','Wand on the back of your hand, then the lip',shot_first=True),step(2,'step 2','7–9s',"Press, don't rub.",'Fingertip pressing the tint in',shot_first=True),step(3,'step 3','10–12s','Done.','Cap goes back on, product set down',shot_first=True)])+\
     cta('13–15s','Orange cart if you want it.','Product next to your phone, cart button on screen')+tail(note='Hands only: what to film comes first in each step; the voiceover is optional.')
SLIDES=[('I wore lip oil for 8 hours to see if it lasts','Selfie holding the lip oil'),('9 AM: one coat, no liner','Applying, close up'),('11 AM: coffee. still shiny','Mug and lips in one shot'),('1 PM: after lunch, a little faded, not sticky','Lips by the window'),('5 PM: still there. my gloss never made it past noon','Old gloss next to the oil'),("it's in my TikTok Shop, tap the orange cart",'Product on its own')]
SKIT=[('Friend','Why do your lips look like that?'),('You','Like what?'),('Friend','Shiny. At 4 PM. Mine have been gone since lunch.'),('You','One coat this morning.'),('Friend',"Okay, that's not fair.")]
QS=[('5–15s','Which one looks more natural?'),('15–25s','Press your lips together. Which one feels sticky?'),('25–33s','Would you wear this one to work?')]
def o1_text():
    return head('lip oil, 8 hours later','6 slides',['Lip oil','Text on screen','Sell it'])+hook('slide 1',SLIDES[0][0],'Behind it: '+SLIDES[0][1],'screen')+\
     body('slides 2–5',[step(i+2,'slide '+str(i+2),'',t,'Behind it: '+b,'screen') for i,(t,b) in enumerate(SLIDES[1:5])])+cta('slide 6',SLIDES[5][0],'Behind it: '+SLIDES[5][1],'screen')+tail(False,'Same layout: lines become on-screen text, each slide is a step, no teleprompter.')
def o1_skit():
    return head('the friend who notices','30 s',['Lip oil','Skit','Funny'])+hook('0–4s','Friend: Why do your lips look like that?','Bathroom mirror, both in frame')+\
     body('4–22s',[step(i+1,w.lower(),'',f'{w}: {s}','') for i,(w,s) in enumerate(SKIT[1:])],'Same spot; film each side and cut together')+cta('22–30s',"It's in my TikTok Shop if you want to steal it too.",'You, to camera')+\
     tail(note='Squeezed: who says what is just a prefix, and scene changes and actions have nowhere to go.')
def o1_street():
    return head('can strangers tell?','45 s',['Lip oil','Street interview','Compare it'])+hook('0–4s','Can strangers tell lip oil from gloss?','You on the street, holding both up')+\
     body('5–33s',[step(i+1,'question '+str(i+1),t,s,'') for i,(t,s) in enumerate(QS)])+cta('40–45s','Linked in my TikTok Shop.','You, to camera')+\
     tail(note='Squeezed: the questions sit where spoken lines go; setup, what to keep and the reveal have no place.')
def o2_slides():
    cards=''.join(f'<section class="lv-slide{" cover" if i==0 else ""}"><div class="sc-ph"><b>{"Cover" if i==0 else "Slide "+str(i+1)}</b><button class="sc-ed">{IC["pen"]}</button></div><p class="lv-sltx">{E(t)}</p>{dirn("Behind it: "+b)}</section>' for i,(t,b) in enumerate(SLIDES))
    return head('lip oil, 8 hours later','6 slides',['Lip oil','Text on screen','Slides'])+cards+\
     '</div><button class="b b2 full-w">'+IC['copy']+'Copy slide text</button><div class="sc-rw"><b>Not quite right?</b><button class="b b2">Rewrite the whole script</button><small>3 of 3 rewrites left</small></div></div>'
def o2_wall():
    w="things I stopped buying because lip oil does it better:\n\ngloss. sticky by noon, every time.\n\nlip balm. looks flat on camera.\n\nlip liner. one coat is enough tint for me.\n\nlip masks. I just put this on before bed.\n\nthe one I use is in my shop."
    return head('what lip oil replaced','12 s',['Lip oil','Text on screen','Wall of text'])+\
     f'<section class="lv-slide cover">{ph("On screen","keep it up 12 s")}<p class="lv-wall">{E(w).replace(chr(10),"<br>")}</p></section>'+\
     f'<section class="sc-ctac">{ph("Behind the text","whole video",False)}{dirn("One slow shot: applying the oil in a mirror, looped")}<p class="lv-note" style="margin:6px 0 0">Sound: a trending sound, low. No talking.</p></section>'+\
     '</div><button class="b b2 full-w">'+IC['copy']+'Copy the text</button><div class="sc-rw"><b>Not quite right?</b><button class="b b2">Rewrite the whole script</button><small>3 of 3 rewrites left</small></div></div>'
def who(w,s): return f'<div class="lv-line"><span class="who {"w-y" if w=="You" else "w-f"}">{E(w)}</span><p class="sc-q2">{q(s)}</p></div>'
def scene(n,t,place,lines,act=''):
    a=f'<p class="lv-act">{E(act)}</p>' if act else ''
    return f'<section class="sc-bodyc lv-scene">{ph("Scene "+str(n),t)}{dirn(place)}{"".join(who(w,s) for w,s in lines)}{a}</section>'
def o2_skit():
    return head('the friend who notices','30 s',['Lip oil','Skit','Funny'])+\
     '<section class="lv-cast"><b>Who&rsquo;s in it</b><span><i class="who w-y">You</i>calm, already wearing the oil</span><span><i class="who w-f">Friend</i>same outfit with a hoodie on, holding a sticky gloss</span></section>'+\
     scene(1,'0–4s · hook','Bathroom mirror, both in frame (film each side, cut together)',SKIT[0:2])+scene(2,'4–12s','Same spot, close on the friend',[SKIT[2]],'Friend pulls a hair off her sticky gloss')+\
     scene(3,'12–22s','Same spot, wide',SKIT[3:5],'You hand over the oil, friend tries it, checks the mirror')+cta('22–30s',"It's in my TikTok Shop if you want to steal it too.",'You, to camera')+tail()
def o2_street():
    qs=''.join(f'<div class="sc-step"><div class="sc-sp"><span class="sn">Q{i+1}</span><b>ask</b><span class="tm">{t}</span><button class="sc-ed">{IC["pen"]}</button></div><p class="sc-q2">{q(s)}</p></div>' for i,(t,s) in enumerate(QS))
    return head('can strangers tell?','45 s',['Lip oil','Street interview','Compare it'])+\
     f'<section class="sc-ctac">{ph("Before you go","setup",False)}<p class="lv-note" style="margin:0">Bring the gloss and the oil with labels covered, wipes, and a clip-on mic. Ask first, film only people who say yes.</p></section>'+\
     hook('0–4s','Can strangers tell lip oil from gloss?','You on the street, holding both up')+\
     f'<section class="sc-bodyc">{ph("Questions to ask","5–33s",False)}{qs}<p class="lv-note" style="padding:0 16px 14px">Keep: surprised faces, and anyone who picks the oil without being told.</p></section>'+\
     f'<section class="sc-ctac">{ph("The reveal","34–40s")}<p class="sc-q1">{q("It is the oil. This one.")}</p>{dirn("Uncover the label, product close up")}</section>'+\
     cta('40–45s','Linked in my TikTok Shop.','You, to camera')+tail(False)
OPT1=[('15s · Sell it',s15_sell()),('60s · Sell it',s60_sell(False)),('15s · Compare it',s15_compare()),('Text on screen',o1_text()),('Skit',o1_skit())]
OPT2=[('Main · 15s Sell it',s15_sell()),('Main · 60s Sell it',s60_sell(True)),('Main · Compare it',s15_compare()),('Main · Hands only',s_hands()),('Text · Slides',o2_slides()),('Text · Wall of text',o2_wall()),('Skit',o2_skit())]
BAR=f'<div class="bk lvbar"><div class="sc-act"><button class="sv">{IC["save"]}<span>Save script</span></button><button>{IC["share"]}<span>Share</span></button><button>{IC["copy"]}<span>Copy</span></button></div></div>'
def phone(key,variants):
    sw=''.join(f'<button class="sw{" on" if j==0 else ""}" data-v="{j}">{E(n)}</button>' for j,(n,_) in enumerate(variants))
    pads=''.join(f'<div class="v{" on" if j==0 else ""}" data-v="{j}"><div class="bk"><div class="dpage">{h}</div></div></div>' for j,(_,h) in enumerate(variants))
    return f'<div class="sws">{sw}</div><div class="phone lvp" id="{key}"><div class="scr">{pads}</div>{BAR}<div class="toast"></div></div>'
FMAP=[('Talking to camera','Main','spoken lines lead, short shot note under each'),
 ('Voiceover + b-roll','Main','spoken line, the clip to show under it'),
 ('Get ready with me','Main','one beat per routine step'),
 ('Green screen','Main','shot note = what is on the screen behind you'),
 ('Car talk','Main','one shot, so shot notes only on the hook'),
 ('Day in my life','Main','one beat per scene, by time of day'),
 ('Hands only','Main','what to film first, voiceover optional'),
 ('Text on screen','Text on screen','slides, or one wall of text; no spoken lines'),
 ('Skit','Skit','cast, scenes, who says what, actions'),
 ('Street interview','Skit','you and the people you ask are the cast; questions are the lines, the reveal is the last scene')]
GMAP=[('Sell it','problem / show it / proof'),('Review it','first take / good / not so good / verdict'),('How to use it','step 1, 2, 3'),('Before and after','before / the switch / after'),('Unboxing','in the box / first look / first try'),('Compare it','A / B / verdict')]
MAP=('<details class="map" open><summary>Which layout each format falls under</summary><table><tr><th>How you film it</th><th>Layout</th><th>What changes</th></tr>'
 +''.join(f'<tr class="{"m" if l=="Main" else "c"}"><td>{E(f)}</td><td><b>{E(l)}</b></td><td>{E(w)}</td></tr>' for f,l,w in FMAP)
 +'</table><p class="mapn">Inside Main, &ldquo;what should the video do&rdquo; names the body beats:</p><table class="g">'
 +''.join(f'<tr><td>{E(g)}</td><td>{E(b)}</td></tr>' for g,b in GMAP)
 +'</table><p class="mapn">Length sets how many beats: 15s = 2, 30 to 45s = 3 to 4, 60s+ = grouped into parts.</p></details>')
CSS=open(D+'page.css').read()
page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Script output options</title>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet"><style>{LIVE}
{CSS}</style></head><body>
<header class="hd"><h1>Script output: 2 options</h1>
<p class="sub">Both use the live script page as it is today (IDEA card, Hook / Body / CTA, pencils, Save / Share / Copy), plus what she picked and the &ldquo;script starts here&rdquo; line. Same lip oil product in every example. Tap the chips above each phone to switch format. Sample copy.</p></header>
<main class="grid">
<section class="col"><h2>Option 1 · One layout that flexes</h2><p class="how">Always Hook / Body / CTA. Length sets how many beats, &ldquo;what should the video do&rdquo; names them, and no-talking formats swap spoken lines for on-screen text. Simplest to build; skits get squeezed.</p>{phone("p1",OPT1)}</section>
<section class="col"><h2>Option 2 · 1 main + 2 custom</h2><p class="how">The main layout covers 7 of the 10 filming styles (talking to camera, voiceover + b-roll, GRWM, green screen, car talk, day in my life, hands only). Text on screen and skit get their own page (street interviews use the skit page). 60s+ is grouped into parts.</p>{MAP}{phone("p2",OPT2)}</section>
</main>
<script>{open(D+'app.js').read()}</script></body></html>'''
open(D+'index.html','w').write(page)
print('ok')
