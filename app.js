/**
 * CYBERWATCH // SIH26184
 * Enterprise Cybercrime Intelligence Command Center Engine (Tailwind / Shadcn Edition)
 */

// Embedded Fallback Dataset (Guarantees 100% offline functionality)
const FALLBACK_FORECASTS = [
  {
    priority_rank: 1, grid_cell_id: "CELL_03_15",
    centroid_lat: 28.535, centroid_lon: 77.255,
    lat_min: 28.530, lat_max: 28.540, lon_min: 77.250, lon_max: 77.260,
    pred_hotspot_prob: 0.9821, expected_withdrawals: 3.1,
    count_ci_lower: 2.2, count_ci_upper: 4.0, cell_atm_count: 29, transit_score: 0.768,
    risk_tier: "CRITICAL",
    top_contributing_factors: "Historical Recency Momentum (30d) | Weekly Repeat Withdrawal Burst",
    sop: "Deploy plainclothes static unit for Shift Alpha (14:00 - 22:00 IST). Monitor ATM vestibules discretely for multi-card cash sweeps."
  },
  {
    priority_rank: 2, grid_cell_id: "CELL_04_15",
    centroid_lat: 28.545, centroid_lon: 77.255,
    lat_min: 28.540, lat_max: 28.550, lon_min: 77.250, lon_max: 77.260,
    pred_hotspot_prob: 0.9821, expected_withdrawals: 7.8,
    count_ci_lower: 6.9, count_ci_upper: 8.7, cell_atm_count: 26, transit_score: 0.742,
    risk_tier: "CRITICAL",
    top_contributing_factors: "Historical Recency Momentum (30d) | Weekly Repeat Withdrawal Burst",
    sop: "Deploy plainclothes static unit for Shift Bravo (22:00 - 06:00 IST). Coordinate with bank security for rapid interdiction."
  },
  {
    priority_rank: 3, grid_cell_id: "CELL_13_11",
    centroid_lat: 28.635, centroid_lon: 77.215,
    lat_min: 28.630, lat_max: 28.640, lon_min: 77.210, lon_max: 77.220,
    pred_hotspot_prob: 0.9595, expected_withdrawals: 2.1,
    count_ci_lower: 1.2, count_ci_upper: 3.0, cell_atm_count: 31, transit_score: 0.910,
    risk_tier: "CRITICAL",
    top_contributing_factors: "Historical Recency Momentum (30d) | Short-Term Cash-Out Surge (3d)",
    sop: "Assign mobile motorcycle patrol in 20-min sweeps. Inspect commercial transit hub ATM vestibules."
  },
  {
    priority_rank: 4, grid_cell_id: "CELL_01_15",
    centroid_lat: 28.515, centroid_lon: 77.255,
    lat_min: 28.510, lat_max: 28.520, lon_min: 77.250, lon_max: 77.260,
    pred_hotspot_prob: 0.9548, expected_withdrawals: 1.9,
    count_ci_lower: 1.0, count_ci_upper: 2.8, cell_atm_count: 22, transit_score: 0.680,
    risk_tier: "CRITICAL",
    top_contributing_factors: "Historical Recency Momentum (30d) | Weekly Repeat Withdrawal Burst",
    sop: "Dispatch Section 91 CrPC CCTV preservation dockets to acquiring banks before automated 15-day purge."
  },
  {
    priority_rank: 5, grid_cell_id: "CELL_05_16",
    centroid_lat: 28.555, centroid_lon: 77.265,
    lat_min: 28.550, lat_max: 28.560, lon_min: 77.260, lon_max: 77.270,
    pred_hotspot_prob: 0.9522, expected_withdrawals: 1.8,
    count_ci_lower: 0.9, count_ci_upper: 2.7, cell_atm_count: 24, transit_score: 0.720,
    risk_tier: "CRITICAL",
    top_contributing_factors: "Weekly Repeat Withdrawal Burst | Historical Recency Momentum (30d)",
    sop: "Plainclothes monitoring during afternoon banking rush (14:00 - 18:00 IST)."
  },
  {
    priority_rank: 6, grid_cell_id: "CELL_03_17",
    centroid_lat: 28.535, centroid_lon: 77.275,
    lat_min: 28.530, lat_max: 28.540, lon_min: 77.270, lon_max: 77.280,
    pred_hotspot_prob: 0.9368, expected_withdrawals: 1.4,
    count_ci_lower: 0.5, count_ci_upper: 2.3, cell_atm_count: 19, transit_score: 0.650,
    risk_tier: "CRITICAL",
    top_contributing_factors: "Historical Recency Momentum (30d) | Weekly Repeat Withdrawal Burst",
    sop: "Monitor commercial shopping complex ATM corridor for repeat mule withdrawals."
  },
  {
    priority_rank: 7, grid_cell_id: "CELL_02_15",
    centroid_lat: 28.525, centroid_lon: 77.255,
    lat_min: 28.520, lat_max: 28.530, lon_min: 77.250, lon_max: 77.260,
    pred_hotspot_prob: 0.9257, expected_withdrawals: 1.5,
    count_ci_lower: 0.6, count_ci_upper: 2.4, cell_atm_count: 18, transit_score: 0.630,
    risk_tier: "CRITICAL",
    top_contributing_factors: "Historical Recency Momentum (30d) | Weekly Repeat Withdrawal Burst",
    sop: "Enforce bank step-up friction: lower single withdrawal caps to INR 10,000."
  },
  {
    priority_rank: 8, grid_cell_id: "CELL_02_16",
    centroid_lat: 28.525, centroid_lon: 77.265,
    lat_min: 28.520, lat_max: 28.530, lon_min: 77.260, lon_max: 77.270,
    pred_hotspot_prob: 0.9234, expected_withdrawals: 1.5,
    count_ci_lower: 0.6, count_ci_upper: 2.4, cell_atm_count: 21, transit_score: 0.690,
    risk_tier: "CRITICAL",
    top_contributing_factors: "Historical Recency Momentum (30d) | Short-Term Cash-Out Surge (3d)",
    sop: "Enforce dynamic friction on non-home debit cards."
  },
  {
    priority_rank: 9, grid_cell_id: "CELL_14_12",
    centroid_lat: 28.645, centroid_lon: 77.225,
    lat_min: 28.640, lat_max: 28.650, lon_min: 77.220, lon_max: 77.230,
    pred_hotspot_prob: 0.9189, expected_withdrawals: 1.3,
    count_ci_lower: 0.4, count_ci_upper: 2.2, cell_atm_count: 27, transit_score: 0.880,
    risk_tier: "CRITICAL",
    top_contributing_factors: "Historical Recency Momentum (30d) | High Density ATM Infrastructure",
    sop: "Coordinate with metro transit police for immediate cash interdiction sweeps."
  },
  {
    priority_rank: 10, grid_cell_id: "CELL_04_16",
    centroid_lat: 28.545, centroid_lon: 77.265,
    lat_min: 28.540, lat_max: 28.550, lon_min: 77.260, lon_max: 77.270,
    pred_hotspot_prob: 0.9122, expected_withdrawals: 1.3,
    count_ci_lower: 0.4, count_ci_upper: 2.2, cell_atm_count: 23, transit_score: 0.710,
    risk_tier: "CRITICAL",
    top_contributing_factors: "Historical Recency Momentum (30d) | Known Mule Syndicate Corridors",
    sop: "High visibility static cruiser deployment during peak afternoon withdrawal window."
  },
  {
    priority_rank: 11, grid_cell_id: "CELL_11_12",
    centroid_lat: 28.615, centroid_lon: 77.225,
    lat_min: 28.610, lat_max: 28.620, lon_min: 77.220, lon_max: 77.230,
    pred_hotspot_prob: 0.8840, expected_withdrawals: 1.1,
    count_ci_lower: 0.2, count_ci_upper: 2.0, cell_atm_count: 17, transit_score: 0.750,
    risk_tier: "ELEVATED",
    top_contributing_factors: "Historical Recency Momentum (30d) | High Density ATM Infrastructure",
    sop: "Routine motorcycle patrol sweeps every 30 minutes."
  },
  {
    priority_rank: 12, grid_cell_id: "CELL_12_11",
    centroid_lat: 28.625, centroid_lon: 77.215,
    lat_min: 28.620, lat_max: 28.630, lon_min: 77.210, lon_max: 77.220,
    pred_hotspot_prob: 0.8650, expected_withdrawals: 1.0,
    count_ci_lower: 0.1, count_ci_upper: 1.9, cell_atm_count: 19, transit_score: 0.820,
    risk_tier: "ELEVATED",
    top_contributing_factors: "Historical Recency Momentum (30d) | Known Mule Syndicate Corridors",
    sop: "Alert bank fraud risk management to monitor withdrawal velocity."
  }
];

