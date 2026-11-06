#!/usr/bin/env python3
"""Builds the static playandplanpaper.com site into the repository root.

Run:  python3 _build/build.py
Edit products in _build/products.json, guides in _build/guides.py, styles in _build/base.css.
"""
import json, html, os, re, shutil, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
B = ROOT / "_build"
SITE = "https://playandplanpaper.com"
SHOP = "https://www.etsy.com/shop/PlayAndPlanPaper"
PINTEREST = "https://www.pinterest.com/playandplanpaper/"
TIKTOK = "https://www.tiktok.com/@play.plan.paper.p"
TODAY = datetime.date.today().isoformat()

PRODUCTS = json.loads((B / "products.json").read_text())
BY = {p["slug"]: p for p in PRODUCTS}
from guides import GUIDES  # noqa: E402

e = html.escape


def img_count(slug):
    n = 0
    while (ROOT / "img" / "p" / f"{slug}-{n + 1}.jpg").exists():
        n += 1
    return n


HUBS = {
    "christmas": dict(path="christmas-games", nav="Christmas", h1="Printable Christmas Games",
        title="Printable Christmas Games for Family, Kids & Adults",
        lede="Party games, family quizzes, bingo, charades and scavenger hunts you can print at home tonight. Every pack works for mixed ages and comes in A4 and US Letter.",
        meta="Printable Christmas games for family, kids and adults: party games, quiz, bingo and scavenger hunts. Instant download, A4 and US Letter, print at home tonight.",
        chips=[("all", "All"), ("adults", "For adults"), ("family", "Family"), ("kids", "Kids"), ("office", "Office party"), ("bundle", "Bundles")]),
    "party": dict(path="party-games", nav="Party games", h1="Printable Party Games",
        title="Printable Party Games for New Year, Valentine's, Showers & Hen Dos",
        lede="Games for every party after Christmas: date nights for two, a family escape room, New Year's Eve, Valentine's and Galentine's, Easter, baby showers, bridal showers and hen dos.",
        meta="Printable party games for New Year's Eve, Valentine's, Easter, baby showers, bridal showers and hen parties. Instant download in A4 and US Letter."),
    "planners": dict(path="planners", nav="Planners", h1="Printable Planners & Organisers",
        title="Printable Planners: Budget, ADHD, Chore Charts & Drone Logbook",
        lede="Calm, simple pages that make home life easier: a UK budget spreadsheet for Google Sheets and Excel, an undated budget planner, an ADHD-friendly planner, chore charts for kids, a Christmas planner and a drone pilot logbook.",
        meta="Printable planners and organisers: UK budget spreadsheet, undated budget planner, ADHD-friendly planner, chore and reward charts, Christmas planner and drone pilot logbook."),
}

CSS_VER = "2"


def head(title, desc, path, og_img="img/og.jpg", og_type="website", schema=None):
    url = f"{SITE}/{path}"
    s = ""
    for block in (schema or []):
        s += f'<script type="application/ld+json">{json.dumps(block, ensure_ascii=False)}</script>\n'
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:site_name" content="Play &amp; Plan Paper">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/{og_img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#2F5D50">
<link rel="icon" href="/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Caveat:wght@700&family=Fraunces:opsz,wght@9..144,500;9..144,700;9..144,800&family=Nunito:wght@400;700;800&display=swap">
<link rel="stylesheet" href="/style.css?v={CSS_VER}">
{s}<script>(function(w,d,e,u,f,l,n){{w[f]=w[f]||function(){{(w[f].q=w[f].q||[]).push(arguments);}},l=d.createElement(e),l.async=1,l.src=u,n=d.getElementsByTagName(e)[0],n.parentNode.insertBefore(l,n);}})(window,document,'script','https://assets.mailerlite.com/js/universal.js','ml');ml('account','2775036');</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="top-strip"><div class="wrap"><strong>Instant download</strong> · print at home in A4 or US Letter · <strong>25% off Christmas</strong> until 24 Nov</div></div>
<header class="site-h">
  <div class="wrap">
    <a class="brand" href="/" aria-label="Play and Plan Paper home"><img src="/img/mark.png" alt="" width="40" height="40"><span class="wm">Play &amp; Plan<small>PAPER</small></span></a>
    <nav class="mainnav" aria-label="Main">
      <a href="/christmas-games/">Christmas</a><a href="/party-games/">Party games</a><a href="/planners/">Planners</a><a href="/ideas/">Ideas</a><a href="/about/">About</a>
    </nav>
    <a class="btn btn-etsy btn-sm" href="{SHOP}" rel="noopener">Shop on Etsy</a>
  </div>
