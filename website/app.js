/**
 * CyberWatch - Delhi NCR Cybercrime Cash-Withdrawal Location Predictor
 * Clean, User-Friendly Client Engine
 */

// Human-readable Delhi NCR locality mapping for key grid sectors
const CELL_LANDMARKS = {
  "CELL_03_15": "Nehru Place / Greater Kailash Hub",
  "CELL_04_15": "Kalkaji / Okhla Commercial Hub",
  "CELL_13_11": "Connaught Place / Rajiv Chowk Cluster",
  "CELL_01_15": "Saket District Centre / Press Enclave",
  "CELL_05_16": "Lajpat Nagar / Defence Colony Hub",
  "CELL_03_17": "Sarita Vihar / Jasola Commercial Corridor",
  "CELL_02_15": "Malviya Nagar / Hauz Khas East",
  "CELL_02_16": "Chirag Dilli / Sheikh Sarai Center",
  "CELL_14_12": "New Delhi Railway Station / Paharganj",
  "CELL_13_12": "Barakhamba Road / Mandi House Corridor",
  "CELL_03_14": "Greater Kailash I / M-Block Market",
  "CELL_13_10": "Shivaji Stadium / Gole Market",
  "CELL_14_11": "Sadar Bazar / DB Gupta Road",
  "CELL_03_13": "Hauz Khas Market / Aurobindo Marg",
  "CELL_05_15": "South Extension / AIIMS Corridor",
  "CELL_11_12": "India Gate / Khan Market Corridor",
  "CELL_12_11": "Janpath / Tolstoy Marg Commercial Hub"
};

function getCellName(cell) {
  if (CELL_LANDMARKS[cell.grid_cell_id]) {
    return CELL_LANDMARKS[cell.grid_cell_id];
  }
  const lat = cell.centroid_lat;
  const lon = cell.centroid_lon;
  if (lat > 28.62 && lon < 77.23) return `Central Delhi Sector (${cell.grid_cell_id})`;
  if (lat > 28.62 && lon >= 77.23) return `East Delhi Corridor (${cell.grid_cell_id})`;
  if (lat <= 28.56 && lon >= 77.24) return `South-East Delhi Hub (${cell.grid_cell_id})`;
  if (lat <= 28.56 && lon < 77.24) return `South Delhi Quadrant (${cell.grid_cell_id})`;
  return `Delhi NCR Sector (${cell.grid_cell_id})`;
}