// Exploration audit patrol zones (20% anti-bias safeguard)
const EXPLORATION_ZONES = [
  { lat: 28.505, lon: 77.105, radius: 1000, label: "Audit Zone Alpha (CELL_00_00)" },
  { lat: 28.685, lon: 77.125, radius: 1000, label: "Audit Zone Bravo (CELL_18_02)" },
  { lat: 28.695, lon: 77.285, radius: 1000, label: "Audit Zone Charlie (CELL_19_18)" },
  { lat: 28.515, lon: 77.285, radius: 1000, label: "Audit Zone Delta (CELL_01_18)" }
];

// Global State
let mapInstance = null;
let top10LayerGroup = null;
let explorationLayerGroup = null;
let gridPolygonsGroup = null;

let activeForecasts = FALLBACK_FORECASTS;
let filteredForecasts = FALLBACK_FORECASTS;
let selectedCell = FALLBACK_FORECASTS[0];

// Table Pagination State
let currentPage = 1;
let pageSize = 10;
let currentSortCol = "rank";
let sortAsc = true;
let activeFilterTier = "ALL";

// Initialize on DOM Ready
document.addEventListener("DOMContentLoaded", () => {
  initLiveClock();
  initViewTabs();
  initMap();
  initTableData();
  setupTableSearch();
  setupFilterChips();
  setupSimulator();
  tryFetchLiveForecasts();
  if (window.lucide) lucide.createIcons();
});

