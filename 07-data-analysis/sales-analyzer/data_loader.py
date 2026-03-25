# This module provides functions to load sales data from CSV files, validate the data, and perform basic cleaning operations. It ensures that the data is in a consistent format for analysis.
import pandas as pd
from pathlib import Path
from helpers import validate_sales_data


# Load sales data from a CSV file, validate it, and preprocess it for analysis
def load_sales_data(filepath):
    filepath = Path(filepath)

    if not filepath.exists():
        raise FileNotFoundError(f"Data file not found: {filepath}")

    # Load data
    df = pd.read_csv(filepath)

    # Validate
    validate_sales_data(df)

    # Preprocess
    df["date"] = pd.to_datetime(df["date"])
    df["total"] = df["quantity"] * df["price"]

    return df


# Load and combine multiple CSV files from a directory, then clean the combined data
def load_multiple_files(data_dir, pattern="*.csv"):
    data_dir = Path(data_dir)
    files = list(data_dir.glob(pattern))

    if not files:
        raise FileNotFoundError(f"No files matching {pattern} in {data_dir}")

    dataframes = []
    for file in files:
        df = load_sales_data(file)
        df["source_file"] = file.name
        dataframes.append(df)

    return pd.concat(dataframes, ignore_index=True)


# Clean the sales data by removing duplicates, filtering out invalid entries, and sorting by date
def clean_sales_data(dataframe):
    df = dataframe.copy()

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove negative quantities/prices
    df = df[(df["quantity"] > 0) & (df["price"] > 0)]

    # Sort by date
    df = df.sort_values("date").reset_index(drop=True)

    return df
