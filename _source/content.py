"""Content for inspectandprotect.net. Everything client-facing lives here."""

PHONE = "(786) 562-0230"
PHONE_TEL = "+17865620230"
EMAIL = "nicholas@inspectandprotect.net"
DOMAIN = "https://www.inspectandprotect.net"
LICENSE = "HI18768"
FORMSPREE = "https://formspree.io/f/meenlplp"
CALENDLY = "https://calendly.com/nicholas-inspectandprotect/inspection"
CALENDLY_EMBED = CALENDLY + "?hide_gdpr_banner=1&primary_color=c9922a&text_color=0d1f35"
def calendly_inline():
    return (f'<div class="calendly-inline-widget" data-url="{CALENDLY_EMBED}" style="min-width:300px;height:1050px"></div>'
            '<script src="https://assets.calendly.com/assets/external/widget.js" async></script>'
            f'<noscript><p><a class="btn btn-gold" href="{CALENDLY}">Open the booking calendar</a></p></noscript>')
GOOGLE_REVIEW_LINK = "https://g.page/r/CTqILax4Rx4oEAE/review"
GOOGLE_PROFILE = "https://www.google.com/maps/place/Inspect+and+Protect/data=!4m2!3m1!1s0x4596fce8a6206f13:0x281e4778ac2d883a"
THUMBTACK_PROFILE = "https://www.thumbtack.com/fl/miami/home-inspection/inspect-protect/service/579292427917369353"

# Poper review widget (free plan: 1 widget). Google Reviews widget id 13726.
POPER_ACCOUNT = "ef7de61f7cb81527786b9c5f35a6bdd5"
POPER_GOOGLE_WIDGET = "13726"
POPER_SNIPPET = (f'<script id="poper-js-script" data-account-id="{POPER_ACCOUNT}" data-domain="inspectandprotect.net" '
                 f'src="https://app.poper.ai/share/poper.js?accountID={POPER_ACCOUNT}" defer></script>'
                 f'<script>window.Poper=window.Poper||[];window.Poper.push({{accountID:"{POPER_ACCOUNT}",domain:"inspectandprotect.net"}});</script>')

def review_feed():
    return f'<div class="review-feed">{POPER_SNIPPET}<div class="poper-{POPER_GOOGLE_WIDGET}"></div></div>'

GOOGLE_RATING, GOOGLE_COUNT = "5.0", 12
THUMBTACK_RATING, THUMBTACK_COUNT = "5.0", 29
TOTAL_REVIEWS = GOOGLE_COUNT + THUMBTACK_COUNT

# ---------------------------------------------------------------- pricing
HOME_TIERS = [
    ("Condo / under 1,200 sq ft", "$325"),
    ("1,200–1,999 sq ft", "$395"),
    ("2,000–2,999 sq ft", "$475"),
    ("3,000–3,999 sq ft", "$550"),
    ("4,000+ sq ft", "from $625"),
]
INSURANCE_PRICES = [
    ("Wind Mitigation (OIR-B1-1802)", "$150"),
    ("4-Point Inspection", "$150"),
]
ENV_PRICES = [
    ("Mold Inspection &amp; Testing", "up to 3 lab samples, incl. outdoor control", "$375"),
    ("Additional mold sample", "", "$75 each"),
]
# Radon and asbestos are held back until credentials are confirmed:
#   ("Radon Test (48-hour)", "", "$225"), ("Asbestos Testing", "up to 3 samples", "$325"),
#   ("Additional asbestos sample", "", "$65 each")
PAYMENT_METHODS = ["Zelle", "Cash", "Check"]
# Flip to True once Afterpay/Affirm are enabled in Stripe.
PAY_OVER_TIME = False

