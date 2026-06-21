#!/usr/bin/env python3
"""Generates Dana Komsky's portfolio prototype: index, about, and project pages."""
import os, glob

ROOT = os.path.dirname(os.path.abspath(__file__))

# ---- Project data ---------------------------------------------------------
# `role/brief/did/outcome` use [brackets] for facts only Dana can confirm.
# `accent` drives that project's color system. `hero` = thumbnail filename.
PROJECTS = [
    {
        "slug": "new-york-knicks",
        "title": "Knicks 2025–26 Season Branding",
        "client": "New York Knicks / MSG",
        "group": "Brand & Identity",
        "tag": "Brand identity",
        "accent": "#F36A1D",
        "hero": "01.jpg",
        "role": "Brand Designer, New York Knicks (Madison Square Garden)",
        "brief": "Build the look that carries the Knicks' 2025–26 season across the city, from the arena to the sidewalk.",
        "did": "Designed the season's “New York Forever” brand system and extended it onto real-world touchpoints like the Chase schedule cart, totes, and game collateral so the identity lived where fans actually are.",
        "outcome": "Part of the 2025–26 Knicks brand system I lead across social, OOH, digital, packaging, and in-arena.",
        "featured": True,
    },
    {
        "slug": "copy-of-new-york-knicks-2024-25-season-branding",
        "title": "NY Knicks Street Signs",
        "client": "New York Knicks / MSG",
        "group": "Brand & Identity",
        "tag": "Campaign · Clio winner",
        "accent": "#1E50FF",
        "hero": "01.jpg",
        "role": "Brand Designer, New York Knicks",
        "brief": "Give the Knicks' 2025 playoff run a citywide moment worthy of the team.",
        "did": "Created the street-sign campaign that renamed New York corners for Knicks stars, like Jalen Brunson Boulevard, turning player tributes into pieces of city iconography.",
        "outcome": "Won a 2025 Clio Sports Award, Silver for Fan Engagement in Experience & Activation.",
    },
    {
        "slug": "new-york-rangers-23-24",
        "title": "Rangers 2023–24 Season Branding",
        "client": "New York Rangers / MSG",
        "group": "Brand & Identity",
        "tag": "Brand identity",
        "accent": "#E5283B",
        "hero": "01.jpg",
        "role": "Brand Designer, Madison Square Garden",
        "brief": "Define the visual identity for the Rangers' full 2023–24 season.",
        "did": "Built and maintained the season's visual identity system and applied it across the Madison Square Garden environment, including the arena jumbotron and in-game graphics.",
        "outcome": "Carried across the Rangers' 2023–24 season in-arena, on social, and in game graphics.",
    },
    {
        "slug": "jr-knicks",
        "title": "Jr. Knicks Rebrand",
        "client": "New York Knicks / MSG",
        "group": "Brand & Identity",
        "tag": "Rebrand",
        "accent": "#FF9500",
        "hero": "01.jpg",
        "role": "Brand Designer, New York Knicks",
        "brief": "Refresh the Jr. Knicks identity for a young audience without losing the Knicks DNA.",
        "did": "Reworked the youth brand and designed a run of social content, keeping the energy high and the system flexible enough for a constant posting cadence.",
        "outcome": "Published across the @juniorknicks social channels, with posts reaching thousands of engagements each.",
    },
    {
        "slug": "discover-student-card-campaign",
        "title": "Discover® Student Card Art",
        "client": "Discover® × @colorintheworld",
        "group": "Illustration & Campaigns",
        "tag": "Illustration / Campaign",
        "accent": "#FF2E93",
        "hero": "01.png",
        "role": "Brand Designer & Content Creator (freelance)",
        "brief": "Design student debit-card art for a national Discover Student Card campaign.",
        "did": "Designed original card concepts in my own color-forward style and created the social content that carried the national campaign.",
        "outcome": "Two of my card designs were selected for permanent circulation, and the campaign's social content reached approximately 75 million consumers.",
    },
    {
        "slug": "new-york-knicks-2025-holiday-card",
        "title": "Knicks 2025 Holiday Card",
        "client": "New York Knicks / MSG",
        "group": "Illustration & Campaigns",
        "tag": "Illustration",
        "accent": "#2B54FF",
        "hero": "02.jpg",
        "role": "Brand Designer, New York Knicks",
        "brief": "Create a Knicks holiday card that feels warm and on-brand.",
        "did": "Illustrated a Knicks gingerbread sticker sheet, blending team marks with holiday charm in the orange-and-blue palette.",
        "outcome": "One of the illustrated holiday pieces I design for the Knicks.",
    },
    {
        "slug": "ny-rangers-holiday-cards-2023-2024",
        "title": "Rangers Holiday Cards, 2022–23",
        "client": "New York Rangers / MSG",
        "group": "Illustration & Campaigns",
        "tag": "Illustration",
        "accent": "#C8102E",
        "hero": "01.jpg",
        "role": "Designer & illustrator, Madison Square Garden",
        "brief": "Design the Rangers' holiday cards across two seasons.",
        "did": "Hand-painted holiday scenes: fans sledding down a Garden-shaped hill, a marshmallow snowman in Rangers cocoa. The brand becomes a story instead of a logo lockup.",
        "outcome": "Illustrated holiday cards designed for the Rangers across the 2022 and 2023 seasons.",
    },
    {
        "slug": "msg-arena-food-and-beverage-packaging",
        "title": "MSG Arena F&B Packaging",
        "client": "Madison Square Garden",
        "group": "Packaging & Concept",
        "tag": "Packaging",
        "accent": "#1230A8",
        "hero": "01.jpg",
        "role": "Brand Designer, Madison Square Garden",
        "brief": "Design food and beverage packaging sold inside Madison Square Garden.",
        "did": "Designed concession packaging, including the Rangers Centennial popcorn boxes, that reads instantly on a busy concourse and photographs well in a fan's hand.",
        "outcome": "Part of the food and beverage creative I design for Madison Square Garden.",
    },
    {
        "slug": "aura-headache-relief",
        "title": "Aura Headache Relief",
        "client": "BFA capstone · Queens College, CUNY · self-directed",
        "group": "Packaging & Concept",
        "tag": "Concept / Branding",
        "accent": "#7A3CFF",
        "hero": "01.png",
        "role": "Brand designer (self-directed)",
        "brief": "A self-initiated brand and product concept for a modern headache-relief line.",
        "did": "Built the full concept end to end: naming direction, identity, and a moody, neon-lit campaign that treats a pharmacy product like a beauty brand. The brief was mine, so this is the clearest look at how I think when nobody's handing me the lines.",
        "outcome": "Senior capstone project. Concept work, not a shipped product.",
    },
]

