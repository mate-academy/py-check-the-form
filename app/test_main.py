import pytest
from app.main import check_password


@pytest.mark.parametrize("password", [
    "Pass@word1",
    "AaBbC123$",
    "AbCdEfGh$9-",
    "AbcDefg$1",
    "A@B1-cdEfgh"
])
def test_valid_passwords(password: any) -> None:
    assert check_password(password) is True

# Invalid passwords


@pytest.mark.parametrize("password", [
    "qwerty",
    "Str@ng",
    "Password12",
    "abcdEFGH12345",
    "invalid@pass&",
    "P@$$word"
])
def test_invalid_passwords(password: any) -> None:
    assert check_password(password) is False
