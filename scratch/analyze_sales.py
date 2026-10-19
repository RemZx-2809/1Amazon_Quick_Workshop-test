import sys
import json
import zipfile
import datetime
import xml.etree.ElementTree as ET
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

path = r'e:\1Amazon_Quick_Workshop test\1Amazon_Quick_Workshop test.xlsx'
with zipfile.ZipFile(path, 'r') as z:
    sst_xml = ET.fromstring(z.read('xl/sharedStrings.xml'))
    ns = {'ns': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    shared_strings = []
    for si in sst_xml.findall('ns:si', ns):
        text = ''.join(t.text or '' for t in si.findall('.//ns:t', ns))
        shared_strings.append(text)
    
    sheet_xml = ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
    raw_rows = []
    for row in sheet_xml.findall('.//ns:row', ns):
        row_data = {}
        for c in row.findall('ns:c', ns):
            ref = c.attrib.get('r')
            col_letter = ''.join(filter(str.isalpha, ref))
            t = c.attrib.get('t')
            v_el = c.find('ns:v', ns)
            val = v_el.text if v_el is not None else None
            if t == 's' and val is not None:
                val = shared_strings[int(val)]
            row_data[col_letter] = (val, t)
        raw_rows.append((int(row.attrib.get('r')), row_data))

base_date = datetime.date(1899, 12, 30)
thai_days = ['วันจันทร์', 'วันอังคาร', 'วันพุธ', 'วันพฤหัสบดี', 'วันศุกร์', 'วันเสาร์', 'วันอาทิตย์']

# Data Quality Checks
header_row = raw_rows[0][1]
headers = {k: v[0] for k, v in header_row.items()}
print("Headers:", headers)

empty_rows_list = []
valid_items = []

for r_idx, r in raw_rows[1:]:
    vals = {k: v[0] for k, v in r.items() if v[0] is not None and str(v[0]).strip() != ''}
    if not vals:
        empty_rows_list.append(r_idx)
        continue
    
    tx_id = r['A'][0]
    date_val = int(r['B'][0])
    dt = base_date + datetime.timedelta(days=date_val)
    branch = r['C'][0]
    product = r['D'][0]
    category = r['E'][0]
    qty = int(r['F'][0])
    unit_price = float(r['G'][0])
    unit_cost = float(r['H'][0])
    
    revenue = qty * unit_price
    gross_profit = qty * (unit_price - unit_cost)
    margin = gross_profit / revenue if revenue else 0
    
    valid_items.append({
        'row': r_idx,
        'id': tx_id,
        'date': dt.strftime('%Y-%m-%d'),
        'date_serial': date_val,
        'day_of_week': thai_days[dt.weekday()],
        'weekday_idx': dt.weekday(),
        'branch': branch,
        'product': product,
        'category': category,
        'qty': qty,
        'unit_price': unit_price,
        'unit_cost': unit_cost,
        'revenue': revenue,
        'gross_profit': gross_profit,
        'margin': margin
    })

print(f"Total rows in sheet: {len(raw_rows)}")
print(f"Valid transactions: {len(valid_items)}")
print(f"Empty rows: {len(empty_rows_list)} (from row {empty_rows_list[0]} to {empty_rows_list[-1]})")

# Check duplicate IDs
ids = [x['id'] for x in valid_items]
id_set = set(ids)
print(f"Unique IDs: {len(id_set)} / {len(ids)}")

# Check spelling variations/whitespace
branches = set(x['branch'] for x in valid_items)
products = set(x['product'] for x in valid_items)
categories = set(x['category'] for x in valid_items)
print("Branches:", sorted(branches))
print("Categories:", sorted(categories))
print("Products:", sorted(products))

# Summary totals
total_rev = sum(x['revenue'] for x in valid_items)
total_qty = sum(x['qty'] for x in valid_items)
total_profit = sum(x['gross_profit'] for x in valid_items)
total_margin = (total_profit / total_rev) * 100
avg_rev_per_tx = total_rev / len(valid_items)
avg_unit_price = sum(x['unit_price'] * x['qty'] for x in valid_items) / total_qty
simple_avg_price = sum(x['unit_price'] for x in valid_items) / len(valid_items)

print("\n=== TOTAL KPI SUMMARY ===")
print(f"Total Revenue: {total_rev:,.2f} บาท")
print(f"Total Quantity: {total_qty:,} หน่วย")
print(f"Total Gross Profit: {total_profit:,.2f} บาท")
print(f"Gross Margin %: {total_margin:.2f}%")
print(f"Avg Revenue / Transaction: {avg_rev_per_tx:,.2f} บาท")
print(f"Weighted Avg Unit Price: {avg_unit_price:,.2f} บาท")
print(f"Simple Avg Unit Price: {simple_avg_price:,.2f} บาท")

print("\n=== BRANCH BREAKDOWN ===")
b_stats = defaultdict(lambda: {'rev': 0, 'qty': 0, 'profit': 0, 'tx': 0})
for x in valid_items:
    b = b_stats[x['branch']]
    b['rev'] += x['revenue']
    b['qty'] += x['qty']
    b['profit'] += x['gross_profit']
    b['tx'] += 1

for b_name in sorted(b_stats.keys(), key=lambda k: b_stats[k]['rev'], reverse=True):
    d = b_stats[b_name]
    m = (d['profit'] / d['rev']) * 100
    share = (d['rev'] / total_rev) * 100
    print(f"{b_name:15}: Rev = {d['rev']:10,.2f} ({share:5.2f}%) | Profit = {d['profit']:10,.2f} | Margin = {m:5.2f}% | Qty = {d['qty']:4} | Tx = {d['tx']:3}")

print("\n=== PRODUCT RANKING & ABC ===")
p_stats = defaultdict(lambda: {'rev': 0, 'qty': 0, 'profit': 0, 'cat': '', 'prices': set(), 'costs': set(), 'tx': 0})
for x in valid_items:
    p = p_stats[x['product']]
    p['rev'] += x['revenue']
    p['qty'] += x['qty']
    p['profit'] += x['gross_profit']
    p['cat'] = x['category']
    p['prices'].add(x['unit_price'])
    p['costs'].add(x['unit_cost'])
    p['tx'] += 1

sorted_prods = sorted(p_stats.items(), key=lambda kv: kv[1]['rev'], reverse=True)
cum_rev = 0
for rank, (p_name, d) in enumerate(sorted_prods, 1):
    prior_pct = (cum_rev / total_rev) * 100
    cum_rev += d['rev']
    cum_pct = (cum_rev / total_rev) * 100
    margin = (d['profit'] / d['rev']) * 100
    abc = 'A' if prior_pct < 80 else ('B' if prior_pct < 95 else 'C')
    price_str = "/".join(str(int(p)) for p in sorted(d['prices']))
    cost_str = "/".join(str(int(c)) for c in sorted(d['costs']))
    print(f"{rank}. {p_name:12} [{d['cat']:15}] | Rev: {d['rev']:9,.2f} ({d['rev']/total_rev*100:5.2f}%) | Cum: {cum_pct:5.2f}% | ABC: {abc} | Margin: {margin:5.2f}% | Qty: {d['qty']:3} | Price: {price_str} | Cost: {cost_str}")

print("\n=== DOW BREAKDOWN ===")
dow_stats = defaultdict(lambda: {'rev': 0, 'qty': 0, 'profit': 0, 'tx': 0})
for x in valid_items:
    d = dow_stats[x['day_of_week']]
    d['rev'] += x['revenue']
    d['qty'] += x['qty']
    d['profit'] += x['gross_profit']
    d['tx'] += 1

for d_name in thai_days:
    d = dow_stats[d_name]
    print(f"{d_name:15}: Rev = {d['rev']:10,.2f} | Profit = {d['profit']:10,.2f} | Qty = {d['qty']:4} | Tx = {d['tx']:3}")

print("\n=== HEATMAP: BRANCH x PRODUCT ===")
heatmap = defaultdict(lambda: defaultdict(float))
for x in valid_items:
    heatmap[x['branch']][x['product']] += x['revenue']

all_prods = [p[0] for p in sorted_prods]
header_line = f"{'Branch':15} | " + " | ".join(f"{p[:6]:>7}" for p in all_prods)
print(header_line)
for b_name in sorted(b_stats.keys()):
    row_vals = " | ".join(f"{heatmap[b_name][p]:7.0f}" for p in all_prods)
    print(f"{b_name:15} | {row_vals}")

# Save JSON dataset
with open(r'e:\1Amazon_Quick_Workshop test\sales_data.json', 'w', encoding='utf-8') as f:
    json.dump(valid_items, f, ensure_ascii=False, indent=2)
print("\nSaved valid_items to sales_data.json")
