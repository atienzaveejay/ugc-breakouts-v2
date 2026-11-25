(function(){
const $$=(s,r=document)=>[...r.querySelectorAll(s)];
const mq=window.matchMedia('(max-width:860px)');
$$('.tab').forEach(t=>t.addEventListener('click',()=>{
  const k=t.dataset.k;$$('.tab').forEach(x=>x.classList.toggle('on',x===t));
  $$('.card').forEach(c=>c.classList.toggle('on',c.dataset.k===k));
  const card=document.getElementById('l-'+k);
  if(!mq.matches){card.scrollIntoView({behavior:'smooth',block:'start'});card.classList.add('flash');setTimeout(()=>card.classList.remove('flash'),900)}
}));
function toast(ph,msg){const t=ph.querySelector('.toast');t.textContent=msg;t.classList.remove('on');void t.offsetWidth;t.classList.add('on');clearTimeout(t._h);t._h=setTimeout(()=>t.classList.remove('on'),1800)}
function closeMenus(ph){$$('.menu',ph).forEach(m=>m.remove());$$('.say.sel',ph).forEach(s=>s.classList.remove('sel'))}
$$('.card').forEach(card=>{
  const ph=card.querySelector('.phone'),scr=ph.querySelector('.scr'),tpb=ph.querySelector('.tpb');
  const cur=()=>ph.querySelector('.pad.v.on');
  $$('.sw',card).forEach(b=>b.addEventListener('click',()=>{
    $$('.sw',card).forEach(x=>x.classList.toggle('on',x===b));
    $$('.pad.v',ph).forEach(p=>p.classList.toggle('on',p.dataset.v===b.dataset.v));
    closeMenus(ph);scr.scrollTop=0;
  }));
  ph.addEventListener('wheel',e=>{const tgt=ph.classList.contains('tpon')?tpb:scr;tgt.scrollTop+=e.deltaY;e.preventDefault()},{passive:false});
  $$('.say',ph).forEach(s=>s.addEventListener('click',()=>{
    const open=s.nextElementSibling&&s.nextElementSibling.classList.contains('menu');
    closeMenus(ph);if(open)return;s.classList.add('sel');
    const m=document.createElement('div');m.className='menu';
    ['Shorter','Punchier','More like me','Redo'].forEach(l=>{const b=document.createElement('button');b.textContent=l;b.addEventListener('click',e=>{e.stopPropagation();toast(ph,l+': rewrites this line only (not simulated)')});m.appendChild(b)});
    s.after(m);
  }));
  $$('.jump a',ph).forEach((a,i)=>a.addEventListener('click',()=>{const p=$$('.l-sec.part',cur())[i];if(p)scr.scrollTo({top:p.offsetTop-12,behavior:'smooth'})}));
  const on=(sel,fn)=>$$(sel,ph).forEach(b=>b.addEventListener('click',fn));
  on('.save',()=>toast(ph,'Saved to your Library'));
  on('.share',()=>toast(ph,'Share link copied'));
  on('.copy',()=>toast(ph,'Script copied'));
  on('.copytext',()=>toast(ph,'Text copied, ready for CapCut or TikTok'));
  let raf=null,paused=false;
  function run(){if(!paused)tpb.scrollTop+=0.6;raf=requestAnimationFrame(run)}
  on('.prac',()=>{closeMenus(ph);
    const ls=$$('.l-say',cur()).map(s=>{const w=s.closest('.sk-l');const who=w?w.querySelector('.who').textContent:'';return (who?'<small>'+who+'</small>':'')+s.textContent.replace(/[“”]/g,'').replace(/</g,'&lt;')});
    tpb.innerHTML=ls.map(l=>'<p>'+l+'</p>').join('');tpb.scrollTop=0;paused=false;ph.querySelector('.tp-pp').textContent='Pause';ph.classList.add('tpon');cancelAnimationFrame(raf);
    if(!matchMedia('(prefers-reduced-motion:reduce)').matches)raf=requestAnimationFrame(run)});
  on('.tp-pp',()=>{paused=!paused;ph.querySelector('.tp-pp').textContent=paused?'Play':'Pause'});
  on('.tp-x',()=>{ph.classList.remove('tpon');cancelAnimationFrame(raf)});
});
})();