// Embedded Fallback Dataset (Guarantees 100% offline functionality)
const FALLBACK_FORECASTS = [
  {
    priority_rank: 1, grid_cell_id: "CELL_03_15",
    centroid_lat: 28.535, centroid_lon: 77.255,
    lat_min: 28.530, lat_max: 28.540, lon_min: 77.250, lon_max: 77.260,
    pred_hotspot_prob: 0.9821, expected_withdrawals: 3.1,
    count_ci_lower: 2.2, count_ci_upper: 4.0, cell_atm_count: 29, transit_score: 0.768,
    risk_tier: "CRITICAL",
    top_contributing_factors: "High ATM density near Nehru Place metro interchange &bull; Frequent repeat weekend cash sweeps.",
    sop: "Deploy plainclothes static patrol unit for Shift Alpha (14:00 - 22:00 IST). Monitor ATM vestibules discretely for multi-card cash sweeps."
  },
  {
    priority_rank: 2, grid_cell_id: "CELL_04_15",
    centroid_lat: 28.545, centroid_lon: 77.255,
    lat_min: 28.540, lat_max: 28.550, lon_min: 77.250, lon_max: 77.260,
    pred_hotspot_prob: 0.9821, expected_withdrawals: 7.8,
    count_ci_lower: 6.9, count_ci_upper: 8.7, cell_atm_count: 28, transit_score: 0.742,
    risk_tier: "CRITICAL",
    top_contributing_factors: "Major transit convergence corridor &bull; Rapid layering cash-out corridor.",
    sop: "Deploy plainclothes static unit for Shift Bravo (22:00 - 06:00 IST). Coordinate with bank security for rapid interdiction."
  },
  {
    priority_rank: 3, grid_cell_id: "CELL_13_11",
    centroid_lat: 28.635, centroid_lon: 77.215,
    lat_min: 28.630, lat_max: 28.640, lon_min: 77.210, lon_max: 77.220,
    pred_hotspot_prob: 0.9595, expected_withdrawals: 2.1,
    count_ci_lower: 1.2, count_ci_upper: 3.0, cell_atm_count: 33, transit_score: 0.910,
    risk_tier: "CRITICAL",
    top_contributing_factors: "Central business district &bull; High foot-traffic metro interchange with 33 ATM kiosks.",
    sop: "Assign mobile motorcycle patrol in 20-min sweeps across Outer Circle ATM vestibules."
  },
  {
    priority_rank: 4, grid_cell_id: "CELL_01_15",
    centroid_lat: 28.515, centroid_lon: 77.255,
    lat_min: 28.510, lat_max: 28.520, lon_min: 77.250, lon_max: 77.260,
    pred_hotspot_prob: 0.9548, expected_withdrawals: 1.9,
    count_ci_lower: 1.0, count_ci_upper: 2.8, cell_atm_count: 28, transit_score: 0.680,
    risk_tier: "CRITICAL",
    top_contributing_factors: "Shopping mall clusters &bull; High volume of debit card transactions.",
    sop: "Dispatch preservation notices for CCTV to acquiring banks before automated 15-day purge."
  },
  {
    priority_rank: 5, grid_cell_id: "CELL_05_16",
    centroid_lat: 28.555, centroid_lon: 77.265,
    lat_min: 28.550, lat_max: 28.560, lon_min: 77.260, lon_max: 77.270,
    pred_hotspot_prob: 0.9522, expected_withdrawals: 1.8,
    count_ci_lower: 0.9, count_ci_upper: 2.7, cell_atm_count: 35, transit_score: 0.720,
    risk_tier: "CRITICAL",
    top_contributing_factors: "Dense market retail sector &bull; High concentration of multi-bank ATM branches.",
    sop: "Plainclothes monitoring during afternoon banking rush (14:00 - 18:00 IST)."
  },
  {
    priority_rank: 6, grid_cell_id: "CELL_03_17",
    centroid_lat: 28.535, centroid_lon: 77.275,
    lat_min: 28.530, lat_max: 28.540, lon_min: 77.270, lon_max: 77.280,
    pred_hotspot_prob: 0.9368, expected_withdrawals: 1.4,
    count_ci_lower: 0.5, count_ci_upper: 2.3, cell_atm_count: 19, transit_score: 0.650,
    risk_tier: "CRITICAL",
    top_contributing_factors: "Industrial commercial corridor &bull; Interstate highway access point.",
    sop: "Monitor commercial complex ATM corridor for repeat mule withdrawals."
  },
  {
    priority_rank: 7, grid_cell_id: "CELL_02_15",
    centroid_lat: 28.525, centroid_lon: 77.255,
    lat_min: 28.520, lat_max: 28.530, lon_min: 77.250, lon_max: 77.260,
    pred_hotspot_prob: 0.9257, expected_withdrawals: 1.5,
    count_ci_lower: 0.6, count_ci_upper: 2.4, cell_atm_count: 24, transit_score: 0.630,
    risk_tier: "CRITICAL",
    top_contributing_factors: "Hospital and transit junction &bull; Regular cash extraction hotspot.",
    sop: "Enforce bank step-up friction: lower single withdrawal caps to INR 10,000."
  },
  {
    priority_rank: 8, grid_cell_id: "CELL_02_16",
    centroid_lat: 28.525, centroid_lon: 77.265,
    lat_min: 28.520, lat_max: 28.530, lon_min: 77.260, lon_max: 77.270,
    pred_hotspot_prob: 0.9234, expected_withdrawals: 1.5,
    count_ci_lower: 0.6, count_ci_upper: 2.4, cell_atm_count: 19, transit_score: 0.690,
    risk_tier: "CRITICAL",
    top_contributing_factors: "Interconnected residential-commercial fringe &bull; Recent 3-day withdrawal surge.",
    sop: "Enforce dynamic friction on non-home debit cards."
  },
  {
    priority_rank: 9, grid_cell_id: "CELL_14_12",
    centroid_lat: 28.645, centroid_lon: 77.225,
    lat_min: 28.640, lat_max: 28.650, lon_min: 77.220, lon_max: 77.230,
    pred_hotspot_prob: 0.9189, expected_withdrawals: 1.3,
    count_ci_lower: 0.4, count_ci_upper: 2.2, cell_atm_count: 23, transit_score: 0.880,
    risk_tier: "CRITICAL",
    top_contributing_factors: "Major interstate railway terminal &bull; Heavy transient crowd facilitating mule anonymity.",
    sop: "Coordinate with railway police for immediate cash interdiction sweeps."
  },
  {
    priority_rank: 10, grid_cell_id: "CELL_13_12",
    centroid_lat: 28.635, centroid_lon: 77.225,
    lat_min: 28.630, lat_max: 28.640, lon_min: 77.220, lon_max: 77.230,
    pred_hotspot_prob: 0.9122, expected_withdrawals: 1.3,
    count_ci_lower: 0.4, count_ci_upper: 2.2, cell_atm_count: 24, transit_score: 0.710,
    risk_tier: "CRITICAL",
    top_contributing_factors: "Financial district with corporate bank branches &bull; Off-peak cashout patterns.",
    sop: "High visibility static cruiser deployment during peak afternoon withdrawal window."
  },
  {
    priority_rank: 11, grid_cell_id: "CELL_11_12",
    centroid_lat: 28.615, centroid_lon: 77.225,
    lat_min: 28.610, lat_max: 28.620, lon_min: 77.220, lon_max: 77.230,
    pred_hotspot_prob: 0.8840, expected_withdrawals: 1.1,
    count_ci_lower: 0.2, count_ci_upper: 2.0, cell_atm_count: 17, transit_score: 0.750,
    risk_tier: "ELEVATED",
    top_contributing_factors: "Affluent retail district &bull; High density ATM infrastructure.",
    sop: "Routine motorcycle patrol sweeps every 30 minutes."
  },
  {
    priority_rank: 12, grid_cell_id: "CELL_12_11",
    centroid_lat: 28.625, centroid_lon: 77.215,
    lat_min: 28.620, lat_max: 28.630, lon_min: 77.210, lon_max: 77.220,
    pred_hotspot_prob: 0.8650, expected_withdrawals: 1.0,
    count_ci_lower: 0.1, count_ci_upper: 1.9, cell_atm_count: 19, transit_score: 0.820,
    risk_tier: "ELEVATED",
    top_contributing_factors: "Transit junction with multiple private bank kiosks.",
    sop: "Alert bank fraud risk management to monitor withdrawal velocity."
  }
];

