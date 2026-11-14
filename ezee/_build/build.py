#!/usr/bin/env python3
"""Builds the ezee site into ../ (midascfo.com/ezee). Run: python3 build.py"""
import os, re, html, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parts import showcase, suite, REWARDS
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
WA = '2348058963692'

def mark(bg='#FFC72C', fg='#0E0E0C', size=None):
    s = f' width="{size}" height="{size}"' if size else ''
    return (f'<svg viewBox="0 0 64 64"{s} aria-hidden="true"><rect width="64" height="64" rx="18" fill="{bg}"/>'
            f'<path d="M47 32A15 15 0 1 0 43.4 41.7" fill="none" stroke="{fg}" stroke-width="7.5" stroke-linecap="round"/>'
            f'<path d="M17.5 32H52" stroke="{fg}" stroke-width="7.5" stroke-linecap="round"/>'
            f'<path d="M46 25.5L52.5 32L46 38.5" fill="none" stroke="{fg}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></svg>')

def wordmark(text='#0E0E0C', bg='#FFC72C', fg='#0E0E0C'):
    return (f'<svg viewBox="0 0 200 64" role="img" aria-label="ezee"><g>{mark(bg, fg)[mark(bg,fg).index(">")+1:-6]}</g>'
            f'<text x="76" y="47" font-family="Bricolage Grotesque, Arial Black, sans-serif" font-weight="800" font-size="52" letter-spacing="-2" fill="{text}">ezee</text></svg>')

FAV = 'data:image/svg+xml,' + mark().replace('"', "'").replace('#', '%23').replace('<', '%3C').replace('>', '%3E')

NAV = [('pay.html', 'Personal'), ('credit.html', 'ezee credit'), ('business.html', 'Business'), ('employers.html', 'Employers'),
       ('government.html', 'Government'), ('about.html', 'About'), ('blog.html', 'Blog')]

ICON = {
 'tap': '<svg viewBox="0 0 24 24" fill="none" stroke="#FFC72C" stroke-width="2.2" stroke-linecap="round"><path d="M8.5 8.5a5 5 0 0 1 0 7M12 6a8.5 8.5 0 0 1 0 12M15.5 3.5a12 12 0 0 1 0 17"/></svg>',
 'shield': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 3l8 3v6c0 4.5-3.4 8.2-8 9-4.6-.8-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/></svg>',
 'arrow': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 'apple': '<svg viewBox="0 0 24 24"><path d="M16.4 12.6c0-2.6 2.1-3.8 2.2-3.9-1.2-1.8-3.1-2-3.7-2-1.6-.2-3.1.9-3.9.9-.8 0-2-.9-3.4-.9-1.7 0-3.3 1-4.2 2.6-1.8 3.1-.5 7.7 1.3 10.2.9 1.2 1.9 2.6 3.2 2.6 1.3-.1 1.8-.8 3.3-.8s2 .8 3.4.8 2.2-1.3 3.1-2.5c1-1.4 1.4-2.8 1.4-2.9-.1 0-2.7-1-2.7-4.1zM13.9 5c.7-.9 1.2-2 1-3.2-1 0-2.3.7-3 1.6-.7.8-1.2 2-1.1 3.1 1.2.1 2.3-.6 3.1-1.5z"/></svg>',
 'play': '<svg viewBox="0 0 24 24"><path d="M4 2.6v18.8c0 .5.5.8.9.6l10.6-10.1L5 1.9c-.5-.2-1 .2-1 .7zm12.4 7.4L6.6 1.3l11.4 6.6-1.6 2.1zm0 4L18 16l-11.4 6.7 9.8-8.7zm4.1-3l-2.7-1.6-1.9 2.5 1.9 2.6 2.7-1.6c.8-.5.8-1.4 0-1.9z"/></svg>',
}

LEGAL = ('<p><b>ezee is a technology company, not a bank.</b> ezee loans are provided by <b>Sage Grey Finance Limited</b>, '
         'which is licensed and regulated by the Central Bank of Nigeria and integrated into the Nigerian Inter-Bank Settlement System (NIBSS). '
         'ezee pay, cards and savings are not yet live; when they launch they will be provided through licensed partners, named here. '
         'All loans are subject to eligibility, a credit check and affordability. Rates, amounts and screens shown on this site are examples. '
         'Targets and market figures are goals or third-party estimates, not ezee results.</p>'
         '<p><b>Privacy.</b> If you join the waitlist we use your name, WhatsApp number and the answers you choose only to contact you about ezee, '
         'in line with the Nigeria Data Protection Act 2023. We do not sell your data. To be removed, message us on WhatsApp.</p>'
         '<p>Photos from Wikimedia Commons under CC BY-SA 4.0: Omoeko Media (danfo buses, Ijora Badia), Agbebiyi Adekunle / Tadek Photography (Oshodi market), '
         'Olatunbosun Success (Mile 12 BRT), Jamie Tubers (Lagos Island). App screens are illustrations.</p><p>© 2026 ezee. Made in Lagos.</p>')

def head(title, desc):
    return f'''<!doctype html>
<html lang="en-NG" class="js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#0E0E0C">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="https://gomidas.co/ezee/img/danfo.jpg">
<link rel="icon" href="{FAV}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/ezee.css?v=2">
</head>
<body>'''

def header(active, dark):
    links = ''.join(f'<a href="{h}"{" class=on" if h == active else ""}>{t}</a>' for h, t in NAV)
    dl = ''.join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    wm = wordmark('#FFFFFF') if dark else wordmark()
    return f'''<header id="top"{' class="dk"' if dark else ''}>
  <div class="wrap nav">
    <a href="./" class="logo" aria-label="ezee home">{wm}</a>
    <nav class="links" aria-label="Main">{links}</nav>
    <div class="nav-r"><a href="index.html#waitlist" class="btn {'btn-y' if dark else 'btn-k'} hide-m">Get the app</a>
    <button class="menu-btn" aria-label="Menu" aria-expanded="false"><span></span></button></div>
  </div>
</header>
<div class="drawer" id="drawer">{dl}<a href="index.html#waitlist" class="btn btn-y">Get early access</a></div>'''

