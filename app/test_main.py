import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Amwee11", False),
        ("Qhj3rty9&3", True),
        ("Ajdnwhjkl90876$!-", False),
        ("kda^W)0", False),
        ("Hkhlhhgf*_", False),
        ("wkkdks876$_", False),
    ],
    ids=[
        "Special character missing",
        "Password length 8-16 symbols",
        "Password length more then 16 symbols",
        "Password length less then 8 symbols",
        "Digits missing",
        "Uppercase letters missing",

    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
