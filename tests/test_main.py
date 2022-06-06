import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("", False),
        ("qwertyqwertyqwertyqwerty", False),
        ("qwertyqw ertyqwertyqwerty", False)
    ]
)
def test_check_password(password, result):
    assert check_password(password) == result