def footer():
    return f'''<footer>
  <div class="wrap">
    <div class="fgrid">
      <div><a href="./" class="logo">{wordmark()}</a>
        <p style="color:var(--muted);margin-top:14px;max-width:32ch;font-size:15.5px">Payments, loans and banking for every Nigerian. Built in Lagos, for the whole of Nigeria.</p>
        <div class="stores" style="margin-top:18px">{store('apple')}{store('play')}</div></div>
      <div><h4>Products</h4><ul><li><a href="pay.html">ezee pay</a></li><li><a href="pay.html#merchants">ezee for merchants</a></li><li><a href="credit.html">Personal loans</a></li><li><a href="business.html">Business loans</a></li><li><a href="https://gomidas.co/">Car finance</a></li></ul></div>
      <div><h4>Company</h4><ul><li><a href="about.html">About us</a></li><li><a href="why-ezee.html">Why "ezee"</a></li><li><a href="government.html">Government partners</a></li><li><a href="blog.html">Blog</a></li></ul></div>
      <div><h4>Talk to us</h4><ul><li><a href="#" data-wa>WhatsApp</a></li><li><a href="index.html#waitlist">Join the waitlist</a></li><li><a href="legal.html">Legal and privacy</a></li></ul></div>
    </div>
    <div class="legal">{LEGAL}</div>
  </div>
</footer>
<a class="fab" href="#" data-wa aria-label="Chat with ezee on WhatsApp"><svg viewBox="0 0 32 32"><path d="M16 3C8.8 3 3 8.7 3 15.8c0 2.5.7 4.9 2 7L3 29l6.4-2c2 1.1 4.3 1.7 6.6 1.7 7.2 0 13-5.7 13-12.8S23.2 3 16 3zm0 23.4c-2.1 0-4.1-.6-5.9-1.6l-.4-.3-3.8 1.2 1.2-3.7-.3-.4c-1.1-1.8-1.8-3.8-1.8-5.9C5 10 9.9 5.2 16 5.2S27 10 27 15.9s-4.9 10.5-11 10.5zm6-7.8c-.3-.2-1.9-1-2.2-1.1-.3-.1-.5-.2-.7.2-.2.3-.8 1-1 1.2-.2.2-.4.2-.7.1-.3-.2-1.4-.5-2.6-1.6-1-.9-1.6-1.9-1.8-2.2-.2-.3 0-.5.1-.7l.5-.6c.2-.2.2-.3.3-.5.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.2 1.1-1.2 2.7s1.2 3.2 1.4 3.4c.2.2 2.4 3.6 5.8 5 .8.3 1.4.5 1.9.7.8.3 1.5.2 2.1.1.6-.1 1.9-.8 2.2-1.5.3-.7.3-1.4.2-1.5-.1-.1-.3-.2-.6-.4z"/></svg></a>
<script>window.EZ_WA="{WA}";</script>
<script src="assets/ezee.js?v=2" defer></script>
</body></html>'''

def store(k):
    return (f'<a class="store" href="index.html#waitlist">{ICON[k]}<span>{"App Store" if k=="apple" else "Google Play"}'
            f'<b><em>Coming soon</em></b></span></a>')

def page(fn, title, desc, body, active='', dark=False):
    out = head(title, desc) + header(active, dark) + '<main>' + body + '</main>' + footer()
    open(os.path.join(OUT, fn), 'w').write(out)
    print('wrote', fn, len(out))

def lic(dark=False):
    return f'''<div class="lic"><span class="seal">{ICON['shield'].replace('currentColor', '#0E0E0C' if dark else '#FFC72C')}</span>
<span>ezee loans are provided by <b>Sage Grey Finance Limited</b>, licensed and regulated by the <b>Central Bank of Nigeria</b> and integrated into <b>NIBSS</b>.</span></div>'''

# ---------- shared pieces ----------
def phones():
    return f'''<div class="cluster" aria-hidden="true">
  <div class="ph b"><div class="sc">
    <div class="bar"><span>ezee for business</span><span>9:41</span></div>
    <div class="hi">Mama Tobi's Kitchen</div>
    <div class="kpi"><div><small>Today's sales</small><b>₦486,200</b></div><div><small>Payments</small><b>214</b></div></div>
    <div class="mchart"><i style="height:30%"></i><i style="height:45%"></i><i style="height:38%"></i><i style="height:62%"></i><i style="height:55%"></i><i style="height:80%"></i><i style="height:100%"></i></div>
    <span class="pill">✓ Settled to your account instantly</span>
    <div class="bal" style="margin-top:auto"><small>Working capital offer</small><div class="n" style="font-size:24px;margin-bottom:4px">₦3,000,000</div><small>Based on your sales. Repay a little from each day's takings.</small></div>
  </div></div>
  <div class="ph c"><div class="sc">
    <div class="bar"><span>ezee loans</span><span>9:41</span></div>
    <div class="hi">Your offer is ready</div>
    <div class="bal"><small>Salary loan</small><div class="n">₦850,000</div>
      <div class="s-row"><span>Monthly</span><span>₦47,530</span></div><div class="s-row"><span>From salary on</span><span>25th</span></div><div class="s-row"><span>Hidden fees</span><span>₦0</span></div></div>
    <span class="pill">✓ Approved in 2 min 41 s</span>
    <div class="tap" style="background:var(--ink);color:#fff;justify-content:center">Accept and get paid</div>
  </div></div>
  <div class="ph a"><div class="sc">
    <div class="bar"><span>{wordmark()[:0]}<b style="font:800 17px var(--display)">ezee</b></span><span>9:41</span></div>
    <div class="hi">Good morning, Tolu 👋🏾</div>
    <div class="bal"><small>Balance</small><div class="n">₦248,350.00</div>
      <div class="qa"><div><i>➜</i>Send</div><div><i>＋</i>Add</div><div><i>📱</i>Airtime</div><div><i>💡</i>Bills</div></div></div>
    <div class="tx">
      <div><span><i>🚌</i><span>BRT Ikorodu to TBS<small>Tap · 07:12</small></span></span><b>−₦500</b></div>
      <div><span><i>🍲</i><span>Mama Tobi's Kitchen<small>Tap · 13:05</small></span></span><b>−₦3,200</b></div>
      <div><span><i>💼</i><span>Salary, Lagos State<small>25 Nov</small></span></span><b style="color:var(--green)">+₦412,000</b></div>
    </div>
    <div class="tap"><span class="w">{ICON['tap']}</span><span>Tap to pay<small>Bus, shop, market. One tap.</small></span></div>
  </div></div>
  <span class="illus2">App screens are illustrations</span>
</div>'''

def strip(items):
    s = ''.join(f'<span>{i}</span>' for i in items)
    return f'<div class="strip" aria-hidden="true"><div>{s}{s}</div></div>'

WAITLIST = open(os.path.join(HERE, 'waitlist.html')).read()

