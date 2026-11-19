/**
 * IVY ARCHITECTURE & CONSTRUCTION
 * Premium Architectural Practice & Portfolio Platform
 */

(function () {
  'use strict';

  // State Management
  const state = {
    projects: window.IVY_PROJECTS || [],
    currentView: 'grid', // 'grid' | 'list'
    currentTypology: 'all',
    searchQuery: '',
    currentModalProjectId: null,
    currentGalleryIndex: 0,
    theme: localStorage.getItem('ivy-theme') || 'dark',
    sortColumn: 'code',
    sortAsc: true
  };

  // DOM Elements Cache
  const el = {
    // Header & Navigation
    themeToggleBtn: document.getElementById('themeToggleBtn'),
    mobileMenuBtn: document.getElementById('mobileMenuBtn'),
    mobileNavDrawer: document.getElementById('mobileNavDrawer'),
    mobileNavClose: document.getElementById('mobileNavClose'),
    navLinks: document.querySelectorAll('.nav-link, .mobile-nav-link'),

    // Projects Toolbar & Views
    typologyFilters: document.getElementById('typologyFilters'),
    searchInput: document.getElementById('searchInput'),
    viewGridBtn: document.getElementById('viewGridBtn'),
    viewListBtn: document.getElementById('viewListBtn'),
    viewGridContainer: document.getElementById('viewGridContainer'),
    viewListContainer: document.getElementById('viewListContainer'),

    // Table Hover Preview
    hoverPreviewCard: document.getElementById('hoverPreviewCard'),
    hoverPreviewImg: document.getElementById('hoverPreviewImg'),
    hoverPreviewTitle: document.getElementById('hoverPreviewTitle'),
    hoverPreviewMeta: document.getElementById('hoverPreviewMeta'),

    // Case Study Modal Drawer
    modalBackdrop: document.getElementById('modalBackdrop'),
    modalCloseBtn: document.getElementById('modalCloseBtn'),
    modalPrevBtn: document.getElementById('modalPrevBtn'),
    modalNextBtn: document.getElementById('modalNextBtn'),
    modalCodeTag: document.getElementById('modalCodeTag'),
    modalProjectTitle: document.getElementById('modalProjectTitle'),
    galleryMainImg: document.getElementById('galleryMainImg'),
    galleryCounter: document.getElementById('galleryCounter'),
    galleryThumbs: document.getElementById('galleryThumbs'),
    specTypology: document.getElementById('specTypology'),
    specLocation: document.getElementById('specLocation'),
    specStatus: document.getElementById('specStatus'),
    specScale: document.getElementById('specScale'),
    specClient: document.getElementById('specClient'),
    specScope: document.getElementById('specScope'),
    specStructure: document.getElementById('specStructure'),
    specEnvelope: document.getElementById('specEnvelope'),
    specClimate: document.getElementById('specClimate'),
    projectDescription: document.getElementById('projectDescription'),
    projectFeaturesList: document.getElementById('projectFeaturesList'),

    // Inquiry Form & Toast
    inquiryForm: document.getElementById('inquiryForm'),
    toastBanner: document.getElementById('toastBanner')
  };

  // App Initialization
  async function init() {
    setupTheme();
    setupEventListeners();
    await loadProjectData();
    renderTypologyFilters();
    render();
    handleHashRouting();
  }

  // Load project data (Fetch JSON with fallback to data.js)
  async function loadProjectData() {
    if (!state.projects || state.projects.length === 0) {
      try {
        const response = await fetch('projects.json');
        if (response.ok) {
          state.projects = await response.json();
        }
      } catch (err) {
        console.warn('Using embedded architectural data fallback', err);
      }
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
      ? `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="5"></circle>
          <line x1="12" y1="1" x2="12" y2="3"></line>
          <line x1="12" y1="21" x2="12" y2="23"></line>
          <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
          <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
          <line x1="1" y1="12" x2="3" y2="12"></line>
          <line x1="21" y1="12" x2="23" y2="12"></line>
          <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
          <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
        </svg>`
      : `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
        </svg>`;
  }

  // Event Listeners
  function setupEventListeners() {
    // Theme toggle
    if (el.themeToggleBtn) el.themeToggleBtn.addEventListener('click', toggleTheme);

    // Mobile nav toggle
    if (el.mobileMenuBtn && el.mobileNavDrawer) {
      el.mobileMenuBtn.addEventListener('click', () => el.mobileNavDrawer.classList.add('open'));
    }
    if (el.mobileNavClose && el.mobileNavDrawer) {
      el.mobileNavClose.addEventListener('click', () => el.mobileNavDrawer.classList.remove('open'));
    }
    document.querySelectorAll('.mobile-nav-link').forEach(link => {
      link.addEventListener('click', () => el.mobileNavDrawer.classList.remove('open'));
    });

    // View switchers
    if (el.viewGridBtn) el.viewGridBtn.addEventListener('click', () => setView('grid'));
    if (el.viewListBtn) el.viewListBtn.addEventListener('click', () => setView('list'));

    // Search input
    if (el.searchInput) {
      el.searchInput.addEventListener('input', (e) => {
        state.searchQuery = e.target.value.trim().toLowerCase();
        render();
      });
    }

    // Modal controls
    if (el.modalCloseBtn) el.modalCloseBtn.addEventListener('click', closeModal);
    if (el.modalBackdrop) {
      el.modalBackdrop.addEventListener('click', (e) => {
        if (e.target === el.modalBackdrop) closeModal();
      });
    }
    if (el.modalPrevBtn) el.modalPrevBtn.addEventListener('click', prevModalProject);
    if (el.modalNextBtn) el.modalNextBtn.addEventListener('click', nextModalProject);

    // Keyboard navigation
    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeModal();
      if (el.modalBackdrop && el.modalBackdrop.classList.contains('open')) {
        if (e.key === 'ArrowLeft') prevModalProject();
        if (e.key === 'ArrowRight') nextModalProject();
      }
    });

    // Inquiry Form Submission
    if (el.inquiryForm) {
      el.inquiryForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const clientName = document.getElementById('clientName').value;
        showToast(`Consultation brief received for ${clientName}. Reference #IVY-${Math.floor(1000 + Math.random() * 9000)} sent to your email.`);
        el.inquiryForm.reset();
      });
    }

    // Floating preview mouse tracking
    window.addEventListener('mousemove', (e) => {
      if (el.hoverPreviewCard && el.hoverPreviewCard.classList.contains('visible')) {
        const offset = 20;
        let x = e.clientX + offset;
        let y = e.clientY + offset;

        // Keep inside viewport bounds
        if (x + 340 > window.innerWidth) x = e.clientX - 340;
        if (y + 240 > window.innerHeight) y = e.clientY - 240;

        el.hoverPreviewCard.style.left = `${x}px`;
        el.hoverPreviewCard.style.top = `${y}px`;
      }
    });

    // Window Popstate (Deep Link Hash)
    window.addEventListener('popstate', handleHashRouting);
  }

  // Toast Notification
  function showToast(msg) {
    if (!el.toastBanner) return;
    el.toastBanner.textContent = msg;
    el.toastBanner.classList.add('show');
    setTimeout(() => {
      el.toastBanner.classList.remove('show');
    }, 4500);
  }

  // Typology Filters Rendering
  function renderTypologyFilters() {
    if (!el.typologyFilters) return;

    const categories = [
      { key: 'all', label: 'All Works' },
      { key: 'residential', label: 'Residential' },
      { key: 'mixed-use', label: 'Mixed-Use' },
      { key: 'corporate', label: 'Corporate' },
      { key: 'education', label: 'Education & Health' },
      { key: 'industrial', label: 'Industrial' },
      { key: 'hospitality', label: 'Hospitality' }
    ];

    el.typologyFilters.innerHTML = categories.map(cat => {
      const count = cat.key === 'all'
        ? state.projects.length
        : state.projects.filter(p => {
            if (cat.key === 'education') return p.category === 'education' || p.category === 'healthcare';
            return p.category === cat.key;
          }).length;

      return `
        <button class="filter-btn ${state.currentTypology === cat.key ? 'active' : ''}" data-typology="${cat.key}">
          <span>${cat.label}</span>
          <span style="opacity: 0.65; margin-left: 0.35rem; font-size: 0.7rem;">(${count})</span>
        </button>
      `;
    }).join('');

    el.typologyFilters.querySelectorAll('.filter-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const target = e.currentTarget;
        el.typologyFilters.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        target.classList.add('active');
        state.currentTypology = target.dataset.typology;
        render();
      });
    });
  }

  // Filter Logic
  function getFilteredProjects() {
    return state.projects.filter(p => {
      // Category filter
      let matchesCategory = false;
      if (state.currentTypology === 'all') {
        matchesCategory = true;
      } else if (state.currentTypology === 'education') {
        matchesCategory = p.category === 'education' || p.category === 'healthcare';
      } else {
        matchesCategory = p.category === state.currentTypology;
      }

      // Search filter
      let matchesSearch = true;
      if (state.searchQuery) {
        const query = state.searchQuery;
        const haystack = [
          p.title,
          p.location,
          p.city,
          p.country,
          p.typology,
          p.client,
          p.code,
          p.scope
        ].join(' ').toLowerCase();
        matchesSearch = haystack.includes(query);
      }

      return matchesCategory && matchesSearch;
    });
  }

  // View Switching
  function setView(viewName) {
    state.currentView = viewName;
    if (el.viewGridBtn) el.viewGridBtn.classList.toggle('active', viewName === 'grid');
    if (el.viewListBtn) el.viewListBtn.classList.toggle('active', viewName === 'list');
    
    if (el.viewGridContainer) el.viewGridContainer.style.display = viewName === 'grid' ? 'grid' : 'none';
    if (el.viewListContainer) el.viewListContainer.style.display = viewName === 'list' ? 'block' : 'none';
    
    render();
  }

  // Master Render
  function render() {
    const filtered = getFilteredProjects();

    if (state.currentView === 'grid') {
      renderGrid(filtered);
    } else {
      renderTable(filtered);
    }
  }

  // Render 3-Column Editorial Grid
  function renderGrid(projects) {
    if (!el.viewGridContainer) return;

    if (projects.length === 0) {
      el.viewGridContainer.innerHTML = `
        <div style="grid-column: 1 / -1; padding: 5rem 2rem; text-align: center; color: var(--text-muted); font-family: var(--font-mono);">
          NO PROJECTS FOUND MATCHING SELECTION CRITERIA.
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
        <article class="project-card" data-id="${p.id}" tabindex="0">
          <div class="card-media-wrapper">
            <span class="card-badge-code">[${p.code}]</span>
            <span class="card-badge-status ${statusClass}">
              <span class="status-dot"></span>${p.status}
            </span>
            <img src="${p.heroImage}" alt="${p.title} architectural view" loading="lazy">
          </div>
          <div class="card-content">
            <span class="card-typology">${p.typology}</span>
            <h3 class="card-title">${p.title}</h3>
            <div class="card-footer-meta">
              <span>${p.city}, ${p.country}</span>
              <span class="card-arrow">
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

    // Attach card click handlers
    el.viewGridContainer.querySelectorAll('.project-card').forEach(card => {
      card.addEventListener('click', () => openModal(card.dataset.id));
      card.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          openModal(card.dataset.id);
        }
      });
    });
  }

  // Render Complete Architectural Table Index
  function renderTable(projects) {
    if (!el.viewListContainer) return;

    if (projects.length === 0) {
      el.viewListContainer.innerHTML = `
        <div style="padding: 4rem 2rem; text-align: center; color: var(--text-muted); font-family: var(--font-mono);">
          NO PROJECTS FOUND MATCHING SELECTION CRITERIA.
        </div>
      `;
      return;
    }

    const tableHtml = `
      <table class="projects-table">
        <thead>
          <tr>
            <th>Code</th>
            <th>Project Title</th>
            <th>Typology</th>
            <th>Location</th>
            <th>Scale / Area</th>
            <th>Status</th>
            <th>Year</th>
          </tr>
        </thead>
        <tbody>
          ${projects.map(p => `
            <tr class="table-row" data-id="${p.id}" data-img="${p.heroImage}" data-title="${p.title}" data-loc="${p.location}">
              <td style="color: var(--accent-bronze); font-weight: 700;">[${p.code}]</td>
              <td style="color: var(--text-primary); font-weight: 600;">${p.title}</td>
              <td>${p.typology}</td>
              <td>${p.location}</td>
              <td>${p.scale}</td>
              <td>${p.status}</td>
              <td>${p.year || '—'}</td>
            </tr>
          `).join('')}
        </tbody>
      </table>
    `;

    el.viewListContainer.innerHTML = tableHtml;

    // Attach row events
    el.viewListContainer.querySelectorAll('.table-row').forEach(row => {
      row.addEventListener('click', () => openModal(row.dataset.id));

      row.addEventListener('mouseenter', () => {
        if (!el.hoverPreviewCard) return;
        el.hoverPreviewImg.src = row.dataset.img;
        el.hoverPreviewTitle.textContent = row.dataset.title;
        el.hoverPreviewMeta.textContent = row.dataset.loc;
        el.hoverPreviewCard.classList.add('visible');
      });

      row.addEventListener('mouseleave', () => {
        if (!el.hoverPreviewCard) return;
        el.hoverPreviewCard.classList.remove('visible');
      });
    });
  }

  // Project Case Study Modal
  function openModal(projectId) {
    const project = state.projects.find(p => p.id === projectId);
    if (!project) return;

    state.currentModalProjectId = projectId;
    state.currentGalleryIndex = 0;

    // Set textual details
    if (el.modalCodeTag) el.modalCodeTag.textContent = `[${project.code}]`;
    if (el.modalProjectTitle) el.modalProjectTitle.textContent = project.title;
    if (el.specTypology) el.specTypology.textContent = project.typology;
    if (el.specLocation) el.specLocation.textContent = project.location;
    if (el.specStatus) el.specStatus.textContent = project.status;
    if (el.specScale) el.specScale.textContent = project.scale;
    if (el.specClient) el.specClient.textContent = project.client;
    if (el.specScope) el.specScope.textContent = project.scope;
    if (el.specStructure) el.specStructure.textContent = project.structure || 'Reinforced Concrete Superstructure';
    if (el.specEnvelope) el.specEnvelope.textContent = project.envelope || 'High-Performance Insulated Glazing';
    if (el.specClimate) el.specClimate.textContent = project.climate || 'Passive Solar Shading & Cross-Ventilation';
    if (el.projectDescription) el.projectDescription.textContent = project.description;

    // Features list
    if (el.projectFeaturesList) {
      if (project.keyFeatures && project.keyFeatures.length > 0) {
        el.projectFeaturesList.innerHTML = project.keyFeatures.map(f => `<li>${f}</li>`).join('');
      } else {
        el.projectFeaturesList.innerHTML = '<li>Full architectural construction documentation</li><li>Seismic analysis & structural foundation engineering</li>';
      }
    }

    // Gallery Render
    renderGallery(project);

    // Open Drawer
    if (el.modalBackdrop) {
      el.modalBackdrop.classList.add('open');
      document.body.style.overflow = 'hidden';
    }

    // Set URL Hash
    history.pushState(null, '', `#project/${project.id}`);
  }

  function renderGallery(project) {
    const images = project.images && project.images.length > 0 ? project.images : [project.heroImage];

    if (el.galleryMainImg) {
      el.galleryMainImg.src = images[state.currentGalleryIndex] || project.heroImage;
    }

    if (el.galleryCounter) {
      el.galleryCounter.textContent = `${String(state.currentGalleryIndex + 1).padStart(2, '0')} / ${String(images.length).padStart(2, '0')}`;
    }

    if (el.galleryThumbs) {
      el.galleryThumbs.innerHTML = images.map((img, idx) => `
        <img src="${img}" class="gallery-thumb ${idx === state.currentGalleryIndex ? 'active' : ''}" data-idx="${idx}" alt="Thumb ${idx + 1}">
      `).join('');

      el.galleryThumbs.querySelectorAll('.gallery-thumb').forEach(thumb => {
        thumb.addEventListener('click', (e) => {
          state.currentGalleryIndex = parseInt(e.currentTarget.dataset.idx, 10);
          renderGallery(project);
        });
      });
    }
  }

  function closeModal() {
    if (el.modalBackdrop) {
      el.modalBackdrop.classList.remove('open');
      document.body.style.overflow = '';
    }
    state.currentModalProjectId = null;
    history.pushState(null, '', window.location.pathname);
  }

  function prevModalProject() {
    const filtered = getFilteredProjects();
    if (filtered.length <= 1) return;
    const currentIndex = filtered.findIndex(p => p.id === state.currentModalProjectId);
    const prevIndex = (currentIndex - 1 + filtered.length) % filtered.length;
    openModal(filtered[prevIndex].id);
  }

  function nextModalProject() {
    const filtered = getFilteredProjects();
    if (filtered.length <= 1) return;
    const currentIndex = filtered.findIndex(p => p.id === state.currentModalProjectId);
    const nextIndex = (currentIndex + 1) % filtered.length;
    openModal(filtered[nextIndex].id);
  }

  // Handle Hash Routing
  function handleHashRouting() {
    const hash = window.location.hash;
    if (hash.startsWith('#project/')) {
      const pId = hash.replace('#project/', '');
      openModal(pId);
    }
  }

  // Execute on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
