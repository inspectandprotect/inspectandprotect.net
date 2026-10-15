import json, os, shutil, sys, datetime
sys.path.insert(0, os.path.dirname(__file__))
from content import *

OUT = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/inspectandprotect-site"
TODAY = datetime.date.today().isoformat()
PAGES = []  # for sitemap
PATH2GROUP = {}  # path -> {lang: path} for hreflang + language switcher
LANG_ROOTS = {"en": "/", "es": "/es/", "ht": "/ht/"}

def set_groups(groups):
    for g in groups:
        for p in g.values():
            PATH2GROUP[p] = g

def lang_switch(path, lang):
    g = PATH2GROUP.get(path, {})
    out = []
    for l, label in (("en", "EN"), ("es", "ES"), ("ht", "KREYÒL")):
        href = g.get(l, LANG_ROOTS[l])
        cur = ' aria-current="true"' if l == lang else ""
        out.append(f'<a href="{href}" hreflang="{l}" lang="{l}"{cur}>{label}</a>')
    return '<nav class="langs" aria-label="Language">' + "".join(out) + "</nav>"

def topbar(path, lang, call_label):
    return f'<div class="topbar"><div class="wrap"><span>{call_label} <a href="tel:{PHONE_TEL}">{PHONE}</a></span>{lang_switch(path, lang)}</div></div>'

def esc_attr(s):
    return s.replace('"', "&quot;")

def strip_tags(s):
    import re
    return re.sub(r"<[^>]+>", "", s).replace("&amp;", "&")

BUSINESS_LD = {
    "@context": "https://schema.org",
    "@type": "HomeAndConstructionBusiness",
    "@id": DOMAIN + "/#business",
    "name": "Inspect and Protect",
    "url": DOMAIN + "/",
    "telephone": PHONE_TEL,
    "email": EMAIL,
    "priceRange": "$150–$625+",
    "address": {"@type": "PostalAddress", "addressLocality": "Miami", "addressRegion": "FL", "addressCountry": "US"},
    "areaServed": [{"@type": "City", "name": f"{a[1]}, FL"} for a in AREAS]
                  + [{"@type": "AdministrativeArea", "name": c} for c in ("Miami-Dade County, FL", "Broward County, FL", "Palm Beach County, FL")],
    "openingHoursSpecification": {"@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
        "opens": "08:00", "closes": "18:00"},
    "logo": DOMAIN + "/apple-touch-icon.png",
    "image": DOMAIN + "/assets/brand/og.jpg",
    "founder": {"@type": "Person", "name": "Nicholas Figaro", "jobTitle": "Florida Licensed Home Inspector"},
    "hasCredential": {"@type": "EducationalOccupationalCredential", "credentialCategory": "license",
                      "name": f"Florida Home Inspector License {LICENSE}"},
    "sameAs": [GOOGLE_PROFILE, THUMBTACK_PROFILE, NACHI_PROFILE],
}

def nav_items():
    return [
        ("/services/", "Services"),
        ("/pricing/", "Pricing"),
        ("/services/mold-inspection-testing/", "Mold Testing"),
        ("/areas/", "Areas"),
        ("/reviews/", "Reviews"),
        ("/resources/", "Resources"),
    ]

def header(path="/"):
    links = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in nav_items())
    return f'''<header class="site-header">{topbar(path, "en", "Call or text")}<div class="wrap">
<a class="logo" href="/"><img src="/assets/brand/shield-white.svg" alt="" width="44" height="44"><span class="wm"><span class="w1">INSPECT &amp;</span><span class="w2">PROTECT</span></span></a>
<ul class="nav">{links}<li><a class="btn btn-gold" href="/contact/">Book Now</a></li></ul>
<details class="menu"><summary aria-label="Open menu">Menu</summary><ul>{links}<li><a href="/contact/">Book Now</a></li><li><a href="tel:{PHONE_TEL}">Call {PHONE}</a></li></ul></details>
</div></header>'''

def footer():
    svc = "".join(f'<li><a href="/services/{s["slug"]}/">{s["nav"]}</a></li>' for s in SERVICES)
    areas = "".join(f'<li><a href="/areas/{a[0]}/">{a[1]}</a></li>' for a in AREAS[:8])
    return f'''<footer class="site-footer"><div class="wrap">
<div class="footer-grid">
<div><a class="logo" href="/"><img src="/assets/brand/shield-white.svg" alt="" width="44" height="44"><span class="wm"><span class="w1">INSPECT &amp;</span><span class="w2">PROTECT</span></span></a>
<p>Licensed home inspections, insurance inspections and mold testing across Miami-Dade, Broward and Palm Beach.</p>
<p><a href="tel:{PHONE_TEL}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>{footer_seals()}</div>
<div><h4>Services</h4><ul>{svc}<li><a href="/pricing/">Pricing</a></li></ul></div>
<div><h4>Areas</h4><ul>{areas}<li><a href="/areas/">All areas</a></li></ul></div>
<div><h4>Company</h4><ul><li><a href="/reviews/">Reviews</a></li><li><a href="/sample-reports/">Sample reports</a></li><li><a href="/certifications/">Certifications</a></li><li><a href="/for-realtors/">For realtors</a></li><li><a href="/for-insurance-agents/">For insurance agents</a></li><li><a href="/resources/">Resources</a></li><li><a href="/contact/">Book an inspection</a></li></ul></div>
</div>
<div class="legal">Florida Licensed Home Inspector #{LICENSE} · InterNACHI Certified · Insured. Mold inspection and testing are performed under our Florida home inspector license; we do not perform mold assessments or mold remediation. © {datetime.date.today().year} Inspect and Protect.</div>
</div></footer>'''