# ---------- HOME ----------
home = f'''
<section class="hx">
  <div class="wrap hx-grid">
    <div class="rv" style="padding-bottom:70px">
      <p class="eyebrow">Payments · Loans · Business · Nigeria</p>
      <h1>money,<br>made <span class="y">ezee.</span></h1>
      <p class="lead">Pay with a tap. Get paid instantly. Borrow fairly against your salary or your sales. One app for the everyday money moves of 200 million Nigerians.</p>
      <div class="cta-row">
        <a href="#waitlist" class="btn btn-y">Get early access {ICON['arrow']}</a>
        <a href="pay.html" class="btn btn-o">See ezee pay</a>
      </div>
      <div class="stores">{store('apple')}{store('play')}</div>
    </div>
    <div class="rv">{phones()}</div>
  </div>
</section>
{strip(['Tap to pay','Free transfers','Airtime and data','Bills','Salary loans','Business loans','Car finance','POS for merchants','School fees','Rent'])}

<section>
  <div class="wrap">
    <p class="eyebrow rv">The everyday money app</p>
    <p class="statement rv">Every ride, every sale, every salary. <span class="m">One app that moves it all, and lends against it fairly.</span></p>
    <div class="mega">
      <a class="tile big rv" href="pay.html"><span class="ic">⚡</span><h3>ezee pay</h3><p>Tap to pay on the bus, at the shop and in the market. Send money free to any bank. Pay bills, airtime and data in seconds.</p><span class="soon" style="color:#FFC72C">Launching</span></a>
      <a class="tile y rv" href="credit.html"><span class="ic">💸</span><h3>Salary loans</h3><p>Up to ₦5m, repaid from your pay.</p></a>
      <a class="tile rv" href="business.html"><span class="ic">🏪</span><h3>Business loans</h3><p>Working capital based on your sales.</p></a>
      <a class="tile rv" href="pay.html#merchants"><span class="ic">📲</span><h3>Accept payments</h3><p>Tap, transfer or POS. Settled instantly.</p><span class="soon">Soon</span></a>
      <a class="tile rv" href="https://gomidas.co/"><span class="ic">🚗</span><h3>Car finance</h3><p>Drive now, pay monthly.</p></a>
      <a class="tile rv" href="credit.html#types"><span class="ic">🎓</span><h3>School fees</h3><p>Spread the term's fees over months.</p></a>
      <a class="tile rv" href="credit.html#types"><span class="ic">🏠</span><h3>Rent</h3><p>Pay the landlord yearly, repay monthly.</p></a>
      <a class="tile rv" href="pay.html"><span class="ic">💳</span><h3>ezee card</h3><p>Spend at home and online abroad.</p><span class="soon">Soon</span></a>
      <a class="tile rv" href="pay.html"><span class="ic">🐷</span><h3>Savings</h3><p>Put a little aside every payday.</p><span class="soon">Soon</span></a>
      <a class="tile rv" href="government.html"><span class="ic">🏛️</span><h3>For government</h3><p>Payroll, transport and revenue, made transparent.</p></a>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <p class="eyebrow rv">For you</p>
    <h2 class="rv">six apps in one.</h2>
    {showcase()}
  </div>
</section>

<section class="dark">
  <div class="wrap">
    <p class="eyebrow rv">For business and employers</p>
    <h2 class="rv">run your whole business on ezee.</h2>
    <p class="lead rv" style="margin-top:16px;max-width:54ch">Get paid, get capital, control spending and pay your people, from the market stall to the 5,000-staff employer.</p>
    {suite()}
  </div>
</section>

{REWARDS}

<section class="dark">
  <div class="wrap">
    <p class="eyebrow rv">Why now</p>
    <h2 class="rv">nigeria is ready for a money app<br>that lends fairly.</h2>
    <div class="nums">
      <div class="num rv"><b>200m+</b><span>Nigerians, most of them under 30</span><small>UN population estimate</small></div>
      <div class="num rv"><b>5–6m</b><span>workers on a formal payroll whose salary can secure a loan</span><small>ezee estimate</small></div>
      <div class="num rv"><b>3.8m</b><span>transport cards already in use in Lagos</span><small>LAMATA</small></div>
      <div class="num rv"><b>500k</b><span>paid trips a day on Lagos public transport</span><small>LAMATA</small></div>
    </div>
    <div class="goal rv"><div class="n">10m</div><p><b>Our goal: 10 million Nigerians on ezee.</b> We start where money already moves every day: transport fares in Lagos, salaries in the public service, and the sales of small businesses. Then we grow state by state.</p></div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow rv">How ezee is built</p>
    <h2 class="rv">payments in. fair credit out.</h2>
    <p class="lead rv" style="margin-top:18px;max-width:52ch">Most lenders guess. ezee sees how money really moves, so it can lend more, charge less and lose less.</p>
    <div class="rails">
      <div class="rail rv"><small>1 · Everyday payments</small><h3>Tap, send, pay</h3><p>Rides, shops, bills and transfers flow through ezee pay.</p></div>
      <div class="rail rv"><small>2 · Income you can trust</small><h3>Salary and sales</h3><p>Payroll and merchant takings show what people can really repay.</p></div>
      <div class="rail core rv"><small>3 · The ezee engine</small><h3>Credit scoring</h3><p>Bureau data from Nigeria's credit registry, plus real cash flow.</p></div>
      <div class="rail rv"><small>4 · Fair loans</small><h3>Lend</h3><p>Salary, business, car, school fees and rent loans at fair prices.</p></div>
      <div class="rail rv"><small>5 · Repaid at source</small><h3>Collect</h3><p>From payroll or daily sales. No chasing, no shaming.</p></div>
    </div>
  </div>
</section>

<section class="band" style="padding:0">
  <figure class="photo-band" style="margin-top:0">
    <picture><source media="(max-width: 800px)" srcset="img/danfo-s.jpg"><img src="img/danfo.jpg" alt="Yellow danfo buses on a Lagos road" loading="lazy"></picture>
    <figcaption class="cap"><div class="wrap"><p>Built for the people who keep Nigeria moving.</p></div></figcaption>
    <span class="credit">Photo: Omoeko Media, CC BY-SA 4.0</span>
  </figure>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow rv">Our promise</p>
    <h2 class="rv">serious about trust.</h2>
    <div class="feat">
      <div class="rv"><h3>Licensed lending</h3><p>ezee loans are provided by Sage Grey Finance Limited, licensed and regulated by the Central Bank of Nigeria and integrated into NIBSS.</p></div>
      <div class="rv"><h3>No shaming. Ever.</h3><p>We will never call or message anyone in your phone about your loan. We talk to you, only you.</p></div>
      <div class="rv"><h3>Every naira shown</h3><p>One monthly amount and every charge, before you say yes. Your data protected under the Nigeria Data Protection Act.</p></div>
    </div>
    {lic()}
  </div>
</section>

<section class="band">
  <div class="wrap">
    <p class="eyebrow rv">From the blog</p>
    <h2 class="rv">read the thinking.</h2>
    BLOGCARDS
  </div>
</section>

{WAITLIST}
'''

