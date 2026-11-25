/**
 * CyberWatch Delhi - ATM Cybercrime Cash-Out Hotspot Tracker
 * Clean, User-Friendly Client Engine
 */

// User-friendly Delhi Area Registry with landmarks and police station jurisdictions
const DELHI_AREAS = [
  {
    id: "CELL_03_15",
    rank: 1,
    name: "Nehru Place Commercial Hub",
    ps: "PS Kalkaji / PS Nehru Place",
    lat: 28.535,
    lon: 77.255,
    atms: 29,
    prob: "98%",
    prob_num: 0.98,
    tier: "HIGH RISK",
    hours: "2:00 PM – 10:00 PM IST (Afternoon & Evening)",
    why: "Massive electronic market with heavy foot traffic, major metro interchange, and 29 bank ATM kiosks near Metro Gate 2.",
    action: "Deploy plainclothes police patrol at Nehru Place Metro Gate 2. Alert bank security guards to look for individuals using multiple cards."
  },
  {
    id: "CELL_04_15",
    rank: 2,
    name: "Kalkaji / Okhla Commercial Corridor",
    ps: "PS Kalkaji / PS Okhla Industrial Area",
    lat: 28.545,
    lon: 77.255,
    atms: 28,
    prob: "98%",
    prob_num: 0.98,
    tier: "HIGH RISK",
    hours: "2:00 PM – 10:00 PM IST (Shift Alpha)",
    why: "Arterial road (Maa Anandmayee Marg) with multiple standalone off-site ATM kiosks facilitating rapid vehicle getaway.",
    action: "Motorcycle patrol sweeps every 15 minutes along Maa Anandmayee Marg. Check unattended ATM kiosks for skimming devices."
  },
  {
    id: "CELL_13_11",
    rank: 3,
    name: "Connaught Place / Rajiv Chowk",
    ps: "PS Connaught Place",
    lat: 28.635,
    lon: 77.215,
    atms: 33,
    prob: "96%",
    prob_num: 0.96,
    tier: "HIGH RISK",
    hours: "1:00 PM – 9:00 PM IST (Business Hours)",
    why: "Central business district with 33 bank branches along Outer Circle Blocks B, C & E, carrying high daily cash turnover.",
    action: "Position static beat constables outside private bank ATM vestibules on Outer Circle. Coordinate with bank managers."
  },
  {
    id: "CELL_01_15",
    rank: 4,
    name: "Saket District Centre / Press Enclave",
    ps: "PS Saket",
    lat: 28.515,
    lon: 77.255,
    atms: 28,
    prob: "95%",
    prob_num: 0.95,
    tier: "HIGH RISK",
    hours: "3:00 PM – 11:00 PM IST (Evening Rush)",
    why: "Major shopping mall and cinema complex where large cash withdrawals blend into evening retail spending.",
    action: "Liaise with mall security supervisors. Monitor basement and exterior standalone ATM kiosks."
  },
  {
    id: "CELL_05_16",
    rank: 5,
    name: "Lajpat Nagar / Defence Colony Hub",
    ps: "PS Lajpat Nagar",
    lat: 28.555,
    lon: 77.265,
    atms: 35,
    prob: "95%",
    prob_num: 0.95,
    tier: "HIGH RISK",
    hours: "4:00 PM – 10:00 PM IST (Market Peak)",
    why: "Bustling central retail market near Ring Road with dense concentration of nationalized and private bank ATMs.",
    action: "Conduct foot patrols through Central Market ATM corridors during peak shopping hours."
  },
  {
    id: "CELL_03_17",
    rank: 6,
    name: "Sarita Vihar / Jasola Corridor",
    ps: "PS Sarita Vihar",
    lat: 28.535,
    lon: 77.275,
    atms: 19,
    prob: "94%",
    prob_num: 0.94,
    tier: "MODERATE",
    hours: "2:00 PM – 10:00 PM IST",
    why: "Commercial office towers and highway access points facilitating rapid regional exit towards Faridabad.",
    action: "Conduct randomized spot checks at isolated ATM kiosks along Mathura Road."
  },
  {
    id: "CELL_02_15",
    rank: 7,
    name: "Malviya Nagar / Hauz Khas East",
    ps: "PS Malviya Nagar",
    lat: 28.525,
    lon: 77.255,
    atms: 24,
    prob: "93%",
    prob_num: 0.93,
    tier: "MODERATE",
    hours: "2:00 PM – 10:00 PM IST",
    why: "Dense commercial and residential market with high ATM transaction velocity.",
    action: "Beat constables to maintain log of visited ATM vestibules and check guard presence."
  },
  {
    id: "CELL_02_16",
    rank: 8,
    name: "Chirag Dilli / Sheikh Sarai Hub",
    ps: "PS Chirag Dilli",
    lat: 28.525,
    lon: 77.265,
    atms: 19,
    prob: "92%",
    prob_num: 0.92,
    tier: "MODERATE",
    hours: "2:00 PM – 10:00 PM IST",
    why: "Panchsheel flyover junction with commercial ATMs on service lanes.",
    action: "Position mobile PCR van at Panchsheel intersection for rapid response upon 1930 dispatch."
  },
  {
    id: "CELL_14_12",
    rank: 9,
    name: "New Delhi Railway Station / Paharganj",
    ps: "PS Paharganj / PS NDLS",
    lat: 28.645,
    lon: 77.225,
    atms: 23,
    prob: "92%",
    prob_num: 0.92,
    tier: "MODERATE",
    hours: "12:00 PM – 8:00 PM IST (Transit Peak)",
    why: "Major transit railway hub where transient crowd allows cash-runners to blend in before boarding outbound trains.",
    action: "Joint surveillance with Railway Police (RPF) at Ajmeri Gate exit ATM kiosks."
  },
  {
    id: "CELL_13_12",
    rank: 10,
    name: "Barakhamba Road / Mandi House",
    ps: "PS Barakhamba Road",
    lat: 28.635,
    lon: 77.225,
    atms: 24,
    prob: "91%",
    prob_num: 0.91,
    tier: "MODERATE",
    hours: "2:00 PM – 8:00 PM IST (Banking Hours)",
    why: "Institutional banking corridor with corporate headquarters and private bank branches.",
    action: "Advise corporate bank security officers to watch for repeated high-value non-home debit card sweeps."
  }
];