def page(path, title, meta, body, extra_ld=None, lang="en", hdr=None, ftr=None):
    """path like '/' or '/services/home-inspection/'"""
    canonical = DOMAIN + path
    g = PATH2GROUP.get(path)
    alt = ""
    if g:
        alt = "".join(f'<link rel="alternate" hreflang="{l}" href="{DOMAIN}{p}">' for l, p in g.items())
        if "en" in g:
            alt += f'<link rel="alternate" hreflang="x-default" href="{DOMAIN}{g["en"]}">'
    head_html = hdr(path) if hdr else header(path)
    foot_html = ftr() if ftr else footer()
    lds = [BUSINESS_LD] + (extra_ld or [])
    ld = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in lds)
    full_title = title if "Inspect" in title else f"{title} | Inspect and Protect"
    html = f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{strip_tags(full_title)}</title>
<meta name="description" content="{esc_attr(strip_tags(meta))}">
<link rel="canonical" href="{canonical}">{alt}
<meta property="og:title" content="{esc_attr(strip_tags(full_title))}">
<meta property="og:description" content="{esc_attr(strip_tags(meta))}">
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="website">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:image" content="{DOMAIN}/assets/brand/og.jpg">
<meta name="theme-color" content="#01172e">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Montserrat:wght@500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
{ld}
<script defer src="/_vercel/insights/script.js"></script>
{SOURCE_JS}
</head>
<body>
{head_html}
<main>
{body}
</main>
{foot_html}
{mobile_bar(lang)}
</body>
</html>'''
    dest = os.path.join(OUT, path.strip("/"), "index.html") if path != "/" else os.path.join(OUT, "index.html")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w") as f:
        f.write(html)
    PAGES.append(path)

def crumbs(items, home="Home", home_href="/"):
    parts = [f'<a href="{home_href}">{home}</a>'] + [f'<a href="{h}">{t}</a>' if h else t for h, t in items]
    return '<nav class="crumbs" aria-label="Breadcrumb">' + " / ".join(parts) + "</nav>"

def breadcrumb_ld(items, home="Home", home_href="/"):
    els = [{"@type": "ListItem", "position": 1, "name": home, "item": DOMAIN + home_href}]
    for i, (h, t) in enumerate(items, start=2):
        el = {"@type": "ListItem", "position": i, "name": strip_tags(t)}
        if h: el["item"] = DOMAIN + h
        els.append(el)
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": els}

def faq_ld(faq):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": strip_tags(q), "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in faq]}

def faq_html(faq):
    return "".join(f'<details class="faq"><summary>{q}</summary><p>{a}</p></details>' for q, a in faq)

def cta_band(text="Ready to book?", sub="Call, text or book online. We confirm within 30 minutes.",
             btn="Book an Inspection", call=None, href="/contact/"):
    call = call or f"Call {PHONE}"
    return f'''<section class="bg-navy on-dark"><div class="wrap">
<h2>{text}</h2><p class="lede">{sub}</p>
<div class="btn-row"><a class="btn btn-gold" href="{href}">{btn}</a><a class="btn btn-line" href="tel:{PHONE_TEL}">{call}</a></div>
</div></section>'''

def cta_strip(text="Ready to book?", sub="Call, text or book online. We confirm within 30 minutes.",
              btn="Book Online", call=None, href="/contact/"):
    call = (call or f"Call or Text {PHONE}").replace(PHONE, f'<span class="nw">{PHONE}</span>')
    return f'''<div class="wrap"><div class="cta-strip">
<div class="cta-strip-text"><strong>{text}</strong><span>{sub}</span></div>
<div class="cta-strip-btns"><a class="btn btn-gold" href="{href}">{btn}</a><a class="btn btn-line" href="tel:{PHONE_TEL}">{call}</a></div>
</div></div>'''

MOBILE_BAR = {"en": ("Book Online", "Call / Text", "/contact/"),
              "es": ("Reservar", "Llamar / Texto", "/es/reservar/"),
              "ht": ("Rezève", "Rele / Tèks", "/ht/rezeve/")}

def mobile_bar(lang="en"):
    book, call, href = MOBILE_BAR.get(lang, MOBILE_BAR["en"])
    return f'<nav class="mobile-bar" aria-label="Book or call"><a class="mb-call" href="tel:{PHONE_TEL}">{call}</a><a class="mb-book" href="{href}">{book}</a></nav>'

def rows(items):
    out = ""
    for it in items:
        if len(it) == 3:
            name, sub, price = it
            out += f'<div class="row"><span>{name}{f"<small>{sub}</small>" if sub else ""}</span><strong>{price}</strong></div>'
        else:
            out += f'<div class="row"><span>{it[0]}</span><strong>{it[1]}</strong></div>'
    return out

def pricing_block():
    pay = "".join(f'<span class="chip">{m}</span>' for m in PAYMENT_METHODS)
    if PAY_OVER_TIME:
        pay = '<span class="chip chip-solid">Afterpay</span><span class="chip chip-solid">Affirm</span>' + pay
        pay_text = "Split your inspection into interest-free payments with Afterpay or Affirm, subject to approval."
    else:
        pay_text = "Pay on the day of your inspection. Your report is released once payment is received."
    return f'''<div class="grid grid-wide">
<div class="card price-card"><h3>Home Inspection</h3><p class="sub">Priced by square footage</p>{rows(HOME_TIERS)}</div>
<div class="card price-card"><h3>Insurance Inspections</h3><p class="sub">Florida forms your insurer accepts</p>{rows(INSURANCE_PRICES)}
<p>Wind mitigation can lower your windstorm premium. A 4-point covers roof, electrical, plumbing and HVAC on older homes.</p></div>
<div class="card price-card feature"><h3>Mold Inspection &amp; Testing</h3><p class="sub">Lab analysis included</p>{rows(ENV_PRICES)}
<p><a href="/services/mold-inspection-testing/">What's included →</a></p></div>
</div>
<div class="paybar"><div style="flex:1 1 320px"><h3>Simple payment</h3><p style="margin:4px 0 0;color:#eef2f6">{pay_text}</p></div><div class="chips">{pay}</div></div>
<p class="note" style="margin-top:12px">Every inspection includes moisture meter and thermal imaging, photos and a full digital report. Travel fee may apply outside Miami-Dade and Broward.</p>'''

def reviews_block():
    return f'''<div class="grid grid-wide">
