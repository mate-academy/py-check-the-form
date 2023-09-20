import pytest
from app.main import check_password


@pytest.mark.parametrize("password, expected", [
    ("Pass@word1", True),
    ("Str@ng", False),
    ("Abc@123", True),
    ("Sp3c!@l", False),
    ("qwerty", False),
    ("Str@ng", False)
])
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
