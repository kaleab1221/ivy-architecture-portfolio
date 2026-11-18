/**
 * IVY CONSTRUCTION & TRADING CO. LTD.
 * Interactive Architectural Platform (BIG.DK Reference)
 */

(function () {
  'use strict';

  // State Management
  const state = {
    projects: window.IVY_PROJECTS || [],
    currentView: 'grid', // 'grid' | 'list' | 'map'
    currentTypology: 'all',
    currentStatus: 'all',
    searchQuery: '',
    currentModalProjectId: null,
    currentGalleryIndex: 0,
    heroIndex: 0,
    theme: localStorage.getItem('ivy-theme') || 'dark',
    activeRegion: 'all'
  };

  // Flagship Hero Showcase IDs
  const HERO_PROJECT_IDS = ['ivy-28', 'ivy-03', 'ivy-05', 'ivy-12', 'ivy-08', 'ivy-22'];

  // DOM Elements
  const el = {
    // Header
    themeToggleBtn: document.getElementById('themeToggleBtn'),
    mobileMenuBtn: document.getElementById('mobileMenuBtn'),
    mobileNavDrawer: document.getElementById('mobileNavDrawer'),
    mobileNavClose: document.getElementById('mobileNavClose'),
    
    // Hero
    heroSliderContainer: document.getElementById('heroSliderContainer'),
    heroTag: document.getElementById('heroTag'),
    heroTitle: document.getElementById('heroTitle'),
    heroLocation: document.getElementById('heroLocation'),
    heroTypology: document.getElementById('heroTypology'),
    heroScale: document.getElementById('heroScale'),
    heroPrevBtn: document.getElementById('heroPrevBtn'),
    heroNextBtn: document.getElementById('heroNextBtn'),
    heroExploreBtn: document.getElementById('heroExploreBtn'),
    
    // Stats
    statProjects: document.getElementById('statProjects'),
    
    // Toolbar & Filters
    typologyFilters: document.getElementById('typologyFilters'),
    statusPills: document.getElementById('statusPills'),
    searchInput: document.getElementById('searchInput'),
    viewGridBtn: document.getElementById('viewGridBtn'),
    viewListBtn: document.getElementById('viewListBtn'),
    viewMapBtn: document.getElementById('viewMapBtn'),
    resultsCount: document.getElementById('resultsCount'),
    
    // Views Containers
    viewGridContainer: document.getElementById('viewGridContainer'),
    viewListContainer: document.getElementById('viewListContainer'),
    viewMapContainer: document.getElementById('viewMapContainer'),
    
    // Floating List Hover Preview
    hoverPreviewCard: document.getElementById('hoverPreviewCard'),
    hoverPreviewImg: document.getElementById('hoverPreviewImg'),
    hoverPreviewTitle: document.getElementById('hoverPreviewTitle'),
    hoverPreviewMeta: document.getElementById('hoverPreviewMeta'),
    
    // Modal / Drawer
    modalBackdrop: document.getElementById('modalBackdrop'),
    modalCloseBtn: document.getElementById('modalCloseBtn'),
    modalPrevBtn: document.getElementById('modalPrevBtn'),
    modalNextBtn: document.getElementById('modalNextBtn'),
    modalCodeTag: document.getElementById('modalCodeTag'),
    modalProjectTitle: document.getElementById('modalProjectTitle'),
    galleryStage: document.getElementById('galleryStage'),
    galleryPrevBtn: document.getElementById('galleryPrevBtn'),
    galleryNextBtn: document.getElementById('galleryNextBtn'),
    galleryCounter: document.getElementById('galleryCounter'),
    galleryThumbs: document.getElementById('galleryThumbs'),
    projectDescription: document.getElementById('projectDescription'),
    projectFeaturesList: document.getElementById('projectFeaturesList'),
    specClient: document.getElementById('specClient'),
    specLocation: document.getElementById('specLocation'),
    specTypology: document.getElementById('specTypology'),
    specStatus: document.getElementById('specStatus'),
    specScale: document.getElementById('specScale'),
    specScope: document.getElementById('specScope'),
    specYear: document.getElementById('specYear'),
    
    // Contact Form & Toast
    rfpForm: document.getElementById('rfpForm'),
    toastNotice: document.getElementById('toastNotice')
  };

  // Initialize
  async function init() {
    setupTheme();
    setupEventListeners();
    await loadProjectData();
    initHero();
    renderTypologyFilters();
    render();
    handleHashRouting();
  }

  // Load project data
  async function loadProjectData() {
    if (!state.projects || state.projects.length === 0) {
      try {
        const response = await fetch('projects.json');
        if (response.ok) {
          state.projects = await response.json();
        }
      } catch (err) {
        console.warn('Using embedded fallback data', err);
      }
    }
    if (el.statProjects) {
      el.statProjects.textContent = `${state.projects.length}+`;
    }
  }

  // Theme setup
  function setupTheme() {
    document.documentElement.setAttribute('data-theme', state.theme);
    updateThemeIcon();
  }

  function toggleTheme() {
    state.theme = state.theme === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', state.theme);
    localStorage.setItem('ivy-theme', state.theme);
    updateThemeIcon();
  }

  function updateThemeIcon() {
    if (!el.themeToggleBtn) return;
    el.themeToggleBtn.innerHTML = state.theme === 'dark' 
      ? '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>'
      : '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';
  }

  // Setup Event Listeners
  function setupEventListeners() {
    // Theme
    el.themeToggleBtn.addEventListener('click', toggleTheme);

    // Mobile nav
    el.mobileMenuBtn.addEventListener('click', () => el.mobileNavDrawer.classList.add('open'));
    el.mobileNavClose.addEventListener('click', () => el.mobileNavDrawer.classList.remove('open'));
    document.querySelectorAll('.mobile-nav-link').forEach(link => {
      link.addEventListener('click', () => el.mobileNavDrawer.classList.remove('open'));
    });

    // View switcher
    el.viewGridBtn.addEventListener('click', () => setView('grid'));
    el.viewListBtn.addEventListener('click', () => setView('list'));
    el.viewMapBtn.addEventListener('click', () => setView('map'));

    // Status pills
    document.querySelectorAll('.status-pill').forEach(pill => {
      pill.addEventListener('click', (e) => {
        document.querySelectorAll('.status-pill').forEach(p => p.classList.remove('active'));
        e.target.classList.add('active');
        state.currentStatus = e.target.dataset.status;
        render();
      });
    });

    // Search input
    el.searchInput.addEventListener('input', (e) => {
      state.searchQuery = e.target.value.trim().toLowerCase();
      render();
    });

    // Hero buttons
    el.heroPrevBtn.addEventListener('click', prevHero);
    el.heroNextBtn.addEventListener('click', nextHero);
    el.heroExploreBtn.addEventListener('click', () => {
      const heroProjects = getHeroProjects();
      const current = heroProjects[state.heroIndex];
      if (current) openModal(current.id);
    });

    // Modal controls
    el.modalCloseBtn.addEventListener('click', closeModal);
    el.modalBackdrop.addEventListener('click', (e) => {
      if (e.target === el.modalBackdrop) closeModal();
    });
    el.modalPrevBtn.addEventListener('click', prevModalProject);
    el.modalNextBtn.addEventListener('click', nextModalProject);

    // Gallery controls
    el.galleryPrevBtn.addEventListener('click', prevGalleryImage);
    el.galleryNextBtn.addEventListener('click', nextGalleryImage);

    // Keyboard navigation
    window.addEventListener('keydown', (e) => {
      if (!el.modalBackdrop.classList.contains('open')) return;
      if (e.key === 'Escape') closeModal();
      else if (e.key === 'ArrowLeft') prevGalleryImage();
      else if (e.key === 'ArrowRight') nextGalleryImage();
    });

    // Hash change
    window.addEventListener('hashchange', handleHashRouting);

    // RFP Form
    if (el.rfpForm) {
      el.rfpForm.addEventListener('submit', (e) => {
        e.preventDefault();
        showToast('Inquiry received. An IVY partner will contact you within 24 hours.');
        el.rfpForm.reset();
      });
    }

    // Auto hero slider
    setInterval(nextHero, 6500);
  }

  // Toast notification
  function showToast(msg) {
    if (!el.toastNotice) return;
    el.toastNotice.textContent = msg;
    el.toastNotice.classList.add('show');
    setTimeout(() => {
      el.toastNotice.classList.remove('show');
    }, 4000);
  }

  // Hero section management
  function getHeroProjects() {
    return state.projects.filter(p => HERO_PROJECT_IDS.includes(p.id));
  }

  function initHero() {
    const heroProjects = getHeroProjects();
    if (!heroProjects || heroProjects.length === 0) return;

    el.heroSliderContainer.innerHTML = heroProjects.map((p, idx) => `
      <div class="hero-slide ${idx === 0 ? 'active' : ''}" data-index="${idx}">
        <img src="${p.heroImage}" alt="${p.title}" loading="${idx === 0 ? 'eager' : 'lazy'}">
      </div>
    `).join('');

    updateHeroDisplay();
  }

  function updateHeroDisplay() {
    const heroProjects = getHeroProjects();
    if (!heroProjects || heroProjects.length === 0) return;
    const p = heroProjects[state.heroIndex];
    if (!p) return;

    // Update slides
    document.querySelectorAll('.hero-slide').forEach((slide, idx) => {
      slide.classList.toggle('active', idx === state.heroIndex);
    });

    // Update textual meta
    el.heroTag.innerHTML = `<span>[${p.code}]</span> <span>/</span> <span>${p.typology}</span>`;
    el.heroTitle.textContent = p.title;
    el.heroLocation.textContent = p.location;
    el.heroTypology.textContent = p.typology;
    el.heroScale.textContent = p.scale;
  }

  function nextHero() {
    const heroProjects = getHeroProjects();
    if (!heroProjects.length) return;
    state.heroIndex = (state.heroIndex + 1) % heroProjects.length;
    updateHeroDisplay();
  }

  function prevHero() {
    const heroProjects = getHeroProjects();
    if (!heroProjects.length) return;
    state.heroIndex = (state.heroIndex - 1 + heroProjects.length) % heroProjects.length;
    updateHeroDisplay();
  }

  // Typology filters rendering
  function renderTypologyFilters() {
    const typologies = [
      { key: 'all', label: 'All Works' },
      { key: 'residential', label: 'Residential' },
      { key: 'mixed-use', label: 'Mixed-Use' },
      { key: 'corporate', label: 'Corporate' },
      { key: 'education', label: 'Education' },
      { key: 'hospitality', label: 'Hospitality' },
      { key: 'industrial', label: 'Industrial' },
      { key: 'monumental', label: 'Monumental' }
    ];

    el.typologyFilters.innerHTML = typologies.map(t => {
      const count = t.key === 'all' 
        ? state.projects.length 
        : state.projects.filter(p => p.category === t.key).length;

      return `
        <button class="filter-btn ${state.currentTypology === t.key ? 'active' : ''}" data-typology="${t.key}">
          ${t.label} <span class="filter-count">(${count})</span>
        </button>
      `;
    }).join('');

    el.typologyFilters.querySelectorAll('.filter-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        el.typologyFilters.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        const target = e.currentTarget;
        target.classList.add('active');
        state.currentTypology = target.dataset.typology;
        render();
      });
    });
  }

  // Filter projects helper
  function getFilteredProjects() {
    return state.projects.filter(p => {
      // Typology match
      const matchTypology = state.currentTypology === 'all' || p.category === state.currentTypology;

      // Status match
      let matchStatus = true;
      if (state.currentStatus !== 'all') {
        if (state.currentStatus === 'completed') matchStatus = p.statusType === 'completed';
        else if (state.currentStatus === 'construction') matchStatus = p.statusType === 'construction';
        else if (state.currentStatus === 'design') matchStatus = p.statusType === 'design';
      }

      // Search match
      let matchSearch = true;
      if (state.searchQuery) {
        const q = state.searchQuery;
        const haystack = [
          p.title,
          p.subtitle,
          p.location,
          p.city,
          p.country,
          p.client,
          p.code,
          p.typology,
          p.description
        ].join(' ').toLowerCase();
        matchSearch = haystack.includes(q);
      }

      return matchTypology && matchStatus && matchSearch;
    });
  }

  // Set View mode ('grid' | 'list' | 'map')
  function setView(viewMode) {
    state.currentView = viewMode;
    el.viewGridBtn.classList.toggle('active', viewMode === 'grid');
    el.viewListBtn.classList.toggle('active', viewMode === 'list');
    el.viewMapBtn.classList.toggle('active', viewMode === 'map');

    el.viewGridContainer.style.display = viewMode === 'grid' ? 'grid' : 'none';
    el.viewListContainer.style.display = viewMode === 'list' ? 'block' : 'none';
    el.viewMapContainer.style.display = viewMode === 'map' ? 'grid' : 'none';

    render();
  }

  // Main Render Router
  function render() {
    const filtered = getFilteredProjects();

    // Results count label
    if (el.resultsCount) {
      el.resultsCount.textContent = `Showing ${filtered.length} of ${state.projects.length} Works`;
    }

    if (state.currentView === 'grid') {
      renderGridView(filtered);
    } else if (state.currentView === 'list') {
      renderListView(filtered);
    } else if (state.currentView === 'map') {
      renderMapView(filtered);
    }
  }

  // Render Grid View
  function renderGridView(projects) {
    if (projects.length === 0) {
      el.viewGridContainer.innerHTML = `
        <div style="grid-column: 1 / -1; padding: 4rem; text-align: center; color: var(--text-muted); font-family: var(--font-mono);">
          NO PROJECTS FOUND MATCHING THE SELECTED CRITERIA.
        </div>
      `;
      return;
    }

    el.viewGridContainer.innerHTML = projects.map(p => {
      const statusClass = p.statusType === 'completed' 
        ? 'status-completed' 
        : p.statusType === 'construction' 
        ? 'status-construction' 
        : 'status-design';

      return `
        <article class="project-card" data-id="${p.id}">
          <div class="card-media">
            <span class="card-badge-code">${p.code}</span>
            <span class="card-badge-status ${statusClass}">
              <span class="status-dot"></span>${p.status}
            </span>
            <img src="${p.heroImage}" alt="${p.title}" loading="lazy">
          </div>
          <div class="card-body">
            <span class="card-typology">${p.typology}</span>
            <h3 class="card-title">${p.title}</h3>
            <div class="card-meta">
              <span>${p.city}, ${p.country}</span>
              <span class="card-action-arrow">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <line x1="5" y1="12" x2="19" y2="12"></line>
                  <polyline points="12 5 19 12 12 19"></polyline>
                </svg>
              </span>
            </div>
          </div>
        </article>
      `;
    }).join('');

    // Attach click listeners to cards
    el.viewGridContainer.querySelectorAll('.project-card').forEach(card => {
      card.addEventListener('click', () => {
        openModal(card.dataset.id);
      });
    });
  }

  // Render List / Index View (The BIG Table)
  function renderListView(projects) {
    if (projects.length === 0) {
      el.viewListContainer.innerHTML = `
        <div style="padding: 4rem; text-align: center; color: var(--text-muted); font-family: var(--font-mono);">
          NO PROJECTS FOUND.
        </div>
      `;
      return;
    }

    el.viewListContainer.innerHTML = `
      <div class="index-table-wrapper">
        <table class="index-table">
          <thead>
            <tr>
              <th style="width: 50px;">NO.</th>
              <th style="width: 90px;">CODE</th>
              <th>PROJECT NAME</th>
              <th>TYPOLOGY</th>
              <th>LOCATION</th>
              <th>STATUS</th>
              <th>SCALE / AREA</th>
              <th>CLIENT</th>
            </tr>
          </thead>
          <tbody>
            ${projects.map((p, idx) => `
              <tr class="table-row" data-id="${p.id}" data-img="${p.heroImage}" data-title="${p.title}" data-loc="${p.location}">
                <td>${String(idx + 1).padStart(2, '0')}</td>
                <td class="col-code">${p.code}</td>
                <td class="col-title">${p.title}</td>
                <td>${p.typology}</td>
                <td>${p.location}</td>
                <td>
                  <span class="status-dot" style="background-color: ${
                    p.statusType === 'completed' ? 'var(--accent-green)' :
                    p.statusType === 'construction' ? 'var(--accent-orange)' : 'var(--accent-blue)'
                  };"></span>
                  ${p.status}
                </td>
                <td>${p.scale}</td>
                <td>${p.client}</td>
              </tr>
            `).join('')}
          </tbody>
        </table>
      </div>
    `;

    // Row clicks & Floating preview card
    const rows = el.viewListContainer.querySelectorAll('.table-row');
    rows.forEach(row => {
      row.addEventListener('click', () => {
        openModal(row.dataset.id);
      });

      row.addEventListener('mouseenter', (e) => {
        el.hoverPreviewImg.src = row.dataset.img;
        el.hoverPreviewTitle.textContent = row.dataset.title;
        el.hoverPreviewMeta.textContent = row.dataset.loc;
        el.hoverPreviewCard.classList.add('visible');
      });

      row.addEventListener('mousemove', (e) => {
        const x = e.clientX + 20;
        const y = e.clientY + 20;
        // Keep within viewport bounds
        const cardWidth = 280;
        const cardHeight = 220;
        const maxX = window.innerWidth - cardWidth - 20;
        const maxY = window.innerHeight - cardHeight - 20;

        el.hoverPreviewCard.style.left = `${Math.min(x, maxX)}px`;
        el.hoverPreviewCard.style.top = `${Math.min(y, maxY)}px`;
      });

      row.addEventListener('mouseleave', () => {
        el.hoverPreviewCard.classList.remove('visible');
      });
    });
  }

  // Render Map / Territory Matrix View
  function renderMapView(projects) {
    const territories = [
      { id: 'all', name: 'All Regions', count: projects.length },
      { id: 'addis', name: 'Addis Ababa Metro', count: projects.filter(p => p.city === 'Addis Ababa').length },
      { id: 'oromia', name: 'Bishoftu & Oromia', count: projects.filter(p => p.city === 'Bishoftu' || p.city === 'Assela').length },
      { id: 'south-sudan', name: 'South Sudan (Juba & Unity)', count: projects.filter(p => p.country === 'South Sudan').length },
      { id: 'regional-et', name: 'Regional Ethiopia (Afar, Gondar, Hosanna)', count: projects.filter(p => ['Afar Region', 'Afedera', 'Gondar', 'Hosanna', 'Gambella', 'Bensa'].includes(p.city)).length },
      { id: 'international', name: 'Middle East (Erbil, Iraq)', count: projects.filter(p => p.country === 'Iraq').length }
    ];

    // Filter projects for selected territory
    let displayedProjects = projects;
    if (state.activeRegion === 'addis') {
      displayedProjects = projects.filter(p => p.city === 'Addis Ababa');
    } else if (state.activeRegion === 'oromia') {
      displayedProjects = projects.filter(p => p.city === 'Bishoftu' || p.city === 'Assela');
    } else if (state.activeRegion === 'south-sudan') {
      displayedProjects = projects.filter(p => p.country === 'South Sudan');
    } else if (state.activeRegion === 'regional-et') {
      displayedProjects = projects.filter(p => ['Afar Region', 'Afedera', 'Gondar', 'Hosanna', 'Gambella', 'Bensa'].includes(p.city));
    } else if (state.activeRegion === 'international') {
      displayedProjects = projects.filter(p => p.country === 'Iraq');
    }

    el.viewMapContainer.innerHTML = `
      <div class="territory-sidebar">
        <h3 class="font-display" style="font-size: 1.25rem; text-transform: uppercase;">Operating Hubs</h3>
        <p style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--text-secondary); line-height: 1.6;">
          Select a geographic territory to inspect localized project nodes and infrastructural deployments across East Africa and the Middle East.
        </p>
        <div class="territory-hub-list">
          ${territories.map(t => `
            <button class="territory-hub-btn ${state.activeRegion === t.id ? 'active' : ''}" data-region="${t.id}">
              <span>${t.name}</span>
              <span class="territory-hub-badge">${t.count}</span>
            </button>
          `).join('')}
        </div>
      </div>
      <div class="territory-map-canvas">
        <div style="margin-bottom: 1.5rem; display: flex; justify-content: space-between; align-items: baseline; border-bottom: 1px solid var(--border-color); padding-bottom: 0.75rem;">
          <span class="mono" style="font-size: 0.75rem; color: var(--accent-gold); text-transform: uppercase;">
            REGIONAL DEPLOYMENTS // ${state.activeRegion.toUpperCase()}
          </span>
          <span class="mono" style="font-size: 0.7rem; color: var(--text-muted);">
            ${displayedProjects.length} COMMISSIONS
          </span>
        </div>
        <div class="matrix-nodes-grid">
          ${displayedProjects.map(p => `
            <div class="matrix-node-card" data-id="${p.id}">
              <div class="node-code">[${p.code}]</div>
              <div class="node-title">${p.title}</div>
              <div class="node-location">${p.location}</div>
            </div>
          `).join('')}
        </div>
      </div>
    `;

    // Territory button clicks
    el.viewMapContainer.querySelectorAll('.territory-hub-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        state.activeRegion = e.currentTarget.dataset.region;
        render();
      });
    });

    // Node card clicks
    el.viewMapContainer.querySelectorAll('.matrix-node-card').forEach(card => {
      card.addEventListener('click', () => {
        openModal(card.dataset.id);
      });
    });
  }

  // Open Project Modal / Case Study Drawer
  function openModal(projectId) {
    const project = state.projects.find(p => p.id === projectId);
    if (!project) return;

    state.currentModalProjectId = projectId;
    state.currentGalleryIndex = 0;

    // Header info
    el.modalCodeTag.textContent = project.code;
    el.modalProjectTitle.textContent = project.title;

    // Gallery render
    updateGallery();

    // Narratives & specs
    el.projectDescription.textContent = project.description;
    
    // Key features list
    if (project.keyFeatures && project.keyFeatures.length > 0) {
      el.projectFeaturesList.innerHTML = project.keyFeatures.map(f => `
        <li class="feature-item">
          <span class="feature-bullet">■</span>
          <span>${f}</span>
        </li>
      `).join('');
    } else {
      el.projectFeaturesList.innerHTML = '';
    }

    // Specifications
    el.specClient.textContent = project.client || 'Confidential';
    el.specLocation.textContent = project.location;
    el.specTypology.textContent = project.typology;
    el.specStatus.textContent = project.status;
    el.specScale.textContent = project.scale || 'N/A';
    el.specScope.textContent = project.scope || 'Turnkey Architecture & Engineering';
    el.specYear.textContent = project.year || '2024';

    // Open drawer
    el.modalBackdrop.classList.add('open');
    document.body.style.overflow = 'hidden';

    // Set URL hash
    window.location.hash = `project/${project.id}`;
  }

  function closeModal() {
    el.modalBackdrop.classList.remove('open');
    document.body.style.overflow = '';
    state.currentModalProjectId = null;
    history.replaceState(null, null, ' ');
  }

  function updateGallery() {
    const project = state.projects.find(p => p.id === state.currentModalProjectId);
    if (!project || !project.images || project.images.length === 0) return;

    const currentImg = project.images[state.currentGalleryIndex] || project.heroImage;
    el.galleryStage.innerHTML = `<img src="${currentImg}" alt="${project.title}">`;
    el.galleryCounter.textContent = `${state.currentGalleryIndex + 1} / ${project.images.length}`;

    // Thumbs
    if (project.images.length > 1) {
      el.galleryThumbs.style.display = 'flex';
      el.galleryThumbs.innerHTML = project.images.map((img, idx) => `
        <div class="gallery-thumb ${idx === state.currentGalleryIndex ? 'active' : ''}" data-index="${idx}">
          <img src="${img}" alt="Thumbnail">
        </div>
      `).join('');

      el.galleryThumbs.querySelectorAll('.gallery-thumb').forEach(th => {
        th.addEventListener('click', (e) => {
          state.currentGalleryIndex = parseInt(e.currentTarget.dataset.index, 10);
          updateGallery();
        });
      });
    } else {
      el.galleryThumbs.style.display = 'none';
    }
  }

  function nextGalleryImage() {
    const project = state.projects.find(p => p.id === state.currentModalProjectId);
    if (!project || !project.images) return;
    state.currentGalleryIndex = (state.currentGalleryIndex + 1) % project.images.length;
    updateGallery();
  }

  function prevGalleryImage() {
    const project = state.projects.find(p => p.id === state.currentModalProjectId);
    if (!project || !project.images) return;
    state.currentGalleryIndex = (state.currentGalleryIndex - 1 + project.images.length) % project.images.length;
    updateGallery();
  }

  function nextModalProject() {
    const filtered = getFilteredProjects();
    const curIdx = filtered.findIndex(p => p.id === state.currentModalProjectId);
    if (curIdx === -1) return;
    const nextIdx = (curIdx + 1) % filtered.length;
    openModal(filtered[nextIdx].id);
  }

  function prevModalProject() {
    const filtered = getFilteredProjects();
    const curIdx = filtered.findIndex(p => p.id === state.currentModalProjectId);
    if (curIdx === -1) return;
    const prevIdx = (curIdx - 1 + filtered.length) % filtered.length;
    openModal(filtered[prevIdx].id);
  }

  // Handle Hash Deep Linking
  function handleHashRouting() {
    const hash = window.location.hash;
    if (hash.startsWith('#project/')) {
      const pId = hash.replace('#project/', '');
      openModal(pId);
    }
  }

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