</header>
<main id="main">
"""


FOOT = f"""</main>
<section class="signup" aria-labelledby="signup-h">
  <div class="wrap signup-in">
    <div class="signup-copy"><p class="kicker">Free printable</p><h2 id="signup-h">Get a free Christmas Emoji Game</h2><p>24 emoji puzzles to print tonight, plus new games before each holiday. No spam, unsubscribe anytime.</p></div>
    <div class="signup-form"><div class="ml-embedded" data-form="AeThT6"></div></div>
  </div>
</section>
<footer class="site-f">
  <div class="wrap">
    <div class="stack" style="gap:.6rem"><a class="brand" href="/"><img src="/img/mark.png" alt="" width="40" height="40" loading="lazy"><span class="wm" style="color:var(--on-band)">Play &amp; Plan<small style="color:var(--honey)">PAPER</small></span></a><p>Printable games and planners, designed in Manchester, England.</p><span class="mail">hello@playandplanpaper.com</span></div>
    <div><h4>Shop</h4><a href="/christmas-games/">Christmas games</a><a href="/party-games/">Party games</a><a href="/planners/">Planners</a><a href="/p/drone-pilot-logbook/">Drone logbook</a><a href="{SHOP}">All on Etsy</a></div>
    <div><h4>Ideas</h4><a href="/ideas/printable-christmas-games-for-adults/">Christmas games for adults</a><a href="/ideas/christmas-games-for-kids/">Christmas games for kids</a><a href="/ideas/">All guides</a><a href="/about/">About us</a></div>
    <div><h4>Follow</h4><a href="{PINTEREST}" rel="noopener">Pinterest</a><a href="{TIKTOK}" rel="noopener">TikTok</a><a href="{SHOP}" rel="noopener">Etsy shop</a></div>
    <p class="legal">© {datetime.date.today().year} Play &amp; Plan Paper. Printables are for personal use. Orders, payments and downloads are handled securely by Etsy.</p>
  </div>