<a class="rating" href="{GOOGLE_PROFILE}"><strong>{GOOGLE_RATING}</strong><span><b>Google</b><small>{GOOGLE_COUNT} reviews · all five-star · read them on Google</small></span></a>
<a class="rating" href="{THUMBTACK_PROFILE}"><strong>{THUMBTACK_RATING}</strong><span><b>Thumbtack</b><small>{THUMBTACK_COUNT} reviews · Top Pro · read them on Thumbtack</small></span></a>
</div>
{review_feed()}
<div class="btn-row"><a class="btn btn-dark" href="{GOOGLE_REVIEW_LINK}">Leave us a Google review</a></div>'''

def services_cards(exclude=None):
    return '<div class="grid">' + "".join(
        f'<a class="card" href="/services/{s["slug"]}/"><h3>{s["nav"]}</h3><p>{strip_tags(s["lede"])[:140].rsplit(" ",1)[0]}…</p><div class="more">From {s["price_from"]} →</div></a>'
        for s in SERVICES if s["slug"] != exclude) + "</div>"

def city_pills_for(svc):
    """Pills linking to service+city pages where they exist, else the city page."""
    out = []
    for a in AREAS:
        href = sc_path(a[0], svc) if has_sc(a[0], svc) else f"/areas/{a[0]}/"
        out.append(f'<a class="pill" href="{href}">{a[1]}</a>')
    return '<div class="pills">' + "".join(out) + "</div>"

def area_pills():
    return '<div class="pills">' + "".join(f'<a class="pill" href="/areas/{a[0]}/">{a[1]}</a>' for a in AREAS) + "</div>"

# ================================================================ HOME
def build_home():
    mold = next(s for s in SERVICES if s["slug"] == "mold-inspection-testing")
    covers = "".join(f'<div class="card"><h3>{t}</h3><p>{d}</p></div>' for t, d in mold["covers"])
    body = f'''
<section class="hero on-dark"><div class="wrap">
<div class="hero-grid"><div>
<p class="kicker">Florida Licensed Home Inspector · {LICENSE}</p>
<h1>Certified Home Inspections.<br><em>Same-Day Reports.</em></h1>
<p class="lede">Home Inspections, Wind Mitigation, 4-Point Inspections and Mold Testing across Miami-Dade, Broward and Palm Beach, with clear prices up front.</p>
<div class="btn-row"><a class="btn btn-gold" href="/contact/">Schedule Inspection</a><a class="btn btn-line" href="/pricing/">See Our Prices</a></div>
</div></div>
<div class="stats">
<div><strong>5.0 <span class="st">★</span></strong><span>{TOTAL_REVIEWS} reviews · Google + Thumbtack</span></div>
<div><strong>Same-Day</strong><span>Reports with photos</span></div>
<div><strong>Thermal + Moisture</strong><span>On every inspection</span></div>
<div><strong>InterNACHI</strong><span>Certified inspector</span></div>
</div></div></section>

<section class="bg-white"><div class="wrap">
<p class="kicker">Services</p><h2>Everything a South Florida home needs inspected</h2>
<div style="margin-top:32px">{services_cards()}</div>
</div>{cta_strip()}</section>
{badge_strip("Certified &amp; verified", f"Florida licensed and InterNACHI certified in {len(CERTS) - 3} inspection specialties", f"See all {len(CERTS)} certifications and verify them")}

<section id="pricing"><div class="wrap">
<p class="kicker">Pricing</p><h2>Straightforward prices. No surprises at the door.</h2>
<div style="margin-top:32px">{pricing_block()}</div>
</div>{cta_strip()}</section>

<section class="bg-white"><div class="wrap">
<p class="kicker">Mold Inspection &amp; Testing</p><h2>We find the moisture first, then test what matters.</h2>
<p class="lede">{strip_tags(mold["lede"])}</p>
<div class="grid" style="margin-top:32px">{covers}</div>
<div class="callout" style="margin-top:28px"><div style="flex:1 1 360px"><h3>We test. We don't sell cleanup.</h3><p style="margin:6px 0 0;color:var(--muted)">We don't do mold removal, so our findings never come with a job attached.</p></div><a class="btn btn-dark" href="/services/mold-inspection-testing/">Mold testing details</a></div>
</div></section>

<section><div class="wrap">
<p class="kicker">Reviews</p><h2>{TOTAL_REVIEWS} five-star reviews and counting</h2>
<div style="margin-top:28px">{reviews_block()}</div>
</div>{cta_strip()}</section>

<section class="bg-white"><div class="wrap">
<p class="kicker">How it works</p><h2>Booked in minutes. Report the same day.</h2>
<ol class="steps" style="margin-top:28px">
<li><b>STEP 1</b><strong>Get your price</strong><p>Prices are listed by square footage, so you know the cost before you call.</p></li>
<li><b>STEP 2</b><strong>Book and sign</strong><p>Pick a time and sign the inspection agreement. Your slot is locked in.</p></li>
<li><b>STEP 3</b><strong>Inspection day</strong><p>You're welcome to attend. We walk you through what we find.</p></li>
<li><b>STEP 4</b><strong>Same-day report</strong><p>Photos, findings and plain-English explanations, delivered that day.</p></li>
</ol>
{sample_callout()}</div></section>

<section><div class="wrap">
<p class="kicker">Areas we serve</p><h2>Miami-Dade, Broward and Palm Beach</h2>
<div style="margin-top:24px">{area_pills()}</div>
<div class="grid" style="margin-top:40px">
<a class="card" href="/for-realtors/"><h3>Real estate agents</h3><p>Fast scheduling, same-day reports and insurance forms in one visit.</p><div class="more">For realtors →</div></a>
<a class="card" href="/for-insurance-agents/"><h3>Insurance agents</h3><p>Current-revision wind mits and 4-points with photos for every answer.</p><div class="more">For insurance agents →</div></a>
</div></div></section>