// 1. Live IST Clock
function initLiveClock() {
  const clockEl = document.getElementById("live-ist-clock");
  function tick() {
    const now = new Date();
    const istTime = now.toLocaleTimeString("en-GB", { timeZone: "Asia/Kolkata" });
    if (clockEl) {
      clockEl.innerText = `IST: ${istTime}`;
    }
  }
  tick();
  setInterval(tick, 1000);
}

// 2. View Mode Tabs (Tab Switching)
function initViewTabs() {
  const tabBtns = document.querySelectorAll(".nav-tab-btn");
  tabBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      const targetPanelId = btn.getAttribute("data-target");
      switchView(targetPanelId, btn);
    });
  });
}

function switchView(panelId, activeBtn) {
  document.querySelectorAll(".nav-tab-btn").forEach(b => {
    b.className = "nav-tab-btn flex items-center gap-2 px-3.5 py-1.5 rounded-lg text-slate-400 hover:text-white transition-all whitespace-nowrap";
  });
  document.querySelectorAll(".deck-panel").forEach(p => {
    p.classList.remove("active");
    p.classList.add("hidden");
  });

  if (activeBtn) {
    activeBtn.className = "nav-tab-btn flex items-center gap-2 px-3.5 py-1.5 rounded-lg text-slate-950 bg-cyan-400 font-bold transition-all whitespace-nowrap active shadow-[0_2px_10px_rgba(56,189,248,0.4)]";
  } else {
    const matchingBtn = document.querySelector(`.nav-tab-btn[data-target="${panelId}"]`);
    if (matchingBtn) {
      matchingBtn.className = "nav-tab-btn flex items-center gap-2 px-3.5 py-1.5 rounded-lg text-slate-950 bg-cyan-400 font-bold transition-all whitespace-nowrap active shadow-[0_2px_10px_rgba(56,189,248,0.4)]";
    }
  }

  const targetPanel = document.getElementById(panelId);
  if (targetPanel) {
    targetPanel.classList.remove("hidden");
    targetPanel.classList.add("active");
  }

  // If switched to map, invalidate size so tiles align smoothly
  if (panelId === "panel-gis" && mapInstance) {
    setTimeout(() => {
      mapInstance.invalidateSize();
    }, 150);
  }
  if (window.lucide) lucide.createIcons();
}

// 3. Initialize Leaflet Map
function initMap() {
  if (typeof L === "undefined") {
    console.warn("Leaflet library not loaded yet.");
    const container = document.getElementById("gis-map-container");
    if (container) {
      container.innerHTML = `
        <div style="display:flex;align-items:center;justify-content:center;height:100%;color:#94a3b8;font-family:sans-serif;text-align:center;padding:20px;">
          <div>
            <div style="font-size:36px;margin-bottom:12px;">🗺️</div>
            <h4 style="color:#f8fafc;margin-bottom:8px;font-size:16px;">Interactive GIS Spatial Surface Ready</h4>
            <p style="max-width:440px;font-size:13px;line-height:1.5;color:#94a3b8;margin:0 auto 16px;">
              Geospatial 20×20 quadrant matrix generated. All 400 prioritized ATM sectors, live 1930 telemetry simulator, and forensic XAI inspector below are fully active.
            </p>
          </div>
        </div>`;
    }
    return;
  }

  const mapCenter = [28.57, 77.23];
  mapInstance = L.map("gis-map-container", {
    center: mapCenter,
    zoom: 11,
    zoomControl: true
  });

  // High-performance CartoDB Dark Matter Tiles (zero rate-limit, crisp dark mode)
  L.tileLayer("https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png", {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
    subdomains: 'abcd',
    maxZoom: 19
  }).addTo(mapInstance);

  top10LayerGroup = L.layerGroup().addTo(mapInstance);
  explorationLayerGroup = L.layerGroup().addTo(mapInstance);
  gridPolygonsGroup = L.layerGroup().addTo(mapInstance);

  renderMapLayers();

  // Layer Toggles
  const btnTop10 = document.getElementById("btn-toggle-top10");
  if (btnTop10) {
    btnTop10.addEventListener("click", function() {
      this.classList.toggle("active");
      this.classList.toggle("opacity-60");
      if (mapInstance.hasLayer(top10LayerGroup)) {
        mapInstance.removeLayer(top10LayerGroup);
      } else {
        mapInstance.addLayer(top10LayerGroup);
      }
    });
  }

  const btnExploration = document.getElementById("btn-toggle-exploration");
  if (btnExploration) {
    btnExploration.addEventListener("click", function() {
      this.classList.toggle("active");
      this.classList.toggle("opacity-60");
      if (mapInstance.hasLayer(explorationLayerGroup)) {
        mapInstance.removeLayer(explorationLayerGroup);
      } else {
        mapInstance.addLayer(explorationLayerGroup);
      }
    });
  }

  const btnReset = document.getElementById("btn-reset-map");
  if (btnReset) {
    btnReset.addEventListener("click", () => {
      mapInstance.setView(mapCenter, 11);
      showToast("Map view reset to metropolitan extent.");
    });
  }
}

