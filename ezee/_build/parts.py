"""Product showcase, business suite and rewards blocks for the ezee site."""

def scr(inner):
    return f'<div class="ph"><div class="sc">{inner}</div></div>'

T = [
 ('wallet', '👛 ezee wallet', 'your money, one tap away.',
  'A free account with its own account number. Send to any bank, receive instantly, buy airtime and data and pay every bill in seconds.',
  ['Free transfers to any bank', 'Airtime, data, electricity and TV', 'Your own account number in minutes'],
  """<div class="bar"><span><b style="font:800 17px var(--display)">ezee</b></span><span>9:41</span></div><div class="hi">Hi Amaka 👋🏾</div>
<div class="bal"><small>ezee wallet · 01 234 5678</small><div class="n">₦184,920.50</div><div class="qa"><div><i>➜</i>Send</div><div><i>＋</i>Add</div><div><i>📱</i>Airtime</div><div><i>💡</i>Bills</div></div></div>
<div class="tx"><div><span><i>🏦</i><span>To Chidi O.<small>Transfer · Free</small></span></span><b>−₦25,000</b></div>
<div><span><i>⚡</i><span>Electricity<small>Prepaid token sent</small></span></span><b>−₦15,000</b></div>
<div><span><i>📶</i><span>Data 20GB<small>Instant</small></span></span><b>−₦6,000</b></div>
<div><span><i>💼</i><span>Salary<small>25 Nov</small></span></span><b style="color:var(--green)">+₦520,000</b></div></div>"""),
 ('pay', '⚡ ezee pay', 'one tap. everywhere.',
  'Tap your phone or card on the bus, at the shop and in the market. Scan a QR. No change, no wahala, every naira recorded.',
  ['Tap to pay on transport and in shops', 'QR payments at any merchant', 'Rewards on every ride'],
  """<div class="bar"><span>ezee pay</span><span>9:41</span></div><div class="hi">Ready to tap</div>
<div style="flex:1;display:grid;place-items:center"><div style="width:160px;height:160px;border-radius:50%;background:var(--yellow);display:grid;place-items:center;box-shadow:0 0 0 16px #FFF3CC,0 0 0 32px #FFF9E6"><svg viewBox="0 0 24 24" width="66" height="66" fill="none" stroke="#0E0E0C" stroke-width="2.2" stroke-linecap="round"><path d="M8.5 8.5a5 5 0 0 1 0 7M12 6a8.5 8.5 0 0 1 0 12M15.5 3.5a12 12 0 0 1 0 17"/></svg></div></div>
<div class="row2"><span>🚌 Bus fare</span><b>₦500</b></div><div class="row2"><span>🎁 Ride streak</span><b>9 of 10, next ride free</b></div>
<div class="tap" style="justify-content:center">Hold near the reader</div>"""),
 ('save', '🐷 ezee save', 'put a little aside, every payday.',
  'Automatic savings from your salary, goals for school fees and rent, and a balance you can watch grow.',
  ['Auto-save a share of every salary', 'Goals for fees, rent and emergencies', 'Withdraw when you need it'],
  """<div class="bar"><span>ezee save</span><span>9:41</span></div><div class="hi">Your goals</div>
<div class="bal"><small>Total saved</small><div class="n">₦642,000</div><small>Auto-saving 10% of every salary</small></div>
<div style="display:grid;gap:12px;margin-top:4px">
<div><div class="row2" style="border:0;padding:0 0 6px"><span>🎓 School fees</span><b>₦380k of ₦450k</b></div><div class="goal-bar"><i style="width:84%"></i></div></div>
<div><div class="row2" style="border:0;padding:0 0 6px"><span>🏠 Rent</span><b>₦210k of ₦900k</b></div><div class="goal-bar"><i style="width:23%"></i></div></div>
<div><div class="row2" style="border:0;padding:0 0 6px"><span>🛟 Emergency fund</span><b>₦52k of ₦200k</b></div><div class="goal-bar"><i style="width:26%"></i></div></div></div>
<span class="pill" style="margin-top:auto">✓ Next auto-save on payday</span>"""),
 ('card', '💳 ezee card', 'spend at home and abroad.',
  'A card for shops, ATMs and online, including international sites. Freeze it, set limits and see every payment in one tap.',
  ['Works in shops, ATMs and online', 'International online payments', 'Freeze and set limits in the app'],
  """<div class="bar"><span>ezee card</span><span>9:41</span></div>
<div class="cardv"><div class="chip2"></div><span>•••• •••• •••• 4821</span><b>ezee</b></div>
<div class="row2"><span>Online payments abroad</span><span class="tog"></span></div><div class="row2"><span>ATM withdrawals</span><span class="tog"></span></div><div class="row2"><span>Freeze card</span><span class="tog off"></span></div>
<div class="tx"><div><span><i>🎬</i><span>Streaming<small>Online · USD</small></span></span><b>−₦9,800</b></div><div><span><i>🛒</i><span>Supermarket<small>Card</small></span></span><b>−₦31,450</b></div></div>"""),
 ('credit', '💸 ezee credit', 'fair credit, repaid on payday.',
  'Salary-backed credit for school fees, rent, health and life. A decision in minutes, one clear monthly amount and never a call to your contacts.',
  ['Up to ₦5m, up to 24 months', 'Repaid from salary automatically', 'Every charge shown before you accept'],
  """<div class="bar"><span>ezee credit</span><span>9:41</span></div><div class="hi">Your offer is ready</div>
<div class="bal"><small>Salary-backed credit</small><div class="n">₦850,000</div><div class="s-row"><span>Monthly</span><span>₦47,530</span></div><div class="s-row"><span>Months</span><span>24</span></div><div class="s-row"><span>From salary on</span><span>25th</span></div><div class="s-row"><span>Hidden fees</span><span>₦0</span></div></div>
<span class="pill">✓ Fits your pay. You keep 86%</span><span class="pill" style="background:#FFF6D6;color:#5C4A0B">🔒 We never contact your contacts</span>
<div class="tap" style="background:var(--ink);color:#fff;justify-content:center;margin-top:auto">Accept and get paid</div>"""),
 ('auto', '🚗 ezee auto', 'drive now, pay monthly.',
  "New cars from Nigeria's leading dealers, financed by partner banks through Midas. Apply in three minutes and drive in 48 hours.",
  ['Apply in 3 minutes', 'Partner banks compete to finance you', 'New cars with manufacturer warranty'],
  """<div class="shot-img"><img src="img/midas-app.jpg" alt="The Midas car finance app" loading="lazy"></div>"""),
]

