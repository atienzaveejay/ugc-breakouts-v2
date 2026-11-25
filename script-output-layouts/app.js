(function(){
const $$=(s,r=document)=>[...r.querySelectorAll(s)];
$$('.col').forEach(col=>{
  const ph=col.querySelector('.phone'),scr=ph.querySelector('.scr'),toast=ph.querySelector('.toast');
  const say=m=>{toast.textContent=m;toast.classList.add('on');clearTimeout(toast._t);toast._t=setTimeout(()=>toast.classList.remove('on'),1600)};
  $$('.sw',col).forEach(b=>b.addEventListener('click',()=>{
    $$('.sw',col).forEach(x=>x.classList.toggle('on',x===b));
    $$('.v',ph).forEach(v=>v.classList.toggle('on',v.dataset.v===b.dataset.v));
    scr.scrollTop=0;
  }));
  ph.addEventListener('click',e=>{
    const b=e.target.closest('button');if(!b)return;
    if(b.classList.contains('sc-ed'))say(b.closest('.sc-hookc')?'Opens Change the hook (as live)':'Opens Refine this part (as live)');
    else if(b.classList.contains('sc-prac-btn'))say('Practice full screen (as live)');
    else if(b.classList.contains('sw'))return;
    else say((b.textContent||'').trim()+' (mock)');
  });
});
})();
