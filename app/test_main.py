import unittest
from app.main import check_password


class TestCheckPassword(unittest.TestCase):
    def test_valid_password(self: "TestCheckPassword") -> None:
        self.assertEqual(check_password("Pass@word1"), True,
                         "Password should be recognized as valid")

    def test_short_password(self: "TestCheckPassword") -> None:
        self.assertEqual(check_password("qwerty"), False,
                         "Short password should "
                         "be recognized as invalid")

    def test_password_without_special_character(
            self: "TestCheckPassword") -> None:
        self.assertEqual(check_password("StrongPassword1"), False,
                         "Password without special "
                         "symbols should be recognized as invalid")

    def test_password_without_digit(self: "TestCheckPassword") -> None:
        self.assertEqual(check_password("Password@"), False,
                         "Password without a digit "
                         "should be recognized as invalid")

    def test_password_without_uppercase(self: "TestCheckPassword") -> None:
        self.assertEqual(check_password("password@1"), False,
                         "Password without an "
                         "uppercase letter should be recognized as invalid")

    def test_long_password(self: "TestCheckPassword") -> None:
        self.assertEqual(check_password("P" * 17 + "@1"), False,
                         "Long password should "
                         "be recognized as invalid")

    def test_password_with_only_lowercase_letters_and_special_characters(
            self: "TestCheckPassword") -> None:
        self.assertEqual(check_password("password@!"), False,
                         "Password without a digit and an "
                         "uppercase letter should be recognized as invalid")

    def test_password_with_only_letters_and_digits(
            self: "TestCheckPassword") -> None:
        self.assertEqual(check_password("Password1"), False,
                         "Password without a special "
                         "character should be recognized as invalid")


if __name__ == "__main__":
    unittest.main()
