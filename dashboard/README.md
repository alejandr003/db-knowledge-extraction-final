# Dashboard Guide — Enterprise Dashboard

> **Owner:** Neyzer (Role 2 — BI Dashboard Lead)
> **Tool:** Power BI Desktop 2.159.1231.0 (Import mode)
> **Status:** Semantic model **complete and validated**; report visuals built in Power BI Desktop.
> **Primary file:** `dashboard/enterprise_dashboard.pbix`
> **Screenshots:** `dashboard/screenshots/`

---

## 1. Purpose

Give executives an interactive view of sales performance, profitability, and geographic
opportunities, with drill-down from category to product and cross-filtering by date, region,
and customer segment.

**Core business question:** *Where is the company making money, where is it losing money, and
which actions would improve profit without sacrificing revenue?*

---

## 2. Data source and model

| Item | Value |
|------|-------|
| Source file | `data/processed/clean_dataset.csv` |
| Source owner | Edwing (Role 1) |
| Fact table | `Sales` |
| Fact rows | **9,994** order lines |
| Date range | 2014-01-03 → 2017-12-30 |
| Refresh mode | Import |
| Date table | `DimDate` (marked as date table, 1,461 days) |
| Implicit measures | **Disabled** (`discourageImplicitMeasures = true`) — always use the `_Measures` table |

### Star schema

```text
DimDate (Date)            1 ──── * Sales (Order Date)
DimProduct (Product ID)   1 ──── * Sales (Product ID)
DimCustomer (Customer ID) 1 ──── * Sales (Customer ID)
DimGeography (State)      1 ──── * Sales (State)
DimShipMode (Ship Mode)   1 ──── * Sales (Ship Mode)
_Measures (no relationship)
```

### Table rows

| Table | Rows | Grain / notes |
|-------|------|---------------|
| `Sales` | 9,994 | One row per order line |
| `DimDate` | 1,461 | 2014-01-01 → 2017-12-31, marked as date table |
| `DimProduct` | 1,862 | `Product ID` is **not** unique in the raw data (1,894 combinations); grouped by `Product ID` with `MIN()` per attribute to keep a valid one-side key |
| `DimCustomer` | 793 | Unique `Customer ID` |
| `DimGeography` | 49 | At **State** grain; `State` has data category *State or Province* |
| `DimShipMode` | 4 | Standard / Second / First / Same Day |
| `_Measures` | — | Host table for all DAX measures (placeholder column hidden) |

### Relationships

| From (many) | To (one) | Cardinality | Cross-filter |
|-------------|----------|-------------|--------------|
| `Sales[Order Date]` | `DimDate[Date]` | Many → One | Single |
| `Sales[Product ID]` | `DimProduct[Product ID]` | Many → One | Single |
| `Sales[Customer ID]` | `DimCustomer[Customer ID]` | Many → One | Single |
| `Sales[State]` | `DimGeography[State]` | Many → One | Single |
| `Sales[Ship Mode]` | `DimShipMode[Ship Mode]` | Many → One | Single |

### Hierarchies (for drill-down)

- `DimProduct[Product Hierarchy]`: Category → Sub-Category → Product
- `DimGeography[Geography Hierarchy]`: Region → State
- `DimDate[Calendar Hierarchy]`: Year → Quarter → Month → Date

### Model hygiene

- Fact columns that duplicate dimension attributes are hidden in the report view.
- `Sales` keeps only `Sales`, `Quantity`, `Discount`, `Profit`, `Shipping Days`, and
  `Discount Band` visible.
- `DimProduct[Product ID]` and `DimCustomer[Customer ID]` are hidden keys.
- Numeric formats: currency for Sales/Profit, percent for Discount, thousand separators for counts.

---

## 3. Measures (DAX)

All measures live in `_Measures`.

