import sys

with open(r'e:\1Amazon_Quick_Workshop test\app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Helper function for clean round tick calculation
nice_max_helper = """
    function getNiceMax(val) {
      if (val <= 0) return 100;
      const target = val * 1.15;
      const rough = target / 5;
      const mag = Math.pow(10, Math.floor(Math.log10(rough)));
      const factor = rough / mag;
      let step;
      if (factor <= 1.2) step = 1 * mag;
      else if (factor <= 2.2) step = 2 * mag;
      else if (factor <= 3) step = 2.5 * mag;
      else if (factor <= 7) step = 5 * mag;
      else step = 10 * mag;
      return Math.ceil(target / step) * step;
    }
"""

# Let's inspect where renderTopProductsChart starts
# We can replace renderParetoChart, renderScatterPlot, renderDowChart, renderTopProductsChart with improved versions.

new_pareto = """    function renderParetoChart(data) {
      const container = document.getElementById('paretoChartContainer');
      const summaryBanner = document.getElementById('abcSummaryBanner');
      const metric = state.globalMetric;

      const pMap = {};
      let totalVal = 0;
      data.forEach(x => {
        if (!pMap[x.product]) pMap[x.product] = { product: x.product, category: x.category, val: 0, revenue: 0, profit: 0, qty: 0 };
        pMap[x.product].val += x[metric];
        pMap[x.product].revenue += x.revenue;
        pMap[x.product].profit += x.gross_profit;
        pMap[x.product].qty += x.qty;
        totalVal += x[metric];
      });

      const prods = Object.values(pMap).sort((a, b) => b.val - a.val);
      if (prods.length === 0 || totalVal === 0) {
        container.innerHTML = '<div style="padding: 40px; text-align: center; color: var(--text-muted);">ไม่มีข้อมูลสำหรับวิเคราะห์ ABC</div>';
        summaryBanner.innerHTML = '';
        return;
      }

      // Classify ABC: Prior cumulative < 80% => A, < 95% => B, else => C
      let cum = 0;
      let countA = 0, countB = 0, countC = 0;
      let valA = 0, valB = 0, valC = 0;

      prods.forEach(p => {
        const priorCumPct = (cum / totalVal) * 100;
        cum += p.val;
        p.cumPct = (cum / totalVal) * 100;

        if (priorCumPct < 80) {
          p.abc = 'A';
          countA++;
          valA += p.val;
        } else if (priorCumPct < 95) {
          p.abc = 'B';
          countB++;
          valB += p.val;
        } else {
          p.abc = 'C';
          countC++;
          valC += p.val;
        }
      });

      // SVG Dual-Axis Pareto with generous spacing and no text collisions
      const margin = { top: 48, right: 65, bottom: 85, left: 80 };
      const width = 860;
      const height = 380;
      const chartW = width - margin.left - margin.right;
      const chartH = height - margin.top - margin.bottom;

      // Nice round ticks for left Y axis
      const maxVal = getNiceMax(prods[0].val);
      const colW = chartW / prods.length;
      const barW = Math.max(20, Math.min(56, colW * 0.62));

      let gridLines = '';
      for (let i = 0; i <= 5; i++) {
        const p = (i / 5) * 100;
        const val = (i / 5) * maxVal;
        const y = margin.top + chartH - (i / 5) * chartH;
        gridLines += `
          <line x1="${margin.left}" y1="${y}" x2="${width - margin.right}" y2="${y}" class="svg-grid-line" />
          <text x="${margin.left - 10}" y="${y + 4}" text-anchor="end" class="svg-axis-text" font-weight="600">${formatInteger(val)}</text>
          <text x="${width - margin.right + 10}" y="${y + 4}" text-anchor="start" class="svg-axis-text" font-weight="600">${p}%</text>
        `;
      }

      // Reference lines at 80% & 95% placed cleanly on LEFT (where cumulative curve is low, zero collision!)
      const y80 = margin.top + chartH - (0.80 * chartH);
      const y95 = margin.top + chartH - (0.95 * chartH);
      const refLines = `
        <!-- 95% Line & Badge -->
        <line x1="${margin.left}" y1="${y95}" x2="${width - margin.right}" y2="${y95}" stroke="#f59e0b" stroke-dasharray="6,4" stroke-width="1.5" />
        <g transform="translate(${margin.left + 14}, ${y95 - 11})">
          <rect x="0" y="0" width="132" height="20" rx="4" fill="var(--bg-card)" stroke="#f59e0b" stroke-width="1.2" opacity="0.96" />
          <text x="66" y="14" text-anchor="middle" fill="#d97706" font-size="10.5" font-weight="700">เกณฑ์ 95% (กลุ่ม B)</text>
        </g>

        <!-- 80% Line & Badge -->
        <line x1="${margin.left}" y1="${y80}" x2="${width - margin.right}" y2="${y80}" stroke="#ea580c" stroke-dasharray="6,4" stroke-width="1.5" />
        <g transform="translate(${margin.left + 14}, ${y80 - 11})">
          <rect x="0" y="0" width="132" height="20" rx="4" fill="var(--bg-card)" stroke="#ea580c" stroke-width="1.2" opacity="0.96" />
          <text x="66" y="14" text-anchor="middle" fill="#ea580c" font-size="10.5" font-weight="700">เกณฑ์ 80% (กลุ่ม A)</text>
        </g>
      `;

      let barsSvg = '';
      const linePoints = [];

      prods.forEach((p, idx) => {
        const cx = margin.left + (idx * colW) + (colW / 2);
        const barH = (p.val / maxVal) * chartH;
        const barY = margin.top + chartH - barH;
        const lineY = margin.top + chartH - ((p.cumPct / 100) * chartH);
        linePoints.push(`${cx},${lineY}`);

        const color = p.abc === 'A' ? 'var(--primary-blue)' : (p.abc === 'B' ? 'var(--primary-orange)' : '#94a3b8');

        barsSvg += `
          <g style="cursor: pointer;" onmousemove="showTooltip(event, '<strong>${p.product}</strong> [กลุ่ม ${p.abc}]<br>${metric === 'qty' ? 'จำนวน' : (metric === 'gross_profit' ? 'กำไร' : 'รายได้')}: ${metric === 'qty' ? formatInteger(p.val) + ' ชิ้น' : formatCurrency(p.val)}<br>สัดส่วนสะสม: ${p.cumPct.toFixed(1)}%')" onmouseleave="hideTooltip()">
            <!-- Bar -->
            <rect x="${cx - barW / 2}" y="${barY}" width="${barW}" height="${barH}" rx="5" fill="${color}" opacity="0.9" />
            <!-- Clean badge INSIDE bar (Never collides with cumulative line above!) -->
            <rect x="${cx - 15}" y="${barY + 6}" width="30" height="20" rx="4" fill="rgba(0, 0, 0, 0.35)" />
            <text x="${cx}" y="${barY + 20}" text-anchor="middle" font-size="11.5" font-weight="800" fill="#ffffff" pointer-events="none">${p.abc}</text>
            <!-- X-Axis Label -->
            <text x="${cx - 6}" y="${height - margin.bottom + 18}" text-anchor="end" transform="rotate(-35, ${cx - 6}, ${height - margin.bottom + 18})" font-size="11.5" font-weight="600" fill="var(--text-main)">${p.product}</text>
          </g>
        `;
      });

      // Line path
      const linePath = `<polyline fill="none" stroke="#ea580c" stroke-width="3" points="${linePoints.join(' ')}" />`;
      const pointsSvg = linePoints.map((pt, i) => `
        <circle cx="${pt.split(',')[0]}" cy="${pt.split(',')[1]}" r="4.5" fill="#ffffff" stroke="#ea580c" stroke-width="2.5" />
      `).join('');

      container.innerHTML = `
        <svg viewBox="0 0 ${width} ${height}" class="interactive-svg">
          ${gridLines}
          ${refLines}
          ${barsSvg}
          ${linePath}
          ${pointsSvg}
          <!-- Axis titles with ample top spacing -->
          <text x="${margin.left}" y="24" class="svg-axis-title">มูลค่าตัวชี้วัด</text>
          <text x="${width - margin.right}" y="24" text-anchor="end" class="svg-axis-title">% สะสม (Cumulative %)</text>
        </svg>
      `;

      // ABC summary box
      summaryBanner.innerHTML = `
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px;">
          <div>
            <strong style="color: var(--primary-blue);">กลุ่ม A (${countA} รายการ):</strong> ${((valA / totalVal) * 100).toFixed(1)}% ของมูลค่ารวม
            <div style="font-size: 0.78rem; color: var(--text-muted);">สินค้าสร้างรายได้หลัก ควรบริหารสต็อกห้ามขาด</div>
          </div>
          <div>
            <strong style="color: var(--primary-orange);">กลุ่ม B (${countB} รายการ):</strong> ${((valB / totalVal) * 100).toFixed(1)}% ของมูลค่ารวม
            <div style="font-size: 0.78rem; color: var(--text-muted);">สินค้าทำเงินระดับรอง จัดโปรโมชันกระตุ้นยอดได้</div>
          </div>
          <div>
            <strong style="color: var(--text-muted);">กลุ่ม C (${countC} รายการ):</strong> ${((valC / totalVal) * 100).toFixed(1)}% ของมูลค่ารวม
            <div style="font-size: 0.78rem; color: var(--text-muted);">สินค้าหางยาว ติดตามต้นทุนและสต็อกอย่างรัดกุม</div>
          </div>
        </div>
      `;
    }"""

new_scatter = """    function renderScatterPlot(data) {
      const container = document.getElementById('scatterChartContainer');
      const prodStats = {};
      let totalQty = 0, totalProfit = 0, totalRev = 0;

      data.forEach(x => {
        if (!prodStats[x.product]) {
          prodStats[x.product] = { product: x.product, category: x.category, qty: 0, revenue: 0, profit: 0 };
        }
        prodStats[x.product].qty += x.qty;
        prodStats[x.product].revenue += x.revenue;
        prodStats[x.product].profit += x.gross_profit;
        totalQty += x.qty;
        totalProfit += x.gross_profit;
        totalRev += x.revenue;
      });

      const prods = Object.values(prodStats).map(p => ({
        ...p,
        margin: p.revenue > 0 ? (p.profit / p.revenue) : 0
      }));

      if (prods.length === 0) {
        container.innerHTML = '<div style="padding: 40px; text-align: center; color: var(--text-muted);">ไม่มีข้อมูล</div>';
        return;
      }

      const avgQty = totalQty / prods.length;
      const avgMargin = totalRev > 0 ? (totalProfit / totalRev) : 0;

      const margin = { top: 38, right: 35, bottom: 48, left: 60 };
      const width = 520;
      const height = 330;
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
      const catColors = { 'กาแฟ': 'var(--primary-blue)', 'เบเกอรี': 'var(--primary-orange)', 'เครื่องดื่มอื่น': 'var(--accent-cyan)' };

      prods.forEach(p => {
        const cx = margin.left + ((p.qty / maxQty) * chartW);
        const cy = margin.top + chartH - (((p.margin - minMargin) / (maxMargin - minMargin)) * chartH);
        const r = Math.max(12, Math.min(26, Math.sqrt(p.revenue) * 0.22));
        const col = catColors[p.category] || 'var(--primary-blue)';

        bubblesSvg += `
          <g style="cursor: pointer;" onmousemove="showTooltip(event, '<strong>${p.product}</strong> (${p.category})<br>จำนวนขาย: ${formatInteger(p.qty)} ชิ้น<br>อัตรากำไร: ${formatPercent(p.margin)}<br>รายได้รวม: ${formatCurrency(p.revenue)}<br>กำไรขั้นต้น: ${formatCurrency(p.profit)}')" onmouseleave="hideTooltip()">
            <circle cx="${cx}" cy="${cy}" r="${r}" fill="${col}" opacity="0.8" stroke="#ffffff" stroke-width="1.5" />
            <text x="${cx}" y="${cy + 3.5}" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff" pointer-events="none">${p.product.slice(0, 3)}</text>
          </g>
        `;
      });

      container.innerHTML = `
        <svg viewBox="0 0 ${width} ${height}" class="interactive-svg">
          <!-- Quadrant borders -->
          <line x1="${splitX}" y1="${margin.top}" x2="${splitX}" y2="${height - margin.bottom}" stroke="var(--border-color)" stroke-dasharray="4,4" stroke-width="1.5" />
          <line x1="${margin.left}" y1="${splitY}" x2="${width - margin.right}" y2="${splitY}" stroke="var(--border-color)" stroke-dasharray="4,4" stroke-width="1.5" />
          
          <!-- Quadrant labels with background badges (Never collide!) -->
          <g transform="translate(${width - margin.right - 180}, ${margin.top + 6})">
            <rect x="0" y="0" width="176" height="20" rx="4" fill="var(--bg-card)" stroke="var(--border-color)" opacity="0.9" />
            <text x="88" y="14" text-anchor="middle" font-size="9.5" font-weight="700" fill="var(--accent-emerald)">⭐ ดาวเด่น (High Vol, High Margin)</text>
          </g>
          <g transform="translate(${width - margin.right - 180}, ${height - margin.bottom - 24})">
            <rect x="0" y="0" width="176" height="20" rx="4" fill="var(--bg-card)" stroke="var(--border-color)" opacity="0.9" />
            <text x="88" y="14" text-anchor="middle" font-size="9.5" font-weight="700" fill="var(--primary-orange)">📦 ขุมพลังทำเงิน (High Vol, Low Margin)</text>
          </g>
          <g transform="translate(${margin.left + 6}, ${margin.top + 6})">
            <rect x="0" y="0" width="168" height="20" rx="4" fill="var(--bg-card)" stroke="var(--border-color)" opacity="0.9" />
            <text x="84" y="14" text-anchor="middle" font-size="9.5" font-weight="700" fill="var(--accent-cyan)">💎 โอกาสสูง (Low Vol, High Margin)</text>
          </g>
          <g transform="translate(${margin.left + 6}, ${height - margin.bottom - 24})">
            <rect x="0" y="0" width="168" height="20" rx="4" fill="var(--bg-card)" stroke="var(--border-color)" opacity="0.9" />
            <text x="84" y="14" text-anchor="middle" font-size="9.5" font-weight="700" fill="var(--text-subtle)">🔍 ต้องทบทวน (Low Vol, Low Margin)</text>
          </g>

          <!-- Axes -->
          <line x1="${margin.left}" y1="${height - margin.bottom}" x2="${width - margin.right}" y2="${height - margin.bottom}" class="svg-axis-line" />
          <line x1="${margin.left}" y1="${margin.top}" x2="${margin.left}" y2="${height - margin.bottom}" class="svg-axis-line" />

          ${bubblesSvg}

          <!-- Axis Titles -->
          <text x="${width / 2}" y="${height - 10}" text-anchor="middle" class="svg-axis-title">จำนวนหน่วยที่ขาย (Units Sold)</text>
          <text x="14" y="${height / 2}" text-anchor="middle" transform="rotate(-90, 14, ${height / 2})" class="svg-axis-title">อัตรากำไรขั้นต้น (Margin %)</text>
        </svg>
      `;
    }"""

new_dow = """    function renderDowChart(data) {
      const container = document.getElementById('dowChartContainer');
      const metric = state.globalMetric;

      const dowMap = {};
      DOW_ORDER.forEach(d => dowMap[d] = { dow: d, val: 0, revenue: 0, profit: 0, qty: 0 });
      data.forEach(x => {
        if (dowMap[x.dayOfWeek]) {
          dowMap[x.dayOfWeek].val += x[metric];
          dowMap[x.dayOfWeek].revenue += x.revenue;
          dowMap[x.dayOfWeek].profit += x.gross_profit;
          dowMap[x.dayOfWeek].qty += x.qty;
        }
      });

      const items = DOW_ORDER.map(d => dowMap[d]);
      const maxVal = getNiceMax(Math.max(...items.map(x => x.val), 1));
      const avgVal = items.reduce((acc, x) => acc + x.val, 0) / items.length;

      const margin = { top: 35, right: 30, bottom: 45, left: 75 };
      const width = 520;
      const height = 290;
      const chartW = width - margin.left - margin.right;
      const chartH = height - margin.top - margin.bottom;
      const colW = chartW / items.length;
      const barW = Math.max(16, colW * 0.62);

      const avgY = margin.top + chartH - ((avgVal / maxVal) * chartH);

      let gridLines = '';
      for (let i = 0; i <= 4; i++) {
        const val = (i / 4) * maxVal;
        const y = margin.top + chartH - (i / 4) * chartH;
        gridLines += `
          <line x1="${margin.left}" y1="${y}" x2="${width - margin.right}" y2="${y}" class="svg-grid-line" />
          <text x="${margin.left - 8}" y="${y + 4}" text-anchor="end" class="svg-axis-text">${formatInteger(val)}</text>
        `;
      }

      let bars = items.map((item, idx) => {
        const cx = margin.left + (idx * colW) + (colW / 2);
        const barH = (item.val / maxVal) * chartH;
        const barY = margin.top + chartH - barH;
        const isWeekend = ['วันเสาร์', 'วันอาทิตย์'].includes(item.dow);
        const col = isWeekend ? 'var(--primary-orange)' : 'var(--primary-blue)';
        const formattedVal = metric === 'qty' ? formatInteger(item.val) : formatCurrency(item.val);

        return `
          <g style="cursor: pointer;" onmousemove="showTooltip(event, '<strong>${item.dow}</strong><br>ค่า: ${formattedVal}<br>รายได้: ${formatCurrency(item.revenue)}<br>กำไร: ${formatCurrency(item.profit)}<br>จำนวน: ${formatInteger(item.qty)} ชิ้น')" onmouseleave="hideTooltip()">
            <rect x="${cx - barW / 2}" y="${barY}" width="${barW}" height="${barH}" rx="4" fill="${col}" opacity="0.9" />
            <text x="${cx}" y="${height - margin.bottom + 18}" text-anchor="middle" font-size="11" font-weight="600" fill="var(--text-main)">${item.dow.replace('วัน', '')}</text>
          </g>
        `;
      }).join('');

      container.innerHTML = `
        <svg viewBox="0 0 ${width} ${height}" class="interactive-svg">
          ${gridLines}
          <!-- Average Line & Badge on LEFT (Never collides with Sunday bar on right!) -->
          <line x1="${margin.left}" y1="${avgY}" x2="${width - margin.right}" y2="${avgY}" stroke="#94a3b8" stroke-dasharray="5,4" stroke-width="1.5" />
          <g transform="translate(${margin.left + 10}, ${avgY - 22})">
            <rect x="0" y="0" width="138" height="20" rx="4" fill="var(--bg-card)" stroke="#94a3b8" stroke-width="1.2" opacity="0.96" />
            <text x="69" y="14" text-anchor="middle" font-size="10" font-weight="700" fill="var(--text-muted)">เฉลี่ย: ${metric === 'qty' ? formatInteger(avgVal) + ' ชิ้น' : formatCurrency(avgVal)}</text>
          </g>
          <line x1="${margin.left}" y1="${height - margin.bottom}" x2="${width - margin.right}" y2="${height - margin.bottom}" class="svg-axis-line" />
          ${bars}
        </svg>
      `;
    }"""

new_top_products = """    function renderTopProductsChart(data) {
      const container = document.getElementById('topProductsChartContainer');
      const metric = state.globalMetric;

      // Group by product across all branches
      const prodMap = {};
      data.forEach(x => {
        if (!prodMap[x.product]) {
          prodMap[x.product] = { product: x.product, category: x.category, revenue: 0, gross_profit: 0, qty: 0 };
        }
        prodMap[x.product].revenue += x.revenue;
        prodMap[x.product].gross_profit += x.gross_profit;
        prodMap[x.product].qty += x.qty;
      });

      let sorted = Object.values(prodMap).sort((a, b) => b[metric] - a[metric]);
      const topItems = sorted.slice(0, state.topRankLimit);

      if (topItems.length === 0) {
        container.innerHTML = '<div style="padding: 40px; text-align: center; color: var(--text-muted);">ไม่มีข้อมูลสำหรับตัวกรองที่เลือก</div>';
        return;
      }

      const maxVal = Math.max(...topItems.map(x => x[metric]), 1);
      const rowHeight = 44;
      const margin = { top: 20, right: 105, bottom: 25, left: 125 };
      const width = 580;
      const height = margin.top + (topItems.length * rowHeight) + margin.bottom;

      let metricLabel = 'รายได้ (฿)';
      if (metric === 'gross_profit') metricLabel = 'กำไรขั้นต้น (฿)';
      else if (metric === 'qty') metricLabel = 'จำนวนขาย (ชิ้น)';

      let barsSvg = '';
      topItems.forEach((item, idx) => {
        const y = margin.top + (idx * rowHeight);
        const val = item[metric];
        const barWidth = ((val / maxVal) * (width - margin.left - margin.right));
        const formattedVal = (metric === 'qty') ? formatInteger(val) + ' ชิ้น' : formatCurrency(val);
        const rankColor = idx === 0 ? '#ea580c' : (idx === 1 ? '#2563eb' : '#3b82f6');

        barsSvg += `
          <g class="bar-group" style="cursor: pointer;" onmousemove="showTooltip(event, '${item.product} (${item.category})<br>${metricLabel}: ${formattedVal}<br>รายได้: ${formatCurrency(item.revenue)}<br>กำไร: ${formatCurrency(item.gross_profit)}<br>จำนวน: ${formatInteger(item.qty)} ชิ้น')" onmouseleave="hideTooltip()">
            <!-- Rank & Label with plenty of left padding -->
            <text x="${margin.left - 12}" y="${y + 22}" text-anchor="end" fill="var(--text-main)" font-size="12" font-weight="600">
              #${idx + 1} ${item.product}
            </text>
            <!-- Background track -->
            <rect x="${margin.left}" y="${y + 8}" width="${width - margin.left - margin.right}" height="20" rx="4" fill="var(--bg-card-subtle)" />
            <!-- Bar fill -->
            <rect x="${margin.left}" y="${y + 8}" width="${barWidth}" height="20" rx="4" fill="${rankColor}" opacity="0.9" />
            <!-- Value text on right -->
            <text x="${margin.left + barWidth + 8}" y="${y + 23}" fill="var(--text-main)" font-size="11" font-weight="700">
              ${formattedVal}
            </text>
          </g>
        `;
      });

      container.innerHTML = `
        <svg viewBox="0 0 ${width} ${height}" class="interactive-svg">
          <line x1="${margin.left}" y1="${margin.top}" x2="${margin.left}" y2="${height - margin.bottom}" stroke="var(--border-color)" stroke-width="1.5" />
          ${barsSvg}
        </svg>
      `;
    }"""

# Find and replace functions in code
# Add getNiceMax helper right before renderKpis
if 'function getNiceMax' not in code:
    code = code.replace('function renderKpis', nice_max_helper + '\n    function renderKpis')

# Replace renderTopProductsChart
idx_top_start = code.find('function renderTopProductsChart')
idx_top_end = code.find('function renderOverviewBranchTable')
code = code[:idx_top_start] + new_top_products.strip() + '\n\n    ' + code[idx_top_end:]

# Replace renderParetoChart
idx_p_start = code.find('function renderParetoChart')
idx_p_end = code.find('function renderScatterPlot')
code = code[:idx_p_start] + new_pareto.strip() + '\n\n    ' + code[idx_p_end:]

# Replace renderScatterPlot
idx_s_start = code.find('function renderScatterPlot')
idx_s_end = code.find('function renderProductMasterTable')
code = code[:idx_s_start] + new_scatter.strip() + '\n\n    ' + code[idx_s_end:]

# Replace renderDowChart
idx_d_start = code.find('function renderDowChart')
idx_d_end = code.find('function renderCalendarGrid')
code = code[:idx_d_start] + new_dow.strip() + '\n\n    ' + code[idx_d_end:]

with open(r'e:\1Amazon_Quick_Workshop test\app.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated app.js successfully with clean, overlap-free charts!")
