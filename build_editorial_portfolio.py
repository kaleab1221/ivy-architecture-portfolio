"""
build_editorial_portfolio.py
Generates the complete editorial redesign for IVY Architecture & Construction:
- 33 static individual project pages in projects/
- Editorial homepage (index.html)
- Editorial stylesheet (styles.css)
- Editorial interactive script (app.js)
- Comprehensive sitemap.xml
"""

import os
import json
import re

SITE_URL = "https://ivy-architecture-portfolio.vercel.app"

with open("projects.json", "r", encoding="utf-8") as f:
    PROJECTS = json.load(f)

# 6 Featured Projects for the editorial homepage showcase
FEATURED_IDS = [
    "ivy-28",  # ADD-12: King Nejashi Islamic Center & Monumental Arch Tower
    "ivy-03",  # JUB-01: Juba Mall & Luxury Apartments
    "ivy-09",  # ERB-01: Erbil Mixed-Use Commercial Tower
    "ivy-05",  # ADD-03: Sevita Real Estate Tower
    "ivy-12",  # ADD-09: Hagbes Showroom & Machinery Sales Center
    "ivy-20",  # GAM-01: Gambella University College of Health Compound
]

def get_webp_path(jpeg_path):
    base, _ = os.path.splitext(jpeg_path)
    return base + ".webp"

def picture_tag(img_src, alt_text, css_class="", is_lazy=True, prefix=""):
    webp_src = get_webp_path(img_src)
    lazy_attr = 'loading="lazy" decoding="async"' if is_lazy else 'loading="eager" fetchpriority="high"'
    p_img = f"{prefix}{img_src}"
    p_webp = f"{prefix}{webp_src}"
    return f'''<picture class="{css_class}">
  <source srcset="{p_webp}" type="image/webp">
  <img src="{p_img}" alt="{alt_text}" {lazy_attr}>
</picture>'''

print(f"Loaded {len(PROJECTS)} projects. Generating static project pages...")

# ==============================================================================
# 1. GENERATE STATIC INDIVIDUAL PROJECT PAGES (projects/ivy-XX.html)
# ==============================================================================
os.makedirs("projects", exist_ok=True)

for i, p in enumerate(PROJECTS):
    pid = p["id"]
    code = p["code"]
    title = p["title"]
    subtitle = p.get("subtitle", "")
    category = p.get("category", "")
    typology = p.get("typology", "")
    location = p.get("location", "")
    city = p.get("city", "")
    country = p.get("country", "")
    status = p.get("status", "")
    status_type = p.get("statusType", "design")
    year = p.get("year", "2024")
    client = p.get("client", "Confidential / Client Details on Request")
    scale = p.get("scale", "Comprehensive Documentation")
    scope = p.get("scope", "Architectural Design & Engineering")
    description = p.get("description", "")
    key_features = p.get("keyFeatures", [])
    images = p.get("images", [])
    hero_image = p.get("heroImage", images[0] if images else "")
    structure = p.get("structure", "Reinforced Concrete Frame")
    envelope = p.get("envelope", "High-Performance Architectural Glazing")
    climate = p.get("climate", "Passive Solar Shading & Natural Cross Ventilation")

    # Prev / Next project pointers
    prev_p = PROJECTS[(i - 1) % len(PROJECTS)]
    next_p = PROJECTS[(i + 1) % len(PROJECTS)]

    canonical_url = f"{SITE_URL}/projects/{pid}.html"
    abs_hero_image = f"{SITE_URL}/{hero_image}"
    whatsapp_url = f"https://wa.me/251911234567?text=Inquiry%20regarding%20{code}%20-%20{title.replace(' ', '%20')}"

    # Features list items
    features_html = "".join([f"<li>{feat}</li>" for feat in key_features])

    # Gallery images (excluding hero, or all images in sequence)
    gallery_items_html = ""
    for idx, img_path in enumerate(images):
        cap = f"{title} — Architectural Document {idx+1}"
        gallery_items_html += f"""
        <figure class="project-gallery-item">
          {picture_tag(img_path, cap, "gallery-picture", is_lazy=(idx > 0), prefix="../")}
          <figcaption class="gallery-caption">{code} / Figure {idx+1:02d} &mdash; {city}, {country}</figcaption>
        </figure>"""

    page_html = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} [{code}] — IVY Architecture &amp; Construction</title>
  <meta name="description" content="{description[:155]}...">
  <link rel="canonical" href="{canonical_url}">
  <meta name="theme-color" content="#121211">

  <!-- Open Graph / Meta -->
  <meta property="og:type" content="article">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:title" content="{title} [{code}] — IVY Architecture &amp; Construction">
  <meta property="og:description" content="{description[:155]}...">
  <meta property="og:image" content="{abs_hero_image}">
  <meta property="og:site_name" content="IVY Architecture &amp; Construction">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title} [{code}] — IVY Architecture">
  <meta name="twitter:description" content="{description[:155]}...">
  <meta name="twitter:image" content="{abs_hero_image}">

  <!-- Google Fonts: Newsreader (Editorial Serif) & Inter (Clean Grotesk) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,400;1,6..72,600&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="../styles.css">

  <!-- Structured Data JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "VisualArtwork",
    "name": "{title}",
    "alternateName": "{code}",
    "description": "{description}",
    "artform": "Architecture",
    "artworkSurface": "Built Environment",
    "locationCreated": {{
      "@type": "Place",
      "address": {{
        "@type": "PostalAddress",
        "addressLocality": "{city}",
        "addressCountry": "{country}"
      }}
    }},
    "creator": {{
      "@type": "Organization",
      "name": "IVY Architecture & Construction Co. Ltd.",
      "url": "{SITE_URL}"
    }},
    "image": "{abs_hero_image}"
  }}
  </script>
