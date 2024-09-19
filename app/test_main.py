from app.main import check_password
import pytest


@pytest.mark.parametrize("password, examination", [
    ("Pass@word1", True),
    ("qwerty", False),
    ("Str@ng", False),
])
def test_check_password(password: str, examination: str) -> None:
    assert check_password(password) == examination
