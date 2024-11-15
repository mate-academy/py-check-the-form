# write your code here
from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Pass@word1") is True


def test_short_password() -> None:
    assert check_password("asdghrd") is False


def test_long_password() -> None:
    assert check_password("asdf123asdf3lkjdu") is False


def test_for_special_symbol() -> None:
    assert check_password("A$@#&!-_89") is True


def test_missing_digit() -> None:
    assert check_password("NoDigit@") is False


def test_missing_special_symbol() -> None:
    assert check_password("NoSpacialSymbol1") is False


def test_all_lowercase() -> None:
    assert check_password("lowercase1@") is False
