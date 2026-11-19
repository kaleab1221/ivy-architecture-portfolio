/**
 * IVY ARCHITECTURE & CONSTRUCTION
 * Premium Architectural Practice & Portfolio Platform
 * Second-Stage Professional Refinement
 */

(function () {
  'use strict';

  // State Management
  const state = {
    projects: window.IVY_PROJECTS || [],
    currentView: 'grid', // 'grid' | 'list' | 'regions'
    currentTypology: 'all',
    searchQuery: '',
    currentModalProjectId: null,
    currentGalleryIndex: 0,
    theme: localStorage.getItem('ivy-theme') || 'dark'
  };

  // DOM Elements Cache
  const el = {
    // Header & Navigation
    themeToggleBtn: document.getElementById('themeToggleBtn'),
    mobileMenuBtn: document.getElementById('mobileMenuBtn'),
    mobileNavDrawer: document.getElementById('mobileNavDrawer'),
    mobileNavClose: document.getElementById('mobileNavClose'),
    navLinks: document.querySelectorAll('.nav-link, .mobile-nav-link'),

    // Projects Grid & Filters
    typologyFilters: document.getElementById('typologyFilters'),
    viewGridContainer: document.getElementById('viewGridContainer'),

    // Case Study Modal Drawer
    modalBackdrop: document.getElementById('modalBackdrop'),
    modalCloseBtn: document.getElementById('modalCloseBtn'),
    modalPrevBtn: document.getElementById('modalPrevBtn'),
    modalNextBtn: document.getElementById('modalNextBtn'),
    modalShareBtn: document.getElementById('modalShareBtn'),
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

    // Inquiry Form, Toast & Back to Top
    inquiryForm: document.getElementById('inquiryForm'),
    toastBanner: document.getElementById('toastBanner'),
    backToTopBtn: document.getElementById('backToTopBtn')
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

    // Modal Share / Copy Link
    if (el.modalShareBtn) {
      el.modalShareBtn.addEventListener('click', async () => {
        try {
          if (navigator.clipboard && navigator.clipboard.writeText) {
            await navigator.clipboard.writeText(window.location.href);
            showToast('Direct project link copied to clipboard.');
          } else {
            showToast(`Project link: ${window.location.href}`);
          }
        } catch (err) {
          showToast(`Project link: ${window.location.href}`);
        }
      });
    }

    // Project Inquiry Form Submission
    const inquiryForm = document.getElementById('projectInquiryForm');
    if (inquiryForm) {
      inquiryForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const name = (document.getElementById('clientName')?.value || '').trim();
        const org = (document.getElementById('clientOrganization')?.value || '').trim();
        const email = (document.getElementById('clientEmail')?.value || '').trim();
        const phone = (document.getElementById('clientPhone')?.value || '').trim();
        const typology = document.getElementById('projectTypology')?.value || '';
        const location = (document.getElementById('projectLocation')?.value || '').trim();
        const description = (document.getElementById('projectDescription')?.value || '').trim();
        const statusNotice = document.getElementById('formStatusNotice');

        if (!name || !org || !email || !phone || !typology || !location || !description) {
          if (statusNotice) {
            statusNotice.style.display = 'block';
            statusNotice.className = 'form-status-notice error';
            statusNotice.textContent = 'Please complete all required fields (* marked) before transmitting your brief.';
          }
          return;
        }

        const subject = encodeURIComponent(`[Project Brief] ${typology} - ${org} (${name})`);
        const body = encodeURIComponent(
          `IVY ARCHITECTURE & CONSTRUCTION — PROJECT INQUIRY BRIEF\n` +
          `=======================================================\n\n` +
          `FULL NAME: ${name}\n` +
          `ORGANIZATION: ${org}\n` +
          `CORPORATE EMAIL: ${email}\n` +
          `TELEPHONE: ${phone}\n` +
          `PROJECT TYPOLOGY: ${typology}\n` +
          `PROJECT LOCATION: ${location}\n\n` +
          `BRIEF & SCOPE REQUIREMENTS:\n${description}\n\n` +
          `=======================================================\n` +
          `Transmitted via ivy-architecture-portfolio.vercel.app`
        );

        window.location.href = `mailto:info@ivyconstruction.com?subject=${subject}&body=${body}`;

        if (statusNotice) {
          statusNotice.style.display = 'block';
          statusNotice.className = 'form-status-notice success';
          statusNotice.innerHTML = `
            <strong>Project brief compiled.</strong><br>
            Your local email client has been launched with your structured technical brief addressed to <em>info@ivyconstruction.com</em>.<br>
            If your mail client did not open automatically, please send this brief directly to <a href="mailto:info@ivyconstruction.com" style="color: var(--accent-bronze); text-decoration: underline;">info@ivyconstruction.com</a> or telephone us at <strong>+251 91 123 4567</strong>.
          `;
        }
      });
    }

    // Back to Top button
    if (el.backToTopBtn) {
      el.backToTopBtn.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
    }

    // Scroll listener for Back to Top
    window.addEventListener('scroll', () => {
      if (el.backToTopBtn) {
        if (window.scrollY > 400) {
          el.backToTopBtn.classList.add('visible');
        } else {
          el.backToTopBtn.classList.remove('visible');
        }
      }
    }, { passive: true });

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
      { key: 'all', label: 'All Projects' },
      { key: 'featured', label: 'Featured Works' },
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
        : cat.key === 'featured'
        ? state.projects.filter(p => p.featured).length
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
      if (state.currentTypology === 'all') {
        return true;
      } else if (state.currentTypology === 'featured') {
        return p.featured === true;
      } else if (state.currentTypology === 'education') {
        return p.category === 'education' || p.category === 'healthcare';
      } else {
        return p.category === state.currentTypology;
      }
    });
  }

  // Master Render (Always 3-Column Editorial Grid)
  function render() {
    const filtered = getFilteredProjects();
    renderGrid(filtered);
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
      const descText = p.subtitle || p.description || '';

      return `
        <article class="project-card" data-id="${p.id}" tabindex="0">
          <div class="card-media-wrapper">
            <img src="${p.heroImage}" alt="${p.title}" loading="lazy">
          </div>
          <div class="card-content">
            <div class="card-header-meta">
              <span class="card-typology">${p.typology}</span>
              <span class="card-code">${p.code}</span>
            </div>
            <h3 class="card-title">${p.title}</h3>
            <p class="card-desc">${descText}</p>
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