// Jump to Sector helper
function jumpToSector(lat, lon, zoom) {
  if (mapInstance) {
    mapInstance.setView([lat, lon], zoom);
    showToast(`Focused sector at ${lat.toFixed(3)}°N, ${lon.toFixed(3)}°E`);
  }
}

// 4. Render GIS Layers on Map
function renderMapLayers() {
  if (!mapInstance) return;

  top10LayerGroup.clearLayers();
  gridPolygonsGroup.clearLayers();
  explorationLayerGroup.clearLayers();

  // Render Grid Quadrants
  activeForecasts.forEach(cell => {
    const isTop10 = cell.priority_rank <= 10;
    const color = isTop10 ? "#fb7185" : "#fbbf24";
    const fillOpacity = isTop10 ? 0.35 : 0.18;

    const bounds = [
      [cell.lat_min || (cell.centroid_lat - 0.005), cell.lon_min || (cell.centroid_lon - 0.005)],
      [cell.lat_max || (cell.centroid_lat + 0.005), cell.lon_max || (cell.centroid_lon + 0.005)]
    ];

    const rect = L.rectangle(bounds, {
      color: color,
      weight: 1.5,
      fillColor: color,
      fillOpacity: fillOpacity
    });

    rect.on("click", () => inspectCell(cell));
    rect.bindTooltip(`<b>${cell.grid_cell_id}</b> (#${cell.priority_rank})<br>P(Hotspot): ${(cell.pred_hotspot_prob * 100).toFixed(1)}%<br>Tier: ${cell.risk_tier}`, {
      sticky: true
    });

    gridPolygonsGroup.addLayer(rect);

    // Glowing Markers for Top-10
    if (isTop10) {
      const markerHtml = `
        <div style="background: rgba(251, 113, 133, 0.95); width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #fff; font-family: monospace; font-size: 10px; font-weight: 800; border: 2px solid #fff; box-shadow: 0 0 10px rgba(251, 113, 133, 0.8);">
          ${cell.priority_rank}
        </div>`;
      const customIcon = L.divIcon({
        html: markerHtml,
        className: 'leaflet-pulsing-marker',
        iconSize: [22, 22],
        iconAnchor: [11, 11]
      });

      const marker = L.marker([cell.centroid_lat, cell.centroid_lon], { icon: customIcon });
      marker.on("click", () => inspectCell(cell));
      marker.bindPopup(`
        <div style="color: #060911; font-family: sans-serif; padding: 4px;">
          <h4 style="margin: 0 0 4px; font-size: 13px;">#${cell.priority_rank}: ${cell.grid_cell_id}</h4>
          <p style="margin: 0 0 2px; font-size: 11px;"><strong>P(Hotspot):</strong> ${(cell.pred_hotspot_prob * 100).toFixed(1)}%</p>
          <p style="margin: 0 0 2px; font-size: 11px;"><strong>Expected 24h:</strong> ${cell.expected_withdrawals} withdrawals</p>
          <p style="margin: 0 0 4px; font-size: 11px;"><strong>Risk Tier:</strong> <span style="color: #e11d48; font-weight: bold;">${cell.risk_tier}</span></p>
          <div style="font-size: 10px; color: #475569; border-top: 1px solid #e2e8f0; padding-top: 4px;">${cell.top_contributing_factors}</div>
        </div>
      `);
      top10LayerGroup.addLayer(marker);
    }
  });

  // Render Exploration Zones
  EXPLORATION_ZONES.forEach(zone => {
    const circle = L.circle([zone.lat, zone.lon], {
      radius: zone.radius,
      color: "#38bdf8",
      weight: 1.5,
      dashArray: "4, 6",
      fillColor: "#38bdf8",
      fillOpacity: 0.12
    });
    circle.bindTooltip(`<b>20% Audit Zone:</b><br>${zone.label}`, { sticky: true });
    explorationLayerGroup.addLayer(circle);
  });
}

