(function(){
"use strict";

/* ---------------- sample data: invented creator, "sample." handles, invented numbers ---------------- */
var IMG={oil:"../img/oil.jpg",face:"../img/face.jpg",brushes:"../img/brushes.jpg",palette:"../img/palette.jpg",flatlay:"../img/flatlay.jpg",mask:"../img/mask.jpg",neon:"../img/neon.jpg",closet:"../img/closet.jpg",tripod:"../img/tripod.jpg"};
/* read from the creator's public videos. Never typed, never written by the model. */
var STATS={videos:62,range:"30 Mar to 26 Sep 2026",fol:"18.4K",avg:"9.2K",er:"7.8%",rate:"2.4",nb:8};
var OWN=[
  {id:"b1",img:"oil",score:91,views:"112K",x:12,len:"0:18",date:"14 Aug",hook:"I stopped buying lip gloss after this."},
  {id:"b2",img:"face",score:78,views:"64K",x:7,len:"0:27",date:"2 Sep",hook:"Hour one vs hour six. No touch-ups."},
  {id:"b3",img:"flatlay",score:69,views:"41K",x:4,len:"0:34",date:"19 Jun",hook:"Everything in my purse, ranked by how often I use it."}
];
/* other creators' breakouts, for the Detail entry only. Links on the deck, never thumbnails. */
var LIPNOTES={img:"oil",score:86,handle:"sample.lipnotes",fol:"84K",hook:"I stopped buying lip gloss after this.",what:"Opens on a close-up swatch before a word is said."};

var ALL_SLIDES=[["cover","Cover"],["nums","My numbers"],["brk","My breakouts"],["work","What works for me"],["pitch","What I'd make for you"],["rate","Rates"]];
var ALTS={
  cover:[{title:"Beauty videos that beat my own average"},{title:"Beauty and GRWM, filmed at home in daylight"}],
  nums:[{title:"My TikTok in numbers"},{title:"Where my TikTok stands today"}],
  brk:[{title:"My three biggest breakouts"},{title:"The videos that beat my usual views"}],
  work:[{title:"My breakouts open on the product before I say a word"},{title:"Viewers stay when the proof is on screen"}],
  pitch:[{c:["I wore Glaze through a 12 hour shift. Here's hour 12.","Glaze vs the lip oil I used to reorder every month.","Getting ready in the car. Glaze is the only step."]},{c:["Six hours, two coffees, one coat of Glaze.","I asked my sister to guess which side is Glaze.","The only thing I reapply at my desk."]}],
  rate:[{next:"Send one Glaze Lip Oil and I'll deliver the first video within 7 days of it arriving."},{next:"Happy to start with one video. Ship a Glaze and the first cut is yours within 7 days."}]
};
function freshDeck(){
  return {
    pitch:true,brand:"Pellwyn",product:"Glaze Lip Oil",site:"pellwyn.example",cat:"Lip oil",refs:["sample.dewdiary","sample.glossroom"],
    me:{name:"Rae M.",handle:"@sample.raefilms",niche:["Beauty","GRWM"],link:"sample.link/rae",brands:"Sample Skin Co. and Sample Hair Lab",email:"rae@sample.email",
        age:"25 to 34",gender:"82% women",loc:"71% US",r1:"200",r3:"480",use:"60",raw:"80"},
    s:{
      cover:{title:ALTS.cover[0].title,sub:"I film beauty and GRWM at home in natural light, for women in their late 20s and 30s."},
      nums:{title:ALTS.nums[0].title},
      brk:{title:ALTS.brk[0].title},
      work:{title:ALTS.work[0].title,hook:"A close-up of the product in the first second. The hook comes in as on-screen text.",fmt:"Tests with the proof on screen, like a wear test with the time showing.",len:"6 of my 8 breakouts run 15 to 30 seconds."},
      pitch:{c:ALTS.pitch[0].c.slice(),f:[["Wear test","0:20 to 0:30","Built on my breakout 2"],["Side by side swatch","0:15 to 0:20","Built on a linked lip oil breakout"],["One product GRWM","0:15","Built on my breakout 1"]]},
      rate:{next:ALTS.rate[0].next}
    },
    alt:{cover:0,nums:0,brk:0,work:0,pitch:0,rate:0}
  };
}
function slides(d){return ALL_SLIDES.filter(function(x){return x[0]!=="pitch"||d.pitch;});}

/* ---------------- state ---------------- */
var S,DEVICE="phone";
function fresh(){return {view:"entry-library",stack:[],railKey:"entry-library",plan:"free",free:1,d:freshDeck(),slide:0,gen:0,read:0,toast:null,sheet:false};}
S=fresh();

function esc(t){return String(t).replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;"}[c];});}
function ic(n,cls){return '<svg'+(cls?' class="'+cls+'"':'')+' aria-hidden="true"><use href="#i-'+n+'"/></svg>';}
function bg(k){return 'background-image:url('+IMG[k]+')';}
function first(d){return d.me.name.split(" ")[0];}
function slug(d){return "ugcbreakouts.com/p/"+first(d).toLowerCase()+"-4k7q";}

/* ---------------- slides ---------------- */
function foot(d,i,n,last){
  var mw='<span class="smp">SAMPLE · invented creator and numbers</span>'+((last&&S.plan==="free")?'<span class="mw">Made with UGC Breakouts</span>':'');
  return '<div class="sfoot"><span>'+esc(d.me.name)+' · '+(d.pitch?'Pitch for '+esc(d.brand):'UGC pitch deck')+'</span>'+mw+'<span>'+(i+1)+' / '+n+'</span></div>';
}
function slideHtml(d,i){
  var list=slides(d),key=list[i][0],n=list.length,s=d.s[key],m=d.me,ft=foot(d,i,n,i===n-1);
  if(key==="cover"){
    var extra=(m.brands?'<p class="cx">Worked with '+esc(m.brands)+'</p>':'')+(m.link?'<p class="cx">'+esc(m.link)+'</p>':'');
    return '<div class="sl s-cover"><div class="cg"><div><p class="se">'+(d.pitch?'UGC pitch for '+esc(d.brand):'UGC creator on TikTok')+'</p><h2 class="sh">'+esc(s.title)+'</h2><p class="ssub">'+esc(s.sub)+'</p>'+
    '<div class="me"><span class="av">'+esc(m.name.charAt(0))+'</span><span><b>'+esc(m.name)+'</b>'+esc(m.handle)+' · '+esc(m.niche.join(" and "))+'</span></div>'+extra+'</div>'+
    '<div class="stackth">'+OWN.map(function(v){return '<div class="th" style="'+bg(v.img)+'"></div>';}).join("")+'</div></div>'+ft+'</div>';
  }
  if(key==="nums"){
    var aud=[m.age,m.gender,m.loc].filter(Boolean);
    return '<div class="sl s-nums"><p class="se">My numbers</p><h2 class="sh">'+esc(s.title)+'</h2><div class="sbody">'+
    '<div class="n4"><div><b>'+STATS.fol+'</b><small>Followers</small></div><div><b>'+STATS.avg+'</b><small>Average views</small></div><div><b>'+STATS.er+'</b><small>Engagement rate</small></div><div><b>'+STATS.rate+'</b><small>Videos a week</small></div></div>'+
    '<p class="src">From my '+STATS.videos+' public TikToks, '+STATS.range+'.</p>'+
    (aud.length?'<div class="aud"><span class="lab">Audience</span><span>'+aud.map(esc).join(' · ')+'</span><small>From my TikTok analytics</small></div>':'')+
    '</div>'+ft+'</div>';
  }
  if(key==="brk")return '<div class="sl s-proof"><p class="se">My breakouts</p><h2 class="sh">'+esc(s.title)+'</h2><div class="sbody"><div class="pc3">'+
    OWN.map(function(v){return '<div class="pcard"><div class="th" style="'+bg(v.img)+'"></div><div><div class="sc"><b>'+v.score+'</b><span>Breakout<br>Score</span></div><div class="xx">'+v.x+'x my usual views</div><div class="m">'+v.views+' views · '+v.len+' · '+v.date+'</div></div><p class="hq">“'+esc(v.hook)+'”</p></div>';}).join("")+
    '</div><p class="def">Breakout Score: a score from 0 to 100. It shows how much a video beat the average of what that account usually gets.</p></div>'+ft+'</div>';
  if(key==="work")return '<div class="sl s-pat"><p class="se">What works for me</p><h2 class="sh">'+esc(s.title)+'</h2><div class="sbody">'+
    '<div class="prow"><i>Hook</i><p>'+esc(s.hook)+'</p></div><div class="prow"><i>Format</i><p>'+esc(s.fmt)+'</p></div><div class="prow"><i>Length</i><p>'+esc(s.len)+'</p></div>'+
    '<p class="src">Across my '+STATS.nb+' breakouts in '+STATS.videos+' public TikToks.</p></div>'+ft+'</div>';
  if(key==="pitch")return '<div class="sl s-con"><p class="se">What I\'d make for '+esc(d.brand)+'</p><h2 class="sh">Three ideas for '+esc(d.product)+'</h2><div class="sbody">'+
    s.c.map(function(h,k){var f=s.f[k];return '<div class="crow"><i>'+(k+1)+'</i><div><q>'+esc(h)+'</q></div><div class="fmt"><b>'+f[0]+'</b>'+f[1]+'<br>'+f[2]+'</div></div>';}).join("")+
    (d.refs.length?'<p class="refs">'+esc(d.cat||d.product)+' breakouts I studied: '+d.refs.map(function(h){return '<u>tiktok.com/@'+esc(h)+'</u>';}).join(' · ')+'</p>':'')+
    '</div>'+ft+'</div>';
  return '<div class="sl s-rate"><p class="se">Rates</p><h2 class="sh">Rates and next step</h2><div class="sbody"><div class="rg"><div><table>'+
    '<tr><td>1 video<small>With 3 opening hooks</small></td><td>$'+esc(m.r1)+'</td></tr>'+
    '<tr><td>3 videos<small>With 3 opening hooks each</small></td><td>$'+esc(m.r3)+'</td></tr>'+
    '<tr><td>Paid usage<small>TikTok, US, 30 days, Spark Ads code</small></td><td>+$'+esc(m.use)+' / video</td></tr>'+
    '<tr><td>Raw footage<small>All clips, unedited</small></td><td>+$'+esc(m.raw)+' / video</td></tr></table>'+
    '<p class="turn">Organic posting rights on the brand account are included.</p></div>'+
    '<div class="nx"><p class="se">Next step</p><p>'+esc(d.s.rate.next)+'</p><div class="em"><small>Reply to</small>'+esc(m.email)+'</div></div></div></div>'+ft+'</div>';
}
function slw(i,cls){return '<div class="slw'+(cls?' '+cls:'')+'">'+slideHtml(S.d,i)+'</div>';}
function fitSlides(root){
  (root||document).querySelectorAll(".slw").forEach(function(w){var k=w.clientWidth/960;if(k>0&&w.firstChild)w.firstChild.style.setProperty("--k",k.toFixed(4));});
}

/* ---------------- shared bits ---------------- */
function backBtn(){return '<button class="ib" data-act="back" aria-label="Back">'+ic("back")+'</button>';}
function menuBtn(){return '<button class="ib" aria-label="Menu">'+ic("menu")+'</button>';}
function qpill(q){return '<span class="qp">'+ic("search")+'<span>'+esc(q)+'</span></span>';}
function stepHead(n,h,sub){
  return '<div class="stack" style="gap:10px"><div class="bar3">'+[1,2,3].map(function(k){return '<i class="'+(k<=n?'on':'')+'"></i>';}).join("")+'</div>'+
  '<div class="stack" style="gap:4px"><h1 class="h1" style="font-size:25px">'+h+'</h1>'+(sub?'<p class="sub" style="font-size:14.5px">'+sub+'</p>':'')+'</div></div>';
}
function inp(id,label,val,opt){opt=opt||{};
  return '<div class="inp"><label for="'+id+'">'+label+(opt.small?'<small>'+opt.small+'</small>':'')+'</label>'+
  (opt.area?'<textarea id="'+id+'" data-bind="'+(opt.bind||'')+'">'+esc(val)+'</textarea>':'<input id="'+id+'" type="'+(opt.type||'text')+'" value="'+esc(val)+'" data-bind="'+(opt.bind||'')+'"'+(opt.ph?' placeholder="'+esc(opt.ph)+'"':'')+'>')+'</div>';
}
function money(id,label,val,bind){return '<div class="inp"><label for="'+id+'">'+label+'</label><div><input id="'+id+'" type="text" inputmode="numeric" value="'+esc(val)+'" data-bind="'+bind+'"></div></div>';}
function stepTop(n){return '<div class="tb">'+backBtn()+'<span class="tt">Pitch deck</span><span class="sp"></span><span class="stepn">Step '+n+' of 3</span></div>';}
function ringSvg(frac){var c=295,off=Math.round(c*(1-Math.min(frac,1)));return '<svg viewBox="0 0 108 108"><circle cx="54" cy="54" r="47" fill="none" stroke="#E4DCD5" stroke-width="8"/><circle class="p" cx="54" cy="54" r="47" fill="none" stroke="#2DD4D8" stroke-width="8" stroke-linecap="round" stroke-dasharray="'+c+'" stroke-dashoffset="'+off+'"/></svg>';}
function procView(g,steps,h,sub,label){
  return '<div class="tb"><span class="ib ghost"></span><span class="sp"></span><span class="logo">UGC <b>Breakouts</b></span><span class="sp"></span><span class="ib ghost"></span></div>'+
  '<div class="proc"><div class="ring">'+ringSvg(g/steps.length)+'<div class="t">'+Math.min(100,Math.round(g/steps.length*100))+'%<small>'+label+'</small></div></div>'+
  '<div class="stack center" style="gap:4px"><h1 class="h1" style="font-size:24px">'+h+'</h1><p class="sub" style="font-size:14.5px">'+sub+'</p></div>'+
  '<ul class="steps">'+steps.map(function(t,k){var c=k<g?"done":(k===g?"now":"todo");return '<li class="'+c+'"><i>'+(c==="done"?ic("check"):"")+'</i>'+t+'</li>';}).join("")+'</ul></div>';
}

/* ---------------- phone views ---------------- */
var V={};
V["entry-library"]=function(){
  var rows=[["Lip oil","Today · 41 breakouts"],["GRWM car","Yesterday · 33 breakouts"],["Night routine","Sep 24 · 28 breakouts"]];
  return '<div class="tb">'+backBtn()+'<span class="tt">Library</span><span class="sp"></span>'+menuBtn()+'</div>'+
  '<div class="pb" style="gap:12px">'+
  '<div class="pdcard"><span class="pi">'+ic("deck")+'</span><div class="tx"><b>Your pitch deck</b><small>Show brands your own TikTok numbers and the videos that beat your average.</small></div>'+
  '<button class="b b1 full-w" data-act="start" data-from="library">'+ic("deck")+'Make my pitch deck</button></div>'+
  '<div class="faded stack" style="gap:12px"><div class="tabs" role="tablist" aria-label="Library"><button role="tab" aria-selected="true">Searches<small>3</small></button><button role="tab" aria-selected="false">Videos<small>2</small></button><button role="tab" aria-selected="false">Analyzed<small>2</small></button></div>'+
  '<p class="lsec">Recent</p>'+rows.map(function(r){return '<div class="srow"><span class="t"><b>'+r[0]+'</b>'+r[1]+'</span>'+ic("chev")+'</div>';}).join("")+'</div>'+
  '</div>';
};
V["entry-first"]=function(){
  return '<div class="tb"><span class="logo">UGC <b>Breakouts</b></span><span class="sp"></span><button class="cp">3 left</button>'+menuBtn()+'</div>'+
  '<div class="pb faded"><div class="stack" style="gap:2px"><h1 class="h1" style="font-size:26px">What are you filming next?</h1><p class="sub" style="font-size:15px">Search a product or format to remake</p></div>'+
  '<div class="srow"><span class="t" style="flex-direction:row;gap:8px;align-items:center">'+ic("search")+'Search</span></div>'+
  '<div class="chips"><span class="chip">Lip oil</span><span class="chip">GRWM</span><span class="chip">Protein bar</span></div></div>';
};
function firstSheet(){
  return '<div class="scrim" aria-hidden="true"></div><div class="sheet fr" role="dialog" aria-label="Make your pitch deck"><span class="grab"></span>'+
  '<div class="frimg">'+OWN.map(function(v){return '<span style="'+bg(v.img)+'"></span>';}).join("")+'</div>'+
  '<h2>Pitching brands?</h2><p>Turn your own TikTok into a pitch deck. We read your public videos and show brands the ones that beat your average.</p>'+
  '<button class="b b1 full-w" data-act="start" data-from="first">'+ic("deck")+'Make my pitch deck</button><button class="b b3" data-act="nothanks">Not now</button></div>';
}
V["entry-detail"]=function(){
  var v=LIPNOTES;
  return '<div class="tb">'+backBtn()+qpill("Lip oil")+'<button class="cp">2 left</button>'+menuBtn()+'</div>'+
  '<div class="pb" style="gap:14px">'+
  '<div class="minihead faded"><span class="th" style="'+bg(v.img)+'"></span><div class="stack" style="gap:4px"><div class="bigs"><b style="font-size:32px">'+v.score+'</b><span>Breakout Score</span></div><div class="hd">@'+v.handle+' <small>· '+v.fol+' followers</small></div></div></div>'+
  '<div class="box teal faded"><h3>Hooks</h3><p class="q">“'+esc(v.hook)+'”</p></div>'+
  '<div class="box white faded"><h3>Why the video worked</h3><ol class="ol"><li>'+esc(v.what)+'</li></ol></div>'+
  '<div class="box next faded"><h3>What you can do next</h3><ol class="ol"><li>Film the swatch first, then say the hook.</li><li>Keep it under 20 seconds.</li></ol></div>'+
  '</div>'+
  '<div class="dock"><div class="row faded"><button class="b b2 grow">'+ic("save")+'Save</button><button class="b b2 grow">'+ic("share")+'Share</button></div>'+
  '<button class="b b1 full-w" data-act="start" data-from="detail">'+ic("deck")+'Pitch this to a brand</button></div>';
};
V.handle=function(){
  return stepTop(1)+'<div class="pb">'+stepHead(1,"Your TikTok","We read your public videos to find your numbers and the ones that beat your average.")+
  inp("f-handle","TikTok handle",S.d.me.handle,{bind:"me.handle",ph:"@yourhandle"})+
  '<p class="shotnote">We never post, and you don\'t log in to TikTok. Private accounts can\'t be read.</p>'+
  '</div><div class="dock"><button class="b b1 full-w" data-act="read">Read my account</button></div>';
};
V.reading=function(){
  return procView(S.read,["Finding your public videos","Working out your usual views","Scoring every video against it","Picking your top breakouts"],"Reading "+esc(S.d.me.handle),"Usually under a minute.","READING");
};
V.few=function(){
  return '<div class="tb">'+backBtn()+'<span class="tt">Pitch deck</span><span class="sp"></span></div>'+
  '<div class="pb" style="gap:16px"><div class="stack center" style="gap:8px;padding-top:28px"><span class="bigic">'+ic("deck")+'</span><h1 class="h1" style="font-size:24px;text-align:center">Not enough videos yet</h1>'+
  '<p class="sub" style="text-align:center;font-size:14.5px">We found 9 public videos on @sample.newfilms. Breakout Scores need at least 15 to know what you usually get.</p></div>'+
  '<p class="shotnote">You can still make a deck with your numbers and rates. Your breakouts get added once you pass 15 videos.</p>'+
  '</div><div class="dock"><button class="b b1 full-w" data-act="go" data-v="you">Make it without breakouts</button><button class="b b3" data-act="back">Back</button></div>';
};
V["private"]=function(){
  return '<div class="tb">'+backBtn()+'<span class="tt">Pitch deck</span><span class="sp"></span></div>'+
  '<div class="pb" style="gap:16px"><div class="stack center" style="gap:8px;padding-top:28px"><span class="bigic">'+ic("deck")+'</span><h1 class="h1" style="font-size:24px;text-align:center">This account is private</h1>'+
  '<p class="sub" style="text-align:center;font-size:14.5px">We can only read public videos on @sample.quietfilms. Switch the account to public in TikTok, then try again.</p></div>'+
  '<p class="fine">Nothing was used from your plan.</p>'+
  '</div><div class="dock"><button class="b b1 full-w" data-act="read">Try again</button><button class="b b3" data-act="back">Use a different handle</button></div>';
};
V.you=function(){
  var m=S.d.me,all=["Beauty","GRWM","Skincare","Day in my life","Food","Home","Fitness","Fashion"];
  return stepTop(2)+'<div class="pb">'+stepHead(2,"About you","Saved for your next deck.")+
  '<div class="found"><p><b>'+esc(m.handle)+'</b> · '+STATS.videos+' public videos read</p><div class="q3"><span><b>'+STATS.fol+'</b>followers</span><span><b>'+STATS.avg+'</b>average views</span><span><b>'+STATS.nb+'</b>breakouts</span></div></div>'+
  inp("f-name","Name",m.name,{bind:"me.name"})+
  '<div class="stack" style="gap:8px"><p class="lbl" style="color:var(--ink);font-weight:700;font-size:14px">What you film <small style="font-weight:600;color:var(--mid);font-size:12.5px;margin-left:4px">From your bio</small></p><div class="chips">'+all.map(function(c){var on=m.niche.indexOf(c)>-1;return '<button class="chip'+(on?' on':'')+'" data-act="niche" data-k="'+c+'" aria-pressed="'+on+'">'+c+'</button>';}).join("")+'</div></div>'+
  '<div class="stack" style="gap:8px"><p class="lbl" style="color:var(--ink);font-weight:700;font-size:14px">Your rates</p><div class="money">'+
  money("f-r1","1 video",m.r1,"me.r1")+money("f-r3","3 videos",m.r3,"me.r3")+money("f-use","Paid usage, 30 days",m.use,"me.use")+money("f-raw","Raw footage",m.raw,"me.raw")+'</div></div>'+
  inp("f-email","Email for replies",m.email,{bind:"me.email",type:"email"})+
  '<div class="optsec"><p class="oh">Optional</p>'+
  inp("f-link","Portfolio link",m.link,{bind:"me.link"})+
  inp("f-brands","Brands you've worked with",m.brands,{bind:"me.brands"})+
  '<div class="stack" style="gap:8px"><p class="lbl" style="color:var(--ink);font-weight:700;font-size:14px">Your audience</p><p class="edhint" style="margin:0">From your TikTok analytics. Public data doesn\'t include this. The slide shows it as yours.</p>'+
  '<div class="three">'+inp("f-age","Top age",m.age,{bind:"me.age"})+inp("f-gen","Gender",m.gender,{bind:"me.gender"})+inp("f-loc","Top country",m.loc,{bind:"me.loc"})+'</div></div></div>'+
  '</div><div class="dock"><button class="b b1 full-w" data-act="go" data-v="brand">Next</button></div>';
};
V.brand=function(){
  var d=S.d,on=d.pitch;
  return stepTop(3)+'<div class="pb">'+stepHead(3,"Pitching one brand?","Add a slide with video ideas for them. Skip it for a deck you can send anyone.")+
  '<div class="tog togbox"><span><b>Add a slide for one brand</b><small>'+(on?'Your deck will have 6 slides':'Your deck will have 5 slides')+'</small></span><button class="sw" role="switch" aria-checked="'+on+'" aria-label="Add a slide for one brand" data-act="pitch"></button></div>'+
  (on?inp("f-brand","Brand",d.brand,{bind:"brand"})+inp("f-prod","Product",d.product,{bind:"product"})+inp("f-site","Brand website or TikTok",d.site,{bind:"site",small:"Optional"})+
   '<div class="stack" style="gap:6px"><p class="lbl">Ideas built from</p><div class="chips"><span class="chip on">'+ic("check")+'Your breakouts</span>'+(d.cat?'<span class="chip on">'+ic("search")+esc(d.cat)+' search, links only</span>':'<span class="chip ghost" style="color:var(--mid)">'+ic("search")+'Add a search</span>')+'</div></div>':'')+
  '</div><div class="dock"><button class="b b1 full-w" data-act="build">'+ic("spark")+'Build my pitch deck</button><p class="fine">'+(S.plan==="pro"?'Pro · 20 pitch decks a month':'Uses your 1 free pitch deck')+'</p></div>';
};
V.gen=function(){
  var d=S.d,st=["Writing your cover","Laying out your numbers","Finding what your breakouts share"];
  if(d.pitch)st.push("Writing ideas for "+esc(d.brand));
  st.push("Laying out "+slides(d).length+" slides");
  return procView(S.gen,st,"Building your pitch deck","Usually about 20 seconds.","BUILDING");
};
var FIELDS={
  cover:[["s.cover.title","Title",1],["s.cover.sub","Intro line",1]],
  nums:[["s.nums.title","Headline",0]],
  brk:[["s.brk.title","Headline",0]],
  work:[["s.work.title","Headline",1],["s.work.hook","Hook",1],["s.work.fmt","Format",1],["s.work.len","Length",1]],
  pitch:[["s.pitch.c.0","Idea 1 hook",1],["s.pitch.c.1","Idea 2 hook",1],["s.pitch.c.2","Idea 3 hook",1]],
  rate:[["s.rate.next","Next step",1]]
};
var HINTS={
  nums:"Numbers come from your public videos and can't be edited. Audience comes from About you.",
  brk:"Scores, views and multiples come from your public videos and can't be edited.",
  work:"Written from your breakout analyses. Any number here comes from your data.",
  pitch:"Other creators' videos show as links only.",
  rate:"Rates come from About you."
};
function getP(o,p){return p.split(".").reduce(function(a,k){return a[k];},o);}
function setP(o,p,v){var ks=p.split("."),last=ks.pop(),t=ks.reduce(function(a,k){return a[k];},o);t[last]=v;}
function curKey(){var l=slides(S.d);if(S.slide>=l.length)S.slide=l.length-1;return l[S.slide][0];}
function fieldsHtml(){
  var k=curKey(),h=FIELDS[k].map(function(f,n){return inp("ed-"+n,f[1],getP(S.d,f[0]),{bind:f[0],area:f[2]});}).join("");
  if(HINTS[k])h+='<p class="edhint">'+HINTS[k]+'</p>';
  if(k==="pitch")h+='<button class="rw" data-act="pitch-off" style="color:var(--mid)">Remove this slide</button>';
  return h;
}
function chipsHtml(){
  var l=slides(S.d);
  return '<div class="slchips" role="group" aria-label="Slides">'+l.map(function(x,k){return '<button data-act="slide" data-k="'+k+'" aria-pressed="'+(S.slide===k)+'"><span>'+(k+1)+'</span>'+x[1]+'</button>';}).join("")+
  (S.d.pitch?'':'<button data-act="pitch-on" class="addsl">+ Brand slide</button>')+'</div>';
}
V.edit=function(){
  return '<div class="tb">'+backBtn()+'<span class="tt">'+(S.d.pitch?esc(S.d.brand)+' pitch':'My pitch deck')+'</span><span class="sp"></span><span class="stepn">Saved</span>'+menuBtn()+'</div>'+
  '<div class="pb" style="gap:14px">'+chipsHtml()+
  '<div id="pv">'+slw(S.slide)+'</div>'+
  '<div class="stack" style="gap:12px" id="flds">'+fieldsHtml()+'</div>'+
  '<button class="rw" data-act="rewrite">'+ic("refresh")+'Rewrite this slide</button>'+
  '</div><div class="dock"><button class="b b1 full-w" data-act="go" data-v="share">'+ic("send")+'Send and export</button></div>';
};
function msgText(){
  var d=S.d,f=first(d),top=OWN[0];
  var niche=d.me.niche.map(function(x){return x==="GRWM"?x:x.toLowerCase();}).join(" and ");
  return "Subject: "+(d.pitch?d.product+" videos from a "+niche+" creator":"UGC creator, "+niche)+"\n\nHi "+(d.pitch?d.brand:"[Brand]")+" team,\n\nI'm "+f+", a UGC creator who films "+niche+" on TikTok. My videos average "+STATS.avg+" views, and my best this year reached "+top.views+", "+top.x+"x my usual.\n\n"+
  (d.pitch?"I put my numbers and three "+d.product+" ideas in a short deck: ":"My numbers and top breakouts are in a short deck: ")+slug(d)+"\n\nIf it fits, I can deliver the first video within 7 days of the product arriving.\n\n"+f;
}
V.share=function(){
  var d=S.d,n=slides(d).length;
  return '<div class="tb">'+backBtn()+'<span class="tt">Send your pitch</span><span class="sp"></span>'+menuBtn()+'</div>'+
  '<div class="pb" style="gap:16px">'+slw(0)+
  '<div class="fld"><label for="link-code" style="font-size:14px">Pitch link</label><div class="linkbox"><code id="link-code">'+slug(d)+'</code><button class="b b1" data-act="copy" style="padding:0 16px;white-space:nowrap">'+ic("copy")+'Copy</button></div><p class="nudge">Anyone with the link sees the '+n+' slides and a Reply button.</p></div>'+
  '<button class="b b2 full-w" data-act="pdf">'+ic("download")+'Download PDF</button>'+
  '<div class="fld msgbox"><label for="msg">Message to send with it <span class="rec">Draft</span></label><textarea id="msg">'+esc(msgText())+'</textarea><div class="lockrow"><p class="nudge">Send it from your own email or DM.</p><button class="editb" data-act="copy-msg">Copy message</button></div></div>'+
  '<p class="shotnote">We don\'t look up brand emails. Most brands list a partnerships or press email on their website or in their TikTok bio.</p>'+
  '<button class="b b3" data-act="go" data-v="brandview">See what '+(d.pitch?esc(d.brand):'a brand')+' sees</button>'+
  '</div>';
};
V.brandview=function(){
  var d=S.d,n=slides(d).length;
  return '<div class="tb"><span class="logo">UGC <b>Breakouts</b></span><span class="sp"></span></div>'+
  '<div class="pb" style="gap:14px">'+
  '<div class="bvbar"><span class="who"><b>'+esc(d.me.name)+'</b> sent '+(d.pitch?esc(d.brand):'you')+' a pitch deck</span><h1>'+esc(d.s.cover.title)+'</h1></div>'+
  Array.apply(null,{length:n}).map(function(_,i){return slw(i);}).join("")+
  '<p class="madewith">'+(S.plan==="free"?'Made with <b>UGC Breakouts</b>. Find Viral Breakouts on TikTok.':'')+'</p>'+
  '</div><div class="dock"><div class="row"><button class="b b2 bi" data-act="pdf" aria-label="Download PDF">'+ic("download")+'</button><button class="b b1 grow" data-act="reply">'+ic("mail")+'Reply to '+esc(first(d))+'</button></div></div>';
};
V.paid=function(){
  return '<div class="tb">'+backBtn()+'<span class="sp"></span><span class="logo">UGC <b>Breakouts</b></span><span class="sp"></span><span class="ib ghost"></span></div>'+
  '<div class="pb" style="gap:18px">'+
  '<div class="stack center" style="gap:6px"><h1 class="h1" style="text-align:center">Keep pitching brands</h1><p class="sub" style="color:var(--coral-d);font-weight:600;text-align:center">You used your free pitch deck.</p></div>'+
  '<div class="price"><span class="eb c">UGC Breakouts Pro</span><div class="amt">$49<small>/mo</small></div><button class="b b1 full-w" data-act="upgrade">Upgrade · $49/mo</button></div>'+
  '<ol class="ol"><li><span><b>20 pitch decks / mo</b><br><small>Built from your own TikTok numbers, ready in about 20 seconds.</small></span></li><li><span><b>No UGC Breakouts line on your slides</b><br><small>Your pitch, your name only.</small></span></li><li><span><b>100 searches / mo</b><br><small>Dozens of Viral Breakouts in every search.</small></span></li><li><span><b>100 video analyses / mo</b><br><small>See exactly why each video broke out.</small></span></li></ol>'+
  '<button class="b b3" data-act="back">Not now</button></div>';
};

/* ---------------- desktop editor ---------------- */
function deskEdit(){
  var l=slides(S.d);
  return '<div class="dtb"><span class="logo" style="font-size:20px">UGC <b>Breakouts</b></span><span class="dt">'+(S.d.pitch?esc(S.d.brand)+' pitch':'My pitch deck')+'</span><span class="saved">Saved</span><span class="sp"></span>'+
  '<button class="b b2" data-act="pdf">'+ic("download")+'Download PDF</button><button class="b b1" data-act="copy">'+ic("copy")+'Copy link</button></div>'+
  '<div class="ded"><div class="thumbs" role="group" aria-label="Slides">'+l.map(function(x,k){return '<button data-act="slide" data-k="'+k+'" aria-pressed="'+(S.slide===k)+'">'+slw(k,"flat")+(k+1)+' · '+x[1]+'</button>';}).join("")+
  (S.d.pitch?'':'<button data-act="pitch-on" class="addth">+ Brand slide</button>')+'</div>'+
  '<div class="canvas"><div id="pv">'+slw(S.slide)+'</div><p class="cnote">Click a slide on the left to edit it. Changes save as you type.</p></div>'+
  '<div class="panel"><h3>Slide '+(S.slide+1)+' · '+l[S.slide][1]+'</h3><div class="stack" style="gap:12px" id="flds">'+fieldsHtml()+'</div><button class="rw" data-act="rewrite">'+ic("refresh")+'Rewrite this slide</button></div></div>';
}

/* ---------------- wide views: sample deck, spec ---------------- */
function sampleWide(){
  var l=slides(S.d);
  return '<div class="whead"><span class="samplechip">SAMPLE · invented creator, brand and numbers. Every handle starts with “sample.”</span><h2>Sample deck: Rae M. pitching Pellwyn</h2><p>What the generator would make from the default inputs in this prototype. Rae M., Pellwyn and every number on these slides are invented, and no real TikTok account appears. Edits you make in the phone editor show up here, and turning off the brand slide in step 3 drops it to 5 slides.</p></div>'+
  '<div class="slist">'+l.map(function(x,k){return '<figure>'+slw(k)+'<figcaption>'+(k+1)+' / '+l.length+' · '+x[1]+'</figcaption></figure>';}).join("")+'</div>';
}
var TERMS='<a href="https://www.tiktok.com/legal/page/us/terms-of-service/en" target="_blank" rel="noopener">TikTok US Terms</a>';
var SPEC='<div class="whead"><h2>Spec for Lester</h2><p>Build notes for the pitch deck generator, reworked on 29 Sept so the deck is about the creator\'s own account. Every number here is a proposal until Ivan confirms it.</p></div><div class="spec">'+
'<h3>What it does</h3><p>A creator types their own TikTok handle. We read their public videos, score each one against the account\'s own average, and build a 5 or 6 slide deck: cover, my numbers, my top 3 breakouts, what works for me, an optional slide of ideas for one brand, then rates. They edit it and share a link or a PDF. The brand opens the link and can reply by email.</p>'+
'<h3>Data</h3><div class="tblwrap"><table><tr><th>What</th><th>Source</th><th>Notes</th></tr>'+
'<tr><td>Handle</td><td>Typed by the creator</td><td>Lowercase, strip the @. No TikTok login (its user info API has no email field, which is why sign in is Google and email).</td></tr>'+
'<tr><td>Public videos</td><td>Apify, the same scrape searches use today</td><td>Proposal: the last 180 days, up to 100 videos. Per video: id, posted_at, views, likes, comments, shares, duration, caption, cover image.</td></tr>'+
'<tr><td>Profile</td><td>Same scrape</td><td>Display name, bio, followers, avatar. Niche tags are suggested from the bio and captions, and the creator confirms them.</td></tr>'+
'<tr><td>Account average</td><td>Computed</td><td>The same baseline the Breakout Score already uses in BrandBeacon and UB: what this account usually gets. Reuse that code, don\'t write a second version.</td></tr>'+
'<tr><td>Breakout Score per video</td><td>Computed</td><td>0 to 100, scored against the account\'s own average. The slide line “12x my usual views” is views divided by the account average, rounded down, shown only at 2x or more.</td></tr>'+
'<tr><td>The creator\'s breakouts</td><td>Computed</td><td>Proposal: videos scoring 60 or more. The top 3 by score go on slide 3. Run the existing analysis (hooks, why it worked) on up to 8 of them for slide 4.</td></tr>'+
'<tr><td>My numbers slide</td><td>Computed</td><td>Followers from the profile. Average views from the same baseline. Engagement rate is likes plus comments plus shares, divided by views, across the window. Videos a week is the video count over the weeks in the window. The date range is the first to the last video read.</td></tr>'+
'<tr><td>Creator entered</td><td>Account fields</td><td>Name, niche, 4 rates, reply email. Optional: portfolio link, past brands, audience age, gender and top country. Public data has no demographics. Audience is labeled “From my TikTok analytics” on the slide.</td></tr>'+
'<tr><td>Brand slide (optional)</td><td>Typed by the creator</td><td>Brand, product, site. Ideas build on the creator\'s own breakouts first. If they started from a search, up to 2 of its breakouts can be cited, as links only.</td></tr>'+
'<tr><td>Deck</td><td>New table <code>pitch_decks</code></td><td>id, user_id, handle, stats snapshot JSON with read_at, slides JSON, brand fields (nullable), slug, created_at, updated_at, plan at creation.</td></tr></table></div>'+
'<h3>Small and private accounts</h3><ul>'+
'<li><b>Private, or handle not found:</b> stop before scoring. Show the Private screen. Nothing counts against the plan.</li>'+
'<li><b>Under 15 public videos in the window</b> (the number is a guess, Ivan and Lester to set it): no Breakout Scores, since the average isn\'t stable. Offer a deck without slides 3 and 4: cover, numbers, the optional brand slide, rates.</li>'+
'<li><b>15 or more videos but fewer than 3 breakouts:</b> show the 1 or 2 there are. With none, drop slides 3 and 4 and tell the creator in the editor.</li>'+
'<li><b>Paid or Spark videos</b> stay in, unlabeled, the same as search results for MVP.</li></ul>'+
'<h3>Generation</h3><p>Two steps. The read and scoring run first (a scrape, so likely 15 seconds to 1 minute, like a search). Then one Claude API call with <code>claude-sonnet-5</code>, structured output, no tools, target under 20 seconds.</p>'+
'<pre>System: You write short UGC pitch decks for US TikTok creators,\nin the creator\'s own first person voice.\nRules: American spelling. TikTok only. Say breakout and Breakout Score.\nNo em dashes or en dashes. Plain slide titles.\nNever write a number. When a line needs one, use a placeholder\nfrom the input, like {breakout_count} or {len_share}. We fill them in.\nNever state a fact about the brand that is not in the input.\n\nInput (JSON): creator profile (name, niche, bio), stats placeholders,\ntop 3 breakouts with their analyses, every breakout analysis\n(hook, why it worked, duration bucket, format tags),\noptional brand block (brand, product, cited links).\n\nReturn JSON:\n  cover.title (max 10 words), cover.sub (max 28 words)\n  numbers.title, breakouts.title (max 10 words each)\n  works.title, works.hook, works.format, works.length (max 22 words each)\n  pitch.concepts[2 or 3]: hook (max 12 words), format, length,\n    based_on (own breakout index, or a cited link)   // only if brand block\n  next_step (max 22 words)</pre>'+
'<p>Every number on the slides comes from our data or the creator\'s fields, never from the model. Validate the output: any digit outside a placeholder is a reject and a retry. “Rewrite this slide” sends that slide\'s JSON back under the same rules and returns one replacement.</p>'+
'<h3>Export</h3><ul><li><b>Link:</b> <code>ugcbreakouts.com/p/{slug}</code>, public, noindex, rendered from the slides JSON. Reply opens a mailto to the creator\'s reply email.</li><li><b>PDF:</b> the same page at 1920 by 1080 per slide with headless Chromium (Playwright <code>page.pdf</code>), stored, with a download URL. Regenerate on edit.</li><li>Thumbnails on slides 1 and 3 are the creator\'s own videos. Each links to the video on TikTok.</li></ul>'+
'<h3>Limits per plan</h3><table><tr><th></th><th>Free</th><th>Pro $49/mo</th></tr><tr><td>Pitch decks</td><td>1</td><td>20 a month</td></tr><tr><td>Rewrites</td><td>5 per deck</td><td>Unlimited, with a soft cap of 30 per deck for cost</td></tr><tr><td>“Made with UGC Breakouts” line</td><td>On the last slide and the link page</td><td>Off</td></tr><tr><td>PDF and link</td><td>Yes</td><td>Yes</td></tr></table><p>A deck counts when generation finishes, the same way a search counts when results arrive. A failed read (private, not found) never counts.</p>'+
'<h3>Risks</h3><ul>'+
'<li><b>Other creators\' content.</b> Mostly gone: the deck now shows only the creator\'s own videos. The one place another creator can appear is the optional brand slide, as a plain link with no thumbnail, handle stats or hook. '+TERMS+' bar using another user\'s content commercially without permission.</li>'+
'<li><b>Someone else\'s handle.</b> Any public handle can be typed. Check it belongs to the signed in creator, or allow it for MVP since the data is public?</li>'+
'<li><b>Audience numbers.</b> Typed by the creator and labeled as theirs. We can\'t check them.</li>'+
'<li><b>Claims about brands.</b> The model says nothing about the brand beyond the creator\'s input.</li>'+
'<li><b>Stale numbers.</b> The stats are a snapshot with a date on slide 2. Refreshing re-reads the account.</li>'+
'<li><b>Public links.</b> Unguessable slugs (random suffix), noindex, and the creator can turn a link off.</li></ul></div>';

/* ---------------- notes ---------------- */
function li(t,txt){return '<li><span class="tag '+t+'">'+({r:"IVAN",a:"ASK",f:"LOCK",d:"DEV",q:"SOURCE",v:"VEEJAY"})[t]+'</span><span>'+txt+'</span></li>';}
function src(u,l){return ' <a href="'+u+'" target="_blank" rel="noopener" style="color:var(--acc)">'+l+'</a>';}
var TERMS_LINK=src("https://www.tiktok.com/legal/page/us/terms-of-service/en","TikTok US Terms");
var NOTES={
  "entry-library":{id:"P1 · main entry, Library",h:"Make my pitch deck",li:[["v","Veejay, 29 Sept: the pitch deck should be about the creator's own profile and stats, not other creators' breakouts. This version is built around that."],["v","Main way in: “Make my pitch deck” on Library. The rest of Library is the live screen, faded."],["a","A “Pitch deck” row in Account, under Library and Affiliate, would be a second spot. Add it?"],["r","Ivan's priority list: “UB - pitch deck generator.”"]]},
  "entry-first":{id:"P2 · first run prompt",h:"First run prompt",li:[["v","Second way in: a one time prompt on Home, behind a sheet."],["a","Show it on the first sign in, or after the first search so it doesn't get in the way of searching?"],["a","Not now closes it for good. The Library card stays."]]},
  "entry-detail":{id:"P3 · from Detail, fills slide 5",h:"From Detail",li:[["v","Kept only as a shortcut. It turns on the brand slide and brings in the Lip oil search. The deck stays about the creator."],["q","The tapped video goes into slide 5 as a plain link. No thumbnail, no stats."+TERMS_LINK],["a","Worth keeping? It adds a third button under Save and Share on Detail. If the creator hasn't read their account yet, step 1 comes first."]]},
  "handle":{id:"P4 · step 1 of 3",h:"Your TikTok",li:[["v","Input is the creator's own handle. We pull their public videos with the same Apify scrape searches use."],["r","No TikTok login. Ivan ruled it out for sign in: TikTok's user info API has no email field. So the handle is typed."],["a","Anyone can type any public handle. Check that it's theirs, or skip that for MVP?"]]},
  "reading":{id:"P5 · reading the account",h:"Reading your account",li:[["v","A short build state while we read and score. Same ring as Processing."],["a","“Under a minute” is a guess: a scrape plus scoring, about the range of a search. Lester to confirm."],["a","Does reading your own account use one of the 3 free searches?"]]},
  "few":{id:"P6 · too few videos",h:"Not enough videos yet",li:[["a","Under 15 public videos, the average isn't stable enough to score against. The deck can still go out without the breakouts slides."],["a","15 is a guess. Ivan and Lester to set the real minimum."]]},
  "private":{id:"P7 · private account",h:"Private account",li:[["d","A private or missing account returns no videos. Show this instead of an empty deck. Nothing is counted."]]},
  "you":{id:"P8 · step 2 of 3",h:"About you",li:[["v","The numbers at the top come from public data and can't be edited."],["d","Public data has no audience age, gender or location. Only the account owner sees that, in TikTok's own analytics. So these fields are optional, typed by the creator, and labeled “From my TikTok analytics” on the slide."],["a","Asked once and saved. The next deck skips this step."],["q","Rate fields follow the guides: a base rate, paid usage, raw footage. inBeat puts paid usage at about 30% of base a month and raw footage at 30 to 50%."+src("https://inbeat.agency/blog/ugc-rates","inBeat")],["q","Collabstr's 2026 report puts the average UGC price at $197. The sample uses $200."+src("https://www.netinfluencer.com/collabstr-report-tiktok-campaigns-plummet-as-brands-pivot-to-ugc/","Collabstr via Net Influencer")]]},
  "brand":{id:"P9 · step 3 of 3",h:"Pitching one brand?",li:[["v","Optional. Off gives a 5 slide deck about the creator. On adds “What I'd make for you” with 2 or 3 ideas for one brand."],["v","The old category research lives here now, cut down. Ideas build on the creator's own breakouts first."],["q","If an idea points to another creator's video, it shows as a link only."+TERMS_LINK],["a","We don't fetch anything about the brand. The deck can't state things about a brand we can't check."]]},
  "gen":{id:"P10 · building",h:"Building the deck",li:[["d","One Claude call writes the words. Every number comes from our data or the creator's fields, never the model."],["a","“About 20 seconds” is a guess. Lester to confirm after a test run."]]},
  "edit":{id:"P11 · edit",h:"Edit the deck",li:[["v","Six slides: cover, my numbers, my breakouts, what works for me, the optional brand slide, rates."],["a","Numbers are read only. Should a creator be able to hide one, like a low engagement rate?"],["a","Rewrite this slide swaps in a new version. Free gets 5 rewrites per deck, Pro is unlimited."],["a","The brand slide can be added or removed here too."]]},
  "share":{id:"P12 · send and export",h:"Send and export",li:[["a","Link first, PDF second. The draft message leads with the creator's own best number."+src("https://www.pitchlo.com/blog/how-to-pitch-brands-as-a-ugc-creator","Pitchlo")],["a","We never look up brand emails. The creator sends it from their own inbox or DMs."],["a","Later: “Opened” on the link and a follow up reminder after 5 to 7 business days. Not built."]]},
  "brandview":{id:"P13 · what the brand sees",h:"The brand's view",li:[["v","Brands now see only the creator's own videos and numbers. That removes the TikTok terms risk of showing other creators' content to brands, the biggest open item in the first version."+TERMS_LINK],["a","On Free, a “Made with UGC Breakouts” line sits under the slides. Pro removes it. OK?"],["f","TikTok only. Video links go to TikTok."]]},
  "paid":{id:"P14 · paid, pitch deck cap",h:"Paid: pitch deck cap",li:[["a","A fourth version of Paid, same layout as the existing three. The pitch lines go first."],["a","Free is 1 pitch deck, Pro is 20 a month. Right numbers?"]]},
  "desk":{id:"P15 · desktop editor",h:"Desktop: deck editor",li:[["a","Slides on the left, the slide in the middle, its fields on the right. Brands mostly open links on a laptop, so this is close to what they see."],["a","Only the editor has a desktop layout here. The steps would reuse the mobile layout at a centered width."]]},
  "sample":{id:"Sample",h:"Sample deck",li:[["f","Invented creator (Rae M.), brand (Pellwyn) and numbers. SAMPLE sits on every slide, and every handle starts with “sample.”"],["q","Media kit guides list the same core: stats, work samples, rates, contact."+src("https://billo.app/blog/ugc-portfolio/","Billo")+" What we add is which videos beat the creator's own average, and the pattern behind them."],["q","Beacons and similar link in bio tools already offer media kits on paid plans."+src("https://beacons.ai/i/plans","Beacons")]]},
  "spec":{id:"Spec",h:"Spec for Lester",li:[["d","Data, small accounts, prompt outline, export, limits and risks are above. Nothing here is built yet."],["a","Two numbers to set: the minimum video count (15?) and the Breakout Score that counts as a breakout (60?)."]]}
};
var QUESTIONS=[
  "Does UB already compute a creator's own baseline when they search their own handle? If so, the deck reuses it.",
  "How many public videos do we need before showing Breakout Scores? We assumed 15.",
  "What Breakout Score counts as one of the creator's breakouts? We assumed 60 or more.",
  "Does reading your own account use one of the 3 free searches?",
  "Analyzing the creator's top breakouts for slide 4: free, or does it use their analyses?",
  "Check that the handle belongs to the signed in creator, or allow any public handle for MVP?",
  "Where does “Make my pitch deck” live: the Library card, a row in Account, or both? And the one time prompt after first sign in?",
  "Keep “Pitch this to a brand” on Detail as a shortcut to the brand slide, or drop it?",
  "Free gets 1 pitch deck and Pro gets 20 a month. Right numbers?",
  "Keep the “Made with UGC Breakouts” line on Free pitches?",
  "Rewrites: 5 per deck on Free, unlimited on Pro?",
  "Later: tell the creator when the brand opens the link, and remind them to follow up?"
];
function notesHtml(key){
  var legend='<div class="legend"><span><span class="tag v">VEEJAY</span> Veejay asked for it</span><span><span class="tag r">IVAN</span> his list and answers</span><span><span class="tag a">ASK</span> our idea, needs Ivan</span><span><span class="tag q">SOURCE</span> research, linked</span><span><span class="tag d">DEV</span> for Lester</span><span><span class="tag f">LOCK</span> his rules</span></div>';
  if(key==="questions")return legend+'<p class="sid">Open</p><h2>Questions for Ivan</h2><ul>'+QUESTIONS.map(function(q){return li("a",q);}).join("")+'</ul>';
  var n=NOTES[key]||NOTES["entry-library"];
  return legend+'<p class="sid">'+n.id+'</p><h2>'+n.h+'</h2><ul>'+n.li.map(function(x){return li(x[0],x[1]);}).join("")+'</ul>';
}

/* ---------------- rail ---------------- */
var RAIL=[
  {g:"Start a deck",items:[["entry-library","P1","Make my pitch deck"],["entry-first","P2","First run prompt"],["entry-detail","P3","From Detail, fills slide 5"]]},
  {g:"Build",items:[["handle","P4","Your TikTok"],["reading","P5","Reading your account"],["few","P6","Not enough videos"],["private","P7","Private account"],["you","P8","About you"],["brand","P9","Pitching one brand?"],["gen","P10","Building"]]},
  {g:"Deck",items:[["edit","P11","Edit the deck"],["share","P12","Send and export"],["brandview","P13","What the brand sees"],["desk","P15","Desktop editor"]]},
  {g:"Money",items:[["paid","P14","Paid, pitch deck cap"]]},
  {g:"Review",items:[["sample","","Sample deck, all slides"],["spec","","Spec for Lester"],["questions","","Questions for Ivan"]]}
];
/* old deep links from the first version */
var ALIAS={"entry-results":"entry-library","pick":"handle"};
function buildRail(){
  var g=document.getElementById("rail-groups"),sel=document.getElementById("jump-sel");
  g.innerHTML=RAIL.map(function(grp){return '<div class="grp"><h2>'+grp.g+'</h2>'+grp.items.map(function(it){return '<button type="button" data-jump="'+it[0]+'"><span>'+it[1]+'</span>'+it[2]+'</button>';}).join("")+'</div>';}).join("");
  sel.innerHTML=RAIL.map(function(grp){return '<optgroup label="'+grp.g+'">'+grp.items.map(function(it){return '<option value="'+it[0]+'">'+(it[1]?it[1]+' · ':'')+it[2]+'</option>';}).join("")+'</optgroup>';}).join("");
  g.addEventListener("click",function(e){var b=e.target.closest("[data-jump]");if(b)jump(b.getAttribute("data-jump"));});
  sel.addEventListener("change",function(){jump(sel.value);});
}
function jump(key){
  var keepDeck=S.d;
  S=fresh();S.d=keepDeck;S.railKey=key;
  var L="entry-library",pre={handle:[L],few:[L,"handle"],"private":[L,"handle"],you:[L,"handle"],brand:[L,"handle","you"],share:["edit"],brandview:["edit","share"],paid:[L,"handle","you","brand"]};
  S.stack=(pre[key]||[]).map(function(v){return {view:v};});
  if(key==="desk"){setDevice("desk",true);S.view="edit";}
  else{if(DEVICE==="desk")setDevice("phone",true);S.view=key;}
  if(key==="entry-first")S.sheet=true;
  if(key==="paid")S.free=0;
  if(key==="gen")startGen();
  if(key==="reading")startRead();
  render(true);
}
function currentKey(){
  if(S.railKey==="sample"||S.railKey==="spec"||S.railKey==="questions")return S.railKey;
  if(DEVICE==="desk")return "desk";
  return S.view;
}
function go(v){S.stack.push({view:S.view});S.view=v;S.railKey=v;S.sheet=false;render(true);}
function back(){var p=S.stack.pop();S.view=p?p.view:"entry-library";S.railKey=S.view;S.sheet=false;render(true);}
var genTm=null,readTm=null;
function startGen(){
  clearInterval(genTm);S.gen=0;var total=slides(S.d).length===6?5:4;
  genTm=setInterval(function(){
    if(S.view!=="gen"){clearInterval(genTm);return;}
    S.gen++;
    if(S.gen>=total){clearInterval(genTm);setTimeout(function(){if(S.view==="gen"){S.view="edit";S.railKey="edit";S.stack=[];S.slide=0;render(true);}},500);}
    render(false);
  },800);
}
function startRead(){
  clearInterval(readTm);S.read=0;
  readTm=setInterval(function(){
    if(S.view!=="reading"){clearInterval(readTm);return;}
    S.read++;
    if(S.read>=4){clearInterval(readTm);setTimeout(function(){if(S.view==="reading"){S.view="you";S.railKey="you";render(true);}},500);}
    render(false);
  },900);
}

/* ---------------- render ---------------- */
var scr=document.getElementById("scr"),ovl=document.getElementById("ovl"),wide=document.getElementById("wide");
var lastNotes=null;
function render(nav){
  var key=currentKey(),isWide=(key==="sample"||key==="spec");
  document.body.classList.toggle("wideon",isWide);
  if(isWide){wide.innerHTML=key==="sample"?sampleWide():SPEC;}
  else{
    var top=scr.scrollTop;
    scr.innerHTML=DEVICE==="desk"?deskEdit():(V[S.view]||V["entry-library"])();
    scr.scrollTop=nav?0:top;
  }
  requestAnimationFrame(function(){fitSlides();});
  fitSlides();
  ovl.innerHTML=(S.sheet&&S.view==="entry-first"&&DEVICE==="phone"?firstSheet():'')+(S.toast?'<div class="toast" role="status">'+ic("checkc")+'<span>'+S.toast+'</span></div>':'');
  document.querySelectorAll("#rail-groups [data-jump]").forEach(function(b){var on=b.getAttribute("data-jump")===key;b.classList.toggle("on",on);if(on)b.setAttribute("aria-current","page");else b.removeAttribute("aria-current");});
  var sel=document.getElementById("jump-sel");if(sel.value!==key)sel.value=key;
  if(key!==lastNotes){document.getElementById("notes").innerHTML=notesHtml(key);lastNotes=key;}
  document.getElementById("where").textContent=NOTES[key]?NOTES[key].id:"Questions";
  var ctl="";
  if(S.view==="reading")ctl+='<button data-ctl="skipread">Skip ahead</button>';
  if(S.view==="gen")ctl+='<button data-ctl="skip">Jump to deck</button>';
  if(S.view==="edit"||S.view==="share"||S.view==="brandview"||DEVICE==="desk")ctl+='<button data-ctl="plan">'+(S.plan==="free"?"View as Pro":"View as Free")+'</button>';
  document.getElementById("ctl").innerHTML=ctl+'<button data-ctl="restart">Restart</button>';
}
function toast(m){S.toast=m;render(false);clearTimeout(toast.tm);toast.tm=setTimeout(function(){S.toast=null;render(false);},2800);}
function refreshPreview(){
  var p=document.getElementById("pv");if(p){p.innerHTML=slw(S.slide);fitSlides(p);}
  if(DEVICE==="desk"){var t=scr.querySelectorAll(".thumbs .slw");if(t[S.slide]){t[S.slide].innerHTML=slideHtml(S.d,S.slide);fitSlides(t[S.slide].parentNode);}}
}

/* ---------------- device ---------------- */
function fitDesk(){
  if(DEVICE!=="desk")return;
  var main=document.querySelector(".main"),w=main.clientWidth-parseFloat(getComputedStyle(main).paddingLeft)*2;
  var sc=Math.min(1,w/1280,Math.max(.45,(window.innerHeight-90)/800));
  document.body.style.setProperty("--sc",sc.toFixed(4));
}
window.addEventListener("resize",function(){fitDesk();fitSlides();});
function setDevice(d,quiet){
  DEVICE=d;
  document.body.classList.toggle("desk",d==="desk");
  document.getElementById("phone").classList.toggle("desk",d==="desk");
  document.getElementById("dev-phone").setAttribute("aria-pressed",String(d==="phone"));
  document.getElementById("dev-desk").setAttribute("aria-pressed",String(d==="desk"));
  fitDesk();
  if(!quiet){S.railKey=d==="desk"?"desk":S.view;if(d==="desk")S.view="edit";render(true);}
}
document.getElementById("dev-phone").addEventListener("click",function(){if(DEVICE!=="phone")setDevice("phone");});
document.getElementById("dev-desk").addEventListener("click",function(){if(DEVICE!=="desk")jump("desk");});

/* ---------------- actions ---------------- */
document.getElementById("ctl").addEventListener("click",function(e){
  var b=e.target.closest("[data-ctl]");if(!b)return;var c=b.getAttribute("data-ctl");
  if(c==="restart"){S.d=freshDeck();jump("entry-library");}
  if(c==="skip"){clearInterval(genTm);S.view="edit";S.railKey="edit";S.stack=[];render(true);}
  if(c==="skipread"){clearInterval(readTm);S.view="you";S.railKey="you";render(true);}
  if(c==="plan"){S.plan=S.plan==="free"?"pro":"free";render(false);}
});
var phone=document.getElementById("phone");
phone.addEventListener("click",function(e){
  var el=e.target.closest("[data-act]");if(!el||!phone.contains(el))return;
  e.preventDefault();
  var a=el.getAttribute("data-act"),d=function(k){return el.getAttribute("data-"+k);};
  switch(a){
    case "back": back(); break;
    case "go": go(d("v")); break;
    case "start":
      if(d("from")==="detail"){S.d.pitch=true;S.d.cat="Lip oil";S.d.refs=["sample.lipnotes","sample.dewdiary"];go("brand");}
      else go("handle");
      break;
    case "nothanks": S.sheet=false; toast("Closed. It's in Library whenever you want it."); break;
    case "read": S.stack.push({view:S.view});S.view="reading";S.railKey="reading";startRead();render(true); break;
    case "niche": var k=d("k"),n=S.d.me.niche,j=n.indexOf(k); if(j>-1){if(n.length>1)n.splice(j,1);}else if(n.length<2)n.push(k);else{n.shift();n.push(k);} render(false); break;
    case "pitch": S.d.pitch=!S.d.pitch; render(false); break;
    case "pitch-on": S.d.pitch=true; S.slide=4; render(false); toast("Added a slide for "+esc(S.d.brand)+"."); break;
    case "pitch-off": S.d.pitch=false; S.slide=Math.min(S.slide,4); render(false); toast("Removed the brand slide."); break;
    case "build": if(S.plan==="free"&&S.free<=0){go("paid");break;} if(S.plan==="free")S.free--; S.stack=[];S.view="gen";S.railKey="gen";startGen();render(true); break;
    case "slide": S.slide=+d("k"); render(false); break;
    case "rewrite":
      var sk=curKey(),al=ALTS[sk];S.d.alt[sk]=(S.d.alt[sk]+1)%al.length;var nv=al[S.d.alt[sk]];
      Object.keys(nv).forEach(function(f){S.d.s[sk][f]=Array.isArray(nv[f])?nv[f].slice():nv[f];});
      render(false); toast("Rewrote slide "+(S.slide+1)+". Tap again for another version."); break;
    case "copy": try{navigator.clipboard&&navigator.clipboard.writeText("https://"+slug(S.d)).catch(function(){});}catch(x){} toast("<b>Link copied.</b> Paste it into your email or DM."); break;
    case "copy-msg": var mm=document.getElementById("msg"); try{navigator.clipboard&&navigator.clipboard.writeText(mm?mm.value:msgText()).catch(function(){});}catch(x){} toast("Message copied"); break;
    case "pdf": toast("PDF ready: "+slides(S.d).length+" slides"); break;
    case "reply": toast("Opens an email to "+esc(S.d.me.email)); break;
    case "upgrade": S.plan="pro";S.free=1;toast("Pro is on. 20 pitch decks a month.");back(); break;
  }
});
phone.addEventListener("input",function(e){
  var b=e.target.getAttribute&&e.target.getAttribute("data-bind");if(!b)return;
  if(b.indexOf("s.")===0||b.indexOf("me.")===0||["brand","product","site"].indexOf(b)>-1){setP(S.d,b,e.target.value);}
  if(S.view==="edit"||DEVICE==="desk")refreshPreview();
});

buildRail();
var h0=(location.hash||"").slice(1),keys=[];RAIL.forEach(function(g){g.items.forEach(function(it){keys.push(it[0]);});});
if(ALIAS[h0])h0=ALIAS[h0];
if(keys.indexOf(h0)>-1)jump(h0);else jump("entry-library");
if(document.fonts&&document.fonts.ready)document.fonts.ready.then(function(){fitSlides();});
})();
