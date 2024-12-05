import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, answer",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False)
    ]
)
def test_change_password(password: str, answer: bool) -> None:
    assert check_password(password) is answer


def test_should_check_min_length() -> None:
    result = check_password("Short1!")
    assert result is False, ("Password shorter than 8 characters"
                             " should fail validation")


def test_should_check_upper_letter() -> None:
    result = check_password("nouppercase1!")
    assert result is False, ("Password without uppercase letters "
                             "should fail validation")


def test_should_check_digit() -> None:
    result = check_password("NoDigitHere!")
    assert result is False, ("Password without digits should fail"
                             " validation")


def test_should_check_special_symbols() -> None:
    result = check_password("NoSpecials1")
    assert result is False, ("Password without special symbols should "
                             "fail validation")


def test_should_check_max_length() -> None:
    result = check_password("ThisPasswordIsWayTooLong123!")
    assert result is False, ("Password longer than 16 characters should "
                             "fail validation")
