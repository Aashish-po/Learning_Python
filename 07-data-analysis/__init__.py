"""
Data analysis package.

pandas, matplotlib, and data processing.
"""

# Import main analyzer if available
try:
    from .sales_analyzer import analyzer

    __all__ = ["analyzer"]
except ImportError:
    pass
