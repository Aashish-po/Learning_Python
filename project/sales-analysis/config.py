from pathlib import Path


# Project directories
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"

# File paths
SALES_FILE = DATA_DIR / "sales.csv"

# Number of top products to display
TOP_N_PRODUCTS = 5

# Currency display
CURRENCY_SYMBOL = "$"
CURRENCY_FORMAT = ",.2f"

# Date format for display
DATE_FORMAT = "%Y-%m-%d"

# Chart settings
CHART_DPI = 300
CHART_FIGSIZE = (12, 6)

# Color scheme
COLORS = {
    "revenue": "steelblue",
    "quantity": "coral",
    "profit": "green",
    "positive": "#2ecc71",
    "negative": "#e74c3c",
}

# Chart style
CHART_STYLE = {
    "title_fontsize": 14,
    "title_fontweight": "bold",
    "label_fontsize": 12,
    "grid_alpha": 0.3,
}

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
LOG_LEVEL = "INFO"


# Ensure directories exist
OUTPUT_DIR.mkdir(exist_ok=True)
DATA_DIR.mkdir(exist_ok=True)

# Create .gitkeep files
(OUTPUT_DIR / ".gitkeep").touch(exist_ok=True)
