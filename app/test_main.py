from app.main import check_password
import pytest


@pytest.fixture
def valid_password() -> None:
    return "Pass@word1"


@pytest.fixture
def invalid_password_too_short() -> None:
    return "AbcD123"


@pytest.fixture
def invalid_password_too_long() -> None:
    return "AbcD12345678901234"


@pytest.fixture
def invalid_password_no_digit() -> None:
    return "Password@"


@pytest.fixture
def invalid_password_no_special_character() -> None:
    return "Password123"


@pytest.fixture
def invalid_password_no_uppercase() -> None:
    return "password@123"


def test_check_password_valid(valid_password: any) -> None:
    assert check_password(valid_password) is True


def test_check_password_invalid_too_short(invalid_password_too_short: any) -> None:
    assert check_password(invalid_password_too_short) is False


def test_check_password_invalid_too_long(invalid_password_too_long: any) -> None:
    assert check_password(invalid_password_too_long) is False


def test_check_password_invalid_no_digit(
        invalid_password_no_digit: any
) -> None:
    assert check_password(invalid_password_no_digit) is False


def test_check_password_invalid_no_special_character(
        invalid_password_no_special_character: any
) -> None:
    assert check_password(invalid_password_no_special_character) is False


def test_check_password_invalid_no_uppercase(
        invalid_password_no_uppercase: any
) -> None:
    assert check_password(invalid_password_no_uppercase) is False