# ---------------------------------------------------------------- services
SERVICES = [
    {
        "slug": "home-inspection",
        "nav": "Home Inspection",
        "title": "Home Inspection in Miami &amp; South Florida",
        "meta": "Licensed Florida home inspector (HI18768) serving Miami-Dade, Broward and Palm Beach. Same-day reports with photos. Prices from $325.",
        "kicker": "Buyer's &amp; seller's inspections",
        "h1": "Home inspections that tell you exactly what you're buying.",
        "lede": "A full visual inspection of the home's structure and systems, with a same-day report full of photos and plain-English explanations.",
        "price_from": "$325",
        "covers": [
            ("Roof &amp; attic", "Roof covering, flashing, visible decking, attic framing, ventilation and insulation."),
            ("Structure", "Foundation, walls, ceilings, floors, windows and doors, with attention to cracks and water intrusion."),
            ("Electrical", "Main panel, breakers, visible wiring, outlets, GFCI and AFCI protection."),
            ("Plumbing", "Supply and drain piping, fixtures, water heater, and signs of leaks."),
            ("HVAC", "Operation of the AC system, air handler, condensate line and drain pan."),
            ("Moisture &amp; thermal", "Moisture meter readings and thermal imaging on suspect areas, included on every inspection."),
        ],
        "body": [
            "South Florida homes face a combination you don't see in most of the country: salt air, intense UV, months of humidity and a hurricane season every year. That shows up in roofs that age faster, AC systems that work harder, and water that finds its way into places you can't see from the hallway.",
            "Every inspection includes a moisture meter and a thermal camera at no extra charge. Water damage is the most common and most expensive surprise in Florida homes, so we look for it on every job, not only when you pay for an add-on.",
            "You're welcome to attend. We walk you through what we found, answer questions on the spot, and send the full report with photos the same day so you can move quickly on your inspection period.",
        ],
        "faq": [
            ("How long does a home inspection take?", "Most inspections take 1 to 2 hours depending on the size, age and condition of the home."),
            ("When do I get the report?", "Your full report with photos is delivered the same day as the inspection."),
            ("Can you add a wind mitigation or 4-point?", "Yes. We can complete both insurance forms during the same visit so you only schedule once."),
        ],
    },
    {
        "slug": "wind-mitigation",
        "nav": "Wind Mitigation",
        "title": "Wind Mitigation Inspection (OIR-B1-1802) – Miami",
        "meta": "Wind mitigation inspections on the current OIR-B1-1802 form for Miami-Dade, Broward and Palm Beach. $150. Can lower your windstorm insurance premium.",
        "kicker": "Insurance inspection",
        "h1": "A wind mitigation report can lower your insurance premium.",
        "lede": "We document your home's wind-resistant features on Florida's official OIR-B1-1802 form so your insurer can apply the discounts you qualify for.",
        "price_from": "$150",
        "covers": [
            ("Building code", "Year built and permit history used to determine which code the home was built to."),
            ("Roof covering", "Roof type and its product approval or permit date."),
            ("Roof deck attachment", "How the roof decking is fastened to the trusses or rafters."),
            ("Roof-to-wall attachment", "Toe nails, clips, single or double wraps connecting the roof to the walls."),
            ("Roof geometry", "Hip, gable or flat roof shape and how much of each."),
            ("Secondary water resistance", "Whether a sealed underlayment would keep water out if shingles or tiles blow off."),
            ("Opening protection", "Impact windows, doors, garage doors and shutters, and their ratings."),
        ],
        "body": [
            "Florida law requires insurers to offer discounts for wind-resistant construction features, but they can only apply them if the features are documented on the official form. A wind mitigation inspection is how that documentation happens.",
            "We complete the current revision of the OIR-B1-1802 form with supporting photos for every answer. Insurers reject reports on outdated form versions, so we keep up with revisions.",
            "A completed form is generally valid for five years as long as nothing on the home changes, like a new roof or new windows. If you replace either, a new inspection can capture the upgrade.",
        ],
        "faq": [
            ("How much can I save?", "It depends on your home's features and your insurer, but homeowners often see meaningful reductions on the windstorm portion of their premium."),
            ("How long does it take?", "Usually 30 to 45 minutes on site."),
            ("Do I need to be home?", "Someone needs to provide access to the attic and the home's exterior openings."),
        ],
    },
    {
        "slug": "4-point-inspection",
        "nav": "4-Point Inspection",
        "title": "4-Point Inspection for Insurance – Miami &amp; South Florida",
        "meta": "4-point insurance inspections (roof, electrical, plumbing, HVAC) for older Florida homes. $150. Same-day report for your insurer.",
        "kicker": "Insurance inspection",
        "h1": "4-point inspections your insurer will accept.",
        "lede": "Insurers often require a 4-point on older homes before they'll write or renew a policy. We inspect the four systems they care about and give you the form the same day.",
        "price_from": "$150",
        "covers": [
            ("Roof", "Covering type, age, remaining life and any signs of leaks or damage."),
            ("Electrical", "Panel brand and condition, wiring type, and hazards such as double taps or missing covers."),
            ("Plumbing", "Supply and drain piping material, water heater age and condition, and visible leaks."),
            ("HVAC", "System age, operation and condition."),
        ],
        "body": [
            "Many Florida insurers ask for a 4-point inspection on homes roughly 25 to 30 years old or more, though each company sets its own rules. If your agent asked for one, it's usually because the home's age triggered the requirement.",
            "Certain items commonly cause problems with insurers, such as some older electrical panel brands, polybutylene piping, aging roofs, and active leaks. We document exactly what's there with photos so your agent has what they need.",
            "If a repair is needed first, we can come back after the work is done to update the report.",
        ],
        "faq": [
            ("How long does a 4-point take?", "About 45 minutes to an hour on site."),
            ("Can you do a wind mitigation at the same time?", "Yes. Most clients book both in one visit."),
            ("What if something fails?", "The report documents what's there. After repairs, we can re-inspect and update it."),
        ],
    },
    {
        "slug": "mold-inspection-testing",
        "nav": "Mold Inspection &amp; Testing",
        "title": "Mold Inspection &amp; Testing in Miami",
        "meta": "Mold inspection and lab testing in Miami-Dade and Broward. Moisture mapping, thermal imaging and up to 3 lab samples for $375. We test, we don't sell cleanup.",
        "kicker": "Environmental testing",
        "h1": "We find the moisture first, then test what matters.",
        "lede": "A spore count alone can't tell you where the water is coming from. We check the home with a moisture meter and thermal camera before a single sample is taken.",
        "price_from": "$375",
        "covers": [
            ("Every accessible room", "Walls, ceilings, floors, baseboards, under sinks, showers, kitchen and laundry."),
            ("Thermal imaging", "Temperature patterns around windows, plumbing and the roofline that can point to hidden moisture."),
            ("AC system &amp; attic", "Air handler, coil, drain pan and line, duct connections and attic insulation."),
            ("Lab-analyzed samples", "Up to 3 air or surface samples with an outdoor control, sent to an accredited lab."),
        ],
        "body": [
            "In South Florida, the air handler often sits in a closet or attic, and the coil, drain pan and duct connections are where mold most often starts. We open up and check the system, not just the rooms.",
            "Samples go where the findings point, not to fill a quota. An indoor air sample is always compared with an outdoor sample taken the same day, because an indoor number means little on its own.",
            "We inspect and test only. We don't do mold removal, so our report has nothing to sell you. If cleanup is needed, you choose the contractor.",
        ],
        "faq": [
            ("What's the difference between a mold inspection and mold testing?", "The inspection finds moisture and visible growth. Testing sends air or surface samples to a lab to measure what's there. Our service includes both."),
            ("How should I prepare?", "Keep windows and doors closed for 24 hours beforehand, skip deep cleaning, turn off air purifiers, and make sure we can reach the AC closet and attic."),
            ("Do you remove mold?", "No. We inspect and test only, so our findings never come with a job attached."),
        ],
        "note": "Mold inspection and testing are performed under our Florida home inspector license. We do not perform mold assessments or mold remediation.",
    },
    {
        "slug": "pre-listing-inspection",
        "nav": "Pre-Listing Inspection",
        "title": "Pre-Listing Home Inspection for Sellers – Miami",
        "meta": "Pre-listing inspections for South Florida sellers. Find issues before buyers do, price with confidence and avoid surprises. Same-day report.",
        "kicker": "For sellers",
        "h1": "Know what the buyer's inspector will find, before they find it.",
        "lede": "A pre-listing inspection gives you time to fix, price around or disclose issues on your terms instead of renegotiating under pressure.",
        "price_from": "$325",
        "covers": [
            ("Full home inspection", "The same scope as a buyer's inspection: roof, structure, electrical, plumbing and HVAC."),
            ("Moisture &amp; thermal", "Moisture meter and thermal imaging included."),
            ("Insurance forms on request", "A current wind mitigation and 4-point can help buyers get insurance quotes faster."),
        ],
        "body": [
            "The most common reason Florida deals fall apart or get renegotiated is an inspection surprise. Finding it first puts you in control.",
            "Having a recent wind mitigation and 4-point ready also helps. Buyers can get insurance quotes quickly, which is a real advantage in today's Florida insurance market.",
        ],
        "faq": [
            ("Do I have to disclose what you find?", "Disclosure rules are a question for your agent or attorney. Our report is a factual record of what we observed."),
        ],
    },
    {
        "slug": "new-construction-inspection",
        "nav": "New Construction &amp; Warranty",
        "title": "New Construction &amp; 11-Month Warranty Inspections – South Florida",
        "meta": "New construction and 11-month builder warranty inspections in Miami-Dade, Broward and Palm Beach. Document defects before your warranty ends.",
        "kicker": "New homes",
        "h1": "New doesn't mean perfect.",
        "lede": "Builders work fast. An independent inspection before closing, and again before your 11-month warranty expires, catches defects while the builder still has to fix them.",
        "price_from": "$325",
        "covers": [
            ("Pre-closing inspection", "A full inspection before your final walkthrough so the punch list is complete."),
            ("11-month warranty inspection", "Documents defects that showed up after move-in, before the builder's warranty ends."),
            ("Moisture &amp; thermal", "Thermal imaging is especially useful in new homes for missing insulation and hidden leaks."),
        ],
        "body": [
            "We've inspected new construction townhomes and single-family homes across South Florida. The most common findings are small but add up: missing insulation, unsealed penetrations, grading and drainage issues, and incomplete finish work.",
            "Book the 11-month inspection about a month before your warranty date so there's time to submit the list to the builder.",
        ],
        "faq": [],
    },
]

