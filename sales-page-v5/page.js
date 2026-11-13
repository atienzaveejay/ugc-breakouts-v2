/* UGC Breakouts sales page v3: header, reveals, phone demos, pricing toggle. */
(function(){
var reduce=window.matchMedia&&window.matchMedia("(prefers-reduced-motion: reduce)").matches;
var shot=/[?&]shot\b/.test(location.search);
var doc=document.documentElement;
if(!reduce&&!shot)doc.classList.add("js");

/* header turns light once the hero is behind it */
var top=document.querySelector(".top"),hero=document.querySelector(".hero");
function hdr(){top.classList.toggle("light",hero.getBoundingClientRect().bottom<70);}
addEventListener("scroll",hdr,{passive:true});hdr();

/* reveals and bar growth */
var io=("IntersectionObserver" in window)?new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add("in");io.unobserve(e.target);}});},{rootMargin:"0px 0px -12% 0px"}):null;
document.querySelectorAll(".rv,.grow,.grow-b").forEach(function(el){if(io&&!shot&&!reduce)io.observe(el);else el.classList.add("in");});

/* how it works: the line fills and each dot lights as you read */
var flow=document.querySelector(".flow");
if(flow){var lis=flow.querySelectorAll("li");
 function fl(){var r=flow.getBoundingClientRect(),mid=innerHeight*.62;
  if(reduce||shot){flow.style.setProperty("--fill",1);lis.forEach(function(l){l.classList.add("on");});return;}
  var p=Math.max(0,Math.min(1,(mid-r.top)/Math.max(1,r.height-40)));flow.style.setProperty("--fill",p.toFixed(3));
  lis.forEach(function(l){l.classList.toggle("on",l.getBoundingClientRect().top+18<mid);});}
 addEventListener("scroll",fl,{passive:true});addEventListener("resize",fl);fl();}

/* phone demos: each iframe loops input > processing > output; tabs jump to a beat */
var HOLD={card:[1900,2300,4600],top:[1900,2300,4600],script:[3300,2300,4800],rewind:[1900,2300,4200,4200],brief:[1900,2300,5000]};
var demos=[];
document.querySelectorAll(".demo").forEach(function(d){
 var f=d.querySelector("iframe"),m=d.getAttribute("data-m"),tabs=[].slice.call(d.querySelectorAll("button[data-i]")),pb=d.querySelector(".dplay");
 var st={el:d,f:f,m:m,tabs:tabs,pb:pb,playing:!reduce&&!shot,vis:false,ready:false};demos.push(st);
 function send(o){try{f.contentWindow.postMessage(o,"*");}catch(e){}}
 st.send=send;
 tabs.forEach(function(b){b.addEventListener("click",function(){st.playing=false;send({cmd:"go",i:+b.getAttribute("data-i")});setPB();});});
 function setPB(){if(!pb)return;pb.setAttribute("aria-label",st.playing?"Pause the sample":"Play the sample");
  pb.innerHTML=st.playing?'<svg viewBox="0 0 12 12"><rect x="2" y="1.5" width="2.8" height="9" rx=".6"/><rect x="7.2" y="1.5" width="2.8" height="9" rx=".6"/></svg>':'<svg viewBox="0 0 12 12"><path d="M3 1.5l7.5 4.5L3 10.5z"/></svg>';}
 st.setPB=setPB;setPB();
 if(pb)pb.addEventListener("click",function(){st.playing=!st.playing;send({cmd:st.playing?"play":"pause"});setPB();});
 if(reduce&&pb)pb.hidden=true;
 f.addEventListener("load",function(){send({cmd:"hello"});});
 send({cmd:"hello"});
});
function mark(st,i,playing){
 st.tabs.forEach(function(b){var on=+b.getAttribute("data-i")===i;b.setAttribute("aria-pressed",on?"true":"false");
  var g=b.querySelector(".pg");if(g){g.classList.remove("run");if(on&&playing){b.style.setProperty("--hold",(HOLD[st.m]||[3000])[i]+"ms");void g.offsetWidth;g.classList.add("run");}}});
}
addEventListener("message",function(e){var d=e.data||{};
 demos.forEach(function(st){if(e.source!==st.f.contentWindow)return;
  if(d.type==="ready"){if(st.ready)return;st.ready=true;if(shot)st.send({cmd:"still"});else if(st.vis&&st.playing)st.send({cmd:"visible"});mark(st,d.out,false);}
  if(d.type==="beat"){if(!d.playing&&st.playing&&st.started){st.playing=false;st.setPB();}if(d.playing)st.started=true;mark(st,d.i,d.playing&&st.vis);}
 });
});
if("IntersectionObserver" in window&&!shot){
 var dio=new IntersectionObserver(function(es){es.forEach(function(e){demos.forEach(function(st){if(st.el!==e.target)return;
  st.vis=e.isIntersecting;if(!st.ready)return;
  if(st.vis&&st.playing)st.send({cmd:"visible"});else if(!st.vis)st.send({cmd:"hidden"});});});},{threshold:.35});
 demos.forEach(function(st){dio.observe(st.el);});
}

/* pricing toggle */
document.querySelectorAll(".tog button").forEach(function(b){b.addEventListener("click",function(){
 var k=b.dataset.b;document.querySelectorAll(".tog button").forEach(function(x){x.classList.toggle("on",x===b);x.setAttribute("aria-pressed",x===b?"true":"false");});
 document.querySelectorAll(".price[data-y]").forEach(function(p){p.firstChild.nodeValue=p.dataset[k];p.classList.remove("flip");void p.offsetWidth;if(!reduce)p.classList.add("flip");});
 document.querySelectorAll(".billed[data-y]").forEach(function(p){p.textContent=p.dataset[k];});
});});
})();
