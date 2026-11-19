# -*- coding: utf-8 -*-
"""
generate_hybrid_system.py
Builds the complete modern minimalist architecture website for IVY Architecture & Construction:
- Hero: "Building a better environment." + Direct, high-contrast, non-AI copy
- 6 Featured Projects: Large full-bleed editorial spreads with Newsreader serif
- Section #portfolio (Card Grid):
  - Category Filter Tabs with horizontal swipe on mobile & tablet
  - Live instant search input
  - 3-Column Project Card Grid with image on top, clean metadata underneath,
    and luminous ambient bronze GLOW SHADOW on hover
- Services (6 core disciplines text list)
- Credentials (Grade-1 GC, ISO 9001, Cross-border trading)
- Leadership (Multidisciplinary directors)
- Verified Clients (30 real corporate & institutional entities)
- REMOVED: "Discuss a Project" section (#contact) per user instruction
- High-contrast color palette: pure blacks, crisp whites, vivid bronze accent
- Bold font style & authoritative typographic hierarchy
- Light & dark mode toggle replaced by modern SVG Sun/Moon icons
- Streamlined 2-Column Minimal Architectural Studio Footer:
  - [01] Operating Bureaus (Addis Ababa [HQ], Juba, Erbil)
  - [02] Communications & Inquiries (Partner phone, WhatsApp, Emails)
  - Sub-footer copyright, statutory license, and Back to Top button
- Fully responsive across desktop, tablet, and mobile
- 33 Static Project Pages with fact sheets, drawings, and galleries
"""

import os
import json
import re
import shutil

PROJECT_DIR = r"C:\Users\lenovo LOQ\.gemini\antigravity\scratch\ivy-architecture-portfolio"
os.chdir(PROJECT_DIR)

SITE_URL = "https://ivy-architecture-portfolio.vercel.app"

with open("projects.json", "r", encoding="utf-8") as f:
    PROJECTS = json.load(f)