// 5. Inspect Cell in Drawer
function inspectCell(cell) {
  selectedCell = cell;

  const idEl = document.getElementById("insp-cell-id");
  const rankEl = document.getElementById("insp-rank");
  const tierEl = document.getElementById("insp-tier");
  const coordsEl = document.getElementById("insp-coords");
  const probEl = document.getElementById("insp-prob");
  const countEl = document.getElementById("insp-count");
  const ciEl = document.getElementById("insp-ci");
  const atmsEl = document.getElementById("insp-atms");
  const transitEl = document.getElementById("insp-transit");
  const sopEl = document.getElementById("insp-sop");
  const driversContainer = document.getElementById("insp-drivers");

  if (idEl) idEl.innerText = cell.grid_cell_id;
  if (rankEl) rankEl.innerText = `PRIORITY #${cell.priority_rank}`;
  
  if (tierEl) {
    tierEl.innerText = `${cell.risk_tier} HOTSPOT`;
    tierEl.className = cell.risk_tier === "CRITICAL"
      ? "px-2 py-0.5 rounded text-[11px] font-mono font-bold uppercase bg-rose-500/15 border border-rose-500/40 text-rose-300"
      : "px-2 py-0.5 rounded text-[11px] font-mono font-bold uppercase bg-amber-500/15 border border-amber-500/40 text-amber-300";
  }

  if (coordsEl) coordsEl.innerText = `${cell.centroid_lat.toFixed(3)}°N, ${cell.centroid_lon.toFixed(3)}°E (1km × 1km Quadrant)`;
  if (probEl) probEl.innerText = `${(cell.pred_hotspot_prob * 100).toFixed(1)}%`;
  if (countEl) countEl.innerText = `${cell.expected_withdrawals}`;
  if (ciEl) ciEl.innerText = `[${cell.count_ci_lower} - ${cell.count_ci_upper}]`;
  if (atmsEl) atmsEl.innerText = `${cell.cell_atm_count || 10} Terminals`;
  if (transitEl) transitEl.innerText = (cell.transit_score !== undefined ? cell.transit_score.toFixed(3) : "0.768");
  if (sopEl) sopEl.innerText = cell.sop || "Deploy plainclothes unit for active corridor interdiction.";

  if (driversContainer) {
    driversContainer.innerHTML = "";
    const rawDrivers = (cell.top_contributing_factors || "Historical Recency Momentum").split("|");
    rawDrivers.forEach(d => {
      const chip = document.createElement("span");
      chip.className = "px-2.5 py-1 rounded-full text-[11px] font-medium bg-cyan-500/10 border border-cyan-500/30 text-cyan-300";
      chip.innerText = d.trim();
      driversContainer.appendChild(chip);
    });
  }

  // Smoothly center map if open
  if (mapInstance) {
    mapInstance.panTo([cell.centroid_lat, cell.centroid_lon]);
  }
}

// 6. Copy Section 91 CrPC Field Docket
function copySection91Docket() {
  if (!selectedCell) return;
  const text = `================================================================================
SECTION 91 CrPC PRESERVATION & TACTICAL INTERDICTION DOCKET
CASE REF: NCRP-1930 // OPERATION HOTSPOT SHIFT
================================================================================
GRID CELL: ${selectedCell.grid_cell_id} (Priority Rank: #${selectedCell.priority_rank})
COORDINATES: ${selectedCell.centroid_lat.toFixed(4)}°N, ${selectedCell.centroid_lon.toFixed(4)}°E (1km Quadrant)
RISK TIER: ${selectedCell.risk_tier}
FORECAST CASH-OUT PROBABILITY: ${(selectedCell.pred_hotspot_prob * 100).toFixed(2)}%
CONFORMAL 90% UNCERTAINTY BAND: [${selectedCell.count_ci_lower} to ${selectedCell.count_ci_upper} withdrawals]
ATM TERMINAL DENSITY: ${selectedCell.cell_atm_count || 10} terminals
TOP XAI DRIVERS: ${selectedCell.top_contributing_factors}

STATUTORY DIRECTIVES:
1. Dispatch plainclothes interdiction team for designated corridor shift.
2. Direct acquiring banks to preserve vestibule CCTV footage pursuant to Section 91 CrPC.
3. Enforce step-up biometric/PIN friction on non-home debit cards (cap: INR 10,000).
================================================================================`;

  navigator.clipboard.writeText(text).then(() => {
    showToast("Section 91 CrPC Field Docket copied to clipboard!");
  }).catch(() => {
    showToast("Docket ready for dispatch review.");
  });
}

// 7. Table Data & Pagination Engine
function initTableData() {
  updateFilterCounts();
  applyFiltersAndSort();
}

function updateFilterCounts() {
  const cntAll = document.getElementById("cnt-all");
  const cntCrit = document.getElementById("cnt-crit");
  const cntElev = document.getElementById("cnt-elev");
  const cntAudit = document.getElementById("cnt-audit");

  const total = activeForecasts.length;
  const crit = activeForecasts.filter(c => c.risk_tier === "CRITICAL").length;
  const elev = activeForecasts.filter(c => c.risk_tier === "ELEVATED").length;
  const audit = EXPLORATION_ZONES.length;

  if (cntAll) cntAll.innerText = total;
  if (cntCrit) cntCrit.innerText = crit;
  if (cntElev) cntElev.innerText = elev;
  if (cntAudit) cntAudit.innerText = audit;
}

function setupFilterChips() {
  const chips = document.querySelectorAll(".filter-chip");
  chips.forEach(chip => {
    chip.addEventListener("click", () => {
      chips.forEach(c => {
        c.className = "filter-chip px-3 py-1.5 rounded-full font-semibold border border-slate-800 bg-slate-900 text-slate-400 hover:text-white transition-all";
      });
      chip.className = "filter-chip px-3 py-1.5 rounded-full font-semibold border border-cyan-500 bg-cyan-500/15 text-cyan-300 transition-all active";
      activeFilterTier = chip.getAttribute("data-filter");
      currentPage = 1;
      applyFiltersAndSort();
    });
  });
}

