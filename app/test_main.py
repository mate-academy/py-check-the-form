import pytest
from app.main import check_password


@pytest.mark.parametrize("password, expected", [
    ("Pass@word1", True),
    ("qwerty", False),
    ("Str@ng", False),
    ("Abcdefg1", False),
    ("P@ssw0rd_WithLongLength123", False),
    ("Abc@123", True),
    ("Short@1", False),
    ("Sp3c!@l", False),
])
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
