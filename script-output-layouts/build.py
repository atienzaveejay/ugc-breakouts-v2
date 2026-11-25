# Script output layouts for Ivan (25 Nov, after his 9:55 PM notes): his 10 "How will you film it?" chips
# grouped into 1 main layout + 3 custom ones. Same lip oil product as script-output-options.
import html as H, json
E=H.escape
D=__file__.replace('build.py','')
CAM='<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 8h3l2-3h6l2 3h3v11H4z"/><circle cx="12" cy="13" r="3.5"/></svg>'
TXT='<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 6h14M12 6v13M9 19h6"/></svg>'
NAV='<div class="nav"><span>Home</span><span>Breakouts</span><b>Script</b><span>Library</span></div>'
TOP='<div class="top"><span class="back">← Home</span><span class="tr"><span class="pro">Pro</span></span></div>'
q=lambda s:'“'+E(s)+'”'
def say(s,cls='l-say'): return f'<p class="{cls} say" tabindex="0">{q(s)}</p>'
def shot(s,ic=CAM): return f'<p class="l-shot">{ic}{E(s)}</p>'

def ingredients(picks,idea_t,idea):
    chips=''.join(f'<span>{E(p)}</span>' for p in picks)
    return f'''{TOP}<div class="ing"><div class="ing-h">What you picked</div><div class="ing-c">{chips}</div>
<div class="ing-idea"><b>The idea</b><h2>{E(idea_t)}</h2><p>{E(idea)}</p></div></div>
<div class="start"><span>Your script starts here</span></div>'''

def sec(label,t,inner,cls=''):
    return f'<div class="l-sec {cls}"><div class="l-sh"><b>{E(label)}</b><span>{E(t)}</span></div>{inner}</div>'
def beat(i,name,t,line,film,film_first=False):
    body=(shot(film)+say(line)) if film_first else (say(line)+shot(film))
    return f'<div class="l-beat"><div class="l-bh"><span class="l-n">{i}</span><span class="l-bn">{E(name)}</span><span class="l-t">{E(t)}</span></div>{body}</div>'
def meta(words,secs,extra=''):
    return f'<div class="meta">@W words · about {secs}{(" · "+extra) if extra else ""}</div>'
PRAC='<button class="btn-o prac">▶ Practice full screen</button>'
DOCK='<div class="dock bar3"><button class="b-o save">Save script</button><button class="b-o share">Share</button><button class="b-t copy">Copy</button></div>'

# ---------- MAIN: say + show, body changes with length and goal ----------
def main_15_sell():
    return ingredients(["Lip oil","Sell it","Talking to camera","15s","Calm and real"],"One coat in daylight","Show one coat of lip oil by the window, and why it beats sticky gloss.")+\
     meta(0,"@S s spoken")+\
     sec("HOOK","0–2s",say("Watch what one coat of this lip oil does.","l-say big hk")+shot("Close up, the lip oil by your face"))+\
     sec("BODY · SELL IT","3–11s",beat(1,"The problem","3–7s","My lips get dry by lunch, and most glosses just sit on top.","Talking, bare lips")+beat(2,"Show it","8–11s","The shine looks natural in daylight, not wet.","Lips by the window"))+\
     sec("CTA","12–15s",say("It's on TikTok Shop. Tap the orange cart.")+shot("Product to camera"))+PRAC
def main_15_compare():
    return ingredients(["Lip oil","Compare it","Talking to camera","15s","Honest review"],"Gloss vs oil, one day","Wear gloss in the morning and lip oil after lunch, then say which one lasted.")+\
     meta(0,"@S s spoken")+\
     sec("HOOK","0–2s",say("Lip oil or gloss? I wore both for a day.","l-say big hk")+shot("Hold one in each hand"))+\
     sec("BODY · COMPARE IT","3–12s",
       '<div class="ab"><div><span class="ab-k">A · Gloss</span>'+say("Looked great at 9. By 11 my hair was stuck to it.","l-say sm")+shot("Gloss on, hair in the wind")+'</div>'
       '<div><span class="ab-k">B · Lip oil</span>'+say("Still shiny at lunch, never sticky.","l-say sm")+shot("Lips by the window at noon")+'</div></div>'
       '<div class="verdict"><b>Verdict</b>'+say("Oil wins for me.","l-say sm")+'</div>')+\
     sec("CTA","13–15s",say("The one I use is in my TikTok Shop.")+shot("Product to camera"))+PRAC