function setupTableSearch() {
  const searchInput = document.getElementById("table-search");
  if (searchInput) {
    searchInput.addEventListener("input", (e) => {
      currentPage = 1;
      applyFiltersAndSort();
    });
  }
}

function applyFiltersAndSort() {
  const searchVal = (document.getElementById("table-search")?.value || "").toLowerCase().trim();

  filteredForecasts = activeForecasts.filter(item => {
    // Tier filter
    if (activeFilterTier === "CRITICAL" && item.risk_tier !== "CRITICAL") return false;
    if (activeFilterTier === "ELEVATED" && item.risk_tier !== "ELEVATED") return false;
    if (activeFilterTier === "EXPLORATION" && item.priority_rank > 80) return false;

    // Search query
    if (searchVal) {
      const matchId = item.grid_cell_id.toLowerCase().includes(searchVal);
      const matchDrivers = (item.top_contributing_factors || "").toLowerCase().includes(searchVal);
      const matchCoords = `${item.centroid_lat},${item.centroid_lon}`.includes(searchVal);
      if (!matchId && !matchDrivers && !matchCoords) return false;
    }
    return true;
  });

  // Sort
  filteredForecasts.sort((a, b) => {
    let valA = a[currentSortCol];
    let valB = b[currentSortCol];

    if (currentSortCol === "rank") {
      valA = a.priority_rank; valB = b.priority_rank;
    } else if (currentSortCol === "id") {
      valA = a.grid_cell_id; valB = b.grid_cell_id;
    } else if (currentSortCol === "prob") {
      valA = a.pred_hotspot_prob; valB = b.pred_hotspot_prob;
    }

    if (valA < valB) return sortAsc ? -1 : 1;
    if (valA > valB) return sortAsc ? 1 : -1;
    return 0;
  });

  renderTablePage();
}

function sortTable(columnKey) {
  if (currentSortCol === columnKey) {
    sortAsc = !sortAsc;
  } else {
    currentSortCol = columnKey;
    sortAsc = true;
  }
  applyFiltersAndSort();
  showToast(`Sorted by ${columnKey.toUpperCase()} (${sortAsc ? 'Ascending' : 'Descending'})`);
}

function renderTablePage() {
  const tbody = document.getElementById("hotspots-tbody");
  if (!tbody) return;
  tbody.innerHTML = "";

  const total = filteredForecasts.length;
  const startIdx = (currentPage - 1) * pageSize;
  const endIdx = Math.min(startIdx + pageSize, total);
  const pageSlice = filteredForecasts.slice(startIdx, endIdx);

  if (pageSlice.length === 0) {
    tbody.innerHTML = `<tr><td colspan="9" style="text-align:center; padding:30px; color:#64748b;">No sectors match current search/filter criteria.</td></tr>`;
    updatePaginationControls(0, 0, 0);
    return;
  }

  pageSlice.forEach(item => {
    const tr = document.createElement("tr");
    tr.className = "hover:bg-slate-900/40 transition-colors";
    const isTop10 = item.priority_rank <= 10;
    const tierBadgeClass = item.risk_tier === "CRITICAL"
      ? "bg-rose-500/15 border-rose-500/40 text-rose-300"
      : "bg-amber-500/15 border-amber-500/40 text-amber-300";

    tr.innerHTML = `
      <td class="py-2.5 px-4"><span class="font-mono font-bold ${isTop10 ? 'text-rose-400' : 'text-slate-400'}">#${item.priority_rank}</span></td>
      <td class="py-2.5 px-4"><span class="font-mono font-semibold text-cyan-400">${item.grid_cell_id}</span></td>
      <td class="py-2.5 px-4 font-mono text-slate-400 text-[11px]">${item.centroid_lat.toFixed(3)}°N, ${item.centroid_lon.toFixed(3)}°E</td>
      <td class="py-2.5 px-4"><span class="font-mono font-extrabold ${isTop10 ? 'text-rose-400' : 'text-amber-400'}">${(item.pred_hotspot_prob * 100).toFixed(1)}%</span></td>
      <td class="py-2.5 px-4 font-mono">${item.expected_withdrawals} <span class="text-slate-500 text-[11px]">[${item.count_ci_lower}-${item.count_ci_upper}]</span></td>
      <td class="py-2.5 px-4 font-mono text-slate-300">${item.cell_atm_count || 10}</td>
      <td class="py-2.5 px-4"><span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold border ${tierBadgeClass}">${item.risk_tier}</span></td>
      <td class="py-2.5 px-4 text-slate-300 max-w-[260px] truncate">${item.top_contributing_factors}</td>
      <td class="py-2.5 px-4 text-right">
        <button class="px-2.5 py-1 rounded bg-slate-800 hover:bg-cyan-500 hover:text-slate-950 text-slate-300 text-[11px] font-semibold transition-all" onclick="inspectFromTable('${item.grid_cell_id}')">Inspect ↗</button>
      </td>
    `;
    tbody.appendChild(tr);
  });

  updatePaginationControls(startIdx + 1, endIdx, total);
  if (window.lucide) lucide.createIcons();
}

