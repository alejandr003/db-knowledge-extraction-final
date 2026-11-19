"""Clean the raw Superstore dataset and produce the project's single source of truth.

Owner: Edwing (Role 1 - Data Architect & Wrangler)
Course: Database Knowledge Extraction - Final Project

Usage
-----
    python src/clean_data.py
    python src/clean_data.py --raw data/raw/superstore_raw.csv \
                             --output data/processed/clean_dataset.csv

The script is intentionally explicit: every imputation decision is logged so it can be
mirrored in ``data/DATA_DICTIONARY.md``.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RAW_PATH = PROJECT_ROOT / "data" / "raw" / "superstore_raw.csv"
DEFAULT_OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "clean_dataset.csv"

DATE_COLUMNS = ["Order Date", "Ship Date"]
NUMERIC_COLUMNS = ["Sales", "Quantity", "Discount", "Profit"]
STRING_COLUMNS = [
    "Order ID",
    "Ship Mode",
    "Customer ID",
    "Customer Name",
    "Segment",
    "Country",
    "City",
    "State",
    "Region",
    "Product ID",
    "Category",
    "Sub-Category",
    "Product Name",
]
CATEGORICAL_FILLS = {
    "Ship Mode": "Unknown",
    "Segment": "Unknown",
    "Country": "Unknown",
    "City": "Unknown",
    "State": "Unknown",
    "Region": "Unknown",
    "Category": "Unknown",
    "Sub-Category": "Unknown",
    "Product Name": "Unknown",
    "Customer Name": "Unknown",
}


def load_raw(path: Path) -> pd.DataFrame:
    """Load the raw CSV, failing with a helpful message when it is missing."""
    if not path.exists():
        raise FileNotFoundError(
            f"Raw dataset not found at {path}.\n"
            "Download it from "
            "https://raw.githubusercontent.com/datasets/sample-superstore/master/data/sample-superstore.csv "
            f"and save it as {path}."
        )
    return pd.read_csv(path, encoding="windows-1252")


def audit(df: pd.DataFrame, label: str) -> None:
    """Print a compact data-quality report before and after cleaning."""
    print(f"\n[{label}] shape: {df.shape[0]:,} rows x {df.shape[1]} columns")
    print(f"[{label}] duplicate rows: {int(df.duplicated().sum()):,}")

    missing = df.isna().sum()
    missing = missing[missing > 0].sort_values(ascending=False)
    if missing.empty:
        print(f"[{label}] missing values: none")
    else:
        print(f"[{label}] missing values by column:")
        for column, count in missing.items():
            rate = count / len(df) * 100
            print(f"  - {column:<20} {count:>5} ({rate:5.2f}%)")


def _normalize_postal_code(series: pd.Series) -> pd.Series:
    """Keep postal codes as text and remove the ``.0`` added by numeric parsing."""

    def convert(value: object) -> object:
        if pd.isna(value):
            return pd.NA
        text = str(value).strip()
        if text.endswith(".0") and text[:-2].isdigit():
            text = text[:-2]
        if text.isdigit() and len(text) < 5:
            text = text.zfill(5)
        return text

    return series.map(convert).astype("string")


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Apply the documented cleaning rules and return a new DataFrame."""
    df = df.copy()

    # 1. Normalize column names and trim text values.
    df.columns = [str(column).strip() for column in df.columns]
    for column in STRING_COLUMNS:
        if column in df.columns:
            df[column] = df[column].astype("string").str.strip()

    # 2. Parse dates. Rows without a valid order date cannot be placed in time.
    for column in DATE_COLUMNS:
        if column in df.columns:
            df[column] = pd.to_datetime(df[column], errors="coerce")

    invalid_order_dates = int(df["Order Date"].isna().sum())
    if invalid_order_dates:
        print(f"Dropping {invalid_order_dates} row(s) with an invalid Order Date.")
        df = df.dropna(subset=["Order Date"])

    # 3. Rebuild a missing Ship Date from the median shipping delay.
    if "Ship Date" in df.columns:
        shipping_days = (df["Ship Date"] - df["Order Date"]).dt.days
        valid_delays = shipping_days[(shipping_days >= 0) & shipping_days.notna()]
        median_delay = int(valid_delays.median()) if not valid_delays.empty else 3
        missing_ship_dates = df["Ship Date"].isna()
        if missing_ship_dates.any():
            print(
                f"Imputing {int(missing_ship_dates.sum())} missing Ship Date(s) "
                f"with Order Date + {median_delay} day(s)."
            )
            df.loc[missing_ship_dates, "Ship Date"] = (
                df.loc[missing_ship_dates, "Order Date"] + pd.Timedelta(days=median_delay)
            )
        df["Shipping Days"] = (df["Ship Date"] - df["Order Date"]).dt.days

    # 4. Enforce numeric dtypes before imputing.
    for column in NUMERIC_COLUMNS:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors="coerce")

    # 5. Impute monetary values with the sub-category median, then the global median.
    for column in ["Sales", "Profit"]:
        if column in df.columns:
            if "Sub-Category" in df.columns:
                grouped_median = df.groupby("Sub-Category")[column].transform("median")
                df[column] = df[column].fillna(grouped_median)
            df[column] = df[column].fillna(df[column].median()).fillna(0)

    # 6. Quantity: category median, then 1. Discount: assume 0 when absent.
    if "Quantity" in df.columns:
        if "Category" in df.columns:
            grouped_quantity = df.groupby("Category")["Quantity"].transform("median")
            df["Quantity"] = df["Quantity"].fillna(grouped_quantity)
        df["Quantity"] = df["Quantity"].fillna(1).round().astype("int64")

    if "Discount" in df.columns:
        df["Discount"] = df["Discount"].fillna(0).clip(lower=0, upper=0.99)

    # 7. Fill categorical gaps without dropping rows.
    for column, fill_value in CATEGORICAL_FILLS.items():
        if column in df.columns:
            df[column] = df[column].fillna(fill_value)

    if "Postal Code" in df.columns:
        df["Postal Code"] = _normalize_postal_code(df["Postal Code"])

    # 8. Remove exact duplicates created by exports or concatenation.
    before = len(df)
    df = df.drop_duplicates()
    if len(df) != before:
        print(f"Removed {before - len(df)} duplicate row(s).")

    # 9. Derived fields used by the notebook, dashboard, and presentation.
    df["Order Year"] = df["Order Date"].dt.year.astype("int64")
    df["Order Month"] = df["Order Date"].dt.to_period("M").astype(str)
    df["Order Quarter"] = df["Order Date"].dt.to_period("Q").astype(str)
    df["Profit Margin"] = (df["Profit"] / df["Sales"].where(df["Sales"].ne(0))).fillna(0)
    df["Is Loss"] = df["Profit"] < 0

    # 10. Keep a stable, readable column order.
    ordered_columns = [
        "Row ID",
        "Order ID",
        "Order Date",
        "Ship Date",
        "Ship Mode",
        "Customer ID",
        "Customer Name",
        "Segment",
        "Country",
        "City",
        "State",
        "Postal Code",
        "Region",
        "Product ID",
        "Category",
        "Sub-Category",
        "Product Name",
        "Sales",
        "Quantity",
        "Discount",
        "Profit",
        "Order Year",
        "Order Month",
        "Order Quarter",
        "Shipping Days",
        "Profit Margin",
        "Is Loss",
    ]
    existing_columns = [column for column in ordered_columns if column in df.columns]
    remaining_columns = [column for column in df.columns if column not in existing_columns]
    return df[existing_columns + remaining_columns].reset_index(drop=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Clean the raw Superstore dataset.")
    parser.add_argument("--raw", type=Path, default=DEFAULT_RAW_PATH, help="Path to the raw CSV.")
    parser.add_argument(
        "--output", type=Path, default=DEFAULT_OUTPUT_PATH, help="Path for the cleaned CSV."
    )
    args = parser.parse_args()

    raw_df = load_raw(args.raw)
    audit(raw_df, "raw")

    cleaned_df = clean(raw_df)
    audit(cleaned_df, "clean")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    cleaned_df.to_csv(args.output, index=False, encoding="utf-8")
    print(f"\nSaved cleaned dataset: {args.output}")
    print(f"Final shape: {cleaned_df.shape[0]:,} rows x {cleaned_df.shape[1]} columns")


if __name__ == "__main__":
    main()
