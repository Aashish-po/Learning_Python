"""Reusable helper functions shared across the sales analysis project."""

from typing import Union

import pandas as pd


def calculate_total(quantity: Union[int, float], price: float) -> float:
    """Return the numeric total for one line item."""
    return float(quantity) * float(price)


def format_currency(amount: float) -> str:
    """Format a number for report output."""
    return f"${amount:,.2f}"


def format_percentage(value: float, decimals: int = 1) -> str:
    """Format a percentage string without changing the underlying numeric value."""
    return f"{value:.{decimals}f}%"


def calculate_revenue(dataframe: pd.DataFrame) -> float:
    """Sum the total revenue, creating the derived total column when needed."""
    if "total" not in dataframe.columns:
        dataframe["total"] = dataframe["quantity"] * dataframe["price"]
    return float(dataframe["total"].sum())


def get_top_products(dataframe: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """Aggregate product totals and return the highest-revenue rows."""
    if "total" not in dataframe.columns:
        dataframe["total"] = dataframe["quantity"] * dataframe["price"]

    product_stats = (
        dataframe.groupby("product")
        .agg({"quantity": "sum", "total": "sum"})
        .sort_values("total", ascending=False)
    )

    return product_stats.head(n)


def calculate_profit_margin(revenue: float, cost: float) -> float:
    """Return profit margin as a percentage, guarding against divide-by-zero."""
    if revenue == 0:
        return 0.0
    return ((revenue - cost) / revenue) * 100


def validate_sales_data(dataframe: pd.DataFrame) -> bool:
    """Confirm the required columns exist before analysis begins."""
    required_columns = ["date", "product", "quantity", "price"]
    missing = [col for col in required_columns if col not in dataframe.columns]

    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")

    return True


def calculate_growth_rate(current: float, previous: float) -> float:
    """Return percentage growth between two values."""
    if previous == 0:
        return 0.0
    return ((current - previous) / previous) * 100


def get_summary_stats(dataframe: pd.DataFrame) -> dict:
    """Build the summary payload used by console output and saved reports."""
    if "total" not in dataframe.columns:
        dataframe["total"] = dataframe["quantity"] * dataframe["price"]

    return {
        "total_revenue": float(dataframe["total"].sum()),
        "total_quantity": int(dataframe["quantity"].sum()),
        "total_transactions": len(dataframe),
        "unique_products": dataframe["product"].nunique(),
        "average_transaction": float(dataframe["total"].mean()),
        "date_range": {
            "start": dataframe["date"].min(),
            "end": dataframe["date"].max(),
        },
    }
