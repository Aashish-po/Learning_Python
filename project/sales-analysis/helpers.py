"""
Helper utility functions for sales analysis.

This module contains reusable functions for calculations,
formatting, and data transformations.
"""

import pandas as pd
from typing import Union


def calculate_total(quantity: Union[int, float], price: float) -> float:
    """
    Calculate total cost for a single line item.

    Args:
        quantity: Number of items
        price: Price per item

    Returns:
        Total cost (quantity * price)

    Examples:
        >>> calculate_total(5, 29.99)
        149.95
        >>> calculate_total(10, 100.0)
        1000.0
    """
    return float(quantity) * float(price)


def format_currency(amount: float) -> str:
    """
    Format number as currency with $ symbol and comma separators.

    Args:
        amount: Dollar amount

    Returns:
        Formatted currency string

    Examples:
        >>> format_currency(1234.56)
        '$1,234.56'
        >>> format_currency(1000000)
        '$1,000,000.00'
    """
    return f"${amount:,.2f}"


def format_percentage(value: float, decimals: int = 1) -> str:
    """
    Format number as percentage.

    Args:
        value: Percentage value (e.g., 15.5 for 15.5%)
        decimals: Number of decimal places

    Returns:
        Formatted percentage string

    Examples:
        >>> format_percentage(15.5)
        '15.5%'
        >>> format_percentage(33.333, 2)
        '33.33%'
    """
    return f"{value:.{decimals}f}%"


def calculate_revenue(dataframe: pd.DataFrame) -> float:
    """
    Calculate total revenue from a sales DataFrame.

    Args:
        dataframe: Sales data with 'quantity' and 'price' columns

    Returns:
        Total revenue

    Examples:
        >>> df = pd.DataFrame({'quantity': [2, 3], 'price': [10.0, 20.0]})
        >>> calculate_revenue(df)
        80.0
    """
    if "total" not in dataframe.columns:
        dataframe["total"] = dataframe["quantity"] * dataframe["price"]
    return float(dataframe["total"].sum())


def get_top_products(dataframe: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """
    Get top N products by revenue.

    Args:
        dataframe: Sales data with 'product' and 'total' columns
        n: Number of top products to return

    Returns:
        DataFrame with top products sorted by revenue
    """
    if "total" not in dataframe.columns:
        dataframe["total"] = dataframe["quantity"] * dataframe["price"]

    product_stats = (
        dataframe.groupby("product")
        .agg({"quantity": "sum", "total": "sum"})
        .sort_values("total", ascending=False)
    )

    return product_stats.head(n)


def calculate_profit_margin(revenue: float, cost: float) -> float:
    """
    Calculate profit margin percentage.

    Args:
        revenue: Total revenue
        cost: Total cost

    Returns:
        Profit margin as percentage

    Examples:
        >>> calculate_profit_margin(100, 60)
        40.0
        >>> calculate_profit_margin(100, 100)
        0.0
    """
    if revenue == 0:
        return 0.0
    return ((revenue - cost) / revenue) * 100


def validate_sales_data(dataframe: pd.DataFrame) -> bool:
    """
    Validate sales DataFrame has required columns.

    Args:
        dataframe: Sales data to validate

    Returns:
        True if valid

    Raises:
        ValueError: If required columns are missing
    """
    required_columns = ["date", "product", "quantity", "price"]
    missing = [col for col in required_columns if col not in dataframe.columns]

    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")

    return True


def calculate_growth_rate(current: float, previous: float) -> float:
    """
    Calculate growth rate percentage.

    Args:
        current: Current period value
        previous: Previous period value

    Returns:
        Growth rate as percentage

    Examples:
        >>> calculate_growth_rate(150, 100)
        50.0
        >>> calculate_growth_rate(80, 100)
        -20.0
    """
    if previous == 0:
        return 0.0
    return ((current - previous) / previous) * 100


def get_summary_stats(dataframe: pd.DataFrame) -> dict:
    """
    Calculate comprehensive summary statistics.

    Args:
        dataframe: Sales data

    Returns:
        Dictionary with summary statistics including:
        - total_revenue: Total revenue amount
        - total_quantity: Total items sold
        - total_transactions: Number of transactions
        - unique_products: Number of unique products
        - average_transaction: Average transaction value
        - date_range: Dictionary with start and end dates

    Example:
        >>> df = pd.DataFrame({
        ...     'date': ['2024-01-01', '2024-01-02'],
        ...     'product': ['Laptop', 'Mouse'],
        ...     'quantity': [2, 5],
        ...     'price': [999.99, 29.99]
        ... })
        >>> df['date'] = pd.to_datetime(df['date'])
        >>> stats = get_summary_stats(df)
        >>> 'total_revenue' in stats
        True
    """
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