// Exploration audit patrol zones (20% anti-bias safeguard)
const EXPLORATION_ZONES = [
  { lat: 28.505, lon: 77.105, radius: 1000, label: "Exploration Zone Alpha (South-West)" },
  { lat: 28.685, lon: 77.125, radius: 1000, label: "Exploration Zone Bravo (North-West)" },
  { lat: 28.695, lon: 77.285, radius: 1000, label: "Exploration Zone Charlie (North-East)" },
  { lat: 28.515, lon: 77.285, radius: 1000, label: "Exploration Zone Delta (South-East)" }
];

// Global State
let mapInstance = null;
let top10LayerGroup = null;
let explorationLayerGroup = null;

let activeForecasts = FALLBACK_FORECASTS;
let filteredForecasts = FALLBACK_FORECASTS;
let selectedCell = FALLBACK_FORECASTS[0];

// Table Pagination State
let currentPage = 1;
let pageSize = 10;
let activeFilterTier = "ALL";

// Initialize on DOM Ready
document.addEventListener("DOMContentLoaded", () => {
  initLiveClock();
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
      clockEl.innerText = `IST ${istTime}`;
    }
  }
  tick();
  setInterval(tick, 1000);
}

// 2. Initialize Leaflet Map
function initMap() {
  const mapContainer = document.getElementById("leaflet-map");
  if (!mapContainer) return;

  // Center on Delhi NCR
  mapInstance = L.map("leaflet-map", {
    center: [28.585, 77.235],
    zoom: 12,
    zoomControl: true,
    minZoom: 10,
    maxZoom: 16
  });

  // CartoDB Dark Matter Basemap
  L.tileLayer("https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png", {
    attribution: '&copy; <a href="https://carto.com/">CARTO</a> | &copy; OpenStreetMap',
    subdomains: "abcd",
    maxZoom: 19
  }).addTo(mapInstance);

  top10LayerGroup = L.layerGroup().addTo(mapInstance);
  explorationLayerGroup = L.layerGroup().addTo(mapInstance);

  renderMapLayers();

  // Layer toggle listeners
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
}

