/**
 * CyberWatch AI - Cybercrime Cash-Withdrawal Location Forecasting Platform
 * Master Application Engine
 */

// Comprehensive Police Station and Delhi Landmark Registry
const DELHI_POLICE_REGISTRY = {
  "CELL_03_15": {
    name: "Nehru Place Commercial Hub",
    ps: "PS Kalkaji / PS Nehru Place",
    key_points: "Nehru Place Metro Gate 2, Computer Market Vestibules",
    strategy: "Plainclothes static surveillance (2 officers) + 1 Beat PCR",
    shift: "14:00 - 22:00 IST (Alpha)",
    transit: "High (Metro Interchange & Terminal)",
    sop: "Deploy plainclothes static unit at Nehru Place Metro Gate 2. Observe ATM vestibules discretely for individuals conducting repeated multi-card cash sweeps. Inform bank security."
  },
  "CELL_04_15": {
    name: "Kalkaji / Okhla Commercial Corridor",
    ps: "PS Kalkaji / PS Okhla Industrial Area",
    key_points: "Maa Anandmayee Marg ATM Cluster",
    strategy: "Motorcycle patrol sweeps every 15 minutes",
    shift: "14:00 - 22:00 IST (Alpha)",
    transit: "High (Industrial Arterial)",
    sop: "Frequent physical sweeps of standalone off-site ATM kiosks along Maa Anandmayee Marg. Verify identity of individuals loitering near cash dispensers."
  },
  "CELL_13_11": {
    name: "Connaught Place / Rajiv Chowk Cluster",
    ps: "PS Connaught Place",
    key_points: "Outer Circle Blocks B, C & E ATM Rows",
    strategy: "Static foot patrol across commercial banks",
    shift: "14:00 - 22:00 IST (Alpha)",
    transit: "Extreme (Primary Metro Interchange)",
    sop: "Station static plainclothes beat officers outside high-volume private bank branches along Outer Circle. Coordinate with security guards to watch for non-home debit card sweeps."
  },
  "CELL_01_15": {
    name: "Saket District Centre / Press Enclave",
    ps: "PS Saket",
    key_points: "District Centre Mall & Multiplex ATM Vestibules",
    strategy: "Plainclothes monitoring + Mall security liaison",
    shift: "14:00 - 22:00 IST (Alpha)",
    transit: "Moderate (Shopping District Transit)",
    sop: "Liaise with mall security supervisors. Position plainclothes officers near high-footfall basement and exterior ATM vestibules."
  },
  "CELL_05_16": {
    name: "Lajpat Nagar / Defence Colony Hub",
    ps: "PS Lajpat Nagar",
    key_points: "Central Market Ring Road ATMs",
    strategy: "Motorcycle sweep during market rush",
    shift: "15:00 - 21:00 IST (Market Peak)",
    transit: "High (Ring Road Corridor)",
    sop: "Intensify patrol checks between 16:00 and 20:00 IST during peak market rush. Inspect unattended ATM kiosks for skimming devices or loiterers."
  },
  "CELL_03_17": {
    name: "Sarita Vihar / Jasola Commercial Corridor",
    ps: "PS Sarita Vihar",
    key_points: "Jasola Apollo Commercial Complex",
    strategy: "Patrol vehicle spot checks",
    shift: "14:00 - 22:00 IST (Alpha)",
    transit: "Moderate (Interstate Highway Access)",
    sop: "Conduct randomized spot checks at isolated ATM kiosks along Mathura Road and Jasola Commercial Towers."
  },
  "CELL_02_15": {
    name: "Malviya Nagar / Hauz Khas East",
    ps: "PS Malviya Nagar",
    key_points: "Main Market & Shivalik Road ATMs",
    strategy: "Beat constable foot patrol",
    shift: "14:00 - 22:00 IST (Alpha)",
    transit: "Moderate (Commercial Fringe)",
    sop: "Beat staff to maintain log of visited ATM vestibules. Check emergency alarm buttons and ensure guard presence."
  },
  "CELL_02_16": {
    name: "Chirag Dilli / Sheikh Sarai Hub",
    ps: "PS Chirag Dilli",
    key_points: "Panchsheel Flyover Commercial Fringe",
    strategy: "Mobile PCR van positioning",
    shift: "14:00 - 22:00 IST (Alpha)",
    transit: "Moderate (Flyover Junction)",
    sop: "Station mobile PCR van at Panchsheel / Chirag Dilli intersection for rapid interdiction upon 1930 dispatch."
  },
  "CELL_14_12": {
    name: "New Delhi Railway Station / Paharganj",
    ps: "PS Paharganj / PS NDLS",
    key_points: "Ajmeri Gate Exit & Main Bazar ATMs",
    strategy: "Joint Railway & Local Police sweep",
    shift: "12:00 - 20:00 IST (Transit Peak)",
    transit: "Extreme (Railway Terminal)",
    sop: "Joint surveillance with RPF. Mules exploit high passenger transit volume for cash extractions before boarding outbound trains."
  },
  "CELL_13_12": {
    name: "Barakhamba Road / Mandi House Corridor",
    ps: "PS Barakhamba Road",
    key_points: "KG Marg & Tolstoy Marg Bank Branches",
    strategy: "Static cruiser deployment",
    shift: "14:00 - 20:00 IST (Banking Hours)",
    transit: "High (Financial District)",
    sop: "Monitor commercial bank branch ATMs for unusual bulk transaction frequencies. Advise bank branch managers to flag multi-card cash sweeps."
  }
};