// Global State
let mapInstance = null;
let mapMarkersGroup = null;
let selectedArea = DELHI_AREAS[0];
let currentFilter = "ALL";

// Initialize on DOM Ready
document.addEventListener("DOMContentLoaded", () => {
  initMap();
  initTable();
  setupHeroSearch();
  setupSimulator();
  setupFilterChips();
  if (window.lucide) lucide.createIcons();
});

// 1. Initialize Map
function initMap() {
  const mapEl = document.getElementById("leaflet-map");
  if (!mapEl) return;

  mapInstance = L.map("leaflet-map", {
    center: [28.585, 77.235],
    zoom: 12,
    zoomControl: true,
    minZoom: 10,
    maxZoom: 16
  });

  // Dark Matter basemap
  L.tileLayer("https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png", {
    attribution: '&copy; <a href="https://carto.com/">CARTO</a> &bull; CyberWatch Delhi',
    subdomains: "abcd",
    maxZoom: 19
  }).addTo(mapInstance);

  mapMarkersGroup = L.layerGroup().addTo(mapInstance);
  renderMapMarkers();
}

function renderMapMarkers() {
  if (!mapInstance || !mapMarkersGroup) return;
  mapMarkersGroup.clearLayers();

  DELHI_AREAS.forEach(area => {
    const isCritical = area.tier === "HIGH RISK";
    const color = isCritical ? "#f43f5e" : "#f59e0b";
    const fillColor = isCritical ? "#fb7185" : "#fbbf24";

    const circle = L.circle([area.lat, area.lon], {
      radius: isCritical ? 750 : 550,
      color: color,
      weight: 2.5,
      fillColor: fillColor,
      fillOpacity: isCritical ? 0.35 : 0.22
    });

    const popupHtml = `
      <div style="font-family:'Plus Jakarta Sans',sans-serif; min-width: 210px; padding: 4px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 4px;">
          <span style="font-size:11px; font-weight:bold; color:${isCritical ? '#fb7185' : '#fbbf24'}; background:${isCritical ? 'rgba(251,113,133,0.15)' : 'rgba(251,191,36,0.15)'}; padding:2px 6px; border-radius:4px;">
            ${area.tier}
          </span>
          <span style="font-size:11px; font-weight:bold; color:#38bdf8;">Priority #${area.rank}</span>
        </div>
        <div style="font-size:13px; font-weight:bold; color:#ffffff; margin-bottom: 2px;">
          ${area.name}
        </div>
        <div style="font-size:11px; color:#94a3b8; margin-bottom: 6px;">
          ${area.ps} &bull; ${area.atms} ATMs
        </div>
        <button onclick="selectAreaByName('${area.name}')" style="width:100%; padding: 6px; font-size:11px; font-weight:bold; background:#0284c7; color:#ffffff; border:none; border-radius:6px; cursor:pointer;">
          View Full Details &rarr;
        </button>
      </div>
    `;

    circle.bindPopup(popupHtml);
    circle.on("click", () => inspectArea(area));
    mapMarkersGroup.addLayer(circle);
  });
}

