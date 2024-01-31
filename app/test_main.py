import pytest
from app.main import check_password


@pytest.mark.parametrize("password, expected_result", [
    ("Pass@word1", True),
    ("AbcdEfgh1", True),
    ("Secret@123", True),
    ("Short1!", False),
    ("Toolongpassword123456789", False),
    ("Abc123", False),
    ("Invalid@password", False),
    ("Invalidpassword!", False),
    ("12345$67890", False),
    ("Onlyletters", False),
    ("NoSpecialCharacter1", False),
    ("Nodigit@norSpecial", False),
    ("Aa1$Bb2&Cc3!Dd4-Ee_5f", True),
    ("Aa1$Bb2&Cc3!Dd4-Ee_5fG", False),
    ("Aa1$Bb", False),
])
def test_check_password(password: str, expected_result: str) -> None:
    assert check_password(password) == expected_result
