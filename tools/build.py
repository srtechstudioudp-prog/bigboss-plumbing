#!/usr/bin/env python3
"""Builds the static preview site into ../public. Run: python tools/build.py"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "public"

PHONE = "(832) 659-7540"
TEL = "+18326597540"

def ic(path):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % path)

I = {
 "phone": ic('<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/>'),
 "arrow": ic('<path d="M4 12h15M13 6l6 6-6 6"/>'),
 "star": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2.8l2.8 5.8 6.4.9-4.6 4.4 1.1 6.3L12 17.3l-5.7 2.9 1.1-6.3L2.8 9.5l6.4-.9z"/></svg>',
 "pin": ic('<path d="M12 21s7-6.2 7-11.5A7 7 0 0 0 5 9.5C5 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>'),
 "clock": ic('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'),
}

LOGO = '''<svg viewBox="0 0 64 40" role="img" aria-label="B&amp;B Big Boss logo concept"><rect x="1" y="5" width="62" height="30" rx="15" fill="#d0662a"/><rect x="7" y="11" width="50" height="18" rx="9" fill="#14181a"/><ellipse cx="32" cy="20" rx="11" ry="5.2" fill="#58bba9"/><path d="M21 12v16M43 12v16" stroke="#f5f3ee" stroke-opacity=".55" stroke-width="1.5"/></svg>'''

SECTION_ART = '''<svg viewBox="0 0 600 420" role="img" aria-label="Section drawing of a house on a slab with piers, a leaking supply line and washed-out soil underneath" font-family="IBM Plex Mono,Consolas,monospace" font-size="11" letter-spacing=".8">
<defs><pattern id="hatch" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="12" stroke="#f5f3ee" stroke-opacity=".13" stroke-width="2"/></pattern></defs>
<rect x="10" y="214" width="580" height="196" fill="url(#hatch)"/>
<path d="M10 214H590" stroke="#f5f3ee" stroke-opacity=".5"/>
<ellipse cx="372" cy="228" rx="46" ry="11" fill="#14181a" stroke="#f5f3ee" stroke-opacity=".7" stroke-dasharray="4 4"/>
<ellipse cx="372" cy="300" rx="64" ry="36" fill="#58bba9" fill-opacity=".16" stroke="#58bba9" stroke-opacity=".6" stroke-dasharray="3 5"/>
<g fill="#d0662a"><rect x="150" y="214" width="20" height="100"/><rect x="290" y="214" width="20" height="100"/><rect x="430" y="214" width="20" height="100"/></g>
<g fill="#14181a" fill-opacity=".35"><rect x="150" y="214" width="20" height="8"/><rect x="290" y="214" width="20" height="8"/><rect x="430" y="214" width="20" height="8"/></g>
<path d="M10 262H590" stroke="#58bba9" stroke-width="9" stroke-linecap="round"/>
<path d="M10 262H590" stroke="#c4f1e8" stroke-opacity=".45" stroke-width="2"/>
<g fill="#58bba9"><path d="M372 274c0 0 7 8 7 13a7 7 0 0 1-14 0c0-5 7-13 7-13z"/><path d="M386 300c0 0 5 6 5 9.5a5 5 0 0 1-10 0c0-3.500 5-9.500 5-9.500z" fill-opacity=".7"/></g>
<rect x="90" y="196" width="420" height="18" fill="#cfc9bd"/>
<path d="M130 196V120L300 40L470 120V196" fill="none" stroke="#f5f3ee" stroke-width="3" stroke-linejoin="round"/>
<g fill="none" stroke="#f5f3ee" stroke-width="2"><rect x="160" y="132" width="56" height="42"/><path d="M188 132v42M160 153h56"/><rect x="266" y="128" width="56" height="68"/><rect x="408" y="132" width="42" height="42"/></g>
<path d="M362 196l7-15-9-12 9-14-5-10" fill="none" stroke="#ea8349" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<g stroke="#f5f3ee" stroke-opacity=".7" fill="none"><path d="M160 346H300M160 338v16M300 338v16"/></g>
<g fill="#f5f3ee">
<text x="22" y="176">SLAB-ON-GRADE</text>
<text x="22" y="250" fill="#58bba9">SUPPLY LINE</text>
<text x="230" y="340" text-anchor="middle">PIER SPACING</text>
<text x="176" y="304">PIER</text>
<text x="368" y="150" fill="#ea8349">CRACK</text>
<text x="462" y="232">WASHED-OUT SOIL</text>
<text x="462" y="304" fill="#58bba9">LEAK</text>
<text x="22" y="398" fill-opacity=".7">GUMBO CLAY</text>
</g>
<path d="M60 182L100 205" stroke="#f5f3ee" stroke-opacity=".7"/>
</svg>'''

def head(title, desc):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow, noarchive, nosnippet">
<meta name="theme-color" content="#14181a">
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&family=IBM+Plex+Mono:wght@400;500&family=Instrument+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/styles.css">
</head>
<body>
<div class="preview-bar"><strong>Design preview concept</strong> prepared exclusively for B&amp;B Big Boss Foundation Repair &amp; Plumbing. Not an active public website.</div>
'''

NAV = [("/", "Home"), ("/foundation-repair.html", "Foundation Repair"), ("/plumbing.html", "Plumbing"),
       ("/about.html", "About"), ("/contact.html", "Contact")]

def header(active):
    links = "".join(
        '<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if h == active else "", t) for h, t in NAV)
    return f'''<header class="site-header"><div class="wrap nav-row">
<a class="brand" href="/" aria-label="B&amp;B Big Boss home">{LOGO}<span class="brand-text"><b>B&amp;B BIG BOSS</b><small>Foundation Repair &amp; Plumbing</small></span></a>
<button class="menu-toggle" aria-label="Menu" aria-expanded="false"><span></span></button>
<nav class="nav" aria-label="Main">{links}<a class="btn" href="tel:{TEL}">{I["phone"]} {PHONE}</a></nav>
</div></header>
'''

def img(src, w, h, alt="", cls="", lazy=True):
    return f'<img src="/img/{src}" width="{w}" height="{h}" alt="{alt}"{f" class=\"{cls}\"" if cls else ""}{" loading=\"lazy\"" if lazy else ""}>'

def form(p="f"):
    return f'''<form class="form-card" data-demo>
<span class="demo-tag">DEMO FORM &middot; NOTHING IS SENT</span>
<h3>Request an inspection</h3>
<p style="color:var(--muted);margin-bottom:1.3rem">Tell us what you are seeing. We will call you back to set a time.</p>
<div class="fields">
<div class="field"><label for="{p}-n">Name</label><input id="{p}-n" name="name" required autocomplete="name"></div>
<div class="field"><label for="{p}-p">Phone</label><input id="{p}-p" name="phone" type="tel" required autocomplete="tel"></div>
<div class="field"><label for="{p}-e">Email</label><input id="{p}-e" name="email" type="email" autocomplete="email"></div>
<div class="field"><label for="{p}-z">ZIP code</label><input id="{p}-z" name="zip" inputmode="numeric" autocomplete="postal-code"></div>
<div class="field full"><label for="{p}-s">What do you need?</label>
<select id="{p}-s" name="service"><option>Foundation repair</option><option>Plumbing</option><option>Both, or not sure</option><option>Commercial property</option></select></div>
<div class="field full"><label for="{p}-m">What are you noticing?</label><textarea id="{p}-m" name="message" placeholder="Cracks, sticking doors, a leak, a high water bill..."></textarea></div>
</div>
<button class="btn" type="submit">Send request {I["arrow"]}</button>
<p class="form-note">Preview only. Submitting shows a message and sends nothing.</p>
</form>'''

def cta(h2="Seeing cracks or hearing water? Start with a call."):
    return f'''<section class="cta dark sec" id="quote">{img("slab-walk.jpg",1400,935,"")}
<div class="wrap cta-grid">
<div><div class="eyebrow">Get in touch</div><h2>{h2}</h2>
<p class="lead">Foundation movement and plumbing leaks are often connected. Describe what you see and the right person will call you back.</p>
<div class="contact-lines">
<a href="tel:{TEL}"><span class="ic">{I["phone"]}</span><span><small>Call</small><b>{PHONE}</b></span></a>
<div><span class="ic">{I["pin"]}</span><span><small>Based in</small><b>Houston, Texas</b></span></div>
<div><span class="ic">{I["clock"]}</span><span><small>Hours listed online</small><b>Mon to Fri 8am to 5pm<br>Sat and Sun 9am to 5pm</b></span></div>
</div></div>
<div>{form("q")}</div>
</div></section>
'''

def faq(items):
    return '<div class="faq">' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items) + "</div>"

def faq_section(items, title="Things people ask before they call", cls=""):
    return f'''<section class="sec {cls}" id="faq"><div class="wrap faq-wrap">
<div class="sticky"><div class="eyebrow">Questions</div><h2>{title}</h2>
<p class="lead" style="margin-bottom:1.6rem">Not on the list? Call and ask.</p><a class="btn btn-ink" href="tel:{TEL}">{I["phone"]} {PHONE}</a></div>
{faq(items)}
</div></section>
'''

def footer():
    return f'''<footer class="site-footer"><div class="wrap">
<div class="foot-grid">
<div><a class="brand" href="/">{LOGO}<span class="brand-text"><b>B&amp;B BIG BOSS</b><small>Foundation Repair &amp; Plumbing</small></span></a>
<p style="margin-top:1.2rem;max-width:34ch">Foundation repair and plumbing for homes and commercial properties in Houston, Texas.</p></div>
<div><h4>Pages</h4><ul><li><a href="/foundation-repair.html">Foundation repair</a></li><li><a href="/plumbing.html">Plumbing</a></li><li><a href="/about.html">About</a></li><li><a href="/contact.html">Contact</a></li></ul></div>
<div><h4>Work</h4><ul><li>Slab and pier foundations</li><li>Leak detection</li><li>Drain and sewer lines</li><li>Commercial plumbing</li></ul></div>
<div><h4>Contact</h4><ul><li><a href="tel:{TEL}">{PHONE}</a></li><li>Houston, Texas</li><li>BBB Accredited since 2023</li></ul></div>
</div>
<div class="foot-bottom"><span>&copy; 2026 B&amp;B Big Boss Foundation Repair &amp; Plumbing. Design preview concept, not an active public website.</span><span>Placeholder photos from Pexels (free licence). Real job-site photos replace them at launch.</span></div>
</div></footer>
<div class="call-bar"><a class="btn" href="tel:{TEL}">{I["phone"]} Call now</a><a class="btn btn-line" href="/contact.html#quote">Request visit</a></div>
<script src="/assets/script.js" defer></script>
</body>
</html>
'''

def page(active, title, desc, body):
    return head(title, desc) + header(active) + "<main>" + body + "</main>" + footer()

# ------------------------------------------------------------------ HOME
home_faq = [
 ("How do I know if my foundation needs repair?",
  "Look for cracks in drywall, brick or the slab, doors and windows that stick, floors that slope, and gaps where walls meet ceilings or trim. One sign on its own can have other causes. Several together deserve a proper inspection."),
 ("Can a plumbing leak damage my foundation?",
  "Yes. A leak under or beside a slab keeps the soil wet and can wash it away, and soil that moves lets the slab move with it. It also works the other way: a shifting foundation can bend or crack the pipes that run through it."),
 ("Do you handle both foundation and plumbing?",
  "Yes. That is the point of the company. Houston homes tend to have both problems at once, so one team looks at the slab and the pipes together."),
 ("Do you work on commercial properties?",
  "Yes. B&amp;B Big Boss is listed for residential and commercial work, including commercial plumbing."),
 ("How much does foundation repair cost?",
  "It depends on what is causing the movement, how much of the structure is affected and how hard it is to reach. We will not guess over the phone. After someone has looked at it, you get a clear scope and a price."),
 ("How quickly can someone come out?",
  "Call (832) 659-7540 or send the form and we will set a time that suits you."),
 ("What should I do before I call?",
  "Take photos of the cracks or damage, note when you first saw them, and check your recent water bills for a jump. It helps us understand the problem before we arrive."),
 ("Is the work guaranteed?",
  "Ask us about warranty terms when you call. We would rather give you the exact terms in writing than a slogan."),
]

signs = [
 ("Cracks in walls, brick or the slab", "Stair-step cracks in brick and hairline cracks above doors are the usual first ones.", "Foundation", ""),
 ("Doors and windows that stick", "They closed fine last year and now rub or will not latch. The frame has probably moved.", "Foundation", ""),
 ("Floors that slope or bounce", "You can feel it in your feet, or see it where furniture sits crooked.", "Foundation", ""),
 ("Gaps at walls, trim and ceilings", "Space opening up between walls, cabinets, door frames or crown moulding.", "Foundation", ""),
 ("A water bill that jumped", "No change in how you live, but the bill went up. A hidden leak is a common cause.", "Plumbing", "pa"),
 ("Damp spots, a musty smell, a warm patch", "A wet patch, a musty smell or a hot spot on the floor can come from a line you cannot see.", "Plumbing", "pa"),
]
signs_html = "".join(
    f'<li class="sign"><h3>{t}</h3><p>{d}</p><span class="pill {c}">{tr}</span></li>' for t, d, tr, c in signs)

home = f'''
<section class="hero">{img("hero-slab.jpg",1800,1440,"Workers on a reinforced concrete slab foundation before the pour","hero-img",lazy=False)}
<div class="wrap">
<div class="hero-main">
<div class="eyebrow">B&amp;B Big Boss &middot; Houston, TX &middot; Foundation + plumbing</div>
<h1>Level ground.<br><span class="pa">Dry</span> <span class="cu">pipes.</span></h1>
<p class="lead">B&amp;B Big Boss repairs foundations and plumbing for Houston homes and commercial properties. When the slab moves and the pipes leak, one team looks at both.</p>
<div class="btn-row"><a class="btn" href="#quote">Request an inspection {I["arrow"]}</a><a class="btn btn-line" href="tel:{TEL}">{I["phone"]} {PHONE}</a></div>
</div>
<div class="level" aria-label="Interactive spirit level">
<div class="vial-wrap"><div class="vial"><span class="tick t1"></span><span class="tick t2"></span><span class="bubble"></span></div>
<span class="vial-hint">Move your pointer across the hero to tilt it</span></div>
<div class="readout"><small>SLAB ANGLE</small><b data-angle>0.00&deg;</b><em>LEVEL</em></div>
</div>
</div></section>

<section class="ledger"><div class="wrap ledger-grid">
<div class="ledger-item"><small>Google reviews</small><b>5.0 from 21</b></div>
<div class="ledger-item"><small>Better Business Bureau</small><b>Accredited, March 2023</b></div>
<div class="ledger-item"><small>In business</small><b>Houston, since 2022</b></div>
<div class="ledger-item"><small>Properties</small><b>Homes and commercial</b></div>
</div></section>

<section class="sec" id="trades"><div class="wrap">
<div class="sec-head"><div class="eyebrow">What we do</div><h2>Two trades, one phone call</h2>
<p class="lead">Most companies do one or the other. We do both, so the person who finds the problem can also fix it.</p></div>
<div class="trades">
<a class="trade" href="/foundation-repair.html">{img("slab-rebar.jpg",1200,960,"Steel reinforcement and workers on a foundation slab")}
<div class="trade-body"><span class="tag">Foundation</span><h3>Foundation repair</h3><p>For homes and buildings that are cracking, sinking or going out of level.</p>
<ul><li>Slab repair and leveling</li><li>Pier and beam</li><li>Crack and settlement diagnosis</li><li>Drainage</li></ul><span class="go">Foundation details {I["arrow"]}</span></div></a>
<a class="trade" href="/plumbing.html">{img("pipe-hands.jpg",1400,933,"Hands fitting a metal pipe joint")}
<div class="trade-body"><span class="tag pa">Plumbing</span><h3>Plumbing</h3><p>For leaks, clogs and failing lines, in houses and in commercial buildings.</p>
<ul><li>Leak detection</li><li>Slab leaks</li><li>Drain and sewer lines</li><li>Water heaters</li><li>Commercial</li></ul><span class="go">Plumbing details {I["arrow"]}</span></div></a>
</div>
<p class="note">// Service list shows typical scope for these trades. The owner confirms it before launch.</p>
</div></section>

<section class="sec dark" id="why"><div class="wrap why">
<div><div class="eyebrow">Why both under one roof</div><h2>The slab and the pipes are one problem</h2>
<p>Houston sits on clay that locals call gumbo. It swells when it is wet and shrinks when it dries. Anything that changes the moisture under a house, a leaking pipe included, changes how the slab sits.</p>
<ul class="chain">
<li><span class="ar">&rarr;</span><div><b>A leak can start a foundation problem</b><span>Water under a slab softens soil and carries it away. The slab loses support and settles.</span></div></li>
<li><span class="ar">&rarr;</span><div><b>Foundation movement can break pipes</b><span>When a slab shifts, the lines running through it bend and crack, and a new leak begins.</span></div></li>
<li><span class="ar">&rarr;</span><div><b>Fixing only one can leave the other</b><span>Lifting a slab without checking the plumbing, or patching a pipe without checking the slab, can mean paying twice.</span></div></li>
</ul></div>
<figure class="drawing" style="margin:0">{SECTION_ART}<figcaption><span>Section, not to scale</span><span>Slab-on-grade</span></figcaption></figure>
</div></section>

<section class="sec" id="signs"><div class="wrap signs">
<figure class="photo" style="margin:0">{img("crack.jpg",1000,1333,"Cracked concrete surface")}<figcaption>Placeholder photo</figcaption></figure>
<div><div class="eyebrow">Warning signs</div><h2>Read your house</h2>
<p class="lead" style="margin-bottom:2rem">You do not need to know what is wrong. If you see any of these, a quick look beats waiting. The tag shows which trade usually deals with it.</p>
<ul class="sign-list" style="margin:0;padding:0;list-style:none">{signs_html}</ul>
<div class="callout"><span class="marble"></span><p><b>The marble test.</b> Set a marble or a ball on a hard floor. If it keeps rolling the same way, the floor is out of level. It is a rough check, but it tells you whether to call.</p></div>
</div></div></section>

<section class="sec band-photo" id="houston">{img("houston-heights.jpg",1500,1000,"Houston Heights neighborhood houses")}
<div class="wrap"><div class="copy"><div class="eyebrow">Houston, Texas</div><h2>Built for ground that moves</h2>
<p>Dry summers, heavy rain and clay soil mean Houston houses move more than most. We work on that ground every day, on homes and on commercial buildings.</p>
<div class="area"><small>Service area</small><b>Houston, Texas and the surrounding area</b><small>Full list confirmed at launch</small></div></div></div></section>

<section class="sec" id="reviews"><div class="wrap rev">
<div><div class="eyebrow">What customers say</div>
<div class="big-score">5.0<sup>/5</sup></div>
<div class="stars">{I["star"]*5}</div><div class="rev-meta">21 Google reviews</div></div>
<div><h2>Honest, fair, hard-working</h2>
<ul class="theme-list"><li>Professional</li><li>Honest advice</li><li>Reasonable pricing</li><li>Hard-working crew</li><li>Would recommend</li></ul>
<div class="say">
<blockquote><span class="q">&ldquo;</span><div><p>One reviewer had both their plumbing and their foundation repaired in three days.</p><cite>Paraphrased from a Google review</cite></div></blockquote>
<blockquote><span class="q">&ldquo;</span><div><p>Another said the owner was friendly and took real care of their parents.</p><cite>Paraphrased from a Google review</cite></div></blockquote>
<blockquote><span class="q">&ldquo;</span><div><p>Reviews in English and in Spanish both praise the company for being honest and responsible.</p><cite>Paraphrased from Google reviews</cite></div></blockquote>
</div>
<p class="note">// Rating and count as listed on public review sites. Real quotes are added with permission at launch.</p></div>
</div></section>

<div class="wrap"><div class="ruler"></div></div>

<section class="sec" id="process"><div class="wrap">
<div class="sec-head"><div class="eyebrow">How a job runs</div><h2>From first call to finished repair</h2></div>
<div class="steps">
<div class="step"><span class="n">Step 1</span><h3>You call or send the form</h3><p>Tell us what you see. Photos help.</p></div>
<div class="step"><span class="n">Step 2</span><h3>We look at the whole picture</h3><p>Foundation and plumbing checked together, on site.</p></div>
<div class="step"><span class="n">Step 3</span><h3>You get a scope and a price</h3><p>What needs fixing, what can wait, and what it costs.</p></div>
<div class="step"><span class="n">Step 4</span><h3>We repair and walk you through it</h3><p>Finished work, explained, with your questions answered.</p></div>
</div>
<p class="note">// Typical process shown for the preview. The owner confirms the exact steps before launch.</p>
</div></section>

{faq_section(home_faq)}

{cta()}
'''

# ------------------------------------------------------------------ FOUNDATION
f_faq = [
 ("What causes foundation problems in Houston?",
  "Mostly the soil. Clay swells when it is wet and shrinks when it is dry, so the ground under a house keeps moving a little. Poor drainage, big trees close to the house and plumbing leaks make it worse."),
 ("What is the difference between slab and pier and beam?",
  "A slab foundation is a single concrete pad poured on the ground. A pier and beam foundation lifts the house on short posts with a crawl space underneath. They fail in different ways and are repaired in different ways."),
 ("Are all cracks serious?",
  "No. Hairline cracks are common in concrete and brick. What matters is the pattern: cracks that keep growing, run diagonally from corners, or show up together with sticking doors and sloping floors."),
 ("Should I fix the foundation or the plumbing first?",
  "Check both before you decide. If a leak is feeding the problem, lifting the slab first can fail. That is why one team looks at both."),
 ("Do I need to leave the house during the work?",
  "It depends on the job. Ask when you book and we will tell you what to expect."),
 ("Can you look at a commercial building?",
  "Yes. Send the address and a short description through the form or call us."),
]
f_body = f'''
<section class="page-hero">{img("slab-walk.jpg",1400,935,"Worker walking across a concrete slab","",lazy=False)}
<div class="wrap"><div class="crumbs"><a href="/">Home</a> / Foundation repair</div>
<div class="eyebrow">Foundation repair</div><h1>Foundation repair in Houston</h1>
<p class="lead">Cracks, sticking doors and sloping floors usually mean a foundation that is moving. We find out why, fix it, and check the plumbing while we are there.</p>
<div class="btn-row"><a class="btn" href="#quote">Request an inspection {I["arrow"]}</a><a class="btn btn-line" href="tel:{TEL}">{I["phone"]} {PHONE}</a></div></div></section>

<section class="sec"><div class="wrap signs">
<figure class="photo" style="margin:0">{img("crack.jpg",1000,1333,"Cracked concrete surface")}<figcaption>Placeholder photo</figcaption></figure>
<div><div class="eyebrow">Signs to watch for</div><h2>How a moving foundation shows up</h2>
<ul class="sign-list" style="margin:2rem 0 0;padding:0;list-style:none">{"".join(f'<li class="sign"><h3>{t}</h3><p>{d}</p><span class="pill">{tr}</span></li>' for t, d, tr, c in signs[:4])}</ul></div>
</div></section>

<section class="sec dark"><div class="wrap duo">
<div><div class="eyebrow">What we work on</div><h2>Slab, pier and beam, and the ground around them</h2>
<ul class="ticks"><li>Slab foundation repair and leveling</li><li>Pier and beam foundation repair</li><li>Diagnosing cracks, gaps and settlement</li><li>Drainage that keeps water away from the foundation</li><li>Foundation checks on commercial buildings</li></ul>
<p class="note">// Typical scope for the trade, confirmed with the owner before launch.</p>
<div class="btn-row"><a class="btn" href="#quote">Book an inspection</a></div></div>
<figure class="photo" style="margin:0">{img("slab-rebar.jpg",1200,960,"Steel reinforcement on a foundation slab")}<figcaption>Placeholder photo</figcaption></figure>
</div></section>

<section class="sec"><div class="wrap duo">
<figure class="drawing" style="margin:0;background-color:var(--ink)">{SECTION_ART}<figcaption><span>Section, not to scale</span><span>Slab-on-grade</span></figcaption></figure>
<div><div class="eyebrow">The plumbing connection</div><h2>We check the pipes while we are under there</h2>
<p class="lead">A slab that is settling because of a leak keeps settling after it is lifted if the leak is still there. Looking at the plumbing at the same time is part of doing the foundation job properly.</p>
<div class="btn-row"><a class="btn btn-ink" href="/plumbing.html">See the plumbing side {I["arrow"]}</a></div></div>
</div></section>

{faq_section(f_faq, "Foundation repair questions")}
{cta("Cracks or sloping floors? Let someone look.")}
'''

# ------------------------------------------------------------------ PLUMBING
p_faq = [
 ("What is a slab leak?",
  "A leak in a water line that runs in or under the concrete slab. You cannot see it, so the first signs are usually a high water bill, the sound of running water when everything is off, or a warm spot on the floor."),
 ("How do I check for a hidden leak?",
  "Turn off every tap and appliance, then look at your water meter. If it is still moving, water is going somewhere. Call us and we will track it down."),
 ("Do you repair drain and sewer lines?",
  "Yes. Drain and sewer line repair is part of the plumbing work, for homes and commercial properties."),
 ("Can you handle commercial plumbing?",
  "Yes. B&amp;B Big Boss is listed with the BBB as a commercial plumber as well as a residential one."),
 ("What if I need plumbing and foundation work?",
  "They are planned together, so you are not scheduling two companies."),
 ("Who do I call for an active leak?",
  "Call (832) 659-7540. If water is running and you cannot stop it, shut off the main valve first, then call."),
]
p_work = [
 ("Leak detection and repair", "Finding where water is going, then stopping it.", ""),
 ("Slab leak repair", "Lines under the concrete, handled with the foundation team.", ""),
 ("Drain and sewer lines", "Clogs, backups and damaged lines.", ""),
 ("Water heaters", "Repair and replacement.", ""),
 ("Fixtures and repairs", "Faucets, toilets, valves and supply lines.", ""),
 ("Commercial plumbing", "Plumbing work for businesses and commercial properties.", ""),
]
p_work_html = "".join(f'<li class="sign"><h3>{t}</h3><p>{d}</p><span class="pill pa">Plumbing</span></li>' for t, d, _ in p_work)
p_body = f'''
<section class="page-hero">{img("pipe-hands.jpg",1400,933,"Hands fitting a metal pipe","",lazy=False)}
<div class="wrap"><div class="crumbs"><a href="/">Home</a> / Plumbing</div>
<div class="eyebrow">Plumbing</div><h1>Plumbing in Houston</h1>
<p class="lead">Leaks, slow drains, old water heaters and broken lines, for homes and commercial properties. We also know when a plumbing problem is really a foundation problem.</p>
<div class="btn-row"><a class="btn" href="#quote">Request a visit {I["arrow"]}</a><a class="btn btn-line" href="tel:{TEL}">{I["phone"]} {PHONE}</a></div></div></section>

<section class="sec"><div class="wrap signs">
<figure class="photo" style="margin:0">{img("pipes-wall.jpg",1000,1333,"Grey plumbing pipes on a wall")}<figcaption>Placeholder photo</figcaption></figure>
<div><div class="eyebrow">What we fix</div><h2>Plumbing work we take on</h2>
<ul class="sign-list" style="margin:2rem 0 0;padding:0;list-style:none">{p_work_html}</ul>
<p class="note">// Typical scope for the trade, confirmed with the owner before launch.</p></div>
</div></section>

<section class="sec dark"><div class="wrap duo">
<div><div class="eyebrow">Signs of a hidden leak</div><h2>What your house tells you</h2>
<ul class="ticks"><li>A water bill that jumped for no clear reason</li><li>A water meter that moves when everything is off</li><li>The sound of running water in a quiet house</li><li>Damp or warm spots on the floor</li><li>A musty smell or mold near walls</li></ul>
<div class="btn-row"><a class="btn" href="tel:{TEL}">{I["phone"]} Call {PHONE}</a></div></div>
<figure class="photo" style="margin:0">{img("boiler.jpg",1200,800,"Hands adjusting a heating unit")}<figcaption>Placeholder photo</figcaption></figure>
</div></section>

<section class="sec"><div class="wrap duo">
<div><div class="eyebrow">The foundation connection</div><h2>A leak is not always only a plumbing problem</h2>
<p class="lead">Water under a slab can soften the soil and let the foundation settle. When we fix a leak we also look at what it may have done to the structure above it.</p>
<div class="btn-row"><a class="btn btn-ink" href="/foundation-repair.html">See the foundation side {I["arrow"]}</a></div></div>
<figure class="drawing" style="margin:0;background-color:var(--ink)">{SECTION_ART}<figcaption><span>Section, not to scale</span><span>Slab-on-grade</span></figcaption></figure>
</div></section>

{faq_section(p_faq, "Plumbing questions")}
{cta("Think you have a leak? Call before it grows.")}
'''

# ------------------------------------------------------------------ ABOUT
about = f'''
<section class="page-hero">{img("houston-skyline.jpg",1600,1067,"Houston skyline","",lazy=False)}
<div class="wrap"><div class="crumbs"><a href="/">Home</a> / About</div>
<div class="eyebrow">About</div><h1>A Houston crew that does both jobs</h1>
<p class="lead">B&amp;B Big Boss Foundation Repair &amp; Plumbing started in March 2022 and handles both trades, because the slab and the pipes are so often part of the same problem.</p></div></section>

<section class="sec"><div class="wrap duo">
<figure class="photo" style="margin:0">{img("houston-home.jpg",1200,900,"House with large trees in Houston")}<figcaption>Placeholder photo</figcaption></figure>
<div><div class="eyebrow">Why both trades</div><h2>One team for the slab and the pipes</h2>
<p>In Houston, homes sit on soil that moves, and the pipes run through the same slab that holds the house up. When something goes wrong with one, the other is often involved. Calling two companies means two visits, two opinions and sometimes two bills for the same root problem.</p>
<p>B&amp;B Big Boss offers both trades. One team looks at the foundation and the plumbing together, explains what it found, and fixes what needs fixing.</p>
<p>The company works on homes and on commercial properties, and has been a BBB Accredited Business since March 2023. Reviewers on Google describe the team as professional, honest, reasonably priced and hard-working.</p>
<div class="facts"><div class="fact"><b>Mar 2022</b><span>Business started</span></div><div class="fact"><b>Mar 2023</b><span>BBB Accredited</span></div><div class="fact"><b>5.0 / 21</b><span>Google rating</span></div></div></div>
</div></section>

<section class="sec dark"><div class="wrap">
<div class="sec-head"><div class="eyebrow">How we work</div><h2>What you can expect</h2></div>
<ul class="chain" style="margin:0;max-width:760px">
<li><span class="ar">&rarr;</span><div><b>Straight answers</b><span>We tell you what is wrong, what is urgent and what can wait.</span></div></li>
<li><span class="ar">&rarr;</span><div><b>Clear pricing</b><span>You see the scope and the price before work starts.</span></div></li>
<li><span class="ar">&rarr;</span><div><b>Work done properly</b><span>Foundation and plumbing checked together so the fix lasts.</span></div></li>
</ul></div></section>

{cta("Want to talk to the team?")}
'''

# ------------------------------------------------------------------ CONTACT
contact = f'''
<section class="page-hero">{img("houston-heights.jpg",1500,1000,"Houston Heights houses","",lazy=False)}
<div class="wrap"><div class="crumbs"><a href="/">Home</a> / Contact</div>
<div class="eyebrow">Contact</div><h1>Talk to B&amp;B Big Boss</h1>
<p class="lead">Call, or send the form and we will call you back.</p></div></section>

<section class="cta dark sec" id="quote"><div class="wrap cta-grid">
<div><h2>Reach us</h2>
<div class="contact-lines">
<a href="tel:{TEL}"><span class="ic">{I["phone"]}</span><span><small>Call</small><b>{PHONE}</b></span></a>
<div><span class="ic">{I["pin"]}</span><span><small>Based in</small><b>Houston, Texas</b></span></div>
</div>
<h3 style="margin-top:2.6rem;font-size:1.1rem">Hours listed online</h3>
<table class="hours"><tr><td>Monday to Friday</td><td>8:00 am to 5:00 pm</td></tr><tr><td>Saturday and Sunday</td><td>9:00 am to 5:00 pm</td></tr></table>
<p class="note">// Hours as shown on a public business listing. Confirmed with the owner at launch.</p></div>
<div>{form("c")}</div>
</div></section>
'''

nf = f'''
<section class="page-hero"><div class="wrap"><div class="eyebrow">404</div><h1>Off level</h1>
<p class="lead">That page is not here. It may have moved, or the link is wrong.</p><div class="btn-row"><a class="btn" href="/">Back to the home page</a></div></div></section>
'''

FAVICON = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 40"><rect x="1" y="5" width="62" height="30" rx="15" fill="#d0662a"/><rect x="7" y="11" width="50" height="18" rx="9" fill="#14181a"/><ellipse cx="32" cy="20" rx="11" ry="5.2" fill="#58bba9"/></svg>'''

PAGES = [
 ("index.html", "/", "Big Boss Foundation Repair & Plumbing | Design Preview",
  "Design preview concept for B&B Big Boss Foundation Repair & Plumbing in Houston, Texas.", home),
 ("foundation-repair.html", "/foundation-repair.html", "Foundation Repair Houston | Design Preview",
  "Design preview of the foundation repair page for B&B Big Boss in Houston, TX.", f_body),
 ("plumbing.html", "/plumbing.html", "Plumbing Houston | Design Preview",
  "Design preview of the plumbing page for B&B Big Boss in Houston, TX.", p_body),
 ("about.html", "/about.html", "About Big Boss | Design Preview",
  "Design preview of the about page for B&B Big Boss Foundation Repair & Plumbing.", about),
 ("contact.html", "/contact.html", "Contact Big Boss | Design Preview",
  "Design preview of the contact page for B&B Big Boss Foundation Repair & Plumbing.", contact),
 ("404.html", "/404.html", "Page not found | Design Preview", "Page not found.", nf),
]

def main():
    OUT.mkdir(exist_ok=True)
    for fn, path, title, desc, body in PAGES:
        (OUT / fn).write_text(page(path, title.replace("&", "&amp;"), desc.replace("&", "&amp;"), body), encoding="utf-8")
    (OUT / "assets" / "favicon.svg").write_text(FAVICON, encoding="utf-8")
    (OUT / "robots.txt").write_text("User-agent: *\nDisallow: /\n", encoding="utf-8")
    print("built", len(PAGES), "pages")

if __name__ == "__main__":
    main()