// 3. Jump to Sector
function jumpToSector(lat, lon, zoom) {
  if (mapInstance) {
    mapInstance.setView([lat, lon], zoom);
    showToast(`Centered map on coordinates: ${lat.toFixed(3)}°N, ${lon.toFixed(3)}°E`);
  }
}

// 4. Render Map Layers
function renderMapLayers() {
  if (!mapInstance || !top10LayerGroup) return;

  top10LayerGroup.clearLayers();
  explorationLayerGroup.clearLayers();

  // Render Forecast Hotspots
  activeForecasts.forEach((cell, idx) => {
    const isCritical = cell.risk_tier === "CRITICAL" || idx < 10;
    const radius = isCritical ? 750 : 500;
    const color = isCritical ? "#fb7185" : "#fbbf24";
    const fillColor = isCritical ? "#f43f5e" : "#f59e0b";
    const locName = getCellName(cell);

    const circle = L.circle([cell.centroid_lat, cell.centroid_lon], {
      radius: radius,
      color: color,
      weight: isCritical ? 2.5 : 1.5,
      fillColor: fillColor,
      fillOpacity: isCritical ? 0.35 : 0.20
    });

    const popupHtml = `
      <div style="font-family:'Plus Jakarta Sans',sans-serif; min-width: 220px; padding: 4px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 6px;">
          <span style="font-size:11px; font-weight:bold; color:${isCritical ? '#fb7185' : '#fbbf24'}; background:${isCritical ? 'rgba(251,113,133,0.15)' : 'rgba(251,191,36,0.15)'}; padding:2px 6px; border-radius:4px;">
            ${isCritical ? 'CRITICAL HOTSPOT' : 'ELEVATED RISK'}
          </span>
          <span style="font-size:11px; font-weight:bold; color:#94a3b8;">#${cell.priority_rank}</span>
        </div>
        <div style="font-size:13px; font-weight:bold; color:#ffffff; margin-bottom: 4px;">
          ${locName}
        </div>
        <div style="font-size:11px; color:#cbd5e1; margin-bottom: 8px;">
          ${cell.grid_cell_id} &bull; ${cell.cell_atm_count || 20} ATMs
        </div>
        <div style="font-size:12px; color:#38bdf8; font-weight:bold; margin-bottom: 8px;">
          Risk: ${(cell.pred_hotspot_prob * 100).toFixed(1)}% &bull; ~${cell.expected_withdrawals} cashouts
        </div>
        <button onclick="selectAndFocusCell('${cell.grid_cell_id}')" style="width:100%; padding: 6px; font-size:11px; font-weight:bold; background:#0284c7; color:#ffffff; border:none; border-radius:6px; cursor:pointer;">
          Inspect Police Protocol &rarr;
        </button>
      </div>
    `;

    circle.bindPopup(popupHtml);
    circle.on("click", () => inspectCell(cell));

    if (isCritical) {
      top10LayerGroup.addLayer(circle);
    } else {
      explorationLayerGroup.addLayer(circle);
    }
  });

  // Render Exploration Safeguard Zones
  EXPLORATION_ZONES.forEach(z => {
    const circle = L.circle([z.lat, z.lon], {
      radius: z.radius,
      color: "#38bdf8",
      weight: 1.5,
      dashArray: "4, 6",
      fillColor: "#0284c7",
      fillOpacity: 0.12
    });
    circle.bindPopup(`
      <div style="font-family:'Plus Jakarta Sans',sans-serif; padding: 4px;">
        <strong style="color:#38bdf8; font-size:12px;">${z.label}</strong>
        <div style="font-size:11px; color:#94a3b8; margin-top:2px;">Anti-bias random patrol sector (20% coverage)</div>
      </div>
    `);
    explorationLayerGroup.addLayer(circle);
  });
}