def main_60_sell():
    p1=beat(1,"Talking","3–9s","My lips get dry by lunch, and every gloss I own just sits on top and gets sticky.","Talking, bare lips")+\
       beat(2,"Show the old stuff","9–15s","I tried balms too, but they look flat on camera, and I end up putting gloss on top anyway.","Hold up an old gloss and a balm")
    p2=beat(3,"Apply","15–24s","One coat, straight from the wand. It goes on clear with a little tint, and it doesn't smell like candy.","Close up, applying")+\
       beat(4,"Finish","24–32s","Press your lips together, and that's it. No liner, no top coat.","Close up, pressing lips")+\
       beat(5,"Daylight","32–38s","Here it is by the window. It looks like my lips, just healthier.","Lips by the window")
    p3=beat(6,"Hours later","38–46s","I put this on at 9 this morning. It's now 1.","Phone clock on screen, then lips")+\
       beat(7,"Proof","46–52s","Still shiny, and I've had two coffees and a sandwich. No reapplying.","Mug in frame, lips close up")
    return ingredients(["Lip oil","Sell it","Talking to camera","60s","Calm and real"],"One coat, four hours","Put the lip oil on in the morning and show it still there after lunch.")+\
     meta(0,"@S s spoken, plus pauses for the shots","3 parts")+\
     '<div class="jump"><span>Jump to</span><a>The problem</a><a>Show it</a><a>Proof</a></div>'+\
     sec("HOOK","0–3s",say("Watch what one coat of this lip oil does.","l-say big hk")+shot("Close up, the lip oil by your face"))+\
     sec("PART 1 · THE PROBLEM","3–15s",p1,"part")+sec("PART 2 · SHOW IT","15–38s",p2,"part")+sec("PART 3 · PROOF","38–52s",p3,"part")+\
     sec("CTA","52–60s",say("If your gloss gets sticky too, this is the one. It's on TikTok Shop, tap the orange cart.")+shot("Product to camera"))+PRAC
def main_hands():
    return ingredients(["Lip oil","How to use it","Hands only","15s","Cozy"],"Lip oil, hands only","Show the lip oil going on, filmed from above, with a short voiceover.")+\
     meta(0,"@S s of voiceover, optional","what to film comes first")+\
     sec("HOOK","0–2s",shot("Hand pulls the wand out, slow, gloss catches the light")+say("The only lip step I do now.","l-say big hk"))+\
     sec("BODY · HOW TO USE IT","3–12s",beat(1,"Step 1","3–6s","One swipe on the bottom lip.","Wand on the back of your hand, then the lip",True)+beat(2,"Step 2","7–9s","Press, don't rub.","Fingertip pressing the tint in",True)+beat(3,"Step 3","10–12s","Done.","Cap goes back on, product set down",True))+\
     sec("CTA","13–15s",shot("Product next to your phone, cart button on screen")+say("Orange cart if you want it."))+PRAC
MAIN={"15s · Sell it":main_15_sell(),"15s · Compare it":main_15_compare(),"60s · Sell it":main_60_sell(),"Hands only":main_hands()}

# ---------- TEXT ON SCREEN: slides or one wall of text ----------
def slide(n,txt,behind,cover=False):
    return f'<div class="sl{" cover" if cover else ""}"><div class="sl-h"><span>{"Cover" if cover else "Slide "+str(n)}</span></div><p class="sl-t say" tabindex="0">{E(txt)}</p>{shot("Behind it: "+behind)}</div>'
def text_slides():
    s=[("I wore lip oil for 8 hours to see if it lasts","Selfie holding the lip oil"),("9 AM: one coat, no liner","Applying, close up"),("11 AM: coffee. still shiny","Mug and lips in one shot"),("1 PM: after lunch, a little faded, not sticky","Lips by the window"),("5 PM: still there. my gloss never made it past noon","Old gloss next to the oil"),("it's in my TikTok Shop, tap the orange cart","Product on its own")]
    return ingredients(["Lip oil","Sell it","Text on screen","6 slides","Honest review"],"8 hours of lip oil","A time-stamped photo set showing one coat lasting the day.")+\
     meta(0,"6 slides","no spoken lines")+''.join(slide(i,t,b,i==0) for i,(t,b) in enumerate(s))+\
     '<button class="btn-o copytext">Copy slide text</button>'
def text_wall():
    w="things I stopped buying because lip oil does it better:\n\ngloss. sticky by noon, every time.\n\nlip balm. looks flat on camera.\n\nlip liner. one coat is enough tint for me.\n\nlip masks. I just put this on before bed.\n\nthe one I use is in my shop."
    return ingredients(["Lip oil","Sell it","Text on screen","Wall of text","Bestie chat"],"What lip oil replaced","One long screen of text listing what she stopped buying.")+\
     meta(0,"12 s on screen to read it","one screen")+\
     '<div class="wall"><div class="wall-h"><span>On screen</span><span>keep it up 12 s</span></div><p class="wall-t say" tabindex="0">'+E(w).replace("\n","<br>")+'</p></div>'+\
     sec("BEHIND THE TEXT","whole video",shot("One slow shot: applying the oil in a mirror, looped")+'<p class="l-note">Sound: a trending sound, low. No talking.</p>')+\
     '<button class="btn-o copytext">Copy the text</button>'
