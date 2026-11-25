(function(){
const $$=(s,r=document)=>[...r.querySelectorAll(s)];
const mq=window.matchMedia('(max-width:860px)');
// tabs: phone = switcher, desktop = jump to the card
$$('.tab').forEach(t=>t.addEventListener('click',()=>{
  const k=t.dataset.k;$$('.tab').forEach(x=>x.classList.toggle('on',x===t));
  $$('.card').forEach(c=>c.classList.toggle('on',c.dataset.k===k));
  const card=document.getElementById('opt'+k);
  if(!mq.matches){card.scrollIntoView({behavior:'smooth',block:'start'});card.classList.add('flash');setTimeout(()=>card.classList.toggle('flash',false),900)}
  else window.scrollTo({top:0});
}));
function toast(ph,msg){const t=ph.querySelector('.toast');t.textContent=msg;t.classList.toggle('on',false);void t.offsetWidth;t.classList.add('on');clearTimeout(t._h);t._h=setTimeout(()=>t.classList.toggle('on',false),1800)}
function closeMenus(ph){$$('.menu',ph).forEach(m=>m.parentNode.removeChild(m));$$('.say.sel',ph).forEach(s=>s.classList.toggle('sel',false))}
function openEdit(ph,say){
  const host=say.closest('.d-p')||say;
  const open=host.nextElementSibling&&host.nextElementSibling.classList.contains('menu');
  closeMenus(ph);if(open)return;
  say.classList.add('sel');
  const m=document.createElement('div');m.className='menu';
  ['Shorter','Punchier','More like me','Redo'].forEach(l=>{const b=document.createElement('button');b.textContent=l;b.addEventListener('click',e=>{e.stopPropagation();toast(ph,l+': rewrites this line only (not simulated in this mock)')});m.appendChild(b)});
  host.after(m);
}
function lines(ph){return $$('.say',ph).filter(s=>!s.closest('.hsheet')).map(s=>s.textContent.replace(/[“”]/g,''))}
function setHook(ph,h){$$('.say.hk',ph).forEach(s=>{s.textContent=s.closest('.d-p')?h:'“'+h+'”'})}
$$('.phone').forEach(ph=>{
  const scr=ph.querySelector('.scr'),tpb=ph.querySelector('.tpb');
  // wheel anywhere over the phone scrolls whatever is open in it
  ph.addEventListener('wheel',e=>{
    const tgt=ph.classList.contains('tpon')?tpb:ph.classList.contains('hson')?ph.querySelector('.hs-in'):scr;
    tgt.scrollTop+=e.deltaY;e.preventDefault();
  },{passive:false});
  $$('.say',ph).forEach(s=>{const host=s.closest('.d-p');(host||s).addEventListener('click',()=>openEdit(ph,s))});
  $$('.pen.ed',ph).forEach(p=>p.addEventListener('click',()=>{const box=p.closest('.v-hook,.v-step,.v-cta');openEdit(ph,box.querySelector('.say'))}));
  const on=(sel,fn)=>$$(sel,ph).forEach(b=>b.addEventListener('click',fn));
  on('.save',()=>toast(ph,'Saved to your Library'));
  on('.share',()=>toast(ph,'Share link copied'));
  on('.copy',()=>toast(ph,'Script copied'));
  on('.rew',()=>toast(ph,'Rewrites the whole script (not simulated in this mock)'));
  // practice full screen
  let raf=null,paused=false;
  function run(){if(!paused)tpb.scrollTop+=0.6;raf=requestAnimationFrame(run)}
  on('.prac',()=>{const ts=ph.querySelector('.toast');clearTimeout(ts._h);ts.classList.toggle('on',false);closeMenus(ph);tpb.innerHTML=lines(ph).map(l=>'<p>'+l.replace(/</g,'&lt;')+'</p>').join('');tpb.scrollTop=0;paused=false;ph.querySelector('.tp-pp').textContent='Pause';ph.classList.add('tpon');cancelAnimationFrame(raf);if(!matchMedia('(prefers-reduced-motion:reduce)').matches)raf=requestAnimationFrame(run)});
  on('.tp-pp',()=>{paused=!paused;ph.querySelector('.tp-pp').textContent=paused?'Play':'Pause'});
  on('.tp-x',()=>{ph.classList.toggle('tpon',false);cancelAnimationFrame(raf)});
  // option 3: pick a hook, 3 new hooks
  const sets=[HOOKS,MORE];let si=0;
  function wireHooks(){$$('.s-hk',ph).forEach(h=>h.addEventListener('click',()=>{$$('.s-hk',ph).forEach(x=>x.classList.toggle('on',x===h));setHook(ph,h.querySelector('.hkt').textContent)}))}
  wireHooks();
  on('.s-more',()=>{si=(si+1)%sets.length;const box=ph.querySelector('.s-hks');box.innerHTML=sets[si].map((h,i)=>'<div class="s-hk'+(i===0?' on':'')+'" tabindex="0"><span class="dot"></span><span class="hkt">'+h+'</span></div>').join('');box.classList.toggle('swap',false);void box.offsetWidth;box.classList.add('swap');wireHooks();setHook(ph,sets[si][0])});
  // option 4: hooks sheet
  on('.hooks',()=>{const cur=(ph.querySelector('.say.hk')||{}).textContent;$$('.d-opt',ph).forEach(o=>o.classList.toggle('on',o.dataset.h===cur));ph.classList.add('hson')});
  on('.hs-x',()=>ph.classList.toggle('hson',false));
  on('.hsheet',e=>{if(e.target.classList.contains('hsheet'))ph.classList.toggle('hson',false)});
  $$('.d-opt',ph).forEach(o=>o.addEventListener('click',()=>{setHook(ph,o.dataset.h);ph.classList.toggle('hson',false);toast(ph,'Hook updated')}));
});
})();
