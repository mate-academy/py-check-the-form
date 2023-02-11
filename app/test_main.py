import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("qwertyq", False),
        ("", False),
        ("qwertqwertqwerty", False),
        ("pass@word1", False),
        ("Passwords", False),
        ("Passwords@", False),
        ("Password1s", False),

    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) is result