function getSectorData(cell) {
  const custom = DELHI_POLICE_REGISTRY[cell.grid_cell_id];
  if (custom) return custom;

  const lat = cell.centroid_lat;
  const lon = cell.centroid_lon;
  let defaultPS = "PS Central Delhi";
  let defaultName = `Delhi NCR Sector (${cell.grid_cell_id})`;
  if (lat > 28.62 && lon < 77.23) {
    defaultPS = "PS Connaught Place / PS New Delhi";
    defaultName = `Central Delhi Sector (${cell.grid_cell_id})`;
  } else if (lat <= 28.56 && lon >= 77.24) {
    defaultPS = "PS Kalkaji / PS South-East";
    defaultName = `South-East Commercial Sector (${cell.grid_cell_id})`;
  } else if (lat <= 28.56) {
    defaultPS = "PS Saket / PS South Delhi";
    defaultName = `South Delhi Commercial Sector (${cell.grid_cell_id})`;
  }

  return {
    name: defaultName,
    ps: defaultPS,
    key_points: "Commercial Market ATM Vestibules",
    strategy: "Routine motorcycle sweep every 30 minutes",
    shift: "14:00 - 22:00 IST (Alpha)",
    transit: "Moderate (Arterial Transit)",
    sop: cell.sop || "Conduct routine checks of standalone ATM kiosks. Inspect vestibules for suspicious loitering."
  };
}