# ---------------------------------------------------------------- areas
# county, intro (unique per city), common housing notes
AREAS = [
    ("miami", "Miami", "Miami-Dade", "From high-rise condos to older single-family homes in neighborhoods built decades ago, Miami's housing stock covers every era of Florida construction.", "Older homes often need a 4-point for insurance, and condo owners commonly need a wind mitigation form for their unit."),
    ("kendall", "Kendall", "Miami-Dade", "Kendall is one of Miami-Dade's largest residential areas, with a mix of single-family homes, townhomes and condos.", "Many homes here are 30 to 50 years old, which is when insurers start asking for 4-point inspections."),
    ("hialeah", "Hialeah", "Miami-Dade", "Hialeah has dense neighborhoods of concrete block homes, many with additions and conversions added over the years.", "We pay close attention to additions, electrical panels and roof condition, which matter to both buyers and insurers."),
    ("homestead", "Homestead", "Miami-Dade", "Homestead mixes newer townhome and single-family communities with older homes rebuilt after Hurricane Andrew.", "Homes rebuilt after 1992 often have wind-resistant features worth documenting on a wind mitigation form."),
    ("doral", "Doral", "Miami-Dade", "Doral's newer communities include many townhomes and condos alongside single-family homes.", "Newer homes here are a good fit for new construction and 11-month warranty inspections."),
    ("miami-gardens", "Miami Gardens", "Miami-Dade", "Miami Gardens is largely single-family homes, many built in the 1960s and 70s.", "Homes of this age commonly need a 4-point inspection, and roofs and plumbing are worth a close look."),
    ("cutler-bay", "Cutler Bay", "Miami-Dade", "Cutler Bay and the Cutler Ridge area include single-family homes and townhomes, many rebuilt or reroofed after Hurricane Andrew.", "Roof permits and opening protection often add up to real wind mitigation savings here."),
    ("miami-beach", "Miami Beach", "Miami-Dade", "Miami Beach is mostly condos, along with older homes exposed to salt air year-round.", "Salt air speeds up corrosion on AC equipment and metal components, and condo owners often need a unit wind mitigation form."),
    ("fort-lauderdale", "Fort Lauderdale", "Broward", "Fort Lauderdale's homes range from older single-family neighborhoods to waterfront properties and condos.", "Waterfront and older homes deserve extra attention to moisture, corrosion and roof condition."),
    ("hollywood", "Hollywood", "Broward", "Hollywood has many mid-century single-family homes plus condos near the beach.", "Mid-century homes often trigger 4-point requirements and may have original plumbing or electrical components."),
    ("pembroke-pines", "Pembroke Pines", "Broward", "Pembroke Pines is made up largely of planned communities, townhomes and condos built from the 1980s onward.", "Condo and townhome owners here frequently need wind mitigation forms for insurance renewals."),
    ("plantation", "Plantation", "Broward", "Plantation is a mature suburb with many single-family homes on larger lots.", "Many homes are old enough to need a 4-point, and an AC system that's been running for years deserves a close look."),
    ("davie", "Davie", "Broward", "Davie includes townhome communities, single-family homes and properties on larger, more rural lots.", "We see a wide range of construction here, so we tailor each inspection to the property."),
    ("west-palm-beach", "West Palm Beach", "Palm Beach", "West Palm Beach has historic neighborhoods, newer condos and everything in between.", "Historic homes often have older systems that matter to both buyers and insurers."),
    ("boca-raton", "Boca Raton", "Palm Beach", "Boca Raton's homes include large planned communities, golf course properties and condos.", "Larger homes and communities with tile roofs make wind mitigation and roof documentation especially valuable."),
    # ---- added Oct 2026
    ("coral-gables", "Coral Gables", "Miami-Dade", "Coral Gables is known for its Mediterranean Revival homes, many decades old, alongside newer construction.", "Older Gables homes often have barrel tile roofs, original plumbing and aging electrical, all of which matter on a 4-point."),
    ("aventura", "Aventura", "Miami-Dade", "Aventura is dominated by high-rise condominiums, with some townhomes and single-family homes.", "Condo owners here mostly need unit inspections and wind mitigation forms for their insurance."),
    ("pinecrest", "Pinecrest", "Miami-Dade", "Pinecrest is made up largely of single-family homes on large lots with mature trees.", "Big trees mean roof debris and drainage issues, and many homes are old enough for a 4-point."),
    ("palmetto-bay", "Palmetto Bay", "Miami-Dade", "Palmetto Bay is mostly single-family neighborhoods, many repaired or rebuilt after Hurricane Andrew.", "Post-Andrew construction often qualifies for wind mitigation credits worth documenting."),
    ("miami-lakes", "Miami Lakes", "Miami-Dade", "Miami Lakes is a planned community with single-family homes, townhomes and condos built from the 1960s onward.", "Homes from the early decades of the community commonly need 4-point inspections."),
    ("north-miami", "North Miami", "Miami-Dade", "North Miami has many mid-century single-family homes along with condos near the bay.", "Mid-century homes often have older plumbing, electrical panels and roofs that insurers look at closely."),
    ("miramar", "Miramar", "Broward", "Miramar runs from older neighborhoods in the east to newer planned communities in the west.", "We see everything from new construction warranty work to 4-points on older homes here."),
    ("weston", "Weston", "Broward", "Weston is a planned city of single-family homes and townhomes, many with tile roofs, built mostly from the late 1980s on.", "Tile roofs and HOA communities make roof documentation and wind mitigation especially useful."),
    ("coral-springs", "Coral Springs", "Broward", "Coral Springs is a family suburb of single-family homes and townhomes from several decades of building.", "Homes from the 1970s and 80s often need a 4-point, and AC systems deserve a close look."),
    ("sunrise", "Sunrise", "Broward", "Sunrise has many condos and 55-plus communities alongside single-family neighborhoods.", "Condo and townhome owners frequently need wind mitigation forms and 4-points for insurance."),
    ("lauderhill", "Lauderhill", "Broward", "Lauderhill is mostly condos, townhomes and modest single-family homes.", "Older condo buildings and townhomes often need insurance inspections at renewal time."),
    ("margate", "Margate", "Broward", "Margate has single-family homes and condo communities, many from the 1960s through the 80s.", "Homes of this era commonly need 4-point inspections."),
    ("oakland-park", "Oakland Park", "Broward", "Oakland Park has many older single-family homes and small condo buildings.", "Original plumbing and electrical in older homes are common 4-point findings."),
    ("north-lauderdale", "North Lauderdale", "Broward", "North Lauderdale is largely townhomes, condos and single-family homes from the 1970s onward.", "Insurance inspections are the most common need here, especially at policy renewal."),
    ("pompano-beach", "Pompano Beach", "Broward", "Pompano Beach mixes beachfront condos with older single-family neighborhoods inland.", "Salt air near the beach speeds up corrosion, so we look closely at AC equipment and metal components."),
    ("deerfield-beach", "Deerfield Beach", "Broward", "Deerfield Beach has large condo communities, including 55-plus communities, plus homes near the beach.", "Condo unit owners here often need wind mitigation and 4-point forms."),
    ("delray-beach", "Delray Beach", "Palm Beach", "Delray Beach combines historic homes near downtown with golf and gated communities to the west.", "Historic homes need careful attention to older systems; newer communities often benefit from wind mitigation credits."),
    ("boynton-beach", "Boynton Beach", "Palm Beach", "Boynton Beach has many 55-plus communities, condos and single-family homes.", "Insurance inspections for renewals are a frequent need here."),
    ("lake-worth-beach", "Lake Worth Beach", "Palm Beach", "Lake Worth Beach has older cottages and bungalows, many dating to the early and mid 1900s.", "Older homes here can have dated wiring and plumbing that insurers look at closely."),
    ("lantana", "Lantana", "Palm Beach", "Lantana is a small coastal town with older single-family homes and condos.", "Older homes and coastal exposure make roof and corrosion checks important."),
    ("royal-palm-beach", "Royal Palm Beach", "Palm Beach", "Royal Palm Beach is mostly single-family homes in neighborhoods built from the 1970s onward.", "Many homes are at the age where insurers start asking for 4-point inspections."),
    ("wellington", "Wellington", "Palm Beach", "Wellington is known for larger homes, equestrian properties and planned communities.", "Larger homes and tile roofs make full inspections and wind mitigation especially valuable."),
]