function inspectFromTable(cellId) {
  const cell = activeForecasts.find(c => c.grid_cell_id === cellId);
  if (cell) {
    inspectCell(cell);
    switchView("panel-gis");
    showToast(`Focused sector ${cellId} on geospatial deck.`);
  }
}

function updatePaginationControls(start, end, total) {
  const summaryEl = document.getElementById("pagination-summary");
  const btnPrev = document.getElementById("btn-prev-page");
  const btnNext = document.getElementById("btn-next-page");
  const pageContainer = document.getElementById("page-numbers-container");

  if (summaryEl) {
    summaryEl.innerText = total > 0 ? `Showing ${start} to ${end} of ${total} sectors` : "0 sectors found";
  }

  const totalPages = Math.ceil(total / pageSize) || 1;
  if (btnPrev) btnPrev.disabled = currentPage <= 1;
  if (btnNext) btnNext.disabled = currentPage >= totalPages;

  if (pageContainer) {
    pageContainer.innerHTML = "";
    const maxButtons = 5;
    let startPage = Math.max(1, currentPage - 2);
    let endPage = Math.min(totalPages, startPage + maxButtons - 1);

    if (endPage - startPage < maxButtons - 1) {
      startPage = Math.max(1, endPage - maxButtons + 1);
    }

    for (let p = startPage; p <= endPage; p++) {
      const pBtn = document.createElement("button");
      pBtn.className = `px-2.5 py-1 text-xs rounded border font-mono ${p === currentPage ? 'bg-cyan-500 border-cyan-400 text-slate-950 font-bold' : 'bg-slate-900 border-slate-800 text-slate-300 hover:border-slate-700'}`;
      pBtn.innerText = p;
      pBtn.onclick = () => { currentPage = p; renderTablePage(); };
      pageContainer.appendChild(pBtn);
    }
  }
}

function changePage(delta) {
  currentPage += delta;
  renderTablePage();
}

function changePageSize(newSize) {
  pageSize = parseInt(newSize);
  currentPage = 1;
  renderTablePage();
}

// 8. ML Diagnostic Plot Tabs
function switchPlotTab(tabId, btn) {
  document.querySelectorAll(".plot-tab-pill").forEach(b => {
    b.className = "plot-tab-pill px-3 py-1.5 rounded-lg font-semibold bg-slate-900 border border-slate-800 text-slate-400 hover:text-white transition-all";
  });
  document.querySelectorAll(".plot-tab-content").forEach(c => c.classList.add("hidden"));

  if (btn) {
    btn.className = "plot-tab-pill px-3 py-1.5 rounded-lg font-semibold bg-cyan-500/15 border border-cyan-500/40 text-cyan-300 transition-all active";
  }
  const target = document.getElementById(tabId);
  if (target) {
    target.classList.remove("hidden");
  }
}

// 9. Lightbox Modal
function openLightbox(imgSrc) {
  const modal = document.getElementById("lightbox-modal");
  const modalImg = document.getElementById("lightbox-img");
  if (modal && modalImg) {
    modalImg.src = imgSrc;
    modal.classList.remove("hidden");
    modal.classList.add("flex");
  }
  if (window.lucide) lucide.createIcons();
}

function closeLightbox() {
  const modal = document.getElementById("lightbox-modal");
  if (modal) {
    modal.classList.remove("flex");
    modal.classList.add("hidden");
  }
}

// 10. Helpline 1930 Incident Burst Simulator
function setupSimulator() {
  const sliderN = document.getElementById("sim-n");
  const sliderLoss = document.getElementById("sim-loss");
  const lblN = document.getElementById("lbl-sim-n");
  const lblLoss = document.getElementById("lbl-sim-loss");
  const btnRun = document.getElementById("btn-run-sim");

  if (!sliderN || !btnRun) return;

  sliderN.addEventListener("input", (e) => {
    if (lblN) lblN.innerText = `${e.target.value} Reports`;
  });

  sliderLoss.addEventListener("input", (e) => {
    if (lblLoss) lblLoss.innerText = `₹${Number(e.target.value).toLocaleString()}`;
  });

  btnRun.addEventListener("click", () => {
    const n = parseInt(sliderN.value);
    const category = document.getElementById("sim-category").value;
    const loss = parseInt(sliderLoss.value);

    // Compute dynamic telemetry
    const totalLoss = n * loss * (0.85 + Math.random() * 0.3);
    const meanDelayHours = (10.5 + Math.random() * 4.5).toFixed(1);

    const candidates = ["CELL_03_15", "CELL_04_15", "CELL_13_11", "CELL_01_15", "CELL_05_16"];
    const targetHub = candidates[Math.floor(Math.random() * candidates.length)];

    const now = new Date();
    const estArrival = new Date(now.getTime() + meanDelayHours * 3600 * 1000);
    const arrivalStr = estArrival.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

    const titleEl = document.getElementById("sim-alert-title");
    const descEl = document.getElementById("sim-alert-desc");
    if (titleEl) titleEl.innerText = `🚨 ACTIVE INTERDICTION ALERT: ${n} COMPLAINTS INGESTED`;
    if (descEl) {
      descEl.innerHTML = `
        Estimated cash-out convergence window: <strong>+${meanDelayHours} Hours</strong> (Opening around <strong>${arrivalStr} IST</strong>).<br>
        High-risk convergence corridor identified: <strong class="text-rose-400">${targetHub}</strong>. Plainclothes interdiction dispatched.
      `;
    }

    document.getElementById("sm-loss").innerText = `₹${Math.round(totalLoss).toLocaleString()}`;
    document.getElementById("sm-window").innerText = `+${meanDelayHours}h (${arrivalStr})`;
    document.getElementById("sm-hub").innerText = targetHub;

    // Stream Telemetry Terminal
    const feed = document.getElementById("telemetry-feed");
    if (feed) {
      feed.innerHTML = "";
      for (let i = 0; i < n; i++) {
        const item = document.createElement("div");
        item.className = "flex justify-between py-1 border-b border-slate-900 text-[11px]";
        const indLoss = Math.round(loss * (0.7 + Math.random() * 0.6));
        const indDelay = (8 + Math.random() * 7).toFixed(1);
        const indCell = candidates[Math.floor(Math.random() * candidates.length)];
        const compId = `NCRP-1930-${104820 + i}`;

        item.innerHTML = `
          <span><strong class="text-cyan-400">${compId}</strong> | ${category}</span>
          <span>Loss: ₹${indLoss.toLocaleString()} | Window: +${indDelay}h -> <span class="text-rose-400 font-bold">${indCell}</span></span>
        `;
        feed.appendChild(item);
      }
    }

    showToast(`Simulation processed: ${n} complaints projected to converge on ${targetHub}`);
  });
}

