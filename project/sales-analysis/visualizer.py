"""
Visualization functions for sales analysis.

This module creates charts, graphs, and visual reports
from sales data.
"""

import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from typing import Union, List
import logging

from config import COLORS, CHART_STYLE, CHART_DPI, CHART_FIGSIZE

logger = logging.getLogger(__name__)


def create_revenue_chart(
    product_stats: pd.DataFrame, output_path: Union[str, Path]
) -> Path:
    """
    Create bar chart of revenue by product.

    Args:
        product_stats: Product statistics with 'total' column
        output_path: Where to save the chart

    Returns:
        Path to saved chart
    """
    logger.info("Creating revenue chart")

    plt.figure(figsize=CHART_FIGSIZE)

    # Use 'total' column (not 'revenue')
    ax = product_stats["total"].plot(
        kind="bar", color=COLORS["revenue"], edgecolor="black", width=0.7
    )

    # Styling
    plt.title(
        "Revenue by Product",
        fontsize=CHART_STYLE["title_fontsize"],
        fontweight=CHART_STYLE["title_fontweight"],
        pad=20,
    )
    plt.xlabel("Product", fontsize=CHART_STYLE["label_fontsize"])
    plt.ylabel("Revenue ($)", fontsize=CHART_STYLE["label_fontsize"])
    plt.grid(axis="y", alpha=CHART_STYLE["grid_alpha"])
    plt.xticks(rotation=45, ha="right")

    # Add value labels on bars
    for i, v in enumerate(product_stats["total"]):
        ax.text(i, v, f"${v:,.0f}", ha="center", va="bottom", fontweight="bold")

    plt.tight_layout()

    output_path = Path(output_path)
    plt.savefig(output_path, dpi=CHART_DPI, bbox_inches="tight")
    plt.close()

    logger.info("Revenue chart saved: %s", output_path.name)
    return output_path


def create_quantity_chart(
    product_stats: pd.DataFrame, output_path: Union[str, Path]
) -> Path:
    """
    Create bar chart of quantity sold by product.

    Args:
        product_stats: Product statistics with 'quantity' column
        output_path: Where to save the chart

    Returns:
        Path to saved chart
    """
    logger.info("Creating quantity chart")

    plt.figure(figsize=CHART_FIGSIZE)

    ax = product_stats["quantity"].plot(
        kind="bar", color=COLORS["quantity"], edgecolor="black", width=0.7
    )

    # Styling
    plt.title(
        "Quantity Sold by Product",
        fontsize=CHART_STYLE["title_fontsize"],
        fontweight=CHART_STYLE["title_fontweight"],
        pad=20,
    )
    plt.xlabel("Product", fontsize=CHART_STYLE["label_fontsize"])
    plt.ylabel("Quantity", fontsize=CHART_STYLE["label_fontsize"])
    plt.grid(axis="y", alpha=CHART_STYLE["grid_alpha"])
    plt.xticks(rotation=45, ha="right")

    # Add value labels on bars
    for i, v in enumerate(product_stats["quantity"]):
        ax.text(i, v, f"{int(v)}", ha="center", va="bottom", fontweight="bold")

    plt.tight_layout()

    output_path = Path(output_path)
    plt.savefig(output_path, dpi=CHART_DPI, bbox_inches="tight")
    plt.close()

    logger.info("Quantity chart saved: %s", output_path.name)
    return output_path


def create_trend_chart(dataframe: pd.DataFrame, output_path: Union[str, Path]) -> Path:
    """
    Create line chart showing revenue trend over time.

    Args:
        dataframe: Sales data with 'date' and 'total' columns
        output_path: Where to save the chart

    Returns:
        Path to saved chart
    """
    logger.info("Creating trend chart")

    # Group by date
    daily_revenue = dataframe.groupby("date")["total"].sum()

    plt.figure(figsize=CHART_FIGSIZE)

    plt.plot(
        daily_revenue.index,
        daily_revenue.values,  # type: ignore
        marker="o",
        linewidth=2,
        markersize=8,
        color=COLORS["revenue"],
    )

    # Styling
    plt.title(
        "Daily Revenue Trend",
        fontsize=CHART_STYLE["title_fontsize"],
        fontweight=CHART_STYLE["title_fontweight"],
        pad=20,
    )
    plt.xlabel("Date", fontsize=CHART_STYLE["label_fontsize"])
    plt.ylabel("Revenue ($)", fontsize=CHART_STYLE["label_fontsize"])
    plt.grid(True, alpha=CHART_STYLE["grid_alpha"])
    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()

    output_path = Path(output_path)
    plt.savefig(output_path, dpi=CHART_DPI, bbox_inches="tight")
    plt.close()

    logger.info("Trend chart saved: %s", output_path.name)
    return output_path


def create_dashboard(
    dataframe: pd.DataFrame, product_stats: pd.DataFrame, output_dir: Union[str, Path]
) -> List[Path]:
    """
    Create complete dashboard with multiple charts.

    Args:
        dataframe: Full sales data
        product_stats: Product statistics
        output_dir: Directory to save charts

    Returns:
        List of paths to created charts
    """
    logger.info("Creating dashboard")

    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)

    created_files = []

    # Revenue chart
    revenue_chart = create_revenue_chart(
        product_stats, output_dir / "revenue_by_product.png"
    )
    created_files.append(revenue_chart)

    # Quantity chart
    quantity_chart = create_quantity_chart(
        product_stats, output_dir / "quantity_by_product.png"
    )
    created_files.append(quantity_chart)

    # Trend chart
    trend_chart = create_trend_chart(dataframe, output_dir / "revenue_trend.png")
    created_files.append(trend_chart)

    logger.info("Dashboard complete: %d charts created", len(created_files))
    return created_files