# ---------- PAY ----------
pay = f'''
<section class="hx" style="padding-bottom:0">
  <div class="wrap hx-grid">
    <div class="rv" style="padding-bottom:70px">
      <p class="eyebrow">ezee pay · launching in Lagos</p>
      <h1>one tap.<br><span class="y">everywhere.</span></h1>
      <p class="lead">The bus. The shop. The market. Your friends. Your bills. ezee pay is the fastest way to move money in Nigeria, with no change, no network wahala and nothing to remember.</p>
      <div class="cta-row"><a href="index.html#waitlist" class="btn btn-y">Be first in line {ICON['arrow']}</a><a href="#merchants" class="btn btn-o">I'm a merchant</a></div>
    </div>
    <div class="rv">{phones()}</div>
  </div>
</section>
{strip(['Tap to ride','Free transfers','Airtime in seconds','Pay any bill','Get paid instantly','QR and POS','Save every payday'])}
<section class="band"><div class="wrap"><p class="eyebrow rv">The ezee app</p><h2 class="rv">wallet, pay, save, card, credit, auto.</h2>{showcase()}</div></section>
<section>
  <div class="wrap">
    <p class="eyebrow rv">For you</p>
    <h2 class="rv">everything your money does in a day.</h2>
    <div class="mega">
      <div class="tile big rv"><span class="ic">🚌</span><h3>Tap to ride</h3><p>Pay for the bus and the ferry with a tap of your phone or card. See every trip, top up from your account and never hunt for change again.</p></div>
      <div class="tile rv"><span class="ic">➜</span><h3>Free transfers</h3><p>Send money to any Nigerian bank account.</p></div>
      <div class="tile rv"><span class="ic">📱</span><h3>Airtime and data</h3><p>Every network, in seconds.</p></div>
      <div class="tile rv"><span class="ic">💡</span><h3>Bills</h3><p>Electricity, TV, water, internet.</p></div>
      <div class="tile rv"><span class="ic">🧾</span><h3>Split and request</h3><p>Share the bill, request the money.</p></div>
      <div class="tile rv"><span class="ic">💳</span><h3>ezee card</h3><p>For shops at home and online abroad.</p></div>
      <div class="tile y rv"><span class="ic">🎁</span><h3>Rewards</h3><p>Ride ten times, the eleventh is on us.</p></div>
    </div>
  </div>
</section>
<section class="dark" id="merchants">
  <div class="wrap split">
    <div class="rv">
      <p class="eyebrow">ezee for merchants</p>
      <h2>get paid the second you sell.</h2>
      <p class="lead" style="margin-top:18px">From the mama put to the supermarket. Accept tap, transfer, QR and card on your phone or an ezee POS, and see the money land instantly.</p>
      <ul class="list"><li>Instant settlement to your account</li><li>Your phone becomes the terminal. No rented machine needed</li><li>Your sales history unlocks working capital from ezee</li><li>One dashboard for every branch and every staff member</li></ul>
      <a href="index.html#waitlist" class="btn btn-y">Sign up my business</a>
    </div>
    <div class="shot rv"><img src="img/market.jpg" alt="Traders at Oshodi market, Lagos" loading="lazy"><span class="credit">Photo: Agbebiyi Adekunle, CC BY-SA 4.0</span></div>
  </div>
</section>
<section>
  <div class="wrap split">
    <div class="shot rv"><img src="img/brt.jpg" alt="BRT bus at Mile 12 bus stop, Lagos" loading="lazy"><span class="credit">Photo: Olatunbosun Success, CC BY-SA 4.0</span></div>
    <div class="rv">
      <p class="eyebrow">For transport operators</p>
      <h2>every fare, counted.</h2>
      <p class="lead" style="margin-top:18px">Digital fares mean no leakage, live data on every route and revenue that can be planned, financed and invested in new buses.</p>
      <ul class="list"><li>Fares settle daily, with a full audit trail</li><li>Route and ridership data in real time</li><li>Revenue you can borrow against to grow your fleet</li></ul>
      <a href="government.html" class="btn btn-k">For governments and operators</a>
    </div>
  </div>
</section>
<section class="band">
  <div class="wrap">
    <p class="eyebrow rv">Built to be trusted</p>
    <h2 class="rv">safe by design.</h2>
    <div class="feat">
      <div class="rv"><h3>Licensed partners</h3><p>ezee pay will run through payment partners licensed by the Central Bank of Nigeria. We'll name them here at launch.</p></div>
      <div class="rv"><h3>Bank-grade security</h3><p>Encryption end to end, PIN and biometric approval for every payment, and instant freeze from the app.</p></div>
      <div class="rv"><h3>Real people, fast</h3><p>Support on WhatsApp, in English and pidgin, with real answers from real people.</p></div>
    </div>
  </div>
</section>
{WAITLIST}
'''

# ---------- LOANS ----------
LOANS = [
 ('💼','Salary loan','Live first','For civil servants and staff of partner employers. Repaid from your pay on payday.',[('Amount','₦50k to ₦5m'),('Term','3 to 24 months'),('Repaid','From salary')]),
 ('🏪','Business loan','Soon','Working capital for traders and small businesses, based on your sales through ezee.',[('Amount','₦100k to ₦20m'),('Term','1 to 12 months'),('Repaid','From daily sales')]),
 ('🚗','Car finance','With Midas','A newer car on a monthly plan, with the car as security.',[('Amount','Up to 80% of the car'),('Term','12 to 48 months'),('Repaid','Monthly')]),
 ('🎓','School fees','Soon','Pay the school in full. Spread it across the term.',[('Amount','Up to ₦3m'),('Term','3 to 9 months'),('Repaid','From salary')]),
 ('🏠','Rent','Soon','Landlords want a year up front. You pay monthly.',[('Amount','Up to ₦6m'),('Term','6 to 12 months'),('Repaid','From salary')]),
 ('⚕️','Health and emergencies','Soon','For the bills that can\'t wait. Fast decision, fair price.',[('Amount','₦50k to ₦2m'),('Term','3 to 12 months'),('Repaid','From salary')]),
 ('🛠️','Car repair','Soon','Fix it now at a trusted workshop, pay it off over months.',[('Amount','Up to ₦1.5m'),('Term','3 to 12 months'),('Repaid','From salary')]),
 ('🚚','Fleet and asset finance','For business','Buses, trucks and equipment for operators and companies.',[('Amount','Tailored'),('Term','Up to 5 years'),('Repaid','From revenue')]),
 ('🏛️','Public-sector programmes','For government','Vehicle and housing schemes for state and federal workers.',[('Amount','Programme-wide'),('Term','Tailored'),('Repaid','Payroll')]),
]
def loancards():
    out = '<div class="loans" id="types">'
    for ic,t,tag,p,dl in LOANS:
        d = ''.join(f'<dt>{a}</dt><dd>{b}</dd>' for a,b in dl)
        out += f'<div class="loan rv"><div class="row"><span class="ic">{ic}</span><span class="t{" live" if tag=="Live first" else ""}">{tag}</span></div><h3>{t}</h3><p>{p}</p><dl>{d}</dl></div>'
    return out + '</div>'