GROUPS = ["Brand & Identity", "Illustration & Campaigns", "Packaging & Concept"]
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Caveat:wght@600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">')

REVEAL_JS = """
<script>
(function(){
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  // Scroll reveal
  if (!reduce) {
    var io = new IntersectionObserver(function(es){
      es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
    }, {threshold: .12, rootMargin: '0px 0px -40px 0px'});
    document.querySelectorAll('[data-reveal]').forEach(function(el){ io.observe(el); });
  } else {
    document.querySelectorAll('[data-reveal]').forEach(function(el){ el.classList.add('in'); });
  }
  // Squiggle: draw the stroke in proportion to scroll position
  var sq = document.querySelector('.squiggle path');
  if (sq) {
    var LEN = 380;
    if (reduce) {
      sq.style.strokeDashoffset = 0;
    } else {
      var queued = false;
      var drawSquiggle = function(){
        queued = false;
        // draws over the first ~320px of scroll: undrawn at top, full once scrolled past
        var sy = window.pageYOffset || document.documentElement.scrollTop || 0;
        var p = Math.max(0, Math.min(1, sy / 320));
        sq.style.strokeDashoffset = String(LEN * (1 - p));
      };
      var onScroll = function(){ if (!queued) { queued = true; requestAnimationFrame(drawSquiggle); } };
      window.addEventListener('scroll', onScroll, {passive:true});
      window.addEventListener('resize', onScroll);
      drawSquiggle();
    }
  }
  // Party mode: toggle + persistence across pages
  var setParty = function(on){
    document.documentElement.classList.toggle('party', on);
    try { localStorage.setItem('party', on ? '1' : '0'); } catch(e){}
    document.querySelectorAll('.party-toggle').forEach(function(b){
      b.setAttribute('aria-pressed', on ? 'true' : 'false');
      b.classList.toggle('on', on);
      b.textContent = on ? '🪩 Party Mode: on' : '🪩 Party Mode';
    });
  };
  setParty(document.documentElement.classList.contains('party'));
  document.querySelectorAll('.party-toggle').forEach(function(b){
    b.addEventListener('click', function(){
      setParty(!document.documentElement.classList.contains('party'));
    });
  });

  // Project carousel arrows
  document.querySelectorAll('.carousel').forEach(function(c){
    var track = c.querySelector('.car-track');
    if (!track) return;
    var step = function(){ return Math.min(track.clientWidth * 0.8, 384); };
    var prev = c.querySelector('.prev'), next = c.querySelector('.next');
    if (prev) prev.addEventListener('click', function(){ track.scrollBy({left: -step(), behavior: 'smooth'}); });
    if (next) next.addEventListener('click', function(){ track.scrollBy({left: step(), behavior: 'smooth'}); });
  });

  // Color-dot cursor (desktop, fine pointer only)
  if (window.matchMedia('(hover:hover) and (pointer:fine)').matches) {
    var dot = document.createElement('div');
    dot.className = 'cursor-dot';
    document.body.appendChild(dot);
    document.documentElement.classList.add('cursor-on');
    var x = innerWidth/2, y = innerHeight/2, cx = x, cy = y;
    var ease = reduce ? 1 : 0.2;
    addEventListener('mousemove', function(e){ x = e.clientX; y = e.clientY; });
    (function loop(){
      cx += (x - cx) * ease; cy += (y - cy) * ease;
      dot.style.transform = 'translate(' + cx + 'px,' + cy + 'px)';
      requestAnimationFrame(loop);
    })();
    var grow = function(){ dot.classList.add('grow'); };
    var shrink = function(){ dot.classList.remove('grow'); };
    document.querySelectorAll('a, button, .card, .feat-card, .next-proj').forEach(function(el){
      el.addEventListener('mouseenter', grow);
      el.addEventListener('mouseleave', shrink);
    });
    // Rainbow cursor trail — party mode only
    var lastTrail = 0;
    window.addEventListener('mousemove', function(e){
      if (!document.documentElement.classList.contains('party')) return;
      var now = Date.now();
      if (now - lastTrail < 45) return;
      lastTrail = now;
      var t = document.createElement('div');
      t.className = 'trail';
      t.style.left = e.clientX + 'px';
      t.style.top = e.clientY + 'px';
      t.style.background = 'hsl(' + (now / 6 % 360) + ',95%,60%)';
      document.body.appendChild(t);
      setTimeout(function(){ t.remove(); }, 650);
    }, {passive:true});
  }
})();
</script>"""

