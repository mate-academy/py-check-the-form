import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("привіт43#&", False),
        ("qwerty", False),
        ("qwertyqwertyqwerty", False),
        ("qwertyqwerty", False),
        ("Pass@word1", True),

    ],
    ids=[
        "check for allowed chars",
        "check for at least 8 characters",
        "check for 16 characters exclusive",
        "check contains digit, special character, uppercase letter.",
        "everything OK!",
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