TEXT={"Slides":text_slides(),"Wall of text":text_wall()}

# ---------- SKIT: who says what, scene by scene ----------
def line(who,s,cls=''): return f'<div class="sk-l {cls}"><span class="who {"w-y" if who=="You" else "w-f"}">{E(who)}</span>{say(s,"l-say sm")}</div>'
def scene(n,place,t,inner,act=None):
    a=f'<p class="act">{E(act)}</p>' if act else ''
    return f'<div class="l-sec"><div class="l-sh"><b>SCENE {n}</b><span>{E(t)}</span></div><p class="place">{CAM}{E(place)}</p>{inner}{a}</div>'
def skit():
    return ingredients(["Lip oil","Sell it","Skit","30s","Funny"],"The friend who notices","A friend asks why your lips still look good at 4 PM. You play both parts.")+\
     meta(0,"@S s of lines, 30 s with the action","2 roles, you play both")+\
     '<div class="cast"><b>Who\'s in it</b><span><i class="w-y">You</i> calm, already wearing the oil</span><span><i class="w-f">Friend</i> same outfit with a hoodie on, holding a sticky gloss</span></div>'+\
     scene(1,"Bathroom mirror, both in frame (film each side, cut together)","0–4s · hook",line("Friend","Why do your lips look like that?","hk")+line("You","Like what?"))+\
     scene(2,"Same spot, close on the friend","4–12s",line("Friend","Shiny. At 4 PM. Mine have been gone since lunch."),"Friend pulls a hair off her sticky gloss")+\
     scene(3,"Same spot, wide","12–22s",line("You","One coat this morning.")+line("Friend","Okay, that's not fair."),"You hand over the oil, friend tries it, checks the mirror")+\
     sec("CTA","22–30s",say("It's in my TikTok Shop if you want to steal it too.")+shot("You, to camera"))+PRAC

# ---------- STREET INTERVIEW: questions, not lines ----------
def street():
    qs=[("Q1","5–15s","Which one looks more natural?"),("Q2","15–25s","Press your lips together. Which one feels sticky?"),("Q3","25–33s","Would you wear this one to work?")]
    qh=''.join(f'<div class="qq"><span class="q-k">{k}</span><span class="l-t">{t}</span>{say(s,"l-say sm")}</div>' for k,t,s in qs)
    return ingredients(["Lip oil","Compare it","Street interview","45s","Honest review"],"Can strangers tell?","Ask people outside a cafe to try gloss on one side, oil on the other.")+\
     meta(0,"45 s, most of it is their answers","you ask, they talk")+\
     sec("BEFORE YOU GO","setup",'<p class="l-note">Bring the gloss and the oil with labels covered, wipes, and a clip-on mic. Ask first, film only people who say yes.</p>')+\
     sec("HOOK","0–4s",say("Can strangers tell lip oil from gloss?","l-say big hk")+shot("You on the street, holding both up"))+\
     sec("QUESTIONS TO ASK","5–33s",qh+'<p class="l-note">Keep: surprised faces, and anyone who picks the oil without being told.</p>')+\
     sec("THE REVEAL","34–40s",say("It's the oil. This one.")+shot("Uncover the label, product close up"))+\
     sec("CTA","40–45s",say("Linked in my TikTok Shop.")+shot("You, to camera"))

LAYOUTS=[
 ("main","Main: say and show",MAIN,"The default for 7 of the 10 filming styles. Hook, body, CTA, each line with what to film under it.",
  "The body is not fixed. Length sets how many beats there are: 15s gets 2, 60s gets about 7 grouped into parts with a jump bar. The goal (Sell it, Compare it, How to use it, and so on) sets what the beats are. Hands only flips it so what to film comes first."),
 ("text","Text on screen",TEXT,"For Text on screen. No spoken lines, so no teleprompter.",
  "Slides: a cover line plus one block per slide, with what's behind each. Wall of text: one long block, how long to keep it up, and the one shot behind it."),
 ("skit","Skit",{"30s":skit()},"For Skit. Lines are split by who says them, scene by scene.",
  "A short cast list at the top, where each scene is filmed, and the action between lines. The creator usually plays both parts, so the roles have a costume cue."),
 ("street","Street interview",{"45s":street()},"For Street interview. The creator can't script other people, so the body is questions.",
  "Setup notes, the hook she says, 3 questions with times, what to keep in the edit, then the reveal and CTA."),
]
ROWS=[("Talking to camera","What to say, small shot notes, teleprompter","Main"),
 ("Voiceover + b-roll","What to say, with the clip under each line","Main"),
 ("Get ready with me","What to say at each step of the routine","Main"),
 ("Green screen","What to say, plus what's on the screen behind her","Main"),
 ("Car talk","What to say; one shot, so shot notes only at the start","Main"),
 ("Day in my life","Short voiceover per scene, scenes by time of day","Main"),
 ("Hands only","What the hands do first, optional voiceover","Main, film first"),
 ("Text on screen","Slides or one wall of text, what's behind it, no spoken lines","Text on screen"),
 ("Skit","Who says what, scene by scene, actions between lines","Skit"),
 ("Street interview","Questions to ask, what to keep, the reveal","Street interview")]