_TICK_ITEMS = ["New York Knicks", "2025 Clio Award Winner", "Madison Square Garden",
               "Discover® Student Card", "80K+ Followers", "≈75M Consumers Reached",
               "New York Rangers", "BFA · Summa Cum Laude", "@colorintheworld"]
_tg = "".join('<span class="tick">' + i + '</span><i class="sep">✦</i>' for i in _TICK_ITEMS)
TICKER = '<div class="ticker"><div class="ticker-track">' + _tg + _tg + '</div></div>'

def _disco_svg():
    """A silver mirror-tile disco ball, generated as inline SVG."""
    import random
    cx, cy, r = 60, 70, 52
    random.seed(11)
    step, t = 7.6, 6.6
    rects = []
    y = cy - r
    while y <= cy + r:
        x = cx - r
        while x <= cx + r:
            mx, my = x + t / 2, y + t / 2
            if ((mx - cx) ** 2 + (my - cy) ** 2) ** 0.5 <= r - 1.2:
                rv = random.random()
                if rv < 0.05:
                    fill = "#ffffff"
                elif rv < 0.15:
                    fill = random.choice(["#5b6678", "#6f7b8d", "#4f5969"])
                else:
                    fill = random.choice(["#fbfdff", "#eef2f8", "#dde5ee", "#c9d2dd",
                                          "#b3bdca", "#9ca7b6", "#e6ebf2", "#d3dbe5"])
                rects.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="0.5" fill="%s"/>'
                             % (x + 0.5, y + 0.5, t, t, fill))
            x += step
        y += step
    facets = "".join(rects)
    return ('<svg viewBox="0 0 120 142" xmlns="http://www.w3.org/2000/svg">'
            '<defs>'
            '<clipPath id="cb"><circle cx="60" cy="70" r="52"/></clipPath>'
            '<radialGradient id="dhl" cx="36%" cy="32%" r="55%">'
            '<stop offset="0%" stop-color="#fff" stop-opacity="0.95"/>'
            '<stop offset="45%" stop-color="#fff" stop-opacity="0.12"/>'
            '<stop offset="100%" stop-color="#fff" stop-opacity="0"/></radialGradient>'
            '<radialGradient id="dsh" cx="40%" cy="36%" r="64%">'
            '<stop offset="52%" stop-color="#000" stop-opacity="0"/>'
            '<stop offset="100%" stop-color="#070a12" stop-opacity="0.62"/></radialGradient>'
            '</defs>'
            '<rect x="59" y="8" width="2" height="13" fill="#c7d0db"/>'
            '<circle cx="60" cy="10" r="4.5" fill="none" stroke="#cdd6e0" stroke-width="2"/>'
            '<g clip-path="url(#cb)">'
            '<circle cx="60" cy="70" r="52" fill="#39414f"/>'
            + facets +
            '<circle cx="60" cy="70" r="52" fill="url(#dsh)"/>'
            '<ellipse cx="45" cy="53" rx="30" ry="26" fill="url(#dhl)"/>'
            '</g></svg>')

