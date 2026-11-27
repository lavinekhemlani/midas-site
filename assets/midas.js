/* Midas shared components. Load with <script src="/assets/midas.js" defer></script>.
   Styles use the page's design tokens when present, with fallbacks so any page can use them. */
(function () {
  if (window.__midasComponents) return;
  window.__midasComponents = true;

  var css =
    /* {{TODO: …}} placeholders: impossible to miss in review */
    '.todo{background:#FFF4C2;color:#7A5200;border:1px dashed #C99A00;border-radius:6px;padding:0 5px;font-weight:600;font-style:normal;white-space:normal}' +
    /* <time-compare before="…" after="…"> */
    'time-compare{display:inline-flex;align-items:center;flex-wrap:wrap;justify-content:center;gap:8px 12px;padding:8px 10px 8px 16px;border-radius:999px;' +
    'background:var(--glass,rgba(255,255,255,.6));-webkit-backdrop-filter:var(--gblur,blur(16px));backdrop-filter:var(--gblur,blur(16px));' +
    'border:1px solid var(--gedge,rgba(255,255,255,.75));box-shadow:var(--gshadow,0 10px 30px -18px rgba(120,78,18,.35));font:500 14px/1.3 "DM Sans",system-ui,sans-serif;color:var(--ink,#1C1915)}' +
    'time-compare .tc-k{font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--mute,#6B6359);margin-right:6px}' +
    'time-compare .tc-before{color:var(--mute,#6B6359)}' +
    'time-compare .tc-before b{font-weight:600;color:var(--ink,#1C1915)}' +
    'time-compare .tc-arrow{color:var(--orange,#E07A10);font-weight:700}' +
    'time-compare .tc-after{background:var(--ink,#1C1915);color:#fff;border-radius:999px;padding:6px 14px}' +
    'time-compare .tc-after .tc-k{color:var(--gold2,#E8B638)}' +
    'time-compare .tc-after b{font-weight:700}' +
    '@media(max-width:480px){time-compare{flex-direction:column;border-radius:20px;padding:12px 14px;gap:6px}time-compare .tc-arrow{transform:rotate(90deg)}}';
  var st = document.createElement('style');
  st.textContent = css;
  document.head.appendChild(st);

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  /* <time-compare before="4 people · ~7 working days" after="~2 minutes"
                   before-label="Before" after-label="Midas"> */
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
})();
