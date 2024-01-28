import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("Pass@word1", True),
        ("Sh@r7", False),
        ("More_than_16_@re_here!", False),
        ("qwertyu#", False),
        ("Str@ng!!", False),
        ("TestPassword", False),
    ],
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
