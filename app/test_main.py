from app.main import check_password
import pytest


@pytest.mark.parametrize("password, examination", [
    ("Pass@word1", True),
    ("qwerty", False),
    ("Str@ng", False),
    ("Password@123", True),
    ("Short@1", False),
])
def test_check_password(password: str, examination: str) -> None:
    assert check_password(password) == examination
