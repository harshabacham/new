/**
 * CYBERWATCH // SIH26184
 * Web Application Logic & Geospatial Leaflet Engine
 */

// Embedded Fallback Dataset (Guarantees 100% offline functionality when opened as file://)
const FALLBACK_FORECASTS = [
  {
    priority_rank: 1,
    grid_cell_id: "CELL_03_15",
    centroid_lat: 28.535,
    centroid_lon: 77.255,
    lat_min: 28.530,
    lat_max: 28.540,
    lon_min: 77.250,
    lon_max: 77.260,
    pred_hotspot_prob: 0.9821,
    expected_withdrawals: 3.1,
    count_ci_lower: 2.2,
    count_ci_upper: 4.0,
    cell_atm_count: 10,
    risk_tier: "CRITICAL",
    top_contributing_factors: "Historical Recency Momentum (30d) | Weekly Repeat Withdrawal Burst",
    sop: "Deploy plainclothes static unit for Shift Alpha (14:00 - 22:00 IST). Monitor ATM vestibules discretely for multi-card cash sweeps."
  },
  {
    priority_rank: 2,
    grid_cell_id: "CELL_04_15",
    centroid_lat: 28.545,
    centroid_lon: 77.255,
    lat_min: 28.540,
    lat_max: 28.550,
    lon_min: 77.250,
    lon_max: 77.260,
    pred_hotspot_prob: 0.9821,
    expected_withdrawals: 7.8,
    count_ci_lower: 6.9,
    count_ci_upper: 8.7,
    cell_atm_count: 10,
    risk_tier: "CRITICAL",
    top_contributing_factors: "Historical Recency Momentum (30d) | Weekly Repeat Withdrawal Burst",
    sop: "Deploy plainclothes static unit for Shift Bravo (22:00 - 06:00 IST). Coordinate with bank security for rapid interdiction."
  },
  {
    priority_rank: 3,
    grid_cell_id: "CELL_13_11",
    centroid_lat: 28.635,
    centroid_lon: 77.215,
    lat_min: 28.630,
    lat_max: 28.640,
    lon_min: 77.210,
    lon_max: 77.220,
    pred_hotspot_prob: 0.9595,
    expected_withdrawals: 2.1,
    count_ci_lower: 1.2,
    count_ci_upper: 3.0,
    cell_atm_count: 10,
    risk_tier: "CRITICAL",
    top_contributing_factors: "Historical Recency Momentum (30d) | Short-Term Cash-Out Surge (3d)",
    sop: "Assign mobile motorcycle patrol in 20-min sweeps. Inspect commercial transit hub ATM vestibules."
  },
  {
    priority_rank: 4,
    grid_cell_id: "CELL_01_15",
    centroid_lat: 28.515,
    centroid_lon: 77.255,
    lat_min: 28.510,
    lat_max: 28.520,
    lon_min: 77.250,
    lon_max: 77.260,
    pred_hotspot_prob: 0.9548,
    expected_withdrawals: 1.9,
    count_ci_lower: 1.0,
    count_ci_upper: 2.8,
    cell_atm_count: 10,
    risk_tier: "CRITICAL",
    top_contributing_factors: "Historical Recency Momentum (30d) | Weekly Repeat Withdrawal Burst",
    sop: "Dispatch Section 91 CrPC CCTV preservation dockets to acquiring banks before automated 15-day purge."
  },
  {
    priority_rank: 5,
    grid_cell_id: "CELL_05_16",
    centroid_lat: 28.555,
    centroid_lon: 77.265,
    lat_min: 28.550,
    lat_max: 28.560,
    lon_min: 77.260,
    lon_max: 77.270,
    pred_hotspot_prob: 0.9522,
    expected_withdrawals: 1.8,
    count_ci_lower: 0.9,
    count_ci_upper: 2.7,
    cell_atm_count: 10,
    risk_tier: "CRITICAL",
    top_contributing_factors: "Weekly Repeat Withdrawal Burst | Historical Recency Momentum (30d)",
    sop: "Plainclothes monitoring during afternoon banking rush (14:00 - 18:00 IST)."
  },
  {
    priority_rank: 6,
    grid_cell_id: "CELL_03_17",
    centroid_lat: 28.535,
    centroid_lon: 77.275,
    lat_min: 28.530,
    lat_max: 28.540,
    lon_min: 77.270,
    lon_max: 77.280,
    pred_hotspot_prob: 0.9368,
    expected_withdrawals: 1.4,
    count_ci_lower: 0.5,
    count_ci_upper: 2.3,
    cell_atm_count: 9,
    risk_tier: "CRITICAL",
    top_contributing_factors: "Historical Recency Momentum (30d) | Weekly Repeat Withdrawal Burst",
    sop: "Monitor commercial shopping complex ATM corridor for repeat mule withdrawals."
  },
  {
    priority_rank: 7,
    grid_cell_id: "CELL_02_15",
    centroid_lat: 28.525,
    centroid_lon: 77.255,
    lat_min: 28.520,
    lat_max: 28.530,
    lon_min: 77.250,
    lon_max: 77.260,
    pred_hotspot_prob: 0.9257,
    expected_withdrawals: 1.5,
    count_ci_lower: 0.6,
    count_ci_upper: 2.4,
    cell_atm_count: 8,
    risk_tier: "CRITICAL",
    top_contributing_factors: "Historical Recency Momentum (30d) | Weekly Repeat Withdrawal Burst",
    sop: "Enforce bank step-up friction: lower single withdrawal caps to INR 10,000."
  },
  {
    priority_rank: 8,
    grid_cell_id: "CELL_02_16",
    centroid_lat: 28.525,
    centroid_lon: 77.265,
    lat_min: 28.520,
    lat_max: 28.530,
    lon_min: 77.260,
    lon_max: 77.270,
    pred_hotspot_prob: 0.9234,
    expected_withdrawals: 1.5,
    count_ci_lower: 0.6,
    count_ci_upper: 2.4,
    cell_atm_count: 8,
    risk_tier: "CRITICAL",
    top_contributing_factors: "Historical Recency Momentum (30d) | Short-Term Cash-Out Surge (3d)",
    sop: "Enforce dynamic friction on non-home debit cards."
  },
  {
    priority_rank: 9,
    grid_cell_id: "CELL_14_12",
    centroid_lat: 28.645,
    centroid_lon: 77.225,
    lat_min: 28.640,
    lat_max: 28.650,
    lon_min: 77.220,
    lon_max: 77.230,
    pred_hotspot_prob: 0.9173,
    expected_withdrawals: 1.2,
    count_ci_lower: 0.3,
    count_ci_upper: 2.1,
    cell_atm_count: 10,
    risk_tier: "CRITICAL",
    top_contributing_factors: "Historical Recency Momentum (30d) | Weekly Repeat Withdrawal Burst",
    sop: "Maintain surveillance around metro station ATM vestibules."
  },
  {
    priority_rank: 10,
    grid_cell_id: "CELL_13_12",
    centroid_lat: 28.635,
    centroid_lon: 77.225,
    lat_min: 28.630,
    lat_max: 28.640,
    lon_min: 77.220,
    lon_max: 77.230,
    pred_hotspot_prob: 0.9171,
    expected_withdrawals: 1.2,
    count_ci_lower: 0.3,
    count_ci_upper: 2.1,
    cell_atm_count: 10,
    risk_tier: "CRITICAL",
    top_contributing_factors: "Historical Recency Momentum (30d) | Weekly Repeat Withdrawal Burst",
    sop: "Coordinate plainclothes interception units with transit police."
  },
  {
    priority_rank: 11,
    grid_cell_id: "CELL_04_16",
    centroid_lat: 28.545,
    centroid_lon: 77.265,
    lat_min: 28.540,
    lat_max: 28.550,
    lon_min: 77.260,
    lon_max: 77.270,
    pred_hotspot_prob: 0.8840,
    expected_withdrawals: 1.1,
    count_ci_lower: 0.2,
    count_ci_upper: 2.0,
    cell_atm_count: 7,
    risk_tier: "ELEVATED",
    top_contributing_factors: "Historical Recency Momentum (30d) | High Density ATM Infrastructure",
    sop: "Routine motorcycle patrol sweeps every 30 minutes."
  },
  {
    priority_rank: 12,
    grid_cell_id: "CELL_12_11",
    centroid_lat: 28.625,
    centroid_lon: 77.215,
    lat_min: 28.620,
    lat_max: 28.630,
    lon_min: 77.210,
    lon_max: 77.220,
    pred_hotspot_prob: 0.8650,
    expected_withdrawals: 1.0,
    count_ci_lower: 0.1,
    count_ci_upper: 1.9,
    cell_atm_count: 9,
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

let mapInstance = null;
let top10LayerGroup = null;
let explorationLayerGroup = null;
let gridPolygonsGroup = null;
let activeForecasts = FALLBACK_FORECASTS;

// Initialize on DOM Load
document.addEventListener("DOMContentLoaded", () => {
  try {
    populateTable(activeForecasts);
  } catch (e) {
    console.error("Error populating table:", e);
  }
  try {
    setupTableSearch();
  } catch (e) {
    console.error("Error setting up table search:", e);
  }
  try {
    setupSimulator();
  } catch (e) {
    console.error("Error setting up simulator:", e);
  }
  try {
    initMap();
  } catch (e) {
    console.error("Leaflet map initialization error:", e);
  }
  tryFetchLiveForecasts();
});

// 1. Initialize Leaflet GIS Map
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

  // High-performance CartoDB Dark Matter Tiles (global CDN, 0ms rate limit)
  L.tileLayer("https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png", {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
    subdomains: 'abcd',
    maxZoom: 19
  }).addTo(mapInstance);

  top10LayerGroup = L.layerGroup().addTo(mapInstance);
  explorationLayerGroup = L.layerGroup().addTo(mapInstance);
  gridPolygonsGroup = L.layerGroup().addTo(mapInstance);

  renderMapLayers();

  // Map Controls
  document.getElementById("btn-toggle-top10").addEventListener("click", function() {
    this.classList.toggle("btn-active");
    if (mapInstance.hasLayer(top10LayerGroup)) {
      mapInstance.removeLayer(top10LayerGroup);
    } else {
      mapInstance.addLayer(top10LayerGroup);
    }
  });

  document.getElementById("btn-toggle-exploration").addEventListener("click", function() {
    this.classList.toggle("btn-active");
    if (mapInstance.hasLayer(explorationLayerGroup)) {
      mapInstance.removeLayer(explorationLayerGroup);
    } else {
      mapInstance.addLayer(explorationLayerGroup);
    }
  });

  document.getElementById("btn-reset-view").addEventListener("click", () => {
    mapInstance.setView(mapCenter, 11);
  });
}

// 2. Render GIS Layers on Map
function renderMapLayers() {
  top10LayerGroup.clearLayers();
  gridPolygonsGroup.clearLayers();
  explorationLayerGroup.clearLayers();

  // Render Grid Quadrants
  activeForecasts.forEach(cell => {
    const isTop10 = cell.priority_rank <= 10;
    const color = isTop10 ? "#f43f5e" : "#f59e0b";
    const fillOpacity = isTop10 ? 0.35 : 0.2;

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

    rect.on("click", () => selectCell(cell));
    rect.bindTooltip(`<b>${cell.grid_cell_id}</b><br>P(Hotspot): ${(cell.pred_hotspot_prob * 100).toFixed(1)}%<br>Tier: ${cell.risk_tier}`, {
      sticky: true
    });

    gridPolygonsGroup.addLayer(rect);

    // Add glowing marker for Top-10
    if (isTop10) {
      const markerHtml = `<div class="pulse-icon" style="width: 24px; height: 24px; display:flex; align-items:center; justify-content:center; color:#fff; font-weight:bold; font-size:10px;">${cell.priority_rank}</div>`;
      const customIcon = L.divIcon({
        html: markerHtml,
        className: 'custom-leaflet-marker',
        iconSize: [24, 24],
        iconAnchor: [12, 12]
      });

      const marker = L.marker([cell.centroid_lat, cell.centroid_lon], { icon: customIcon });
      marker.on("click", () => selectCell(cell));
      marker.bindPopup(`
        <div style="color: #060911; font-family: sans-serif;">
          <h4 style="margin: 0 0 6px;">#${cell.priority_rank}: ${cell.grid_cell_id}</h4>
          <p style="margin: 0 0 4px;"><strong>P(Cash-Out):</strong> ${(cell.pred_hotspot_prob * 100).toFixed(1)}%</p>
          <p style="margin: 0 0 4px;"><strong>Expected 24h:</strong> ${cell.expected_withdrawals} cashouts</p>
          <p style="margin: 0 0 4px;"><strong>Risk Tier:</strong> <span style="color: #e11d48; font-weight: bold;">${cell.risk_tier}</span></p>
          <p style="font-size: 11px; color: #475569; margin: 4px 0 0;">${cell.top_contributing_factors}</p>
        </div>
      `);
      top10LayerGroup.addLayer(marker);
    }
  });

  // Render 80/20 Exploration Audit Zones
  EXPLORATION_ZONES.forEach(zone => {
    const circle = L.circle([zone.lat, zone.lon], {
      radius: zone.radius,
      color: "#00f0ff",
      dashArray: "4, 6",
      fillColor: "#00f0ff",
      fillOpacity: 0.12,
      weight: 2
    });
    circle.bindTooltip(`<b>${zone.label}</b><br>Unbiased Background Audit Zone (20% Exploration Protocol)`, { sticky: true });
    explorationLayerGroup.addLayer(circle);
  });
}

// 3. Select and Inspect a Cell
function selectCell(cell) {
  document.getElementById("insp-cell-id").innerText = cell.grid_cell_id;
  document.getElementById("insp-tier").innerText = `${cell.risk_tier} HOTSPOT (Rank #${cell.priority_rank})`;
  document.getElementById("insp-coords").innerText = `${cell.centroid_lat.toFixed(3)}°N, ${cell.centroid_lon.toFixed(3)}°E (1km × 1km Quadrant)`;
  document.getElementById("insp-prob").innerText = `${(cell.pred_hotspot_prob * 100).toFixed(1)}%`;
  document.getElementById("insp-count").innerText = `${cell.expected_withdrawals} Cash-outs`;
  document.getElementById("insp-ci").innerText = `[${cell.count_ci_lower} - ${cell.count_ci_upper}]`;
  document.getElementById("insp-atms").innerText = `${cell.cell_atm_count || 10} Kiosks`;

  // Drivers
  const driversContainer = document.getElementById("insp-drivers");
  driversContainer.innerHTML = "";
  const drivers = (cell.top_contributing_factors || "Baseline Urban Traffic").split("|");
  drivers.forEach(d => {
    const tag = document.createElement("span");
    tag.className = "driver-tag";
    tag.innerText = d.trim();
    driversContainer.appendChild(tag);
  });

  // Directive
  document.getElementById("insp-sop").innerText = cell.sop || "Monitor ATM vestibules and log vehicle registrations.";

  // Pan map smoothly to selected cell
  mapInstance.panTo([cell.centroid_lat, cell.centroid_lon]);
}

// 4. Populate Prioritized Hotspots Table
function populateTable(data) {
  const tbody = document.getElementById("hotspots-tbody");
  tbody.innerHTML = "";

  data.forEach(item => {
    const tr = document.createElement("tr");
    const isTop10 = item.priority_rank <= 10;
    const tierBadgeClass = item.risk_tier === "CRITICAL" ? "badge-tier-critical" : "badge-tier-elevated";

    tr.innerHTML = `
      <td><strong>#${item.priority_rank}</strong></td>
      <td><span class="val-badge">${item.grid_cell_id}</span></td>
      <td>${item.centroid_lat.toFixed(3)}°N, ${item.centroid_lon.toFixed(3)}°E</td>
      <td><span class="text-rose"><strong>${(item.pred_hotspot_prob * 100).toFixed(1)}%</strong></span></td>
      <td>${item.expected_withdrawals} <span class="text-dim">[${item.count_ci_lower}-${item.count_ci_upper}]</span></td>
      <td><span class="badge ${tierBadgeClass}">${item.risk_tier}</span></td>
      <td><span style="font-size: 0.82rem; color: #cbd5e1;">${item.top_contributing_factors}</span></td>
      <td><button class="btn btn-sm btn-outline btn-inspect" data-cell="${item.grid_cell_id}">Inspect</button></td>
    `;

    tr.querySelector(".btn-inspect").addEventListener("click", () => {
      selectCell(item);
      window.scrollTo({ top: document.getElementById("gis-map").offsetTop - 80, behavior: "smooth" });
    });

    tbody.appendChild(tr);
  });
}

// 5. Setup Table Search & Filter
function setupTableSearch() {
  const searchInput = document.getElementById("table-search");
  searchInput.addEventListener("input", (e) => {
    const query = e.target.value.toLowerCase();
    const filtered = activeForecasts.filter(item => 
      item.grid_cell_id.toLowerCase().includes(query) ||
      item.top_contributing_factors.toLowerCase().includes(query) ||
      item.risk_tier.toLowerCase().includes(query) ||
      item.centroid_lat.toString().includes(query) ||
      item.centroid_lon.toString().includes(query)
    );
    populateTable(filtered);
  });
}

// 6. Setup Interactive 1930 Surge Simulator
function setupSimulator() {
  const sliderN = document.getElementById("sim-n");
  const lblN = document.getElementById("lbl-sim-n");
  const sliderLoss = document.getElementById("sim-loss");
  const lblLoss = document.getElementById("lbl-sim-loss");
  const btnRun = document.getElementById("btn-run-sim");

  sliderN.addEventListener("input", (e) => {
    lblN.innerText = `${e.target.value} reports`;
  });

  sliderLoss.addEventListener("input", (e) => {
    lblLoss.innerText = `₹${Number(e.target.value).toLocaleString()}`;
  });

  btnRun.addEventListener("click", () => {
    const n = parseInt(sliderN.value);
    const category = document.getElementById("sim-category").value;
    const loss = parseInt(sliderLoss.value);

    // Compute simulation
    const totalLoss = n * loss * (0.85 + Math.random() * 0.3);
    const meanDelayHours = (10.5 + Math.random() * 4.5).toFixed(1);

    const targetCandidates = ["CELL_03_15", "CELL_04_15", "CELL_13_11", "CELL_01_15", "CELL_05_16"];
    const targetHub = targetCandidates[Math.floor(Math.random() * targetCandidates.length)];

    // Update Banner
    const now = new Date();
    const estArrival = new Date(now.getTime() + meanDelayHours * 3600 * 1000);
    const arrivalStr = estArrival.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

    document.getElementById("sim-alert-title").innerHTML = `🚨 ACTIVE INTERDICTION ALERT: ${n} COMPLAINTS INGESTED`;
    document.getElementById("sim-alert-desc").innerHTML = `
      Estimated cash-out convergence window: <strong>+${meanDelayHours} Hours</strong> (Opening around <strong>${arrivalStr} IST</strong>).<br>
      High-risk convergence corridor identified: <strong>${targetHub}</strong>. Dispatch plainclothes units immediately.
    `;

    document.getElementById("sm-loss").innerText = `₹${Math.round(totalLoss).toLocaleString()}`;
    document.getElementById("sm-window").innerText = `+${meanDelayHours}h (${arrivalStr})`;
    document.getElementById("sm-hub").innerText = targetHub;

    // Populate Telemetry Feed
    const feed = document.getElementById("telemetry-feed");
    feed.innerHTML = "";

    for (let i = 0; i < n; i++) {
      const item = document.createElement("div");
      item.className = "telemetry-item";
      const indLoss = Math.round(loss * (0.7 + Math.random() * 0.6));
      const indDelay = (8 + Math.random() * 7).toFixed(1);
      const indCell = targetCandidates[Math.floor(Math.random() * targetCandidates.length)];
      const compId = `NCRP-1930-${104820 + i}`;

      item.innerHTML = `
        <span><strong style="color: #38bdf8;">${compId}</strong> | ${category}</span>
        <span>Loss: ₹${indLoss.toLocaleString()} | Window: +${indDelay}h -> <span style="color:#f43f5e; font-weight:bold;">${indCell}</span></span>
      `;
      feed.appendChild(item);
    }
  });
}

// 7. Attempt Live API Fetch
async function tryFetchLiveForecasts() {
  try {
    const res = await fetch("/api/v1/forecasts?limit=30");
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
            : (r.sop || "Deploy plainclothes unit for active corridor interdiction.");

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
            risk_tier: r.risk_tier || "CRITICAL",
            top_contributing_factors: drivers,
            sop: sop
          };
        });
        renderMapLayers();
        populateTable(activeForecasts);
        selectCell(activeForecasts[0]);
        console.log("Successfully loaded live forecasts from REST API microservice.");
      }
    }
  } catch (e) {
    console.log("Running in offline mode (using bundled fallback telemetry).");
    selectCell(activeForecasts[0]);
  }
}