| Measure | DAX | Format |
|---------|-----|--------|
| `Total Sales` | `SUM ( Sales[Sales] )` | `$#,##0` |
| `Total Profit` | `SUM ( Sales[Profit] )` | `$#,##0` |
| `Total Quantity` | `SUM ( Sales[Quantity] )` | `#,##0` |
| `Total Orders` | `DISTINCTCOUNT ( Sales[Order ID] )` | `#,##0` |
| `Profit Margin %` | `DIVIDE ( [Total Profit], [Total Sales], 0 )` | `0.0%` |
| `Average Discount` | `AVERAGE ( Sales[Discount] )` | `0.0%` |
| `Loss-Making Rows` | `CALCULATE ( COUNTROWS ( Sales ), Sales[Profit] < 0 )` | `#,##0` |
| `Loss Rate %` | `DIVIDE ( [Loss-Making Rows], COUNTROWS ( Sales ), 0 )` | `0.0%` |
| `Loss Amount` | `CALCULATE ( SUM ( Sales[Profit] ), Sales[Profit] < 0 )` | `$#,##0` |
| `Loss-Making Products` | `COUNTROWS ( FILTER ( VALUES ( DimProduct[Product ID] ), CALCULATE ( [Total Profit] ) < 0 ) )` | `#,##0` |
| `Avg Shipping Days` | `AVERAGE ( Sales[Shipping Days] )` | `0.0` |
| `Sales per Order` | `DIVIDE ( [Total Sales], [Total Orders], 0 )` | `$#,##0.00` |
| `Profit per Order` | `DIVIDE ( [Total Profit], [Total Orders], 0 )` | `$#,##0.00` |

---

## 4. Discount band (key insight)

Calculated column `Sales[Discount Band]` (sorted by hidden `Discount Band Order`):

| Band | Rows | Sales | Profit | Loss rate |
|------|------|-------|--------|-----------|
| 0% | 4,798 | $1,087,908 | **$320,988** | 0% |
| 1–10% | 94 | $54,369 | $9,029 | 4.3% |
| 11–20% | 3,709 | $792,153 | $91,756 | 14.0% |
| 21–30% | 227 | $103,227 | **−$10,369** | 91.6% |
| 31–40% | 233 | $130,911 | **−$25,448** | 88.8% |
| >40% | 933 | $128,632 | **−$99,559** | 100% |

> **Insight:** discounts **above 20%** (21%+) are loss-making. At exactly 20% the aggregate
> margin is still 11.8%; at 15% it falls to 5.1%. Discount policy — not volume — is the profit
> leak.

---

## 5. Report pages — build sheet

### Page 1 — Executive Overview

| Element | Visual type | Fields | Purpose |
|---------|-------------|--------|---------|
| Total Sales | Card | `[Total Sales]` | Revenue headline |
| Total Profit | Card | `[Total Profit]` | Profit headline |
| Profit Margin % | Card | `[Profit Margin %]` | Efficiency headline |
| Total Orders | Card | `[Total Orders]` | Volume headline |
| Loss Rate % | Card | `[Loss Rate %]` | Risk headline |
| Sales trend | Line chart | Axis `DimDate[Calendar Hierarchy]`; values `[Total Sales]`, `[Total Profit]` | Temporal pattern |
| Sales by state | Map (filled/bubble) | Location `DimGeography[State]`; size/color `[Total Sales]` | Geographic opportunity |
| Sales by category | Clustered bar | Axis `DimProduct[Category]`; value `[Total Sales]` | Portfolio comparison |
| Filters | Slicers | `DimDate[Year]` (or date range), `DimGeography[Region]`, `DimCustomer[Segment]` | Interactive slicing |

Layout: KPI cards across the top, trend on the left-middle, map on the right-middle, category bar
at the bottom. Add a **Reset filters** bookmark/button.

### Page 2 — Operational Drill-Down

