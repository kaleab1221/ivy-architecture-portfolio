/**
 * IVY ARCHITECTURE & CONSTRUCTION — INTERACTIVE CONTROLLER
 * Handles:
 * 1. Hybrid Project Card Grid Category Tabs & Instant Live Search
 * 2. Complete Project Index Table Ledger Dynamic Multi-Filter
 * 3. Theme Toggle (Dark / Light with LocalStorage Persistence)
 * 4. 4-Field Consultation Brief Form Submission & Mailto / WhatsApp Routing
 * 5. Smooth Anchor Scrolling & Accessibility Enhancements
 */

(function () {
  'use strict';

  // State Management
  const state = {
    theme: localStorage.getItem('ivy-editorial-theme') || 'dark',
    activeCategory: 'all',
    searchQuery: '',
    tableSector: 'all',
    tableCountry: 'all',
    tableStatus: 'all'
  };

  // DOM Elements
  const dom = {
    html: document.documentElement,
    themeToggleBtn: document.getElementById('themeToggleBtn'),
    // Hybrid Card Grid
    categoryTabs: document.querySelectorAll('.category-tab-btn'),
    projectSearchInput: document.getElementById('projectSearchInput'),
    gridCountIndicator: document.getElementById('gridCountIndicator'),
    projectCards: document.querySelectorAll('.project-card'),
    // Table Ledger
    filterSector: document.getElementById('filterSector'),
    filterCountry: document.getElementById('filterCountry'),
    filterStatus: document.getElementById('filterStatus'),
    resetFiltersBtn: document.getElementById('resetFiltersBtn'),
    indexCountIndicator: document.getElementById('indexCountIndicator'),
    indexRows: document.querySelectorAll('.index-row'),
    // Form
    consultationBriefForm: document.getElementById('consultationBriefForm'),
    formFeedbackBanner: document.getElementById('formFeedbackBanner')
  };

  // ============================================================================
  // 1. THEME MANAGEMENT
  // ============================================================================
  function initTheme() {
    dom.html.setAttribute('data-theme', state.theme);
    updateThemeButtonLabel();

    if (dom.themeToggleBtn) {
      dom.themeToggleBtn.addEventListener('click', toggleTheme);
    }
  }

  function toggleTheme() {
    state.theme = state.theme === 'dark' ? 'light' : 'dark';
    dom.html.setAttribute('data-theme', state.theme);
    localStorage.setItem('ivy-editorial-theme', state.theme);
    updateThemeButtonLabel();
  }

  function updateThemeButtonLabel() {
    if (!dom.themeToggleBtn) return;
    const label = dom.themeToggleBtn.querySelector('.theme-toggle-label');
    if (label) {
      label.textContent = state.theme === 'dark' ? 'Light' : 'Dark';
    }
  }

  // ============================================================================
  // 2. HYBRID CARD GRID FILTERING & LIVE SEARCH
  // ============================================================================
  function initCardGrid() {
    if (!dom.projectCards || dom.projectCards.length === 0) return;

    // Category Tabs click handler
    if (dom.categoryTabs) {
      dom.categoryTabs.forEach(btn => {
        btn.addEventListener('click', () => {
          dom.categoryTabs.forEach(b => {
            b.classList.remove('active');
            b.setAttribute('aria-selected', 'false');
          });
          btn.classList.add('active');
          btn.setAttribute('aria-selected', 'true');

          state.activeCategory = btn.getAttribute('data-category') || 'all';
          applyGridFilter();
        });
      });
    }

    // Live Instant Search input handler
    if (dom.projectSearchInput) {
      dom.projectSearchInput.addEventListener('input', (e) => {
        state.searchQuery = e.target.value.trim().toLowerCase();
        applyGridFilter();
      });
    }

    applyGridFilter();
  }

  function applyGridFilter() {
    let visibleCount = 0;
    const totalCount = dom.projectCards.length;

    dom.projectCards.forEach(card => {
      const cat = card.getAttribute('data-category') || '';
      const isFeatured = card.getAttribute('data-featured') === 'true';
      const title = card.getAttribute('data-title') || '';
      const city = card.getAttribute('data-city') || '';
      const country = card.getAttribute('data-country') || '';
      const client = card.getAttribute('data-client') || '';

      // 1. Category Tab match
      let matchCategory = false;
      if (state.activeCategory === 'all') {
        matchCategory = true;
      } else if (state.activeCategory === 'featured') {
        matchCategory = isFeatured;
      } else if (state.activeCategory === 'education') {
        matchCategory = (cat === 'education' || cat === 'healthcare');
      } else {
        matchCategory = (cat === state.activeCategory);
      }

      // 2. Search Query match
      let matchSearch = true;
      if (state.searchQuery) {
        const query = state.searchQuery;
        const haystack = `${title} ${city} ${country} ${client} ${cat}`.toLowerCase();
        matchSearch = haystack.includes(query);
      }

      if (matchCategory && matchSearch) {
        card.style.display = '';
        visibleCount++;
      } else {
        card.style.display = 'none';
      }
    });

    if (dom.gridCountIndicator) {
      dom.gridCountIndicator.textContent = `Showing ${visibleCount} of ${totalCount} projects`;
    }
  }

  // ============================================================================
  // 3. TABLE LEDGER MULTI-FILTER (SECTOR, COUNTRY, STATUS)
  // ============================================================================
  function initTableLedger() {
    if (!dom.indexRows || dom.indexRows.length === 0) return;

    if (dom.filterSector) {
      dom.filterSector.addEventListener('change', (e) => {
        state.tableSector = e.target.value;
        applyTableFilter();
      });
    }

    if (dom.filterCountry) {
      dom.filterCountry.addEventListener('change', (e) => {
        state.tableCountry = e.target.value;
        applyTableFilter();
      });
    }

    if (dom.filterStatus) {
      dom.filterStatus.addEventListener('change', (e) => {
        state.tableStatus = e.target.value;
        applyTableFilter();
      });
    }

    if (dom.resetFiltersBtn) {
      dom.resetFiltersBtn.addEventListener('click', () => {
        state.tableSector = 'all';
        state.tableCountry = 'all';
        state.tableStatus = 'all';
        if (dom.filterSector) dom.filterSector.value = 'all';
        if (dom.filterCountry) dom.filterCountry.value = 'all';
        if (dom.filterStatus) dom.filterStatus.value = 'all';
        applyTableFilter();
      });
    }

    applyTableFilter();
  }

  function applyTableFilter() {
    let visibleRows = 0;
    const totalRows = dom.indexRows.length;

    dom.indexRows.forEach(row => {
      const sector = row.getAttribute('data-sector') || '';
      const country = row.getAttribute('data-country') || '';
      const status = row.getAttribute('data-status') || '';

      const matchSector = state.tableSector === 'all' || sector === state.tableSector;
      const matchCountry = state.tableCountry === 'all' || country === state.tableCountry;
      const matchStatus = state.tableStatus === 'all' || status === state.tableStatus;

      if (matchSector && matchCountry && matchStatus) {
        row.style.display = '';
        visibleRows++;
      } else {
        row.style.display = 'none';
      }
    });

    if (dom.indexCountIndicator) {
      dom.indexCountIndicator.textContent = `Showing ${visibleRows} of ${totalRows} commissions`;
    }
  }

  // ============================================================================
  // 4. CONSULTATION BRIEF FORM HANDLER
  // ============================================================================
  function initForm() {
    if (!dom.consultationBriefForm) return;

    dom.consultationBriefForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const name = (document.getElementById('clientName')?.value || '').trim();
      const contact = (document.getElementById('clientContact')?.value || '').trim();
      const sector = (document.getElementById('projectSector')?.value || '').trim();
      const brief = (document.getElementById('projectBrief')?.value || '').trim();

      if (!name || !contact || !sector || !brief) {
        showFormFeedback('Please complete all four fields before transmitting your brief.', 'error');
        return;
      }

      // Format email transmission
      const subject = encodeURIComponent(`IVY Commission Brief: ${sector} &mdash; ${name}`);
      const body = encodeURIComponent(
        `Dear IVY Architecture & Construction Partners,

` +
        `Client Name & Organization: ${name}
` +
        `Direct Contact: ${contact}
` +
        `Sector / Typology: ${sector}

` +
        `Project Scope & Target Timeline:
${brief}

` +
        `---
Transmitted via IVY Integrated Architecture Portfolio Monograph`
      );

      const mailtoUrl = `mailto:info@ivyconstruction.com?subject=${subject}&body=${body}`;
      
      showFormFeedback('Brief prepared. Opening executive partner mail client...', 'success');

      setTimeout(() => {
        window.location.href = mailtoUrl;
      }, 600);
    });
  }

  function showFormFeedback(msg, type) {
    if (!dom.formFeedbackBanner) return;
    dom.formFeedbackBanner.textContent = msg;
    dom.formFeedbackBanner.className = `form-feedback-banner ${type}`;
    dom.formFeedbackBanner.style.display = 'block';

    setTimeout(() => {
      if (dom.formFeedbackBanner) {
        dom.formFeedbackBanner.style.display = 'none';
      }
    }, 6000);
  }

  // ============================================================================
  // 5. SMOOTH SCROLLING WITH OFFSET FOR STICKY HEADER
  // ============================================================================
  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function (e) {
        const targetId = this.getAttribute('href');
        if (targetId === '#' || targetId === '#main-content') return;
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
          e.preventDefault();
          const headerOffset = 84;
          const elementPosition = targetElement.getBoundingClientRect().top;
          const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

          window.scrollTo({
            top: offsetPosition,
            behavior: 'smooth'
          });
        }
      });
    });
  }

  // Initialize all controllers on DOM ready
  document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    initCardGrid();
    initTableLedger();
    initForm();
    initSmoothScroll();
  });
})();