<section class="bg-white"><div class="wrap narrow">
<p class="kicker">FAQ</p><h2>Common questions</h2>
<div style="margin-top:20px">{faq_html(HOME_FAQ)}</div>
</div></section>
{cta_band()}'''
    page("/", "Home Inspector Miami &amp; South Florida | Inspect and Protect",
         f"Licensed Florida home inspector (HI18768) serving Miami-Dade, Broward and Palm Beach. Home inspections from $325, wind mitigation and 4-point $150, mold testing $375. Same-day reports. {TOTAL_REVIEWS} five-star reviews.",
         body, [faq_ld(HOME_FAQ)])

HOME_FAQ = [
    ("How much does a home inspection cost?", "Home inspections start at $325 for condos and homes under 1,200 sq ft and are priced by size. Wind mitigation and 4-point inspections are $150 each. See the full price list on our pricing page."),
    ("How long does a home inspection take?", "Most inspections take 1 to 2 hours depending on the size and condition of the home. You're welcome to attend."),
    ("When will I receive my report?", "Reports and photos are delivered the same day as your inspection."),
    ("What areas do you serve?", "Miami-Dade, Broward and Palm Beach counties. Call for availability elsewhere in Florida."),
    ("Are you licensed and insured?", f"Yes. We're a Florida licensed home inspector (#{LICENSE}), InterNACHI certified, and carry errors and omissions and general liability insurance."),
]

# ================================================================ SERVICES
def build_services():
    body = f'''<section class="page-hero on-dark"><div class="wrap">{crumbs([(None,"Services")])}
<h1>Inspection services</h1><p class="lede">Home inspections, insurance inspections and mold testing for Miami-Dade, Broward and Palm Beach homes.</p></div></section>
<section class="bg-white"><div class="wrap">{services_cards()}</div></section>{cta_band()}'''
    page("/services/", "Home Inspection Services – Miami &amp; South Florida",
         "Home inspections, wind mitigation, 4-point, mold inspection and testing, pre-listing and new construction inspections in South Florida.", body,
         [breadcrumb_ld([("/services/", "Services")])])
    for s in SERVICES:
        covers = "".join(f'<div class="card"><h3>{t}</h3><p>{d}</p></div>' for t, d in s["covers"])
        paras = "".join(f"<p>{p}</p>" for p in s["body"])
        note = f'<p class="note">{s["note"]}</p>' if s.get("note") else ""
        faq = f'<section><div class="wrap narrow"><h2>Questions</h2><div style="margin-top:16px">{faq_html(s["faq"])}</div></div></section>' if s["faq"] else ""
        related = "".join(f'<a class="card" href="/resources/{a["slug"]}/"><h3>{a["title"]}</h3><p>{a["summary"]}</p></a>' for a in ARTICLES if a["cta_service"] == s["slug"])
        related = f'<h3 style="margin:40px 0 16px">Learn more</h3><div class="grid">{related}</div>' if related else ""
        body = f'''<section class="page-hero on-dark"><div class="wrap">{crumbs([("/services/","Services"),(None,s["nav"])])}
<p class="kicker">{s["kicker"]}</p><h1>{s["h1"]}</h1><p class="lede">{s["lede"]}</p>
<div class="btn-row"><a class="btn btn-gold" href="/contact/">Book · from {s["price_from"]}</a><a class="btn btn-line" href="/pricing/">Full price list</a></div></div></section>
<section class="bg-white"><div class="wrap"><h2>What we check</h2><div class="grid" style="margin-top:28px">{covers}</div></div></section>
<section><div class="wrap narrow prose">{paras}{note}{sample_callout() if s["slug"] in SAMPLE_SERVICES else ""}{related}</div></section>
{faq}
<section class="bg-white"><div class="wrap"><h2>Areas we serve</h2><div style="margin-top:20px">{city_pills_for(s["slug"])}</div>
<h2 style="margin-top:48px">Other services</h2><div style="margin-top:24px">{services_cards(exclude=s["slug"])}</div></div></section>
{cta_band()}'''
        price_num = s["price_from"].replace("$", "")
        svc_ld = {"@context": "https://schema.org", "@type": "Service", "name": strip_tags(s["nav"]),
                  "provider": {"@id": DOMAIN + "/#business"}, "areaServed": ["Miami-Dade County, FL", "Broward County, FL", "Palm Beach County, FL"],
                  "offers": {"@type": "Offer", "price": price_num, "priceCurrency": "USD"}}
        lds = [svc_ld, breadcrumb_ld([("/services/", "Services"), (None, s["nav"])])]
        if s["faq"]: lds.append(faq_ld(s["faq"]))
        page(f'/services/{s["slug"]}/', s["title"], s["meta"], body, lds)

# ================================================================ PRICING / REVIEWS / CONTACT
def build_pricing():
    body = f'''<section class="page-hero on-dark"><div class="wrap">{crumbs([(None,"Pricing")])}
<h1>Inspection prices</h1><p class="lede">Clear prices before you book. No hidden fees.</p></div></section>
<section class="bg-white"><div class="wrap">{pricing_block()}</div></section>
<section><div class="wrap narrow"><h2>Pricing questions</h2><div style="margin-top:16px">{faq_html(PRICING_FAQ)}</div></div></section>{cta_band()}'''
    page("/pricing/", "Home Inspection Prices – Miami, Broward &amp; Palm Beach",
         "Home inspection prices by square footage from $325. Wind mitigation and 4-point $150 each. Mold inspection and testing $375 with lab analysis.", body,
         [faq_ld(PRICING_FAQ), breadcrumb_ld([(None, "Pricing")])])

PRICING_FAQ = [
    ("Why is pricing based on square footage?", "Larger homes take longer to inspect and have more systems to check, so the price scales with size."),
    ("Do you charge for travel?", "Not within Miami-Dade and Broward. A travel fee may apply farther out; we'll tell you before you book."),
    ("When do I pay?", "Payment is due on the day of the inspection. Your report is released once payment is received."),
]

def build_reviews():
    body = f'''<section class="page-hero on-dark"><div class="wrap">{crumbs([(None,"Reviews")])}