CALC = open(os.path.join(HERE, 'calc.html')).read()
COMPARE = open(os.path.join(HERE, 'compare.html')).read()
loans = f'''
<section class="ph-hero yel">
  <div class="wrap">
    <p class="eyebrow rv">ezee credit</p>
    <h1 class="rv">credit that respects your salary.</h1>
    <p class="lead rv">Fair loans for the things that matter, decided in minutes and repaid automatically. One clear monthly amount. No hidden charges. No wahala.</p>
    <div class="cta-row rv" style="margin-top:30px"><a href="#calculator" class="btn btn-k">See your monthly</a><a href="index.html#waitlist" class="btn btn-o">Join the waitlist</a></div>
    {lic()}
  </div>
</section>
<section>
  <div class="wrap">
    <p class="eyebrow rv">Every loan you need</p>
    <h2 class="rv">one place for all of it.</h2>
    {loancards()}
    <p class="rv" style="margin-top:16px;color:var(--muted);font-size:14px">Amounts and terms are planned ranges. Your offer depends on your credit check and affordability.</p>
  </div>
</section>
{COMPARE}
{CALC}
<section>
  <div class="wrap">
    <p class="eyebrow rv">How it works</p>
    <h2 class="rv">four steps. no queue. no paper.</h2>
    <div class="steps">
      <div class="step rv"><h3>Apply on your phone</h3><p>A few minutes. Your BVN, your payslip, your bank. That's it.</p></div>
      <div class="step rv"><h3>We check, fast</h3><p>Your salary and credit history with Nigeria's credit bureau.</p></div>
      <div class="step rv"><h3>Say yes</h3><p>See your exact monthly and every charge. Accept only if it works for you.</p></div>
      <div class="step rv"><h3>Repay on payday</h3><p>Your repayment comes off your salary automatically. Done.</p></div>
    </div>
  </div>
</section>
{WAITLIST}
'''

# ---------- BUSINESS ----------
business = f'''
<section class="ph-hero dark">
  <div class="wrap">
    <p class="eyebrow rv">ezee for business</p>
    <h1 class="rv">grow on your own <span style="color:var(--yellow)">sales.</span></h1>
    <p class="lead rv">Accept payments, see your money in real time and unlock working capital based on what you actually sell. From the market stall to the fleet operator.</p>
    <div class="cta-row rv" style="margin-top:30px"><a href="index.html#waitlist" class="btn btn-y">Sign up my business</a><a href="#credit" class="btn btn-o" style="color:#fff;box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.5)">Business loans</a></div>
  </div>
</section>
<section class="dark" style="padding-top:20px"><div class="wrap">{suite()}</div></section>
<section id="credit">
  <div class="wrap">
    <p class="eyebrow rv">ezee finance</p>
    <h2 class="rv">capital for every stage.</h2>
    <div class="loans">
      <div class="loan rv"><div class="row"><span class="ic">📈</span><span class="t">Soon</span></div><h3>Working capital</h3><p>Restock before the rush. Repaid automatically from a small share of daily sales.</p><dl><dt>Amount</dt><dd>₦100k to ₦20m</dd><dt>Term</dt><dd>1 to 12 months</dd></dl></div>
      <div class="loan rv"><div class="row"><span class="ic">🧾</span><span class="t">Soon</span></div><h3>Invoice finance</h3><p>Big client paying in 90 days? Get most of the invoice now.</p><dl><dt>Advance</dt><dd>Up to 80%</dd><dt>Term</dt><dd>30 to 120 days</dd></dl></div>
      <div class="loan rv"><div class="row"><span class="ic">🚚</span><span class="t">Soon</span></div><h3>Asset and fleet finance</h3><p>Buses, trucks, generators, machines. The asset secures the loan.</p><dl><dt>Amount</dt><dd>Tailored</dd><dt>Term</dt><dd>Up to 5 years</dd></dl></div>
      <div class="loan rv"><div class="row"><span class="ic">🌍</span><span class="t">Soon</span></div><h3>Trade finance</h3><p>Pay your suppliers abroad on time, sell at home, then settle.</p><dl><dt>Amount</dt><dd>Tailored</dd><dt>Term</dt><dd>60 to 180 days</dd></dl></div>
      <div class="loan rv"><div class="row"><span class="ic">👥</span><span class="t">Soon</span></div><h3>Staff loans</h3><p>Offer your team fair salary loans at no cost to the company.</p><dl><dt>Cost to you</dt><dd>₦0</dd><dt>Repaid</dt><dd>Payroll</dd></dl></div>
      <div class="loan rv"><div class="row"><span class="ic">🏗️</span><span class="t">Soon</span></div><h3>Contract finance</h3><p>Won a government or corporate contract? Fund the delivery.</p><dl><dt>Amount</dt><dd>Tailored</dd><dt>Term</dt><dd>Contract length</dd></dl></div>
    </div>
    <p class="rv" style="margin-top:16px;color:var(--muted);font-size:14px">Planned products and ranges. All business credit is subject to approval.</p>
  </div>
</section>
<section class="band">
  <div class="wrap split">
    <div class="rv">
      <p class="eyebrow">Accept payments</p>
      <h2>your phone is the till.</h2>
      <p class="lead" style="margin-top:18px">Tap, transfer, QR or card. Settled instantly, recorded automatically, ready for your accountant and your next loan.</p>
      <ul class="list"><li>Instant settlement</li><li>Every branch and staff member on one dashboard</li><li>Payroll and supplier payments in one click</li></ul>
      <a href="pay.html#merchants" class="btn btn-k">See ezee for merchants</a>
    </div>
    <div class="shot rv"><img src="img/market.jpg" alt="Traders at Oshodi market, Lagos" loading="lazy"><span class="credit">Photo: Agbebiyi Adekunle, CC BY-SA 4.0</span></div>
  </div>
</section>
<section class="dark" id="spend"><div class="wrap split"><div class="rv"><p class="eyebrow">ezee spend</p><h2>company money, under control.</h2><p class="lead" style="margin-top:18px">Give every team member a card with its own limit, pay suppliers in bulk and approve expenses from your phone.</p><ul class="list"><li>Team cards with limits per person and category</li><li>Bulk supplier and vendor payouts</li><li>Receipts snapped, expenses approved in-app</li><li>Spend by branch, team and project in real time</li></ul></div><div class="stage" style="display:flex;justify-content:center"><div class="ph" style="position:relative"><div class="sc"><div class="bar"><span>ezee spend</span><span>9:41</span></div><div class="hi">This month</div><div class="kpi"><div><small>Team spend</small><b>₦4.2m</b></div><div><small>Budget left</small><b>₦1.8m</b></div></div><div class="tx"><div><span><i>⛽</i><span>Fuel · Logistics<small>Card · Tunde</small></span></span><b>−₦85,000</b></div><div><span><i>📦</i><span>Supplier batch (12)<small>Bulk payout</small></span></span><b>−₦2.1m</b></div><div><span><i>🧾</i><span>Client lunch<small>Receipt attached</small></span></span><b>−₦46,500</b></div></div><span class="pill">✓ 3 expenses approved</span><div class="tap" style="margin-top:auto;justify-content:center">Issue a new card</div></div></div></div></div></section>
<section>
  <div class="wrap"><div class="cta-band rv"><div><h2>talk to our business team.</h2><p>Payments, payroll, staff loans or fleet finance. Tell us what you need on WhatsApp.</p></div><div class="cta-row"><a href="#" data-wa data-msg="Hi ezee, I'd like to talk about ezee for my business." class="btn btn-y">Chat on WhatsApp</a></div></div></div>
</section>
{WAITLIST}
'''

