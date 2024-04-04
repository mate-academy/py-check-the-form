import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_return",
    [
        ("Pass@word1", True),
        ("Pass@word1Pass@word1", False),
        ("Pass@word", False),
        ("Password1", False),
        ("pass@word1", False),
        ("P@ss1w", False)
    ],
    ids=["has_uppercase_has_symbol_has_number_good_length",
         "has_uppercase_has_symbol_has_number_too_long_length",
         "has_uppercase_has_symbol_NO_number_good_length",
         "has_uppercase_NO_symbol_has_number_good_length",
         "NO_uppercase_has_symbol_has_number_good_length",
         "has_uppercase_has_symbol_has_number_too_short_length"]
)
def test_check_password(password, expected_return):
    assert check_password(password) is expected_return