<h1>{TOTAL_REVIEWS} five-star reviews</h1><p class="lede">Every review on Google and Thumbtack is five stars. Read them where they were posted.</p></div></section>
<section class="bg-white"><div class="wrap">{reviews_block()}</div></section>{cta_band()}'''
    page("/reviews/", "Reviews – 5.0 on Google and Thumbtack",
         f"Inspect and Protect has {TOTAL_REVIEWS} five-star reviews on Google and Thumbtack from home buyers, sellers, investors and homeowners across South Florida.", body,
         [breadcrumb_ld([(None, "Reviews")])])

def build_contact():
    opts = "".join(f"<option>{strip_tags(s['nav'])}</option>" for s in SERVICES) + "<option>Multiple services</option>"
    body = f'''<section class="page-hero on-dark"><div class="wrap">{crumbs([(None,"Book")])}
<h1>Book an inspection</h1><p class="lede">Pick your date and arrival time below; it goes straight onto our calendar. Prefer to talk? Call or text <a href="tel:{PHONE_TEL}" style="color:#fff">{PHONE}</a>.</p></div></section>
<section class="bg-white" id="calendar"><div class="wrap narrow">
<p class="kicker">Book online</p><h2>Choose a date and time</h2>
<p class="note" style="font-size:15px">Open slots are Monday to Saturday. Inspections take 1 to 2 hours on site; you get the full report with photos the same day. Payment by Zelle, cash or check.</p>
{calendly_inline()}
</div></section>
<section><div class="wrap narrow" id="request">
<p class="kicker">Or send a request</p><h2>Don't see a time that works?</h2>
<p class="note" style="font-size:15px;margin-bottom:20px">Send your details and we'll call or text you within 30 minutes to find a time.</p>
<form class="book" action="{FORMSPREE}" method="POST">
<input type="hidden" name="_subject" value="New inspection request – inspectandprotect.net">
<label>First name<input name="first_name" required autocomplete="given-name"></label>
<label>Last name<input name="last_name" required autocomplete="family-name"></label>
<label>Phone<input name="phone" type="tel" required autocomplete="tel"></label>
<label>Email<input name="email" type="email" required autocomplete="email"></label>
<label class="full">Property address<input name="property_address" required autocomplete="street-address"></label>
<label>Service<select name="service">{opts}</select></label>
<label>Square footage<input name="square_footage" inputmode="numeric"></label>
<label>Preferred date<input name="preferred_date" type="date"></label>
<label>How did you find us?<select name="source"><option>Google</option><option>Thumbtack</option><option>Realtor</option><option>Insurance agent</option><option>Friend or family</option><option>Other</option></select></label>
<label class="full">Anything we should know?<textarea name="notes"></textarea></label>
<div class="full"><button class="btn btn-gold" type="submit">Request my inspection →</button>
<p class="note">The inspection agreement is signed before the visit; signing locks in your date and time.</p></div>
</form></div></section>'''
    page("/contact/", "Book a Home Inspection", "Book a home inspection, wind mitigation, 4-point or mold test in South Florida online. Pick your date and time, Monday to Saturday.", body)

# ================================================================ AREAS
def build_areas():
    body = f'''<section class="page-hero on-dark"><div class="wrap">{crumbs([(None,"Areas")])}
<h1>Areas we serve</h1><p class="lede">Home Inspections, Wind Mitigation, 4-Point Inspections and Mold Testing across Miami-Dade, Broward and Palm Beach counties.</p></div></section>
<section class="bg-white"><div class="wrap">'''
    for county in ("Miami-Dade", "Broward", "Palm Beach"):
        cities = [a for a in AREAS if a[2] == county]
        body += f'<h2 style="margin:24px 0 16px">{county} County</h2><div class="pills">' + "".join(f'<a class="pill" href="/areas/{a[0]}/">{a[1]}</a>' for a in cities) + "</div>"
    body += f'<p class="note" style="margin-top:32px">Outside these areas? Call {PHONE}; we take jobs elsewhere in Florida with a travel fee.</p></div></section>{cta_band()}'
    page("/areas/", "Service Areas – Miami-Dade, Broward &amp; Palm Beach",
         "Inspect and Protect serves Miami, Kendall, Hialeah, Homestead, Doral, Fort Lauderdale, Hollywood, Pembroke Pines, West Palm Beach, Boca Raton and more.",
         body, [breadcrumb_ld([(None, "Areas")])])
    for slug, name, county, intro, note in AREAS:
        nearby = [a for a in AREAS if a[2] == county and a[0] != slug][:6]
        nearby_html = "".join(f'<a class="pill" href="/areas/{a[0]}/">{a[1]}</a>' for a in nearby)
        svc = "".join(f'<a class="card" href="{sc_path(slug, s["slug"]) if has_sc(slug, s["slug"]) else "/services/" + s["slug"] + "/"}"><h3>{s["nav"]} in {name}</h3><p>From {s["price_from"]}</p></a>' for s in SERVICES[:4])
        faq = [
            (f"How much is a home inspection in {name}?", f"Home inspections in {name} start at $325 and are priced by square footage. Wind mitigation and 4-point inspections are $150 each."),
            (f"How soon can you inspect in {name}?", f"We schedule {name} inspections 7 days a week and often within a day or two. Reports are delivered the same day."),
            (f"Do you charge travel to {name}?", "No travel fee within Miami-Dade and Broward." if county != "Palm Beach" else "A travel fee may apply in Palm Beach County; we'll tell you before you book."),
        ]
        body = f'''<section class="page-hero on-dark"><div class="wrap">{crumbs([("/areas/","Areas"),(None,name)])}
