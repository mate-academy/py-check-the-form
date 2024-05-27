import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, is_password",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False)
    ]
)
def test_check_password(password: str, is_password: bool) -> None:
    assert check_password(password) == is_password
