import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("Pass@word1", True),
        ("Sh@r7", False),
        ("More_than_16_are_here!", False),
        ("qwerty", False),
        ("Str@ng", False),
        ("TestPassword", False),
    ],
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