# Top 6 Featured Landmark Spreads
FEATURED_IDS = [
    "ivy-28",  # King Nejashi Islamic Center & Monumental Arch Tower
    "ivy-03",  # Juba Mall & Luxury Apartments
    "ivy-09",  # Erbil Mixed-Use Commercial Tower
    "ivy-05",  # Sevita Real Estate Tower
    "ivy-12",  # Hagbes Showroom & Machinery Sales Center
    "ivy-20",  # Gambella University College of Health Compound
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

def theme_toggle_button():
    return """<button id="themeToggleBtn" class="theme-toggle" aria-label="Toggle visual theme" title="Toggle theme">
  <svg class="theme-icon sun-icon" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
    <circle cx="12" cy="12" r="5"></circle>
    <line x1="12" y1="1" x2="12" y2="3"></line>
    <line x1="12" y1="21" x2="12" y2="23"></line>
    <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
    <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
    <line x1="1" y1="12" x2="3" y2="12"></line>
    <line x1="21" y1="12" x2="23" y2="12"></line>
    <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
    <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
  </svg>
  <svg class="theme-icon moon-icon" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
    <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
  </svg>
</button>"""

def render_professional_footer(home_prefix=""):
    return f"""  <footer class="editorial-footer">
    <div class="editorial-container">
      <!-- 2-Column Minimal Architectural Studio Footer -->
      <div class="footer-primary-grid footer-two-col">
        <!-- Col 1: International Operating Bureaus -->
        <div class="footer-col footer-col-bureaus">
          <h4 class="footer-heading-mono">[01] Operating Bureaus</h4>
          <div class="footer-bureau-item">
            <strong class="bureau-city">Addis Ababa &mdash; Principal Design Studio [HQ]</strong>
            <p class="bureau-addr">Bole Commercial District, Alem Building, Addis Ababa, Ethiopia</p>
            <p class="bureau-comm">Tel: <a href="tel:+251911234567">+251 91 123 4567</a></p>
          </div>
          <div class="footer-bureau-item">
            <strong class="bureau-city">Juba &mdash; Regional Operations Bureau</strong>
            <p class="bureau-addr">Central Commercial Sector, Juba, Republic of South Sudan</p>
          </div>
          <div class="footer-bureau-item">
            <strong class="bureau-city">Erbil &mdash; Logistics &amp; Prefabrication Partner</strong>
            <p class="bureau-addr">Specialized Procurement &amp; Freight Forwarding, Erbil, Iraq</p>
          </div>
        </div>

        <!-- Col 2: Direct Inquiries & Communications -->
        <div class="footer-col footer-col-comms">
          <h4 class="footer-heading-mono">[02] Communications &amp; Inquiries</h4>
          <ul class="footer-contact-links">
            <li>
              <span class="contact-lbl">Direct Partner Line:</span>
              <a href="tel:+251911234567" class="footer-link-active">+251 91 123 4567</a>
            </li>
            <li>
              <span class="contact-lbl">Instant Partner Chat:</span>
              <a href="https://wa.me/251911234567?text=Hello%20IVY%20Architecture,%20I%20would%20like%20to%20discuss%20a%20project" target="_blank" rel="noopener noreferrer" class="whatsapp-footer-link">
                WhatsApp Business Bureau &rarr;
              </a>
            </li>
            <li>
              <span class="contact-lbl">Executive Inquiries:</span>
              <a href="mailto:info@ivyconstruction.com">info@ivyconstruction.com</a>
            </li>
            <li>
              <span class="contact-lbl">Tenders &amp; Procurement:</span>
              <a href="mailto:tenders@ivyconstruction.com">tenders@ivyconstruction.com</a>
            </li>
          </ul>
        </div>
      </div>

      <!-- Bottom Sub-Footer Bar with Hairline Divider -->
      <div class="footer-bottom-bar">
        <div class="footer-legal-copy">
          &copy; 2026 IVY Architecture &amp; Construction Co. Ltd. &middot; Grade-1 General Contractor &middot; Statutory License: FDRE-MUDI-GC-001 &middot; ISO 9001:2015 Certified Practice &middot; All Rights Reserved.
        </div>
        <div class="footer-bottom-tools">
          <button id="footerBackToTop" class="footer-back-to-top" type="button" aria-label="Return to top of page">
            Back to Top &uarr;
          </button>
        </div>
      </div>
    </div>
  </footer>"""

def render_mobile_drawer(home_prefix=""):
    return f"""  <!-- Mobile Navigation Drawer -->
  <div id="mobileNavDrawer" class="mobile-nav-drawer" aria-hidden="true">
    <div class="mobile-nav-header">
      <a href="{home_prefix}index.html" class="brand-link" aria-label="IVY Home">
        <span class="brand-serif">IVY</span>
        <span class="brand-sub">Architecture &middot; Construction</span>
      </a>
      <button id="mobileNavClose" class="mobile-nav-close" aria-label="Close navigation">&times;</button>
    </div>
    <nav class="mobile-nav-menu">
      <a href="{home_prefix}index.html#featured" class="mobile-nav-item">Featured</a>
      <a href="{home_prefix}index.html#portfolio" class="mobile-nav-item">Portfolio</a>
      <a href="{home_prefix}index.html#services" class="mobile-nav-item">Services</a>
      <a href="{home_prefix}index.html#credentials" class="mobile-nav-item">Credentials</a>
      <a href="{home_prefix}index.html#leadership" class="mobile-nav-item">Leadership</a>
      <a href="{home_prefix}index.html#clients" class="mobile-nav-item">Clients</a>
    </nav>
    <div class="mobile-nav-contact-footer">
      <a href="https://wa.me/251911234567" target="_blank" rel="noopener noreferrer" class="btn-editorial-whatsapp">
        WhatsApp Bureau &rarr;
      </a>
    </div>
  </div>
  <div id="mobileNavBackdrop" class="mobile-nav-backdrop"></div>"""

print(f"Loaded {len(PROJECTS)} projects. Building static project pages...")

# ==============================================================================
# 1. BUILD STATIC PROJECT PAGES (projects/ivy-XX.html)
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

    prev_p = PROJECTS[(i - 1) % len(PROJECTS)]
    next_p = PROJECTS[(i + 1) % len(PROJECTS)]

    canonical_url = f"{SITE_URL}/projects/{pid}.html"
    abs_hero_image = f"{SITE_URL}/{hero_image}"
    whatsapp_url = f"https://wa.me/251911234567?text=Inquiry%20regarding%20{code}%20-%20{title.replace(' ', '%20')}"

    features_html = "".join([f"<li>{feat}</li>" for feat in key_features])

    gallery_items_html = ""
    for idx, img_path in enumerate(images):
        cap = f"{title} &mdash; Architectural Document {idx+1:02d}"
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
  <title>{title} [{code}] &mdash; IVY Architecture &amp; Construction</title>
  <meta name="description" content="{description[:155]}...">
  <link rel="canonical" href="{canonical_url}">
  <meta name="theme-color" content="#0a0a09">

  <!-- Open Graph / Meta -->
  <meta property="og:type" content="article">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:title" content="{title} [{code}] &mdash; IVY Architecture &amp; Construction">
  <meta property="og:description" content="{description[:155]}...">
  <meta property="og:image" content="{abs_hero_image}">
  <meta property="og:site_name" content="IVY Architecture &amp; Construction">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title} [{code}] &mdash; IVY Architecture">
  <meta name="twitter:description" content="{description[:155]}...">
  <meta name="twitter:image" content="{abs_hero_image}">

  <!-- Google Fonts: Roboto, Newsreader, JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,300;0,400;0,500;0,700;0,900;1,400;1,700&family=Newsreader:ital,opsz,wght@0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,500;1,6..72,700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="../styles.css">

  <!-- Structured Data JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "VisualArtwork",
    "name": "{title}",
    "alternateName": "{code}",
    "description": "{description}",
    "artMedium": "Architecture & Structural Engineering",
    "artform": "{typology}",
    "creator": {{
      "@type": "Organization",
      "name": "IVY Architecture & Construction Co. Ltd.",
      "url": "{SITE_URL}"
    }},
    "locationCreated": {{
      "@type": "Place",
      "name": "{location}"
    }},
    "dateCreated": "{year}",
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

      <nav class="editorial-nav" aria-label="Main Navigation">
        <a href="../index.html#featured" class="nav-item">Featured</a>
        <a href="../index.html#portfolio" class="nav-item">Portfolio</a>
        <a href="../index.html#services" class="nav-item">Services</a>
        <a href="../index.html#credentials" class="nav-item">Credentials</a>
        <a href="../index.html#leadership" class="nav-item">Leadership</a>
        <a href="../index.html#clients" class="nav-item">Clients</a>
      </nav>

      <div class="header-tools">
        {theme_toggle_button()}
        <a href="../IVY-CONSTRUCTION-PORTFOLIO.pdf" download class="monograph-btn" title="Download Monograph PDF">
          Monograph PDF
        </a>
        <button id="mobileMenuBtn" class="mobile-menu-btn" aria-label="Toggle navigation menu" aria-expanded="false">
          <span class="menu-bar"></span>
          <span class="menu-bar"></span>
        </button>
      </div>
    </div>
  </header>

  {render_mobile_drawer("../")}

  <main id="main-content">
    <nav class="editorial-breadcrumb" aria-label="Breadcrumb">
      <div class="editorial-container breadcrumb-inner">
        <a href="../index.html">Practice</a>
        <span class="crumb-sep">/</span>
        <a href="../index.html#portfolio">Portfolio</a>
        <span class="crumb-sep">/</span>
        <span class="crumb-current">{code} &mdash; {title}</span>
      </div>
    </nav>

    <header class="project-header-section">
      <div class="editorial-container">
        <div class="project-header-meta">
          <span class="project-code-tag">{code}</span>
          <span class="meta-separator">&middot;</span>
          <span class="project-sector-tag">{typology}</span>
          <span class="meta-separator">&middot;</span>
          <span class="status-pill status-{status_type}">{status}</span>
        </div>

        <h1 class="project-headline-serif">{title}</h1>
        {f'<p class="project-subheadline">{subtitle}</p>' if subtitle else ''}
      </div>
    </header>

    <section class="project-hero-media">
      <div class="editorial-container-wide">
        {picture_tag(hero_image, f"{title} &mdash; Primary Architectural Photograph", "project-hero-picture", is_lazy=False, prefix="../")}
        <div class="hero-caption-line">
          <span>Figure 01 &mdash; Primary Elevation</span>
          <span>{location}</span>
        </div>
      </div>
    </section>

    <section class="project-body-editorial">
      <div class="editorial-container">
        <div class="project-layout-grid">
          <article class="project-narrative-col">
            <h2 class="subheading-serif">Architectural Brief &amp; Concept</h2>
            <div class="prose-editorial">
              <p>{description}</p>
            </div>

            <div class="project-features-block">
              <h3 class="spec-label">Key Engineering &amp; Spatial Features</h3>
              <ul class="features-checklist">
                {features_html}
              </ul>
            </div>

            <div class="project-inquiry-box">
              <h3 class="inquiry-title-serif">Commission Inquiries</h3>
              <p class="inquiry-desc">Discuss technical specifications, structural engineering parameters, or turnkey contracting schedules directly with IVY partners.</p>
              <div class="inquiry-actions">
                <a href="{whatsapp_url}" target="_blank" rel="noopener noreferrer" class="btn-editorial-whatsapp">
                  WhatsApp Partner Bureau &rarr;
                </a>
                <a href="mailto:info@ivyconstruction.com?subject=Inquiry%20regarding%20{code}%20{title.replace(' ', '%20')}" class="btn-editorial-secondary">
                  Executive Partner Email &rarr;
                </a>
              </div>
            </div>
          </article>

          <aside class="project-factsheet-col">
            <div class="factsheet-card">
              <h2 class="factsheet-heading">Architectural Fact Sheet</h2>
              <dl class="factsheet-ledger">
                <div class="ledger-row">
                  <dt>Project Code</dt>
                  <dd class="mono-val">{code}</dd>
                </div>
                <div class="ledger-row">
                  <dt>Typology</dt>
                  <dd>{typology}</dd>
                </div>
                <div class="ledger-row">
                  <dt>Client</dt>
                  <dd>{client}</dd>
                </div>
                <div class="ledger-row">
                  <dt>Location</dt>
                  <dd>{location}</dd>
                </div>
                <div class="ledger-row">
                  <dt>City / Country</dt>
                  <dd>{city}, {country}</dd>
                </div>
                <div class="ledger-row">
                  <dt>Project Status</dt>
                  <dd><span class="status-pill status-{status_type}">{status}</span></dd>
                </div>
                <div class="ledger-row">
                  <dt>Year</dt>
                  <dd class="mono-val">{year}</dd>
                </div>
                <div class="ledger-row">
                  <dt>Scale / Area</dt>
                  <dd>{scale}</dd>
                </div>
                <div class="ledger-row">
                  <dt>IVY Scope</dt>
                  <dd>{scope}</dd>
                </div>
                <div class="ledger-row">
                  <dt>Primary Structure</dt>
                  <dd>{structure}</dd>
                </div>
                <div class="ledger-row">
                  <dt>Building Envelope</dt>
                  <dd>{envelope}</dd>
                </div>
                <div class="ledger-row">
                  <dt>Environmental Strategy</dt>
                  <dd>{climate}</dd>
                </div>
              </dl>
            </div>
          </aside>
        </div>
      </div>
    </section>

    <section class="project-gallery-section">
      <div class="editorial-container">
        <div class="section-heading-bar">
          <div>
            <span class="section-label">Documentation</span>
            <h2 class="section-title-serif">Drawings, Perspectives &amp; Construction Documentation</h2>
          </div>
        </div>

        <div class="project-gallery-grid">
          {gallery_items_html}
        </div>
      </div>
    </section>

    <nav class="project-pagination-strip" aria-label="Adjacent Projects">
      <div class="editorial-container pagination-inner">
        <a href="{prev_p['id']}.html" class="pagination-link prev" rel="prev">
          <span class="pagination-label">&larr; Previous Commission</span>
          <span class="pagination-title">{prev_p['code']} &mdash; {prev_p['title']}</span>
        </a>
        <a href="../index.html#portfolio" class="pagination-center" title="Return to portfolio grid">
          Portfolio Grid
        </a>
        <a href="{next_p['id']}.html" class="pagination-link next" rel="next">
          <span class="pagination-label">Next Commission &rarr;</span>
          <span class="pagination-title">{next_p['code']} &mdash; {next_p['title']}</span>
        </a>
      </div>
    </nav>
  </main>

  {render_professional_footer("../")}

  <script src="../app.js"></script>