// 2. Inspect Area in Detail Card
function inspectArea(area) {
  selectedArea = area;

  const nameEl = document.getElementById("detail-area-name");
  const psEl = document.getElementById("detail-ps");
  const rankEl = document.getElementById("detail-rank");
  const tierEl = document.getElementById("detail-tier-badge");
  const probEl = document.getElementById("detail-prob");
  const atmsEl = document.getElementById("detail-atms");
  const hoursEl = document.getElementById("detail-hours");
  const whyEl = document.getElementById("detail-why");
  const actionEl = document.getElementById("detail-action");

  if (nameEl) nameEl.innerText = area.name;
  if (psEl) psEl.innerText = `Police Station: ${area.ps}`;
  if (rankEl) rankEl.innerText = `Priority #${area.rank}`;
  if (probEl) probEl.innerText = area.prob;
  if (atmsEl) atmsEl.innerText = `${area.atms} ATMs`;
  if (hoursEl) hoursEl.innerText = area.hours;
  if (whyEl) whyEl.innerText = area.why;
  if (actionEl) actionEl.innerText = area.action;

  if (tierEl) {
    const isCrit = area.tier === "HIGH RISK";
    tierEl.innerText = isCrit ? "HIGH RISK AREA" : "MODERATE RISK";
    tierEl.className = isCrit
      ? "px-3 py-1 rounded-full text-xs font-bold uppercase bg-rose-500/15 border border-rose-500/30 text-rose-300"
      : "px-3 py-1 rounded-full text-xs font-bold uppercase bg-amber-500/15 border border-amber-500/30 text-amber-300";
  }
}

function selectAreaByName(name) {
  const match = DELHI_AREAS.find(a => a.name.toLowerCase().includes(name.toLowerCase()));
  if (match) {
    inspectArea(match);
    focusArea(match.name);
  }
}

function focusArea(name) {
  const match = DELHI_AREAS.find(a => a.name.toLowerCase().includes(name.toLowerCase()));
  if (match && mapInstance) {
    inspectArea(match);
    mapInstance.setView([match.lat, match.lon], 14);
    showToast(`Focused on ${match.name}`);
    const mapSec = document.getElementById("map-section");
    if (mapSec) mapSec.scrollIntoView({ behavior: "smooth" });
  }
}

