(function(){
  var WA = window.EZ_WA || '2348058963692';
  var naira = function(n){ return '₦' + Math.round(n).toLocaleString('en-NG'); };
  var short = function(n){ return n >= 1e6 ? '₦' + (n/1e6).toFixed(n % 1e6 ? 1 : 0) + 'm' : '₦' + Math.round(n/1000) + 'k'; };
  var $ = function(s){ return document.querySelector(s); }, $$ = function(s){ return document.querySelectorAll(s); };

  var hd = $('header');
  if (hd) addEventListener('scroll', function(){ hd.classList.toggle('scrolled', scrollY > 8); }, {passive:true});

  var mb = $('.menu-btn'), dr = $('#drawer');
  if (mb && dr) {
    mb.addEventListener('click', function(){ var o = dr.classList.toggle('open'); mb.setAttribute('aria-expanded', o); document.body.style.overflow = o ? 'hidden' : ''; });
    dr.querySelectorAll('a').forEach(function(a){ a.addEventListener('click', function(){ dr.classList.remove('open'); document.body.style.overflow=''; }); });
  }

  var io = 'IntersectionObserver' in window ? new IntersectionObserver(function(es){
    es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
  }, {rootMargin:'0px 0px -6% 0px'}) : null;
  $$('.rv').forEach(function(el){ io ? io.observe(el) : el.classList.add('in'); });

  // product tabs
  $$('[data-tabs]').forEach(function(box){
    var btns = box.querySelectorAll('[data-tab]'), panes = box.querySelectorAll('[data-pane]');
    btns.forEach(function(b){ b.addEventListener('click', function(){
      btns.forEach(function(x){ x.classList.toggle('on', x === b); });
      panes.forEach(function(p){ p.classList.toggle('on', p.dataset.pane === b.dataset.tab); });
    }); });
  });

  // calculator
  var amt = $('#amt'), mo = $('#mo');
  if (amt && mo) {
    var R = 0.025, take = 300000;
    var fill = function(el){ el.style.setProperty('--p', ((el.value - el.min) / (el.max - el.min) * 100) + '%'); };
    var calc = function(){
      var P = +amt.value, n = +mo.value, m = P * R / (1 - Math.pow(1 + R, -n));
      $('#amtO').textContent = naira(P); $('#moO').textContent = n + ' months';
      $('#mon').textContent = naira(m); $('#rRec').textContent = naira(P); $('#rTot').textContent = naira(m * n);
      var share = m / take, f = $('#fit');
      if (share <= 1/3) { f.className = 'fit'; f.textContent = 'This fits a ' + short(take) + ' take-home. You keep ' + Math.round((1 - share) * 100) + '% of your salary.'; }
      else { var maxP = (take / 3) * (1 - Math.pow(1 + R, -n)) / R; f.className = 'fit bad'; f.textContent = 'A bit high for a ' + short(take) + ' take-home. Try about ' + naira(Math.floor(maxP / 50000) * 50000) + ' over ' + n + ' months, or a longer term.'; }
      fill(amt); fill(mo);
    };
    amt.addEventListener('input', calc); mo.addEventListener('input', calc);
    $$('#payb button').forEach(function(b){ b.addEventListener('click', function(){
      $$('#payb button').forEach(function(x){ x.classList.remove('on'); }); b.classList.add('on'); take = +b.dataset.v; calc(); }); });
    calc();
  }

  var wa = function(text){ return 'https://wa.me/' + WA + '?text=' + encodeURIComponent(text); };
  $$('[data-wa]').forEach(function(a){ a.href = wa(a.dataset.msg || 'Hi ezee, I have a question.'); a.target = '_blank'; a.rel = 'noopener'; });

  var form = $('#wlf');
  if (form) form.addEventListener('submit', function(e){
    e.preventDefault();
    var d = new FormData(form), bad = null;
    ['name','phone','work','pay'].forEach(function(k){ var el = form.elements[k]; var v = (d.get(k) || '').trim(); el.style.borderColor = v ? '' : '#9A2C10'; if(!v && !bad) bad = el; });
    if ((d.get('phone') || '').replace(/\D/g,'').length < 10) { form.elements.phone.style.borderColor = '#9A2C10'; bad = bad || form.elements.phone; }
    if (!form.elements.ok.checked) { bad = bad || form.elements.ok; form.elements.ok.parentNode.style.color = '#9A2C10'; }
    if (bad) { bad.focus(); return; }
    window.open(wa('Hi ezee, please add me to the waitlist.\n\nName: ' + d.get('name') + '\nWhatsApp: ' + d.get('phone') + '\nWork: ' + d.get('work') + '\nTake-home: ' + d.get('pay') + '\nInterested in: ' + d.get('want')), '_blank', 'noopener');
    $('#ok').style.display = 'block';
  });
})();