DISCO_BALL = _disco_svg()

# ---- Helpers --------------------------------------------------------------
def imgs_for(slug):
    files = sorted(glob.glob(os.path.join(ROOT, "images", slug, "*")))
    return [os.path.basename(f) for f in files]

def head(title, prefix=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow"><!-- preview only: remove before launching on danakomsky.com -->
<title>{title}</title>
{FONTS}
<link rel="stylesheet" href="{prefix}style.css">
<script>try{{if(localStorage.getItem('party')==='1')document.documentElement.classList.add('party');}}catch(e){{}}</script>
</head>
<body>"""

def nav(prefix=""):
    return f"""
<div class="lasers" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i></div>
<div class="strobe" aria-hidden="true"></div>
<div class="disco-light" aria-hidden="true"></div>
<div class="disco" aria-hidden="true"><div class="disco-rope"><span class="disco-cord"></span><span class="disco-ball">{DISCO_BALL}</span></div></div>
<svg class="defs" width="0" height="0" aria-hidden="true"><defs><filter id="goo"><feGaussianBlur in="SourceGraphic" stdDeviation="18" result="b"/><feColorMatrix in="b" type="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 16 -7" result="g"/><feBlend in="SourceGraphic" in2="g"/></filter></defs></svg>
<div class="colorbar"></div>
<header class="nav">
  <a class="brand" href="{prefix}index.html">Dana Komsky</a>
  <nav>
    <a href="{prefix}index.html#work">Work</a>
    <a href="{prefix}about.html">About</a>
    <a href="https://www.instagram.com/colorintheworld/" target="_blank" rel="noopener">Art</a>
    <a href="{prefix}dana-komsky-resume.pdf" target="_blank" rel="noopener">Résumé</a>
    <button class="party-toggle" type="button" aria-pressed="false">🪩 Party Mode</button>
    <a class="nav-cta" href="mailto:dekomsky@gmail.com">Contact</a>
  </nav>
</header>
<div class="party-wrap">"""

def footer(prefix=""):
    return f"""
<footer class="footer" id="contact">
  <div class="footer-big" data-reveal>Let's make something<br>worth a <span class="hl">second look.</span></div>
  <div class="footer-links" data-reveal>
    <a href="mailto:dekomsky@gmail.com">dekomsky@gmail.com</a>
    <a href="https://www.linkedin.com/in/dana-komsky/" target="_blank" rel="noopener">LinkedIn</a>
    <a href="https://www.instagram.com/colorintheworld/" target="_blank" rel="noopener">Instagram</a>
    <a href="https://www.tiktok.com/@colorintheworld" target="_blank" rel="noopener">TikTok</a>
  </div>
  <div class="footer-fine">Open to full-time design roles and select freelance. New York, NY.</div>
</footer>
{TICKER}
</div>
{REVEAL_JS}
</body></html>"""

# ---- Index ----------------------------------------------------------------
def build_index():
    cards = ""
    for g in GROUPS:
        group_cards = "".join(
            f'<a class="card" data-reveal href="work/{p["slug"]}.html" style="--accent:{p["accent"]}">'
            f'<div class="card-img"><img loading="lazy" src="images/{p["slug"]}/{p["hero"]}" alt="{p["title"]}"></div>'
            f'<div class="card-meta"><span class="card-title">{p["title"]}</span><span class="card-tag">{p["tag"]}</span></div>'
            f'</a>'
            for p in PROJECTS if p["group"] == g
        )
        cards += f'<h3 class="group-label" data-reveal>{g}</h3>\n<div class="grid">{group_cards}</div>\n'

    squiggle = ('<svg class="squiggle" viewBox="0 0 320 22" fill="none" preserveAspectRatio="none" aria-hidden="true">'
                '<path d="M4 14 C 54 4, 96 20, 150 11 S 250 3, 316 13" stroke="url(#sg)" stroke-width="6" stroke-linecap="round"/>'
                '<defs><linearGradient id="sg" x1="0" y1="0" x2="1" y2="0">'
                '<stop offset="0" stop-color="#F36A1D"/><stop offset=".4" stop-color="#FF2E93"/>'
                '<stop offset=".7" stop-color="#7A3CFF"/><stop offset="1" stop-color="#1E50FF"/>'
                '</linearGradient></defs></svg>')
    html = head("Dana Komsky — Brand & Graphic Designer") + nav() + f"""
<section class="hero">
  <div class="blobs" aria-hidden="true"><span></span><span></span><span></span><span></span></div>
  <div class="hero-inner">
    <div class="hero-text">
      <span class="hand-note" data-reveal>color in the world<svg viewBox="0 0 60 40" fill="none" aria-hidden="true"><path d="M55 4 C 30 6, 8 14, 6 33 M6 33 L2 24 M6 33 L15 30" stroke="#FF2E93" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
      <p class="hero-kicker" data-reveal>Brand &amp; graphic designer · New York</p>
      <h1 class="hero-h1" data-reveal>I design brand, packaging, and campaigns that make people <span class="hl">look twice.</span>{squiggle}</h1>
      <p class="hero-sub" data-reveal>Brand Designer for the New York Knicks at Madison Square Garden, and founder of <a href="https://www.instagram.com/colorintheworld/" target="_blank" rel="noopener">@colorintheworld</a> (80K+ followers). I love work that lets me think in color and concept, not just execute.</p>
      <div class="hero-actions" data-reveal><a class="btn" href="#work">See the work</a><a class="btn ghost" href="mailto:dekomsky@gmail.com">Get in touch</a></div>
    </div>
    <div class="hero-portrait" data-reveal>
      <img class="star-halo" src="images/star-burst.png" alt="" aria-hidden="true">
      <img class="portrait-flat" src="images/star-composite.png" alt="Dana Komsky">
    </div>
  </div>
</section>

<section class="work" id="work">
  <div class="section-head" data-reveal><h2>Selected work</h2><p>Sports brands, seasonal campaigns, packaging, and concept work.</p></div>
  {cards}
</section>
""" + footer()
    open(os.path.join(ROOT, "index.html"), "w").write(html)

# ---- About ----------------------------------------------------------------
def build_about():
    html = head("About — Dana Komsky") + nav() + """
<section class="about">
  <div class="about-grid">
    <div class="about-copy">
      <p class="hero-kicker" data-reveal>About</p>
      <h1 data-reveal>Hi, I'm Dana.</h1>
      <p data-reveal>I'm a New York-based brand and graphic designer with a love for color and ideas that make people look twice.</p>
      <p data-reveal>I'm the Brand Designer for the New York Knicks at Madison Square Garden, leading 360 brand experiences across social, out-of-home, digital, packaging, and in-arena. My NY Knicks street-sign campaign won a 2025 Clio Sports Award, Silver for Fan Engagement.</p>
      <p data-reveal>I also founded <a href="https://www.instagram.com/colorintheworld/" target="_blank" rel="noopener">@colorintheworld</a>, a color-first art brand with 80K+ followers and 1.2M+ TikTok likes, where I've partnered with Prismacolor, Discover, Arteza, and Blick. I hold a BFA in Design from Queens College, CUNY, where I graduated summa cum laude with highest honors.</p>
      <p data-reveal>I'm drawn to work that gives me room to think differently and find the unexpected angle. When I'm not designing, I'm doing photography, traveling, hiking, listening to music, and hunting for a sitcom that gets as many laughs as The Office.</p>
      <div class="about-links" data-reveal>
        <a class="btn" href="mailto:dekomsky@gmail.com">Email me</a>
        <a class="btn ghost" href="dana-komsky-resume.pdf" target="_blank" rel="noopener">Résumé</a>
        <a class="btn ghost" href="https://www.linkedin.com/in/dana-komsky/" target="_blank" rel="noopener">LinkedIn</a>
        <a class="btn ghost" href="https://danakphotos.com" target="_blank" rel="noopener">Photography</a>
      </div>
    </div>
    <div class="about-facts">
      <div class="fact" data-reveal><span class="fact-n">2025 Clio</span><span class="fact-l">Sports Award, Silver for Fan Engagement (Knicks Street Signs)</span></div>
      <div class="fact" data-reveal><span class="fact-n">80K+</span><span class="fact-l">followers, 1.2M+ TikTok likes as @colorintheworld</span></div>
      <div class="fact" data-reveal><span class="fact-n">~75M</span><span class="fact-l">consumers reached, Discover Student Card campaign</span></div>
      <div class="fact" data-reveal><span class="fact-n">BFA</span><span class="fact-l">Design, Queens College CUNY, summa cum laude</span></div>
    </div>
  </div>
</section>
""" + footer()
    open(os.path.join(ROOT, "about.html"), "w").write(html)

# ---- Project pages --------------------------------------------------------
def build_projects():
    os.makedirs(os.path.join(ROOT, "work"), exist_ok=True)
    for i, p in enumerate(PROJECTS):
        imgs = imgs_for(p["slug"])
        nxt = PROJECTS[(i + 1) % len(PROJECTS)]
        gallery = ""
        for im in imgs:
            gallery += f'    <img loading="lazy" data-reveal src="../images/{p["slug"]}/{im}" alt="{p["title"]}">\n'
        html = head(f"{p['title']} · Dana Komsky", prefix="../") + nav("../") + f"""
<article class="project" style="--accent:{p['accent']}">
  <div class="proj-head">
    <a class="back" href="../index.html#work">&larr; All work</a>
    <span class="proj-tag" data-reveal>{p['tag']}</span>
    <h1 data-reveal>{p['title']}</h1>
    <p class="proj-client" data-reveal>{p['client']}</p>
  </div>
  <div class="proj-brief" data-reveal>
    <div class="brief-row"><span class="brief-k">Role</span><span class="brief-v">{p['role']}</span></div>
    <div class="brief-row"><span class="brief-k">The brief</span><span class="brief-v">{p['brief']}</span></div>
    <div class="brief-row"><span class="brief-k">What I did</span><span class="brief-v">{p['did']}</span></div>
    <div class="brief-row"><span class="brief-k">Outcome</span><span class="brief-v">{p['outcome']}</span></div>
  </div>
  <div class="proj-gallery">
{gallery}  </div>
  <a class="next-proj" href="{nxt['slug']}.html" style="--accent:{nxt['accent']}">
    <span class="next-label">Next project</span>
    <span class="next-title">{nxt['title']} <span class="arr">&rarr;</span></span>
  </a>
</article>
""" + footer("../")
        open(os.path.join(ROOT, "work", p["slug"] + ".html"), "w").write(html)

build_index()
build_about()
build_projects()
print("Built index.html, about.html, and", len(PROJECTS), "project pages.")
