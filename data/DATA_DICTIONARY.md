# Data Dictionary — Superstore Sales Dataset

> **Owner:** Edwing (Role 1 — Data Architect & Wrangler)
> **Status:** Template — complete every `TBD` after running `src/clean_data.py`.
> **Last updated:** 2026-11-06

---

## 1. Dataset metadata

| Item | Value |
|------|-------|
| Dataset name | Superstore Sales Dataset |
| Source | [Kaggle — Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) |
| Raw mirror | [sample-superstore.csv](https://raw.githubusercontent.com/datasets/sample-superstore/master/data/sample-superstore.csv) |
| Raw file | `data/raw/superstore_raw.csv` |
| Processed file | `data/processed/clean_dataset.csv` |
| Original rows | 9,994 |
| Original columns | 21 |
| Granularity | One row per order line (product within an order) |
| Time range | TBD (`Order Date` min → max) |
| Geographic scope | United States |
| Currency | USD |

---

## 2. Field dictionary

**Field types:** `identifier`, `temporal`, `continuous`, `categorical`, `geospatial`.
**Data types:** final dtype after cleaning (`string`, `datetime64[ns]`, `int64`, `float64`).

| # | Column | Final dtype | Field type | Description | Example / allowed values | Null rate | Notes |
|---|--------|-------------|------------|-------------|--------------------------|-----------|-------|
| 1 | `Row ID` | int64 | identifier | Unique row number in the source file | `1`, `2`, `3` … | TBD | Not a business key; do not use for joins |
| 2 | `Order ID` | string | identifier | Order identifier; repeats across line items | `CA-2016-152156` | TBD | One order can contain several rows |
| 3 | `Order Date` | datetime64[ns] | temporal | Date the order was placed | `2016-11-08` | TBD | Converted to ISO `YYYY-MM-DD` |
| 4 | `Ship Date` | datetime64[ns] | temporal | Date the order was shipped | `2016-11-11` | TBD | Must be ≥ `Order Date` |
| 5 | `Ship Mode` | string | categorical | Shipping service level | `Standard Class`, `Second Class`, `First Class`, `Same Day` | TBD | Trimmed and title-cased |
| 6 | `Customer ID` | string | identifier | Unique customer code | `CG-12520` | TBD | Repeats across orders |
| 7 | `Customer Name` | string | categorical | Customer full name | `Claire Gute` | TBD | PII: do not publish outside the course |
| 8 | `Segment` | string | categorical | Customer segment | `Consumer`, `Corporate`, `Home Office` | TBD | |
| 9 | `Country` | string | geospatial | Country of delivery | `United States` | TBD | Single-country dataset |
| 10 | `City` | string | geospatial | Delivery city | `Henderson` | TBD | Trimmed |
| 11 | `State` | string | geospatial | Delivery state | `Kentucky` | TBD | Trimmed |
| 12 | `Postal Code` | string | geospatial | Delivery postal code | `42420` | TBD | Kept as **string** to preserve leading zeros |
| 13 | `Region` | string | categorical / geospatial | Sales region | `South`, `West`, `Central`, `East` | TBD | |
| 14 | `Product ID` | string | identifier | Product code | `FUR-BO-10001798` | TBD | Repeats across orders |
| 15 | `Category` | string | categorical | Top-level product category | `Furniture`, `Office Supplies`, `Technology` | TBD | |
| 16 | `Sub-Category` | string | categorical | Product sub-category | `Bookcases`, `Chairs`, `Phones` … | TBD | 17 expected values |
| 17 | `Product Name` | string | categorical | Product description | `Bush Somerset Collection Bookcase` | TBD | Trimmed |
| 18 | `Sales` | float64 | continuous | Gross revenue for the line item (USD) | `261.9600` | TBD | Should be ≥ 0; flag negatives |
| 19 | `Quantity` | int64 | continuous (discrete) | Units sold in the line item | `1`, `2`, `3` … | TBD | Should be ≥ 1 |
| 20 | `Discount` | float64 | continuous | Discount rate applied (0–1) | `0.00`, `0.15`, `0.20` | TBD | Validate `0 ≤ Discount < 1` |
| 21 | `Profit` | float64 | continuous | Profit for the line item (USD) | `41.9136`, `-15.20` | TBD | Negative values are valid (losses) |

---

## 3. Derived fields (created by `clean_data.py`)

Add rows here only if Role 1 creates them; keep the notebook and dashboard in sync.

| Column | Type | Formula / rule | Purpose |
|--------|------|----------------|---------|
| `Order Year` | int64 | `Order Date.dt.year` | Annual trend analysis |
| `Order Month` | string | `Order Date.dt.to_period("M")` | Monthly time series |
| `Order Quarter` | string | `Order Date.dt.to_period("Q")` | Quarterly comparisons |
| `Shipping Days` | int64 | `(Ship Date - Order Date).dt.days` | Operational efficiency |
| `Profit Margin` | float64 | `Profit / Sales` (guard `Sales = 0`) | Profitability KPI |
| `Is Loss` | boolean | `Profit < 0` | Loss/diverging color encoding |

---

## 4. Data quality summary

Fill this table with the output of the audit step.

| Check | Result | Action taken |
|-------|--------|--------------|
| Total rows | TBD | — |
| Total columns | TBD | — |
| Duplicate rows | TBD | TBD |
| Duplicate `Row ID` | TBD | TBD |
| Total missing cells | TBD | See section 5 |
| `Order Date` parse failures | TBD | TBD |
| `Ship Date` < `Order Date` | TBD | TBD |
| `Sales` < 0 | TBD | TBD |
| `Quantity` ≤ 0 | TBD | TBD |
| `Discount` outside `[0, 1)` | TBD | TBD |
| `Postal Code` invalid length | TBD | TBD |
| Outliers in `Profit` (IQR) | TBD | Retained / flagged |

---

## 5. Missing-value and imputation log

Document every decision before applying it. **Never silently drop rows.**

| Column | Nulls found | Strategy | Justification | Rows affected |
|--------|-------------|----------|---------------|---------------|
| `Sales` | TBD | Median by `Sub-Category`, fallback global median | Skewed monetary variable | TBD |
| `Profit` | TBD | Median by `Sub-Category`, fallback global median | Skewed monetary variable | TBD |
| `Quantity` | TBD | Median by `Category`, fallback `1` | Discrete, low-cardinality | TBD |
| `Discount` | TBD | Fill with `0` | Most likely no discount recorded | TBD |
| `Ship Mode` / `Segment` / `Region` | TBD | Fill with `"Unknown"` | Preserve row; low null risk | TBD |
| `City` / `State` / `Postal Code` | TBD | Fill with `"Unknown"` | Cannot infer reliably | TBD |
| `Order Date` | TBD | Drop row if unparseable | Cannot place in time series | TBD |
| `Ship Date` | TBD | `Order Date` + median `Shipping Days` | Preserves row and date ordering | TBD |

---

## 6. Cleaning rules applied

1. Strip leading/trailing whitespace from all string columns.
2. Normalize column names to a consistent `Title Case` with single spaces.
3. Parse `Order Date` and `Ship Date` as ISO datetimes (`errors="coerce"`).
4. Cast `Postal Code` to string and zero-pad only when the source is clearly numeric.
5. Remove exact duplicate rows; keep the first occurrence.
6. Validate monetary ranges and flag (do not delete) outliers.
7. Export to UTF-8 CSV with `index=False`.

---

## 7. Reproducibility

```bash
python src/clean_data.py
```

Expected output:

```text
Loaded raw data: 9994 rows x 21 columns
...
Saved cleaned dataset: data/processed/clean_dataset.csv
```

---

## 8. Change log

| Date | Author | Change |
|------|--------|--------|
| 2026-11-06 | Jesus (Role 5) | Initial template created |
| TBD | Edwing (Role 1) | Audit results, null rates, and cleaning decisions completed |
