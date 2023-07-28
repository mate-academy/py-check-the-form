import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result", [
        ("Pass@word1", True),
        ("TestPass@123", True),
        ("AbCdEfGh1$", True),
        ("$ecretP@ss", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("str", False),
        ("passwordistoolong1234567890987654321", False),
        ("abcdEFGH$", False),
    ]
)
def test_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result
