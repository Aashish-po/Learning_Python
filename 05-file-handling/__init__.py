"""
File handling package.

Working with files, CSV, JSON, and paths.
"""

__version__ = "1.0.0"
__all__ = ["file_handling", "csv_handling", "json_handling", "path_handling"]
from . import csv_handling, file_handling, json_handling, path_handling