def showcase():
    tabs = ''.join(f'<button type="button" data-tab="{t[0]}"{" class=on" if i == 0 else ""}>{t[1]}</button>' for i, t in enumerate(T))
    panes = ''
    for i, (k, n, h, p, lst, inner) in enumerate(T):
        li = ''.join(f'<li>{x}</li>' for x in lst)
        if k == 'auto':
            cta = '<a href="https://gomidas.co/" class="btn btn-y" rel="noopener">Browse cars on Midas</a>'
        elif k == 'credit':
            cta = '<a href="credit.html" class="btn btn-y">See ezee credit</a>'
        else:
            cta = '<a href="index.html#waitlist" class="btn btn-y">Get early access</a>'
        panes += (f'<div class="pane{" on" if i == 0 else ""}" data-pane="{k}"><div><h3>{h}</h3><p class="lead">{p}</p>'
                  f'<ul class="list">{li}</ul>{cta}</div><div class="stage">{scr(inner)}</div></div>')
    return (f'<div class="show" data-tabs><div class="tabs" role="tablist">{tabs}</div>{panes}'
            '<p style="margin-top:18px;font-size:12.5px;color:var(--muted)">App screens are illustrations. The ezee auto screen is the live Midas site, gomidas.co.</p></div>')

def suite(light=False):
    c = ' lt' if light else ''
    return f"""<div class="suite">
<div class="su{c} rv" id="accept"><div class="nm">ezee <i>business</i></div><p>Accept every kind of payment and see your money land instantly.</p><ul><li>Tap, QR, transfer and card on your phone or an ezee POS</li><li>Instant settlement</li><li>Payment links and invoices</li><li>Every branch and staff member on one dashboard</li></ul><a href="pay.html#merchants">Accept payments →</a></div>
<div class="su{c} rv"><div class="nm">ezee <i>finance</i></div><p>Capital based on what you actually sell.</p><ul><li>Working capital repaid from daily sales</li><li>Invoice finance on big clients</li><li>Asset and fleet finance</li><li>Trade finance for imports</li></ul><a href="business.html#credit">Get capital →</a></div>
<div class="su{c} rv" id="spend"><div class="nm">ezee <i>spend</i></div><p>Company money, under control.</p><ul><li>Cards for every team member, with limits</li><li>Bulk supplier and vendor payments</li><li>Receipts captured, expenses approved in the app</li><li>Real-time spend by team and branch</li></ul><a href="business.html#spend">Control spend →</a></div>
<div class="su{c} rv"><div class="nm">ezee <i>payroll</i></div><p>Pay your people and look after them.</p><ul><li>Run payroll to any bank in one click</li><li>PAYE and pension schedules ready to file</li><li>Fair staff credit at no cost to you</li><li>Salary advances before payday</li></ul><a href="employers.html">For employers →</a></div>
</div>"""

REWARDS = """<section style="background:var(--yellow)">
  <div class="wrap">
    <p class="eyebrow rv" style="color:#5C4A0B">ezee rewards</p>
    <h2 class="rv">money that gives back.</h2>
    <p class="lead rv" style="margin-top:16px;color:#3D3208">Every tap, top-up and on-time repayment earns you something. The best apps in Nigeria are the ones people love opening.</p>
    <div class="rw">
      <div class="rv"><b>11th</b><span>ride on us</span><p>Tap to ride ten times and the next one is free.</p></div>
      <div class="rv"><b>₦1,000</b><span>for every friend</span><p>When a friend you invite joins and makes their first payment.</p></div>
      <div class="rv"><b>Cashback</b><span>on airtime and bills</span><p>A little back on the things you pay every month.</p></div>
      <div class="rv"><b>Better rates</b><span>for paying on time</span><p>Repay on time and your next ezee credit costs less.</p></div>
    </div>
    <p class="rv" style="margin-top:16px;font-size:13px;color:#5C4A0B">Planned rewards. Full terms will be published at launch.</p>
  </div>
</section>"""