# ---------- GOVERNMENT ----------
gov = f'''
<section class="ph-hero dark">
  <div class="wrap">
    <p class="eyebrow rv">For federal, state and local government</p>
    <h1 class="rv">public money, <span style="color:var(--yellow)">made transparent.</span></h1>
    <p class="lead rv">ezee helps governments collect revenue without leakage, give public servants fair access to credit and finance the buses, vehicles and homes their people need, all on licensed, auditable rails.</p>
    <div class="cta-row rv" style="margin-top:30px"><a href="#" data-wa data-msg="Hi ezee, I'm writing on behalf of a government agency and would like a briefing." class="btn btn-y">Request a briefing</a></div>
  </div>
</section>
<section>
  <div class="wrap">
    <p class="eyebrow rv">What we do with governments</p>
    <h2 class="rv">four programmes. one platform.</h2>
    <div class="mega" style="grid-template-columns:repeat(2,1fr)">
      <div class="tile big rv" style="grid-column:span 1"><span class="ic">🚌</span><h3>Transport revenue</h3><p>Digital fares across bus, rail and ferry. Every naira counted, settled daily and auditable, with live data on every route.</p></div>
      <div class="tile y rv"><span class="ic">💼</span><h3>Public servant credit</h3><p>Fair salary loans through payroll, so public servants stop paying loan-app prices. No cost to the state.</p></div>
      <div class="tile rv"><span class="ic">🚗</span><h3>Vehicle and housing schemes</h3><p>Programmes that put cars, motorcycles and homes within reach of state and federal workers, repaid through payroll.</p></div>
      <div class="tile rv"><span class="ic">🏗️</span><h3>Infrastructure finance</h3><p>Revenue from new buses and transport can be ring-fenced to repay the finance that bought them, bringing in new fleets without new budget.</p></div>
    </div>
  </div>
</section>
<section class="dark">
  <div class="wrap">
    <p class="eyebrow rv">Why it matters</p>
    <h2 class="rv">what a state gets.</h2>
    <div class="feat">
      <div class="rv"><h3>No leakage</h3><p>Cash disappears. Digital collections settle daily into accounts the state can see, with a full audit trail.</p></div>
      <div class="rv"><h3>Happier workforce</h3><p>Public servants get fair credit for school fees, rent and cars, without predatory lenders or shaming.</p></div>
      <div class="rv"><h3>New assets, no new debt</h3><p>Buses and vehicles financed against their own revenue, with private capital and international partners.</p></div>
    </div>
  </div>
</section>
<section>
  <div class="wrap split">
    <div class="shot rv"><img src="img/brt.jpg" alt="BRT bus at Mile 12, Lagos" loading="lazy"><span class="credit">Photo: Olatunbosun Success, CC BY-SA 4.0</span></div>
    <div class="rv">
      <p class="eyebrow">How we work</p>
      <h2>start with one programme. scale to every state.</h2>
      <ul class="list"><li>Start with a pilot in one agency, one corridor or one payroll</li><li>Licensed partners: lending through Sage Grey Finance Limited, licensed and regulated by the CBN and integrated into NIBSS</li><li>Data protected under the Nigeria Data Protection Act 2023</li><li>Reporting built for auditors, treasuries and accountants-general</li></ul>
      <a href="#" data-wa data-msg="Hi ezee, I'm writing on behalf of a government agency and would like a briefing." class="btn btn-k">Request a briefing</a>
    </div>
  </div>
</section>
<section><div class="wrap">{lic()}</div></section>
'''

# ---------- ABOUT ----------
about = f'''
<section class="ph-hero">
  <div class="wrap">
    <p class="eyebrow rv">About ezee</p>
    <h1 class="rv">we're making money <span style="background:linear-gradient(transparent 62%, var(--yellow) 62%, var(--yellow) 92%, transparent 92%)">easy</span> for every Nigerian.</h1>
    <p class="lead rv">Paying shouldn't take three tries. Borrowing shouldn't cost a third of your pay. Getting paid shouldn't take a week. We're building the app that fixes all three.</p>
  </div>
</section>
<section class="band" style="padding:0">
  <figure class="photo-band" style="margin-top:0"><picture><source media="(max-width: 800px)" srcset="img/danfo-s.jpg"><img src="img/danfo.jpg" alt="Danfo buses in Lagos" loading="lazy"></picture><span class="credit">Photo: Omoeko Media, CC BY-SA 4.0</span></figure>
</section>
<section>
  <div class="wrap">
    <p class="eyebrow rv">Our mission</p>
    <p class="statement rv">Fair, fast money for the people who keep Nigeria running. <span class="m">Starting in Lagos. Built for all 36 states.</span></p>
    <div class="feat">
      <div class="rv"><h3>What we believe</h3><p>Nigerians don't have a credit problem. They have a pricing problem. People who earn a salary or run a busy shop deserve credit priced on what they earn, not on what lenders fear.</p></div>
      <div class="rv"><h3>What we're building</h3><p>One app for paying, getting paid and borrowing fairly. Payments show us how money really moves, so we can lend more, charge less and never chase.</p></div>
      <div class="rv"><h3>How we behave</h3><p>Every charge shown up front. No shaming. Licensed partners. Data protected. Real people on WhatsApp. Simple as that.</p></div>
    </div>
  </div>
</section>
<section class="dark">
  <div class="wrap">
    <p class="eyebrow rv">Who's behind it</p>
    <h2 class="rv">bankers, builders and operators.</h2>
    <p class="lead rv" style="margin-top:18px;max-width:58ch">ezee brings together decades of experience across Nigerian banking, payments, credit and capital markets, with a licensed lending partner, Nigeria's credit bureau and international investors behind the loan book.</p>
    <div class="nums">
      <div class="num rv"><b>CBN</b><span>Licensed and regulated lending partner, integrated into NIBSS</span></div>
      <div class="num rv"><b>Bureau</b><span>Every borrower scored with Nigeria's credit registry</span></div>
      <div class="num rv"><b>Global</b><span>Capital-markets partners in Lagos, Dubai, London and Hong Kong</span></div>
      <div class="num rv"><b>36</b><span>States we're building for, one at a time</span></div>
    </div>
  </div>
</section>
<section>
  <div class="wrap"><div class="cta-band rv"><div><h2>why the name?</h2><p>It started with a joke at dinner and became the whole company. Read the story.</p></div><div class="cta-row"><a href="why-ezee.html" class="btn btn-y">Why "ezee" {ICON['arrow']}</a></div></div></div>
</section>
{WAITLIST}
'''

