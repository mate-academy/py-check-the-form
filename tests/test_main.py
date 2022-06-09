from app.main import check_password

import pytest


@pytest.mark.parametrize(
    "password, expected",
    [
        ("1l0v3m@t3_", False),
        ("$@#&!-_1dddwfj", False),
    ],
)
def test_without_upper_letters(password, expected):
    assert check_password(password) is expected


@pytest.mark.parametrize(
    "password, expected",
    [
        ("HKnDs@$@t..uUhLs_", False),
        ("$@#&!-_ddwfj", False),
    ],
)
def test_without_digits(password, expected):
    assert check_password(password) is expected


@pytest.mark.parametrize(
    "password, expected",
    [
        ("1Df5Fes6ErfgG548", False),
        ("1qW6G8Kkl4BB7sJ", False),
    ],
)
def test_without_special_character(password, expected):
    assert check_password(password) is expected


@pytest.mark.parametrize(
    "password, expected",
    [
        ("$@#&!1D", False),
        ("Q!@#$1346fdsfdshDVUJhDVYUkldn", False),
    ],
)
def test_when_length_less_8_or_more_16(password, expected):
    assert check_password(password) is expected


@pytest.mark.parametrize(
    "password, expected",
    [
        ("1!Q#E$RhTd75", True),
        ("Q!@#$1346Fsfd", True),
    ],
)
def test_when_all_right(password, expected):
    assert check_password(password) is expected