function resetMap() {
  if (mapInstance) {
    mapInstance.setView([28.585, 77.235], 12);
    showToast("Map reset to Delhi NCR overview");
  }
}

// 3. Hero Search Functionality
function setupHeroSearch() {
  const input = document.getElementById("hero-search");
  if (!input) return;

  input.addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
      searchAndHighlight();
    }
  });
}

function searchAndHighlight() {
  const val = (document.getElementById("hero-search")?.value || "").toLowerCase().trim();
  if (!val) {
    showToast("Please type an area name (e.g. Nehru Place, Connaught Place)");
    return;
  }

  const match = DELHI_AREAS.find(a => 
    a.name.toLowerCase().includes(val) || 
    a.ps.toLowerCase().includes(val) ||
    a.why.toLowerCase().includes(val)
  );

  if (match) {
    focusArea(match.name);
  } else {
    showToast(`No exact match for "${val}". Showing nearest monitored sector: Nehru Place`);
    focusArea("Nehru Place");
  }
}

function quickJumpSearch(name) {
  const input = document.getElementById("hero-search");
  if (input) input.value = name;
  focusArea(name);
}

// 4. Copy Police / Citizen Notice
function copyPatrolDirective() {
  if (!selectedArea) return;
  const text = `🚨 CYBERWATCH DELHI - ATM FRAUD RISK ALERT 🚨
Area: ${selectedArea.name}
Police Jurisdiction: ${selectedArea.ps}
Total ATMs in Sector: ${selectedArea.atms}
Risk Level: ${selectedArea.tier} (${selectedArea.prob} probability of mule withdrawal)
Peak Attack Window: ${selectedArea.hours}
Action Protocol: ${selectedArea.action}
Helpline: Call 1930 immediately to freeze fraudulent beneficiary accounts.`;

  navigator.clipboard.writeText(text).then(() => {
    showToast(`Copied Patrol Alert for ${selectedArea.name}`);
  }).catch(() => {
    showToast("Unable to copy to clipboard.");
  });
}

// 5. High-Risk Directory Table
function initTable() {
  renderTable();

  const searchInput = document.getElementById("table-search");
  if (searchInput) {
    searchInput.addEventListener("input", (e) => {
      renderTable(e.target.value.toLowerCase().trim());
    });
  }
}

function renderTable(query = "") {
  const tbody = document.getElementById("hotspots-tbody");
  if (!tbody) return;

  tbody.innerHTML = "";

  const rows = DELHI_AREAS.filter(area => {
    if (currentFilter === "CRITICAL" && area.tier !== "HIGH RISK") return false;
    if (query) {
      return area.name.toLowerCase().includes(query) || 
             area.ps.toLowerCase().includes(query) ||
             area.why.toLowerCase().includes(query);
    }
    return true;
  });

  if (rows.length === 0) {
    tbody.innerHTML = `
      <tr>
        <td colspan="7" class="text-center py-6 text-slate-500 text-xs">
          No matching areas found. Try searching for "Nehru", "Connaught", or "Saket".
        </td>
      </tr>
    `;
    return;
  }

  rows.forEach(area => {
    const isCrit = area.tier === "HIGH RISK";
    const tr = document.createElement("tr");
    tr.className = "hover:bg-slate-800/50 transition-colors";

    tr.innerHTML = `
      <td class="py-3 px-4 font-mono font-bold ${area.rank <= 3 ? 'text-rose-400' : 'text-slate-300'}">
        #${area.rank}
      </td>
      <td class="py-3 px-4 font-bold text-white">
        ${area.name}
      </td>
      <td class="py-3 px-4 text-sky-400 font-medium">
        ${area.ps}
      </td>
      <td class="py-3 px-4 text-slate-200">
        ${area.atms} ATMs
      </td>
      <td class="py-3 px-4">
        <span class="px-2.5 py-0.5 rounded-full text-[10px] font-bold uppercase ${isCrit ? 'bg-rose-500/15 border border-rose-500/30 text-rose-300' : 'bg-amber-500/15 border border-amber-500/30 text-amber-300'}">
          ${area.tier}
        </span>
      </td>
      <td class="py-3 px-4 text-amber-300 text-xs font-medium">
        ${area.hours.split('(')[0]}
      </td>
      <td class="py-3 px-4 text-right">
        <button onclick="focusArea('${area.name}')" class="px-2.5 py-1 text-xs font-bold rounded-lg bg-sky-500/10 hover:bg-sky-500/20 text-sky-300 border border-sky-500/30 transition-all">
          View on Map &rarr;
        </button>
      </td>
    `;
    tbody.appendChild(tr);
  });
}