</footer>
<script src="/site.js?v={CSS_VER}" defer></script>
</body>
</html>
"""


def crumbs(items):
    """items: list of (name, path or None)."""
    parts = ['<a href="/">Home</a>']
    for name, path in items:
        parts.append(f'<a href="/{path}">{e(name)}</a>' if path else e(name))
    schema = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}] + [
        {"@type": "ListItem", "position": i + 2, "name": n, **({"item": f"{SITE}/{p}"} if p else {})}
        for i, (n, p) in enumerate(items)]}
    return f'<p class="crumbs">{" › ".join(parts)}</p>', schema


def card(p, tag=None):
    tag = tag or p.get("tag")
    t = f'<span class="tag">{e(tag)}</span>' if tag else ""
    return (f'<article class="card" data-f="{" ".join(p.get("filters", []))}"><div class="ph">'
            f'<a href="/p/{p["slug"]}/" tabindex="-1" aria-hidden="true"><img src="/img/p/{p["slug"]}-1.jpg" alt="{e(p["name"])} printable" loading="lazy" width="900" height="900"></a>{t}</div>'
            f'<div class="bd"><h3><a href="/p/{p["slug"]}/">{e(p["name"])}</a></h3><p class="meta">{e(p["short"])}</p>'
            f'<div class="row"><span class="price-note">Instant download</span><a class="buy" href="/p/{p["slug"]}/">View →</a></div></div></article>')


def faq_block(items, schema_list):
    schema_list.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]})
    return '<div class="faq">' + "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in items) + "</div>"


KEEP_UPPER = {"UK", "US", "EU", "PDF", "A4", "A5", "ADHD", "FAA", "NYE", "XMAS"}


def desc_html(text):
    out, ul = [], False
    for line in text.splitlines():
        s = line.strip()
        if not s:
            if ul:
                out.append("</ul>"); ul = False
            continue
        if s.startswith("•"):
            if not ul:
                out.append("<ul>"); ul = True
            out.append(f"<li>{e(s[1:].strip())}</li>")
            continue
        if ul:
            out.append("</ul>"); ul = False
        letters = re.sub(r"[^A-Za-z]", "", s)
        if letters and sum(c.isupper() for c in letters) / len(letters) > 0.6 and len(s) < 70:
            clean = re.sub(r"^[^A-Za-z0-9]+", "", s).strip()
            words = clean.lower().split()
            words = [w.upper() if w.strip("()&,:").upper() in KEEP_UPPER else w for w in words]
            text = " ".join(words).replace("pdfs", "PDFs")
            out.append(f"<h3>{e(text[:1].upper() + text[1:])}</h3>")
        else:
            out.append(f"<p>{e(s)}</p>")
    if ul:
        out.append("</ul>")
    return "\n".join(out)


def write(path, content):
    f = ROOT / path
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(content)


ORG = {"@context": "https://schema.org", "@type": "Organization", "name": "Play & Plan Paper", "url": SITE + "/",
       "logo": f"{SITE}/img/mark.png", "sameAs": [SHOP, PINTEREST, TIKTOK]}
SITE_SCHEMA = {"@context": "https://schema.org", "@type": "WebSite", "name": "Play & Plan Paper", "url": SITE + "/"}

HOME_FAQ = [
    ("How do I get my printable?", "Every product is sold through our Etsy shop. Right after checkout Etsy gives you a download link and emails it to you. Open the PDF and print."),
    ("Will it print on my home printer?", "Yes. Every pack comes in A4 and US Letter, with an ink-saver version that uses far less colour ink."),
    ("Can I print more than one copy?", "Yes, as many as your own household, party or classroom needs."),
    ("Do you post anything?", "No. Everything is a digital download, so there is no waiting and no postage."),
]
XMAS_FAQ = [
    ("What are good printable Christmas games for adults?", "Who's Most Likely To, Christmas charades, Would You Rather and the Left Right gift game all work with no setup. The Christmas Party Games pack has 12 games like these."),
    ("Which Christmas games work for all ages?", "Bingo, charades and the scavenger hunt work from about age 5 to 95."),
    ("Can I play on Christmas Day if I buy on Christmas Eve?", "Yes. Downloads are instant, so you can buy, print and play the same day."),
    ("Do the games come in A4 and US Letter?", "Yes. Every pack includes A4 and US Letter PDFs, each in full colour and ink-saver versions."),
]


def build_home():
    schema = [ORG, SITE_SCHEMA]
    best = ["ultimate-christmas-games-bundle", "christmas-party-games", "christmas-family-quiz", "christmas-bingo"]
    tags = {"ultimate-christmas-games-bundle": "Best value"}
    body = f"""
<section class="hero">
  <div class="wrap">
    <div class="copy">
      <p class="hand-kicker">Buy at 6, playing by 7</p>
      <h1>Printable party games &amp; planners <em>for real-life families</em></h1>
      <p class="lede">Christmas games, family quizzes, party packs and calm, simple planners. Download the PDF, print it at home and get the party going tonight.</p>
      <div class="ctas"><a class="btn btn-pri" href="/christmas-games/">Shop Christmas games</a><a class="btn btn-sec" href="/ideas/printable-christmas-games-for-adults/">Get game ideas</a></div>
      <ul class="facts"><li>Instant PDF download</li><li>A4 + US Letter</li><li>Colour + ink-saver</li><li>UK &amp; US spellings</li></ul>
    </div>
    <div class="fan" aria-hidden="true">
      <figure class="f1"><img src="/img/p/christmas-family-quiz-1.jpg" alt="" width="900" height="900"></figure>
      <figure class="f2"><img src="/img/p/christmas-bingo-1.jpg" alt="" width="900" height="900"></figure>
      <figure class="f3"><img src="/img/p/ultimate-christmas-games-bundle-1.jpg" alt="" width="900" height="900"></figure>
      <div class="scrawl">30+ games<br>in one download!</div>
    </div>
  </div>