| Element | Visual type | Fields | Purpose |
|---------|-------------|--------|---------|
| Profit by category | Clustered bar | Axis `DimProduct[Product Hierarchy]` (start at Category); value `[Total Profit]` | Where profit is created/lost (drill down to Sub-Category and Product) |
| Profit by sub-category | Clustered bar | Axis `DimProduct[Sub-Category]`; value `[Total Profit]` | Narrow the driver |
| Product detail | Matrix | Rows `DimProduct[Product Name]`; values `[Total Sales]`, `[Total Profit]`, `[Average Discount]`; sort `[Total Profit]` ascending | Root-cause inspection |
| Discount vs. profit | Scatter | X `Sales[Discount]`; Y `Sales[Profit]`; details `DimProduct[Sub-Category]` / `DimProduct[Product Name]` | Margin erosion |
| Discount band | Clustered column | Axis `Sales[Discount Band]`; value `[Total Profit]`; line `[Loss Rate %]` | Threshold evidence |
| Losses | Card | `[Loss-Making Rows]`, `[Loss Amount]`, `[Loss-Making Products]` | Risk totals |

Layout: use the **drill-down** buttons on the hierarchy bar; keep the matrix sorted ascending by
profit so the worst products surface first.

#### As built (2026-11-19)

- Page 1 titles (Spanish): `Sales by State`, `Sales por Category`, `Total Sales y Total Profit
  por Date`; slicers `Year`, `Region`, `Segment` (checkbox lists, no overlap).
- Page 2 titles (Spanish): `Product Details`, `Total Profit por Sub-Category`, `Total Profit por
  Category`, `Total Profit y Loss Rate % por Discount Band`, `Average Discount y Total Profit
  por Sub-Category`.
- Page 2 scatter is aggregated by `DimProduct[Sub-Category]` (X = `Average Discount`,
  Y = `Total Profit`) instead of order-line detail; the matrix is sorted by
  `Total Profit` ascending (worst products first).
- The trend line is at daily grain (`DimDate[Date]`); switch the X axis to `DimDate[Year Quarter]`
  for a cleaner executive view.

### Optional Page 3 — Geography / Operations

- `Avg Shipping Days` by `DimShipMode[Ship Mode]` (bar, 0-baseline).
- Profit by `DimGeography[Geography Hierarchy]` (Region → State), diverging colors.
- Loss-making states table (`DimGeography[State]`, `[Total Profit]`, `[Loss Rate %]`), sorted ascending.

---

## 6. Visual design standards

- **0-baseline:** every bar and column chart starts at 0. Never truncate the axis.
- **Sequential palette:** ordered magnitudes (sales, quantity) use Blues or Viridis.
- **Diverging palette:** profit vs. loss uses a diverging scale centered at **0** (blue/orange),
  never red/green.
- **Qualitative palette:** categories use a colorblind-safe palette.
- **Decluttering:** remove gridlines, borders, redundant legends, and default titles; use
  action-oriented titles.
- **Preattentive attributes:** highlight only the 1–2 numbers or bars that support the insight.
- Conditional formatting on the product matrix: profit cells with a diverging color scale centered at 0.

---

## 7. Interactivity checklist

- [ ] Date slicer filters every page.
- [ ] Region and Segment slicers cross-filter the visuals.
- [ ] Category bar drills to Sub-Category, then Product (Product Hierarchy).
- [ ] Map tooltip shows Sales, Profit, and Profit Margin.
- [ ] Reset-filters bookmark or button available.
- [ ] Page navigation is obvious (buttons or tabs).
- [ ] Mobile layout checked (optional but recommended).

---

## 8. How to refresh / open the dashboard

1. Confirm `data/processed/clean_dataset.csv` exists (Role 1).
2. Open `dashboard/enterprise_dashboard.pbix` in Power BI Desktop.
3. If prompted, update the source path:
   `Transform data → Data source settings → Change Source`.
   The source is the absolute OneDrive path used during authoring; each teammate must point it
   to their local clone.
4. Select **Refresh**.
5. Verify the KPI cards match section 10.
6. Save (`Ctrl+S`) and commit the `.pbix`.