// 11. Live Forecast Fetcher from Edge JSON
async function tryFetchLiveForecasts() {
  try {
    const res = await fetch("/api/v1/forecasts");
    if (res.ok) {
      const data = await res.json();
      if (data && data.results && data.results.length > 0) {
        activeForecasts = data.results.map(r => {
          const lat = r.coordinates ? r.coordinates.latitude : 28.535;
          const lon = r.coordinates ? r.coordinates.longitude : 77.255;
          const bbox = r.bounding_box || {};
          const cBounds = r.conformal_bounds_90 || {};
          const ciList = r.conformal_90_ci || [0, 5];
          const drivers = Array.isArray(r.primary_drivers)
            ? r.primary_drivers.join(" | ")
            : (r.top_xai_drivers || "Historical Recency Momentum");
          const sop = (r.tactical_directives && r.tactical_directives.length > 0)
            ? r.tactical_directives[0]
            : "Deploy plainclothes unit for active corridor interdiction.";

          return {
            priority_rank: r.priority_rank,
            grid_cell_id: r.grid_cell_id,
            centroid_lat: lat,
            centroid_lon: lon,
            lat_min: bbox.latitude_min !== undefined ? bbox.latitude_min : lat - 0.005,
            lat_max: bbox.latitude_max !== undefined ? bbox.latitude_max : lat + 0.005,
            lon_min: bbox.longitude_min !== undefined ? bbox.longitude_min : lon - 0.005,
            lon_max: bbox.longitude_max !== undefined ? bbox.longitude_max : lon + 0.005,
            pred_hotspot_prob: r.hotspot_probability !== undefined ? r.hotspot_probability : 0.85,
            expected_withdrawals: r.expected_withdrawals_24h !== undefined ? r.expected_withdrawals_24h : (r.expected_withdrawals || 2.5),
            count_ci_lower: cBounds.lower !== undefined ? cBounds.lower : ciList[0],
            count_ci_upper: cBounds.upper !== undefined ? cBounds.upper : ciList[1],
            cell_atm_count: r.cell_atm_count || 10,
            transit_score: r.transit_score || 0.768,
            risk_tier: r.risk_tier || "CRITICAL",
            top_contributing_factors: drivers,
            sop: sop
          };
        });

        updateFilterCounts();
        applyFiltersAndSort();
        renderMapLayers();
        inspectCell(activeForecasts[0]);
        console.log("CYBERWATCH: Ingested complete 400-quadrant operational forecast surface.");
      }
    }
  } catch (e) {
    console.log("CYBERWATCH: Running on offline telemetry cache.");
    inspectCell(activeForecasts[0]);
  }
}

// 12. Floating Toast Messenger
function showToast(message) {
  const container = document.getElementById("toast-container");
  if (!container) return;

  const toast = document.createElement("div");
  toast.className = "flex items-center gap-2.5 px-4 py-2.5 rounded-xl bg-slate-900/95 border border-cyan-500/50 text-white text-xs font-semibold shadow-2xl backdrop-blur-md pointer-events-auto transition-all duration-300";
  toast.innerHTML = `
    <i data-lucide="check-circle-2" class="w-4 h-4 text-cyan-400"></i>
    <span>${message}</span>
  `;

  container.appendChild(toast);
  if (window.lucide) lucide.createIcons();
  setTimeout(() => {
    toast.style.opacity = "0";
    toast.style.transform = "translateY(8px)";
    setTimeout(() => toast.remove(), 300);
  }, 3200);
}