# ---------- WHY EZEE ----------
why = f'''
<section class="ph-hero yel">
  <div class="wrap">
    <p class="eyebrow rv">Why we called it ezee</p>
    <div class="name-big rv">ezee<i></i></div>
    <p class="lead rv" style="margin-top:30px;max-width:46ch">Say it out loud. It's "easy", the way Lagos says it. Because that's the whole point.</p>
  </div>
</section>
<section>
  <div class="wrap">
    <p class="statement rv">Money in Nigeria is hard. <span class="m">Failed transfers. Loan apps that shame you. Change for the bus. We named the company after the one thing everyone wants it to be.</span></p>
    <div class="defs">
      <div class="def rv"><b>e · easy</b><p>Pay with one tap. Borrow in minutes. Nothing to print, no branch to visit, no queue.</p></div>
      <div class="def rv"><b>z · zero wahala</b><p>No hidden charges, no surprise fees and no calls to your family. Every naira shown before you agree.</p></div>
      <div class="def rv"><b>ee · everyone, everywhere</b><p>From the danfo to the boardroom, Lagos to Kano. Built for all 200 million of us.</p></div>
    </div>
  </div>
</section>
<section class="band">
  <div class="wrap">
    <p class="eyebrow rv">The mark</p>
    <h2 class="rv">an e that moves forward.</h2>
    <p class="lead rv" style="margin-top:18px;max-width:54ch">Our mark is a lowercase e whose stroke turns into an arrow: money moving forward, one tap at a time. The yellow is the yellow of the Lagos danfo, the colour of a city that never stops moving.</p>
    <div class="logo-show">
      <div class="lg k rv">{wordmark('#FFFFFF')}<small>On ink</small></div>
      <div class="lg y rv">{wordmark('#0E0E0C','#0E0E0C','#FFC72C')}<small>On danfo yellow</small></div>
      <div class="lg w rv"><span class="app">{mark()}</span><small>App icon</small></div>
    </div>
  </div>
</section>
{WAITLIST}
'''

# ---------- BLOG ----------
POSTS = [
 ('fair-credit.html','img/market.jpg','Credit','Why salary-backed credit costs less','When repayment comes straight from payroll, the lender\'s biggest risk disappears. Here\'s why that should make loans cheaper for every salaried Nigerian.',
  '''<p>Ask any Nigerian who has used a loan app and you'll hear the same story: a small amount, a short deadline, charges that pile up the moment you're late, and then the calls. Calls to you. Calls to your sister. Calls to your boss.</p>
<p>That model exists for a reason. A lender who doesn't know whether you'll repay has to price for the people who won't. So everyone pays for the defaults of a few, and the lender chases hard to recover what it can.</p>
<h2>The salary changes everything</h2>
<p>About five to six million Nigerians earn a regular salary, in the civil service, in banks, in oil and gas and in established companies. For them, there is a better way. When repayment is deducted from payroll on payday, the lender no longer has to guess whether the money will come back.</p>
<blockquote>Less risk for the lender should mean a lower price for the borrower. That's the whole idea behind ezee loans.</blockquote>
<p>Lower risk means the lender needs a smaller margin for losses. It means no army of collectors. And it means bigger amounts over longer terms, so a teacher can pay school fees in instalments instead of borrowing ₦30,000 at a time.</p>
<h2>What we promise in return</h2>
<ul><li>One monthly amount, with every charge shown before you accept.</li><li>Repayments kept at or below a third of your take-home pay.</li><li>No calls or messages to anyone in your phone. Ever.</li></ul>
<p>Fair credit isn't charity. It's just credit priced on what people really earn. That's what we're building.</p>'''),
 ('tap-to-pay.html','img/brt.jpg','Payments','What tap-to-pay could mean for Lagos','Millions of journeys a day, most still paid in cash. What changes when every fare is a tap?',
  '''<p>Lagos moves. Hundreds of thousands of paid trips happen every day on public transport alone, and millions of Lagosians already carry a transport card. Yet for most daily journeys, cash is still king, and with cash comes the hunt for change, the arguments, and money that never quite reaches the operator.</p>
<h2>A tap is data</h2>
<p>Every tap is a record: which route, what time, how much. For commuters, that means seeing exactly where their transport money goes. For operators, it means knowing which routes are full and which need more buses. For government, it means revenue that can be counted, audited and planned.</p>
<blockquote>Cash disappears. Taps add up.</blockquote>
<h2>From fares to finance</h2>
<p>Predictable, digital fare revenue does something powerful: it can be used to finance new buses. When lenders can see the revenue a route generates, they can fund the fleet that serves it, repaid from the fares themselves.</p>
<p>That's why ezee pay starts with the journeys people make every day. Pay for the ride with a tap, then for lunch, then for airtime. One habit, one app, a whole economy that runs a little more smoothly.</p>'''),
 ('no-shaming.html','img/danfo.jpg','Our promise','Our promise: we will never shame a borrower','Debt-shaming has no place in Nigerian finance. Here\'s how ezee does collections differently.',
  '''<p>Few things have damaged trust in digital lending in Nigeria as much as debt-shaming: lenders contacting a borrower's family, friends and colleagues, sometimes with messages designed to humiliate. Regulators have rightly cracked down on it.</p>
<p>At ezee, we've made a simple promise. We will never message or call anyone in your phone about your loan. We don't even ask for access to your contacts.</p>
<h2>Why we can afford to be decent</h2>
<p>Shaming is a tactic for lenders who have no other way to get paid. Because ezee loans are repaid from salary or from daily sales through ezee pay, we don't need it. Repayment happens automatically, in the background.</p>
<blockquote>If you hit a hard month, talk to us. We'll work it out with you, not around you.</blockquote>
<h2>What happens if life gets in the way</h2>
<ul><li>Changed jobs? We'll move your repayment to your new salary account.</li><li>Unexpected bill? We'll look at a payment plan that works.</li><li>Something wrong? Real people on WhatsApp, in English and pidgin.</li></ul>
<p>Decent lending is good lending. It's how we'll earn the trust of millions of Nigerians, one fair loan at a time.</p>'''),
]
def blogcards(n=3):
    out = '<div class="posts">'
    for fn,img,cat,t,ex,_ in POSTS[:n]:
        out += f'<a class="post rv" href="{fn}"><div class="im"><img src="{img}" alt="" loading="lazy"></div><small>{cat} · 5 min read</small><h3>{t}</h3><p>{ex}</p></a>'
    return out + '</div>'

blog = f'''
<section class="ph-hero">
  <div class="wrap">
    <p class="eyebrow rv">The ezee blog</p>
    <h1 class="rv">money, explained.</h1>
    <p class="lead rv">Ideas on fair credit, everyday payments and building a fintech for every Nigerian.</p>
  </div>
</section>
<section style="padding-top:0"><div class="wrap">{blogcards()}</div></section>
'''

home = home.replace('BLOGCARDS', blogcards())

legal = f'''
<section class="ph-hero"><div class="wrap article" style="margin:0">
<p class="eyebrow">Legal and privacy</p><h1>the fine print, in plain words.</h1></div></section>
<section style="padding-top:0"><div class="wrap article">
<h2>Who we are</h2><p>ezee is a technology company, not a bank. ezee loans are provided by Sage Grey Finance Limited, which is licensed and regulated by the Central Bank of Nigeria and integrated into the Nigerian Inter-Bank Settlement System (NIBSS).</p>
<p>ezee pay, the ezee card and savings are not yet live. When they launch they will be provided through payment and banking partners licensed by the Central Bank of Nigeria, and we will name them on this page.</p>
<h2>Loans</h2><p>All loans are subject to eligibility, a credit check with a licensed credit bureau and an affordability assessment. Before you accept any loan you will see the amount, the term, the monthly repayment, the total cost and every charge. Rates, amounts, terms and app screens on this website are examples and illustrations.</p>
<h2>Collections</h2><p>We will never contact anyone in your phone, your family, your friends or your colleagues about your loan, and we do not ask for access to your contacts.</p>
<h2>Your data</h2><p>We process personal data in line with the Nigeria Data Protection Act 2023. If you join the waitlist we use your name, WhatsApp number and the answers you choose only to contact you about ezee. We do not sell personal data. To ask what we hold, to correct it or to be removed, message us on WhatsApp.</p>
<h2>Figures on this site</h2><p>Market figures are third-party estimates (UN population estimates; LAMATA transport data) or ezee estimates, and are labelled. Targets such as "10 million Nigerians" are goals, not results.</p>
</div></section>
'''