> Power BI stores absolute file paths. After cloning the repository, re-point the CSV source and
> refresh. Do not commit temporary lock files.

---

## 9. Screenshots for the deck

Clean page captures are in `dashboard/screenshots/` for Josmar (Role 4):

- [x] `dashboard_executive_overview.png` — Page 1, 1488×845
- [x] `dashboard_drilldown.png` — Page 2, 1488×845
- [ ] `dashboard_geography.png` (optional, not built)

Captured from Power BI Desktop at *Fit to page* (78%) and cropped to the report canvas (no
ribbon or panes). Visual titles are in Spanish in the current build; translate them in the slides
if needed. Do not edit the data in the images.

---

## 10. Verification values (must match the notebook)

| Metric | Value |
|--------|-------|
| Total Sales | **$2,297,200.86** |
| Total Profit | **$286,397.02** |
| Profit Margin % | **12.47%** |
| Total Orders | **5,009** |
| Total Quantity | **37,873** |
| Average Discount | **15.62%** |
| Loss-Making Rows | **1,871** |
| Loss Rate % | **18.72%** |
| Loss Amount | **−$156,131.29** |
| Loss-Making Products (by Product ID) | **299** |
| Avg Shipping Days | **3.96** |

> **Note on 299 vs 301:** at 2-decimal currency precision, **299** products have a negative
> total profit. A raw floating-point `< 0` in pandas returns 301 because two product IDs have
> totals of −1.78e−15 (`FUR-CH-10004289`) and −7.11e−15 (`OFF-SU-10003505`); both round to
> **$0.00**. Power BI's `SUM` returns 0 for them, so the DAX measure correctly returns **299**.

---

## 11. Known issues and decisions

| Date | Issue / decision | Resolution | Owner |
|------|------------------|------------|-------|
| 2026-11-19 | `Product ID` not unique across attributes (1,862 IDs vs 1,894 combinations) | `DimProduct` groups by `Product ID` using `MIN()` for Name/Category/Sub-Category, preserving a valid 1→* relationship | Neyzer |
| 2026-11-19 | Geography kept at State grain instead of Postal Code | Map and regional analysis only need State; avoids duplicate postal-code keys across cities | Neyzer |
| 2026-11-19 | Discount bands initially off by one boundary | Rebuilt with inclusive upper bounds (`≤10%`, `≤20%`, …); totals now match the Python analysis | Neyzer |
| 2026-11-19 | Implicit measures could distort aggregates | `discourageImplicitMeasures = true`; all visuals must use `_Measures` | Neyzer |
| 2026-11-19 | Data source is an absolute OneDrive path | Documented in section 8; re-point after cloning | Neyzer |
| 2026-11-19 | KPI cards use Auto display units ("mil") | Set **Display units = None** if exact figures are required in the deck; exact values remain in the matrix and tooltips | Neyzer |
| 2026-11-20 | QA reported `Loss-Making Products` as 301 vs the dashboard's 299 | **299 is correct at currency precision.** The 301 count comes from two float residues (−1.78e−15 and −7.11e−15) that round to $0.00; the DAX `SUM` returns 0 for both. Documented in section 10; no model change required | Neyzer |

---

## 12. Changelog

| Date | Author | Change |
|------|--------|--------|
| 2026-11-06 | Jesus (Role 5) | Initial template created |
| 2026-11-19 | Neyzer (Role 2) | Star-schema model, 5 relationships, 3 hierarchies, 13 DAX measures, discount-band column; README completed; visuals pending |
| 2026-11-19 | Neyzer (Role 2) | Page 1 (Executive Overview) and Page 2 (Operational Drill-Down) built; screenshots captured to `dashboard/screenshots/` |
| 2026-11-20 | Neyzer (Role 2) | QA reconciliation for `Loss-Making Products` (299 is correct at 2-decimal precision; 301 is a float artifact); matrix sort note corrected to `Total Profit` ascending |