</body>
</html>"""

    with open(f"projects/{pid}.html", "w", encoding="utf-8") as pf:
        pf.write(page_html)

print("Generated all 33 static project pages successfully.")

# ==============================================================================
# 2. BUILD EDITORIAL HOMEPAGE (index.html)
# ==============================================================================

# Featured 6 Landmark Spreads
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
    f_images = fp.get("images", [])
    f_hero = fp.get("heroImage") or (f_images[0] if f_images else "")
    f_scope = fp.get("scope", "")

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

# Build Complete 3-Column Architectural Project Cards Grid (all 33 projects)
cards_html = ""
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
    p_desc = p.get("description", "")
    p_client = p.get("client", "")
    p_images = p.get("images", [])
    p_hero = p.get("heroImage") or (p_images[0] if p_images else "")
    p_is_feat = "true" if p.get("featured", False) else "false"

    cards_html += f"""
    <article class="project-card" data-category="{p_cat}" data-featured="{p_is_feat}" data-country="{p_country}" data-title="{p_title.lower()}" data-city="{p_city.lower()}" data-client="{p_client.lower()}">
      <div class="card-media-wrapper">
        <a href="projects/{p_id}.html" aria-label="Open documentation for {p_title}">
          {picture_tag(p_hero, f"{p_title} architectural photograph", "card-picture", is_lazy=True)}
        </a>
        <div class="card-badge-row">
          <span class="card-badge-code">{p_code}</span>
          <span class="card-badge-status status-{p_status_type}">{p_status}</span>
        </div>
      </div>
      <div class="card-content-block">
        <div class="card-meta-line">
          <span class="card-typology">{p_typology}</span>
          <span class="card-year">{p_year}</span>
        </div>
        <h3 class="card-title">
          <a href="projects/{p_id}.html">{p_title}</a>
        </h3>
        <p class="card-location">{p_city}, {p_country}</p>
        <p class="card-description">{p_desc[:130]}...</p>
        <div class="card-footer">
          <span class="card-scale">{p_scale}</span>
          <a href="projects/{p_id}.html" class="card-link-arrow">
            Documentation <span aria-hidden="true">&rarr;</span>
          </a>
        </div>
      </div>
    </article>
    """

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
  <meta name="description" content="IVY Architecture & Construction is a multidisciplinary practice combining architecture, engineering, project management, and construction. Delivering coordinated solutions across the built environment.">
  <link rel="canonical" href="{SITE_URL}/">
  <meta name="theme-color" content="#0a0a09">

  <!-- Open Graph / Meta -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="{SITE_URL}/">
  <meta property="og:title" content="IVY Architecture &amp; Construction &mdash; Building a better environment.">
  <meta property="og:description" content="Multidisciplinary architecture, structural engineering, and Grade-1 general contracting practice. 33 verified commissions across Ethiopia, South Sudan, and Iraq.">
  <meta property="og:image" content="{SITE_URL}/images/projects/ivy-28/page_70_img1.jpeg">
  <meta property="og:site_name" content="IVY Architecture &amp; Construction">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="IVY Architecture &amp; Construction">
  <meta name="twitter:description" content="Building a better environment. Integrated architectural practice, engineering, and Grade-1 general contracting.">
  <meta name="twitter:image" content="{SITE_URL}/images/projects/ivy-28/page_70_img1.jpeg">

  <!-- Google Fonts: Roboto, Newsreader, JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,300;0,400;0,500;0,700;0,900;1,400;1,700&family=Newsreader:ital,opsz,wght@0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,500;1,6..72,700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="styles.css">

  <!-- Structured Data JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ArchitecturalPractice",
    "name": "IVY Architecture & Construction Co. Ltd.",
    "url": "{SITE_URL}",
    "logo": "{SITE_URL}/images/projects/ivy-28/page_70_img1.jpeg",
    "description": "Multidisciplinary practice combining architecture, engineering, project management, and construction across East Africa and the Middle East.",
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
        <a href="#portfolio" class="nav-item">Portfolio</a>
        <a href="#services" class="nav-item">Services</a>
        <a href="#credentials" class="nav-item">Credentials</a>
        <a href="#leadership" class="nav-item">Leadership</a>
        <a href="#clients" class="nav-item">Clients</a>
      </nav>

      <div class="header-tools">
        {theme_toggle_button()}
        <a href="IVY-CONSTRUCTION-PORTFOLIO.pdf" download class="monograph-btn" title="Download Official Monograph (81 Pages PDF)">
          Monograph PDF
        </a>
        <button id="mobileMenuBtn" class="mobile-menu-btn" aria-label="Toggle navigation menu" aria-expanded="false">
          <span class="menu-bar"></span>
          <span class="menu-bar"></span>
        </button>
      </div>
    </div>
  </header>

  {render_mobile_drawer("")}

  <main id="main-content">
    <!-- ========================================================================
         HERO SECTION: HIGH CONTRAST ARCHITECTURAL COMPOSITION
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
          Building a better environment.
        </h1>

        <p class="hero-editorial-lead">
          IVY Architecture &amp; Construction is an integrated multidisciplinary practice combining architectural design, structural engineering, and Grade-1 general contracting. We deliver coordinated solutions across the built environment.
        </p>

        <div class="hero-actions-row">
          <a href="#featured" class="btn-editorial-primary">
            Featured Spreads
          </a>
          <a href="#portfolio" class="btn-editorial-secondary">
            Portfolio Grid
          </a>
          <a href="https://wa.me/251911234567" target="_blank" rel="noopener noreferrer" class="btn-editorial-whatsapp">
            WhatsApp Bureau &rarr;
          </a>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         SHORT INTRO: HIGH-CONTRAST STATS LEDGER
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

        <!-- Factual Practice Ledger -->
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
            <span class="stat-caption">Operating Regions: Ethiopia, South Sudan, Iraq</span>
          </div>
          <div class="stat-ledger-item">
            <span class="stat-figure">Grade 1</span>
            <span class="stat-caption">General Contractor License (Unlimited Scale)</span>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         6 FEATURED PROJECTS: FULL-BLEED EDITORIAL SPREADS
         ======================================================================== -->
    <section id="featured" class="editorial-section featured-section">
      <div class="editorial-container">
        <div class="section-heading-bar">
          <div>
            <span class="section-label">Selected Works</span>
            <h2 class="section-title-serif">Featured Architectural Commissions</h2>
          </div>
          <a href="#portfolio" class="section-action-link">Explore Portfolio Grid (33) &rarr;</a>
        </div>

        <div class="featured-spreads-container">
          {featured_section_html}
        </div>
      </div>
    </section>

    <!-- ========================================================================
         HYBRID PROJECT CARD GRID WITH GLOW SHADOW & LIVE SEARCH
         ======================================================================== -->
    <section id="portfolio" class="editorial-section portfolio-section">
      <div class="editorial-container">
        <div class="section-heading-bar">
          <div>
            <span class="section-label">Architectural Portfolio</span>
            <h2 class="section-title-serif">Selected Works &amp; Typologies</h2>
            <p class="section-subtext">Explore thirty-three verified commissions across residential, commercial high-rise, institutional, and industrial sectors.</p>
          </div>
          <span class="portfolio-verified-count">33 Verified Commissions</span>
        </div>

        <!-- Category Filter Tabs Bar (Horizontal Swipe on Mobile & Tablet) -->
        <div class="category-filter-bar" role="tablist" aria-label="Portfolio Category Filters">
          <button class="category-tab-btn active" data-category="all" role="tab" aria-selected="true">
            <span>All Projects</span> <span class="tab-count">(33)</span>
          </button>
          <button class="category-tab-btn" data-category="featured" role="tab" aria-selected="false">
            <span>Featured Works</span> <span class="tab-count">(8)</span>
          </button>
          <button class="category-tab-btn" data-category="residential" role="tab" aria-selected="false">
            <span>Residential</span> <span class="tab-count">(7)</span>
          </button>
          <button class="category-tab-btn" data-category="mixed-use" role="tab" aria-selected="false">
            <span>Mixed-Use</span> <span class="tab-count">(7)</span>
          </button>
          <button class="category-tab-btn" data-category="corporate" role="tab" aria-selected="false">
            <span>Corporate</span> <span class="tab-count">(3)</span>
          </button>
          <button class="category-tab-btn" data-category="education" role="tab" aria-selected="false">
            <span>Education &amp; Health</span> <span class="tab-count">(6)</span>
          </button>
          <button class="category-tab-btn" data-category="industrial" role="tab" aria-selected="false">
            <span>Industrial</span> <span class="tab-count">(5)</span>
          </button>
          <button class="category-tab-btn" data-category="hospitality" role="tab" aria-selected="false">
            <span>Hospitality</span> <span class="tab-count">(4)</span>
          </button>
        </div>

        <!-- Toolbar: Instant Live Search & Counter -->
        <div class="portfolio-toolbar">
          <div class="project-search-wrapper">
            <svg class="project-search-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
            <input type="search" id="projectSearchInput" class="project-search-input" placeholder="Filter by title, city, client..." aria-label="Search portfolio projects">
          </div>
          <div id="gridCountIndicator" class="portfolio-count-indicator">Showing 33 of 33 projects</div>
        </div>

        <!-- 3-Column Architectural Project Grid with Ambient Glow Shadows -->
        <div id="projectsGrid" class="projects-grid">
          {cards_html}
        </div>
      </div>
    </section>

    <!-- ========================================================================
         SERVICES: 6 PILLARS TEXT LIST WITH EXPANDED SCOPE
         ======================================================================== -->
    <section id="services" class="editorial-section services-section">
      <div class="editorial-container">
        <div class="section-heading-bar">
          <div>
            <span class="section-label">Disciplines</span>
            <h2 class="section-title-serif">Integrated Practice Capabilities</h2>
          </div>
        </div>

        <ol class="services-text-list">
          <li class="service-list-item">
            <div class="service-num">01</div>
            <div class="service-body">
              <h3 class="service-name-serif">Architectural Design &amp; Masterplanning</h3>
              <p class="service-detail">
                Regional masterplanning, high-rise commercial architecture, civic institutions, and luxury residential developments. We synthesize solar orientation, natural ventilation, and material longevity into enduring architectural forms.
              </p>
            </div>
          </li>

          <li class="service-list-item">
            <div class="service-num">02</div>
            <div class="service-body">
              <h3 class="service-name-serif">Structural &amp; Civil Engineering</h3>
              <p class="service-detail">
                Seismic-resistant reinforced concrete frames, post-tensioned floor systems, deep foundation design in complex soils, and computational finite-element load modeling for multi-story buildings and industrial spans.
              </p>
            </div>
          </li>

          <li class="service-list-item">
            <div class="service-num">03</div>
            <div class="service-body">
              <h3 class="service-name-serif">Mechanical, Electrical &amp; Plumbing (MEP)</h3>
              <p class="service-detail">
                Passive building physics, high-efficiency VRF climate control, centralized electrical distribution, emergency backup power infrastructure, clean water filtration, and certified building fire suppression systems.
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
  </main>

  {render_professional_footer("")}

  <script src="app.js"></script>
</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as hf:
    hf.write(homepage_html)

print("Generated editorial index.html without contact section successfully.")

# ==============================================================================
# 3. BUILD SITEMAP (sitemap.xml)
# ==============================================================================
sitemap_urls = [f"""  <url>
    <loc>{SITE_URL}/</loc>
    <lastmod>2026-11-19</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>"""]

for p in PROJECTS:
    pid = p["id"]
    sitemap_urls.append(f"""  <url>
    <loc>{SITE_URL}/projects/{pid}.html</loc>
    <lastmod>2026-11-19</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>""")

sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(sitemap_urls)}
</urlset>"""

with open("sitemap.xml", "w", encoding="utf-8") as sf:
    sf.write(sitemap_xml)

print(f"Generated sitemap.xml with {len(sitemap_urls)} URLs.")

# ==============================================================================
# 4. SYNC TO PUBLIC/ DIRECTORY FOR VERCEL DEPLOYMENT
# ==============================================================================
public_dir = "public"
os.makedirs(public_dir, exist_ok=True)
public_projects = os.path.join(public_dir, "projects")
os.makedirs(public_projects, exist_ok=True)

for f in ["index.html", "styles.css", "app.js", "sitemap.xml"]:
    if os.path.exists(f):
        shutil.copy2(f, os.path.join(public_dir, f))

if os.path.exists("projects"):
    for pf in os.listdir("projects"):
        if pf.endswith(".html"):
            shutil.copy2(os.path.join("projects", pf), os.path.join(public_projects, pf))

print("Successfully synchronized all files and static project pages to public/.")