# Main cities that get their own service pages (city slug list)
SERVICE_CITY_CITIES = ["miami", "kendall", "hialeah", "homestead", "doral", "miami-gardens", "coral-gables",
                       "fort-lauderdale", "hollywood", "pembroke-pines", "plantation", "miramar",
                       "west-palm-beach", "boca-raton"]
SERVICE_CITY_SERVICES = ["home-inspection", "wind-mitigation", "4-point-inspection", "mold-inspection-testing"]

# ---------------------------------------------------------------- articles
ARTICLES = [
    {
        "slug": "wind-mitigation-inspection-florida",
        "title": "What a Florida Wind Mitigation Inspection Checks, and How It Lowers Your Premium",
        "meta": "The 7 questions on Florida's OIR-B1-1802 wind mitigation form, what qualifies for discounts, and how long the form is valid.",
        "summary": "The seven questions on the OIR-B1-1802 form and what each one means for your insurance.",
        "sections": [
            ("Why the inspection exists", ["Florida law requires insurers to offer premium discounts for construction features that reduce hurricane damage. Your insurer can't apply those discounts until the features are documented on the state's official Uniform Mitigation Verification Inspection Form, the OIR-B1-1802."]),
            ("The seven questions", [
                "<strong>1. Building code.</strong> Homes built to the 2001 Florida Building Code or later, or the South Florida Building Code in Miami-Dade and Broward for qualifying years, can earn credit.",
                "<strong>2. Roof covering.</strong> Whether the roof covering meets current code, shown by a product approval or a permit date.",
                "<strong>3. Roof deck attachment.</strong> How the plywood or decking is nailed to the trusses. Larger nails at tighter spacing score better.",
                "<strong>4. Roof-to-wall attachment.</strong> Toe nails, clips, single wraps or double wraps. Wraps and clips usually earn more credit than toe nails.",
                "<strong>5. Roof geometry.</strong> Hip roofs perform better in wind than gable roofs and typically earn a discount.",
                "<strong>6. Secondary water resistance.</strong> A sealed underlayment that keeps water out if the roof covering is lost.",
                "<strong>7. Opening protection.</strong> Impact-rated windows, doors and garage doors, or approved shutters on every opening.",
            ]),
            ("How long it's good for", ["A completed form is generally accepted for five years, as long as the home hasn't changed. A new roof or new impact windows are a good reason to get a new inspection, since they can earn more credit."]),
            ("Tips to get the most out of it", ["Find your roof permit and any window or shutter permits ahead of time. Make sure the attic is accessible. Insurers reject forms on outdated revisions, so ask your inspector which revision they use."]),
        ],
        "cta_service": "wind-mitigation",
    },
    {
        "slug": "what-fails-a-4-point-inspection",
        "title": "What Fails a 4-Point Inspection in Florida",
        "meta": "The roof, electrical, plumbing and HVAC issues that most often cause problems with Florida insurers on a 4-point inspection.",
        "summary": "The roof, electrical, plumbing and HVAC items insurers flag most often.",
        "sections": [
            ("A 4-point isn't pass or fail, but insurers decide", ["The inspector documents what's there. Each insurer then decides what it will accept, so the same report can be fine for one company and a problem for another."]),
            ("Roof", ["Insurers want to know the roof's age, type and remaining life. Older roofs, roofs with active leaks, and visible damage are the most common reasons a policy is delayed."]),
            ("Electrical", ["Some older panel brands are commonly declined by insurers. Other frequent issues are double-tapped breakers, missing panel covers, exposed wiring, and older wiring types."]),
            ("Plumbing", ["Polybutylene supply piping is widely declined. Insurers also look at the water heater's age, missing pressure relief lines, and any active leaks."]),
            ("HVAC", ["The system needs to be working. Age matters too, and a unit in poor condition can raise questions."]),
            ("What to do if something comes up", ["Repair or replace the item, keep the invoice or permit, and have the inspector update the report. Ask your agent what their company requires before you schedule repairs."]),
        ],
        "cta_service": "4-point-inspection",
    },
    {
        "slug": "mold-inspection-vs-mold-testing",
        "title": "Mold Inspection vs. Mold Testing: What You Actually Need",
        "meta": "The difference between a mold inspection and mold testing, why moisture comes first, and when lab samples are worth it in South Florida.",
        "summary": "Why finding the moisture comes first, and when lab samples are worth it.",
        "sections": [
            ("Two different questions", ["A mold inspection asks where moisture and growth are and why. Mold testing asks what's in a sample of air or a surface. A test alone tells you a number, not where the water is coming from."]),
            ("Why moisture comes first", ["Mold needs water. In South Florida the usual sources are AC condensate problems, roof and window leaks, plumbing leaks and high indoor humidity. Finding and fixing the moisture is what actually solves the problem."]),
            ("When lab samples help", ["Samples are useful when there's a musty smell with no visible source, after a water event, for documentation in a sale or claim, or when someone in the home has symptoms. An indoor air sample should always be compared with an outdoor sample taken the same day."]),
            ("Be careful with free inspections", ["A company that inspects and also sells removal has a reason to find a problem. An independent inspection with no cleanup to sell gives you an unbiased answer."]),
        ],
        "cta_service": "mold-inspection-testing",
    },
    {
        "slug": "roof-age-insurance-florida",
        "title": "How Old Can Your Roof Be for Insurance in Florida?",
        "meta": "Florida's roof age rules: insurers can't refuse a policy solely over a roof under 15 years old, and older roofs can stay insured with an inspection showing 5+ years of life.",
        "summary": "The 15-year rule, the 5-year remaining-life inspection, and who can do it.",
        "sections": [
            ("Roofs under 15 years old", ["Florida law says an insurer can't refuse to write or renew a homeowner's policy solely because the roof is less than 15 years old."]),
            ("Roofs 15 years or older", ["Before an insurer requires you to replace an older roof, it has to let you get the roof inspected. If the inspection shows at least 5 years of useful life left, the insurer can't refuse the policy solely because of the roof's age. The inspection is at the homeowner's expense."]),
            ("Who can do the inspection", ["The law lists several kinds of authorized inspectors, including Florida licensed home inspectors, licensed contractors and roofers, engineers and architects. The insurer has to accept the inspector, so check with your agent first."]),
            ("What the inspector looks at", ["Covering type and condition, missing or damaged shingles or tiles, flashing, signs of leaks in the attic, and the permit history. A 4-point inspection includes the roof's estimated remaining life, which is often what the insurer needs."]),
        ],
        "cta_service": "4-point-inspection",
    },
    {
        "slug": "condo-wind-mitigation-4-point",
        "title": "Do Condo Owners Need a Wind Mitigation or 4-Point Inspection?",
        "meta": "When Florida condo owners need a wind mitigation form or 4-point inspection for HO-6 insurance, and what the inspector checks inside a unit.",
        "summary": "What condo unit owners need for HO-6 insurance, and what gets inspected.",
        "sections": [
            ("It depends on your insurer", ["Condo unit owners carry an HO-6 policy, and each insurer sets its own rules. Many ask for a 4-point on older buildings, and a wind mitigation form can lower the windstorm part of the premium."]),
            ("Wind mitigation for a condo unit", ["The OIR-B1-1802 form covers the building's construction and the unit's openings. Impact windows and doors in your unit are often where the savings come from."]),
            ("4-point for a condo unit", ["For a unit, the 4-point usually focuses on what's inside: the electrical panel, plumbing and water heater, and the AC system. The roof belongs to the association, so it's often noted from available information."]),
            ("Mid-rise and high-rise buildings", ["Some insurers ask for a building-level form for taller buildings. That is typically completed by a contractor or engineer for the association, not for an individual unit."]),
        ],
        "cta_service": "wind-mitigation",
    },
    {
        "slug": "florida-home-buyer-inspection-checklist",
        "title": "Florida Home Buyer's Inspection Checklist",
        "meta": "What Florida home buyers should check during the inspection period: roof, AC, moisture, electrical, plumbing, and the insurance forms you'll need.",
        "summary": "What to look at, and what to line up, during your inspection period.",
        "sections": [
            ("Book early in your inspection period", ["Florida contracts often give buyers a short inspection window. Book the inspection right away so there's time for follow-ups, repair quotes and insurance quotes."]),
            ("Get insurance forms in the same visit", ["Your insurer may need a 4-point and will usually give credit for a wind mitigation form. Getting both during the home inspection means you can shop for insurance before your deadline."]),
            ("What matters most in Florida homes", ["Roof age and condition, the AC system and its drain line, signs of moisture and past leaks, the electrical panel, and the type of plumbing. These drive both repair costs and insurability."]),
            ("Attend if you can", ["Walking the home with the inspector is the fastest way to understand what's serious and what's routine maintenance."]),
        ],
        "cta_service": "home-inspection",
    },
]