<p class="kicker">{county} County</p><h1>Home Inspector in {name}, FL</h1>
<p class="lede">Licensed Home Inspections, Wind Mitigation, 4-Point Inspections and Mold Testing in {name}, with same-day reports.</p>
<div class="btn-row"><a class="btn btn-gold" href="/contact/">Book in {name}</a><a class="btn btn-line" href="tel:{PHONE_TEL}">Call {PHONE}</a></div></div></section>
<section class="bg-white"><div class="wrap narrow prose">
<h2>Inspecting homes in {name}</h2><p>{intro}</p><p>{note}</p>
<p>Every inspection includes moisture meter readings and thermal imaging, and your report with photos arrives the same day. We hold Florida Home Inspector License #{LICENSE} and are InterNACHI certified.</p>
</div></section>
<section><div class="wrap"><h2>Services in {name}</h2><div class="grid" style="margin-top:24px">{svc}</div>
<h2 style="margin-top:48px">Prices</h2><div style="margin-top:24px">{pricing_block()}</div></div></section>
<section class="bg-white"><div class="wrap narrow"><h2>{name} questions</h2><div style="margin-top:16px">{faq_html(faq)}</div>
<h3 style="margin-top:40px">Nearby areas</h3><div class="pills" style="margin-top:14px">{nearby_html}</div></div></section>
{cta_band(f"Need an inspector in {name}?")}'''
        page(f"/areas/{slug}/", f"Home Inspector in {name}, FL – Wind Mitigation &amp; 4-Point",
             f"Licensed home inspector serving {name}, FL. Home inspections from $325, wind mitigation and 4-point $150, mold testing $375. Same-day reports.",
             body, [faq_ld(faq), breadcrumb_ld([("/areas/", "Areas"), (None, name)])])

# ================================================================ SERVICE + CITY
SHORT = {"home-inspection": "Home Inspection", "wind-mitigation": "Wind Mitigation Inspection",
         "4-point-inspection": "4-Point Inspection", "mold-inspection-testing": "Mold Inspection &amp; Testing"}

def sc_path(city, svc):
    return f"/areas/{city}/{svc}/"

def has_sc(city, svc):
    return city in SERVICE_CITY_CITIES and svc in SERVICE_CITY_SERVICES

def sc_faq(svc, name, county):
    travel = "There's no travel fee within Miami-Dade and Broward." if county != "Palm Beach" else "A small travel fee may apply in Palm Beach County; we'll confirm before you book."
    if svc == "wind-mitigation":
        return [(f"How much is a wind mitigation inspection in {name}?", f"$150. {travel}"),
                (f"How long does a wind mitigation take in {name}?", "Usually 30 to 45 minutes on site, with the form delivered the same day."),
                ("Will it lower my insurance?", "If your home has qualifying features, your insurer applies the discounts once the form is on file. The amount depends on your home and your insurer.")]
    if svc == "4-point-inspection":
        return [(f"How much is a 4-point inspection in {name}?", f"$150. {travel}"),
                ("How fast do I get the form?", "The same day in most cases, so your agent can move forward quickly."),
                ("Can you do it with a wind mitigation?", "Yes, most clients book both in one visit.")]
    if svc == "mold-inspection-testing":
        return [(f"How much is mold testing in {name}?", f"$375, including up to 3 lab samples with an outdoor control. Extra samples are $75 each. {travel}"),
                ("Do you remove mold?", "No. We inspect and test only, so our findings never come with a cleanup job attached."),
                ("How long do lab results take?", "Results follow once the lab returns them, and we explain them in plain English.")]
    return [(f"How much is a home inspection in {name}?", f"From $325, priced by square footage. {travel}"),
            ("When do I get the report?", "The same day as the inspection, with photos."),
            ("Can I add a wind mitigation and 4-point?", "Yes, both can be done during the same visit.")]

def build_service_cities():
    by_slug = {a[0]: a for a in AREAS}
    for city in SERVICE_CITY_CITIES:
        slug, name, county, intro, note = by_slug[city]
        for svc in SERVICE_CITY_SERVICES:
            s = next(x for x in SERVICES if x["slug"] == svc)
            covers = "".join(f'<div class="card"><h3>{t}</h3><p>{d}</p></div>' for t, d in s["covers"])
            paras = "".join(f"<p>{p}</p>" for p in s["body"][:2])
            faq = sc_faq(svc, name, county)
            same_svc = [c for c in SERVICE_CITY_CITIES if c != city and by_slug[c][2] == county][:6]
            other_svc = [x for x in SERVICE_CITY_SERVICES if x != svc]
            note_html = f'<p class="note">{s["note"]}</p>' if s.get("note") else ""
            body = f'''<section class="page-hero on-dark"><div class="wrap">{crumbs([("/areas/","Areas"),(f"/areas/{city}/",name),(None,SHORT[svc])])}
<p class="kicker">{county} County · {s["price_from"]}</p><h1>{SHORT[svc]} in {name}, FL</h1>
<p class="lede">{strip_tags(s["lede"])}</p>
<div class="btn-row"><a class="btn btn-gold" href="/contact/">Book in {name}</a><a class="btn btn-line" href="tel:{PHONE_TEL}">Call {PHONE}</a></div></div></section>
<section class="bg-white"><div class="wrap narrow prose"><h2>{SHORT[svc]} for {name} homes</h2><p>{intro} {note}</p>{paras}{note_html}</div></section>
<section><div class="wrap"><h2>What we check</h2><div class="grid" style="margin-top:24px">{covers}</div></div></section>
<section class="bg-white"><div class="wrap narrow"><h2>{name} {strip_tags(SHORT[svc]).lower()} questions</h2><div style="margin-top:16px">{faq_html(faq)}</div>
<h3 style="margin-top:40px">More in {name}</h3><div class="pills" style="margin-top:14px">{"".join(f'<a class="pill" href="{sc_path(city,o)}">{SHORT[o]}</a>' for o in other_svc)}<a class="pill" href="/areas/{city}/">All services in {name}</a></div>
<h3 style="margin-top:32px">{SHORT[svc]} nearby</h3><div class="pills" style="margin-top:14px">{"".join(f'<a class="pill" href="{sc_path(c,svc)}">{by_slug[c][1]}</a>' for c in same_svc)}</div>
</div></section>
{cta_band(f"Book your {strip_tags(SHORT[svc]).lower()} in {name}")}'''
            svc_ld = {"@context": "https://schema.org", "@type": "Service", "name": f"{strip_tags(SHORT[svc])} in {name}, FL",
                      "provider": {"@id": DOMAIN + "/#business"}, "areaServed": {"@type": "City", "name": f"{name}, FL"},
                      "offers": {"@type": "Offer", "price": s["price_from"].replace("$", ""), "priceCurrency": "USD"}}
            page(sc_path(city, svc), f"{SHORT[svc]} in {name}, FL – {s['price_from']}",
                 f"{strip_tags(SHORT[svc])} in {name}, FL from a licensed home inspector (HI18768). {s['price_from']}. Same-day reports. {TOTAL_REVIEWS} five-star reviews.",
                 body, [svc_ld, faq_ld(faq), breadcrumb_ld([("/areas/", "Areas"), (f"/areas/{city}/", name), (None, SHORT[svc])])])

# ================================================================ RESOURCES / PARTNERS
def build_resources():
    cards = "".join(f'<a class="card" href="/resources/{a["slug"]}/"><h3>{a["title"]}</h3><p>{a["summary"]}</p><div class="more">Read →</div></a>' for a in ARTICLES)
    body = f'''<section class="page-hero on-dark"><div class="wrap">{crumbs([(None,"Resources")])}