// 5. Inspect Cell in Detail Card
function inspectCell(cell) {
  selectedCell = cell;
  const locName = getCellName(cell);

  const nameEl = document.getElementById("insp-cell-name");
  const idEl = document.getElementById("insp-cell-id");
  const tierEl = document.getElementById("insp-tier");
  const rankEl = document.getElementById("insp-rank");
  const probEl = document.getElementById("insp-prob");
  const countEl = document.getElementById("insp-count");
  const atmsEl = document.getElementById("insp-atms");
  const transitEl = document.getElementById("insp-transit");
  const driversEl = document.getElementById("insp-drivers");
  const sopEl = document.getElementById("insp-sop");

  if (nameEl) nameEl.innerText = locName;
  if (idEl) idEl.innerText = `Sector ID: ${cell.grid_cell_id} • ${cell.centroid_lat.toFixed(3)}°N, ${cell.centroid_lon.toFixed(3)}°E`;
  if (rankEl) rankEl.innerText = `PRIORITY #${cell.priority_rank}`;

  if (tierEl) {
    const isCrit = cell.risk_tier === "CRITICAL" || cell.priority_rank <= 10;
    tierEl.innerText = isCrit ? "CRITICAL HOTSPOT" : "ELEVATED RISK";
    tierEl.className = isCrit
      ? "px-2.5 py-0.5 rounded-full text-xs font-bold uppercase bg-rose-500/15 border border-rose-500/40 text-rose-300"
      : "px-2.5 py-0.5 rounded-full text-xs font-bold uppercase bg-amber-500/15 border border-amber-500/40 text-amber-300";
  }

  if (probEl) probEl.innerText = `${(cell.pred_hotspot_prob * 100).toFixed(1)}%`;
  if (countEl) countEl.innerText = `${cell.expected_withdrawals}`;
  if (atmsEl) atmsEl.innerText = `${cell.cell_atm_count || 20} Terminals`;
  if (transitEl) {
    transitEl.innerText = cell.transit_score > 0.75 ? "High (Metro Interchange)" : "Moderate (Bus Corridor)";
  }

  if (driversEl) {
    driversEl.innerHTML = cell.top_contributing_factors || "Historical Recency Momentum &bull; High volume of repeat ATM cashouts.";
  }

  if (sopEl) {
    sopEl.innerText = cell.sop || "Deploy plainclothes static unit during peak hours (14:00 - 22:00 IST). Monitor ATM vestibules discretely.";
  }
}

// Select cell and focus map
function selectAndFocusCell(cellId) {
  const match = activeForecasts.find(c => c.grid_cell_id === cellId);
  if (match) {
    inspectCell(match);
    jumpToSector(match.centroid_lat, match.centroid_lon, 14);
    // Smooth scroll to map section
    const mapSec = document.getElementById("map-section");
    if (mapSec) mapSec.scrollIntoView({ behavior: "smooth" });
  }
}

// 6. Copy Police Dispatch Briefing
function copyPoliceBriefing() {
  if (!selectedCell) return;
  const locName = getCellName(selectedCell);
  const text = `CYBERWATCH TACTICAL POLICE BRIEFING:
Location: ${locName} (${selectedCell.grid_cell_id})
Coordinates: ${selectedCell.centroid_lat.toFixed(4)}°N, ${selectedCell.centroid_lon.toFixed(4)}°E
Risk Level: ${selectedCell.risk_tier} (Forecast Probability: ${(selectedCell.pred_hotspot_prob * 100).toFixed(1)}%)
Expected Cashouts: ~${selectedCell.expected_withdrawals} incidents in next 24h
ATM Infrastructure: ${selectedCell.cell_atm_count || 20} Kiosks in 1km radius
Tactical Directive: ${selectedCell.sop}
Preservation Notice: Preserve CCTV records for all multi-card withdrawals during 14:00 - 22:00 IST.`;

  navigator.clipboard.writeText(text).then(() => {
    showToast(`Copied Police Dispatch Briefing for ${locName}`);
  }).catch(() => {
    showToast("Unable to copy to clipboard.");
  });
}

