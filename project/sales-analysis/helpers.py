import pandas as pd
from typing import Union


# This module provides helper functions for sales data analysis, including calculations, formatting, and validation. These functions are designed to be reusable across different parts of the project to maintain consistency and reduce code duplication.
def calculate_total(quantity: Union[int, float], price: float) -> float:

    return float(quantity) * float(price)


# Format a number as currency with the specified symbol and format
def format_currency(amount: float) -> str:

    return f"${amount:,.2f}"


# Format a number as percentage with specified decimal places
def format_percentage(value: float, decimals: int = 1) -> str:

    return f"{value:.{decimals}f}%"


# Format a date using the specified format string
def calculate_revenue(dataframe: pd.DataFrame) -> float:
    if "total" not in dataframe.columns:
        dataframe["total"] = dataframe["quantity"] * dataframe["price"]
    return float(dataframe["total"].sum())


# Format a date using the specified format string
def get_top_products(dataframe: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    if "total" not in dataframe.columns:
        dataframe["total"] = dataframe["quantity"] * dataframe["price"]

    product_stats = (
        dataframe.groupby("product")
        .agg({"quantity": "sum", "total": "sum"})
        .sort_values("total", ascending=False)
    )

    return product_stats.head(n)


# Format a date using the specified format string
def calculate_profit_margin(revenue: float, cost: float) -> float:

    if revenue == 0:
        return 0.0
    return ((revenue - cost) / revenue) * 100


# Format a date using the specified format string
def validate_sales_data(dataframe: pd.DataFrame) -> bool:
    required_columns = ["date", "product", "quantity", "price"]
    missing = [col for col in required_columns if col not in dataframe.columns]

    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")

    return True


# Format a date using the specified format string
def calculate_growth_rate(current: float, previous: float) -> float:

    if previous == 0:
        return 0.0
    return ((current - previous) / previous) * 100


# Format a date using the specified format string
def get_summary_stats(dataframe: pd.DataFrame) -> dict:

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