function setupFilterChips() {
  const chips = document.querySelectorAll(".filter-chip");
  chips.forEach(chip => {
    chip.addEventListener("click", () => {
      chips.forEach(c => {
        c.className = "filter-chip px-3.5 py-1.5 rounded-lg font-semibold bg-slate-900 border border-slate-800 text-slate-400 hover:text-white text-xs transition-all";
      });
      chip.className = "filter-chip px-3.5 py-1.5 rounded-lg font-bold bg-sky-500/20 border border-sky-500 text-sky-300 text-xs transition-all active";
      currentFilter = chip.getAttribute("data-filter");
      renderTable();
    });
  });
}

// 6. 1930 Fraud Calculator Simulator
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
    else if (category.includes("Skimming")) baseDelay = 1.0;
    else if (category.includes("Investment")) baseDelay = 5.0;

    const remainingDelay = Math.max(0.5, (baseDelay - timeElapsedHours + (Math.random() * 0.4 - 0.2))).toFixed(1);

    const candidates = [
      { name: "Nehru Place Hub", ps: "PS Kalkaji / Nehru Place" },
      { name: "Connaught Place", ps: "PS Connaught Place" },
      { name: "Saket Centre", ps: "PS Saket" },
      { name: "Lajpat Nagar", ps: "PS Lajpat Nagar" }
    ];
    const topCandidate = candidates[Math.floor(Math.random() * candidates.length)];

    const now = new Date();
    const estArrival = new Date(now.getTime() + remainingDelay * 3600 * 1000);
    const arrivalStr = estArrival.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

    const titleEl = document.getElementById("sim-alert-title");
    const descEl = document.getElementById("sim-alert-desc");
    const winEl = document.getElementById("sm-window");
    const hubEl = document.getElementById("sm-hub");
    const urgEl = document.getElementById("sm-urgency");

    if (titleEl) titleEl.innerText = `Target Predicted: ${topCandidate.name}`;
    if (descEl) {
      descEl.innerHTML = `
        Incident assessed: <strong>${category}</strong> (Stolen: <strong>&#8377;${loss.toLocaleString()}</strong>).<br>
        Cash withdrawal predicted around <strong>${arrivalStr} IST</strong> in <strong>${topCandidate.ps}</strong> area.
      `;
    }

    if (winEl) winEl.innerText = `~${remainingDelay} Hours`;
    if (hubEl) hubEl.innerText = topCandidate.name;
    if (urgEl) urgEl.innerText = remainingDelay < 2 ? "Call 1930 Now" : "Urgent Action";

    showToast(`Prediction calculated: ${topCandidate.name} (~${remainingDelay}h)`);
  });
}

// 7. Toast Notification Engine
function showToast(message) {
  const container = document.getElementById("toast-container");
  if (!container) return;

  const toast = document.createElement("div");
  toast.className = "flex items-center gap-2.5 px-4 py-2.5 rounded-xl bg-slate-900 border border-sky-500/50 text-white text-xs font-semibold shadow-2xl backdrop-blur-md pointer-events-auto transition-all duration-300";
  toast.innerHTML = `
    <i data-lucide="check-circle" class="w-4 h-4 text-sky-400"></i>
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