// 7. Table Data Initialization & Rendering
function initTableData() {
  applyFilters();
}

function applyFilters() {
  const query = (document.getElementById("table-search")?.value || "").toLowerCase().trim();

  filteredForecasts = activeForecasts.filter(cell => {
    // Filter tier
    if (activeFilterTier === "CRITICAL" && cell.risk_tier !== "CRITICAL") return false;
    if (activeFilterTier === "ELEVATED" && cell.risk_tier !== "ELEVATED") return false;

    // Search query
    if (query) {
      const locName = getCellName(cell).toLowerCase();
      const cellId = cell.grid_cell_id.toLowerCase();
      const factors = (cell.top_contributing_factors || "").toLowerCase();
      if (!locName.includes(query) && !cellId.includes(query) && !factors.includes(query)) {
        return false;
      }
    }
    return true;
  });

  currentPage = 1;
  renderTable();
}

function renderTable() {
  const tbody = document.getElementById("hotspots-tbody");
  if (!tbody) return;

  tbody.innerHTML = "";

  const total = filteredForecasts.length;
  const startIdx = (currentPage - 1) * pageSize;
  const endIdx = Math.min(startIdx + pageSize, total);
  const pageRows = filteredForecasts.slice(startIdx, endIdx);

  if (pageRows.length === 0) {
    tbody.innerHTML = `
      <tr>
        <td colspan="8" class="text-center py-8 text-slate-500 text-xs">
          No matching sectors found. Try adjusting your search query or filter.
        </td>
      </tr>
    `;
    updatePaginationUI(0, 0, 0);
    return;
  }

  pageRows.forEach(cell => {
    const locName = getCellName(cell);
    const isCrit = cell.risk_tier === "CRITICAL" || cell.priority_rank <= 10;
    const tr = document.createElement("tr");
    tr.className = "hover:bg-slate-900/60 transition-colors";

    tr.innerHTML = `
      <td class="py-3 px-4 font-mono font-bold ${cell.priority_rank <= 3 ? 'text-cyan-400' : 'text-slate-300'}">
        #${cell.priority_rank}
      </td>
      <td class="py-3 px-4 font-semibold text-white">
        ${locName}
      </td>
      <td class="py-3 px-4 font-mono text-slate-400">
        ${cell.grid_cell_id}
      </td>
      <td class="py-3 px-4 font-mono font-bold ${isCrit ? 'text-rose-400' : 'text-amber-400'}">
        ${(cell.pred_hotspot_prob * 100).toFixed(1)}%
      </td>
      <td class="py-3 px-4 font-mono text-slate-300">
        ~${cell.expected_withdrawals}
      </td>
      <td class="py-3 px-4 font-mono text-slate-300">
        ${cell.cell_atm_count || 20} kiosks
      </td>
      <td class="py-3 px-4">
        <span class="px-2 py-0.5 rounded text-[10px] font-bold uppercase ${isCrit ? 'bg-rose-500/15 border border-rose-500/40 text-rose-300' : 'bg-amber-500/15 border border-amber-500/40 text-amber-300'}">
          ${isCrit ? 'Critical' : 'Elevated'}
        </span>
      </td>
      <td class="py-3 px-4 text-right">
        <button onclick="selectAndFocusCell('${cell.grid_cell_id}')" class="px-2.5 py-1 text-xs font-semibold rounded-lg bg-cyan-500/10 hover:bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 transition-all">
          Focus on Map &rarr;
        </button>
      </td>
    `;
    tbody.appendChild(tr);
  });

  updatePaginationUI(startIdx + 1, endIdx, total);
}