<h1>Resources for Florida homeowners</h1><p class="lede">Plain-English guides to inspections, insurance forms and mold.</p></div></section>
<section class="bg-white"><div class="wrap"><div class="grid grid-wide">{cards}</div></div></section>{cta_band()}'''
    page("/resources/", "Florida Home Inspection Guides", "Guides to Florida wind mitigation, 4-point inspections and mold testing from a licensed South Florida home inspector.", body,
         [breadcrumb_ld([(None, "Resources")])])
    for a in ARTICLES:
        secs = "".join(f"<h2>{h}</h2>" + "".join(f"<p>{p}</p>" for p in ps) for h, ps in a["sections"])
        svc = next(s for s in SERVICES if s["slug"] == a["cta_service"])
        body = f'''<section class="page-hero on-dark"><div class="wrap narrow">{crumbs([("/resources/","Resources"),(None,"Guide")])}
<h1 style="font-size:clamp(32px,4.5vw,48px)">{a["title"]}</h1><p class="lede">{a["summary"]}</p></div></section>
<section class="bg-white"><div class="wrap narrow prose">{secs}
<div class="callout" style="margin-top:40px"><div style="flex:1 1 300px"><h3>{svc["nav"]} from {svc["price_from"]}</h3><p style="margin:6px 0 0;color:var(--muted)">Serving Miami-Dade, Broward and Palm Beach with same-day reports.</p></div><a class="btn btn-dark" href="/services/{svc["slug"]}/">Learn more</a></div>
</div></section>{cta_band()}'''
        art_ld = {"@context": "https://schema.org", "@type": "Article", "headline": strip_tags(a["title"]),
                  "author": {"@type": "Person", "name": "Nicholas Figaro"}, "publisher": {"@id": DOMAIN + "/#business"},
                  "datePublished": TODAY, "mainEntityOfPage": DOMAIN + f'/resources/{a["slug"]}/'}
        page(f'/resources/{a["slug"]}/', a["title"], a["meta"], body, [art_ld, breadcrumb_ld([("/resources/", "Resources"), (None, a["title"])])])

def build_partners():
    for p in PARTNERS:
        pts = "".join(f'<div class="card"><h3>{t}</h3><p>{d}</p></div>' for t, d in p["points"])
        body = f'''<section class="page-hero on-dark"><div class="wrap">{crumbs([(None,p["title"])])}
<p class="kicker">{p["title"]}</p><h1>{p["h1"]}</h1><p class="lede">{p["lede"]}</p>
<div class="btn-row"><a class="btn btn-gold" href="tel:{PHONE_TEL}">Call {PHONE}</a><a class="btn btn-line" href="mailto:{EMAIL}?subject=Referral%20partnership">Email us</a></div></div></section>
<section class="bg-white"><div class="wrap"><div class="grid">{pts}</div>
<h2 style="margin-top:48px">Prices your clients can see up front</h2><div style="margin-top:24px">{pricing_block()}</div></div></section>
<section><div class="wrap">{reviews_block()}</div></section>{cta_band("Let's work together", "Call or email to set up a referral relationship. It takes one conversation.")}'''
        page(f'/{p["slug"]}/', f'{p["title"]} – South Florida Home Inspector', p["meta"], body, [breadcrumb_ld([(None, p["title"])])])

def build_404():
    body = f'''<section class="page-hero on-dark"><div class="wrap"><h1>Page not found</h1><p class="lede">That page moved or doesn't exist.</p>
<div class="btn-row"><a class="btn btn-gold" href="/">Go home</a><a class="btn btn-line" href="/contact/">Book an inspection</a></div></div></section>'''
    page("/404/", "Page not found", "Page not found.", body)
    shutil.move(os.path.join(OUT, "404", "index.html"), os.path.join(OUT, "404.html"))
    os.rmdir(os.path.join(OUT, "404"))
    PAGES.remove("/404/")

SAMPLE_SERVICES = {"home-inspection", "pre-listing-inspection", "new-construction-inspection"}
SAMPLES = [
    ("sample-report-single-family-home.pdf", "Single-family home", "70 pages · 5 MB",
     "A one-story house with an attached living space and a rear accessory structure. Shows how we document additions, roof, electrical panels, AC equipment and moisture readings."),
    ("sample-report-townhome.pdf", "Two-story townhome", "17 pages · 6 MB",
     "An all-electric end-unit townhome. A shorter report that shows the same layout: a summary of findings, then each system with photos and plain-English notes."),
]

def sample_callout(title="See exactly what you'll get", text="Real reports from real South Florida inspections, with client details removed.",
                   btn="View sample reports", href="/sample-reports/"):
    return f'''<div class="callout" style="margin-top:32px"><div style="flex:1 1 360px"><h3>{title}</h3><p style="margin:6px 0 0;color:var(--muted)">{text}</p></div><a class="btn btn-dark" href="{href}">{btn}</a></div>'''

def build_samples():
    cards = "".join(
        f'''<div class="card"><p class="kicker" style="margin:0 0 6px">{meta}</p><h3>{name}</h3><p>{desc}</p>