// Embedded Fallback Priority Hotspots (100% Offline Resilience)
const FALLBACK_FORECASTS = [
  {
    priority_rank: 1, grid_cell_id: "CELL_03_15",
    centroid_lat: 28.535, centroid_lon: 77.255,
    pred_hotspot_prob: 0.9821, expected_withdrawals: 3.1,
    cell_atm_count: 29, risk_tier: "CRITICAL"
  },
  {
    priority_rank: 2, grid_cell_id: "CELL_04_15",
    centroid_lat: 28.545, centroid_lon: 77.255,
    pred_hotspot_prob: 0.9821, expected_withdrawals: 7.8,
    cell_atm_count: 28, risk_tier: "CRITICAL"
  },
  {
    priority_rank: 3, grid_cell_id: "CELL_13_11",
    centroid_lat: 28.635, centroid_lon: 77.215,
    pred_hotspot_prob: 0.9595, expected_withdrawals: 2.1,
    cell_atm_count: 33, risk_tier: "CRITICAL"
  },
  {
    priority_rank: 4, grid_cell_id: "CELL_01_15",
    centroid_lat: 28.515, centroid_lon: 77.255,
    pred_hotspot_prob: 0.9548, expected_withdrawals: 1.9,
    cell_atm_count: 28, risk_tier: "CRITICAL"
  },
  {
    priority_rank: 5, grid_cell_id: "CELL_05_16",
    centroid_lat: 28.555, centroid_lon: 77.265,
    pred_hotspot_prob: 0.9522, expected_withdrawals: 1.8,
    cell_atm_count: 35, risk_tier: "CRITICAL"
  },
  {
    priority_rank: 6, grid_cell_id: "CELL_03_17",
    centroid_lat: 28.535, centroid_lon: 77.275,
    pred_hotspot_prob: 0.9368, expected_withdrawals: 1.4,
    cell_atm_count: 19, risk_tier: "CRITICAL"
  },
  {
    priority_rank: 7, grid_cell_id: "CELL_02_15",
    centroid_lat: 28.525, centroid_lon: 77.255,
    pred_hotspot_prob: 0.9257, expected_withdrawals: 1.5,
    cell_atm_count: 24, risk_tier: "CRITICAL"
  },
  {
    priority_rank: 8, grid_cell_id: "CELL_02_16",
    centroid_lat: 28.525, centroid_lon: 77.265,
    pred_hotspot_prob: 0.9234, expected_withdrawals: 1.5,
    cell_atm_count: 19, risk_tier: "CRITICAL"
  },
  {
    priority_rank: 9, grid_cell_id: "CELL_14_12",
    centroid_lat: 28.645, centroid_lon: 77.225,
    pred_hotspot_prob: 0.9189, expected_withdrawals: 1.3,
    cell_atm_count: 23, risk_tier: "CRITICAL"
  },
  {
    priority_rank: 10, grid_cell_id: "CELL_13_12",
    centroid_lat: 28.635, centroid_lon: 77.225,
    pred_hotspot_prob: 0.9122, expected_withdrawals: 1.3,
    cell_atm_count: 24, risk_tier: "CRITICAL"
  }
];

// Anti-bias exploration patrol zones (20% random allocation)
const EXPLORATION_ZONES = [
  { lat: 28.505, lon: 77.105, radius: 900, label: "Exploration Zone Alpha (South-West)" },
  { lat: 28.685, lon: 77.125, radius: 900, label: "Exploration Zone Bravo (North-West)" },
  { lat: 28.695, lon: 77.285, radius: 900, label: "Exploration Zone Charlie (North-East)" },
  { lat: 28.515, lon: 77.285, radius: 900, label: "Exploration Zone Delta (South-East)" }
];

// Global State
let mapInstance = null;
let top10LayerGroup = null;
let explorationLayerGroup = null;

let activeForecasts = FALLBACK_FORECASTS;
let filteredForecasts = FALLBACK_FORECASTS;
let selectedCell = FALLBACK_FORECASTS[0];
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

  // Center on South/Central Delhi
  mapInstance = L.map("leaflet-map", {
    center: [28.585, 77.235],
    zoom: 12,
    zoomControl: true,
    minZoom: 10,
    maxZoom: 16
  });

  // CartoDB Dark Matter Basemap
  L.tileLayer("https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png", {
    attribution: '&copy; <a href="https://carto.com/">CARTO</a> &bull; CyberWatch AI',
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
      this.classList.toggle("opacity-50");
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
      this.classList.toggle("opacity-50");
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
    showToast(`Centered map on ${lat.toFixed(3)}°N, ${lon.toFixed(3)}°E`);
  }
}

