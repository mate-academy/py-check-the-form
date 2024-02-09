import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("пароль43$2#", False),
        ("frD#3", False),
        ("frD#dserdtututu2sdasdaf", False),
        ("Qwertysse#", False)
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
