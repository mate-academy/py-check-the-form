from app.main import check_password

import pytest


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Password!", False),
        ("AnotherLongPassword!@#", False),
        ("alllower123!", False),
        ("NoSpecialChar1A", False),
        ("Short1@", False),
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