GOALS=[("Sell it","the problem, show it, proof"),("Review it","first impression, what's good, what's not, verdict"),("How to use it","step 1, step 2, step 3"),("Before and after","before, the switch, after"),("Unboxing","what's in the box, first look, first try"),("Compare it","A, B, verdict")]
LEN=[("15s","2 body beats"),("30–45s","3 to 4 beats"),("60s","about 7 beats in 3 parts, jump bar"),("90s+","parts with headers, jump bar, chapters for the teleprompter")]

import re
def fill(h):
    says=re.findall(r'class="(?:l-say[^"]*|sl-t|wall-t) say"[^>]*>(.*?)</p>',h,re.S)
    w=len(' '.join(H.unescape(re.sub('<[^>]+>',' ',x)) for x in says).replace('“',' ').replace('”',' ').split())
    return h.replace('about 6 slides','6 slides').replace('@W',str(w)).replace('@S',str(round(w/2.5)))
rows=''.join(f'<tr><td>{E(a)}</td><td>{E(b)}</td><td><b>{E(c)}</b></td></tr>' for a,b,c in ROWS)
goals=''.join(f'<tr><td>{E(a)}</td><td>{E(b)}</td></tr>' for a,b in GOALS)
lens=''.join(f'<tr><td>{E(a)}</td><td>{E(b)}</td></tr>' for a,b in LEN)
tabs=''.join(f'<button class="tab{" on" if i==0 else ""}" data-k="{k}">{i+1}. {E(t)}</button>' for i,(k,t,*_) in enumerate(LAYOUTS))
cards=''
for i,(k,t,variants,what,how) in enumerate(LAYOUTS):
    names=list(variants)
    sw=''.join(f'<button class="sw{" on" if j==0 else ""}" data-v="{j}">{E(n)}</button>' for j,n in enumerate(names)) if len(names)>1 else ''
    scr=''.join(f'<div class="pad v{" on" if j==0 else ""}" data-v="{j}">{fill(variants[n])}<div class="sp"></div></div>' for j,n in enumerate(names))
    cards+=f'''<section class="card{" on" if i==0 else ""}" id="l-{k}" data-k="{k}"><h3>{i+1}. {E(t)}</h3>{f'<div class="sws">{sw}</div>' if sw else '<div class="sws empty"></div>'}
<div class="phone"><div class="scr">{scr}</div>{DOCK}{NAV}<div class="tp"><div class="tph"><span>Practice</span><span><button class="tp-pp">Pause</button><button class="tp-x">Close</button></span></div><div class="tpb"></div></div><div class="toast"></div></div>
<div class="txt"><p>{E(what)}</p><p class="m">{E(how)}</p></div></section>'''
CSS=open(D+'../script-output-options/style.css').read()+open(D+'extra.css').read()
JS=open(D+'app.js').read()
html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Script output layouts</title>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet"><style>{CSS}</style></head><body>
<header class="hd"><h1>Script output: 1 main layout and 3 for special formats</h1>
<p class="sub">The 10 filming styles from the question screen don't need 10 layouts. 7 of them are someone saying lines over shots, so they share one main layout. Text on screen, Skit and Street interview each need a different page. In all 4, what she picked and the idea sit in their own section at the top, and a clear line shows where the script starts.</p>
<div class="maps"><div><h4>Which layout each filming style gets</h4><table><tr><th>How she films</th><th>What she needs on the page</th><th>Layout</th></tr>{rows}</table></div>
<div><h4>What changes the body in the main layout</h4><table><tr><th>Goal</th><th>Body beats</th></tr>{goals}</table>
<table class="t2"><tr><th>Length</th><th>Body</th></tr>{lens}</table><p class="fn">Word count follows the length, at about 2.5 spoken words a second.</p></div></div>
<p class="subm">Tap inside each phone. Sample copy.</p><nav class="tabs">{tabs}</nav></header><main class="grid">{cards}</main>
<script>{JS}</script></body></html>'''
open(D+'index.html','w').write(html)
print('ok')
