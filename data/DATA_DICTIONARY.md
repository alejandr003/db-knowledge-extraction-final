# Data Dictionary - Superstore Sales Dataset

> **Owner:** Edwing (Role 1 - Data Architect & Wrangler)
> **Status:** Completed - Audit and cleaning finished via `src/clean_data.py`.
> **Last updated:** 2026-11-17

---

## 1. Dataset metadata

| Item | Value |
|------|-------|
| Dataset name | Superstore Sales Dataset |
| Source | [Kaggle - Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) |
| Raw mirror | [sample-superstore.csv](https://raw.githubusercontent.com/datasets/sample-superstore/master/data/sample-superstore.csv) |
| Raw file | `data/raw/superstore_raw.csv` |
| Processed file | `data/processed/clean_dataset.csv` |
| Original rows | 9,994 |
| Original columns | 21 |
| Processed columns | 27 |
| Granularity | One row per order line (product within an order) |
| Time range | Evaluated automatically in Notebooks |
| Geographic scope | United States |
| Currency | USD |

---

## 2. Field dictionary

**Field types:** `identifier`, `temporal`, `continuous`, `categorical`, `geospatial`.
**Data types:** final dtype after cleaning (`string`, `datetime64[ns]`, `int64`, `float64`).

| # | Column | Final dtype | Field type | Description | Example / allowed values | Null rate | Notes |
|---|--------|-------------|------------|-------------|--------------------------|-----------|-------|
| 1 | `Row ID` | int64 | identifier | Unique row number in the source file | `1`, `2`, `3` … | 0% | Not a business key; do not use for joins |
| 2 | `Order ID` | string | identifier | Order identifier; repeats across line items | `CA-2016-152156` | 0% | One order can contain several rows |
| 3 | `Order Date` | datetime64[ns] | temporal | Date the order was placed | `2016-11-08` | 0% | Converted to ISO `YYYY-MM-DD` |
| 4 | `Ship Date` | datetime64[ns] | temporal | Date the order was shipped | `2016-11-11` | 0% | Must be ≥ `Order Date` |
| 5 | `Ship Mode` | string | categorical | Shipping service level | `Standard Class`, `Second Class`, `First Class`, `Same Day` | 0% | Trimmed and title-cased |
| 6 | `Customer ID` | string | identifier | Unique customer code | `CG-12520` | 0% | Repeats across orders |
| 7 | `Customer Name` | string | categorical | Customer full name | `Claire Gute` | 0% | PII: do not publish outside the course |
| 8 | `Segment` | string | categorical | Customer segment | `Consumer`, `Corporate`, `Home Office` | 0% | |
| 9 | `Country` | string | geospatial | Country of delivery | `United States` | 0% | Single-country dataset |
| 10 | `City` | string | geospatial | Delivery city | `Henderson` | 0% | Trimmed |
| 11 | `State` | string | geospatial | Delivery state | `Kentucky` | 0% | Trimmed |
| 12 | `Postal Code` | string | geospatial | Delivery postal code | `42420` | 0% | Kept as **string** to preserve leading zeros |
| 13 | `Region` | string | categorical / geospatial | Sales region | `South`, `West`, `Central`, `East` | 0% | |
| 14 | `Product ID` | string | identifier | Product code | `FUR-BO-10001798` | 0% | Repeats across orders |
| 15 | `Category` | string | categorical | Top-level product category | `Furniture`, `Office Supplies`, `Technology` | 0% | |
| 16 | `Sub-Category` | string | categorical | Product sub-category | `Bookcases`, `Chairs`, `Phones` … | 0% | 17 expected values |
| 17 | `Product Name` | string | categorical | Product description | `Bush Somerset Collection Bookcase` | 0% | Trimmed |
| 18 | `Sales` | float64 | continuous | Gross revenue for the line item (USD) | `261.9600` | 0% | Should be ≥ 0; flag negatives |
| 19 | `Quantity` | int64 | continuous (discrete) | Units sold in the line item | `1`, `2`, `3` … | 0% | Should be ≥ 1 |
| 20 | `Discount` | float64 | continuous | Discount rate applied (0–1) | `0.00`, `0.15`, `0.20` | 0% | Validate `0 ≤ Discount < 1` |
| 21 | `Profit` | float64 | continuous | Profit for the line item (USD) | `41.9136`, `-15.20` | 0% | Negative values are valid (losses) |

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
| Total rows | 9,994 | Preserved successfully |
| Total columns | 21 (raw) -> 27 (clean) | Derived columns added |
| Duplicate rows | 0 found | None required |
| Duplicate `Row ID` | 0 found | None required |
| Total missing cells | 0 found | Verified by audit |
| `Order Date` parse failures | 0 found | None required |
| `Ship Date` < `Order Date` | 0 found | None required |
| `Sales` < 0 | 0 found | None required |
| `Quantity` ≤ 0 | 0 found | None required |
| `Discount` outside `[0, 1)` | 0 found | None required |
| `Postal Code` invalid length | 0 found | Standardized to 5 chars |
| Outliers in `Profit` (IQR) | Retained | Flagged for Dashboard |

---

## 5. Missing-value and imputation log

Document every decision before applying it. **Never silently drop rows.**

| Column | Nulls found | Strategy | Justification | Rows affected |
|--------|-------------|----------|---------------|---------------|
| `Sales` | 0 | Median by `Sub-Category`, fallback global median | Skewed monetary variable | 0 |
| `Profit` | 0 | Median by `Sub-Category`, fallback global median | Skewed monetary variable | 0 |
| `Quantity` | 0 | Median by `Category`, fallback `1` | Discrete, low-cardinality | 0 |
| `Discount` | 0 | Fill with `0` | Most likely no discount recorded | 0 |
| `Ship Mode` / `Segment` / `Region` | 0 | Fill with `"Unknown"` | Preserve row; low null risk | 0 |
| `City` / `State` / `Postal Code` | 0 | Fill with `"Unknown"` | Cannot infer reliably | 0 |
| `Order Date` | 0 | Drop row if unparseable | Cannot place in time series | 0 |
| `Ship Date` | 0 | `Order Date` + median `Shipping Days` | Preserves row and date ordering | 0 |

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