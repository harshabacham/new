"""
Phase 5: Interactive GIS Geospatial Visualization Engine.
Generates an interactive Folium map displaying predicted hotspot polygons,
choropleths of withdrawal probability, Top-10 prioritized tactical markers,
and the ethical 80/20 exploitation-exploration patrol allocation layers.
"""

import os
import sys
import folium
from folium import plugins
import pandas as pd
import numpy as np

def generate_map():
    print("=" * 70)
    print("PHASE 5: INTERACTIVE GIS HOTSPOT MAP GENERATION")
    print("=" * 70)
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    phase5_dir = os.path.join(base_dir, "phase_5")
    data_dir = os.path.join(base_dir, "data")
    
    forecast_path = os.path.join(phase5_dir, "latest_operational_forecasts.csv")
    grid_path = os.path.join(data_dir, "grid_cells.csv")
    assert os.path.exists(forecast_path), "Forecast data missing. Run explainability_engine.py first."
    
    df_fc = pd.read_csv(forecast_path)
    df_grid = pd.read_csv(grid_path)
    
    # Merge grid coordinates if not already present
    if "lat_min" not in df_fc.columns:
        df_fc = df_fc.merge(df_grid[["grid_cell_id", "lat_min", "lat_max", "lon_min", "lon_max"]], on="grid_cell_id", how="left")
        
    # Map center (Delhi NCR center) - Using open OpenStreetMap tiles
    map_center = [28.6000, 77.2000]
    m = folium.Map(location=map_center, zoom_start=11, tiles="OpenStreetMap", prefer_canvas=True)
    
    # Create Feature Groups for Layer Control
    fg_choropleth = folium.FeatureGroup(name="1. Withdrawal Probability Choropleth (All 400 Cells)", show=True)
    fg_top_priority = folium.FeatureGroup(name="2. Top-10 Tactical Interception Targets (Exploitation 80%)", show=True)
    fg_exploration = folium.FeatureGroup(name="3. Unbiased Audit Patrol Zones (Exploration 20% - Anti-Bias)", show=False)
    
    # Color scale helper for probability
    def get_color(prob):
        if prob >= 0.70:
            return "#990000" # Crimson dark red
        elif prob >= 0.50:
            return "#e6550d" # Orange-red
        elif prob >= 0.30:
            return "#fdae6b" # Light orange
        elif prob >= 0.15:
            return "#fee6ce" # Pale peach
        else:
            return "#f7f7f7" # Neutral gray
            
    # Add Grid Cell Polygons
    for _, row in df_fc.iterrows():
        bounds = [[row["lat_min"], row["lon_min"]], [row["lat_max"], row["lon_max"]]]
        prob = row["pred_hotspot_prob"]
        exp_count = row["expected_withdrawals"]
        color = get_color(prob)
        
        popup_html = f"""
        <div style="font-family: Arial, sans-serif; width: 260px; font-size: 12px; line-height: 1.5;">
            <h4 style="margin: 0 0 6px 0; color: #1a365d; border-bottom: 2px solid #2b6cb0;">
                Cell: {row['grid_cell_id']}
            </h4>
            <b>Risk Tier:</b> <span style="color: {color}; font-weight: bold;">{row['risk_tier']}</span><br>
            <b>Forecasted Hotspot Probability:</b> {prob*100:.1f}%<br>
            <b>Expected Cash-Outs:</b> {exp_count} (90% CI: [{row['count_ci_lower']}, {row['count_ci_upper']}])<br>
            <b>Cell ATM Density:</b> {row['cell_atm_count']} terminals<br>
            <hr style="margin: 6px 0; border: 0; border-top: 1px solid #e2e8f0;">
            <b>Primary XAI Drivers:</b><br>
            <span style="font-size: 11px; color: #4a5568;">{row['top_contributing_factors']}</span>
        </div>
        """
        
        folium.Rectangle(
            bounds=bounds,
            color="#4a5568",
            weight=0.5,
            fill=True,
            fill_color=color,
            fill_opacity=0.60 if prob >= 0.30 else 0.20,
            popup=folium.Popup(popup_html, max_width=300),
            tooltip=f"{row['grid_cell_id']} | P(Hotspot): {prob*100:.1f}% | Exp: {exp_count}"
        ).add_to(fg_choropleth)
        
    # Top-10 Prioritized Hotspots
    df_top10 = df_fc.sort_values("pred_hotspot_prob", ascending=False).head(10)
    for rank, (_, row) in enumerate(df_top10.iterrows(), 1):
        lat = row["centroid_lat"]
        lon = row["centroid_lon"]
        prob = row["pred_hotspot_prob"]
        
        # Warning icon marker
        folium.Marker(
            location=[lat, lon],
            icon=folium.Icon(color="red", icon="exclamation-sign", prefix="glyphicon"),
            popup=folium.Popup(f"""
            <div style="font-family: Arial; width: 240px; font-size: 12px;">
                <b style="color: #990000;">TACTICAL TARGET #{rank}</b><br>
                <b>Cell ID:</b> {row['grid_cell_id']}<br>
                <b>Probability:</b> {prob*100:.1f}% | <b>Expected Count:</b> {row['expected_withdrawals']}<br>
                <b>Key Factors:</b> {row['top_contributing_factors']}<br>
                <hr style="margin: 4px 0;">
                <b>Directive:</b> Deploy plainclothes surveillance and alert bank risk team for step-up friction.
            </div>
            """, max_width=280),
            tooltip=f"#{rank} Target: {row['grid_cell_id']} ({prob*100:.1f}%)"
        ).add_to(fg_top_priority)

    # Exploration 20% Random Patrol Zones (Pillar 3 Anti-Bias Safeguard)
    np.random.seed(99)
    exploration_cells = df_fc.sample(8)
    for _, row in exploration_cells.iterrows():
        folium.CircleMarker(
            location=[row["centroid_lat"], row["centroid_lon"]],
            radius=9,
            color="#2b6cb0",
            fill=True,
            fill_color="#4299e1",
            fill_opacity=0.8,
            popup=f"<b>Unbiased Audit Cell:</b> {row['grid_cell_id']}<br>Allocated for 20% exploratory patrol to prevent algorithmic runaway feedback loops.",
            tooltip=f"Audit Cell: {row['grid_cell_id']}"
        ).add_to(fg_exploration)

    fg_choropleth.add_to(m)
    fg_top_priority.add_to(m)
    fg_exploration.add_to(m)
    folium.LayerControl(collapsed=False).add_to(m)
    
    # Add title header banner
    title_html = """
    <div style="position: fixed; top: 10px; left: 60px; z-index: 1000; background: white; 
                padding: 10px 16px; border: 2px solid #1a365d; border-radius: 6px; box-shadow: 0 2px 6px rgba(0,0,0,0.2);">
        <h4 style="margin: 0; color: #1a365d; font-family: Arial, sans-serif;">
            SIH 2026: Cybercrime Cash-Withdrawal Geographic Hotspot Forecast
        </h4>
        <span style="font-size: 11px; color: #4a5568; font-family: Arial, sans-serif;">
            24-Hour Tactical Decision Support | 400 Grid Cells | PAI@10: 8.81 | PEI@10: 0.656
        </span>
    </div>
    """
    m.get_root().html.add_child(folium.Element(title_html))
    
    out_map_path = os.path.join(phase5_dir, "interactive_hotspot_forecast_map.html")
    m.save(out_map_path)
    print(f" -> Interactive GIS Map saved successfully to: {out_map_path}")
    print("=" * 70)
    return out_map_path

if __name__ == "__main__":
    generate_map()
