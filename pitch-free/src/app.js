(function(){
"use strict";

/* ---------------- sample data: invented creators, "sample." handles, invented numbers ---------------- */
/* Same sample creator as the pitch deck proposal. */
var IMG={oil:"../img/oil.jpg",face:"../img/face.jpg",flatlay:"../img/flatlay.jpg",brushes:"../img/brushes.jpg",palette:"../img/palette.jpg",mask:"../img/mask.jpg",neon:"../img/neon.jpg",closet:"../img/closet.jpg",tripod:"../img/tripod.jpg"};
var RAE={handle:"sample.raefilms",name:"Rae M.",videos:62,range:"30 Mar to 26 Sep 2026",avg:9.2,nb:8};
var TOP=[
  {img:"oil",x:12,score:91,views:"112K",date:"14 Aug",hook:"I stopped buying lip gloss after this."},
  {img:"face",x:7,score:78,views:"64K",date:"2 Sep",hook:"Hour one vs hour six. No touch-ups."},
  {img:"flatlay",x:4,score:69,views:"41K",date:"19 Jun",hook:"Everything in my purse, ranked by how often I use it."}
];
var SLOW={handle:"sample.slowstart",videos:24,range:"2 Jun to 24 Sep 2026",avg:3.1,closest:"2.4x"};

/* ---------------- icons ---------------- */
var ICON={
  x:'<path class="i" d="M6 6l12 12M18 6 6 18"/>',
  pause:'<path class="i" d="M9 5v14M15 5v14"/>',
  play:'<path class="i" d="M7 5l12 7-12 7z"/>',
  down:'<path class="i" d="M12 4v11M7.5 10.5 12 15l4.5-4.5M5 19h14"/>',
  share:'<path class="i" d="M12 15V4M8 8l4-4 4 4M5 13v6h14v-6"/>',
  arrow:'<path class="i" d="M5 12h14M13 6l6 6-6 6"/>',
  left:'<path class="i" d="M15 5l-7 7 7 7"/>',
  right:'<path class="i" d="M9 5l7 7-7 7"/>',
  check:'<path class="i" d="M5 12.5l4.5 4.5L19 7.5"/>'
};
function ic(n){return '<svg viewBox="0 0 24 24" aria-hidden="true">'+ICON[n]+'</svg>';}
function bg(k){return 'background-image:url('+IMG[k]+')';}
function esc(t){return String(t).replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;"}[c];});}
function cnt(n,d,s,label){return '<span data-n="'+n+'" data-d="'+(d||0)+'" data-s="'+(s||"")+'">'+(label||(n.toFixed?Number(n).toFixed(d||0):n)+(s||""))+'</span>';}
var SMP='<span class="smp">SAMPLE</span>';

/* ---------------- cards ---------------- */
function readCard(p,hits){
  var t="";for(var k=0;k<p.videos;k++)t+='<i class="'+(hits.indexOf(k)>-1?'hit':'')+'" style="animation-delay:'+(k*14)+'ms"></i>';
  return '<div class="cin"><p class="lab rise">We read</p><p class="big rise d1">'+cnt(p.videos)+'</p><p class="lead rise d2">of your public TikToks.</p>'+
  '<div class="fill"><div class="tiles">'+t+'</div></div><div class="cfoot rise d3"><span>'+p.range+'</span>'+SMP+'</div></div>'+
  '<i class="shp ring bob" style="width:44cqw;height:44cqw;right:-16cqw;top:14cqw;opacity:.9"></i>';
}
function usualCard(p,ups){
  var H=[34,52,41,28,95,47,38,56,44,31,72,49,36,58,42,100],b="";
  H.forEach(function(h,k){var up=ups&&h>70;if(!ups&&h>70)h=h*.62;b+='<i class="'+(up?'up':'')+'" style="height:'+h+'%;animation-delay:'+(k*40)+'ms"></i>';});
  return '<div class="cin"><p class="lab rise">Your usual</p><p class="big rise d1">'+cnt(p.avg,1,"K")+'</p><p class="lead rise d2">views on a typical video of yours.</p>'+
  '<div class="fill"><div class="vbars">'+b+'<div class="base" style="bottom:45%"><span>your usual</span></div></div></div>'+
  '<p class="body rise d3">Every video gets measured against this. Your own bar, not a bigger account’s.</p><div class="cfoot">'+'<span></span>'+SMP+'</div></div>';
}
var CARD={
  c1:{t:"t-ink",n:"Videos we read",h:function(){return readCard(RAE,[4,11,19,27,33,41,50,57]);}},
  c2:{t:"t-cyan",n:"Your usual views",h:function(){return usualCard(RAE,true);}},
  c3:{t:"t-coral",n:"Your biggest breakout",h:function(){var v=TOP[0];return '<i class="shp star spin" style="width:84cqw;height:84cqw;right:-30cqw;top:12cqw"></i>'+
    '<div class="cin"><p class="lab rise">Your biggest breakout</p><p class="big pop" style="font-size:44cqw">'+cnt(v.x,0,"x")+'</p><p class="lead rise d2">your usual views</p>'+
    '<div class="fill"><div class="hero3 rise d3"><div class="th" style="'+bg(v.img)+'"></div><div><q>'+esc(v.hook)+'</q><span class="m">'+v.views+' views · '+v.date+'</span></div></div></div>'+
    '<div class="cfoot"><span></span>'+SMP+'</div></div>';}},
  c4:{t:"t-deep",n:"Your top 3 breakouts",h:function(){return '<i class="shp dot bob" style="width:30cqw;height:30cqw;right:-10cqw;top:15cqw;opacity:.9"></i>'+
    '<div class="cin"><p class="lab rise">Your top 3 breakouts</p><div class="fill"><div class="top3">'+
    TOP.map(function(v,k){return '<div class="t3 rise d'+(k+1)+'"><span class="rk">'+(k+1)+'</span><div class="th" style="'+bg(v.img)+'"></div><div><b>'+v.x+'x</b><span>'+esc(v.hook)+'</span><em>Breakout Score '+v.score+'</em></div></div>';}).join("")+
    '</div></div><p class="body rise d4">Breakout Score: 0 to 100. It shows how much a video beat what your account usually gets.</p><div class="cfoot"><span></span>'+SMP+'</div></div>';}},
  c5:{t:"t-gold",n:"Your breakout rate",h:function(){var o="";for(var k=0;k<8;k++)o+='<i class="'+(k===5?'on':'')+'"></i>';
    return '<i class="shp half" style="width:70cqw;height:35cqw;left:-20cqw;bottom:-2cqw;opacity:.18"></i><div class="cin"><p class="lab rise">Your breakout rate</p><p class="big rise d1">1<small>in</small>8</p><p class="lead rise d2">of your videos broke out.</p>'+
    '<div class="fill"><div class="odds">'+o+'</div></div><p class="body rise d3">8 of your 62 videos beat your usual by enough to count.</p><div class="cfoot"><span></span>'+SMP+'</div></div>';}},
  c6:{t:"t-blush",n:"Your hook style",h:function(){return '<i class="shp ring spin" style="width:70cqw;height:70cqw;right:-40cqw;top:14cqw;border-style:dashed"></i><i class="shp dot bob" style="width:16cqw;height:16cqw;right:12cqw;top:34cqw;background:var(--ac)"></i>'+
    '<div class="cin"><p class="lab rise">Your hook style</p><div class="fill" style="justify-content:flex-start"><p class="hook pop">You open on the <span>product.</span></p></div>'+
    '<p class="body rise d2">In your breakouts, the product is on screen in the first second, before you say a word.</p><div class="cfoot rise d3"><span>From your 8 breakouts</span>'+SMP+'</div></div>';}},
  c7:{t:"t-teal",n:"What works for you",h:function(){
    var S=[18,27,34,22,16,29,48,24],p="",pct=function(s){return (s/60*100).toFixed(2)+'%';};
    S.forEach(function(s,k){p+='<i class="pt" style="left:'+pct(s)+';top:'+(k%2?13:7.4)+'cqw;animation-delay:'+(300+k*90)+'ms"></i>';});
    return '<div class="cin"><p class="lab rise">What works for you</p><p class="big rise d1" style="font-size:27cqw">15<small>to</small>30</p><p class="lead rise d2">seconds long.</p>'+
    '<div class="fill"><div class="tl"><div class="axis"></div><div class="band" style="left:25%;width:25%"></div>'+p+
    ['0s','15s','30s','60s'].map(function(t,k){return '<span class="tk" style="left:'+[3,25,50,95][k]+'%">'+t+'</span>';}).join("")+'</div></div>'+
    '<p class="body rise d3">6 of your 8 breakouts run this long. Most are tests with the proof on screen.</p><div class="cfoot"><span></span>'+SMP+'</div></div>';}},
  c8:{t:"t-ink",n:"Your share card",share:1,h:function(){return '<div class="shareview"><div class="frame">'+shareCard("still")+'</div>'+
    '<div class="row"><a class="save" href="img/share-sample.png" download="my-breakouts-sample.png" data-act="save">'+ic("down")+'Save image</a><button type="button" class="share" data-act="share">'+ic("share")+'Share</button></div>'+
    '<p class="hint">Post it to your TikTok story.</p></div>';}},
  c9:{t:"t-cyan",n:"Find Breakouts of your own",h:function(){return '<i class="shp sq bob" style="width:30cqw;height:30cqw;left:-8cqw;top:40cqw;rotate:18deg;opacity:.9"></i>'+
    '<div class="cin"><div class="fill"><div class="fan">'+
    ['112K','64K','41K'].map(function(n,k){return '<div class="sl s'+(k+1)+'"><i class="c"></i><i class="h"></i><i></i><i style="width:80%"></i><div class="n"><b>'+n+'</b></div></div>';}).join("")+
    '</div></div><p class="cta-h rise d1">Find Breakouts of your own!</p><p class="body rise d2">Try it on your own brand, product, or style. See what’s breaking out on TikTok and how to remake it.</p>'+
    '<div class="cbtns rise d3">'+(APP?'<button type="button" class="cbtn" data-act="appsearch">Search a new product or video style</button>':'<a class="cbtn" href="../#teaser" target="_blank" rel="noopener">Start free '+ic("arrow").replace('<svg','<svg style="width:5cqw;height:5cqw"')+'</a>')+'<button type="button" class="cbtn alt" data-act="replay">Watch again</button></div>'+
    '<div class="cfoot"><span>'+(APP?'':'Free. Just your email.')+'</span>'+SMP+'</div></div>';}},
  /* edge cases */
  p1:{t:"t-ink",n:"Private account",h:function(){return '<i class="shp ring" style="width:56cqw;height:56cqw;right:-26cqw;top:-8cqw"></i>'+
    '<div class="cin"><p class="lab rise">@sample.quietfilms</p><div class="fill" style="justify-content:flex-start"><p class="hook pop" style="font-size:17cqw">This account is <span>private.</span></p></div>'+
    '<p class="body rise d2">We can only read public videos. Switch the account to public in TikTok, then try again.</p><div class="cbtns rise d3"><button type="button" class="cbtn" data-act="again">Try another handle</button></div><div class="cfoot"><span></span>'+SMP+'</div></div>';}},
  f1:{t:"t-gold",n:"Not enough videos yet",h:function(){var o="";for(var k=0;k<15;k++)o+='<i class="'+(k<9?'on':'')+'"></i>';
    return '<div class="cin"><p class="lab rise">Not enough videos yet</p><p class="big rise d1">'+cnt(9)+'</p><p class="lead rise d2">public videos so far.</p><div class="fill"><div class="odds w5">'+o+'</div></div>'+
    '<p class="body rise d3">We need 15 to know what you usually get. Post 6 more and your breakouts show up here.</p><div class="cbtns rise d4"><button type="button" class="cbtn" data-act="again">Try another handle</button></div><div class="cfoot"><span></span>'+SMP+'</div></div>';}},
  n1:{t:"t-ink",n:"Videos we read",h:function(){return readCard(SLOW,[]);}},
  n2:{t:"t-cyan",n:"Your usual views",h:function(){return usualCard(SLOW,false);}},
  n3:{t:"t-blush",n:"No breakouts yet",h:function(){return '<i class="shp dot bob" style="width:22cqw;height:22cqw;right:10cqw;top:26cqw;background:var(--ac)"></i><i class="shp ring" style="width:50cqw;height:50cqw;left:-26cqw;top:34cqw;border-style:dashed"></i>'+
    '<div class="cin"><p class="lab rise">Your breakouts</p><div class="fill" style="justify-content:flex-start;align-items:flex-end"><p class="hook pop" style="font-size:24cqw">Not <span>yet.</span></p></div>'+
    '<p class="body rise d2">None of your 24 videos beat your usual by enough to count. Your closest did '+SLOW.closest+' your usual views.</p><p class="body rise d3">Most accounts get their first one by posting more of what came closest.</p>'+
    '<div class="cbtns rise d4"><button type="button" class="cbtn" data-act="ub">See breakouts in your niche</button><button type="button" class="cbtn alt" data-act="replay">Watch again</button></div><div class="cfoot"><span></span>'+SMP+'</div></div>';}}
};
function shareCard(mode){
  var v=TOP[0];
  return '<div class="card sc t-coral '+(mode||"still")+'"><i class="shp star" style="width:46cqw;height:46cqw;right:-12cqw;top:-10cqw;background:#FFC53A"></i>'+
  '<div class="cin"><p class="hdl"><span class="av">R</span>@'+RAE.handle+'</p>'+
  '<p class="h1" style="margin-top:3cqw">My biggest<br>TikTok did</p><p class="big" style="color:#171312">'+v.x+'x</p><p class="h1">my usual views.</p>'+
  '<div class="fill"><div class="row2"><div class="th" style="'+bg(v.img)+'"></div><div class="facts"><p><b>1 in 8</b> of my videos broke out.</p><p>I open on the <b>product</b>.</p></div></div></div>'+
  '<div class="cfoot"><span class="mark">ugcbreakouts.com/story</span>'+SMP+'</div></div></div>';
}
var SETS={
  main:{h:RAE.handle,a:"R",cards:["c2","c3","c5","c6","c7","c8","c9"]},
  none:{h:SLOW.handle,a:"S",cards:["n1","n2","n3"]},
  priv:{h:"sample.quietfilms",a:"Q",cards:["p1"]},
  few:{h:"sample.newfilms",a:"N",cards:["f1"]}
};
function renderCard(id,mode,mini){
  var c=CARD[id];
  if(mini&&c.share)return shareCard("still");
  return '<div class="card '+c.t+' '+mode+'">'+c.h()+'</div>';
}
function player(set,i,o){
  o=o||{};var st=SETS[set],id=st.cards[i],c=CARD[id],n=st.cards.length;
  var bars=st.cards.map(function(x,k){return '<i class="'+(k<i?'done':(k===i?(o.play?'cur':'full'):''))+'"><b></b></i>';}).join("");
  return '<div class="story '+c.t+(o.play?' play':'')+'" data-story="'+set+'" style="--dur:'+(c.share?9:6)+'s">'+
    '<div class="schrome"><div class="bars">'+bars+'</div><div class="srow"><span class="who"><span class="av">'+st.a+'</span><span>@'+st.h+'</span></span><span class="sp"></span>'+
    (o.bare?'':'<button type="button" class="sbtn" data-act="toggle" aria-label="'+(o.play?'Pause':'Play')+'">'+ic(o.play?"pause":"play")+'</button><button type="button" class="sbtn" data-act="close" aria-label="Close">'+ic("x")+'</button>')+
    '</div></div>'+renderCard(id,o.still?"still":"anim")+
    (o.bare?'':'<button type="button" class="sr" data-act="prev">Previous card</button><button type="button" class="sr" data-act="next">Next card</button>')+'</div>';
}

/* ---------------- screens ---------------- */
function mini(id,cls){return '<div class="mini '+(cls||"")+'">'+renderCard(id,"still",true)+'</div>';}
function landingBody(){
  return '<div class="lbody"><h1>Which of your TikToks <span>broke out?</span></h1><p class="sub">Type your handle. We compare every video to what you usually get, then show you your breakouts.</p>'+
  '<form class="hform" data-form="handle"><label for="hdl">Your TikTok handle</label><div class="hin"><span>@</span><input id="hdl" name="hdl" autocomplete="off" autocapitalize="none" spellcheck="false" value="'+esc(S.handle)+'"></div>'+
  '<button class="go" type="submit">Show my breakouts '+ic("arrow")+'</button></form>'+(S.err?'<p class="herr" role="alert">'+S.err+'</p>':'')+'<p class="tiny">Reads public videos only. No login.</p></div>';
}
var V={
  landing:function(){
    return '<div class="land"><div class="ltop"><span class="logo">UGC <b>Breakouts</b></span><span class="sp"></span><button type="button" class="signin" data-act="signin">Sign in</button></div>'+
    '<div class="lfan">'+mini("c2","m1")+mini("c3","m2")+mini("c5","m3")+'</div>'+landingBody()+'</div>';
  },
  reading:function(){
    var steps=["Finding your usual views","Scoring every video","Picking your breakouts"];
    return '<div class="read"><i class="glow"></i><div class="deal">'+["oil","face","palette","flatlay"].map(function(k,j){return '<div class="th" style="'+bg(k)+';--r:'+([-6,4,-2,7][j])+'deg;animation-delay:'+(j*.6)+'s"></div>';}).join("")+'</div>'+
    '<div><div class="cnt" id="rcnt">'+S.rc+'</div><p class="cl">videos read on @'+esc(S.handle)+'</p></div>'+
    '<ol>'+steps.map(function(s,k){return '<li class="'+(S.rs>k?'on':'')+'"><i></i>'+s+'</li>';}).join("")+'</ol></div>';
  },
  story:function(){return player(S.set,S.i,{play:S.play,still:S.still});},
  dm:function(){
    var link='<a class="dmlink" href="#" data-act="openlink"><div class="mini" style="'+bg("oil")+'"></div><div><b>@'+RAE.handle+', your breakouts</b><span>ugcbreakouts.com/story/'+RAE.handle+'</span></div></a>';
    return '<div class="dm"><div class="dmtop"><button type="button" class="dmback" aria-label="Back" data-act="noop">'+ic("left")+'</button><span class="av ub">UB</span><div><b>UGC Breakouts</b><span>@ugcbreakouts</span></div></div>'+
    '<div class="dmbody"><p class="dmday">Today</p>'+
    '<div class="msg them">Hey Rae! We ran your TikToks through UGC Breakouts and found your breakouts. Want to see them?</div>'+
    '<div class="msg me">yes!! show me</div>'+
    '<div class="msg them">Here you go. Tap through, it takes a minute.</div>'+
    '<div class="msg them lk">'+link+'</div></div>'+
    '<div class="dmbar"><span>Message...</span></div></div>';
  }
};
function desk1(){
  return '<div class="dk"><div class="ltop"><span class="logo">UGC <b>Breakouts</b></span><span class="sp"></span><button type="button" class="signin" data-act="signin">Sign in</button></div>'+
  '<div class="dk1">'+landingBody()+'<div class="dkwrap"><button type="button" class="dkarrow l" data-act="prev" aria-label="Previous card">'+ic("left")+'</button>'+
  '<div class="dkp">'+player("main",S.i,{play:S.play,still:S.still})+'</div><button type="button" class="dkarrow r" data-act="next" aria-label="Next card">'+ic("right")+'</button></div></div></div>';
}
function desk2(){
  return '<div class="dk"><div class="ltop"><span class="logo">UGC <b>Breakouts</b></span></div><div class="dk2"><h2>@'+RAE.handle+', your breakouts</h2><p class="sub">All '+SETS.main.cards.length+' cards. Click one to play it.</p><div class="cgrid">'+
  SETS.main.cards.map(function(id,k){return '<figure><div class="mini" role="button" tabindex="0" data-k="'+k+'" aria-label="Play card '+(k+1)+'">'+renderCard(id,"still",true)+'</div><figcaption><span>'+(k+1)+'</span>'+CARD[id].n+'</figcaption></figure>';}).join("")+
  '</div></div></div>';
}

/* ---------------- notes ---------------- */
function li(t,txt){return '<li><span class="tag '+t+'">'+({r:"IVAN",c:"CALL",a:"ASK",f:"LOCK",d:"DEV",q:"SOURCE",v:"VEEJAY"})[t]+'</span><span>'+txt+'</span></li>';}
function src(u,l){return ' <a href="'+u+'" target="_blank" rel="noopener" style="color:var(--acc)">'+l+'</a>';}
var NOTES={
  dm:{id:"L0 · the DM",h:"The DM",li:[
    ["r","Ivan, 1 Oct: DM creators from the UB TikTok, tell them we found their breakouts, and if they say yes, send their profile analysis."],
    ["a","Sample DM copy only. The real script is its own row on the priorities Sheet."],
    ["a","The link opens straight into their story, with the handle already filled in. No typing, no login."]]},
  landing:{id:"L1 · ugcbreakouts.com/story",h:"Landing",li:[
    ["r","Ivan, 1 Oct: not a fan of the pitch deck for now, keep the profile story. The deck ask at the end is gone."],
    ["v","Veejay, 3 Oct: these breakout cards are their own thing, separate from the profile analyzer (how creators read their own account on their profile in the app)."],
    ["a","Anyone can still type a handle here. Keep this public page, or only open it from the DM link?"],
    ["d","Anyone can type any public handle. Cache each handle’s result for 24 hours and rate limit per IP, since every read is a scrape."]]},
  reading:{id:"L2 · reading the account",h:"Reading your account",li:[
    ["v","The short “reading your account” moment from the brief. The count runs up while videos deal across the screen."],
    ["a","How long a read takes is a guess. Searches take 15 seconds to a minute, and this scrapes one account. Expect the short end. Lester to confirm."],
    ["d","Needs: public videos with views and length, the account’s average, a Breakout Score per video. Same pipeline as a search on one handle."]]},
  c1:{id:"Card 1 of 9 · free",h:"Videos we read",li:[
    ["a","Opens on the count and the date range, which makes the numbers after it read as fair. The lit tiles hint at the 8 breakouts to come."],
    ["f","SAMPLE on every card, and every handle starts with “sample.” Nothing here is a real account."]]},
  c2:{id:"Card 1 of 7 · free",h:"Your usual views",li:[
    ["v","Veejay, 2 Oct: less overwhelming. The story is 7 cards now: “Videos we read” (the reading screen already counts them) and “Your top 3” (it repeated the biggest breakout) are out."],
    ["a","The baseline, framed as the creator’s own bar and never compared with bigger accounts. It is what makes the next card’s 12x mean something."],
    ["d","Average of the creator’s public videos in the range. If Ivan prefers a median so one huge video doesn’t skew it, the wording stays the same."]]},
  c3:{id:"Card 2 of 7 · free",h:"Your biggest breakout",li:[
    ["v","From the brief: “12x your usual views”, the video thumbnail and its hook."],
    ["f","Breakout Score: “A score from 0 to 100. It shows how much a video beat the average of what that account usually gets.” The card leads with the multiple because it needs no explaining."],
    ["a","Thumbnails here are the creator’s own videos, shown to the creator. No other creator’s content appears anywhere in the free tool."]]},
  c4:{id:"Card 4 of 9 · free",h:"Your top 3 breakouts",li:[
    ["a","A ranked list, with the multiple as the big number and the Breakout Score under it. The one line definition sits under the list."],
    ["a","Tapping a breakout could open it on TikTok. Left out for now, the same as Ivan’s “no Watch on TikTok” call in the app."]]},
  c5:{id:"Card 3 of 7 · free",h:"Your breakout rate",li:[
    ["a","8 of 62 is shown as “1 in 8”, which reads faster than 13% on a phone."],
    ["a","What counts as a breakout is still open. This card assumes a Breakout Score of 60 or more."]]},
  c6:{id:"Card 4 of 7 · free",h:"Your hook style",li:[
    ["f","A plain label from the creator’s own breakouts. No rarity figure and no “top x% of creators”: UB doesn’t see a fair sample of all creators, so any percentile would be invented. Ivan’s lock: never invent Breakout numbers."],
    ["a","The label needs a breakout analysis of the top videos, which costs a model call. Run it for free here, or hide this card until sign up?"]]},
  c7:{id:"Card 5 of 7 · free",h:"What works for you",li:[
    ["a","Length comes straight from public data. The format line (“tests with the proof on screen”) comes from the same analysis as card 6."],
    ["a","If there aren’t enough breakouts to find a length pattern, this card is skipped rather than shown weak."]]},
  c8:{id:"Card 6 of 7 · free",h:"Share card",li:[
    ["v","A 9:16 image the creator can save and post, with a small ugcbreakouts.com/story mark. Save image downloads the sample PNG."],
    ["f","The hint says TikTok story only. Share opens the phone’s own share sheet. UB copy names TikTok only."],
    ["a","No text under about 36px at 1080 wide. The handle is on by default. Let creators hide it?"],
    ["q","Spotify reports 500M+ Wrapped shares in the first 24 hours (company claim). Duolingo saw share rates go up when the flattering number moved onto the share card."+src("https://blog.duolingo.com/year-in-review-behind-the-scenes","Duolingo Blog")]]},
  c9:{id:"Card 7 of 7 · the ask",h:"Find Breakouts of your own",li:[
    ["r","Replaces the pitch deck ask. Heading, line and “Free. Just your email.” are Ivan’s own copy from the Shared screen CTA."]
    ]},
  "private":{id:"E1 · edge case",h:"Private account",li:[
    ["a","One card, then back to the handle box. Nothing is read."]]},
  few:{id:"E2 · edge case",h:"Not enough videos yet",li:[
    ["a","Under 15 public videos, the average isn’t steady enough. The card counts what they have and what’s left, 9 of 15."],
    ["a","15 is a guess. An “email me at 15 videos” button would bring these creators back. Worth building?"]]},
  none:{id:"E3 · edge case",h:"No breakouts yet",li:[
    ["v","From the brief: encouraging, and it still gives the baseline. Cards 1 and 2 play as normal, then this one."],
    ["a","Shows the closest video as a multiple, from their own data. The button goes to UB’s search."]]},
  desk1:{id:"D1 · desktop",h:"Story beside the landing",li:[
    ["v","The desktop view from the brief: the landing on the left, the story as a phone sized card on the right."],
    ["a","Arrows and the keyboard’s left and right keys move between cards. The handle box stays usable for trying another account."]]},
  desk2:{id:"D2 · desktop",h:"All cards",li:[
    ["v","The other desktop option from the brief: every card in a grid. Click one to play it."],
    ["a","Pick one of the two for launch. D1 keeps the story feel, D2 is quicker to scan."]]},
  split:{id:"Review",h:"Free vs sign up",li:[
    ["v","<b>Free, no login:</b> the DM link, the handle box, the reading moment, all 7 story cards, the share card with Save image and Share."],
    ["v","<b>Sign up:</b> UB itself, from the last card."]]}
};
var QUESTIONS=[
  "Keep a public page where anyone types a handle, or only open the cards from the DM link?",
  "Cache each handle for 24 hours and rate limit per IP? Every read is a scrape.",
  "Run a breakout analysis for free to get the hook style and format (cards 6 and 7), or hide those until sign up?",
  "15 public videos minimum and a Breakout Score of 60 to count as a breakout?",
  "Handle on the share card by default, with an option to hide it?",
  "Launch the desktop as the story beside the landing (D1) or as a grid of cards (D2)?"
];
function notesHtml(key){
  var legend='<div class="legend"><span><span class="tag r">IVAN</span> his notes</span><span><span class="tag c">CALL</span> Ivan calls</span><span><span class="tag v">VEEJAY</span> Veejay asked for it</span><span><span class="tag a">ASK</span> our suggestion, needs Ivan</span><span><span class="tag q">SOURCE</span> research, linked</span><span><span class="tag d">DEV</span> for Lester</span><span><span class="tag f">LOCK</span> his rules</span></div>';
  if(key==="questions")return legend+'<p class="sid">Open</p><h2>Questions for Ivan</h2><ul>'+QUESTIONS.map(function(q){return li("a",q);}).join("")+'</ul>';
  var n=NOTES[key]||NOTES.landing;
  return legend+'<p class="sid">'+n.id+'</p><h2>'+n.h+'</h2><ul>'+n.li.map(function(x){return li(x[0],x[1]);}).join("")+'</ul>';
}

/* ---------------- rail ---------------- */
var RAIL=[
  {g:"Landing",items:[["dm","L0","The DM"],["landing","L1","/story landing"],["reading","L2","Reading your account"]]},
  {g:"Story, free",items:SETS.main.cards.map(function(id,k){return [id,String(k+1),CARD[id].n];})},
  {g:"Edge cases",items:[["private","E1","Private account"],["few","E2","Not enough videos yet"],["none","E3","No breakouts yet"]]},
  {g:"Desktop",items:[["desk1","D1","Story beside the landing"],["desk2","D2","All cards"]]},
  {g:"Review",items:[["split","","Free vs sign up"],["questions","","Questions for Ivan"]]}
];
var KEYS=[];RAIL.forEach(function(g){g.items.forEach(function(it){KEYS.push(it[0]);});});

/* ---------------- state ---------------- */
var Q=new URLSearchParams(location.search),EXP=Q.get("export"),STILL=Q.has("still")||!!EXP,APP=Q.has("app");
if(APP)document.body.classList.add("app");
function toApp(m){try{parent.postMessage({ub:m},"*");}catch(e){}}
var S={key:"landing",view:"landing",set:"main",i:0,play:false,still:STILL,handle:RAE.handle,err:"",rc:0,rs:0,toast:""};
var DEVICE="phone";
var scr=document.getElementById("scr"),ovl=document.getElementById("ovl");

function railKeyFor(){
  if(DEVICE==="desk")return S.key;
  if(S.view==="story"){if(S.set==="main")return SETS.main.cards[S.i];return {none:"none",priv:"private",few:"few"}[S.set];}
  return S.view;
}
function jump(key){
  clearTimers();S.err="";S.toast="";
  if(key==="desk1"||key==="desk2"){setDevice("desk");S.key=key;S.i=key==="desk1"?2:S.i;S.play=false;render();return;}
  setDevice("phone");S.key=key;
  if(CARD[key]&&SETS.main.cards.indexOf(key)>-1){S.view="story";S.set="main";S.i=SETS.main.cards.indexOf(key);S.play=false;}
  else if(key==="private"){S.view="story";S.set="priv";S.i=0;S.play=false;}
  else if(key==="few"){S.view="story";S.set="few";S.i=0;S.play=false;}
  else if(key==="none"){S.view="story";S.set="none";S.i=2;S.play=false;}
  else if(key==="reading"){S.view="reading";startRead();}
  else if(key==="split"||key==="questions"){S.view="landing";}
  else {S.view=key;}
  render();
}
var readTm=null,autoTm=null;
function clearTimers(){clearInterval(readTm);readTm=null;}
function startRead(){
  clearTimers();S.rc=0;S.rs=0;var target=S.set==="none"?SLOW.videos:RAE.videos,t0=performance.now(),dur=3600;
  if(STILL){S.rc=target;S.rs=3;return;}
  readTm=setInterval(function(){
    if(S.view!=="reading"){clearTimers();return;}
    var p=Math.min(1,(performance.now()-t0)/dur);S.rc=Math.round(target*(1-Math.pow(1-p,2)));S.rs=p>.85?3:(p>.5?2:(p>.15?1:0));
    var el=document.getElementById("rcnt");if(el)el.textContent=S.rc;
    document.querySelectorAll(".read ol li").forEach(function(li,k){li.classList.toggle("on",S.rs>k);});
    if(p>=1){clearTimers();setTimeout(function(){if(S.view==="reading"){S.view="story";S.i=0;S.play=true;S.key=railKeyFor();render();}},700);}
  },50);
}

/* ---------------- render ---------------- */
function render(){
  var key=DEVICE==="desk"?S.key:(S.key==="split"||S.key==="questions"?S.key:railKeyFor());
  S.key=key;
  if(DEVICE==="desk")scr.innerHTML=S.key==="desk2"?desk2():desk1();
  else scr.innerHTML=(V[S.view]||V.landing)();
  scr.scrollTop=0;
  ovl.innerHTML=S.toast?'<div class="toast" role="status">'+S.toast+'</div>':'';
  document.querySelectorAll("#rail-groups [data-jump]").forEach(function(b){var on=b.getAttribute("data-jump")===key;b.classList.toggle("on",on);if(on)b.setAttribute("aria-current","page");else b.removeAttribute("aria-current");});
  var sel=document.getElementById("jump-sel");if(sel.value!==key)sel.value=key;
  document.getElementById("notes").innerHTML=notesHtml(key);
  document.getElementById("where").textContent=key==="questions"?"Questions":(NOTES[key]?NOTES[key].id:"");
  var ctl="";
  if(S.view==="reading"&&DEVICE==="phone")ctl+='<button data-ctl="skip">Skip ahead</button>';
  if(DEVICE==="phone"&&S.view==="landing")ctl+='<button data-ctl="try" data-h="sample.quietfilms">Try private</button><button data-ctl="try" data-h="sample.newfilms">Try 9 videos</button><button data-ctl="try" data-h="sample.slowstart">Try no breakouts</button>';
  if(S.view==="story"||DEVICE==="desk")ctl+='<button data-ctl="auto">'+(S.play?"Pause auto play":"Auto play")+'</button>';
  document.getElementById("ctl").innerHTML=ctl+'<button data-ctl="restart">Restart</button>';
  if(!S.still)countUp(scr);
  if(history.replaceState&&!EXP)history.replaceState(null,"","#"+key);
}
function countUp(root){
  var reduce=window.matchMedia&&window.matchMedia("(prefers-reduced-motion: reduce)").matches;if(reduce)return;
  root.querySelectorAll(".anim [data-n]").forEach(function(el){
    var n=parseFloat(el.getAttribute("data-n")),d=+el.getAttribute("data-d"),s=el.getAttribute("data-s"),t0=performance.now(),dur=900;
    (function step(){var p=Math.min(1,(performance.now()-t0)/dur),v=n*(1-Math.pow(1-p,3));el.textContent=v.toFixed(d)+s;if(p<1)requestAnimationFrame(step);})();
  });
}
function toast(m){S.toast=m;ovl.innerHTML='<div class="toast" role="status">'+m+'</div>';clearTimeout(toast.tm);toast.tm=setTimeout(function(){S.toast="";ovl.innerHTML="";},2600);}

/* ---------------- story navigation ---------------- */
function curSet(){return DEVICE==="desk"?"main":S.set;}
function step(d){
  var n=SETS[curSet()].cards.length,j=S.i+d;
  if(j<0)j=0;
  if(j>=n){S.play=false;j=n-1;}
  S.i=j;if(DEVICE==="desk"&&S.key==="desk2")S.key="desk1";
  render();
}
function onAct(a,el,e){
  switch(a){
    case "next":step(1);break;
    case "prev":step(-1);break;
    case "toggle":S.play=!S.play;render();break;
    case "close":if(APP){toApp("close");break;}if(DEVICE==="desk"){S.i=0;S.play=false;render();}else{S.view="landing";S.key="landing";render();}break;
    case "replay":S.i=0;S.play=true;render();break;
    case "again":S.view="landing";S.key="landing";S.handle="";render();var h=document.getElementById("hdl");if(h)h.focus();break;
    case "openlink":e.preventDefault();S.handle=RAE.handle;S.set="main";S.view="reading";startRead();render();break;
    case "noop":break;
    case "appsearch":toApp("search");break;
    case "signin":toast("Existing accounts sign in the usual way.");break;
    case "ub":toast("Opens UGC Breakouts search, signed out.");break;
    case "share":e.preventDefault();toast("Opens the phone’s share sheet with the image.");break;
    case "save":toast("Saved the sample image.");break;
    case "dplay":S.i=+el.getAttribute("data-k");S.key="desk1";S.play=false;render();break;
  }
}
var phone=document.getElementById("phone");
phone.addEventListener("click",function(e){
  var gm=e.target.closest(".cgrid .mini");if(gm){e.preventDefault();S.i=+gm.getAttribute("data-k");S.key="desk1";S.play=false;render();return;}
  var el=e.target.closest("[data-act]");
  if(el&&phone.contains(el)){if(el.tagName!=="A"||/^(save|openlink)$/.test(el.getAttribute("data-act")))onAct(el.getAttribute("data-act"),el,e);if(el.tagName!=="A")e.preventDefault();return;}
  var st=e.target.closest(".story");
  if(st&&!e.target.closest(".schrome")){var r=st.getBoundingClientRect();step((e.clientX-r.left)<r.width*.32?-1:1);}
});
phone.addEventListener("animationend",function(e){
  if(e.animationName==="fillbar"&&S.play){step(1);}
});
phone.addEventListener("submit",function(e){
  e.preventDefault();var f=e.target.getAttribute("data-form");
  if(f==="handle"){
    var v=(document.getElementById("hdl").value||"").trim().replace(/^@/,"").toLowerCase();
    if(!v){S.err="Type a TikTok handle to start.";render();return;}
    if(v.indexOf("sample.")!==0){S.err="This prototype only reads sample handles. Try sample.raefilms.";S.handle=v;render();return;}
    S.handle=v;S.err="";
    if(v==="sample.quietfilms"){setDevice("phone");S.view="story";S.set="priv";S.i=0;S.play=false;render();return;}
    if(v==="sample.newfilms"){setDevice("phone");S.view="story";S.set="few";S.i=0;S.play=false;render();return;}
    S.set=v==="sample.slowstart"?"none":"main";
    if(DEVICE==="desk"){S.i=0;S.play=true;S.key="desk1";render();return;}
    S.view="reading";startRead();render();
  }
});
document.addEventListener("keydown",function(e){
  if((e.key==="Enter"||e.key===" ")&&e.target.matches&&e.target.matches(".cgrid .mini")){e.preventDefault();e.target.click();return;}
  if(e.target.matches&&e.target.matches("input,select,textarea"))return;
  var onStory=S.view==="story"||DEVICE==="desk";
  if(!onStory)return;
  if(e.key==="ArrowRight"){e.preventDefault();step(1);}
  if(e.key==="ArrowLeft"){e.preventDefault();step(-1);}
});
document.getElementById("ctl").addEventListener("click",function(e){
  var b=e.target.closest("[data-ctl]");if(!b)return;var c=b.getAttribute("data-ctl");
  if(c==="restart"){S.handle=RAE.handle;S.set="main";S.i=0;jump(DEVICE==="desk"?"desk1":"landing");}
  if(c==="skip"){clearTimers();S.view="story";S.i=0;S.play=true;render();}
  if(c==="auto"){S.play=!S.play;render();}
  if(c==="try"){S.handle=b.getAttribute("data-h");render();}
});

/* ---------------- device ---------------- */
function fitDesk(){
  if(DEVICE!=="desk")return;
  var main=document.querySelector(".main"),w=main.clientWidth-parseFloat(getComputedStyle(main).paddingLeft)*2;
  var sc=document.body.classList.contains("fs")?Math.min(1.25,(window.innerWidth-24)/1280,(window.innerHeight-70)/800):Math.min(1,w/1280,Math.max(.45,(window.innerHeight-90)/800));
  document.body.style.setProperty("--sc",sc.toFixed(4));
}
window.addEventListener("resize",fitDesk);
function setDevice(d){
  DEVICE=d;document.body.classList.toggle("desk",d==="desk");
  document.getElementById("dev-phone").setAttribute("aria-pressed",String(d==="phone"));
  document.getElementById("dev-desk").setAttribute("aria-pressed",String(d==="desk"));
  fitDesk();
}
document.getElementById("dev-phone").addEventListener("click",function(){if(DEVICE!=="phone")jump("landing");});
document.getElementById("dev-desk").addEventListener("click",function(){if(DEVICE!=="desk")jump("desk1");});

/* ---------------- rail ---------------- */
(function(){
  var g=document.getElementById("rail-groups"),sel=document.getElementById("jump-sel");
  g.innerHTML=RAIL.map(function(grp){return '<div class="grp"><h2>'+grp.g+'</h2>'+grp.items.map(function(it){return '<button type="button" data-jump="'+it[0]+'"><span>'+it[1]+'</span>'+it[2]+'</button>';}).join("")+'</div>';}).join("");
  sel.innerHTML=RAIL.map(function(grp){return '<optgroup label="'+grp.g+'">'+grp.items.map(function(it){return '<option value="'+it[0]+'">'+(it[1]?it[1]+' · ':'')+it[2]+'</option>';}).join("")+'</optgroup>';}).join("");
  g.addEventListener("click",function(e){var b=e.target.closest("[data-jump]");if(b)jump(b.getAttribute("data-jump"));});
  sel.addEventListener("change",function(){jump(sel.value);});
})();

/* ---------------- export mode (for PNGs) ---------------- */
if(EXP){
  document.body.classList.add("exp");
  var box=document.createElement("div");box.className="expbox";
  var m=EXP.match(/^(main|none|priv|few)-(\d)$/);
  if(EXP==="share")box.innerHTML=shareCard("still");
  else if(m)box.innerHTML=player(m[1],+m[2],{still:true,bare:true});
  document.body.appendChild(box);
  return;
}
window.addEventListener("hashchange",function(){var k=(location.hash||"").slice(1);if(KEYS.indexOf(k)>-1&&k!==S.key)jump(k);});
var h0=(location.hash||"").slice(1);
if(!APP)/* ---------------- full screen mockup ---------------- */
(function(){
  var bar=document.querySelector(".stagebar");if(!bar)return;
  var b=document.createElement("button");b.type="button";b.className="fsbtn";b.setAttribute("aria-pressed","false");
  var ICO='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5"/></svg>';
  function label(on){b.innerHTML=ICO+(on?"Exit full screen":"Full screen");b.setAttribute("aria-pressed",String(on));}
  label(false);
  var ctl=bar.querySelector(".ctl");bar.insertBefore(b,ctl);
  bar.style.gap="8px";
  function set(on){
    document.body.classList.toggle("fs",on);label(on);
    if(on&&document.documentElement.requestFullscreen&&!document.fullscreenElement){document.documentElement.requestFullscreen().catch(function(){});}
    if(!on&&document.fullscreenElement&&document.exitFullscreen){document.exitFullscreen().catch(function(){});}
    window.dispatchEvent(new Event("resize"));
  }
  b.addEventListener("click",function(){set(!document.body.classList.contains("fs"));});
  document.addEventListener("fullscreenchange",function(){if(!document.fullscreenElement&&document.body.classList.contains("fs"))set(false);});
  document.addEventListener("keydown",function(e){
    if(e.target.matches&&e.target.matches("input,textarea,select"))return;
    if(e.key==="Escape"&&document.body.classList.contains("fs"))set(false);
    if((e.key==="f"||e.key==="F")&&!e.metaKey&&!e.ctrlKey)set(!document.body.classList.contains("fs"));
  });
  if(/[?&]fs\b/.test(location.search))set(true);
})();
if(APP){jump("c2");S.play=true;render();}
else jump(KEYS.indexOf(h0)>-1?h0:"dm");
})();
