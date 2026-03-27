"""Command-line entry point for the sales analysis workflow."""

import logging
import sys
from datetime import datetime

# Import our custom modules
from config import (
    SALES_FILE,
    OUTPUT_DIR,
    TOP_N_PRODUCTS,
    LOG_FORMAT,
    LOG_DATE_FORMAT,
    LOG_LEVEL,
)
from data_loader import load_sales_data, clean_sales_data
from helpers import format_currency, get_top_products, get_summary_stats
from visualizer import create_dashboard


# Give each run its own log so previous analysis output is never overwritten.
log_file = OUTPUT_DIR / f"analysis_{datetime.now():%Y%m%d_%H%M%S}.log"

# Write logs to both disk and stdout so the run is traceable in real time and later.
file_handler = logging.FileHandler(log_file, encoding="utf-8")
file_handler.setLevel(LOG_LEVEL)
file_handler.setFormatter(logging.Formatter(LOG_FORMAT, datefmt=LOG_DATE_FORMAT))

# Configure console handler with UTF-8 encoding (Windows-compatible)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(LOG_LEVEL)
console_handler.setFormatter(logging.Formatter(LOG_FORMAT, datefmt=LOG_DATE_FORMAT))

# Set up root logger
logging.basicConfig(level=LOG_LEVEL, handlers=[file_handler, console_handler])

logger = logging.getLogger(__name__)


def print_header(title: str, width: int = 60):
    """Print formatted section header."""
    print("\n" + "=" * width)
    print(title.center(width))
    print("=" * width)


def print_analysis_results(df, product_stats):
    """Print the key business metrics in a readable console layout."""

    print_header("SALES ANALYSIS RESULTS")

    # Get summary statistics
    stats = get_summary_stats(df)

    # Overall statistics
    print(f"\n💰 Total Revenue: {format_currency(stats['total_revenue'])}")
    print(f"📦 Total Items Sold: {stats['total_quantity']:,}")
    print(f"📋 Total Transactions: {stats['total_transactions']:,}")
    print(f"🏷️  Unique Products: {stats['unique_products']}")
    print(f"💵 Average Transaction: {format_currency(stats['average_transaction'])}")
    print(
        f"📅 Date Range: {stats['date_range']['start']} to {stats['date_range']['end']}"
    )

    # Top products
    print(f"\n🏆 Top {TOP_N_PRODUCTS} Products by Revenue:")
    print("-" * 60)
    print(f"{'Product':<20} {'Quantity':>10} {'Revenue':>15}")
    print("-" * 60)

    for product, row in product_stats.iterrows():
        print(
            f"{product:<20} {int(row['quantity']):>10,} {format_currency(row['total']):>15}"
        )

    print("=" * 60)


def save_results(df, product_stats):
    """Persist analysis outputs so charts and summaries can be reused later."""

    logger.info("Saving results...")

    # Save product statistics
    stats_file = OUTPUT_DIR / "product_statistics.csv"
    product_stats.to_csv(stats_file)
    logger.info("Saved: %s", stats_file.name)

    # Save detailed data
    details_file = OUTPUT_DIR / "sales_details.csv"
    df.to_csv(details_file, index=False)
    logger.info("Saved: %s", details_file.name)

    # The text summary is intentionally plain text so it is easy to open anywhere.
    stats = get_summary_stats(df)
    summary_file = OUTPUT_DIR / "summary_statistics.txt"

    with open(summary_file, "w", encoding="utf-8") as f:
        f.write("SALES ANALYSIS SUMMARY\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Total Revenue: {format_currency(stats['total_revenue'])}\n")
        f.write(f"Total Items Sold: {stats['total_quantity']:,}\n")
        f.write(f"Total Transactions: {stats['total_transactions']:,}\n")
        f.write(f"Unique Products: {stats['unique_products']}\n")
        f.write(
            f"Average Transaction: {format_currency(stats['average_transaction'])}\n"
        )
        f.write(
            f"Date Range: {stats['date_range']['start']} to {stats['date_range']['end']}\n"
        )

    logger.info("Saved: %s", summary_file.name)


def generate_final_summary(charts):
    """Show a final inventory of the files created during this run."""
    print_header("SUMMARY")

    output_files = list(OUTPUT_DIR.glob("*"))
    # .gitkeep is only there to keep the folder in version control.
    output_files = [f for f in output_files if f.is_file() and f.name != ".gitkeep"]

    print(f"\n📁 Generated {len(output_files)} files in output/")
    print("\nCharts:")
    for chart in charts:
        print(f"  📊 {chart.name}")

    print("\nData Files:")
    for file in output_files:
        if file.suffix == ".csv":
            print(f"  📄 {file.name}")

    print("\nReports:")
    for file in output_files:
        if file.suffix in [".txt", ".log"]:
            print(f"  📋 {file.name}")

    print("\n✅ Analysis complete!")
    print(f"📂 All files saved to: {OUTPUT_DIR}")
    print("=" * 60)


def main():
    """Run the end-to-end sales analysis pipeline with basic error reporting."""
    logger.info("=" * 60)
    logger.info("Starting Sales Analysis Tool")
    logger.info("=" * 60)

    try:
        # 1. Load data
        logger.info("Step 1: Loading data")
        df = load_sales_data(SALES_FILE)
        logger.info("Loaded %d records", len(df))

        # 2. Clean data
        logger.info("Step 2: Cleaning data")
        df = clean_sales_data(df)
        logger.info("%d records after cleaning", len(df))

        # 3. Analyze
        logger.info("Step 3: Analyzing data")
        product_stats = get_top_products(df, TOP_N_PRODUCTS)
        logger.info("Analyzed %d top products", len(product_stats))

        # 4. Print results
        logger.info("Step 4: Displaying results")
        print_analysis_results(df, product_stats)

        # 5. Create visualizations
        logger.info("Step 5: Creating visualizations")
        charts = create_dashboard(df, product_stats, OUTPUT_DIR)
        logger.info("Created %d charts", len(charts))

        # 6. Save results
        logger.info("Step 6: Saving results")
        save_results(df, product_stats)

        # 7. Final summary
        generate_final_summary(charts)

        logger.info("Log file: %s", log_file)
        logger.info("=" * 60)

    except FileNotFoundError as e:
        logger.error("File Error: %s", e)
        logger.error("Make sure data/sales.csv exists!")
        print("\nTip: Check that your data file is in the correct location:")
        print(f"   Expected: {SALES_FILE}")

    except ValueError as e:
        logger.error("Data Validation Error: %s", e)
        print("\nTip: Check your CSV file format and required columns")

    except Exception as e:
        logger.exception("Unexpected Error: %s", e)
        raise


if __name__ == "__main__":
    main()
