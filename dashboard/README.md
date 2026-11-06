# Dashboard Guide — Enterprise Dashboard

> **Owner:** Neyzer (Role 2 — BI Dashboard Lead)
> **Tool:** Power BI Desktop (`.pbix`) or Tableau Public (`.twbx`)
> **Status:** Template — complete each section as the dashboard is built.
> **Primary file:** `dashboard/enterprise_dashboard.pbix`

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
| Fact table (suggested name) | `Sales` |
| Rows | TBD |
| Refresh mode | Import |
| Date table | TBD (`DimDate` recommended) |
| Relationships | TBD |

### Suggested star schema

```text
DimDate (Date) 1 ──── * Sales (Order Date)
DimCustomer (Customer ID) 1 ──── * Sales (Customer ID)
DimProduct (Product ID) 1 ──── * Sales (Product ID)
DimGeography (Postal Code / City / State) 1 ──── * Sales
DimShipMode (Ship Mode) 1 ──── * Sales
```

If the model stays as a single flat table, document that decision here:

> TBD — reason for keeping a flat table:

---

## 3. Report pages

### Page 1 — Executive Overview

| Element | Visual type | Fields | Purpose |
|---------|-------------|--------|---------|
| Total Sales | KPI card | `Sales` | Revenue headline |
| Total Profit | KPI card | `Profit` | Profit headline |
| Profit Margin % | KPI card | `Profit / Sales` | Efficiency headline |
| Sales trend | Line chart | `Order Date`, `Sales` | Temporal pattern |
| Sales by region | Filled map / bubble map | `State`, `Sales` | Geographic opportunity |
| Sales by category | Bar chart | `Category`, `Sales` | Portfolio comparison |
| Filters | Slicers | `Order Date`, `Region`, `Segment` | Interactive slicing |

### Page 2 — Operational Drill-Down

| Element | Visual type | Fields | Purpose |
|---------|-------------|--------|---------|
| Profit by category | Bar chart | `Category`, `Profit` | Where profit is created/lost |
| Profit by sub-category | Bar chart | `Sub-Category`, `Profit` | Narrow the driver |
| Product detail | Matrix/table | `Product Name`, `Sales`, `Profit`, `Discount` | Root-cause inspection |
| Discount vs. profit | Scatter chart | `Discount`, `Profit`, `Sub-Category` | Margin erosion |
| Drill path | Hierarchy | `Category → Sub-Category → Product Name` | Guided investigation |

### Optional Page 3 — Geography / Operations

- Shipping delay by state (`Shipping Days`).
- Sales vs. profit bubble map.
- Loss-making states or cities.

---

## 4. Measures (DAX)

Create these in a dedicated `_Measures` table.

```dax
Total Sales = SUM ( Sales[Sales] )

Total Profit = SUM ( Sales[Profit] )

Total Quantity = SUM ( Sales[Quantity] )

Total Orders = DISTINCTCOUNT ( Sales[Order ID] )

Profit Margin % = DIVIDE ( [Total Profit], [Total Sales], 0 )

Average Discount = AVERAGE ( Sales[Discount] )

Loss-Making Rows =
CALCULATE ( COUNTROWS ( Sales ), Sales[Profit] < 0 )

Loss Rate % =
DIVIDE ( [Loss-Making Rows], COUNTROWS ( Sales ), 0 )
```

Format `[Total Sales]` and `[Total Profit]` as currency (USD) and `[Profit Margin %]` as a
percentage with one decimal.

---

## 5. Visual design standards

- **0-baseline:** every bar and column chart starts at 0. Never truncate the axis.
- **Sequential palette:** ordered magnitudes (sales volume, quantity) use Viridis or Blues.
- **Diverging palette:** profit vs. loss uses a diverging scale centered at **0** (blue/orange
  or red/blue), never red/green.
- **Qualitative palette:** categories use a colorblind-safe qualitative palette.
- **Decluttering:** remove unnecessary gridlines, borders, redundant legends, and default
  titles; every visual needs a clear, action-oriented title.
- **Preattentive attributes:** highlight only the 1–2 numbers or bars that support the insight.

---

## 6. Interactivity checklist

- [ ] Date slicer filters every page.
- [ ] Region and Segment slicers cross-filter the visuals.
- [ ] Category bar drills to Sub-Category, then Product Name.
- [ ] Map tooltips show Sales, Profit, and Profit Margin.
- [ ] Reset-filters bookmark or button available.
- [ ] Page navigation is obvious (buttons or tabs).
- [ ] Mobile layout checked (optional but recommended).

---

## 7. How to refresh / open the dashboard

1. Confirm `data/processed/clean_dataset.csv` exists (Role 1).
2. Open `dashboard/enterprise_dashboard.pbix`.
3. If prompted, update the source path:
   `Transform data → Data source settings → Change Source`.
4. Select **Refresh**.
5. Verify the KPI cards match the notebook totals.
6. Save and commit the `.pbix` file.

> Power BI stores absolute file paths. When another teammate opens the file, they may need to
> update the path to their local clone. Document any path issue in section 9.

---

## 8. Screenshots for the deck

Export the final views to `assets/plots/` for Role 4 (storytelling lead):

- [ ] `dashboard_executive_overview.png`
- [ ] `dashboard_drilldown.png`
- [ ] `dashboard_geography.png` (optional)

Use **File → Export → Export current view** or a clean screenshot at 1920×1080.

---

## 9. Known issues and decisions

| Date | Issue / decision | Resolution | Owner |
|------|------------------|------------|-------|
| TBD | TBD | TBD | Neyzer |

---

## 10. Changelog

| Date | Author | Change |
|------|--------|--------|
| 2026-11-06 | Jesus (Role 5) | Initial template created |
| TBD | Neyzer (Role 2) | Data model, pages, and measures completed |
