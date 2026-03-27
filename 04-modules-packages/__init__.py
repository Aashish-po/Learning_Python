"""
Modules and packages examples.

Creating and organizing Python modules.
"""


def example_function():
    """Example function in the __init__.py module."""
    print("This is an example function in the __init__.py module.")


__version__ = "1.0.0"
__all__ = ["example_function"]
from . import example_function