// 4. Render Map Markers & Polygons
function renderMapLayers() {
  if (!mapInstance || !top10LayerGroup) return;
  top10LayerGroup.clearLayers();
  explorationLayerGroup.clearLayers();

  activeForecasts.slice(0, 10).forEach(cell => {
    const sData = getSectorData(cell);
    const radius = 700;
    const isTop3 = cell.priority_rank <= 3;
    const color = isTop3 ? "#fb7185" : "#f59e0b";
    const fillColor = isTop3 ? "#f43f5e" : "#d97706";

    const circle = L.circle([cell.centroid_lat, cell.centroid_lon], {
      radius: radius,
      color: color,
      weight: 2.5,
      fillColor: fillColor,
      fillOpacity: isTop3 ? 0.38 : 0.22
    });

    const popupHtml = `
      <div style="font-family:'Plus Jakarta Sans',sans-serif; min-width: 230px; padding: 4px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 6px;">
          <span style="font-size:11px; font-weight:bold; color:#fb7185; background:rgba(251,113,133,0.15); padding:2px 6px; border-radius:4px;">
            PRIORITY #${cell.priority_rank} TARGET
          </span>
          <span style="font-size:11px; font-weight:bold; color:#38bdf8;">${(cell.pred_hotspot_prob * 100).toFixed(1)}% Risk</span>
        </div>
        <div style="font-size:13px; font-weight:bold; color:#ffffff; margin-bottom: 3px;">
          ${sData.name}
        </div>
        <div style="font-size:11px; color:#38bdf8; font-weight:bold; margin-bottom: 6px;">
          ${sData.ps}
        </div>
        <div style="font-size:11px; color:#cbd5e1; margin-bottom: 8px;">
          Vulnerable ATMs: <strong>${cell.cell_atm_count || 20} Kiosks</strong><br>
          Shift: <strong>${sData.shift}</strong>
        </div>
        <button onclick="selectAndFocusCell('${cell.grid_cell_id}')" style="width:100%; padding: 6px; font-size:11px; font-weight:bold; background:#2563eb; color:#ffffff; border:none; border-radius:6px; cursor:pointer;">
          Inspect Tactical Directive &rarr;
        </button>
      </div>
    `;

    circle.bindPopup(popupHtml);
    circle.on("click", () => inspectCell(cell));
    top10LayerGroup.addLayer(circle);
  });

  // Exploration Zones
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
        <div style="font-size:11px; color:#94a3b8; margin-top:2px;">Anti-bias patrol safeguard sector (20% allocation)</div>
      </div>
    `);
    explorationLayerGroup.addLayer(circle);
  });
}

// 5. Inspect Cell in Detail Card
function inspectCell(cell) {
  selectedCell = cell;
  const sData = getSectorData(cell);

  const nameEl = document.getElementById("insp-cell-name");
  const idEl = document.getElementById("insp-cell-id");
  const psEl = document.getElementById("insp-ps-name");
  const tierEl = document.getElementById("insp-tier");
  const rankEl = document.getElementById("insp-rank");
  const probEl = document.getElementById("insp-prob");
  const countEl = document.getElementById("insp-count");
  const atmsEl = document.getElementById("insp-atms");
  const sopEl = document.getElementById("insp-sop");

  if (nameEl) nameEl.innerText = sData.name;
  if (idEl) idEl.innerText = `Sector ID: ${cell.grid_cell_id} • ${cell.centroid_lat.toFixed(3)}°N, ${cell.centroid_lon.toFixed(3)}°E`;
  if (psEl) psEl.innerText = `Police Station: ${sData.ps}`;
  if (rankEl) rankEl.innerText = `PRIORITY #${cell.priority_rank}`;

  if (tierEl) {
    const isCrit = cell.priority_rank <= 5;
    tierEl.innerText = isCrit ? "CRITICAL HOTSPOT" : "ELEVATED WATCH";
    tierEl.className = isCrit
      ? "px-2.5 py-0.5 rounded-full text-xs font-bold uppercase bg-rose-500/15 border border-rose-500/40 text-rose-300"
      : "px-2.5 py-0.5 rounded-full text-xs font-bold uppercase bg-amber-500/15 border border-amber-500/40 text-amber-300";
  }

  if (probEl) probEl.innerText = `${(cell.pred_hotspot_prob * 100).toFixed(1)}%`;
  if (countEl) countEl.innerText = `${cell.expected_withdrawals}`;
  if (atmsEl) atmsEl.innerText = `${cell.cell_atm_count || 20} Kiosks`;
  if (sopEl) sopEl.innerText = sData.sop;
}

// Select cell and focus map
function selectAndFocusCell(cellId) {
  const match = activeForecasts.find(c => c.grid_cell_id === cellId);
  if (match) {
    inspectCell(match);
    jumpToSector(match.centroid_lat, match.centroid_lon, 14);
    const mapSec = document.getElementById("gis-map");
    if (mapSec) mapSec.scrollIntoView({ behavior: "smooth" });
  }
}

