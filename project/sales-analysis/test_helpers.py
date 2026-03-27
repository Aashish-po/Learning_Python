"""Regression tests for the reusable sales-analysis helper functions."""

from helpers import calculate_total, format_currency, calculate_profit_margin


def test_calculate_total():
    assert calculate_total(5, 10.0) == 50.0
    assert calculate_total(0, 100.0) == 0.0
    assert calculate_total(3, 33.33) == 99.99


# Test currency formatting
def test_format_currency():
    assert format_currency(1234.56) == "$1,234.56"
    assert format_currency(0) == "$0.00"
    assert format_currency(1000000) == "$1,000,000.00"


# Test profit margin calculation
def test_calculate_profit_margin():
    assert calculate_profit_margin(100, 60) == 40.0
    assert calculate_profit_margin(100, 100) == 0.0
    assert calculate_profit_margin(0, 50) == 0.0


if __name__ == "__main__":
    # Run tests
    test_calculate_total()
    print("✅ calculate_total tests passed")

    test_format_currency()
    print("✅ format_currency tests passed")

    test_calculate_profit_margin()
    print("✅ calculate_profit_margin tests passed")

    print("\n✅ All tests passed!")
