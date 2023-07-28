import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result", [
        ("Pass@word1", True),
        ("TestPass@123", True),
        ("AbCdEfGh1$", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("str", False),
        ("passwordistoolong1234567890987654321", False),
        ("abcdEFGH$", False),
        ("pass@word1", False),
        ("Test@123456789012345", False),
        ("", False),
        ("Pa5$$_", False),
        ("Password12345", False),
    ]
)
def test_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result