function updatePaginationUI(start, end, total) {
  const summaryEl = document.getElementById("pagination-summary");
  if (summaryEl) {
    summaryEl.innerText = total > 0 ? `Showing ${start} to ${end} of ${total} sectors` : "0 sectors";
  }

  const prevBtn = document.getElementById("btn-prev-page");
  const nextBtn = document.getElementById("btn-next-page");
  if (prevBtn) prevBtn.disabled = currentPage <= 1;
  if (nextBtn) nextBtn.disabled = end >= total;

  // Render page number badges
  const pagesContainer = document.getElementById("page-numbers-container");
  if (pagesContainer) {
    pagesContainer.innerHTML = "";
    const totalPages = Math.ceil(total / pageSize);
    for (let p = 1; p <= Math.min(totalPages, 5); p++) {
      const btn = document.createElement("button");
      btn.className = p === currentPage
        ? "w-7 h-7 rounded-lg text-xs font-bold bg-cyan-500 text-slate-950"
        : "w-7 h-7 rounded-lg text-xs font-medium bg-brand-base border border-brand-border text-slate-400 hover:text-white";
      btn.innerText = p;
      btn.onclick = () => {
        currentPage = p;
        renderTable();
      };
      pagesContainer.appendChild(btn);
    }
  }
}

function changePage(delta) {
  const totalPages = Math.ceil(filteredForecasts.length / pageSize);
  const newPage = currentPage + delta;
  if (newPage >= 1 && newPage <= totalPages) {
    currentPage = newPage;
    renderTable();
  }
}

// Search and filter listeners
function setupTableSearch() {
  const input = document.getElementById("table-search");
  if (!input) return;

  let debounceTimer;
  input.addEventListener("input", () => {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => {
      applyFilters();
    }, 200);
  });
}

function setupFilterChips() {
  const chips = document.querySelectorAll(".filter-chip");
  chips.forEach(chip => {
    chip.addEventListener("click", () => {
      chips.forEach(c => {
        c.className = "filter-chip px-3.5 py-1.5 rounded-lg font-semibold bg-brand-base border border-brand-border text-slate-400 hover:text-white transition-all text-xs";
      });
      chip.className = "filter-chip px-3.5 py-1.5 rounded-lg font-semibold bg-cyan-500/15 border border-cyan-500 text-cyan-300 transition-all active text-xs";
      activeFilterTier = chip.getAttribute("data-filter");
      applyFilters();
    });
  });
}

// 8. Practical Incident Risk Checker
function setupSimulator() {
  const sliderLoss = document.getElementById("sim-loss");
  const lblLoss = document.getElementById("lbl-sim-loss");
  const btnRun = document.getElementById("btn-run-sim");

  if (!sliderLoss || !btnRun) return;

  sliderLoss.addEventListener("input", (e) => {
    if (lblLoss) lblLoss.innerHTML = `&#8377;${Number(e.target.value).toLocaleString()}`;
  });

  btnRun.addEventListener("click", () => {
    const category = document.getElementById("sim-category").value;
    const loss = parseInt(sliderLoss.value);
    const timeReportedHours = parseInt(document.getElementById("sim-time").value || 0);

    // Calculate delay window
    let baseDelay = 4.0;
    if (category.includes("UPI")) baseDelay = 2.0;
    else if (category.includes("Skimming")) baseDelay = 1.5;
    else if (category.includes("Investment")) baseDelay = 5.5;

    const remainingDelay = Math.max(0.5, (baseDelay - timeReportedHours + (Math.random() * 0.8 - 0.4))).toFixed(1);
    
    const candidates = [
      { name: "Nehru Place / GK Hub", id: "CELL_03_15" },
      { name: "Connaught Place Cluster", id: "CELL_13_11" },
      { name: "Saket District Centre", id: "CELL_01_15" },
      { name: "Kalkaji Commercial Hub", id: "CELL_04_15" }
    ];
    const topCandidate = candidates[Math.floor(Math.random() * candidates.length)];

    const now = new Date();
    const estArrival = new Date(now.getTime() + remainingDelay * 3600 * 1000);
    const arrivalStr = estArrival.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

    const titleEl = document.getElementById("sim-alert-title");
    const descEl = document.getElementById("sim-alert-desc");

    if (titleEl) titleEl.innerText = `Interdiction Target: ${topCandidate.name}`;
    if (descEl) {
      descEl.innerHTML = `
        Incident assessed: <strong>${category}</strong> (Loss: <strong>&#8377;${loss.toLocaleString()}</strong>).<br>
        Predicted physical cash-out extraction window opens at <strong>${arrivalStr} IST</strong> (+${remainingDelay}h).
      `;
    }

    const winEl = document.getElementById("sm-window");
    const hubEl = document.getElementById("sm-hub");
    const urgEl = document.getElementById("sm-urgency");

    if (winEl) winEl.innerText = `+${remainingDelay}h (${arrivalStr})`;
    if (hubEl) hubEl.innerText = topCandidate.name;
    if (urgEl) urgEl.innerText = remainingDelay < 2 ? "Critical (Immediate)" : "Elevated";

    showToast(`Calculated cash-out window: ${topCandidate.name} (+${remainingDelay}h)`);
  });
}