<div class="btn-row" style="margin-top:18px"><a class="btn btn-dark" href="/reports/{f}">Open the report (PDF)</a></div></div>'''
        for f, name, meta, desc in SAMPLES)
    body = f'''<section class="page-hero on-dark"><div class="wrap">{crumbs([(None, "Sample reports")])}
<h1>Sample inspection reports</h1>
<p class="lede">These are real reports from our inspections, shared so you can see the detail before you book. Client names, addresses, dates and identifying details in the photos have been removed.</p></div></section>
<section class="bg-white"><div class="wrap"><div class="grid grid-wide">{cards}</div>
<div class="prose narrow" style="margin-top:40px"><h2>What every report includes</h2>
<ul><li>A summary of findings sorted by severity: safety hazards, deficiencies, maintenance items and limitations</li>
<li>Roof, structure, exterior, electrical, plumbing, water heater, AC and interior, each with photos</li>
<li>Moisture meter readings and thermal images where we found something worth checking</li>
<li>Plain-English notes on what each finding means and who should look at it</li>
<li>Delivered the same day as the inspection</li></ul></div></div></section>{cta_band()}'''
    page("/sample-reports/", "Sample Home Inspection Reports",
         "See real Inspect and Protect home inspection reports from South Florida: a single-family home and a townhome, with client details removed.",
         body, [breadcrumb_ld([(None, "Sample reports")])])

def build_certifications():
    grid = "".join(f'<div class="cert">{badge_img(s, 140)}<p>{n}</p></div>' for s, n in CERTS)
    body = f'''<section class="page-hero on-dark"><div class="wrap">{crumbs([(None,"Certifications")])}
<h1>Licenses &amp; certifications</h1><p class="lede">Licensed by the State of Florida and certified by InterNACHI, the world's largest home inspector association. Every credential below can be verified.</p></div></section>
<section class="bg-white"><div class="wrap license-feature">
<a href="/assets/brand/fl-license-sm.jpg" target="_blank" rel="noopener"><img src="/assets/brand/fl-license-sm.jpg" alt="Florida DBPR home inspector license HI18768 for Nicholas Figaro, expires July 31, 2028" width="640" height="471"></a>
<div><p class="kicker">Florida license</p><h2>Licensed by the State of Florida</h2>
<p class="lede">Home Inspector License #{LICENSE}, issued by the Florida Department of Business and Professional Regulation under Chapter 468, Florida Statutes. Valid through July 31, 2028.</p>
<div class="btn-row"><a class="btn btn-gold" href="https://www.myfloridalicense.com/wl11.asp" target="_blank" rel="noopener">Verify on MyFloridaLicense</a></div></div>
</div></section>
<section><div class="wrap"><div class="grid grid-wide">
<div class="card"><p class="kicker">InterNACHI</p><h3>Certified Professional Inspector (CPI)</h3><p>InterNACHI member ID {NACHI_ID}. CPI certification requires passing the inspector exam, completing ongoing education and following InterNACHI's Standards of Practice and Code of Ethics.</p><p><a class="more" href="{NACHI_VERIFY}" target="_blank" rel="noopener">Verify the certification →</a></p></div>
<div class="card"><p class="kicker">Guarantee</p><h3>$25,000 Honor Guarantee</h3><p>As InterNACHI members, our inspections are backed by InterNACHI's $25,000 Honor Guarantee.</p><p><a class="more" href="https://www.nachi.org/honor.htm" target="_blank" rel="noopener">How the guarantee works →</a></p></div>
</div></div></section>
<section class="bg-white"><div class="wrap"><p class="kicker">Specialty training</p><h2>{len(CERTS)} InterNACHI certifications</h2>
<p class="lede">Each badge is earned by completing InterNACHI's course and exam for that specialty. They're listed on Nicholas's <a href="{NACHI_PROFILE}" target="_blank" rel="noopener">public InterNACHI profile</a>.</p>
<div class="cert-grid">{grid}</div></div></section>{cta_band()}'''
    page("/certifications/", "Licenses & Certifications",
         f"Florida licensed home inspector #{LICENSE} and InterNACHI Certified Professional Inspector with {len(CERTS)} certifications including wind mitigation, roof, mold and moisture intrusion.",
         body, [breadcrumb_ld([(None, "Certifications")])])

def build_static():
    src_reports = os.path.join(os.path.dirname(__file__), "reports")
    if os.path.isdir(src_reports):
        shutil.copytree(src_reports, os.path.join(OUT, "reports"))
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    shutil.copy(os.path.join(os.path.dirname(__file__), "style.css"), os.path.join(OUT, "assets", "style.css"))
    brand = os.path.join(os.path.dirname(__file__), "brand")
    shutil.copytree(brand, os.path.join(OUT, "assets", "brand"))
    shutil.copy(os.path.join(brand, "shield.svg"), os.path.join(OUT, "favicon.svg"))
    shutil.copy(os.path.join(brand, "apple-touch-icon.png"), os.path.join(OUT, "apple-touch-icon.png"))
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")
    urls = "".join(f"<url><loc>{DOMAIN}{p}</loc><lastmod>{TODAY}</lastmod></url>" for p in PAGES)
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    with open(os.path.join(OUT, "vercel.json"), "w") as f:
        json.dump({"framework": None, "buildCommand": "", "installCommand": "", "outputDirectory": ".",
                   "cleanUrls": True, "trailingSlash": True,
                   "redirects": [{"source": "/index.html", "destination": "/", "permanent": True}]}, f, indent=2)

if __name__ == "__main__":
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT)
    import i18n
    set_groups(i18n.groups())
    build_home(); build_services(); build_pricing(); build_reviews(); build_contact()
    build_areas(); build_service_cities(); build_resources(); build_partners(); build_samples(); build_certifications()
    i18n.build_all(sys.modules[__name__])
    build_404(); build_static()
    print(len(PAGES), "pages"); print("\n".join(PAGES))