PARTNERS = [
    {
        "slug": "for-realtors",
        "title": "For Real Estate Agents",
        "meta": "A South Florida home inspector agents can count on: fast scheduling, same-day reports, wind mitigation and 4-point in the same visit.",
        "h1": "An inspector who keeps your deals moving.",
        "lede": "Fast scheduling, same-day reports, and insurance forms in the same visit so your buyers can get quotes before the inspection period ends.",
        "points": [
            ("Same-day reports", "Your buyer has the report the day of the inspection, with photos and plain-English findings."),
            ("Insurance forms in one visit", "Wind mitigation and 4-point completed during the home inspection, so insurance quotes don't hold up closing."),
            ("Clear, calm walkthroughs", "We explain findings without alarming language, so buyers understand what's serious and what's routine maintenance."),
            ("Direct line", "You and your clients reach the inspector directly at " + PHONE + "."),
        ],
    },
    {
        "slug": "for-insurance-agents",
        "title": "For Insurance Agents",
        "meta": "Wind mitigation and 4-point inspections for Florida insurance agencies. Current OIR-B1-1802 revision, photo documentation, fast turnaround.",
        "h1": "Wind mits and 4-points your underwriters can work with.",
        "lede": "We complete the current OIR-B1-1802 revision and 4-point forms with clear photos for every answer, and get them back fast.",
        "points": [
            ("Current form revisions", "We use the current OIR-B1-1802 revision so reports don't bounce back."),
            ("Photos for every answer", "Each wind mitigation question and 4-point item is backed by photos."),
            ("Fast turnaround", "Reports delivered same day in most cases."),
            ("Coverage", "Miami-Dade, Broward and Palm Beach counties."),
        ],
    },
]