</section>
<div class="ribbon"><div class="wrap"><span><span class="num" id="days">–</span> days until Christmas</span><span>Nothing to post, nothing to wait for.</span><a href="/p/ultimate-christmas-games-bundle/">See the Ultimate Bundle →</a></div></div>
<section style="padding-bottom:0">
  <div class="wrap">
    <div class="sec-head"><div class="stack"><p class="eyebrow">Just added</p><h2>New in the shop</h2></div><p>Christmas emoji games, a kids' escape room to save Santa's sleigh, and a low-overwhelm cleaning planner.</p></div>
    <div class="grid grid-3">{"".join(card(BY[s]) for s in ["christmas-emoji-games", "christmas-escape-room", "adhd-cleaning-planner"])}</div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="sec-head"><div class="stack"><p class="eyebrow">Shop by occasion</p><h2>What are you planning?</h2></div><p>Find games and planners for every part of the year.</p></div>
    <div class="occ">
      <a href="/christmas-games/"><b>Christmas games</b><span>Quizzes, bingo, charades, hunts</span><span class="when">Now – 25 Dec</span></a>
      <a href="/p/new-years-eve-games/"><b>New Year's Eve</b><span>Games for the countdown</span><span class="when">31 Dec</span></a>
      <a href="/p/valentines-games/"><b>Valentine's &amp; Galentine's</b><span>Couples quiz, party games</span><span class="when">14 Feb</span></a>
      <a href="/p/secret-santa-kit/"><b>Secret Santa</b><span>Questionnaires, name draw, swap games</span><span class="when">Now – Dec</span></a>
      <a href="/p/christmas-eve-box-kit/"><b>Christmas Eve box</b><span>Magic key, labels, tickets</span><span class="when">24 Dec</span></a>
      <a href="/p/date-night-murder-mystery/"><b>Date night for two</b><span>Murder mystery and couples games</span><span class="when">14 Feb</span></a>
      <a href="/p/christmas-escape-room/"><b>Christmas escape room</b><span>Save Santa's sleigh, ages 6+</span><span class="when">Now – 25 Dec</span></a>
      <a href="/p/escape-room-kids/"><b>Family escape room</b><span>Puzzles for ages 8+</span><span class="when">All year</span></a>
      <a href="/party-games/"><b>Showers &amp; hen dos</b><span>Baby shower, bridal shower, hen party</span><span class="when">All year</span></a>
      <a href="/planners/"><b>Planners</b><span>ADHD cleaning, UK budget spreadsheet, chore charts</span><span class="when">New year, new plan</span></a>
      <a href="/p/drone-pilot-logbook/"><b>Drone pilots</b><span>Logbook + flight tracker spreadsheet</span><span class="when">UK, EU &amp; US</span></a>
    </div>
  </div>
</section>
<section style="padding-top:0">
  <div class="wrap">
    <div class="sec-head"><div class="stack"><p class="eyebrow">Most loved this season</p><h2>Christmas favourites</h2></div><a class="btn btn-sec btn-sm" href="/christmas-games/">See all Christmas →</a></div>
    <div class="grid">{"".join(card(BY[s], tags.get(s)) for s in best)}</div>
  </div>
</section>
<section class="band">
  <div class="wrap">
    <div class="sec-head"><div class="stack"><p class="eyebrow" style="color:var(--honey)">How it works</p><h2>From basket to game night in three steps</h2></div></div>
    <ol class="steps">
      <li><h3>Buy on Etsy</h3><p>Checkout is safe and simple through our Etsy shop.</p></li>
      <li><h3>Download the PDF</h3><p>Pick A4 or US Letter, full colour or ink-saver. It arrives in seconds.</p></li>
      <li><h3>Print and play</h3><p>A home printer is fine. Print as many copies as your family needs.</p></li>
    </ol>
    <div class="inuse"><img src="/img/inuse.jpg" alt="Printed Christmas party game sheets on a wooden table with a coffee mug and pencil" width="1200" height="900" loading="lazy"></div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="freebie">
      <div class="stack">
        <p class="eyebrow">New printables every week</p>
        <h2>Follow along for new games and ideas</h2>
        <p style="color:var(--muted)">We share new packs, game ideas and seasonal printables on Pinterest and TikTok first.</p>
      </div>
      <div class="ctas"><a class="btn btn-pri" href="{PINTEREST}" rel="noopener">Follow on Pinterest</a><a class="btn btn-sec" href="{TIKTOK}" rel="noopener">Watch on TikTok</a></div>
    </div>
  </div>
</section>
<section style="padding-top:0">
  <div class="wrap">
    <div class="sec-head"><div class="stack"><p class="eyebrow">Ideas &amp; guides</p><h2>Party ideas from the blog</h2></div><a class="btn btn-sec btn-sm" href="/ideas/">All ideas →</a></div>
    <div class="posts">{"".join(post_card(g) for g in GUIDES)}</div>
  </div>
