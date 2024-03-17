import pytest

# Assume check_password is defined in a module named password_validator.py
from app.main import check_password


@pytest.mark.parametrize("password, expected_result", [
    ("Pass@word1", True),  # Meets all criteria
    ("qwerty", False),  # Too short, no digit, no special character, no uppercase letter
    ("Str@ng", False),  # Too short, no digit
    ("12345678", False),  # Only digits
    ("ABCDEFGH", False),  # Only uppercase letters
    ("abcdefgh", False),  # Only lowercase letters
    ("@#$%^&*", False),  # Only special characters
    ("Password", False),  # No digit, no special character
    ("pass@1", False),  # Too short
    ("Password123", False),  # No special character
    ("pass@word1", False),  # No uppercase letter
    ("PASSWORD@1", True),  # No lowercase letter
    ("Pass@word123456789", False),  # Too long
    ("P@ssw0rd", True),  # Exactly 8 characters, meets all other criteria
    ("Passw0rd@", True),  # Exactly 8 characters, at the end special character, meets all criteria
    ("LongPass@word1", True),  # More than 8 characters, meets all criteria
    ("ReallyLongPassword123@", False),  # More than 16 characters
    ("P@1", False),  # Too short, even though it has a digit, uppercase letter, and special character
    ("ValidPassw@rd1", True),  # Valid with mixed characters
    ("InvalidPassword!!!!", False),  # No digits
    ("1234@678", False),  # No letters
    ("PASS@1234", True),  # No lowercase letter
    ("valid@pass1", False),  # No uppercase letter
    ("PASSWORD@123", False),  # No lowercase letter
    ("validpassword1", False),  # No special character
    ("$@#&!-_123Aa", True),  # All special characters, meets all criteria
])
def test_check_password(password, expected_result):
    assert check_password(password) == expected_result