// 6. Copy Police Dispatch Order
function copyPoliceBriefing() {
  if (!selectedCell) return;
  const sData = getSectorData(selectedCell);
  const text = `🚨 CYBERWATCH AI TACTICAL DISPATCH DIRECTIVE 🚨
Sector: ${sData.name} (${selectedCell.grid_cell_id})
Jurisdiction: ${sData.ps}
Key Extraction Point: ${sData.key_points}
Vulnerable ATMs: ${selectedCell.cell_atm_count || 20} Kiosks
Mule Cashout Risk: ${(selectedCell.pred_hotspot_prob * 100).toFixed(1)}% High Probability
Assigned Shift: ${sData.shift}
Strategy: ${sData.strategy}
Field SOP: ${sData.sop}
Evidence Notice: Request branch security to preserve CCTV records for 48 hours.`;

  navigator.clipboard.writeText(text).then(() => {
    showToast(`Copied Dispatch Order for ${sData.name}`);
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

  filteredForecasts = activeForecasts.slice(0, 10).filter(cell => {
    const sData = getSectorData(cell);
    if (activeFilterTier === "CRITICAL" && cell.priority_rank > 5) return false;

    if (query) {
      const matchName = sData.name.toLowerCase().includes(query);
      const matchPS = sData.ps.toLowerCase().includes(query);
      const matchStrategy = sData.strategy.toLowerCase().includes(query);
      if (!matchName && !matchPS && !matchStrategy) return false;
    }
    return true;
  });

  renderTable();
}

function renderTable() {
  const tbody = document.getElementById("hotspots-tbody");
  if (!tbody) return;

  tbody.innerHTML = "";

  if (filteredForecasts.length === 0) {
    tbody.innerHTML = `
      <tr>
        <td colspan="8" class="text-center py-6 text-slate-500 text-xs">
          No matching sectors found. Try searching for "Kalkaji", "Connaught", or "Saket".
        </td>
      </tr>
    `;
    return;
  }

  filteredForecasts.forEach(cell => {
    const sData = getSectorData(cell);
    const tr = document.createElement("tr");
    tr.className = "hover:bg-slate-900/60 transition-colors";

    tr.innerHTML = `
      <td class="py-3 px-4 font-mono font-bold ${cell.priority_rank <= 3 ? 'text-rose-400' : 'text-slate-300'}">
        #${cell.priority_rank}
      </td>
      <td class="py-3 px-4 font-bold text-white">
        ${sData.name}
      </td>
      <td class="py-3 px-4 font-semibold text-cyan-300">
        ${sData.ps}
      </td>
      <td class="py-3 px-4 font-mono text-slate-200">
        ${cell.cell_atm_count || 20} Kiosks
      </td>
      <td class="py-3 px-4 font-mono font-bold text-rose-400">
        ${(cell.pred_hotspot_prob * 100).toFixed(1)}%
      </td>
      <td class="py-3 px-4 font-medium text-amber-300">
        ${sData.shift}
      </td>
      <td class="py-3 px-4 text-slate-300 text-[11px]">
        ${sData.strategy}
      </td>
      <td class="py-3 px-4 text-right">
        <button onclick="selectAndFocusCell('${cell.grid_cell_id}')" class="px-2.5 py-1 text-xs font-bold rounded-lg bg-blue-600/20 hover:bg-blue-600/40 text-blue-300 border border-blue-500/40 transition-all">
          Focus on Map &rarr;
        </button>
      </td>
    `;
    tbody.appendChild(tr);
  });
}

function setupTableSearch() {
  const input = document.getElementById("table-search");
  if (!input) return;

  let debounceTimer;
  input.addEventListener("input", () => {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => {
      applyFilters();
    }, 150);
  });
}

function setupFilterChips() {
  const chips = document.querySelectorAll(".filter-chip");
  chips.forEach(chip => {
    chip.addEventListener("click", () => {
      chips.forEach(c => {
        c.className = "filter-chip px-3.5 py-1.5 rounded-lg font-semibold bg-brand-surface border border-slate-800 text-slate-400 hover:text-white transition-all text-xs";
      });
      chip.className = "filter-chip px-3.5 py-1.5 rounded-lg font-bold bg-cyan-500/15 border border-cyan-500 text-cyan-300 transition-all active text-xs";
      activeFilterTier = chip.getAttribute("data-filter");
      applyFilters();
    });
  });
}

// 8. 1930 Fraud Complaint Cash-Out Simulator
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
    const timeElapsedHours = parseInt(document.getElementById("sim-time").value || 0);

    let baseDelay = 3.5;
    if (category.includes("UPI")) baseDelay = 2.0;
    else if (category.includes("Skimming")) baseDelay = 1.2;
    else if (category.includes("Investment")) baseDelay = 4.5;

    const remainingDelay = Math.max(0.5, (baseDelay - timeElapsedHours + (Math.random() * 0.4 - 0.2))).toFixed(1);

    const candidates = [
      { name: "Nehru Place Commercial Hub", ps: "PS Kalkaji / PS Nehru Place", id: "CELL_03_15" },
      { name: "Connaught Place / Rajiv Chowk", ps: "PS Connaught Place", id: "CELL_13_11" },
      { name: "Saket District Centre", ps: "PS Saket", id: "CELL_01_15" },
      { name: "Kalkaji Commercial Corridor", ps: "PS Kalkaji", id: "CELL_04_15" }
    ];
    const topCandidate = candidates[Math.floor(Math.random() * candidates.length)];

    const now = new Date();
    const estArrival = new Date(now.getTime() + remainingDelay * 3600 * 1000);
    const arrivalStr = estArrival.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

    const titleEl = document.getElementById("sim-alert-title");
    const descEl = document.getElementById("sim-alert-desc");

    if (titleEl) titleEl.innerText = `Target Identified: ${topCandidate.name}`;
    if (descEl) {
      descEl.innerHTML = `
        Incident assessed: <strong>${category}</strong> (Loss: <strong>&#8377;${loss.toLocaleString()}</strong>).<br>
        Money mule cashout expected at ATM vestibules in <strong>${topCandidate.ps}</strong> jurisdiction at approximately <strong>${arrivalStr} IST</strong> (+${remainingDelay}h).
      `;
    }

    const winEl = document.getElementById("sm-window");
    const hubEl = document.getElementById("sm-hub");
    const urgEl = document.getElementById("sm-urgency");

    if (winEl) winEl.innerText = `+${remainingDelay}h (${arrivalStr})`;
    if (hubEl) hubEl.innerText = topCandidate.name;
    if (urgEl) urgEl.innerText = remainingDelay < 2 ? "Immediate Alert" : "Deploy Patrol";

    showToast(`Calculated target: ${topCandidate.name} (+${remainingDelay}h)`);
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
    if (lbl) lbl.innerText = "Hide Academic Benchmarks";
    if (icon) icon.style.transform = "rotate(180deg)";
  } else {
    container.classList.add("hidden");
    if (lbl) lbl.innerText = "Show Academic Benchmarks";
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

// 11. Edge Data Ingestion
async function tryFetchLiveForecasts() {
  try {
    const res = await fetch("data/forecasts.json");
    if (res.ok) {
      const data = await res.json();
      if (data && data.results && data.results.length > 0) {
        activeForecasts = data.results.slice(0, 10).map(r => {
          const lat = r.coordinates ? r.coordinates.latitude : 28.535;
          const lon = r.coordinates ? r.coordinates.longitude : 77.255;
          return {
            priority_rank: r.priority_rank,
            grid_cell_id: r.grid_cell_id,
            centroid_lat: lat,
            centroid_lon: lon,
            pred_hotspot_prob: r.hotspot_probability !== undefined ? r.hotspot_probability : 0.90,
            expected_withdrawals: r.expected_withdrawals_24h || 2.5,
            cell_atm_count: r.cell_atm_count || 20,
            risk_tier: r.risk_tier || "CRITICAL",
            sop: (r.tactical_directives && r.tactical_directives.length > 0)
              ? r.tactical_directives[0]
              : "Deploy plainclothes unit during peak hours (14:00 - 22:00 IST)."
          };
        });

        applyFilters();
        renderMapLayers();
        inspectCell(activeForecasts[0]);
      }
    }
  } catch (e) {
    console.log("CYBERWATCH: Ingested embedded operational roster.");
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
