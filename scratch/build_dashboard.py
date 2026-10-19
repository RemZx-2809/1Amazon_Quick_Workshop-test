import json
import os

with open(r'e:\1Amazon_Quick_Workshop test\scratch\raw_sales.json', 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

raw_data_json = json.dumps(raw_data, ensure_ascii=False)

html_content = f'''<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ระบบวิเคราะห์ข้อมูลการขายอัจฉริยะ | Amazon Quick Workshop</title>
  <style>
    :root {{
      --primary-blue: #1d4ed8;
      --primary-blue-hover: #1e40af;
      --primary-blue-light: #eff6ff;
      --primary-orange: #ea580c;
      --primary-orange-hover: #c2410c;
      --primary-orange-light: #fff7ed;
      --accent-cyan: #0284c7;
      --accent-emerald: #059669;
      --accent-amber: #d97706;
      --accent-rose: #e11d48;
      
      --bg-page: #f8fafc;
      --bg-card: #ffffff;
      --bg-card-subtle: #f1f5f9;
      --bg-input: #ffffff;
      --border-color: #e2e8f0;
      --border-focus: #3b82f6;
      --text-main: #0f172a;
      --text-muted: #64748b;
      --text-subtle: #94a3b8;
      --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
      --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
      --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
      --radius-sm: 6px;
      --radius-md: 10px;
      --radius-lg: 16px;
      --font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Sarabun", "Prompt", sans-serif;
    }}

    [data-theme="dark"] {{
      --primary-blue: #3b82f6;
      --primary-blue-hover: #60a5fa;
      --primary-blue-light: #1e293b;
      --primary-orange: #f97316;
      --primary-orange-hover: #fb923c;
      --primary-orange-light: #2c1e15;
      
      --bg-page: #0b0f19;
      --bg-card: #131c2e;
      --bg-card-subtle: #1e293b;
      --bg-input: #1e293b;
      --border-color: #2e3c54;
      --border-focus: #60a5fa;
      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
      --text-subtle: #64748b;
      --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.5);
      --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.4);
      --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.5);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: var(--font-family);
      background-color: var(--bg-page);
      color: var(--text-main);
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
      padding-bottom: 50px;
      transition: background-color 0.25s ease, color 0.25s ease;
    }}

    .container {{
      max-width: 1400px;
      margin: 0 auto;
      padding: 0 20px;
    }}

    /* Top Notice Banner */
    .edu-banner {{
      background: linear-gradient(90deg, #1e3a8a, #ea580c);
      color: #ffffff;
      text-align: center;
      padding: 7px 14px;
      font-size: 0.85rem;
      font-weight: 600;
      letter-spacing: 0.5px;
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 10px;
    }}
    .edu-banner span.badge {{
      background: rgba(255, 255, 255, 0.2);
      padding: 2px 8px;
      border-radius: 999px;
      font-size: 0.75rem;
    }}

    /* Header */
    header {{
      background-color: var(--bg-card);
      border-bottom: 1px solid var(--border-color);
      padding: 18px 0;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: var(--shadow-sm);
    }}
    .header-inner {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
    }}
    .brand {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .brand-icon {{
      width: 44px;
      height: 44px;
      border-radius: var(--radius-md);
      background: linear-gradient(135deg, var(--primary-blue), var(--primary-orange));
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-weight: 800;
      font-size: 1.4rem;
      box-shadow: var(--shadow-sm);
    }}
    .brand-info h1 {{
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .brand-info p {{
      font-size: 0.82rem;
      color: var(--text-muted);
    }}
    .header-actions {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }}

    /* Buttons */
    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 14px;
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      border: 1px solid transparent;
      transition: all 0.2s ease;
      font-family: inherit;
    }}
    .btn-primary {{
      background-color: var(--primary-blue);
      color: white;
    }}
    .btn-primary:hover {{
      background-color: var(--primary-blue-hover);
    }}
    .btn-orange {{
      background-color: var(--primary-orange);
      color: white;
    }}
    .btn-orange:hover {{
      background-color: var(--primary-orange-hover);
    }}
    .btn-outline {{
      background-color: transparent;
      border-color: var(--border-color);
      color: var(--text-main);
    }}
    .btn-outline:hover {{
      background-color: var(--bg-card-subtle);
      border-color: var(--text-muted);
    }}
    .btn-sm {{
      padding: 4px 9px;
      font-size: 0.78rem;
    }}
    .btn-audit {{
      background: rgba(5, 150, 105, 0.1);
      color: var(--accent-emerald);
      border-color: rgba(5, 150, 105, 0.25);
    }}
    .btn-audit:hover {{
      background: rgba(5, 150, 105, 0.2);
    }}

    /* Filter Panel */
    .filter-section {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 16px 20px;
      margin: 20px 0;
      box-shadow: var(--shadow-sm);
    }}
    .filter-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
      flex-wrap: wrap;
      gap: 10px;
    }}
    .filter-title {{
      font-size: 0.95rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 8px;
      color: var(--text-main);
    }}
    .filter-stats {{
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--primary-blue);
      background: var(--primary-blue-light);
      padding: 4px 10px;
      border-radius: 999px;
      border: 1px solid rgba(59, 130, 246, 0.2);
    }}
    .filter-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 16px;
    }}
    .filter-group {{
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}
    .filter-label {{
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .filter-quick-btns {{
      display: flex;
      gap: 4px;
    }}
    .filter-pills {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }}
    .pill-checkbox {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 5px 10px;
      border-radius: var(--radius-sm);
      font-size: 0.82rem;
      background: var(--bg-card-subtle);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      cursor: pointer;
      user-select: none;
      transition: all 0.15s ease;
    }}
    .pill-checkbox:hover {{
      border-color: var(--primary-blue);
    }}
    .pill-checkbox input {{
      accent-color: var(--primary-blue);
      cursor: pointer;
    }}
    .pill-checkbox.active {{
      background: var(--primary-blue-light);
      border-color: var(--primary-blue);
      color: var(--primary-blue);
      font-weight: 600;
    }}
    .date-inputs {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .date-inputs input[type="date"] {{
      background: var(--bg-input);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 6px 10px;
      border-radius: var(--radius-sm);
      font-family: inherit;
      font-size: 0.82rem;
      flex: 1;
    }}
    .date-presets {{
      display: flex;
      flex-wrap: wrap;
      gap: 4px;
      margin-top: 4px;
    }}
    .date-preset-btn {{
      background: transparent;
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      padding: 2px 7px;
      font-size: 0.72rem;
      border-radius: 4px;
      cursor: pointer;
    }}
    .date-preset-btn:hover {{
      border-color: var(--primary-blue);
      color: var(--primary-blue);
    }}

    /* Active filter badges bar */
    .active-filters-bar {{
      margin-top: 14px;
      padding-top: 12px;
      border-top: 1px dashed var(--border-color);
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 6px;
      font-size: 0.8rem;
    }}
    .active-filter-tag {{
      background: var(--primary-orange-light);
      color: var(--primary-orange);
      border: 1px solid rgba(234, 88, 12, 0.3);
      padding: 3px 8px;
      border-radius: 4px;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      font-weight: 600;
    }}
    .active-filter-tag span.close {{
      cursor: pointer;
      font-weight: bold;
    }}
    .active-filter-tag span.close:hover {{
      color: var(--accent-rose);
    }}

    /* Metric Switcher Controls */
    .metric-control-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin: 15px 0 20px 0;
      flex-wrap: wrap;
      gap: 12px;
    }}
    .metric-switch {{
      display: inline-flex;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 3px;
      box-shadow: var(--shadow-sm);
    }}
    .metric-btn {{
      padding: 7px 16px;
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
      font-weight: 600;
      background: transparent;
      border: none;
      color: var(--text-muted);
      cursor: pointer;
      font-family: inherit;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .metric-btn.active {{
      background: var(--primary-blue);
      color: #ffffff;
      box-shadow: var(--shadow-sm);
    }}

    /* Tabs Bar */
    .tabs-nav {{
      display: flex;
      gap: 6px;
      border-bottom: 2px solid var(--border-color);
      margin-bottom: 24px;
      overflow-x: auto;
      padding-bottom: 2px;
    }}
    .tab-btn {{
      padding: 10px 18px;
      background: transparent;
      border: none;
      border-bottom: 3px solid transparent;
      color: var(--text-muted);
      font-weight: 600;
      font-size: 0.92rem;
      cursor: pointer;
      font-family: inherit;
      white-space: nowrap;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: -2px;
    }}
    .tab-btn:hover {{
      color: var(--primary-blue);
    }}
    .tab-btn.active {{
      color: var(--primary-blue);
      border-bottom-color: var(--primary-blue);
      font-weight: 700;
    }}

    /* Tab Content panels */
    .tab-content {{
      display: none;
    }}
    .tab-content.active {{
      display: block;
      animation: fadeIn 0.25s ease-out;
    }}
    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(4px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* KPI Cards Grid */
    .kpi-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 16px;
      margin-bottom: 24px;
    }}
    .kpi-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 18px 20px;
      box-shadow: var(--shadow-sm);
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }}
    .kpi-card:hover {{
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
    }}
    .kpi-card::before {{
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4px;
      background: var(--card-accent, var(--primary-blue));
    }}
    .kpi-title {{
      font-size: 0.82rem;
      font-weight: 600;
      color: var(--text-muted);
      margin-bottom: 8px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .kpi-value {{
      font-size: 1.65rem;
      font-weight: 800;
      color: var(--text-main);
      letter-spacing: -0.5px;
    }}
    .kpi-subtext {{
      font-size: 0.76rem;
      color: var(--text-subtle);
      margin-top: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .kpi-badge {{
      display: inline-block;
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 0.72rem;
      font-weight: 700;
    }}
    .badge-success {{
      background: rgba(5, 150, 105, 0.15);
      color: var(--accent-emerald);
    }}
    .badge-orange {{
      background: var(--primary-orange-light);
      color: var(--primary-orange);
    }}
    .badge-blue {{
      background: var(--primary-blue-light);
      color: var(--primary-blue);
    }}

    /* Card Panels */
    .card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 22px;
      box-shadow: var(--shadow-sm);
      margin-bottom: 24px;
    }}
    .card-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 18px;
      flex-wrap: wrap;
      gap: 12px;
    }}
    .card-title {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .card-subtitle {{
      font-size: 0.82rem;
      color: var(--text-muted);
      margin-top: 2px;
    }}

    /* Two column grid */
    .grid-2 {{
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 24px;
      margin-bottom: 24px;
    }}
    @media (max-width: 1024px) {{
      .grid-2 {{
        grid-template-columns: 1fr;
      }}
    }}

    /* Tables */
    .table-container {{
      width: 100%;
      overflow-x: auto;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      background: var(--bg-card);
    }}
    table.data-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.86rem;
      text-align: left;
    }}
    table.data-table th {{
      background: var(--bg-card-subtle);
      color: var(--text-muted);
      font-weight: 700;
      padding: 10px 14px;
      border-bottom: 1px solid var(--border-color);
      cursor: pointer;
      user-select: none;
      white-space: nowrap;
    }}
    table.data-table th:hover {{
      color: var(--primary-blue);
    }}
    table.data-table th.sorted-asc::after {{
      content: " ↑";
      color: var(--primary-blue);
    }}
    table.data-table th.sorted-desc::after {{
      content: " ↓";
      color: var(--primary-blue);
    }}
    table.data-table td {{
      padding: 10px 14px;
      border-bottom: 1px solid var(--border-color);
      color: var(--text-main);
    }}
    table.data-table tr:hover td {{
      background-color: var(--bg-card-subtle);
    }}
    table.data-table tr.selected td {{
      background-color: var(--primary-blue-light);
      font-weight: 600;
    }}
    table.data-table tr.total-row td {{
      background-color: var(--bg-card-subtle);
      font-weight: 800;
      border-top: 2px solid var(--border-color);
      border-bottom: 2px solid var(--border-color);
    }}
    .text-right {{
      text-align: right;
    }}
    .text-center {{
      text-align: center;
    }}

    /* Progress bar in table */
    .share-bar-container {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .share-bar-outer {{
      flex: 1;
      height: 7px;
      background: var(--bg-card-subtle);
      border-radius: 999px;
      overflow: hidden;
      min-width: 50px;
    }}
    .share-bar-inner {{
      height: 100%;
      border-radius: 999px;
      background: linear-gradient(90deg, var(--primary-blue), var(--primary-orange));
    }}

    /* SVG Chart Containers */
    .chart-container {{
      width: 100%;
      position: relative;
    }}
    svg.interactive-svg {{
      width: 100%;
      height: auto;
      display: block;
    }}

    /* SVG Elements Styling */
    .svg-grid-line {{
      stroke: var(--border-color);
      stroke-dasharray: 4, 4;
      stroke-width: 1;
    }}
    .svg-axis-line {{
      stroke: var(--border-color);
      stroke-width: 1.5;
    }}
    .svg-axis-text {{
      fill: var(--text-muted);
      font-size: 11px;
      font-family: var(--font-family);
    }}
    .svg-axis-title {{
      fill: var(--text-main);
      font-size: 12px;
      font-weight: 700;
      font-family: var(--font-family);
    }}
    .chart-tooltip {{
      position: absolute;
      background: rgba(15, 23, 42, 0.92);
      color: #ffffff;
      padding: 8px 12px;
      border-radius: 6px;
      font-size: 0.78rem;
      pointer-events: none;
      z-index: 1000;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
      border: 1px solid rgba(255, 255, 255, 0.15);
      backdrop-filter: blur(4px);
      display: none;
      line-height: 1.4;
      white-space: nowrap;
    }}

    /* Insights Box */
    .insights-card {{
      background: linear-gradient(135deg, rgba(30, 58, 138, 0.04), rgba(234, 88, 12, 0.06));
      border: 1px solid rgba(59, 130, 246, 0.25);
      border-radius: var(--radius-lg);
      padding: 20px;
      margin-bottom: 24px;
    }}
    .insights-header {{
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--primary-blue);
      margin-bottom: 14px;
    }}
    .insights-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 14px;
    }}
    .insight-item {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 12px 16px;
      display: flex;
      gap: 12px;
      align-items: flex-start;
      box-shadow: var(--shadow-sm);
    }}
    .insight-icon {{
      font-size: 1.3rem;
      line-height: 1;
    }}
    .insight-text {{
      font-size: 0.85rem;
      color: var(--text-main);
    }}
    .insight-text strong {{
      color: var(--primary-orange);
    }}

    /* Heatmap styling */
    .heatmap-grid {{
      display: grid;
      gap: 4px;
      margin-top: 15px;
    }}
    .heatmap-cell {{
      padding: 12px 8px;
      border-radius: 4px;
      text-align: center;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      transition: transform 0.15s ease, filter 0.15s ease;
      position: relative;
    }}
    .heatmap-cell:hover {{
      transform: scale(1.04);
      filter: brightness(1.1);
      z-index: 2;
      box-shadow: var(--shadow-md);
    }}

    /* Calendar Heatmap */
    .calendar-wrapper {{
      display: flex;
      flex-direction: column;
      gap: 8px;
      margin-top: 10px;
    }}
    .calendar-days-header {{
      display: grid;
      grid-template-columns: repeat(7, 1fr);
      gap: 6px;
      text-align: center;
      font-size: 0.76rem;
      font-weight: 700;
      color: var(--text-muted);
    }}
    .calendar-grid {{
      display: grid;
      grid-template-columns: repeat(7, 1fr);
      gap: 6px;
    }}
    .cal-day-cell {{
      aspect-ratio: 1;
      border-radius: 6px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 6px;
      font-size: 0.74rem;
      cursor: pointer;
      border: 1px solid var(--border-color);
      transition: all 0.15s ease;
    }}
    .cal-day-cell:hover {{
      transform: translateY(-2px);
      box-shadow: var(--shadow-sm);
      border-color: var(--primary-blue);
    }}
    .cal-day-cell.empty {{
      background: transparent;
      border-color: transparent;
      cursor: default;
    }}

    /* Modals */
    .modal-overlay {{
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.6);
      backdrop-filter: blur(4px);
      z-index: 9999;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }}
    .modal-overlay.active {{
      display: flex;
      animation: fadeIn 0.2s ease-out;
    }}
    .modal-box {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      max-width: 800px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      padding: 24px;
      box-shadow: var(--shadow-lg);
    }}
    .modal-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 18px;
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 12px;
    }}
    .modal-close {{
      background: transparent;
      border: none;
      font-size: 1.5rem;
      color: var(--text-muted);
      cursor: pointer;
      line-height: 1;
    }}
    .modal-close:hover {{
      color: var(--text-main);
    }}

    /* Search & Pagination */
    .table-controls {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
      flex-wrap: wrap;
      gap: 10px;
    }}
    .search-box {{
      position: relative;
      min-width: 260px;
    }}
    .search-box input {{
      width: 100%;
      background: var(--bg-input);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 8px 12px 8px 32px;
      border-radius: var(--radius-sm);
      font-family: inherit;
      font-size: 0.85rem;
    }}
    .search-box::before {{
      content: "🔍";
      position: absolute;
      left: 10px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 0.8rem;
      opacity: 0.5;
    }}
    .pagination-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 14px;
      flex-wrap: wrap;
      gap: 10px;
      font-size: 0.84rem;
      color: var(--text-muted);
    }}
    .page-nav {{
      display: flex;
      gap: 4px;
      align-items: center;
    }}
    .page-nav button {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 4px 10px;
      border-radius: 4px;
      cursor: pointer;
      font-family: inherit;
      font-size: 0.82rem;
    }}
    .page-nav button:hover:not(:disabled) {{
      border-color: var(--primary-blue);
      color: var(--primary-blue);
    }}
    .page-nav button:disabled {{
      opacity: 0.4;
      cursor: not-allowed;
    }}
    .page-nav button.active {{
      background: var(--primary-blue);
      color: #ffffff;
      border-color: var(--primary-blue);
    }}

    /* What-If Simulation Box */
    .simulator-box {{
      background: var(--bg-card);
      border: 2px dashed var(--primary-orange);
      border-radius: var(--radius-lg);
      padding: 20px;
      margin-bottom: 24px;
    }}
    .slider-group {{
      display: flex;
      flex-direction: column;
      gap: 6px;
      margin-bottom: 16px;
    }}
    .slider-header {{
      display: flex;
      justify-content: space-between;
      font-size: 0.85rem;
      font-weight: 600;
    }}
    input[type="range"] {{
      width: 100%;
      accent-color: var(--primary-orange);
      cursor: pointer;
    }}

    /* Footer */
    footer {{
      margin-top: 40px;
      border-top: 1px solid var(--border-color);
      padding: 24px 0;
      text-align: center;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}
    .footer-highlight {{
      font-weight: 700;
      color: var(--primary-orange);
      margin-bottom: 4px;
    }}

    /* Print Styles */
    @media print {{
      body {{
        background: #ffffff !important;
        color: #000000 !important;
        font-size: 10pt;
      }}
      header, .filter-section, .metric-control-bar, .tabs-nav, .search-box, .pagination-bar, .btn, .simulator-box, .active-filters-bar {{
        display: none !important;
      }}
      .tab-content {{
        display: block !important;
        page-break-after: always;
      }}
      .card, .kpi-card {{
        border: 1px solid #ccc !important;
        box-shadow: none !important;
        background: #fff !important;
        page-break-inside: avoid;
      }}
      .edu-banner {{
        background: #eee !important;
        color: #000 !important;
      }}
    }}
  </style>
</head>
<body>

  <!-- Top Educational Notice Banner -->
  <div class="edu-banner">
    <span>⚠️ <strong>ข้อมูลจำลองเพื่อการเรียนรู้ (Simulated Data for Educational Purpose)</strong></span>
    <span class="badge">Amazon Quick Workshop</span>
  </div>

  <!-- Header -->
  <header>
    <div class="container header-inner">
      <div class="brand">
        <div class="brand-icon">☕</div>
        <div class="brand-info">
          <h1>ระบบวิเคราะห์ข้อมูลการขายอัจฉริยะ <span style="font-size: 0.8rem; font-weight: 500; color: var(--primary-orange);">v3.0 Pro</span></h1>
          <p>แดชบอร์ดติดตามรายได้ กำไร และพฤติกรรมการขาย (ข้อมูลชีต Sales • 1–31 ส.ค. 2569)</p>
        </div>
      </div>
      <div class="header-actions">
        <button id="btnAuditReport" class="btn btn-audit btn-sm" title="ดูผลการตรวจความสมบูรณ์ของข้อมูล">
          🛡️ ตรวจข้อมูล: สมบูรณ์ 100%
        </button>
        <button id="btnThemeToggle" class="btn btn-outline btn-sm">
          🌙 สลับธีม
        </button>
        <button id="btnPrint" class="btn btn-outline btn-sm">
          🖨️ พิมพ์รายงาน
        </button>
        <button id="btnDownloadCSV" class="btn btn-orange btn-sm">
          📥 ดาวน์โหลด CSV
        </button>
      </div>
    </div>
  </header>

  <main class="container">

    <!-- Filter Section -->
    <section class="filter-section" id="filterSection">
      <div class="filter-header">
        <div class="filter-title">
          <span>🔍 ตัวกรองข้อมูลขั้นสูง (Interactive Multi-Select Filters)</span>
          <span id="filterRowCountBadge" class="filter-stats">กำลังแสดง 100 / 100 รายการ (100%)</span>
        </div>
        <div style="display: flex; gap: 8px;">
          <button id="btnResetFilters" class="btn btn-outline btn-sm">
            ↺ ล้างตัวกรองทั้งหมด
          </button>
        </div>
      </div>

      <div class="filter-grid">
        <!-- Branch Filter -->
        <div class="filter-group">
          <div class="filter-label">
            <span>สาขา (Branch)</span>
            <div class="filter-quick-btns">
              <button class="date-preset-btn" onclick="quickSelectFilter('branch', true)">ทั้งหมด</button>
              <button class="date-preset-btn" onclick="quickSelectFilter('branch', false)">ล้าง</button>
            </div>
          </div>
          <div class="filter-pills" id="branchFilterPills"></div>
        </div>

        <!-- Category Filter -->
        <div class="filter-group">
          <div class="filter-label">
            <span>หมวดหมู่ (Category)</span>
            <div class="filter-quick-btns">
              <button class="date-preset-btn" onclick="quickSelectFilter('category', true)">ทั้งหมด</button>
              <button class="date-preset-btn" onclick="quickSelectFilter('category', false)">ล้าง</button>
            </div>
          </div>
          <div class="filter-pills" id="categoryFilterPills"></div>
        </div>

        <!-- Day of Week Filter -->
        <div class="filter-group">
          <div class="filter-label">
            <span>วันในสัปดาห์ (Day)</span>
            <div class="filter-quick-btns">
              <button class="date-preset-btn" onclick="setDowPreset('all')">ทั้งหมด</button>
              <button class="date-preset-btn" onclick="setDowPreset('weekday')">จ.-ศ.</button>
              <button class="date-preset-btn" onclick="setDowPreset('weekend')">ส.-อา.</button>
            </div>
          </div>
          <div class="filter-pills" id="dowFilterPills"></div>
        </div>

        <!-- Date Range Filter -->
        <div class="filter-group">
          <div class="filter-label">
            <span>ช่วงวันที่ (Date Range)</span>
            <div class="filter-quick-btns">
              <button class="date-preset-btn" onclick="setDatePreset('all')">ทั้งเดือน</button>
            </div>
          </div>
          <div class="date-inputs">
            <input type="date" id="filterStartDate" min="2026-08-01" max="2026-08-31" value="2026-08-01">
            <span style="color: var(--text-muted); font-size: 0.8rem;">ถึง</span>
            <input type="date" id="filterEndDate" min="2026-08-01" max="2026-08-31" value="2026-08-31">
          </div>
          <div class="date-presets">
            <button class="date-preset-btn" onclick="setDatePreset('w1')">สัปดาห์ 1 (1-7)</button>
            <button class="date-preset-btn" onclick="setDatePreset('w2')">สัปดาห์ 2 (8-14)</button>
            <button class="date-preset-btn" onclick="setDatePreset('w3')">สัปดาห์ 3 (15-21)</button>
            <button class="date-preset-btn" onclick="setDatePreset('w4')">สัปดาห์ 4+ (22-31)</button>
          </div>
        </div>
      </div>

      <!-- Product Multi-select -->
      <div style="margin-top: 14px; border-top: 1px dashed var(--border-color); padding-top: 12px;">
        <div class="filter-label" style="margin-bottom: 8px;">
          <span>สินค้า (Product) - รวมทุกสาขาก่อนกรอง</span>
          <div class="filter-quick-btns">
            <button class="date-preset-btn" onclick="quickSelectFilter('product', true)">เลือกทั้ง 8 สินค้า</button>
            <button class="date-preset-btn" onclick="quickSelectFilter('product', false)">ล้าง</button>
          </div>
        </div>
        <div class="filter-pills" id="productFilterPills"></div>
      </div>

      <!-- Active Filters Tag Bar -->
      <div class="active-filters-bar" id="activeFiltersBar" style="display: none;">
        <span style="font-weight: 700; color: var(--text-muted);">ตัวกรองที่ใช้งาน:</span>
        <div id="activeFilterTags" style="display: flex; flex-wrap: wrap; gap: 6px;"></div>
      </div>
    </section>

    <!-- Global Metric Switcher & Navigation Controls -->
    <div class="metric-control-bar">
      <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
        <span style="font-size: 0.85rem; font-weight: 700; color: var(--text-muted);">ตัวชี้วัดของกราฟ (Metric):</span>
        <div class="metric-switch">
          <button class="metric-btn active" data-metric="revenue" onclick="setGlobalMetric('revenue')">
            💰 รายได้ (฿)
          </button>
          <button class="metric-btn" data-metric="gross_profit" onclick="setGlobalMetric('gross_profit')">
            📈 กำไรขั้นต้น (฿)
          </button>
          <button class="metric-btn" data-metric="qty" onclick="setGlobalMetric('qty')">
            📦 จำนวนหน่วย (ชิ้น)
          </button>
        </div>
      </div>
      <div style="display: flex; align-items: center; gap: 8px;">
        <button class="btn btn-outline btn-sm" onclick="toggleSimulator()">
          💡 แบบจำลองกำไร (What-If Simulator)
        </button>
      </div>
    </div>

    <!-- What-If Simulator Panel (Collapsible) -->
    <section class="simulator-box" id="simulatorSection" style="display: none;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
        <div style="font-weight: 700; font-size: 1rem; color: var(--primary-orange);">
          🎯 แบบจำลองสถานการณ์ราคาและต้นทุน (What-If Profit Simulator)
        </div>
        <button class="btn btn-outline btn-sm" onclick="resetSimulator()">รีเซ็ตแบบจำลอง</button>
      </div>
      <p style="font-size: 0.82rem; color: var(--text-muted); margin-bottom: 16px;">
        ทดลองปรับเปอร์เซ็นต์ราคาขายเฉลี่ยหรือต้นทุนต่อหน่วย เพื่อพยากรณ์ผลกระทบต่อกำไรขั้นต้นจากชุดข้อมูลที่กำลังเลือก
      </p>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px;">
        <div>
          <div class="slider-group">
            <div class="slider-header">
              <span>ปรับราคาขายต่อหน่วย:</span>
              <span id="simPriceVal" style="color: var(--primary-blue);">0%</span>
            </div>
            <input type="range" id="simPriceSlider" min="-20" max="20" value="0" step="1" oninput="updateSimulation()">
          </div>
          <div class="slider-group">
            <div class="slider-header">
              <span>ปรับต้นทุนต่อหน่วย:</span>
              <span id="simCostVal" style="color: var(--primary-orange);">0%</span>
            </div>
            <input type="range" id="simCostSlider" min="-20" max="20" value="0" step="1" oninput="updateSimulation()">
          </div>
        </div>
        <div style="background: var(--bg-card-subtle); padding: 14px; border-radius: var(--radius-md); display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
          <div>
            <div style="font-size: 0.76rem; color: var(--text-muted);">รายได้พยากรณ์</div>
            <div id="simProjRevenue" style="font-size: 1.15rem; font-weight: 800;">฿0</div>
          </div>
          <div>
            <div style="font-size: 0.76rem; color: var(--text-muted);">กำไรขั้นต้นพยากรณ์</div>
            <div id="simProjProfit" style="font-size: 1.15rem; font-weight: 800; color: var(--accent-emerald);">฿0</div>
          </div>
          <div>
            <div style="font-size: 0.76rem; color: var(--text-muted);">อัตรากำไรพยากรณ์</div>
            <div id="simProjMargin" style="font-size: 1.15rem; font-weight: 800;">0%</div>
          </div>
          <div>
            <div style="font-size: 0.76rem; color: var(--text-muted);">ผลต่างกำไร (Delta)</div>
            <div id="simDeltaProfit" style="font-size: 1.15rem; font-weight: 800;">±฿0</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Navigation Tabs -->
    <nav class="tabs-nav" id="mainTabsNav">
      <button class="tab-btn active" data-tab="tabOverview" onclick="switchTab('tabOverview')">
        📊 ภาพรวม (Overview)
      </button>
      <button class="tab-btn" data-tab="tabBranches" onclick="switchTab('tabBranches')">
        🏢 สาขา (Branches & Heatmap)
      </button>
      <button class="tab-btn" data-tab="tabProducts" onclick="switchTab('tabProducts')">
        ☕ สินค้า & ABC (Pareto & Matrix)
      </button>
      <button class="tab-btn" data-tab="tabTrends" onclick="switchTab('tabTrends')">
        📅 มิติเวลา (Time Trends & Calendar)
      </button>
      <button class="tab-btn" data-tab="tabTransactions" onclick="switchTab('tabTransactions')">
        📑 รายการขาย (Transactions)
      </button>
    </nav>

    <!-- TAB 1: OVERVIEW -->
    <div id="tabOverview" class="tab-content active">

      <!-- 6 KPI Cards (Core 3 Cards are #1, #2, #3) -->
      <div class="kpi-grid">
        <div class="kpi-card" style="--card-accent: var(--primary-blue);">
          <div class="kpi-title">
            <span>รายได้รวม (Total Revenue)</span>
            <span style="font-size: 1.1rem;">💰</span>
          </div>
          <div class="kpi-value" id="kpiTotalRevenue">฿0.00</div>
          <div class="kpi-subtext">
            <span>จำนวนขาย × ราคาขายต่อหน่วย</span>
          </div>
        </div>

        <div class="kpi-card" style="--card-accent: var(--accent-cyan);">
          <div class="kpi-title">
            <span>จำนวนหน่วยที่ขายรวม (Units Sold)</span>
            <span style="font-size: 1.1rem;">📦</span>
          </div>
          <div class="kpi-value" id="kpiTotalQty">0 ชิ้น</div>
          <div class="kpi-subtext">
            <span>ปริมาณสินค้าที่จำหน่ายได้</span>
          </div>
        </div>

        <div class="kpi-card" style="--card-accent: var(--primary-orange);">
          <div class="kpi-title">
            <span>กำไรขั้นต้นรวม (Gross Profit)</span>
            <span style="font-size: 1.1rem;">📈</span>
          </div>
          <div class="kpi-value" id="kpiTotalProfit">฿0.00</div>
          <div class="kpi-subtext">
            <span>อัตรากำไรเฉลี่ย: </span>
            <span id="kpiGrossMarginBadge" class="kpi-badge badge-orange">0.00%</span>
          </div>
        </div>

        <div class="kpi-card" style="--card-accent: #6366f1;">
          <div class="kpi-title">
            <span>จำนวนรายการขาย (Transactions)</span>
            <span style="font-size: 1.1rem;">🧾</span>
          </div>
          <div class="kpi-value" id="kpiTxCount">0 บิล</div>
          <div class="kpi-subtext">
            <span>รหัสรายการจำหน่ายที่บันทึก</span>
          </div>
        </div>

        <div class="kpi-card" style="--card-accent: #14b8a6;">
          <div class="kpi-title">
            <span>รายได้เฉลี่ยต่อรายการ (Ticket Size)</span>
            <span style="font-size: 1.1rem;">🏷️</span>
          </div>
          <div class="kpi-value" id="kpiAvgTx">฿0.00</div>
          <div class="kpi-subtext">
            <span>ยอดซื้อเฉลี่ยต่อบิล</span>
          </div>
        </div>

        <div class="kpi-card" style="--card-accent: #ec4899;">
          <div class="kpi-title">
            <span>ราคาขายเฉลี่ยต่อหน่วย (Avg Price)</span>
            <span style="font-size: 1.1rem;">💎</span>
          </div>
          <div class="kpi-value" id="kpiAvgPrice">฿0.00</div>
          <div class="kpi-subtext">
            <span>ถ่วงน้ำหนักตามจำนวนชิ้น</span>
          </div>
        </div>
      </div>

      <!-- Core Chart & Table Grid (Top Products Chart + Branch Revenue Table) -->
      <div class="grid-2">
        <!-- Top Products Bar Chart (Switchable Top 3 / 5 / 8) -->
        <div class="card">
          <div class="card-header">
            <div>
              <div class="card-title">
                <span>🏆 สินค้าที่มีผลงานสูงสุด (Top Products Ranking)</span>
              </div>
              <div class="card-subtitle">
                รวมยอดสินค้าเดียวกันจากทุกสาขาตามกติกา • สลับตัวชี้วัดได้
              </div>
            </div>
            <div style="display: flex; gap: 4px;">
              <button class="date-preset-btn top-rank-btn active" data-top="3" onclick="setTopRankLimit(3)">Top 3 (เริ่มต้น)</button>
              <button class="date-preset-btn top-rank-btn" data-top="5" onclick="setTopRankLimit(5)">Top 5</button>
              <button class="date-preset-btn top-rank-btn" data-top="8" onclick="setTopRankLimit(8)">Top 8 (ทั้งหมด)</button>
            </div>
          </div>
          <div class="chart-container" id="topProductsChartContainer" style="min-height: 280px;">
            <!-- SVG Rendered Dynamically -->
          </div>
        </div>

        <!-- Branch Revenue Comparison Table -->
        <div class="card">
          <div class="card-header">
            <div>
              <div class="card-title">
                <span>🏢 เปรียบเทียบรายได้แต่ละสาขา (Branch Breakdown)</span>
              </div>
              <div class="card-subtitle">
                ตารางเปรียบเทียบสัดส่วนและผลการดำเนินงานของสาขา
              </div>
            </div>
          </div>
          <div class="table-container">
            <table class="data-table" id="overviewBranchTable">
              <thead>
                <tr>
                  <th>สาขา</th>
                  <th class="text-right">รายได้ (฿)</th>
                  <th class="text-right">สัดส่วน</th>
                  <th class="text-right">กำไรขั้นต้น (฿)</th>
                  <th class="text-right">อัตรากำไร</th>
                </tr>
              </thead>
              <tbody id="overviewBranchTableBody"></tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Automated Dynamic Insights -->
      <div class="insights-card">
        <div class="insights-header">
          <span>🧠 ข้อสังเกตอัตโนมัติจากการประมวลผลข้อมูล (Automated Smart Insights)</span>
        </div>
        <div class="insights-grid" id="smartInsightsContainer">
          <!-- Dynamically populated -->
        </div>
      </div>

      <!-- Live Reconciliation Table (ตารางตรวจกระทบยอด) -->
      <div class="card">
        <div class="card-header">
          <div>
            <div class="card-title">
              <span>⚖️ ตารางตรวจกระทบยอดรายได้ (Revenue Reconciliation Balance Sheet)</span>
            </div>
            <div class="card-subtitle">
              ตรวจสอบว่าผลรวมรายได้แยกตาม 5 มิติ (สินค้า, สาขา, หมวดหมู่, วันที่, วันในสัปดาห์) เท่ากับรายได้รวมแบบเรียลไทม์
            </div>
          </div>
          <span class="badge badge-success" style="padding: 6px 12px; font-size: 0.82rem;">
            ผลต่างที่ยอมรับได้: ฿0.00
          </span>
        </div>
        <div class="table-container">
          <table class="data-table">
            <thead>
              <tr>
                <th>มิติการรวมข้อมูล (Aggregation Dimension)</th>
                <th class="text-center">จำนวนกลุ่ม</th>
                <th class="text-right">รายได้รวมของมิติ (฿)</th>
                <th class="text-right">รายได้รวมเป้าหมาย (฿)</th>
                <th class="text-right">ผลต่าง (Discrepancy)</th>
                <th class="text-center">สถานะกระทบยอด</th>
              </tr>
            </thead>
            <tbody id="reconciliationTableBody"></tbody>
          </table>
        </div>
      </div>

    </div>

    <!-- TAB 2: BRANCHES & HEATMAP -->
    <div id="tabBranches" class="tab-content">
      <div class="card">
        <div class="card-header">
          <div>
            <div class="card-title">
              <span>🏢 ผลการดำเนินงานเชิงลึกรายสาขา (Branch Performance Matrix)</span>
            </div>
            <div class="card-subtitle">
              คลิกแถวเพื่อดูการแจกแจงรายสินค้าเฉพาะสาขานั้น • คลิกหัวตารางเพื่อเรียงลำดับ
            </div>
          </div>
          <div id="selectedBranchIndicator" class="kpi-badge badge-blue" style="font-size: 0.85rem; padding: 6px 12px;">
            กำลังเลือก: ทุกสาขา
          </div>
        </div>
        <div class="table-container">
          <table class="data-table" id="fullBranchTable">
            <thead>
              <tr>
                <th onclick="sortBranchTable('branch')">สาขา</th>
                <th class="text-right" onclick="sortBranchTable('share')">สัดส่วนรายได้</th>
                <th class="text-right" onclick="sortBranchTable('revenue')">รายได้รวม (฿)</th>
                <th class="text-right" onclick="sortBranchTable('gross_profit')">กำไรขั้นต้น (฿)</th>
                <th class="text-right" onclick="sortBranchTable('margin')">อัตรากำไร (%)</th>
                <th class="text-right" onclick="sortBranchTable('qty')">จำนวนขาย (หน่วย)</th>
                <th class="text-right" onclick="sortBranchTable('tx')">จำนวนรายการ</th>
              </tr>
            </thead>
            <tbody id="fullBranchTableBody"></tbody>
          </table>
        </div>
      </div>

      <!-- Drilldown: Branch Product Breakdown -->
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <div>
              <div class="card-title" id="branchDrilldownTitle">
                <span>📦 ยอดขายรายสินค้าสำหรับ: ทุกสาขา</span>
              </div>
              <div class="card-subtitle">
                อันดับสินค้าในสาขาที่เลือก
              </div>
            </div>
          </div>
          <div class="chart-container" id="branchDrilldownChart" style="min-height: 280px;"></div>
        </div>

        <!-- Revenue Heatmap Matrix: Branch x Product -->
        <div class="card">
          <div class="card-header">
            <div>
              <div class="card-title">
                <span>🔥 แผนที่ความร้อนรายได้: สาขา × สินค้า (Heatmap Matrix)</span>
              </div>
              <div class="card-subtitle">
                ความเข้มของสีแสดงระดับรายได้ • นำเมาส์ชี้เพื่อดูรายละเอียด
              </div>
            </div>
          </div>
          <div class="table-container" id="heatmapContainer">
            <!-- Heatmap Table Rendered Dynamically -->
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 3: PRODUCTS & ABC ANALYSIS -->
    <div id="tabProducts" class="tab-content">
      <!-- Pareto ABC Chart -->
      <div class="card">
        <div class="card-header">
          <div>
            <div class="card-title">
              <span>📊 กราฟ Pareto & การวิเคราะห์กลุ่มสินค้า ABC (80/20 Rule)</span>
            </div>
            <div class="card-subtitle">
              จัดกลุ่มตามกติกา: กลุ่ม A (รายได้สะสมก่อนหน้า &lt;80%), กลุ่ม B (&lt;95%), กลุ่ม C (ที่เหลือ)
            </div>
          </div>
          <div style="display: flex; gap: 8px;">
            <span class="badge" style="background: rgba(37, 99, 235, 0.2); color: var(--primary-blue);">กลุ่ม A (&lt;80%)</span>
            <span class="badge" style="background: rgba(234, 88, 12, 0.2); color: var(--primary-orange);">กลุ่ม B (&lt;95%)</span>
            <span class="badge" style="background: rgba(148, 163, 184, 0.2); color: var(--text-muted);">กลุ่ม C (ที่เหลือ)</span>
          </div>
        </div>
        <div class="chart-container" id="paretoChartContainer" style="min-height: 340px;">
          <!-- Dynamic SVG Pareto -->
        </div>
        <div id="abcSummaryBanner" style="margin-top: 14px; padding: 12px; background: var(--bg-card-subtle); border-radius: var(--radius-md); font-size: 0.85rem;">
          <!-- Populated dynamically -->
        </div>
      </div>

      <!-- BCG Matrix / Scatter: Units x Margin% with Bubble Size = Revenue -->
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <div>
              <div class="card-title">
                <span>🎯 เมทริกซ์กลยุทธ์สินค้า (Scatter: จำนวนหน่วย × อัตรากำไร)</span>
              </div>
              <div class="card-subtitle">
                แกน X: จำนวนหน่วย • แกน Y: อัตรากำไรขั้นต้น • ขนาดวงกลม: รายได้รวม
              </div>
            </div>
          </div>
          <div class="chart-container" id="scatterChartContainer" style="min-height: 320px;">
            <!-- Dynamic SVG Scatter Plot -->
          </div>
        </div>

        <!-- Full Product Performance Table -->
        <div class="card">
          <div class="card-header">
            <div>
              <div class="card-title">
                <span>📋 ตารางเปรียบเทียบสินค้าทุกรายการ (Product Master Table)</span>
              </div>
              <div class="card-subtitle">
                คลิกหัวคอลัมน์เพื่อเรียงลำดับ
              </div>
            </div>
          </div>
          <div class="table-container">
            <table class="data-table" id="productMasterTable">
              <thead>
                <tr>
                  <th onclick="sortProductTable('product')">สินค้า</th>
                  <th onclick="sortProductTable('category')">หมวดหมู่</th>
                  <th class="text-center" onclick="sortProductTable('abc')">กลุ่ม ABC</th>
                  <th class="text-right" onclick="sortProductTable('price')">ราคา (฿)</th>
                  <th class="text-right" onclick="sortProductTable('cost')">ต้นทุน (฿)</th>
                  <th class="text-right" onclick="sortProductTable('qty')">ขาย (ชิ้น)</th>
                  <th class="text-right" onclick="sortProductTable('revenue')">รายได้ (฿)</th>
                  <th class="text-right" onclick="sortProductTable('gross_profit')">กำไร (฿)</th>
                  <th class="text-right" onclick="sortProductTable('margin')">มาร์จิ้น</th>
                </tr>
              </thead>
              <tbody id="productMasterTableBody"></tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 4: TIME TRENDS & CALENDAR -->
    <div id="tabTrends" class="tab-content">
      <!-- Cumulative Daily Revenue Area Chart -->
      <div class="card">
        <div class="card-header">
          <div>
            <div class="card-title">
              <span>📈 แนวโน้มรายได้สะสมรายวัน (Cumulative Daily Revenue Curve)</span>
            </div>
            <div class="card-subtitle">
              เส้นสะสมรายได้ตลอดเดือนสิงหาคม 2569 (วันที่ 1–31 ส.ค.)
            </div>
          </div>
        </div>
        <div class="chart-container" id="cumulativeTrendChart" style="min-height: 280px;">
          <!-- Dynamic SVG Trend Area -->
        </div>
      </div>

      <div class="grid-2">
        <!-- Day-of-Week Revenue Bar Chart -->
        <div class="card">
          <div class="card-header">
            <div>
              <div class="card-title">
                <span>📅 ผลประกอบการแยกตามวันในสัปดาห์ (Day of Week Analysis)</span>
              </div>
              <div class="card-subtitle">
                เปรียบเทียบยอดขายวันจันทร์ ถึง วันอาทิตย์ พร้อมเส้นค่าเฉลี่ย
              </div>
            </div>
          </div>
          <div class="chart-container" id="dowChartContainer" style="min-height: 280px;">
            <!-- Dynamic SVG DOW Bar -->
          </div>
        </div>

        <!-- Daily Calendar Heatmap -->
        <div class="card">
          <div class="card-header">
            <div>
              <div class="card-title">
                <span>🗓️ ปฏิทินความร้อนรายวัน (August 2026 Daily Heatmap)</span>
              </div>
              <div class="card-subtitle">
                คลิกที่วันที่เพื่อกรองดูยอดเฉพาะวันนั้น
              </div>
            </div>
          </div>
          <div class="calendar-wrapper">
            <div class="calendar-days-header">
              <div>จันทร์</div>
              <div>อังคาร</div>
              <div>พุธ</div>
              <div>พฤหัส</div>
              <div>ศุกร์</div>
              <div>เสาร์</div>
              <div>อาทิตย์</div>
            </div>
            <div class="calendar-grid" id="calendarGridContainer">
              <!-- Rendered via JS -->
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 5: TRANSACTIONS LOG -->
    <div id="tabTransactions" class="tab-content">
      <div class="card">
        <div class="card-header">
          <div>
            <div class="card-title">
              <span>📑 บันทึกรายการขายทั้งหมด (All Sales Transactions)</span>
            </div>
            <div class="card-subtitle">
              ค้นหา เรียงลำดับ แบ่งหน้า และดาวน์โหลดไฟล์ CSV ตามตัวกรองปัจจุบัน
            </div>
          </div>
          <div style="display: flex; gap: 10px; align-items: center;">
            <button class="btn btn-orange btn-sm" onclick="exportFilteredCSV()">
              📥 ดาวน์โหลด CSV ตามตัวกรอง
            </button>
          </div>
        </div>

        <!-- Table controls (Search + Items per page) -->
        <div class="table-controls">
          <div class="search-box">
            <input type="text" id="txSearchInput" placeholder="ค้นหารหัส, สินค้า, สาขา, หมวดหมู่..." oninput="handleTxSearch()">
          </div>
          <div style="display: flex; align-items: center; gap: 8px; font-size: 0.85rem;">
            <span>แสดงแถวต่อหน้า:</span>
            <select id="txPageSizeSelect" onchange="changePageSize(this.value)" style="background: var(--bg-input); border: 1px solid var(--border-color); color: var(--text-main); padding: 4px 8px; border-radius: 4px;">
              <option value="10">10 แถว</option>
              <option value="25" selected>25 แถว</option>
              <option value="50">50 แถว</option>
              <option value="100">ทั้งหมด (100 แถว)</option>
            </select>
          </div>
        </div>

        <!-- Transactions Table -->
        <div class="table-container">
          <table class="data-table" id="txTable">
            <thead>
              <tr>
                <th onclick="sortTxTable('id')">รหัสรายการ</th>
                <th onclick="sortTxTable('date')">วันที่</th>
                <th onclick="sortTxTable('day_of_week')">วันในสัปดาห์</th>
                <th onclick="sortTxTable('branch')">สาขา</th>
                <th onclick="sortTxTable('product')">สินค้า</th>
                <th onclick="sortTxTable('category')">หมวดหมู่</th>
                <th class="text-right" onclick="sortTxTable('qty')">จำนวนขาย</th>
                <th class="text-right" onclick="sortTxTable('price')">ราคา/หน่วย</th>
                <th class="text-right" onclick="sortTxTable('cost')">ต้นทุน/หน่วย</th>
                <th class="text-right" onclick="sortTxTable('revenue')">รายได้ (฿)</th>
                <th class="text-right" onclick="sortTxTable('gross_profit')">กำไรขั้นต้น (฿)</th>
                <th class="text-right" onclick="sortTxTable('margin')">อัตรากำไร</th>
              </tr>
            </thead>
            <tbody id="txTableBody"></tbody>
          </table>
        </div>

        <!-- Pagination Bar -->
        <div class="pagination-bar">
          <div id="txPaginationInfo">กำลังแสดง 1-25 จาก 100 รายการ</div>
          <div class="page-nav" id="txPageNav"></div>
        </div>
      </div>
    </div>

  </main>

  <!-- Tooltip Element for SVG charts -->
  <div class="chart-tooltip" id="globalTooltip"></div>

  <!-- Data Quality Audit Modal -->
  <div class="modal-overlay" id="auditModal">
    <div class="modal-box">
      <div class="modal-header">
        <div style="font-weight: 700; font-size: 1.15rem; color: var(--primary-blue); display: flex; align-items: center; gap: 8px;">
          <span>🛡️ รายงานการตรวจสอบคุณภาพข้อมูล (Data Quality Audit Report)</span>
        </div>
        <button class="modal-close" onclick="closeAuditModal()">&times;</button>
      </div>
      <div>
        <div style="background: rgba(5, 150, 105, 0.1); border: 1px solid rgba(5, 150, 105, 0.3); border-radius: var(--radius-md); padding: 14px; margin-bottom: 18px; color: var(--accent-emerald); font-weight: 600; display: flex; align-items: center; gap: 10px;">
          <span style="font-size: 1.4rem;">✔</span>
          <span>ผ่านเกณฑ์การตรวจสอบข้อมูลทั้งหมด 100% ข้อมูลมีความถูกต้อง สะอาด พร้อมนำไปประมวลผล</span>
        </div>

        <div style="display: flex; flex-direction: column; gap: 14px; font-size: 0.88rem;">
          <div style="border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 12px 16px;">
            <div style="font-weight: 700; color: var(--text-main); margin-bottom: 4px;">1. การตรวจค่าว่าง (Null / Empty Rows Check)</div>
            <div style="color: var(--text-muted);">
              • ตรวจพบแถวว่างทั้งหมด <strong>899 แถว</strong> ในชีต Sales (จากแถวที่ 102 ถึง 1000 ที่เป็นพื้นที่ว่างในไฟล์ Excel)<br>
              • ใน <strong>100 แถวข้อมูลจริง (แถวที่ 2 ถึง 101)</strong> ไม่พบค่าว่างในคอลัมน์ใดเลย (Complete 100%)
            </div>
          </div>

          <div style="border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 12px 16px;">
            <div style="font-weight: 700; color: var(--text-main); margin-bottom: 4px;">2. การตรวจรหัสรายการซ้ำ (Duplicate Transaction IDs Check)</div>
            <div style="color: var(--text-muted);">
              • ตรวจสอบคอลัมน์ รหัสรายการ พบรหัสตั้งแต่ S001 ถึง S100 รวม 100 รายการ<br>
              • ค่าไม่ซ้ำกัน (Unique): <strong>100 / 100 รายการ</strong> (ไม่พบรหัสซ้ำ 0 รายการ)
            </div>
          </div>

          <div style="border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 12px 16px;">
            <div style="font-weight: 700; color: var(--text-main); margin-bottom: 4px;">3. การตรวจความสอดคล้องและการสะกดคำ (Spelling & Whitespace Consistency)</div>
            <div style="color: var(--text-muted);">
              • <strong>สาขา (3 แห่ง):</strong> มหาวิทยาลัย, สำนักงาน, ห้างสรรพสินค้า (สะกดตรงกัน 100% ไม่มีวรรคหน้า/หลัง)<br>
              • <strong>หมวดหมู่ (3 หมวด):</strong> กาแฟ, เบเกอรี, เครื่องดื่มอื่น (ตรงตามมาตรฐานทุกรายการ)<br>
              • <strong>สินค้า (8 รายการ):</strong> ครัวซองต์, คาปูชิโน, ชาไทย, ชีสเค้ก, บราวนี, ลาเต้, อเมริกาโน, โกโก้ (ไม่มีคำสะกดผิด)
            </div>
          </div>

          <div style="border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 12px 16px;">
            <div style="font-weight: 700; color: var(--text-main); margin-bottom: 4px;">4. การตรวจตัวเลขที่เก็บเป็นข้อความ (Data Types Check)</div>
            <div style="color: var(--text-muted);">
              • คอลัมน์ จำนวนขาย, ราคาขายต่อหน่วย, ต้นทุนต่อหน่วย ถูกจัดเก็บเป็นตัวเลขทั้งหมด (Numeric)<br>
              • ไม่พบตัวเลขที่ถูกแปลงเป็นสตริงหรือมีสัญลักษณ์แปลกปลอม
            </div>
          </div>

          <div style="border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 12px 16px;">
            <div style="font-weight: 700; color: var(--text-main); margin-bottom: 4px;">5. สรุปกติกาการคำนวณที่ใช้ในระบบ (Formulas Applied)</div>
            <div style="color: var(--text-muted);">
              • รายได้ = จำนวนขาย × ราคาขายต่อหน่วย<br>
              • กำไรขั้นต้น = จำนวนขาย × (ราคาขายต่อหน่วย − ต้นทุนต่อหน่วย)<br>
              • อัตรากำไรขั้นต้น = กำไรขั้นต้น ÷ รายได้<br>
              • รวมข้อมูลสินค้าเดียวกันจากทุกสาขาก่อนการจัดอันดับและวิเคราะห์ ABC
            </div>
          </div>
        </div>

        <div style="text-align: right; margin-top: 20px;">
          <button class="btn btn-primary" onclick="closeAuditModal()">รับทราบและปิดหน้ารายงาน</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Footer -->
  <footer>
    <div class="container">
      <div class="footer-highlight">⚠️ ข้อมูลจำลองเพื่อการเรียนรู้ (Simulated Data for Educational Purpose)</div>
      <p>พัฒนาสำหรับ Amazon Quick Workshop • ประมวลผลจากชีต Sales ในไฟล์ Excel ต้นฉบับ</p>
      <p style="font-size: 0.78rem; margin-top: 6px; color: var(--text-subtle);">
        สถาปัตยกรรม Single-File HTML • แสดงผลด้วย Custom Scalable Vector Graphics (SVG) โดยไม่พึ่งพาไลบรารีภายนอก
      </p>
    </div>
  </footer>

  <!-- Embedded Raw Dataset & Application Logic -->
  <script>
    // Embedded Sales Dataset (Exact 100 rows from sheet 'Sales')
    const RAW_SALES_DATA = {raw_data_json};

    // Pre-calculate derived columns for each record
    const THAI_DAYS = ['วันอาทิตย์', 'วันจันทร์', 'วันอังคาร', 'วันพุธ', 'วันพฤหัสบดี', 'วันศุกร์', 'วันเสาร์'];

    const SALES_DATA = RAW_SALES_DATA.map((row, idx) => {{
      const d = new Date(row.date + 'T00:00:00');
      const dayOfWeek = THAI_DAYS[d.getDay()];
      const revenue = row.qty * row.price;
      const profit = row.qty * (row.price - row.cost);
      const margin = revenue > 0 ? (profit / revenue) : 0;
      return {{
        id: row.id,
        date: row.date,
        dayOfWeek: dayOfWeek,
        dayIndex: d.getDay(),
        branch: row.branch,
        product: row.product,
        category: row.category,
        qty: Number(row.qty),
        price: Number(row.price),
        cost: Number(row.cost),
        revenue: revenue,
        gross_profit: profit,
        margin: margin
      }};
    }});

    // Distinct dimension values
    const ALL_BRANCHES = Array.from(new Set(SALES_DATA.map(x => x.branch))).sort();
    const ALL_CATEGORIES = Array.from(new Set(SALES_DATA.map(x => x.category))).sort();
    const ALL_PRODUCTS = Array.from(new Set(SALES_DATA.map(x => x.product))).sort();
    const DOW_ORDER = ['วันจันทร์', 'วันอังคาร', 'วันพุธ', 'วันพฤหัสบดี', 'วันศุกร์', 'วันเสาร์', 'วันอาทิตย์'];

    // State Management
    const state = {{
      filters: {{
        branches: new Set(ALL_BRANCHES),
        categories: new Set(ALL_CATEGORIES),
        products: new Set(ALL_PRODUCTS),
        dows: new Set(DOW_ORDER),
        startDate: '2026-08-01',
        endDate: '2026-08-31'
      }},
      globalMetric: 'revenue', // 'revenue' | 'gross_profit' | 'qty'
      topRankLimit: 3,
      selectedBranchDrilldown: null, // null = all
      currentTab: 'tabOverview',
      txTable: {{
        search: '',
        sortCol: 'id',
        sortAsc: true,
        page: 1,
        pageSize: 25
      }},
      branchTable: {{
        sortCol: 'revenue',
        sortAsc: false
      }},
      productTable: {{
        sortCol: 'revenue',
        sortAsc: false
      }},
      simulation: {{
        priceDeltaPct: 0,
        costDeltaPct: 0
      }}
    }};

    // Formatters
    function formatCurrency(val) {{
      return '฿' + Number(val).toLocaleString('th-TH', {{ minimumFractionDigits: 2, maximumFractionDigits: 2 }});
    }}
    function formatInteger(val) {{
      return Number(val).toLocaleString('th-TH');
    }}
    function formatPercent(val) {{
      return (Number(val) * 100).toFixed(2) + '%';
    }}

    // Filter Logic
    function getFilteredData() {{
      return SALES_DATA.filter(row => {{
        if (!state.filters.branches.has(row.branch)) return false;
        if (!state.filters.categories.has(row.category)) return false;
        if (!state.filters.products.has(row.product)) return false;
        if (!state.filters.dows.has(row.dayOfWeek)) return false;
        if (state.filters.startDate && row.date < state.filters.startDate) return false;
        if (state.filters.endDate && row.date > state.filters.endDate) return false;
        return true;
      }});
    }}

    // Initial Filter Pills Rendering
    function initFilterPills() {{
      // Branches
      const branchContainer = document.getElementById('branchFilterPills');
      branchContainer.innerHTML = ALL_BRANCHES.map(b => `
        <label class="pill-checkbox active" id="pill_branch_${{b}}">
          <input type="checkbox" checked onchange="toggleFilter('branch', '${{b}}', this.checked)">
          <span>${{b}}</span>
        </label>
      `).join('');

      // Categories
      const catContainer = document.getElementById('categoryFilterPills');
      catContainer.innerHTML = ALL_CATEGORIES.map(c => `
        <label class="pill-checkbox active" id="pill_category_${{c}}">
          <input type="checkbox" checked onchange="toggleFilter('category', '${{c}}', this.checked)">
          <span>${{c}}</span>
        </label>
      `).join('');

      // Day of Week
      const dowContainer = document.getElementById('dowFilterPills');
      dowContainer.innerHTML = DOW_ORDER.map(d => `
        <label class="pill-checkbox active" id="pill_dow_${{d}}">
          <input type="checkbox" checked onchange="toggleFilter('dow', '${{d}}', this.checked)">
          <span>${{d.replace('วัน', '')}}</span>
        </label>
      `).join('');

      // Products
      const prodContainer = document.getElementById('productFilterPills');
      prodContainer.innerHTML = ALL_PRODUCTS.map(p => `
        <label class="pill-checkbox active" id="pill_product_${{p}}">
          <input type="checkbox" checked onchange="toggleFilter('product', '${{p}}', this.checked)">
          <span>${{p}}</span>
        </label>
      `).join('');

      // Date inputs
      document.getElementById('filterStartDate').addEventListener('change', (e) => {{
        state.filters.startDate = e.target.value;
        onFilterChange();
      }});
      document.getElementById('filterEndDate').addEventListener('change', (e) => {{
        state.filters.endDate = e.target.value;
        onFilterChange();
      }});

      // Reset filters button
      document.getElementById('btnResetFilters').addEventListener('click', resetAllFilters);
    }}

    function toggleFilter(type, value, isChecked) {{
      let setRef;
      if (type === 'branch') setRef = state.filters.branches;
      else if (type === 'category') setRef = state.filters.categories;
      else if (type === 'product') setRef = state.filters.products;
      else if (type === 'dow') setRef = state.filters.dows;

      if (isChecked) {{
        setRef.add(value);
      }} else {{
        setRef.delete(value);
      }}

      const pill = document.getElementById(`pill_${{type}}_${{value}}`);
      if (pill) {{
        if (isChecked) pill.classList.add('active');
        else pill.classList.remove('active');
      }}

      onFilterChange();
    }}

    function quickSelectFilter(type, selectAll) {{
      let allItems = [];
      let setRef;
      if (type === 'branch') {{ allItems = ALL_BRANCHES; setRef = state.filters.branches; }}
      else if (type === 'category') {{ allItems = ALL_CATEGORIES; setRef = state.filters.categories; }}
      else if (type === 'product') {{ allItems = ALL_PRODUCTS; setRef = state.filters.products; }}

      setRef.clear();
      allItems.forEach(item => {{
        if (selectAll) setRef.add(item);
        const pill = document.getElementById(`pill_${{type}}_${{item}}`);
        if (pill) {{
          const cb = pill.querySelector('input');
          if (cb) cb.checked = selectAll;
          if (selectAll) pill.classList.add('active');
          else pill.classList.remove('active');
        }}
      }});
      onFilterChange();
    }}

    function setDowPreset(preset) {{
      state.filters.dows.clear();
      DOW_ORDER.forEach(d => {{
        let shouldSelect = false;
        if (preset === 'all') shouldSelect = true;
        else if (preset === 'weekday' && ['วันจันทร์', 'วันอังคาร', 'วันพุธ', 'วันพฤหัสบดี', 'วันศุกร์'].includes(d)) shouldSelect = true;
        else if (preset === 'weekend' && ['วันเสาร์', 'วันอาทิตย์'].includes(d)) shouldSelect = true;

        if (shouldSelect) state.filters.dows.add(d);
        const pill = document.getElementById(`pill_dow_${{d}}`);
        if (pill) {{
          const cb = pill.querySelector('input');
          if (cb) cb.checked = shouldSelect;
          if (shouldSelect) pill.classList.add('active');
          else pill.classList.remove('active');
        }}
      }});
      onFilterChange();
    }}

    function setDatePreset(preset) {{
      const startInp = document.getElementById('filterStartDate');
      const endInp = document.getElementById('filterEndDate');
      if (preset === 'all') {{
        startInp.value = '2026-08-01';
        endInp.value = '2026-08-31';
      }} else if (preset === 'w1') {{
        startInp.value = '2026-08-01';
        endInp.value = '2026-08-07';
      }} else if (preset === 'w2') {{
        startInp.value = '2026-08-08';
        endInp.value = '2026-08-14';
      }} else if (preset === 'w3') {{
        startInp.value = '2026-08-15';
        endInp.value = '2026-08-21';
      }} else if (preset === 'w4') {{
        startInp.value = '2026-08-22';
        endInp.value = '2026-08-31';
      }}
      state.filters.startDate = startInp.value;
      state.filters.endDate = endInp.value;
      onFilterChange();
    }}

    function resetAllFilters() {{
      state.filters.branches = new Set(ALL_BRANCHES);
      state.filters.categories = new Set(ALL_CATEGORIES);
      state.filters.products = new Set(ALL_PRODUCTS);
      state.filters.dows = new Set(DOW_ORDER);
      state.filters.startDate = '2026-08-01';
      state.filters.endDate = '2026-08-31';
      state.selectedBranchDrilldown = null;

      document.querySelectorAll('.pill-checkbox').forEach(p => {{
        p.classList.add('active');
        const cb = p.querySelector('input');
        if (cb) cb.checked = true;
      }});
      document.getElementById('filterStartDate').value = '2026-08-01';
      document.getElementById('filterEndDate').value = '2026-08-31';

      onFilterChange();
    }}

    function updateActiveFilterTags(filtered) {{
      const tagsContainer = document.getElementById('activeFilterTags');
      const bar = document.getElementById('activeFiltersBar');
      const tags = [];

      if (state.filters.branches.size < ALL_BRANCHES.length) {{
        tags.push(`สาขา: ${{Array.from(state.filters.branches).join(', ') || 'ไม่มี'}}`);
      }}
      if (state.filters.categories.size < ALL_CATEGORIES.length) {{
        tags.push(`หมวด: ${{Array.from(state.filters.categories).join(', ') || 'ไม่มี'}}`);
      }}
      if (state.filters.products.size < ALL_PRODUCTS.length) {{
        tags.push(`สินค้า: ${{state.filters.products.size}} รายการ`);
      }}
      if (state.filters.dows.size < DOW_ORDER.length) {{
        tags.push(`วัน: ${{Array.from(state.filters.dows).map(d => d.replace('วัน','')).join(', ') || 'ไม่มี'}}`);
      }}
      if (state.filters.startDate !== '2026-08-01' || state.filters.endDate !== '2026-08-31') {{
        tags.push(`วันที่: ${{state.filters.startDate}} ถึง ${{state.filters.endDate}}`);
      }}

      if (tags.length > 0) {{
        bar.style.display = 'flex';
        tagsContainer.innerHTML = tags.map(t => `
          <span class="active-filter-tag">${{t}}</span>
        `).join('');
      }} else {{
        bar.style.display = 'none';
      }}

      const badge = document.getElementById('filterRowCountBadge');
      const pct = ((filtered.length / SALES_DATA.length) * 100).toFixed(1);
      badge.textContent = `กำลังแสดง ${{filtered.length}} / ${{SALES_DATA.length}} รายการ (${{pct}}%)`;
    }}

    function onFilterChange() {{
      const filtered = getFilteredData();
      updateActiveFilterTags(filtered);
      renderAllViews(filtered);
    }}

    function setGlobalMetric(metric) {{
      state.globalMetric = metric;
      document.querySelectorAll('.metric-btn').forEach(btn => {{
        if (btn.dataset.metric === metric) btn.classList.add('active');
        else btn.classList.remove('active');
      }});
      const filtered = getFilteredData();
      renderAllViews(filtered);
    }}

    function setTopRankLimit(limit) {{
      state.topRankLimit = limit;
      document.querySelectorAll('.top-rank-btn').forEach(btn => {{
        if (Number(btn.dataset.top) === limit) btn.classList.add('active');
        else btn.classList.remove('active');
      }});
      const filtered = getFilteredData();
      renderTopProductsChart(filtered);
    }}

    function switchTab(tabId) {{
      state.currentTab = tabId;
      document.querySelectorAll('.tab-btn').forEach(btn => {{
        if (btn.dataset.tab === tabId) btn.classList.add('active');
        else btn.classList.remove('active');
      }});
      document.querySelectorAll('.tab-content').forEach(panel => {{
        if (panel.id === tabId) panel.classList.add('active');
        else panel.classList.remove('active');
      }});

      // Render chart for newly active tab
      const filtered = getFilteredData();
      if (tabId === 'tabBranches') renderBranchTab(filtered);
      else if (tabId === 'tabProducts') renderProductTab(filtered);
      else if (tabId === 'tabTrends') renderTrendsTab(filtered);
      else if (tabId === 'tabTransactions') renderTxTable(filtered);
    }}

    // ==========================================
    // RENDER ALL VIEWS
    // ==========================================
    function renderAllViews(data) {{
      renderKpis(data);
      renderTopProductsChart(data);
      renderOverviewBranchTable(data);
      renderSmartInsights(data);
      renderReconciliationTable(data);
      updateSimulation();

      // Refresh tab specific views
      if (state.currentTab === 'tabBranches') renderBranchTab(data);
      else if (state.currentTab === 'tabProducts') renderProductTab(data);
      else if (state.currentTab === 'tabTrends') renderTrendsTab(data);
      else if (state.currentTab === 'tabTransactions') renderTxTable(data);
    }}

    // --- 1. KPI CARDS ---
    function renderKpis(data) {{
      const totalRev = data.reduce((acc, x) => acc + x.revenue, 0);
      const totalQty = data.reduce((acc, x) => acc + x.qty, 0);
      const totalProfit = data.reduce((acc, x) => acc + x.gross_profit, 0);
      const margin = totalRev > 0 ? (totalProfit / totalRev) : 0;
      const txCount = data.length;
      const avgTx = txCount > 0 ? (totalRev / txCount) : 0;
      const avgPrice = totalQty > 0 ? (totalRev / totalQty) : 0;

      document.getElementById('kpiTotalRevenue').textContent = formatCurrency(totalRev);
      document.getElementById('kpiTotalQty').textContent = formatInteger(totalQty) + ' ชิ้น';
      document.getElementById('kpiTotalProfit').textContent = formatCurrency(totalProfit);
      document.getElementById('kpiGrossMarginBadge').textContent = formatPercent(margin);
      document.getElementById('kpiTxCount').textContent = formatInteger(txCount) + ' รายการ';
      document.getElementById('kpiAvgTx').textContent = formatCurrency(avgTx);
      document.getElementById('kpiAvgPrice').textContent = formatCurrency(avgPrice);
    }}

    // --- 2. TOP PRODUCTS CHART (SVG HORIZONTAL BAR) ---
    function renderTopProductsChart(data) {{
      const container = document.getElementById('topProductsChartContainer');
      const metric = state.globalMetric;

      // Group by product across all branches
      const prodMap = {{}};
      data.forEach(x => {{
        if (!prodMap[x.product]) {{
          prodMap[x.product] = {{ product: x.product, category: x.category, revenue: 0, gross_profit: 0, qty: 0 }};
        }}
        prodMap[x.product].revenue += x.revenue;
        prodMap[x.product].gross_profit += x.gross_profit;
        prodMap[x.product].qty += x.qty;
      }});

      let sorted = Object.values(prodMap).sort((a, b) => b[metric] - a[metric]);
      const topItems = sorted.slice(0, state.topRankLimit);

      if (topItems.length === 0) {{
        container.innerHTML = '<div style="padding: 40px; text-align: center; color: var(--text-muted);">ไม่มีข้อมูลสำหรับตัวกรองที่เลือก</div>';
        return;
      }}

      const maxVal = Math.max(...topItems.map(x => x[metric]), 1);
      const rowHeight = 44;
      const margin = {{ top: 20, right: 90, bottom: 25, left: 110 }};
      const width = 560;
      const height = margin.top + (topItems.length * rowHeight) + margin.bottom;

      let metricLabel = 'รายได้ (฿)';
      if (metric === 'gross_profit') metricLabel = 'กำไรขั้นต้น (฿)';
      else if (metric === 'qty') metricLabel = 'จำนวนขาย (ชิ้น)';

      let barsSvg = '';
      topItems.forEach((item, idx) => {{
        const y = margin.top + (idx * rowHeight);
        const val = item[metric];
        const barWidth = ((val / maxVal) * (width - margin.left - margin.right));
        const formattedVal = (metric === 'qty') ? formatInteger(val) + ' ชิ้น' : formatCurrency(val);
        const rankColor = idx === 0 ? '#ea580c' : (idx === 1 ? '#2563eb' : '#3b82f6');

        barsSvg += `
          <g class="bar-group" style="cursor: pointer;" onmousemove="showTooltip(event, '${{item.product}} (${{item.category}})<br>${{metricLabel}}: ${{formattedVal}}<br>รายได้: ${{formatCurrency(item.revenue)}}<br>กำไร: ${{formatCurrency(item.gross_profit)}}<br>จำนวน: ${{formatInteger(item.qty)}} ชิ้น')" onmouseleave="hideTooltip()">
            <!-- Rank & Label -->
            <text x="${{margin.left - 10}}" y="${{y + 22}}" text-anchor="end" fill="var(--text-main)" font-size="12" font-weight="600">
              #${{idx + 1}} ${{item.product}}
            </text>
            <!-- Background track -->
            <rect x="${{margin.left}}" y="${{y + 8}}" width="${{width - margin.left - margin.right}}" height="20" rx="4" fill="var(--bg-card-subtle)" />
            <!-- Bar fill -->
            <rect x="${{margin.left}}" y="${{y + 8}}" width="${{barWidth}}" height="20" rx="4" fill="${{rankColor}}" opacity="0.9" />
            <!-- Value text -->
            <text x="${{margin.left + barWidth + 8}}" y="${{y + 23}}" fill="var(--text-main)" font-size="11" font-weight="700">
              ${{formattedVal}}
            </text>
          </g>
        `;
      }});

      container.innerHTML = `
        <svg viewBox="0 0 ${{width}} ${{height}}" class="interactive-svg">
          <line x1="${{margin.left}}" y1="${{margin.top}}" x2="${{margin.left}}" y2="${{height - margin.bottom}}" stroke="var(--border-color)" stroke-width="1.5" />
          ${{barsSvg}}
        </svg>
      `;
    }}

    // --- 3. OVERVIEW BRANCH TABLE ---
    function renderOverviewBranchTable(data) {{
      const tbody = document.getElementById('overviewBranchTableBody');
      const bMap = {{}};
      let totalRev = 0;
      let totalProfit = 0;
      let totalQty = 0;

      data.forEach(x => {{
        if (!bMap[x.branch]) {{
          bMap[x.branch] = {{ branch: x.branch, revenue: 0, gross_profit: 0, qty: 0 }};
        }}
        bMap[x.branch].revenue += x.revenue;
        bMap[x.branch].gross_profit += x.gross_profit;
        bMap[x.branch].qty += x.qty;
        totalRev += x.revenue;
        totalProfit += x.gross_profit;
        totalQty += x.qty;
      }});

      const branches = Object.values(bMap).sort((a, b) => b.revenue - a.revenue);

      if (branches.length === 0) {{
        tbody.innerHTML = '<tr><td colspan="5" class="text-center" style="padding: 20px; color: var(--text-muted);">ไม่มีข้อมูลสำหรับตัวกรองที่เลือก</td></tr>';
        return;
      }}

      let html = branches.map(b => {{
        const share = totalRev > 0 ? (b.revenue / totalRev) * 100 : 0;
        const margin = b.revenue > 0 ? (b.gross_profit / b.revenue) : 0;
        return `
          <tr>
            <td style="font-weight: 600;">${{b.branch}}</td>
            <td class="text-right" style="font-weight: 700;">${{formatCurrency(b.revenue)}}</td>
            <td class="text-right">
              <div class="share-bar-container">
                <span style="min-width: 42px;">${{share.toFixed(1)}}%</span>
                <div class="share-bar-outer"><div class="share-bar-inner" style="width: ${{share}}%;"></div></div>
              </div>
            </td>
            <td class="text-right" style="color: var(--accent-emerald); font-weight: 600;">${{formatCurrency(b.gross_profit)}}</td>
            <td class="text-right">${{formatPercent(margin)}}</td>
          </tr>
        `;
      }}).join('');

      // Total Row
      const totalMargin = totalRev > 0 ? (totalProfit / totalRev) : 0;
      html += `
        <tr class="total-row">
          <td>รวมทั้งหมด (${{branches.length}} สาขา)</td>
          <td class="text-right">${{formatCurrency(totalRev)}}</td>
          <td class="text-right">100.0%</td>
          <td class="text-right" style="color: var(--accent-emerald);">${{formatCurrency(totalProfit)}}</td>
          <td class="text-right">${{formatPercent(totalMargin)}}</td>
        </tr>
      `;

      tbody.innerHTML = html;
    }}

    // --- 4. SMART INSIGHTS ---
    function renderSmartInsights(data) {{
      const container = document.getElementById('smartInsightsContainer');
      if (data.length === 0) {{
        container.innerHTML = '<div style="color: var(--text-muted);">ไม่มีข้อมูลสำหรับวิเคราะห์</div>';
        return;
      }}

      // Top revenue product vs top profit product
      const prodStats = {{}};
      const branchStats = {{}};
      const dowStats = {{}};
      let totalRev = 0;
      let totalProfit = 0;

      data.forEach(x => {{
        totalRev += x.revenue;
        totalProfit += x.gross_profit;
        if (!prodStats[x.product]) prodStats[x.product] = {{ rev: 0, profit: 0, qty: 0, margin: x.margin, cat: x.category }};
        prodStats[x.product].rev += x.revenue;
        prodStats[x.product].profit += x.gross_profit;
        prodStats[x.product].qty += x.qty;

        if (!branchStats[x.branch]) branchStats[x.branch] = {{ rev: 0, profit: 0, qty: 0 }};
        branchStats[x.branch].rev += x.revenue;
        branchStats[x.branch].profit += x.gross_profit;

        if (!dowStats[x.dayOfWeek]) dowStats[x.dayOfWeek] = {{ rev: 0, profit: 0, qty: 0 }};
        dowStats[x.dayOfWeek].rev += x.revenue;
        dowStats[x.dayOfWeek].qty += x.qty;
      }});

      const prodsSortedRev = Object.entries(prodStats).sort((a, b) => b[1].rev - a[1].rev);
      const prodsSortedProfit = Object.entries(prodStats).sort((a, b) => b[1].profit - a[1].profit);
      const branchesSorted = Object.entries(branchStats).sort((a, b) => b[1].rev - a[1].rev);
      const dowSorted = Object.entries(dowStats).sort((a, b) => b[1].rev - a[1].rev);

      const topRevProd = prodsSortedRev[0];
      const topProfitProd = prodsSortedProfit[0];
      const topBranch = branchesSorted[0];
      const topDow = dowSorted[0];

      const topBranchShare = totalRev > 0 ? ((topBranch[1].rev / totalRev) * 100).toFixed(1) : 0;
      const topRevShare = totalRev > 0 ? ((topRevProd[1].rev / totalRev) * 100).toFixed(1) : 0;

      container.innerHTML = `
        <div class="insight-item">
          <span class="insight-icon">🏆</span>
          <div class="insight-text">
            <strong>${{topRevProd[0]}}</strong> ครองแชมป์ยอดขายสูงสุด สร้างรายได้ <strong>${{formatCurrency(topRevProd[1].rev)}}</strong> (${{topRevShare}}% ของรายได้ทั้งหมด) โดยมีกำไรขั้นต้น ${{formatCurrency(topRevProd[1].profit)}}
          </div>
        </div>
        <div class="insight-item">
          <span class="insight-icon">💎</span>
          <div class="insight-text">
            สินค้าสร้างกำไรสูงสุดคือ <strong>${{topProfitProd[0]}}</strong> ด้วยกำไรขั้นต้น <strong>${{formatCurrency(topProfitProd[1].profit)}}</strong> (อัตรากำไร ${{(topProfitProd[1].profit / topProfitProd[1].rev * 100).toFixed(1)}}%)
          </div>
        </div>
        <div class="insight-item">
          <span class="insight-icon">🏢</span>
          <div class="insight-text">
            สาขา <strong>${{topBranch[0]}}</strong> มีผลงานอันดับ 1 กวาดรายได้ไป <strong>${{formatCurrency(topBranch[1].rev)}}</strong> คิดเป็น ${{topBranchShare}}% ของยอดรวมทั้งหมด
          </div>
        </div>
        <div class="insight-item">
          <span class="insight-icon">📅</span>
          <div class="insight-text">
            ช่วงเวลาขายดีที่สุดในสัปดาห์คือ <strong>${{topDow[0]}}</strong> มียอดขายรวม <strong>${{formatCurrency(topDow[1].rev)}}</strong> (${{topDow[1].qty}} ชิ้น)
          </div>
        </div>
      `;
    }}

    // --- 5. RECONCILIATION TABLE ---
    function renderReconciliationTable(data) {{
      const tbody = document.getElementById('reconciliationTableBody');
      const targetRevenue = data.reduce((acc, x) => acc + x.revenue, 0);

      const dimensions = [
        {{ name: 'รวมตามสินค้า (Sum by Product)', getGroup: x => x.product }},
        {{ name: 'รวมตามสาขา (Sum by Branch)', getGroup: x => x.branch }},
        {{ name: 'รวมตามหมวดหมู่ (Sum by Category)', getGroup: x => x.category }},
        {{ name: 'รวมตามวันที่ (Sum by Date)', getGroup: x => x.date }},
        {{ name: 'รวมตามวันในสัปดาห์ (Sum by Day of Week)', getGroup: x => x.dayOfWeek }}
      ];

      const html = dimensions.map(dim => {{
        const groups = {{}};
        data.forEach(x => {{
          const key = dim.getGroup(x);
          groups[key] = (groups[key] || 0) + x.revenue;
        }});

        const groupCount = Object.keys(groups).length;
        const dimTotal = Object.values(groups).reduce((acc, v) => acc + v, 0);
        const diff = Math.abs(dimTotal - targetRevenue);
        const isMatched = diff < 0.001;

        return `
          <tr>
            <td style="font-weight: 600;">${{dim.name}}</td>
            <td class="text-center">${{groupCount}} กลุ่ม</td>
            <td class="text-right" style="font-weight: 700;">${{formatCurrency(dimTotal)}}</td>
            <td class="text-right">${{formatCurrency(targetRevenue)}}</td>
            <td class="text-right" style="color: ${{diff === 0 ? 'var(--text-muted)' : 'var(--accent-rose)'}};">฿${{diff.toFixed(2)}}</td>
            <td class="text-center">
              ${{isMatched 
                ? '<span class="badge badge-success" style="font-size: 0.8rem;">✔ กระทบยอดตรง 100%</span>' 
                : '<span class="badge" style="background: rgba(225,29,72,0.15); color: var(--accent-rose);">✖ ไม่ตรงกัน</span>'}}
            </td>
          </tr>
        `;
      }}).join('');

      tbody.innerHTML = html;
    }}

    // --- 6. TAB 2: BRANCHES & HEATMAP ---
    function renderBranchTab(data) {{
      renderFullBranchTable(data);
      renderBranchDrilldown(data);
      renderHeatmap(data);
    }}

    function renderFullBranchTable(data) {{
      const tbody = document.getElementById('fullBranchTableBody');
      const bMap = {{}};
      let totalRev = 0, totalProfit = 0, totalQty = 0, totalTx = 0;

      data.forEach(x => {{
        if (!bMap[x.branch]) {{
          bMap[x.branch] = {{ branch: x.branch, revenue: 0, gross_profit: 0, qty: 0, tx: 0 }};
        }}
        bMap[x.branch].revenue += x.revenue;
        bMap[x.branch].gross_profit += x.gross_profit;
        bMap[x.branch].qty += x.qty;
        bMap[x.branch].tx += 1;
        totalRev += x.revenue;
        totalProfit += x.gross_profit;
        totalQty += x.qty;
        totalTx += 1;
      }});

      let list = Object.values(bMap).map(b => ({{
        ...b,
        share: totalRev > 0 ? (b.revenue / totalRev) * 100 : 0,
        margin: b.revenue > 0 ? (b.gross_profit / b.revenue) : 0
      }}));

      const col = state.branchTable.sortCol;
      const asc = state.branchTable.sortAsc;
      list.sort((a, b) => asc ? (a[col] > b[col] ? 1 : -1) : (a[col] < b[col] ? 1 : -1));

      let html = list.map(b => {{
        const isSelected = state.selectedBranchDrilldown === b.branch;
        return `
          <tr class="${{isSelected ? 'selected' : ''}}" style="cursor: pointer;" onclick="selectBranchDrilldown('${{b.branch}}')">
            <td style="font-weight: 700;">${{b.branch}} ${{isSelected ? '📌' : ''}}</td>
            <td class="text-right">
              <div class="share-bar-container">
                <span style="min-width: 42px;">${{b.share.toFixed(1)}}%</span>
                <div class="share-bar-outer"><div class="share-bar-inner" style="width: ${{b.share}}%;"></div></div>
              </div>
            </td>
            <td class="text-right" style="font-weight: 700;">${{formatCurrency(b.revenue)}}</td>
            <td class="text-right" style="color: var(--accent-emerald); font-weight: 600;">${{formatCurrency(b.gross_profit)}}</td>
            <td class="text-right">${{formatPercent(b.margin)}}</td>
            <td class="text-right">${{formatInteger(b.qty)}}</td>
            <td class="text-right">${{formatInteger(b.tx)}}</td>
          </tr>
        `;
      }}).join('');

      const totalMargin = totalRev > 0 ? (totalProfit / totalRev) : 0;
      html += `
        <tr class="total-row" onclick="selectBranchDrilldown(null)" style="cursor: pointer;" title="คลิกเพื่อเลือกทุกสาขา">
          <td>รวมทุกสาขา (${{list.length}} สาขา)</td>
          <td class="text-right">100.0%</td>
          <td class="text-right">${{formatCurrency(totalRev)}}</td>
          <td class="text-right" style="color: var(--accent-emerald);">${{formatCurrency(totalProfit)}}</td>
          <td class="text-right">${{formatPercent(totalMargin)}}</td>
          <td class="text-right">${{formatInteger(totalQty)}}</td>
          <td class="text-right">${{formatInteger(totalTx)}}</td>
        </tr>
      `;

      tbody.innerHTML = html;
    }}

    function selectBranchDrilldown(branch) {{
      state.selectedBranchDrilldown = (state.selectedBranchDrilldown === branch) ? null : branch;
      const ind = document.getElementById('selectedBranchIndicator');
      ind.textContent = state.selectedBranchDrilldown ? `กำลังเลือก: ${{state.selectedBranchDrilldown}}` : 'กำลังเลือก: ทุกสาขา';
      const filtered = getFilteredData();
      renderFullBranchTable(filtered);
      renderBranchDrilldown(filtered);
    }}

    function sortBranchTable(col) {{
      if (state.branchTable.sortCol === col) {{
        state.branchTable.sortAsc = !state.branchTable.sortAsc;
      }} else {{
        state.branchTable.sortCol = col;
        state.branchTable.sortAsc = false;
      }}
      renderFullBranchTable(getFilteredData());
    }}

    function renderBranchDrilldown(data) {{
      const container = document.getElementById('branchDrilldownChart');
      const title = document.getElementById('branchDrilldownTitle');
      const branch = state.selectedBranchDrilldown;
      title.innerHTML = `<span>📦 ยอดขายรายสินค้าสำหรับ: <strong>${{branch || 'ทุกสาขา'}}</strong></span>`;

      const subset = branch ? data.filter(x => x.branch === branch) : data;
      const prodMap = {{}};
      subset.forEach(x => {{
        if (!prodMap[x.product]) prodMap[x.product] = {{ product: x.product, revenue: 0, profit: 0, qty: 0 }};
        prodMap[x.product].revenue += x.revenue;
        prodMap[x.product].profit += x.gross_profit;
        prodMap[x.product].qty += x.qty;
      }});

      const metric = state.globalMetric;
      const list = Object.values(prodMap).sort((a, b) => b[metric] - a[metric]);

      if (list.length === 0) {{
        container.innerHTML = '<div style="padding: 40px; text-align: center; color: var(--text-muted);">ไม่มีข้อมูล</div>';
        return;
      }}

      const maxVal = Math.max(...list.map(x => x[metric]), 1);
      const rowHeight = 30;
      const margin = {{ top: 15, right: 80, bottom: 20, left: 95 }};
      const width = 500;
      const height = margin.top + (list.length * rowHeight) + margin.bottom;

      let bars = list.map((item, idx) => {{
        const y = margin.top + (idx * rowHeight);
        const w = (item[metric] / maxVal) * (width - margin.left - margin.right);
        const labelVal = metric === 'qty' ? formatInteger(item[metric]) : formatCurrency(item[metric]);
        return `
          <g>
            <text x="${{margin.left - 8}}" y="${{y + 16}}" text-anchor="end" fill="var(--text-main)" font-size="11" font-weight="600">${{item.product}}</text>
            <rect x="${{margin.left}}" y="${{y + 4}}" width="${{width - margin.left - margin.right}}" height="16" rx="3" fill="var(--bg-card-subtle)" />
            <rect x="${{margin.left}}" y="${{y + 4}}" width="${{w}}" height="16" rx="3" fill="var(--primary-blue)" opacity="0.85" />
            <text x="${{margin.left + w + 6}}" y="${{y + 16}}" fill="var(--text-main)" font-size="10" font-weight="700">${{labelVal}}</text>
          </g>
        `;
      }}).join('');

      container.innerHTML = `
        <svg viewBox="0 0 ${{width}} ${{height}}" class="interactive-svg">
          <line x1="${{margin.left}}" y1="${{margin.top}}" x2="${{margin.left}}" y2="${{height - margin.bottom}}" stroke="var(--border-color)" />
          ${{bars}}
        </svg>
      `;
    }}

    function renderHeatmap(data) {{
      const container = document.getElementById('heatmapContainer');
      const matrix = {{}};
      const branchTotals = {{}};
      const prodTotals = {{}};
      let maxRev = 0;

      ALL_BRANCHES.forEach(b => {{
        matrix[b] = {{}};
        branchTotals[b] = 0;
        ALL_PRODUCTS.forEach(p => matrix[b][p] = 0);
      }});
      ALL_PRODUCTS.forEach(p => prodTotals[p] = 0);

      data.forEach(x => {{
        if (matrix[x.branch] && matrix[x.branch][x.product] !== undefined) {{
          matrix[x.branch][x.product] += x.revenue;
          branchTotals[x.branch] += x.revenue;
          prodTotals[x.product] += x.revenue;
          if (matrix[x.branch][x.product] > maxRev) maxRev = matrix[x.branch][x.product];
        }}
      }});

      let thead = '<tr><th>สาขา \\ สินค้า</th>' + ALL_PRODUCTS.map(p => `<th class="text-right" style="font-size: 0.76rem;">${{p}}</th>`).join('') + '<th class="text-right">รวมสาขา</th></tr>';

      let rows = ALL_BRANCHES.map(b => {{
        let cells = ALL_PRODUCTS.map(p => {{
          const rev = matrix[b][p];
          const intensity = maxRev > 0 ? (rev / maxRev) : 0;
          // Gradient from subtle blue to vibrant orange
          const bg = intensity > 0 
            ? `rgba(234, 88, 12, ${{Math.max(0.12, intensity * 0.85)}})` 
            : 'var(--bg-card-subtle)';
          const textColor = intensity > 0.5 ? '#ffffff' : 'var(--text-main)';
          return `
            <td class="text-right heatmap-cell" style="background: ${{bg}}; color: ${{textColor}};" onmousemove="showTooltip(event, '${{b}} × ${{p}}<br>รายได้: ${{formatCurrency(rev)}}')" onmouseleave="hideTooltip()">
              ${{rev > 0 ? formatCurrency(rev).replace('฿', '') : '-'}}
            </td>
          `;
        }}).join('');

        return `
          <tr>
            <td style="font-weight: 700;">${{b}}</td>
            ${{cells}}
            <td class="text-right" style="font-weight: 800; background: var(--bg-card-subtle);">${{formatCurrency(branchTotals[b])}}</td>
          </tr>
        `;
      }}).join('');

      let footerCells = ALL_PRODUCTS.map(p => `<td class="text-right" style="font-weight: 800;">${{formatCurrency(prodTotals[p])}}</td>`).join('');
      let totalRevAll = Object.values(prodTotals).reduce((a, b) => a + b, 0);

      container.innerHTML = `
        <table class="data-table" style="font-size: 0.8rem;">
          <thead>${{thead}}</thead>
          <tbody>${{rows}}</tbody>
          <tfoot>
            <tr class="total-row">
              <td>รวมสินค้า</td>
              ${{footerCells}}
              <td class="text-right" style="color: var(--primary-orange);">${{formatCurrency(totalRevAll)}}</td>
            </tr>
          </tfoot>
        </table>
      `;
    }}

    // --- 7. TAB 3: PRODUCTS & ABC (PARETO & SCATTER) ---
    function renderProductTab(data) {{
      renderParetoChart(data);
      renderScatterPlot(data);
      renderProductMasterTable(data);
    }}

    function renderParetoChart(data) {{
      const container = document.getElementById('paretoChartContainer');
      const summaryBanner = document.getElementById('abcSummaryBanner');
      const metric = state.globalMetric;

      const pMap = {{}};
      let totalVal = 0;
      data.forEach(x => {{
        if (!pMap[x.product]) pMap[x.product] = {{ product: x.product, category: x.category, val: 0, revenue: 0, profit: 0, qty: 0 }};
        pMap[x.product].val += x[metric];
        pMap[x.product].revenue += x.revenue;
        pMap[x.product].profit += x.gross_profit;
        pMap[x.product].qty += x.qty;
        totalVal += x[metric];
      }});

      const prods = Object.values(pMap).sort((a, b) => b.val - a.val);
      if (prods.length === 0 || totalVal === 0) {{
        container.innerHTML = '<div style="padding: 40px; text-align: center; color: var(--text-muted);">ไม่มีข้อมูลสำหรับวิเคราะห์ ABC</div>';
        summaryBanner.innerHTML = '';
        return;
      }}

      // Classify ABC: Prior cumulative < 80% => A, < 95% => B, else => C
      let cum = 0;
      let countA = 0, countB = 0, countC = 0;
      let valA = 0, valB = 0, valC = 0;

      prods.forEach(p => {{
        const priorCumPct = (cum / totalVal) * 100;
        cum += p.val;
        p.cumPct = (cum / totalVal) * 100;

        if (priorCumPct < 80) {{
          p.abc = 'A';
          countA++;
          valA += p.val;
        }} else if (priorCumPct < 95) {{
          p.abc = 'B';
          countB++;
          valB += p.val;
        }} else {{
          p.abc = 'C';
          countC++;
          valC += p.val;
        }}
      }});

      // Draw SVG Dual-Axis Pareto
      const margin = {{ top: 30, right: 50, bottom: 70, left: 70 }};
      const width = 800;
      const height = 340;
      const maxVal = prods[0].val * 1.15;
      const chartW = width - margin.left - margin.right;
      const chartH = height - margin.top - margin.bottom;
      const colW = chartW / prods.length;
      const barW = Math.max(16, colW * 0.6);

      let gridLines = '';
      for (let p = 0; p <= 100; p += 20) {{
        const y = margin.top + chartH - (p / 100) * chartH;
        gridLines += `
          <line x1="${{margin.left}}" y1="${{y}}" x2="${{width - margin.right}}" y2="${{y}}" class="svg-grid-line" />
          <text x="${{margin.left - 8}}" y="${{y + 4}}" text-anchor="end" class="svg-axis-text">${{formatInteger((p / 100) * maxVal)}}</text>
          <text x="${{width - margin.right + 8}}" y="${{y + 4}}" text-anchor="start" class="svg-axis-text">${{p}}%</text>
        `;
      }}

      // Reference line at 80% & 95%
      const y80 = margin.top + chartH - (0.80 * chartH);
      const y95 = margin.top + chartH - (0.95 * chartH);
      const refLines = `
        <line x1="${{margin.left}}" y1="${{y80}}" x2="${{width - margin.right}}" y2="${{y80}}" stroke="#ea580c" stroke-dasharray="6,3" stroke-width="1.5" />
        <text x="${{width - margin.right - 6}}" y="${{y80 - 6}}" text-anchor="end" fill="#ea580c" font-size="10" font-weight="700">เกณฑ์ 80% (กลุ่ม A)</text>
        <line x1="${{margin.left}}" y1="${{y95}}" x2="${{width - margin.right}}" y2="${{y95}}" stroke="#f59e0b" stroke-dasharray="6,3" stroke-width="1.5" />
        <text x="${{width - margin.right - 6}}" y="${{y95 - 6}}" text-anchor="end" fill="#f59e0b" font-size="10" font-weight="700">เกณฑ์ 95% (กลุ่ม B)</text>
      `;

      let barsSvg = '';
      const linePoints = [];

      prods.forEach((p, idx) => {{
        const cx = margin.left + (idx * colW) + (colW / 2);
        const barH = (p.val / maxVal) * chartH;
        const barY = margin.top + chartH - barH;
        const lineY = margin.top + chartH - ((p.cumPct / 100) * chartH);
        linePoints.push(`${{cx}},${{lineY}}`);

        const color = p.abc === 'A' ? 'var(--primary-blue)' : (p.abc === 'B' ? 'var(--primary-orange)' : '#94a3b8');

        barsSvg += `
          <g style="cursor: pointer;" onmousemove="showTooltip(event, '<strong>${{p.product}}</strong> (กลุ่ม ${{p.abc}})<br>ค่า: ${{metric === 'qty' ? formatInteger(p.val) : formatCurrency(p.val)}}<br>สะสม: ${{p.cumPct.toFixed(1)}}%')" onmouseleave="hideTooltip()">
            <rect x="${{cx - barW / 2}}" y="${{barY}}" width="${{barW}}" height="${{barH}}" rx="4" fill="${{color}}" opacity="0.9" />
            <text x="${{cx}}" y="${{height - margin.bottom + 18}}" text-anchor="end" transform="rotate(-35, ${{cx}}, ${{height - margin.bottom + 18}})" font-size="11" font-weight="600" fill="var(--text-main)">${{p.product}}</text>
            <text x="${{cx}}" y="${{barY - 6}}" text-anchor="middle" font-size="10" font-weight="700" fill="${{color}}">${{p.abc}}</text>
          </g>
        `;
      }});

      // Line path
      const linePath = `<polyline fill="none" stroke="#ea580c" stroke-width="3" points="${{linePoints.join(' ')}}" />`;
      const pointsSvg = linePoints.map((pt, i) => `
        <circle cx="${{pt.split(',')[0]}}" cy="${{pt.split(',')[1]}}" r="4" fill="#ffffff" stroke="#ea580c" stroke-width="2.5" />
      `).join('');

      container.innerHTML = `
        <svg viewBox="0 0 ${{width}} ${{height}}" class="interactive-svg">
          ${{gridLines}}
          ${{refLines}}
          ${{barsSvg}}
          ${{linePath}}
          ${{pointsSvg}}
          <!-- Axis titles -->
          <text x="${{margin.left}}" y="18" class="svg-axis-title">มูลค่าตัวชี้วัด</text>
          <text x="${{width - margin.right}}" y="18" text-anchor="end" class="svg-axis-title">% สะสม (Cumulative %)</text>
        </svg>
      `;

      // ABC summary box
      summaryBanner.innerHTML = `
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px;">
          <div>
            <strong style="color: var(--primary-blue);">กลุ่ม A (${{countA}} รายการ):</strong> ${{((valA / totalVal) * 100).toFixed(1)}}% ของมูลค่ารวม
            <div style="font-size: 0.78rem; color: var(--text-muted);">สินค้าสร้างรายได้หลัก ควรบริหารสต็อกห้ามขาด</div>
          </div>
          <div>
            <strong style="color: var(--primary-orange);">กลุ่ม B (${{countB}} รายการ):</strong> ${{((valB / totalVal) * 100).toFixed(1)}}% ของมูลค่ารวม
            <div style="font-size: 0.78rem; color: var(--text-muted);">สินค้าทำเงินระดับรอง จัดโปรโมชันกระตุ้นยอดได้</div>
          </div>
          <div>
            <strong style="color: var(--text-muted);">กลุ่ม C (${{countC}} รายการ):</strong> ${{((valC / totalVal) * 100).toFixed(1)}}% ของมูลค่ารวม
            <div style="font-size: 0.78rem; color: var(--text-muted);">สินค้าหางยาว ติดตามต้นทุนและสต็อกอย่างรัดกุม</div>
          </div>
        </div>
      `;
    }}

    function renderScatterPlot(data) {{
      const container = document.getElementById('scatterChartContainer');
      const prodStats = {{}};
      let totalQty = 0, totalProfit = 0, totalRev = 0;

      data.forEach(x => {{
        if (!prodStats[x.product]) {{
          prodStats[x.product] = {{ product: x.product, category: x.category, qty: 0, revenue: 0, profit: 0 }};
        }}
        prodStats[x.product].qty += x.qty;
        prodStats[x.product].revenue += x.revenue;
        prodStats[x.product].profit += x.gross_profit;
        totalQty += x.qty;
        totalProfit += x.gross_profit;
        totalRev += x.revenue;
      }});

      const prods = Object.values(prodStats).map(p => ({{
        ...p,
        margin: p.revenue > 0 ? (p.profit / p.revenue) : 0
      }}));

      if (prods.length === 0) {{
        container.innerHTML = '<div style="padding: 40px; text-align: center; color: var(--text-muted);">ไม่มีข้อมูล</div>';
        return;
      }}

      const avgQty = totalQty / prods.length;
      const avgMargin = totalRev > 0 ? (totalProfit / totalRev) : 0;

      const margin = {{ top: 25, right: 30, bottom: 45, left: 55 }};
      const width = 500;
      const height = 320;
      const chartW = width - margin.left - margin.right;
      const chartH = height - margin.top - margin.bottom;

      const maxQty = Math.max(...prods.map(p => p.qty)) * 1.25;
      const minMargin = 0.20;
      const maxMargin = 0.75;

      // Quadrant lines
      const splitX = margin.left + ((avgQty / maxQty) * chartW);
      const splitY = margin.top + chartH - (((avgMargin - minMargin) / (maxMargin - minMargin)) * chartH);

      // Bubbles
      let bubblesSvg = '';
      const catColors = {{ 'กาแฟ': 'var(--primary-blue)', 'เบเกอรี': 'var(--primary-orange)', 'เครื่องดื่มอื่น': 'var(--accent-cyan)' }};

      prods.forEach(p => {{
        const cx = margin.left + ((p.qty / maxQty) * chartW);
        const cy = margin.top + chartH - (((p.margin - minMargin) / (maxMargin - minMargin)) * chartH);
        // Radius between 10 and 26
        const r = Math.max(10, Math.min(26, Math.sqrt(p.revenue) * 0.22));
        const col = catColors[p.category] || 'var(--primary-blue)';

        bubblesSvg += `
          <g style="cursor: pointer;" onmousemove="showTooltip(event, '<strong>${{p.product}}</strong> (${{p.category}})<br>จำนวนขาย: ${{formatInteger(p.qty)}} ชิ้น<br>อัตรากำไร: ${{formatPercent(p.margin)}}<br>รายได้รวม: ${{formatCurrency(p.revenue)}}<br>กำไรขั้นต้น: ${{formatCurrency(p.profit)}}')" onmouseleave="hideTooltip()">
            <circle cx="${{cx}}" cy="${{cy}}" r="${{r}}" fill="${{col}}" opacity="0.75" stroke="#ffffff" stroke-width="1.5" />
            <text x="${{cx}}" y="${{cy + 3}}" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff" pointer-events="none">${{p.product.slice(0, 3)}}</text>
          </g>
        `;
      }});

      container.innerHTML = `
        <svg viewBox="0 0 ${{width}} ${{height}}" class="interactive-svg">
          <!-- Quadrant borders -->
          <line x1="${{splitX}}" y1="${{margin.top}}" x2="${{splitX}}" y2="${{height - margin.bottom}}" stroke="var(--border-color)" stroke-dasharray="4,4" stroke-width="1.5" />
          <line x1="${{margin.left}}" y1="${{splitY}}" x2="${{width - margin.right}}" y2="${{splitY}}" stroke="var(--border-color)" stroke-dasharray="4,4" stroke-width="1.5" />
          
          <!-- Quadrant labels -->
          <text x="${{width - margin.right - 8}}" y="${{margin.top + 16}}" text-anchor="end" font-size="10" font-weight="700" fill="var(--accent-emerald)">⭐ ดาวเด่น (High Vol, High Margin)</text>
          <text x="${{width - margin.right - 8}}" y="${{height - margin.bottom - 10}}" text-anchor="end" font-size="10" font-weight="700" fill="var(--primary-orange)">📦 ขุมพลังทำเงิน (High Vol, Low Margin)</text>
          <text x="${{margin.left + 8}}" y="${{margin.top + 16}}" text-anchor="start" font-size="10" font-weight="700" fill="var(--accent-cyan)">💎 โอกาสสูง (Low Vol, High Margin)</text>
          <text x="${{margin.left + 8}}" y="${{height - margin.bottom - 10}}" text-anchor="start" font-size="10" font-weight="700" fill="var(--text-subtle)">🔍 ต้องทบทวน (Low Vol, Low Margin)</text>

          <!-- Axes -->
          <line x1="${{margin.left}}" y1="${{height - margin.bottom}}" x2="${{width - margin.right}}" y2="${{height - margin.bottom}}" class="svg-axis-line" />
          <line x1="${{margin.left}}" y1="${{margin.top}}" x2="${{margin.left}}" y2="${{height - margin.bottom}}" class="svg-axis-line" />

          ${{bubblesSvg}}

          <!-- Axis Titles -->
          <text x="${{width / 2}}" y="${{height - 8}}" text-anchor="middle" class="svg-axis-title">จำนวนหน่วยที่ขาย (Units Sold)</text>
          <text x="14" y="${{height / 2}}" text-anchor="middle" transform="rotate(-90, 14, ${{height / 2}})" class="svg-axis-title">อัตรากำไรขั้นต้น (Margin %)</text>
        </svg>
      `;
    }}

    function renderProductMasterTable(data) {{
      const tbody = document.getElementById('productMasterTableBody');
      const pMap = {{}};
      let totalRev = 0;

      data.forEach(x => {{
        if (!pMap[x.product]) {{
          pMap[x.product] = {{ product: x.product, category: x.category, price: x.price, cost: x.cost, qty: 0, revenue: 0, gross_profit: 0 }};
        }}
        pMap[x.product].qty += x.qty;
        pMap[x.product].revenue += x.revenue;
        pMap[x.product].gross_profit += x.gross_profit;
        totalRev += x.revenue;
      }});

      let list = Object.values(pMap).map(p => ({{
        ...p,
        margin: p.revenue > 0 ? (p.gross_profit / p.revenue) : 0,
        unitProfit: p.price - p.cost
      }}));

      // Calculate ABC rank
      list.sort((a, b) => b.revenue - a.revenue);
      let cum = 0;
      list.forEach(p => {{
        const priorCumPct = (cum / totalRev) * 100;
        cum += p.revenue;
        p.abc = priorCumPct < 80 ? 'A' : (priorCumPct < 95 ? 'B' : 'C');
      }});

      const col = state.productTable.sortCol;
      const asc = state.productTable.sortAsc;
      list.sort((a, b) => asc ? (a[col] > b[col] ? 1 : -1) : (a[col] < b[col] ? 1 : -1));

      tbody.innerHTML = list.map(p => `
        <tr>
          <td style="font-weight: 700;">${{p.product}}</td>
          <td>${{p.category}}</td>
          <td class="text-center">
            <span class="badge" style="background: ${{p.abc === 'A' ? 'rgba(37,99,235,0.15)' : (p.abc === 'B' ? 'rgba(234,88,12,0.15)' : 'rgba(148,163,184,0.15)')}}; color: ${{p.abc === 'A' ? 'var(--primary-blue)' : (p.abc === 'B' ? 'var(--primary-orange)' : 'var(--text-muted)')}};">
              กลุ่ม ${{p.abc}}
            </span>
          </td>
          <td class="text-right">฿${{p.price.toFixed(2)}}</td>
          <td class="text-right">฿${{p.cost.toFixed(2)}}</td>
          <td class="text-right">${{formatInteger(p.qty)}}</td>
          <td class="text-right" style="font-weight: 700;">${{formatCurrency(p.revenue)}}</td>
          <td class="text-right" style="color: var(--accent-emerald); font-weight: 600;">${{formatCurrency(p.gross_profit)}}</td>
          <td class="text-right">${{formatPercent(p.margin)}}</td>
        </tr>
      `).join('');
    }}

    function sortProductTable(col) {{
      if (state.productTable.sortCol === col) state.productTable.sortAsc = !state.productTable.sortAsc;
      else {{ state.productTable.sortCol = col; state.productTable.sortAsc = false; }}
      renderProductMasterTable(getFilteredData());
    }}

    // --- 8. TAB 4: TIME TRENDS & CALENDAR ---
    function renderTrendsTab(data) {{
      renderCumulativeTrend(data);
      renderDowChart(data);
      renderCalendarGrid(data);
    }}

    function renderCumulativeTrend(data) {{
      const container = document.getElementById('cumulativeTrendChart');
      // Aggregate by date from 2026-08-01 to 2026-08-31
      const dateMap = {{}};
      for (let day = 1; day <= 31; day++) {{
        const dStr = `2026-08-${{String(day).padStart(2, '0')}}`;
        dateMap[dStr] = 0;
      }}
      data.forEach(x => {{
        if (dateMap[x.date] !== undefined) dateMap[x.date] += x.revenue;
      }});

      const dates = Object.keys(dateMap).sort();
      let runningSum = 0;
      const trendPoints = dates.map(d => {{
        runningSum += dateMap[d];
        return {{ date: d, day: d.slice(8), daily: dateMap[d], cum: runningSum }};
      }});

      const maxCum = Math.max(...trendPoints.map(p => p.cum), 1);
      const margin = {{ top: 20, right: 30, bottom: 40, left: 75 }};
      const width = 800;
      const height = 280;
      const chartW = width - margin.left - margin.right;
      const chartH = height - margin.top - margin.bottom;

      let gridLines = '';
      for (let i = 0; i <= 4; i++) {{
        const val = (maxCum / 4) * i;
        const y = margin.top + chartH - (i / 4) * chartH;
        gridLines += `
          <line x1="${{margin.left}}" y1="${{y}}" x2="${{width - margin.right}}" y2="${{y}}" class="svg-grid-line" />
          <text x="${{margin.left - 8}}" y="${{y + 4}}" text-anchor="end" class="svg-axis-text">${{formatCurrency(val)}}</text>
        `;
      }}

      const coords = trendPoints.map((p, idx) => {{
        const x = margin.left + (idx / (trendPoints.length - 1)) * chartW;
        const y = margin.top + chartH - ((p.cum / maxCum) * chartH);
        return {{ x, y, ...p }};
      }});

      const areaPoints = [`${{margin.left}},${{margin.top + chartH}}`, ...coords.map(c => `${{c.x}},${{c.y}}`), `${{width - margin.right}},${{margin.top + chartH}}`].join(' ');
      const linePoints = coords.map(c => `${{c.x}},${{c.y}}`).join(' ');

      const circles = coords.filter((c, i) => i % 3 === 0 || i === coords.length - 1).map(c => `
        <circle cx="${{c.x}}" cy="${{c.y}}" r="3.5" fill="#ffffff" stroke="var(--primary-blue)" stroke-width="2" style="cursor: pointer;" onmousemove="showTooltip(event, 'วันที่ ${{c.date}}<br>ยอดขายวันนั้น: ${{formatCurrency(c.daily)}}<br>ยอดสะสม: ${{formatCurrency(c.cum)}}')" onmouseleave="hideTooltip()" />
      `).join('');

      container.innerHTML = `
        <svg viewBox="0 0 ${{width}} ${{height}}" class="interactive-svg">
          <defs>
            <linearGradient id="areaGrad" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stop-color="var(--primary-blue)" stop-opacity="0.35" />
              <stop offset="100%" stop-color="var(--primary-blue)" stop-opacity="0.02" />
            </linearGradient>
          </defs>
          ${{gridLines}}
          <polygon fill="url(#areaGrad)" points="${{areaPoints}}" />
          <polyline fill="none" stroke="var(--primary-blue)" stroke-width="2.5" points="${{linePoints}}" />
          ${{circles}}
          <!-- X Axis Dates -->
          <line x1="${{margin.left}}" y1="${{height - margin.bottom}}" x2="${{width - margin.right}}" y2="${{height - margin.bottom}}" class="svg-axis-line" />
          <text x="${{margin.left}}" y="${{height - 12}}" class="svg-axis-text">1 ส.ค.</text>
          <text x="${{margin.left + chartW * 0.25}}" y="${{height - 12}}" class="svg-axis-text">8 ส.ค.</text>
          <text x="${{margin.left + chartW * 0.5}}" y="${{height - 12}}" class="svg-axis-text">15 ส.ค.</text>
          <text x="${{margin.left + chartW * 0.75}}" y="${{height - 12}}" class="svg-axis-text">22 ส.ค.</text>
          <text x="${{width - margin.right}}" y="${{height - 12}}" text-anchor="end" class="svg-axis-text">31 ส.ค.</text>
        </svg>
      `;
    }}

    function renderDowChart(data) {{
      const container = document.getElementById('dowChartContainer');
      const metric = state.globalMetric;

      const dowMap = {{}};
      DOW_ORDER.forEach(d => dowMap[d] = {{ dow: d, val: 0, revenue: 0, profit: 0, qty: 0 }});
      data.forEach(x => {{
        if (dowMap[x.dayOfWeek]) {{
          dowMap[x.dayOfWeek].val += x[metric];
          dowMap[x.dayOfWeek].revenue += x.revenue;
          dowMap[x.dayOfWeek].profit += x.gross_profit;
          dowMap[x.dayOfWeek].qty += x.qty;
        }}
      }});

      const items = DOW_ORDER.map(d => dowMap[d]);
      const maxVal = Math.max(...items.map(x => x.val), 1);
      const avgVal = items.reduce((acc, x) => acc + x.val, 0) / items.length;

      const margin = {{ top: 25, right: 25, bottom: 40, left: 75 }};
      const width = 500;
      const height = 280;
      const chartW = width - margin.left - margin.right;
      const chartH = height - margin.top - margin.bottom;
      const colW = chartW / items.length;
      const barW = colW * 0.65;

      const avgY = margin.top + chartH - ((avgVal / maxVal) * chartH);

      let bars = items.map((item, idx) => {{
        const cx = margin.left + (idx * colW) + (colW / 2);
        const barH = (item.val / maxVal) * chartH;
        const barY = margin.top + chartH - barH;
        const isWeekend = ['วันเสาร์', 'วันอาทิตย์'].includes(item.dow);
        const col = isWeekend ? 'var(--primary-orange)' : 'var(--primary-blue)';
        const formattedVal = metric === 'qty' ? formatInteger(item.val) : formatCurrency(item.val);

        return `
          <g style="cursor: pointer;" onmousemove="showTooltip(event, '<strong>${{item.dow}}</strong><br>ค่า: ${{formattedVal}}<br>รายได้: ${{formatCurrency(item.revenue)}}<br>กำไร: ${{formatCurrency(item.profit)}}<br>จำนวน: ${{formatInteger(item.qty)}} ชิ้น')" onmouseleave="hideTooltip()">
            <rect x="${{cx - barW / 2}}" y="${{barY}}" width="${{barW}}" height="${{barH}}" rx="4" fill="${{col}}" opacity="0.9" />
            <text x="${{cx}}" y="${{height - margin.bottom + 16}}" text-anchor="middle" font-size="10.5" font-weight="600" fill="var(--text-main)">${{item.dow.replace('วัน', '')}}</text>
          </g>
        `;
      }}).join('');

      container.innerHTML = `
        <svg viewBox="0 0 ${{width}} ${{height}}" class="interactive-svg">
          <line x1="${{margin.left}}" y1="${{height - margin.bottom}}" x2="${{width - margin.right}}" y2="${{height - margin.bottom}}" class="svg-axis-line" />
          <line x1="${{margin.left}}" y1="${{avgY}}" x2="${{width - margin.right}}" y2="${{avgY}}" stroke="#94a3b8" stroke-dasharray="4,4" stroke-width="1.5" />
          <text x="${{width - margin.right}}" y="${{avgY - 4}}" text-anchor="end" font-size="10" fill="var(--text-muted)">เฉลี่ย: ${{metric === 'qty' ? formatInteger(avgVal) : formatCurrency(avgVal)}}</text>
          ${{bars}}
        </svg>
      `;
    }}

    function renderCalendarGrid(data) {{
      const container = document.getElementById('calendarGridContainer');
      const daySales = {{}};
      let maxDaily = 0;

      data.forEach(x => {{
        daySales[x.date] = (daySales[x.date] || 0) + x.revenue;
        if (daySales[x.date] > maxDaily) maxDaily = daySales[x.date];
      }});

      // August 2026: Day 1 is Saturday (dayOfWeek = 6 in Sun=0 based)
      // If Monday is col 0, Sat is col 5. Empty cells for Mon..Fri (5 cells)
      let html = '';
      for (let empty = 0; empty < 5; empty++) {{
        html += '<div class="cal-day-cell empty"></div>';
      }}

      for (let day = 1; day <= 31; day++) {{
        const dStr = `2026-08-${{String(day).padStart(2, '0')}}`;
        const rev = daySales[dStr] || 0;
        const intensity = maxDaily > 0 ? (rev / maxDaily) : 0;
        const bg = intensity > 0 
          ? `rgba(234, 88, 12, ${{Math.max(0.15, intensity * 0.9)}})` 
          : 'var(--bg-card-subtle)';
        const textColor = intensity > 0.55 ? '#ffffff' : 'var(--text-main)';

        html += `
          <div class="cal-day-cell" style="background: ${{bg}}; color: ${{textColor}};" onclick="setDateFilterSingle('${{dStr}}')" onmousemove="showTooltip(event, '${{dStr}}<br>รายได้: ${{formatCurrency(rev)}}')" onmouseleave="hideTooltip()">
            <span style="font-weight: 700;">${{day}}</span>
            <span style="font-size: 0.65rem;">${{rev > 0 ? '฿' + Math.round(rev) : '-'}}</span>
          </div>
        `;
      }}

      container.innerHTML = html;
    }}

    function setDateFilterSingle(dateStr) {{
      document.getElementById('filterStartDate').value = dateStr;
      document.getElementById('filterEndDate').value = dateStr;
      state.filters.startDate = dateStr;
      state.filters.endDate = dateStr;
      onFilterChange();
    }}

    // --- 9. TAB 5: TRANSACTIONS TABLE & PAGINATION ---
    function renderTxTable(data) {{
      const tbody = document.getElementById('txTableBody');
      const search = state.txTable.search.toLowerCase().trim();

      let filtered = data;
      if (search) {{
        filtered = data.filter(x => 
          x.id.toLowerCase().includes(search) ||
          x.product.toLowerCase().includes(search) ||
          x.branch.toLowerCase().includes(search) ||
          x.category.toLowerCase().includes(search) ||
          x.date.includes(search)
        );
      }}

      const col = state.txTable.sortCol;
      const asc = state.txTable.sortAsc;
      filtered.sort((a, b) => asc ? (a[col] > b[col] ? 1 : -1) : (a[col] < b[col] ? 1 : -1));

      const totalRows = filtered.length;
      const pageSize = state.txTable.pageSize;
      const totalPages = Math.ceil(totalRows / pageSize) || 1;
      if (state.txTable.page > totalPages) state.txTable.page = totalPages;

      const startIdx = (state.txTable.page - 1) * pageSize;
      const pageRows = filtered.slice(startIdx, startIdx + pageSize);

      if (pageRows.length === 0) {{
        tbody.innerHTML = '<tr><td colspan="12" class="text-center" style="padding: 30px; color: var(--text-muted);">ไม่พบรายการที่ค้นหา</td></tr>';
      }} else {{
        tbody.innerHTML = pageRows.map(r => `
          <tr>
            <td style="font-weight: 700; color: var(--primary-blue);">${{r.id}}</td>
            <td>${{r.date}}</td>
            <td>${{r.dayOfWeek.replace('วัน', '')}}</td>
            <td>${{r.branch}}</td>
            <td style="font-weight: 600;">${{r.product}}</td>
            <td>${{r.category}}</td>
            <td class="text-right">${{formatInteger(r.qty)}}</td>
            <td class="text-right">฿${{r.price.toFixed(2)}}</td>
            <td class="text-right">฿${{r.cost.toFixed(2)}}</td>
            <td class="text-right" style="font-weight: 700;">${{formatCurrency(r.revenue)}}</td>
            <td class="text-right" style="color: var(--accent-emerald); font-weight: 600;">${{formatCurrency(r.gross_profit)}}</td>
            <td class="text-right">${{formatPercent(r.margin)}}</td>
          </tr>
        `).join('');
      }}

      // Update Pagination info
      document.getElementById('txPaginationInfo').textContent = 
        `กำลังแสดง ${{totalRows > 0 ? startIdx + 1 : 0}}–${{Math.min(startIdx + pageSize, totalRows)}} จาก ${{totalRows}} รายการ`;

      // Render pagination buttons
      const nav = document.getElementById('txPageNav');
      let navHtml = `
        <button onclick="goToPage(1)" ${{state.txTable.page === 1 ? 'disabled' : ''}}>« แรก</button>
        <button onclick="goToPage(${{state.txTable.page - 1}})" ${{state.txTable.page === 1 ? 'disabled' : ''}}>‹ ก่อน</button>
      `;
      for (let p = 1; p <= totalPages; p++) {{
        if (p === 1 || p === totalPages || (p >= state.txTable.page - 1 && p <= state.txTable.page + 1)) {{
          navHtml += `<button class="${{p === state.txTable.page ? 'active' : ''}}" onclick="goToPage(${{p}})">${{p}}</button>`;
        }} else if (p === state.txTable.page - 2 || p === state.txTable.page + 2) {{
          navHtml += '<span style="padding: 0 4px;">...</span>';
        }}
      }}
      navHtml += `
        <button onclick="goToPage(${{state.txTable.page + 1}})" ${{state.txTable.page === totalPages ? 'disabled' : ''}}>ถัดไป ›</button>
        <button onclick="goToPage(${{totalPages}})" ${{state.txTable.page === totalPages ? 'disabled' : ''}}>ท้าย »</button>
      `;
      nav.innerHTML = navHtml;
    }}

    function handleTxSearch() {{
      state.txTable.search = document.getElementById('txSearchInput').value;
      state.txTable.page = 1;
      renderTxTable(getFilteredData());
    }}

    function changePageSize(val) {{
      state.txTable.pageSize = Number(val);
      state.txTable.page = 1;
      renderTxTable(getFilteredData());
    }}

    function goToPage(p) {{
      state.txTable.page = p;
      renderTxTable(getFilteredData());
    }}

    function sortTxTable(col) {{
      if (state.txTable.sortCol === col) state.txTable.sortAsc = !state.txTable.sortAsc;
      else {{ state.txTable.sortCol = col; state.txTable.sortAsc = true; }}
      renderTxTable(getFilteredData());
    }}

    // Export CSV with UTF-8 BOM
    function exportFilteredCSV() {{
      const data = getFilteredData();
      let csv = '\\uFEFF'; // BOM for Excel Thai support
      csv += 'รหัสรายการ,วันที่,วันในสัปดาห์,สาขา,สินค้า,หมวดหมู่,จำนวนขาย (หน่วย),ราคาขายต่อหน่วย (บาท),ต้นทุนต่อหน่วย (บาท),รายได้ (บาท),กำไรขั้นต้น (บาท),อัตรากำไรขั้นต้น\\n';

      data.forEach(r => {{
        csv += `"${{r.id}}","${{r.date}}","${{r.dayOfWeek}}","${{r.branch}}","${{r.product}}","${{r.category}}",${{r.qty}},${{r.price}},${{r.cost}},${{r.revenue}},${{r.gross_profit}},${{r.margin.toFixed(4)}}\\n`;
      }});

      const blob = new Blob([csv], {{ type: 'text/csv;charset=utf-8;' }});
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.setAttribute('href', url);
      link.setAttribute('download', `sales_export_${{new Date().toISOString().slice(0, 10)}}.csv`);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }}

    // --- 10. WHAT-IF PROFIT SIMULATOR ---
    function toggleSimulator() {{
      const el = document.getElementById('simulatorSection');
      el.style.display = (el.style.display === 'none') ? 'block' : 'none';
      if (el.style.display === 'block') updateSimulation();
    }}

    function updateSimulation() {{
      const pSlider = document.getElementById('simPriceSlider');
      const cSlider = document.getElementById('simCostSlider');
      if (!pSlider || !cSlider) return;

      const pPct = Number(pSlider.value);
      const cPct = Number(cSlider.value);

      document.getElementById('simPriceVal').textContent = (pPct >= 0 ? '+' : '') + pPct + '%';
      document.getElementById('simCostVal').textContent = (cPct >= 0 ? '+' : '') + cPct + '%';

      const data = getFilteredData();
      let baselineRevenue = 0;
      let baselineProfit = 0;
      let simRevenue = 0;
      let simProfit = 0;

      data.forEach(x => {{
        baselineRevenue += x.revenue;
        baselineProfit += x.gross_profit;

        const newPrice = x.price * (1 + (pPct / 100));
        const newCost = x.cost * (1 + (cPct / 100));
        simRevenue += x.qty * newPrice;
        simProfit += x.qty * (newPrice - newCost);
      }});

      const simMargin = simRevenue > 0 ? (simProfit / simRevenue) : 0;
      const deltaProfit = simProfit - baselineProfit;

      document.getElementById('simProjRevenue').textContent = formatCurrency(simRevenue);
      document.getElementById('simProjProfit').textContent = formatCurrency(simProfit);
      document.getElementById('simProjMargin').textContent = formatPercent(simMargin);

      const deltaEl = document.getElementById('simDeltaProfit');
      deltaEl.textContent = (deltaProfit >= 0 ? '+' : '') + formatCurrency(deltaProfit);
      deltaEl.style.color = deltaProfit >= 0 ? 'var(--accent-emerald)' : 'var(--accent-rose)';
    }}

    function resetSimulator() {{
      document.getElementById('simPriceSlider').value = 0;
      document.getElementById('simCostSlider').value = 0;
      updateSimulation();
    }}

    // --- 11. TOOLTIPS & MODALS ---
    const tooltip = document.getElementById('globalTooltip');
    function showTooltip(e, text) {{
      tooltip.innerHTML = text;
      tooltip.style.display = 'block';
      const x = e.pageX + 14;
      const y = e.pageY + 14;
      tooltip.style.left = x + 'px';
      tooltip.style.top = y + 'px';
    }}
    function hideTooltip() {{
      tooltip.style.display = 'none';
    }}

    function openAuditModal() {{
      document.getElementById('auditModal').classList.add('active');
    }}
    function closeAuditModal() {{
      document.getElementById('auditModal').classList.remove('active');
    }}

    // --- 12. THEME & PRINT ---
    function initThemeAndPrint() {{
      const btnTheme = document.getElementById('btnThemeToggle');
      btnTheme.addEventListener('click', () => {{
        const isDark = document.body.getAttribute('data-theme') === 'dark';
        if (isDark) {{
          document.body.removeAttribute('data-theme');
          btnTheme.textContent = '🌙 สลับธีม';
        }} else {{
          document.body.setAttribute('data-theme', 'dark');
          btnTheme.textContent = '☀️ ธีมสว่าง';
        }}
        // Re-render charts to adjust text color
        onFilterChange();
      }});

      document.getElementById('btnPrint').addEventListener('click', () => window.print());
      document.getElementById('btnDownloadCSV').addEventListener('click', exportFilteredCSV);
      document.getElementById('btnAuditReport').addEventListener('click', openAuditModal);
    }}

    // Initializer
    window.addEventListener('DOMContentLoaded', () => {{
      initFilterPills();
      initThemeAndPrint();
      onFilterChange();
    }});
  </script>
</body>
</html>'''

with open(r'e:\1Amazon_Quick_Workshop test\dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Successfully generated dashboard.html with size: {os.path.getsize(r'e:\1Amazon_Quick_Workshop test\dashboard.html')} bytes")