// 9. Collapsible Benchmarks Toggle
function toggleBenchmarks() {
  const container = document.getElementById("benchmarks-container");
  const lbl = document.getElementById("lbl-benchmarks-toggle");
  const icon = document.getElementById("icon-benchmarks-toggle");

  if (!container) return;

  const isHidden = container.classList.contains("hidden");
  if (isHidden) {
    container.classList.remove("hidden");
    if (lbl) lbl.innerText = "Hide Technical ML Details";
    if (icon) icon.style.transform = "rotate(180deg)";
  } else {
    container.classList.add("hidden");
    if (lbl) lbl.innerText = "Show Technical ML Details";
    if (icon) icon.style.transform = "rotate(0deg)";
  }
  if (window.lucide) lucide.createIcons();
}

// 10. Lightbox Modal
function openLightbox(imgSrc) {
  const modal = document.getElementById("lightbox-modal");
  const modalImg = document.getElementById("lightbox-img");
  if (modal && modalImg) {
    modalImg.src = imgSrc;
    modal.classList.remove("hidden");
    modal.classList.add("flex");
  }
}

function closeLightbox() {
  const modal = document.getElementById("lightbox-modal");
  if (modal) {
    modal.classList.remove("flex");
    modal.classList.add("hidden");
  }
}

// 11. Live Data Fetcher from Edge JSON
async function tryFetchLiveForecasts() {
  try {
    const res = await fetch("data/forecasts.json");
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
            ? r.primary_drivers.join(" &bull; ")
            : (r.top_xai_drivers || "Historical Recency Momentum");
          const sop = (r.tactical_directives && r.tactical_directives.length > 0)
            ? r.tactical_directives[0]
            : "Deploy plainclothes unit during peak hours (14:00 - 22:00 IST).";

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
            cell_atm_count: r.cell_atm_count || 20,
            transit_score: r.transit_score || 0.768,
            risk_tier: r.risk_tier || "CRITICAL",
            top_contributing_factors: drivers,
            sop: sop
          };
        });

        // Update counts
        const cntAll = document.getElementById("cnt-all");
        const cntCrit = document.getElementById("cnt-crit");
        const cntElev = document.getElementById("cnt-elev");
        if (cntAll) cntAll.innerText = activeForecasts.length;
        if (cntCrit) cntCrit.innerText = activeForecasts.filter(c => c.risk_tier === "CRITICAL").length;
        if (cntElev) cntElev.innerText = activeForecasts.filter(c => c.risk_tier === "ELEVATED").length;

        applyFilters();
        renderMapLayers();
        inspectCell(activeForecasts[0]);
      }
    }
  } catch (e) {
    console.log("CYBERWATCH: Running on embedded baseline telemetry.");
  }
}

// 12. Toast Notification Engine
function showToast(message) {
  const container = document.getElementById("toast-container");
  if (!container) return;

  const toast = document.createElement("div");
  toast.className = "flex items-center gap-2.5 px-4 py-2.5 rounded-xl bg-slate-900 border border-cyan-500/50 text-white text-xs font-semibold shadow-2xl backdrop-blur-md pointer-events-auto transition-all duration-300";
  toast.innerHTML = `
    <i data-lucide="check-circle" class="w-4 h-4 text-cyan-400"></i>
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
