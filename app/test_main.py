import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_value",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False)
    ]
)
def test_check_password(password: str, expected_value: bool) -> None:
    assert check_password(password) == expected_value
