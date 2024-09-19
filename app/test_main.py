from app.main import check_password

import pytest


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