</section>
<section class="band" style="padding-block:2.5rem">
  <div class="wrap about">
    <img src="/img/mark.png" alt="" width="72" height="72" loading="lazy">
    <div class="stack">
      <h2 style="font-size:var(--step-2)">Designed in Manchester for busy hosts</h2>
      <p>Play &amp; Plan Paper makes printables that do the hard part of hosting for you. Every game is laid out to print cleanly on a home printer, every pack comes in A4 and US Letter, and there is always an ink-saver version. If something isn't right, message us and we'll fix it.</p>
    </div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="sec-head"><div class="stack"><p class="eyebrow">Questions</p><h2>Good to know</h2></div></div>
    {faq_block(HOME_FAQ, schema)}
  </div>
</section>
"""
    write("index.html", head("Play & Plan Paper | Printable Party Games & Planners",
        "Printable Christmas games, party games and simple planners. Instant download in A4 and US Letter, colour and ink-saver. Print at home tonight.",
        "", schema=schema) + body + FOOT)


def post_card(g):
    return (f'<a class="post" href="/ideas/{g["slug"]}/"><div class="ph"><img src="/img/p/{g["image"]}" alt="" loading="lazy" width="900" height="900"></div>'
            f'<span class="cat">{e(g["cat"])}</span><h3>{e(g["title"])}</h3><p>{e(g["teaser"])}</p></a>')


def build_hub(key):
    h = HUBS[key]
    items = [p for p in PRODUCTS if p["cat"] == key]
    cr, cs = crumbs([(h["h1"], None)])
    schema = [cs]
    chips = ""
    if h.get("chips"):
        chips = '<div class="chips" role="group" aria-label="Filter">' + "".join(
            f'<button type="button" aria-pressed="{"true" if v == "all" else "false"}" data-f="{v}">{e(l)}</button>' for v, l in h["chips"]) + "</div>"
    extra = ""
    if key == "christmas":
        extra = f"""
<section>
  <div class="wrap">
    <div class="sec-head"><div class="stack"><p class="eyebrow">Not sure which to pick?</p><h2>Find the right Christmas pack</h2></div></div>
    <div class="tbl-wrap"><table>
      <thead><tr><th>If you're hosting…</th><th>Best pack</th><th>Group size</th><th>Time to play</th></tr></thead>
      <tbody>
        <tr><td>A big family Christmas Day</td><td><a href="/p/ultimate-christmas-games-bundle/"><b>Ultimate Christmas Games Bundle</b></a></td><td>4–30</td><td>All afternoon</td></tr>
        <tr><td>A grown-ups' party</td><td><a href="/p/christmas-party-games/"><b>Christmas Party Games</b></a></td><td>6–20</td><td>1–2 hours</td></tr>
        <tr><td>A quiz night</td><td><a href="/p/christmas-family-quiz/"><b>Christmas Family Quiz</b></a></td><td>4–30</td><td>45–90 min</td></tr>
        <tr><td>A quiet night with the kids</td><td><a href="/p/kids-christmas-bundle/"><b>Kids' Christmas Fun Bundle</b></a></td><td>1–6</td><td>30–60 min</td></tr>
        <tr><td>The work Christmas do</td><td><a href="/p/office-christmas-party/"><b>Office Christmas Party Pack</b></a></td><td>8–40</td><td>1 hour</td></tr>
        <tr><td>A class at school</td><td><a href="/p/classroom-christmas/"><b>Classroom Christmas Pack</b></a></td><td>Up to 30</td><td>One lesson</td></tr>
      </tbody>
    </table></div>
  </div>
</section>
<section style="padding-top:0"><div class="wrap"><div class="sec-head"><div class="stack"><p class="eyebrow">Questions</p><h2>Christmas games FAQ</h2></div></div>{faq_block(XMAS_FAQ, schema)}</div></section>"""
    body = f"""
<div class="wrap">
  {cr}
  <div class="hub-head"><h1>{e(h["h1"])}</h1><p>{e(h["lede"])}</p></div>
  {chips}
  <div class="grid" id="hub-grid">{"".join(card(p) for p in items)}</div>
