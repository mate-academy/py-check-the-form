import pytest
from app.main import check_password


@pytest.fixture
def pass_template() -> str:
    return "123455678"


def test_valid_password() -> None:
    assert check_password("Pass@word1")


def test_should_check_min_length(pass_template: str) -> None:
    assert len(pass_template) >= 8 and len(pass_template) <= 16


def test_should_check_digit(pass_template: str) -> None:
    assert not check_password("Str@ng")


def test_should_check_special_character() -> None:
    assert not check_password("Password1")


def test_should_check_upper_letter() -> None:
    assert not check_password("pass@word1")


def test_should_check_max_length() -> None:
    assert not check_password("ThisIsTooLongPassword@1234")


def test_empty_password() -> None:
    assert not check_password("")