# ---------------------------------------------------------------- CREDENTIALS
NACHI_ID = "NACHI26041410"
NACHI_VERIFY = f"https://www.nachi.org/verify?nachiid={NACHI_ID}"
NACHI_PROFILE = "https://www.nachi.org/certified-inspectors/nicholas-figaro-205492"
DBPR_VERIFY = "https://www.myfloridalicense.com/wl11.asp?mode=0&SID=&brd=0&typ="
# (file in /assets/brand/badges/, display name)  -- order = importance
CERTS = [
    ("internachi-certified-professional-inspector-cpi", "Certified Professional Inspector (CPI)"),
    ("internachi-certified-blue-gold", "InterNACHI Certified"),
    ("honor-guarantee", "$25,000 Honor Guarantee"),
    ("residential-property-inspector", "Residential Property Inspector"),
    ("wind-mitigation-inspector", "Wind Mitigation Inspector"),
    ("roof-inspector", "Roof Inspector"),
    ("mold-inspector", "Mold Inspector"),
    ("moisture-intrusion-inspector", "Moisture Intrusion Inspector"),
    ("post-hurricane-building-safety-inspector", "Post-Hurricane Building Safety Inspector"),
    ("electrical-inspector", "Electrical Inspector"),
    ("plumbing-inspector", "Plumbing Inspector"),
    ("exterior-inspector", "Exterior Inspector"),
    ("attic-insulation-ventilation-interior", "Attic, Insulation, Ventilation & Interior"),
    ("new-construction-inspector", "New Construction Inspector"),
    ("11th-month-warranty-inspector", "11th Month Warranty Inspections"),
    ("annual-home-maintenance-inspections", "Annual Home Maintenance Inspections"),
    ("kitchen-inspector", "Kitchen Inspector"),
    ("deck-inspector", "Deck Inspector"),
    ("crawlspace-inspector", "Crawlspace Inspector"),
    ("chimney-inspector", "Chimney Inspector"),
    ("safe-workplace-inspector", "Safe Workplace Inspector"),
]
HOME_BADGES = ["internachi-certified-professional-inspector-cpi", "honor-guarantee", "wind-mitigation-inspector",
               "roof-inspector", "mold-inspector", "moisture-intrusion-inspector", "post-hurricane-building-safety-inspector",
               "residential-property-inspector"]