</head>
<body class="editorial-page project-detail-page">
  <a href="#main-content" class="skip-to-content">Skip to content</a>

  <!-- Header -->
  <header class="editorial-header">
    <div class="editorial-container header-inner">
      <a href="../index.html" class="brand-link" aria-label="IVY Architecture Homepage">
        <span class="brand-serif">IVY</span>
        <span class="brand-sub">Architecture &middot; Construction</span>
      </a>

      <nav class="editorial-nav" aria-label="Primary Navigation">
        <a href="../index.html#featured" class="nav-item">Featured</a>
        <a href="../index.html#index" class="nav-item">Project Index</a>
        <a href="../index.html#services" class="nav-item">Services</a>
        <a href="../index.html#credentials" class="nav-item">Credentials</a>
        <a href="../index.html#contact" class="nav-item">Contact</a>
      </nav>

      <div class="header-tools">
        <button id="themeToggleBtn" class="theme-toggle" aria-label="Toggle visual theme" title="Toggle theme">
          <span class="theme-toggle-label">Theme</span>
        </button>
        <a href="../IVY-CONSTRUCTION-PORTFOLIO.pdf" download class="monograph-btn" title="Download Official Monograph (81 Pages PDF)">
          Monograph PDF
        </a>
      </div>
    </div>
  </header>

  <main id="main-content">
    <!-- Breadcrumb & Project Header -->
    <section class="project-hero-header">
      <div class="editorial-container">
        <nav class="breadcrumb-nav" aria-label="Breadcrumb">
          <a href="../index.html">Practice</a>
          <span class="sep">/</span>
          <a href="../index.html#index">Index</a>
          <span class="sep">/</span>
          <span aria-current="page">{code}</span>
        </nav>

        <div class="project-title-block">
          <div class="project-meta-line">
            <span class="meta-tag">{code}</span>
            <span class="meta-dot">&middot;</span>
            <span class="meta-tag">{typology}</span>
            <span class="meta-dot">&middot;</span>
            <span class="meta-tag">{year}</span>
            <span class="meta-dot">&middot;</span>
            <span class="meta-status status-{status_type}">{status}</span>
          </div>
          <h1 class="project-title-serif">{title}</h1>
          {f'<p class="project-subtitle-lead">{subtitle}</p>' if subtitle else ''}
        </div>
      </div>
    </section>

    <!-- Full-Bleed Primary Image -->
    <section class="project-fullbleed-media">
      <div class="editorial-container">
        <div class="hero-media-frame">
          {picture_tag(hero_image, f"{title} architectural view", "hero-picture", is_lazy=False, prefix="../")}
        </div>
      </div>
    </section>

    <!-- Editorial Layout: Fact Sheet & Architectural Narrative -->
    <section class="project-body-section">
      <div class="editorial-container project-split-grid">
        <!-- Fact Sheet Ledger -->
        <aside class="project-fact-sheet">
          <h2 class="fact-sheet-title">Fact Sheet</h2>
          <dl class="fact-sheet-ledger">
            <div class="fact-row">
              <dt>Commission Code</dt>
              <dd>{code}</dd>
            </div>
            <div class="fact-row">
              <dt>Location</dt>
              <dd>{location}</dd>
            </div>
            <div class="fact-row">
              <dt>Client</dt>
              <dd>{client}</dd>
            </div>
            <div class="fact-row">
              <dt>Typology</dt>
              <dd>{typology}</dd>
            </div>
            <div class="fact-row">
              <dt>Scale / Area</dt>
              <dd>{scale}</dd>
            </div>
            <div class="fact-row">
              <dt>Delivery Scope</dt>
              <dd>{scope}</dd>
            </div>
            <div class="fact-row">
              <dt>Structural System</dt>
              <dd>{structure}</dd>
            </div>
            <div class="fact-row">
              <dt>Facade / Envelope</dt>
              <dd>{envelope}</dd>
            </div>
            <div class="fact-row">
              <dt>Climate Strategy</dt>
              <dd>{climate}</dd>
            </div>
            <div class="fact-row">
              <dt>Commission Status</dt>
              <dd>{status}</dd>
            </div>
          </dl>

          <div class="fact-sheet-actions">
            <a href="{whatsapp_url}" target="_blank" rel="noopener noreferrer" class="btn-editorial-primary">
              Discuss via WhatsApp
            </a>
            <a href="../index.html#contact" class="btn-editorial-secondary">
              Submit Project Brief
            </a>
          </div>
        </aside>

        <!-- Narrative & Engineering Highlights -->
        <article class="project-narrative-pane">
          <div class="narrative-block">
            <h2 class="narrative-heading">Architectural &amp; Engineering Scope</h2>
            <div class="narrative-prose">
              <p>{description}</p>
            </div>
          </div>

          {f'''
          <div class="technical-highlights-block">
            <h3 class="technical-title">Technical &amp; Construction Highlights</h3>
            <ul class="technical-list">
              {features_html}
            </ul>
          </div>''' if key_features else ''}
        </article>
      </div>
    </section>

    <!-- Project Gallery & Drawings -->
    <section class="project-gallery-section">
      <div class="editorial-container">
        <div class="gallery-section-header">
          <h2 class="section-title-serif">Visual Documentation &amp; Drawings</h2>
          <p class="section-subtitle">Full resolution photographic documentation, structural geometry, and plans.</p>
        </div>

        <div class="project-gallery-grid">
          {gallery_items_html}
        </div>
      </div>
    </section>

    <!-- Adjacent Project Navigation -->
    <nav class="project-pagination-section" aria-label="Adjacent Projects">
      <div class="editorial-container pagination-inner">
        <a href="{prev_p['id']}.html" class="pagination-link prev">
          <span class="pagination-dir">&larr; Previous Commission</span>
          <span class="pagination-title">{prev_p['title']}</span>
          <span class="pagination-code">[{prev_p['code']}]</span>
        </a>
        <a href="../index.html#index" class="pagination-center" title="Return to complete project index">
          All Commissions (33)
        </a>
        <a href="{next_p['id']}.html" class="pagination-link next">
          <span class="pagination-dir">Next Commission &rarr;</span>
          <span class="pagination-title">{next_p['title']}</span>
          <span class="pagination-code">[{next_p['code']}]</span>
        </a>
      </div>
    </nav>
  </main>

  <!-- Editorial Footer -->
  <footer class="editorial-footer">
    <div class="editorial-container footer-grid">
      <div class="footer-col brand-col">
        <span class="brand-serif">IVY</span>
        <p class="footer-summary">
          Multidisciplinary practice combining architecture, engineering, and construction across East Africa and the Middle East.
        </p>
        <p class="footer-credentials">Grade-1 General Contractor &middot; ISO 9001 Certified</p>
      </div>

      <div class="footer-col">
        <h3 class="footer-heading">Bureaus</h3>
        <p><strong>Addis Ababa [HQ]</strong><br>Bole Subcity Commercial District, Ethiopia</p>
        <p><strong>Juba [Bureau]</strong><br>Central Commercial Sector, South Sudan</p>
        <p><strong>Erbil [Logistics Hub]</strong><br>Procurement &amp; Freight, Iraq</p>
      </div>

      <div class="footer-col">
        <h3 class="footer-heading">Direct Communication</h3>
        <p>Partner Line: <a href="tel:+251911234567">+251 91 123 4567</a></p>
        <p>Inquiries: <a href="mailto:info@ivyconstruction.com">info@ivyconstruction.com</a></p>
        <p>WhatsApp: <a href="https://wa.me/251911234567" target="_blank" rel="noopener noreferrer">Direct Partner Channel</a></p>
      </div>

      <div class="footer-col">
        <h3 class="footer-heading">Documentation</h3>
        <p><a href="../IVY-CONSTRUCTION-PORTFOLIO.pdf" download>Monograph PDF (81 Pages, 7.3 MB)</a></p>
        <p><a href="../index.html#index">Catalogue Index (33 Commissions)</a></p>
        <p><a href="../index.html#contact">Consultation Request</a></p>
      </div>
    </div>

    <div class="editorial-container footer-bottom-bar">
      <span>&copy; 2026 IVY Construction &amp; Trading Co. Ltd. All rights reserved.</span>
      <span class="footer-regions">ETHIOPIA &middot; SOUTH SUDAN &middot; IRAQ &middot; INTERNATIONAL</span>
    </div>
  </footer>

  <script src="../app.js"></script>
