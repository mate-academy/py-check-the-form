from typing import Union
import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        (
            "Pass@word1", True
        ),
        (
            "qwerty", False
        ),
        (
            "Str@ng", False
        ),
        (
            "Password_123456789@", False
        ),
        (
            "S-1234567", True
        ),
        (
            "2222-3345", False
        ),
        (
            "B5553345", False
        ),
        (
            "Words_Box", False
        ),
        (
            "checktext", False
        ),
        (
            "9876543210", False
        ),
        (
            "$@#&!-_-#", False
        ),
    ]
)
def test_check_password_correctly(
        password: Union[int | str],
        result: bool
) -> None:

    assert check_password(password) == result
