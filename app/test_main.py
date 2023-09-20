import pytest
from app.main import check_password


@pytest.mark.parametrize("password, expected", [
    ("Pass@word1", True),
    ("Str@ng", False),
    ("Sp3c!als", False),
    ("qwerty", False),
])
def test_check_password(password, expected):
    assert check_password(password) == expected