def badge_img(slug, size=96):
    name = dict(CERTS)[slug]
    return f'<img src="/assets/brand/badges/{slug}.webp" alt="InterNACHI {name} badge" title="{name}" width="{size}" height="{size}" loading="lazy">'

def badge_strip(heading, sub, more_text, more_href="/certifications/"):
    imgs = "".join(badge_img(s) for s in HOME_BADGES)
    return f'''<section class="bg-white badges-sec"><div class="wrap">
<p class="kicker">{heading}</p><h2>{sub}</h2>
<div class="badge-row">{imgs}</div>
<p style="margin-top:20px"><a class="more" href="{more_href}">{more_text} →</a></p></div></section>'''

def footer_seals():
    return (f'<div class="seals"><a href="{NACHI_VERIFY}" target="_blank" rel="noopener"><img src="https://www.nachi.org/webseals/sb-v2-{NACHI_ID}.gif" width="98" height="102" alt="Certified by the International Association of Certified Home Inspectors" loading="lazy"></a>'
            f'<a href="{NACHI_VERIFY}" target="_blank" rel="noopener"><img src="https://www.nachi.org/webseals/internachi-honor-guarantee.png?nachiid={NACHI_ID}" width="102" height="102" alt="$25,000 Honor Guarantee, Backed by InterNACHI" loading="lazy"></a></div>')