employers = f"""
<section class="ph-hero dark">
  <div class="wrap">
    <p class="eyebrow rv">ezee for employers</p>
    <h1 class="rv">look after your people. <span style="color:var(--yellow)">at no cost.</span></h1>
    <p class="lead rv">Run payroll, give staff fair credit and salary advances, and help them save. Your team stops borrowing from loan apps, and your company pays nothing for the benefit.</p>
    <div class="cta-row rv" style="margin-top:30px"><a href="#" data-wa data-msg="Hi ezee, I'd like to offer ezee to my staff." class="btn btn-y">Offer ezee to my staff</a></div>
  </div>
</section>
<section>
  <div class="wrap">
    <p class="eyebrow rv">What your staff get</p>
    <h2 class="rv">a better payday for everyone.</h2>
    <div class="mega">
      <div class="tile big rv"><span class="ic">💸</span><h3>Fair staff credit</h3><p>Salary-backed credit for school fees, rent and emergencies, repaid through payroll, at a fraction of loan-app prices.</p></div>
      <div class="tile y rv"><span class="ic">⏩</span><h3>Salary advance</h3><p>Access part of what they've already earned before payday.</p></div>
      <div class="tile rv"><span class="ic">🐷</span><h3>Auto-save</h3><p>A share of every salary into ezee save.</p></div>
      <div class="tile rv"><span class="ic">🚗</span><h3>Staff car scheme</h3><p>A car on a monthly plan, repaid through payroll.</p></div>
    </div>
  </div>
</section>
<section class="band">
  <div class="wrap">
    <p class="eyebrow rv">What you get</p>
    <h2 class="rv">ezee payroll.</h2>
    <div class="feat">
      <div class="rv"><h3>Pay everyone in one click</h3><p>Salaries to any Nigerian bank, with PAYE and pension schedules ready to file.</p></div>
      <div class="rv"><h3>Zero cost, zero risk</h3><p>We fund the credit. You run one deduction per staff member. No balance-sheet exposure for the company.</p></div>
      <div class="rv"><h3>A calmer workforce</h3><p>Money stress is the hidden cost of absenteeism and churn. Fair credit and savings take it off the table.</p></div>
    </div>
  </div>
</section>
<section>
  <div class="wrap">
    <p class="eyebrow rv">How it works</p>
    <h2 class="rv">live in a week.</h2>
    <div class="steps">
      <div class="step rv"><h3>Sign up</h3><p>A short agreement and your payroll contact.</p></div>
      <div class="step rv"><h3>Connect payroll</h3><p>Upload a file or connect your payroll system.</p></div>
      <div class="step rv"><h3>Staff join</h3><p>Your team downloads ezee and sees their offers.</p></div>
      <div class="step rv"><h3>One deduction</h3><p>Repayments come off payroll each month. Done.</p></div>
    </div>
    <div class="cta-band rv" style="margin-top:56px"><div><h2>public sector too.</h2><p>State and federal payrolls can offer ezee to civil servants. See our government programmes.</p></div><div class="cta-row"><a href="government.html" class="btn btn-y">For government</a></div></div>
  </div>
</section>
{WAITLIST}
"""
page('employers.html', 'ezee for employers', 'Payroll, fair staff credit, salary advances and savings at no cost to the employer.', employers, 'employers.html', True)
page('index.html', 'ezee · money, made ezee', 'Pay with a tap, get paid instantly and borrow fairly. Payments, loans and business banking for every Nigerian.', home, '', True)
page('pay.html', 'ezee pay · one tap, everywhere', 'Tap to pay on the bus and at the shop, free transfers, bills and instant settlement for merchants.', pay, 'pay.html', True)
page('credit.html', 'ezee credit · credit that respects your salary', 'Salary, business, car, school fees and rent loans. Decided in minutes, repaid automatically.', loans, 'credit.html')
page('business.html', 'ezee for business', 'Accept payments and unlock working capital, invoice, fleet and trade finance based on your sales.', business, 'business.html', True)
page('government.html', 'ezee for government', 'Transparent transport revenue, fair public-servant credit and vehicle programmes on licensed rails.', gov, 'government.html', True)
page('about.html', 'About ezee', 'We are making money easy for every Nigerian.', about, 'about.html')
page('why-ezee.html', 'Why we called it ezee', 'Easy, the way Lagos says it.', why, 'about.html')
page('blog.html', 'The ezee blog', 'Ideas on fair credit, payments and fintech in Nigeria.', blog, 'blog.html')
page('legal.html', 'Legal and privacy · ezee', 'Licensing, loans, collections and data protection at ezee.', legal)
for fn,img,cat,t,ex,body in POSTS:
    more = ''.join(f'<a class="post" href="{f2}"><small>{c2}</small><h3>{t2}</h3></a>' for f2,i2,c2,t2,e2,b2 in POSTS if f2 != fn)
    art = f'''<section class="ph-hero" style="padding-bottom:24px"><div class="wrap article"><p class="eyebrow"><a href="blog.html" style="text-decoration:none">Blog</a> · {cat}</p><h1>{t}</h1><p class="meta">The ezee team · 5 min read</p></div></section>
<section style="padding-top:0"><div class="wrap article"><div class="hero-im"><img src="{img}" alt=""></div>{body}
<div class="cta-band" style="margin-top:44px"><div><h2 style="font-size:32px">be first on ezee.</h2></div><div class="cta-row"><a href="index.html#waitlist" class="btn btn-y">Join the waitlist</a></div></div>
<h2>Keep reading</h2><div class="posts" style="grid-template-columns:1fr 1fr;margin-top:10px">{more}</div></div></section>'''
    page(fn, t + ' · ezee blog', ex, art, 'blog.html')

css = open(os.path.join(HERE, 'base.css')).read() + open(os.path.join(HERE, 'extra.css')).read()
open(os.path.join(OUT, 'assets', 'ezee.css'), 'w').write(css)
open(os.path.join(OUT, 'assets', 'ezee.js'), 'w').write(open(os.path.join(HERE, 'ezee.js')).read())
open(os.path.join(OUT, 'img', 'icon.svg'), 'w').write(mark().replace('<svg ', '<svg xmlns="http://www.w3.org/2000/svg" '))
print('done')
