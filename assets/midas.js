/* Midas shared components and tracking.
   Load at the end of <body>: <script src="/assets/midas.js"></script> (relative paths are fine too).
   Components:  <time-compare before="…" after="…">   <four-roles variant="default|retail">   <pilot-offer [compact] [href]>
   Tracking:    window.midasTrack(event, props) pushes to window.dataLayer. No analytics script is loaded here;
                add the owner's tag (e.g. Google Tag Manager) and these events flow into it.
                Declarative: data-track="cta_book_demo" data-loc="hero" on any link or button.
   Pilot intent: links with data-intent="pilot" set the hidden <input name="intent"> on the demo form. */
(function () {
  if (window.__midasComponents) return;
  window.__midasComponents = true;

  /* ---------- tracking ---------- */
  window.dataLayer = window.dataLayer || [];
  function track(ev, props) {
    var o = { event: ev };
    if (props) for (var k in props) o[k] = props[k];
    window.dataLayer.push(o);
  }
  window.midasTrack = track;
  document.addEventListener('click', function (e) {
    var t = e.target.closest && e.target.closest('[data-track],[data-intent]');
    if (!t) return;
    if (t.dataset.track) track(t.dataset.track, { location: t.dataset.loc || '' });
    if (t.dataset.intent === 'pilot') track('cta_start_pilot', { location: t.dataset.loc || '' });
  });
  document.addEventListener('play', function (e) {
    if (e.target.closest && e.target.closest('[data-track-play]')) track(e.target.closest('[data-track-play]').dataset.trackPlay);
  }, true);
  function onReady(fn) { if (document.readyState !== 'loading') fn(); else document.addEventListener('DOMContentLoaded', fn); }
  onReady(function () { if (document.body.dataset.pageview) track(document.body.dataset.pageview, { path: location.pathname }); });

  /* ---------- pilot intent on the demo form ---------- */
  function setIntent(v) {
    document.querySelectorAll('form input[name="intent"]').forEach(function (i) { i.value = v; });
    var h = document.getElementById('demoTitle');
    if (h && v === 'pilot' && h.dataset.pilot) h.innerHTML = h.dataset.pilot;
  }
  onReady(function () {
    try { var q = new URLSearchParams(location.search).get('intent'); if (q) setIntent(q); } catch (e) {}
  });
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[data-intent]');
    if (!a) return;
    var demo = document.getElementById('demo');
    var url = new URL(a.href, location.href);
    if (!demo || url.pathname !== location.pathname) return; /* other page: normal navigation, ?intent is read on load */
    e.preventDefault();
    setIntent(a.dataset.intent);
    try { history.replaceState(null, '', '?intent=' + encodeURIComponent(a.dataset.intent) + '#demo'); } catch (err) {}
    demo.scrollIntoView({ behavior: 'smooth' });
    var f = demo.querySelector('input:not([type=hidden])'); if (f) setTimeout(function () { f.focus({ preventScroll: true }); }, 500);
  });

  /* ---------- styles ---------- */
  var css =
    '.todo{background:#FFF4C2;color:#6B4700;border:1px dashed #B88A00;border-radius:6px;padding:0 5px;font-weight:600;font-style:normal;white-space:normal}' +
    /* time-compare */
    'time-compare{display:inline-flex;align-items:center;flex-wrap:wrap;justify-content:center;gap:8px 12px;padding:8px 10px 8px 16px;border-radius:999px;' +
    'background:var(--glass,rgba(255,255,255,.6));-webkit-backdrop-filter:var(--gblur,blur(16px));backdrop-filter:var(--gblur,blur(16px));' +
    'border:1px solid var(--gedge,rgba(255,255,255,.75));box-shadow:var(--gshadow,0 10px 30px -18px rgba(120,78,18,.35));font:500 14px/1.3 "DM Sans",system-ui,sans-serif;color:var(--ink,#1C1915)}' +
    'time-compare .tc-k{font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--mute,#6B6359);margin-right:6px}' +
    'time-compare .tc-before{color:var(--mute,#6B6359)}time-compare .tc-before b{font-weight:600;color:var(--ink,#1C1915)}' +
    'time-compare .tc-arrow{color:var(--orange,#E07A10);font-weight:700}' +
    'time-compare .tc-after{background:var(--ink,#1C1915);color:#fff;border-radius:999px;padding:6px 14px}' +
    'time-compare .tc-after .tc-k{color:var(--gold2,#E8B638)}time-compare .tc-after b{font-weight:700}' +
    '@media(max-width:480px){time-compare{flex-direction:column;border-radius:20px;padding:12px 14px;gap:6px}time-compare .tc-arrow{transform:rotate(90deg)}}' +
    /* four-roles */
    'four-roles{display:block;text-align:left}' +
    '.fr-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:40px}' +
    '.fr-card{display:flex;flex-direction:column;gap:12px;border-radius:20px;padding:24px;background:var(--glass,rgba(255,255,255,.6));-webkit-backdrop-filter:var(--gblur,blur(16px));backdrop-filter:var(--gblur,blur(16px));border:1px solid var(--gedge,rgba(255,255,255,.75));box-shadow:var(--gshadow,0 10px 30px -18px rgba(120,78,18,.35))}' +
    '.fr-n{font:500 34px/1 "EB Garamond",Georgia,serif;color:var(--gold,#D9A21B)}' +
    '.fr-card h3{margin:0;font-size:18px;line-height:1.25}' +
    '.fr-card dl{margin:0;display:flex;flex-direction:column;gap:12px;flex:1}' +
    '.fr-card dt{font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--mute,#6B6359);margin-bottom:3px}' +
    '.fr-card dd{margin:0;font-size:14.5px;line-height:1.5}' +
    '.fr-card .fr-do dd{color:var(--mute,#6B6359)}' +
    '.fr-card .fr-mid{margin-top:auto;padding:12px 14px;border-radius:14px;background:rgba(224,122,16,.08);border:1px solid rgba(224,122,16,.2)}' +
    '.fr-card .fr-mid dt{color:var(--orange-ink,#A8520A)}' +
    '.fr-foot{margin:16px 0 0;font-size:13px;color:var(--mute,#6B6359);text-align:center}' +
    '.fr-foot a,.fr-bars a{color:var(--orange-ink,#A8520A);font-weight:600;text-decoration:underline;text-underline-offset:3px}' +
    '.fr-bars{max-width:760px;margin:36px auto 0;display:grid;grid-template-columns:120px 1fr;gap:12px 16px;align-items:center}' +
    '.fr-bars .lb{font-weight:600;font-size:15px}' +
    '.fr-bars .tr{display:flex;align-items:center;gap:12px;min-width:0}' +
    '.fr-bars .bar{height:30px;border-radius:999px;flex:none}' +
    '.fr-bars .b1{width:calc(100% - 150px);background:linear-gradient(90deg,#E9DCC6,#CDB99A)}' +
    '.fr-bars .b2{width:10px;background:linear-gradient(90deg,var(--gold,#D9A21B),var(--orange,#E07A10))}' +
    '.fr-bars .v{font-size:14px;font-weight:600;white-space:nowrap}.fr-bars .v small{display:block;font-weight:500;color:var(--mute,#6B6359)}' +
    '@media(max-width:980px){.fr-grid{grid-template-columns:1fr 1fr}}' +
    '@media(max-width:600px){.fr-grid{grid-template-columns:1fr}.fr-bars{grid-template-columns:1fr;gap:6px}.fr-bars .tr{margin-bottom:10px}.fr-bars .b1{width:calc(100% - 130px)}}' +
    /* pilot-offer */
    'pilot-offer{display:block;text-align:left}' +
    '.po{border-radius:24px;padding:32px;background:linear-gradient(160deg,rgba(255,255,255,.7) 35%,rgba(252,236,206,.5));-webkit-backdrop-filter:var(--gblur,blur(16px));backdrop-filter:var(--gblur,blur(16px));border:1px solid var(--gedge,rgba(255,255,255,.75));box-shadow:var(--gshadow,0 10px 30px -18px rgba(120,78,18,.35));display:grid;grid-template-columns:1.1fr 1fr;gap:28px;align-items:start}' +
    '.po h3{font:500 32px/1.1 "EB Garamond",Georgia,serif;margin:6px 0 10px}' +
    '.po p{margin:0;color:var(--mute,#6B6359)}' +
    '.po ul{list-style:none;margin:0;padding:0;font-size:15px}' +
    '.po li{padding:10px 0;border-top:1px solid var(--line,rgba(190,145,80,.2));display:grid;grid-template-columns:110px 1fr;gap:10px}' +
    '.po li:first-child{border-top:0;padding-top:0}.po li b{font-weight:600}' +
    '.po .po-cta{margin-top:20px}' +
    '.po-k{font-size:12px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--orange-ink,#A8520A)}' +
    'pilot-offer[compact] .po{display:block;padding:20px;border-radius:16px;box-shadow:none;margin-top:12px}' +
    'pilot-offer[compact] .po h3{font-size:22px;margin:0 0 6px}pilot-offer[compact] .po p{font-size:14.5px;margin-bottom:12px}' +
    'pilot-offer[compact] .po li{grid-template-columns:96px 1fr;font-size:14px;padding:7px 0}' +
    '@media(max-width:760px){.po{grid-template-columns:1fr;padding:24px}.po li{grid-template-columns:1fr;gap:2px}}';
  var st = document.createElement('style');
  st.textContent = css;
  document.head.appendChild(st);

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; });
  }
  function todo(s) { return '<span class="todo">{{TODO: ' + esc(s) + '}}</span>'; }

  /* ---------- <time-compare> ---------- */
  customElements.define('time-compare', class extends HTMLElement {
    static get observedAttributes() { return ['before', 'after', 'before-label', 'after-label']; }
    connectedCallback() { this.render(); }
    attributeChangedCallback() { if (this.isConnected) this.render(); }
    render() {
      var b = this.getAttribute('before') || '', a = this.getAttribute('after') || '';
      var bl = this.getAttribute('before-label') || 'Before', al = this.getAttribute('after-label') || 'Midas';
      this.setAttribute('role', 'img');
      this.setAttribute('aria-label', bl + ': ' + b + '. ' + al + ': ' + a + '.');
      this.innerHTML =
        '<span class="tc-before" aria-hidden="true"><span class="tc-k">' + esc(bl) + '</span><b>' + esc(b) + '</b></span>' +
        '<span class="tc-arrow" aria-hidden="true">→</span>' +
        '<span class="tc-after" aria-hidden="true"><span class="tc-k">' + esc(al) + '</span><b>' + esc(a) + '</b></span>';
    }
  });

  /* ---------- <four-roles> ---------- */
  var ROLES = {
    'default': [
      ['Chartered Accountant (CA)', 'Bank and ledger reconciliations, accruals, VAT workings, month-end close', '~3 days',
        'Reconciles and categorizes automatically, prepares the close and drafts VAT and corporate tax workings for review'],
      ['CFA-level analyst', 'Variance analysis, margins by store, SKU and channel, cash forecast', '~2 days',
        'Explains every variance, profit by store, SKU, channel or entity, and a rolling 13-week cash forecast'],
      ['IT / data person', 'Pulling exports from the ERP, POS and banks, fixing mappings, building spreadsheets', '~1.5 days',
        'Connects read-only to the ERP, POS, banks and e-commerce, and keeps one clean ledger'],
      ['CFO', 'Reviewing, writing commentary, the board pack, decisions', '~0.5 day',
        'Board pack with commentary, red flags and recommended actions, ready for sign-off']
    ],
    retail: [
      ['Chartered Accountant (CA)', 'Matching every store’s POS takings and card settlements to the bank, supplier statements, accruals, VAT in each country', '~3 days',
        'Matches POS, card and bank lines for every store, and drafts VAT and corporate tax workings per entity for review'],
      ['CFA-level analyst', 'Store league tables, margin by category, markdown and shrinkage analysis', '~2 days',
        'Ranks every store by margin, sales per sq ft and shrinkage, and explains what moved and why'],
      ['IT / data person', 'Exporting from several POS systems and the ERP, mapping store codes, rebuilding the group spreadsheet', '~1.5 days',
        'Connects read-only to the ERP, POS and banks, and maps every store and entity into one ledger'],
      ['CFO', 'Group consolidation review, board commentary, supplier and expansion decisions', '~0.5 day',
        'Group board pack with store highlights, red flags and recommended actions, ready for sign-off']
    ]
  };
  customElements.define('four-roles', class extends HTMLElement {
    connectedCallback() {
      if (this.dataset.done) return; this.dataset.done = '1';
      var rows = ROLES[this.getAttribute('variant')] || ROLES['default'];
      var bm = this.getAttribute('benchmark') || '/benchmark';
      var h = '<div class="fr-grid">';
      rows.forEach(function (r, i) {
        h += '<article class="fr-card"><div class="fr-n">0' + (i + 1) + '</div><h3>' + esc(r[0]) + '</h3><dl>' +
          '<div class="fr-do"><dt>What they usually do</dt><dd>' + esc(r[1]) + '</dd></div>' +
          '<div><dt>Typical time*</dt><dd>' + esc(r[2]) + '</dd></div>' +
          '<div class="fr-mid"><dt>What Midas does</dt><dd>' + esc(r[3]) + '</dd></div></dl></article>';
      });
      h += '</div><p class="fr-foot">*Typical times are our estimates for a multi-entity month-end and vary by business' +
        '. <a href="' + esc(bm) + '">See how we estimate it →</a></p>';
      if (!this.hasAttribute('no-bars')) {
        h += '<div class="fr-bars" role="img" aria-label="Typical team: about 7 working days. Midas: about 2 minutes, plus your review time.">' +
          '<span class="lb" aria-hidden="true">Typical team</span><span class="tr" aria-hidden="true"><span class="bar b1"></span><span class="v">~7 working days</span></span>' +
          '<span class="lb" aria-hidden="true">Midas</span><span class="tr" aria-hidden="true"><span class="bar b2"></span><span class="v">~2 minutes<small>+ your review time</small></span></span></div>';
      }
      this.innerHTML = h;
    }
  });

  /* ---------- <pilot-offer> ---------- */
  customElements.define('pilot-offer', class extends HTMLElement {
    connectedCallback() {
      if (this.dataset.done) return; this.dataset.done = '1';
      var href = this.getAttribute('href') || '/?intent=pilot#demo';
      var loc = this.getAttribute('loc') || '';
      var compact = this.hasAttribute('compact');
      var tag = compact ? 'h4' : 'h3';
      var intro = '<div>' + (compact ? '' : '<span class="po-k">Pilot</span>') +
        '<' + tag + ' class="po-t">Start with a 30-day pilot</' + tag + '>' +
        '<p>Pick one entity or a group of stores. We connect read-only, run Midas alongside your team and measure the time saved on your own close. If it doesn’t prove itself, you walk away.</p>' +
        (compact ? '' : '<p class="po-cta"><a class="btn btn-dark" href="' + esc(href) + '" data-intent="pilot" data-loc="' + esc(loc) + '">Discuss a pilot →</a></p>') + '</div>';
      var list = '<ul>' +
        '<li><b>Scope</b><span>One entity or a group of stores, agreed on the first call</span></li>' +
        '<li><b>Setup</b><span>~1 day, read-only</span></li>' +
        '<li><b>Deliverable</b><span>Side-by-side close + a time-saved report</span></li>' +
        '<li><b>Commercials</b><span>Agreed up front, before any work starts</span></li></ul>' +
        (compact && !this.hasAttribute('no-cta') ? '<p class="po-cta" style="margin-top:12px"><a class="btn btn-dark" href="' + esc(href) + '" data-intent="pilot" data-loc="' + esc(loc) + '">Discuss a pilot →</a></p>' : '');
      this.innerHTML = '<div class="po">' + intro + list + '</div>';
      var t = this.querySelector('.po-t'); if (compact && t) t.style.cssText = 'font:500 22px/1.15 "EB Garamond",Georgia,serif;margin:0 0 6px';
    }
  });
})();
