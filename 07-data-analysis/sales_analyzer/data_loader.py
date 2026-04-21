"""Load, validate, and normalize sales CSV data before analysis."""

from pathlib import Path

import pandas as pd
from helpers import validate_sales_data


def load_sales_data(filepath):
    """Read one CSV file and add the derived columns expected by analyzers."""
    filepath = Path(filepath)

    if not filepath.exists():
        raise FileNotFoundError(f"Data file not found: {filepath}")

    # Load data
    df = pd.read_csv(filepath)

    # Validate
    validate_sales_data(df)

    # Normalize dates and totals once so downstream code can assume both exist.
    df["date"] = pd.to_datetime(df["date"])
    df["total"] = df["quantity"] * df["price"]

    return df


def load_multiple_files(data_dir, pattern="*.csv"):
    """Combine multiple matching CSV files into one analysis-ready DataFrame."""
    data_dir = Path(data_dir)
    files = list(data_dir.glob(pattern))

    if not files:
        raise FileNotFoundError(f"No files matching {pattern} in {data_dir}")

    dataframes = []
    for file in files:
        df = load_sales_data(file)
        # Preserve provenance so combined reports can trace rows back to the source file.
        df["source_file"] = file.name
        dataframes.append(df)

    return pd.concat(dataframes, ignore_index=True)


def clean_sales_data(dataframe):
    """Drop obviously invalid rows while keeping the original DataFrame untouched."""
    df = dataframe.copy()

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove negative quantities/prices
    df = df[(df["quantity"] > 0) & (df["price"] > 0)]

    # Sort by date
    df = df.sort_values("date").reset_index(drop=True)

    return df