</div>
{extra}
<section><div class="wrap"><p class="assure">All products are sold and delivered through our <a href="{SHOP}">Etsy shop</a>.</p></div></section>
"""
    write(f'{h["path"]}/index.html', head(h["title"] + " | Play & Plan Paper", h["meta"], h["path"] + "/", schema=schema) + body + FOOT)


def related(p):
    same = [x for x in PRODUCTS if x["cat"] == p["cat"] and x["slug"] != p["slug"]]
    return same[:4]


def build_product(p):
    hub = HUBS[p["cat"]]
    cr, cs = crumbs([(hub["h1"], hub["path"] + "/"), (p["name"], None)])
    n = img_count(p["slug"])
    imgs = [f"/img/p/{p['slug']}-{i + 1}.jpg" for i in range(n)]
    first_para = next((l.strip() for l in p["description"].splitlines() if l.strip()), "")
    meta = (first_para[:150].rsplit(" ", 1)[0] + "…") if len(first_para) > 155 else first_para
    thumbs = "".join(
        f'<button type="button" aria-pressed="{"true" if i == 0 else "false"}" data-src="{src}" aria-label="Photo {i + 1}"><img src="{src}" alt="" loading="lazy"></button>'
        for i, src in enumerate(imgs)) if n > 1 else ""
    body = f"""
<div class="wrap">
  {cr}
  <div class="pdp">
    <div class="gallery">
      <div class="main"><img id="pdp-main" src="{imgs[0]}" alt="{e(p['name'])} printable" width="900" height="900"></div>
      <div class="thumbs">{thumbs}</div>
    </div>
    <div class="buybox">
      <p class="eyebrow">{e(hub['nav'])} · {e(p.get('kind', 'printable PDF'))}</p>
      <h1>{e(p['name'])}</h1>
      <p class="lede-sm">{e(first_para)}</p>
      <a class="btn btn-pri" href="{p['etsy']}" rel="noopener">See price &amp; buy on Etsy</a>
      <dl class="spec"><dt>Format</dt><dd>{e(p.get("format", "Digital PDF download"))}</dd><dt>Sizes</dt><dd>{e(p.get("sizes", "A4 and US Letter"))}</dd><dt>Versions</dt><dd>{e(p.get("versions", "Full colour + ink-saver"))}</dd><dt>Delivery</dt><dd>Instant, straight after checkout</dd></dl>
      <p class="assure">{e(p.get("assure", "Secure checkout through Etsy. Print as many copies as you need for your own household."))}</p>
    </div>
  </div>
  <div class="desc">{desc_html(p['description'].split(chr(10), 1)[1] if chr(10) in p['description'] else '')}</div>
</div>
<section>
  <div class="wrap">
    <div class="sec-head"><div class="stack"><p class="eyebrow">You might also like</p><h2>More {e(hub['nav'].lower())}</h2></div><a class="btn btn-sec btn-sm" href="/{hub['path']}/">See all →</a></div>
    <div class="grid">{"".join(card(x) for x in related(p))}</div>
  </div>
</section>
"""
    write(f"p/{p['slug']}/index.html",
          head(f"{p['name']} Printable | Play & Plan Paper", meta, f"p/{p['slug']}/", og_img=imgs[0][1:], og_type="product", schema=[cs]) + body + FOOT)


def build_guides():
    cr, cs = crumbs([("Ideas", None)])
    body = f"""
<div class="wrap">
  {cr}
  <div class="hub-head"><h1>Party ideas &amp; guides</h1><p>Game ideas, hosting tips and planning help, tested at real family parties.</p></div>
  <div class="posts" style="padding-bottom:3rem">{"".join(post_card(g) for g in GUIDES)}</div>
</div>"""
    write("ideas/index.html", head("Party Ideas & Printable Game Guides | Play & Plan Paper",
        "Christmas game ideas, party hosting tips and printable planning guides from Play & Plan Paper.", "ideas/", schema=[cs]) + body + FOOT)
    for g in GUIDES:
        cr, cs = crumbs([("Ideas", "ideas/"), (g["title"], None)])
        schema = [cs, {"@context": "https://schema.org", "@type": "Article", "headline": g["title"],
                       "image": f"{SITE}/img/p/{g['image']}", "datePublished": g["date"], "dateModified": g["date"],
                       "author": {"@type": "Organization", "name": "Play & Plan Paper", "url": SITE + "/"}}]
        toc = "".join(f'<a href="#{sid}">{e(t)}</a>' for sid, t in g["toc"])
        body = f"""