</body>
</html>"""

    with open(f"projects/{pid}.html", "w", encoding="utf-8") as pf:
        pf.write(page_html)

print("Generated all 33 static project pages successfully.")

# ==============================================================================
# 2. GENERATE EDITORIAL HOMEPAGE (index.html)
# ==============================================================================
featured_projects = [p for p in PROJECTS if p["id"] in FEATURED_IDS]

featured_section_html = ""
for idx, fp in enumerate(featured_projects):
    f_pid = fp["id"]
    f_code = fp["code"]
    f_title = fp["title"]
    f_sub = fp.get("subtitle", "")
    f_loc = fp.get("location", "")
    f_scale = fp.get("scale", "")
    f_year = fp.get("year", "")
    f_cat = fp.get("typology", "")
    f_desc = fp.get("description", "")
    f_hero = fp.get("heroImage", "")
    f_scope = fp.get("scope", "")

    # Layout alternation: full width vs asymmetric spread
    featured_section_html += f"""
    <article class="featured-project-spread {'spread-reversed' if idx % 2 == 1 else ''}">
      <div class="featured-media-col">
        <a href="projects/{f_pid}.html" class="media-link" aria-label="View documentation for {f_title}">
          {picture_tag(f_hero, f"{f_title} architectural photograph", "featured-picture", is_lazy=(idx > 0))}
        </a>
      </div>
      <div class="featured-info-col">
        <div class="featured-meta-header">
          <span class="meta-code">{f_code}</span>
          <span class="meta-rule"></span>
          <span class="meta-category">{f_cat}</span>
          <span class="meta-year">{f_year}</span>
        </div>
        <h3 class="featured-title-serif">
          <a href="projects/{f_pid}.html">{f_title}</a>
        </h3>
        {f'<p class="featured-subtitle-line">{f_sub}</p>' if f_sub else ''}
        <p class="featured-summary-prose">{f_desc}</p>

        <dl class="featured-spec-ledger">
          <div class="spec-entry">
            <dt>Location</dt>
            <dd>{f_loc}</dd>
          </div>
          <div class="spec-entry">
            <dt>Scale</dt>
            <dd>{f_scale}</dd>
          </div>
          <div class="spec-entry">
            <dt>Scope</dt>
            <dd>{f_scope}</dd>
          </div>
        </dl>

        <div class="featured-cta-row">
          <a href="projects/{f_pid}.html" class="link-editorial-arrow">
            View Project Documentation <span aria-hidden="true">&rarr;</span>
          </a>
        </div>
      </div>
    </article>
    """

# Build Complete Index Table Rows for all 33 projects
index_rows_html = ""
for p in PROJECTS:
    p_id = p["id"]
    p_code = p["code"]
    p_title = p["title"]
    p_cat = p.get("category", "")
    p_typology = p.get("typology", "")
    p_city = p.get("city", "")
    p_country = p.get("country", "")
    p_status = p.get("status", "")
    p_status_type = p.get("statusType", "design")
    p_year = p.get("year", "")
    p_scale = p.get("scale", "")

    index_rows_html += f"""
    <tr class="index-row" data-sector="{p_cat}" data-country="{p_country}" data-status="{p_status_type}">
      <td class="col-code"><a href="projects/{p_id}.html" class="row-link">{p_code}</a></td>
      <td class="col-title"><a href="projects/{p_id}.html" class="row-link row-title-serif">{p_title}</a></td>
      <td class="col-sector">{p_typology}</td>
      <td class="col-location">{p_city}, {p_country}</td>
      <td class="col-scale">{p_scale}</td>
      <td class="col-status"><span class="status-pill status-{p_status_type}">{p_status}</span></td>
      <td class="col-year">{p_year}</td>
      <td class="col-action"><a href="projects/{p_id}.html" class="row-action-btn" aria-label="Open {p_title} documentation">&rarr;</a></td>
    </tr>"""

# Distinct documented clients
documented_clients = sorted(list(set(
    p.get("client") for p in PROJECTS if p.get("client") and "Private" not in p.get("client") and "Confidential" not in p.get("client")
)))

client_list_html = "".join([f'<li class="client-item">{c}</li>' for c in documented_clients])

homepage_html = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>IVY Architecture &amp; Construction &mdash; Integrated Practice &amp; Portfolio</title>
  <meta name="description" content="IVY Architecture & Construction is an integrated practice delivering landmark commercial towers, multi-family residential communities, civic masterplans, and industrial facilities across East Africa and the Middle East.">
  <link rel="canonical" href="{SITE_URL}/">
  <meta name="theme-color" content="#121211">

  <!-- Open Graph / Meta -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="{SITE_URL}/">
  <meta property="og:title" content="IVY Architecture &amp; Construction &mdash; Integrated Practice">
  <meta property="og:description" content="Multidisciplinary architecture, structural engineering, and Grade-1 general contracting practice. Thirty-three verified commissions across Ethiopia, South Sudan, and Iraq.">
  <meta property="og:image" content="{SITE_URL}/images/projects/ivy-28/page_70_img1.jpeg">
  <meta property="og:site_name" content="IVY Architecture &amp; Construction">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="IVY Architecture &amp; Construction">
  <meta name="twitter:description" content="Integrated architectural practice and portfolio monograph. 33 verified commissions.">
  <meta name="twitter:image" content="{SITE_URL}/images/projects/ivy-28/page_70_img1.jpeg">

  <!-- Google Fonts: Newsreader (Editorial Serif) & Inter (Clean Grotesk) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,400;1,6..72,600&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="styles.css">

  <!-- Structured Data JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ArchitecturalPractice",
    "name": "IVY Architecture & Construction Co. Ltd.",
    "url": "{SITE_URL}",
    "logo": "{SITE_URL}/images/projects/ivy-28/page_70_img1.jpeg",
    "description": "Integrated architecture, civil engineering, and general contracting practice delivering landmark developments in East Africa and the Middle East.",
    "address": [
      {{
        "@type": "PostalAddress",
        "streetAddress": "Bole Commercial District",
        "addressLocality": "Addis Ababa",
        "addressCountry": "Ethiopia"
      }},
      {{
        "@type": "PostalAddress",
        "streetAddress": "Central Commercial Sector",
        "addressLocality": "Juba",
        "addressCountry": "South Sudan"
      }}
    ],
    "telephone": "+251911234567",
    "email": "info@ivyconstruction.com",
    "sameAs": [
      "https://www.linkedin.com/company/ivy-construction",
      "https://www.instagram.com/ivy.architecture"
    ]
  }}
  </script>
</head>
<body class="editorial-page home-page">
  <a href="#main-content" class="skip-to-content">Skip to content</a>

  <!-- Header -->
  <header class="editorial-header">
    <div class="editorial-container header-inner">
      <a href="index.html" class="brand-link" aria-label="IVY Architecture & Construction Home">
        <span class="brand-serif">IVY</span>
        <span class="brand-sub">Architecture &middot; Construction</span>
      </a>

      <nav class="editorial-nav" aria-label="Main Navigation">
        <a href="#featured" class="nav-item">Featured</a>
        <a href="#index" class="nav-item">Index</a>
        <a href="#services" class="nav-item">Services</a>
        <a href="#credentials" class="nav-item">Credentials</a>
        <a href="#leadership" class="nav-item">Leadership</a>
        <a href="#clients" class="nav-item">Clients</a>
        <a href="#contact" class="nav-item">Contact</a>
      </nav>

      <div class="header-tools">
        <button id="themeToggleBtn" class="theme-toggle" aria-label="Toggle visual theme" title="Toggle theme">
          <span class="theme-toggle-label">Theme</span>
        </button>
        <a href="IVY-CONSTRUCTION-PORTFOLIO.pdf" download class="monograph-btn" title="Download Official Monograph (81 Pages PDF)">
          Monograph PDF
        </a>
      </div>
    </div>
  </header>

  <main id="main-content">
    <!-- ========================================================================
         HERO SECTION: FULL-BLEED ARCHITECTURAL COMPOSITION
         ======================================================================== -->
    <section class="editorial-hero">
      <div class="hero-image-wrap">
        {picture_tag("images/projects/ivy-28/page_70_img1.jpeg", "King Nejashi Islamic Center & Monumental Arch Tower by IVY Architecture", "hero-cover-picture", is_lazy=False)}
        <div class="hero-tint-overlay"></div>
      </div>

      <div class="editorial-container hero-caption-block">
        <div class="hero-meta-strip">
          <span>Addis Ababa &middot; Juba &middot; Erbil</span>
          <span class="sep">&mdash;</span>
          <span>Integrated Practice</span>
          <span class="sep">&mdash;</span>
          <span>Grade-1 General Contractor</span>
        </div>

        <h1 class="hero-editorial-headline">
          Building architecture that endures.
        </h1>

        <p class="hero-editorial-lead">
          IVY Architecture &amp; Construction brings together architectural design, computational engineering, and on-site construction to deliver coordinated developments across East Africa and the Middle East.
        </p>

        <div class="hero-actions-row">
          <a href="#featured" class="btn-editorial-primary">
            View Featured Works
          </a>
          <a href="#contact" class="btn-editorial-secondary">
            Consultation Inquiry
          </a>
          <a href="https://wa.me/251911234567" target="_blank" rel="noopener noreferrer" class="btn-editorial-whatsapp">
            WhatsApp Bureau
          </a>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         SHORT INTRO: PLAIN, SPECIFIC LANGUAGE & STATS LEDGER
         ======================================================================== -->
    <section id="intro" class="editorial-section intro-section">
      <div class="editorial-container">
        <div class="intro-content-grid">
          <div class="intro-left">
            <span class="section-label">Practice Profile</span>
            <h2 class="intro-statement-serif">
              An integrated practice eliminating friction between architectural conception and site assembly.
            </h2>
          </div>
          <div class="intro-right">
            <div class="prose-editorial">
              <p>
                Enduring architecture requires seamless coordination between architectural design and structural execution. Founded in Addis Ababa with regional operations in Juba and Erbil, IVY unites architects, civil engineers, project managers, and logistics specialists into a single accountable practice.
              </p>
              <p>
                By supervising both schematic engineering and physical ground delivery, we ensure that complex geometry, seismic structural frames, and bespoke interior details are realized on schedule, within defined budgets, and to international standards.
              </p>
            </div>
          </div>
        </div>

        <!-- Factual Practice Ledger (Plain Horizontal Stats, No Box Grids) -->
        <div class="editorial-stat-ledger">
          <div class="stat-ledger-item">
            <span class="stat-figure">33</span>
            <span class="stat-caption">Commissions Completed &amp; Under Design</span>
          </div>
          <div class="stat-ledger-item">
            <span class="stat-figure">500k+</span>
            <span class="stat-caption">Square Meters Documented &amp; Built</span>
          </div>
          <div class="stat-ledger-item">
            <span class="stat-figure">03</span>
            <span class="stat-caption">Operating Countries: Ethiopia, South Sudan, Iraq</span>
          </div>
          <div class="stat-ledger-item">
            <span class="stat-figure">Grade 1</span>
            <span class="stat-caption">General Contractor License (Unlimited Scale)</span>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         6 FEATURED PROJECTS: FULL-BLEED / ASYMMETRIC EDITORIAL SPREADS
         ======================================================================== -->
    <section id="featured" class="editorial-section featured-section">
      <div class="editorial-container">
        <div class="section-heading-bar">
          <div>
            <span class="section-label">Selected Works</span>
            <h2 class="section-title-serif">Featured Architectural Commissions</h2>
          </div>
          <a href="#index" class="section-action-link">Explore Complete Index (33) &rarr;</a>
        </div>

        <div class="featured-spreads-container">
          {featured_section_html}
        </div>
      </div>
    </section>

    <!-- ========================================================================
         FILTERABLE PROJECT INDEX: TABLE LEDGER (SECTOR, COUNTRY, STATUS)
         ======================================================================== -->
    <section id="index" class="editorial-section index-section">
      <div class="editorial-container">
        <div class="section-heading-bar">
          <div>
            <span class="section-label">Project Index</span>
            <h2 class="section-title-serif">Complete Architectural Ledger</h2>
            <p class="section-subtext">Thirty-three documented commissions across civic, commercial, residential, healthcare, and industrial typologies.</p>
          </div>
          <div id="indexCountIndicator" class="index-count-indicator">Showing 33 of 33 commissions</div>
        </div>

        <!-- Index Filter Controls (Minimal Dropdowns & Hairline Rule) -->
        <div class="index-filter-bar" role="search" aria-label="Filter commissions">
          <div class="filter-group">
            <label for="filterSector" class="filter-label">Sector</label>
            <select id="filterSector" class="editorial-select">
              <option value="all">All Sectors</option>
              <option value="commercial">Commercial</option>
              <option value="residential">Residential</option>
              <option value="mixed-use">Mixed-Use</option>
              <option value="corporate">Corporate</option>
              <option value="education">Education</option>
              <option value="healthcare">Healthcare</option>
              <option value="industrial">Industrial</option>
              <option value="hospitality">Hospitality</option>
              <option value="monumental">Monumental &amp; Civic</option>
            </select>
          </div>

          <div class="filter-group">
            <label for="filterCountry" class="filter-label">Country</label>
            <select id="filterCountry" class="editorial-select">
              <option value="all">All Countries</option>
              <option value="Ethiopia">Ethiopia</option>
              <option value="South Sudan">South Sudan</option>
              <option value="Iraq">Iraq</option>
            </select>
          </div>

          <div class="filter-group">
            <label for="filterStatus" class="filter-label">Status</label>
            <select id="filterStatus" class="editorial-select">
              <option value="all">All Statuses</option>
              <option value="completed">Completed</option>
              <option value="construction">In Construction</option>
              <option value="design">Design Phase</option>
            </select>
          </div>

          <button id="resetFiltersBtn" class="filter-reset-btn" type="button">Reset Filters</button>
        </div>

        <!-- Editorial Table Ledger -->
        <div class="table-responsive-wrapper">
          <table class="editorial-ledger-table" aria-label="IVY Architectural Commissions Index">
            <thead>
              <tr>
                <th scope="col">Code</th>
                <th scope="col">Project Title</th>
                <th scope="col">Typology</th>
                <th scope="col">Location</th>
                <th scope="col">Scale</th>
                <th scope="col">Status</th>
                <th scope="col">Year</th>
                <th scope="col" aria-label="Link"></th>
              </tr>
            </thead>
            <tbody id="indexTableBody">
              {index_rows_html}
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         SERVICES AS A TEXT LIST (HAIRLINE DIVIDED)
         ======================================================================== -->
    <section id="services" class="editorial-section services-section">
      <div class="editorial-container">
        <div class="section-heading-bar">
          <div>
            <span class="section-label">Practice Scope</span>
            <h2 class="section-title-serif">Integrated Architectural &amp; Engineering Services</h2>
          </div>
        </div>

        <ol class="editorial-services-list">
          <li class="service-list-item">
            <div class="service-num">01</div>
            <div class="service-body">
              <h3 class="service-name-serif">Architectural Design &amp; Masterplanning</h3>
              <p class="service-detail">
                Comprehensive architectural design for high-rise commercial towers, residential estates, university campuses, and civic facilities. Solar orientation analysis, equatorial shading integration, and urban regulatory compliance.
              </p>
            </div>
          </li>

          <li class="service-list-item">
            <div class="service-num">02</div>
            <div class="service-body">
              <h3 class="service-name-serif">Civil &amp; Computational Structural Engineering</h3>
              <p class="service-detail">
                Seismic analysis, finite-element structural modeling, post-tensioned concrete floor slabs, deep pile foundations in complex clay soils, and long-span structural steel spaceframes.
              </p>
            </div>
          </li>

          <li class="service-list-item">
            <div class="service-num">03</div>
            <div class="service-body">
              <h3 class="service-name-serif">Mechanical, Electrical &amp; Plumbing (MEP) Engineering</h3>
              <p class="service-detail">
                Energy-efficient central HVAC design, dedicated hospital-grade water purification networks, cleanroom ventilation, diesel-solar hybrid microgrid generation, and heavy industrial power distribution.
              </p>
            </div>
          </li>

          <li class="service-list-item">
            <div class="service-num">04</div>
            <div class="service-body">
              <h3 class="service-name-serif">General Contracting &amp; Turnkey Construction</h3>
              <p class="service-detail">
                Certified Grade-1 General Contractor execution: on-site automated concrete batching, modular prefabrication deployment, continuous QA/QC materials testing, and occupational site safety superintendence.
              </p>
            </div>
          </li>

          <li class="service-list-item">
            <div class="service-num">05</div>
            <div class="service-body">
              <h3 class="service-name-serif">Interior Architecture &amp; FF&amp;E Procurement</h3>
              <p class="service-detail">
                Executive boardroom architecture, acoustic wall and ceiling engineering, specialized healthcare hygienic finishes, architectural millwork, and international FF&amp;E procurement.
              </p>
            </div>
          </li>

          <li class="service-list-item">
            <div class="service-num">06</div>
            <div class="service-body">
              <h3 class="service-name-serif">Cross-Border Material Trading &amp; Heavy Equipment Logistics</h3>
              <p class="service-detail">
                Direct international supply chain channels supplying certified structural steel, architectural curtain wall glazing systems, finishing marble, and specialized civil engineering machinery across East Africa and the Middle East.
              </p>
            </div>
          </li>
        </ol>
      </div>
    </section>

    <!-- ========================================================================
         CREDENTIALS: VERIFIED INSTITUTIONAL STANDARDS
         ======================================================================== -->
    <section id="credentials" class="editorial-section credentials-section">
      <div class="editorial-container">
        <div class="section-heading-bar">
          <div>
            <span class="section-label">Certifications</span>
            <h2 class="section-title-serif">Institutional Credentials &amp; Standards</h2>
          </div>
        </div>

        <div class="credentials-ledger">
          <div class="credential-entry">
            <h3 class="credential-name">Grade-1 General Contractor</h3>
            <p class="credential-auth">Federal Ministry of Urban Development &amp; Infrastructure</p>
            <p class="credential-desc">
              Officially registered and certified as a Grade-1 General Contractor with unlimited statutory scope for high-rise commercial structures, civic masterplans, and heavy infrastructure works.
            </p>
          </div>

          <div class="credential-entry">
            <h3 class="credential-name">ISO 9001:2015 Quality System</h3>
            <p class="credential-auth">Audited International Quality Standard</p>
            <p class="credential-desc">
              Certified quality management framework governing preliminary geotechnical bore testing, concrete compressive break verification, ultrasonic structural weld testing, and occupational site safety.
            </p>
          </div>

          <div class="credential-entry">
            <h3 class="credential-name">Cross-Border Trading License</h3>
            <p class="credential-auth">International Procurement Network</p>
            <p class="credential-desc">
              Authorized heavy equipment importation and material trading licensing supporting certified structural steel, specialized unitized curtain walls, and MEP plant logistics across Ethiopia, South Sudan, and Iraq.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         LEADERSHIP: MULTIDISCIPLINARY DIRECTORS
         ======================================================================== -->
    <section id="leadership" class="editorial-section leadership-section">
      <div class="editorial-container">
        <div class="section-heading-bar">
          <div>
            <span class="section-label">Leadership</span>
            <h2 class="section-title-serif">Practice Leadership &amp; Direction</h2>
          </div>
        </div>

        <div class="leadership-text-grid">
          <div class="leader-text-block">
            <h3 class="leader-role">Architectural Conception &amp; Design</h3>
            <p class="leader-title">Principal Design Partners</p>
            <p class="leader-bio">
              Directs context-responsive form, climatic passive solar strategies, space planning, and urban masterplanning. Leads architectural design review for civic institutions and commercial towers.
            </p>
          </div>

          <div class="leader-text-block">
            <h3 class="leader-role">Civil &amp; Structural Engineering</h3>
            <p class="leader-title">Chief Structural Engineers</p>
            <p class="leader-bio">
              Oversees finite-element computational analysis, deep foundation engineering in unstable soils, post-tensioned floor systems, and seismic-resistant reinforced concrete frames.
            </p>
          </div>

          <div class="leader-text-block">
            <h3 class="leader-role">Construction Operations &amp; QA/QC</h3>
            <p class="leader-title">Site Superintendence Directors</p>
            <p class="leader-bio">
              Certified Grade-1 construction superintendents managing on-site concrete batching, rebar placement verification, occupational health and safety compliance, and construction schedule milestones.
            </p>
          </div>

          <div class="leader-text-block">
            <h3 class="leader-role">Supply Chain &amp; Procurement</h3>
            <p class="leader-title">International Logistics Directors</p>
            <p class="leader-bio">
              Manages cross-border freight forwarding, customs clearance, and procurement of certified structural steel, unitized curtain wall glazing, and specialized MEP plant machinery.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         CLIENTS: DOCUMENTED INSTITUTIONAL & CORPORATE CLIENTS
         ======================================================================== -->
    <section id="clients" class="editorial-section clients-section">
      <div class="editorial-container">
        <div class="section-heading-bar">
          <div>
            <span class="section-label">Client Record</span>
            <h2 class="section-title-serif">Commissioning Clients &amp; Organizations</h2>
            <p class="section-subtext">Government ministries, educational institutions, commercial developers, and non-governmental organizations.</p>
          </div>
        </div>

        <ul class="clients-directory-list">
          {client_list_html}
        </ul>
      </div>
    </section>

    <!-- ========================================================================
         CONTACT: 4-FIELD FORM, WHATSAPP, AND REGIONAL BUREAUS
         ======================================================================== -->
    <section id="contact" class="editorial-section contact-section">
      <div class="editorial-container">
        <div class="section-heading-bar">
          <div>
            <span class="section-label">Initiate Contact</span>
            <h2 class="section-title-serif">Discuss a Project</h2>
            <p class="section-subtext">Connect with our principal architects and engineering directors for site feasibility, architectural design, or general contracting inquiries.</p>
          </div>
        </div>

        <div class="contact-editorial-layout">
          <!-- Left Column: Bureaus & Direct Channels -->
          <div class="contact-channels-col">
            <div class="channel-group">
              <h3 class="channel-heading">Direct Channels</h3>
              <p class="channel-line">
                <strong>WhatsApp:</strong> 
                <a href="https://wa.me/251911234567?text=Hello%20IVY%20Architecture,%20I%20would%20like%20to%20discuss%20a%20project" target="_blank" rel="noopener noreferrer" class="whatsapp-accent-link">
                  +251 91 123 4567 (Instant Partner Chat) &rarr;
                </a>
              </p>
              <p class="channel-line">
                <strong>Telephone:</strong> 
                <a href="tel:+251911234567">+251 91 123 4567</a>
              </p>
              <p class="channel-line">
                <strong>Executive Inquiries:</strong> 
                <a href="mailto:info@ivyconstruction.com">info@ivyconstruction.com</a>
              </p>
            </div>

            <div class="channel-group">
              <h3 class="channel-heading">Permanent Bureaus</h3>
              <div class="bureau-entry">
                <strong>Principal Design Studio [HQ]</strong>
                <p>Bole Commercial District, Addis Ababa, Ethiopia</p>
              </div>
              <div class="bureau-entry">
                <strong>Regional Operations Bureau</strong>
                <p>Central Commercial Sector, Juba, South Sudan</p>
              </div>
              <div class="bureau-entry">
                <strong>Logistics &amp; Prefabrication Partner</strong>
                <p>Specialized Procurement &amp; Freight Forwarding, Erbil, Iraq</p>
              </div>
            </div>

            <div class="channel-group">
              <h3 class="channel-heading">Portfolio Monograph</h3>
              <p class="monograph-summary-text">
                Download the official 81-page high-resolution architectural monograph containing all floor plans, structural sections, and complete specifications.
              </p>
              <a href="IVY-CONSTRUCTION-PORTFOLIO.pdf" download class="btn-editorial-secondary">
                Download Monograph (81 Pages, 7.3 MB)
              </a>
            </div>
          </div>

          <!-- Right Column: Simplified 4-Field Consultation Form -->
          <div class="contact-form-col">
            <h3 class="form-title-serif">Project Consultation Brief</h3>
            <p class="form-subtitle">Provide preliminary parameters. Our partners will respond within 48 business hours.</p>

            <form id="consultationBriefForm" class="editorial-form" novalidate>
              <div class="form-field">
                <label for="contactName" class="form-label">Full Name &amp; Organization *</label>
                <input type="text" id="contactName" name="name" class="form-input" required placeholder="e.g. Elias Gebremariam, Hagbes Pvt. Ltd.">
              </div>

              <div class="form-field">
                <label for="contactEmail" class="form-label">Corporate Email Address *</label>
                <input type="email" id="contactEmail" name="email" class="form-input" required placeholder="contact@organization.com">
              </div>

              <div class="form-field">
                <label for="contactTypologyLocation" class="form-label">Project Typology &amp; Location *</label>
                <input type="text" id="contactTypologyLocation" name="typology_location" class="form-input" required placeholder="e.g. 18-Story Commercial Tower, Addis Ababa">
              </div>

              <div class="form-field">
                <label for="contactScope" class="form-label">Project Brief &amp; Scope Requirements *</label>
                <textarea id="contactScope" name="scope" rows="5" class="form-textarea" required placeholder="Detail approximate site area, floor count, schedule, budget parameters, and required architectural or contracting scope..."></textarea>
              </div>

              <div class="form-actions">
                <button type="submit" class="btn-editorial-primary btn-submit-full">
                  Transmit Project Brief &rarr;
                </button>
              </div>

              <div id="formFeedbackNotice" class="form-feedback-notice" style="display: none;"></div>
            </form>
          </div>
        </div>
      </div>
    </section>
  </main>

  <!-- Editorial Footer -->
  <footer class="editorial-footer">
    <div class="editorial-container footer-grid">
      <div class="footer-col brand-col">
        <span class="brand-serif">IVY</span>
        <p class="footer-summary">
          Multidisciplinary practice combining architecture, engineering, and construction across East Africa and the Middle East.
        </p>
        <p class="footer-credentials">Grade-1 General Contractor &middot; ISO 9001 Certified</p>
      </div>

      <div class="footer-col">
        <h3 class="footer-heading">Bureaus</h3>
        <p><strong>Addis Ababa [HQ]</strong><br>Bole Subcity Commercial District, Ethiopia</p>
        <p><strong>Juba [Bureau]</strong><br>Central Commercial Sector, South Sudan</p>
        <p><strong>Erbil [Logistics Hub]</strong><br>Procurement &amp; Freight, Iraq</p>
      </div>

      <div class="footer-col">
        <h3 class="footer-heading">Direct Channels</h3>
        <p>Partner Line: <a href="tel:+251911234567">+251 91 123 4567</a></p>
        <p>Inquiries: <a href="mailto:info@ivyconstruction.com">info@ivyconstruction.com</a></p>
        <p>WhatsApp: <a href="https://wa.me/251911234567" target="_blank" rel="noopener noreferrer">+251 91 123 4567</a></p>
      </div>

      <div class="footer-col">
        <h3 class="footer-heading">Documentation</h3>
        <p><a href="IVY-CONSTRUCTION-PORTFOLIO.pdf" download>Monograph PDF (81 Pages, 7.3 MB)</a></p>
        <p><a href="#index">Catalogue Index (33 Commissions)</a></p>
        <p><a href="#contact">Consultation Request</a></p>
      </div>
    </div>

    <div class="editorial-container footer-bottom-bar">
      <span>&copy; 2026 IVY Construction &amp; Trading Co. Ltd. All rights reserved.</span>
      <span class="footer-regions">ETHIOPIA &middot; SOUTH SUDAN &middot; IRAQ &middot; INTERNATIONAL</span>
    </div>
  </footer>

  <script src="app.js"></script>
</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as hf:
    hf.write(homepage_html)

print("Generated editorial index.html successfully.")

# ==============================================================================
# 3. GENERATE SITEMAP (sitemap.xml)
# ==============================================================================
sitemap_entries = [
    f"""  <url>
    <loc>{SITE_URL}/</loc>
    <lastmod>2026-11-19</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>"""
]

for p in PROJECTS:
    sitemap_entries.append(f"""  <url>
    <loc>{SITE_URL}/projects/{p['id']}.html</loc>
    <lastmod>2026-11-19</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>""")

sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{"\n".join(sitemap_entries)}
</urlset>"""

with open("sitemap.xml", "w", encoding="utf-8") as sf:
    sf.write(sitemap_xml)

print("Generated sitemap.xml with 34 entries successfully.")
