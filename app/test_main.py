import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Password1", False),
        ("qwertywdzd", False),
        ("strongerr", False),
        ("slow", False),
        ("Ghj2@lkfjhdasdffffq", False),
        ("qwertyqwer", False),
    ],
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
