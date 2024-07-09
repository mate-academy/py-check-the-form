import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, validity",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Too_long_password1", False),
        ("no_capital_let", False),
        ("No_spec_char", False),
        ("1Small!", False)
    ]

)
def test_check_password(password: str, validity: bool) -> None:
    assert check_password(password) == validity


@pytest.mark.parametrize(
    "password, expected_error",
    [
        (12, TypeError),
        (12.548, TypeError),
        ({12}, TypeError),
        ([12], TypeError),
    ]

)
def test_check_password_for_error(
        password: str,
        expected_error: Exception
) -> None:
    with pytest.raises(Exception):
        check_password(password)