<div class="wrap">
  {cr}
  <div class="article">
    <article class="prose">
      <h1>{e(g['title'])}</h1>
      <p class="by">By Play &amp; Plan Paper · Updated {datetime.date.fromisoformat(g['date']).strftime('%-d %B %Y')} · {g['mins']} min read</p>
      <div class="answer"><b>Quick answer:</b> {e(g['answer'])}</div>
      {g['html']}
      <h2 id="faq">FAQ</h2>
      {faq_block(g['faq'], schema)}
    </article>
    <aside class="toc" aria-label="In this guide"><span class="hand">In this guide</span>{toc}<a href="#faq">FAQ</a></aside>
  </div>
</div>"""
        write(f"ideas/{g['slug']}/index.html",
              head(g["seo_title"], g["meta"], f"ideas/{g['slug']}/", og_img="img/p/" + g["image"], og_type="article", schema=schema) + body + FOOT)


def build_about():
    cr, cs = crumbs([("About", None)])
    body = f"""
<div class="wrap" style="padding-bottom:3rem">
  {cr}
  <div class="prose" style="padding-top:1rem">
    <h1>About Play &amp; Plan Paper</h1>
    <p>Play &amp; Plan Paper is a small printables shop based in Manchester, England. We make party games and planners that you can buy, download and print in minutes, so the fun part of hosting starts sooner.</p>
    <h2>What makes our printables different</h2>
    <ul><li>Every pack comes in A4 and US Letter, with UK spellings in the A4 edition and US spellings in the Letter edition.</li><li>There is an ink-saver version of every page, because colour ink is expensive.</li><li>Games are written to work for mixed ages, so nobody sits out.</li><li>Pages are checked by hand before they go in the shop.</li></ul>
    <h2>How to buy</h2>
    <p>All our printables are sold through our <a href="{SHOP}">Etsy shop</a>, which handles payment and delivers your download straight away.</p>
    <h2>Get in touch</h2>
    <p>Questions, a problem with a file, or an idea for a game you'd like us to make? Message us on Etsy or email <span class="mail-inline">hello@playandplanpaper.com</span>.</p>
  </div>
</div>"""
    write("about/index.html", head("About Play & Plan Paper | Printable Games & Planners",
        "Play & Plan Paper is a Manchester printables shop making party games and planners in A4 and US Letter, with ink-saver versions.", "about/", schema=[cs]) + body + FOOT)


def build_404():
    body = """<div class="wrap" style="padding-block:4rem"><div class="prose"><h1>That page has wandered off</h1><p>It may have moved. Try the <a href="/christmas-games/">Christmas games</a>, <a href="/party-games/">party games</a> or <a href="/planners/">planners</a>, or go back to the <a href="/">home page</a>.</p></div></div>"""
    write("404.html", head("Page not found | Play & Plan Paper", "This page could not be found.", "404.html").replace('<link rel="canonical"', '<meta name="robots" content="noindex">\n<link rel="canonical"') + body + FOOT)


def build_seo_files():
    urls = ["", "christmas-games/", "party-games/", "planners/", "ideas/", "about/"] + [f"p/{p['slug']}/" for p in PRODUCTS] + [f"ideas/{g['slug']}/" for g in GUIDES]
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
        f"  <url><loc>{SITE}/{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls) + "</urlset>\n"
    write("sitemap.xml", xml)
    write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /_build/\n\nSitemap: {SITE}/sitemap.xml\n")
    write("_headers", "/img/*\n  Cache-Control: public, max-age=2592000\n/style.css\n  Cache-Control: public, max-age=604800\n/site.js\n  Cache-Control: public, max-age=604800\n/_build/*\n  X-Robots-Tag: noindex\n")
    write("_redirects", "/shop " + SHOP + " 302\n/etsy " + SHOP + " 302\n/pinterest " + PINTEREST + " 302\n/tiktok " + TIKTOK + " 302\n")


def build_assets():
    css = (B / "base.css").read_text() + (B / "extra.css").read_text()
    write("style.css", css)
    shutil.copy(B / "site.js", ROOT / "site.js")


if __name__ == "__main__":
    build_assets()
    build_home()
    for k in HUBS:
        build_hub(k)
    for p in PRODUCTS:
        build_product(p)
    build_guides()
    build_about()
    build_404()
    build_seo_files()
    print("Built", 6 + len(PRODUCTS) + len(GUIDES), "pages")
