import pytest
from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize("password, expected_result", [
        ("Pass@word1", True),
        ("short", False),
        ("Too_long_password123456789", False),
        ("NoDigit@SpecialChar", False),
        ("NoSpecialChar1", False),
        ("nouppercase@1", False),
        ("Aa@12345", True),
        ("Max@length123456", True),
        ("Bound@123", True),
        ("Invalid@123", True),
        ("passwordWithoutDigits@", False),
        ("short1@", False),
        ("ThisPasswordIsWayTooLong123456789@", False)
    ])
    def test_check_password(
            self, password: str, expected_result: bool) -> None:
        assert check_password(password) == expected_result, \
            f"Password '{password}' should return {expected_result}"

    def test_should_check_min_length(self) -> None:
        invalid_passwords = ["", "aB@12", "12345678901234567890A"]
        for password in invalid_passwords:
            assert not check_password(password), \
                f"Password '{password}' should be invalid"

    def test_should_check_digit(self) -> None:
        invalid_passwords = ["aB@cdefgh", "NoDigit@SpecialChar",
                             "NoSpecialChar1", "nouppercase@1"]
        for password in invalid_passwords:
            assert not check_password(password), \
                f"Password '{password}' should be invalid"

    def test_should_check_length(self) -> None:
        valid_passwords = ["aB@12345", "LongEnough1$"]
        for password in valid_passwords:
            assert check_password(password), \
                f"Password '{password}' should be valid"

        invalid_passwords = ["Valid@Password",
                             "short1@", "TooLongPassword123456789"]
        for password in invalid_passwords:
            assert not check_password(password), \
                f"Password '{password}' should be invalid"
