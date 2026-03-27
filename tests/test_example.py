"""Small smoke tests that confirm the test runner is wired correctly."""


def test_addition():
    """Verify basic arithmetic works inside the pytest setup."""
    assert 1 + 1 == 2


def test_string():
    """Verify simple string transformations behave as expected."""
    assert "hello".upper() == "HELLO"
