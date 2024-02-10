from app.main import check_password


class TestCheckPassword():
    def test_check_password_short(self) -> None:
        assert check_password("Q@1wert") is False

    def test_check_password_long(self) -> None:
        assert check_password("TooLongPassword123!@#$") is False

    def test_check_password_check_upper_letter(self) -> None:
        assert check_password("pass@word1") is False

    def test_check_password_check_check_digit(self) -> None:
        assert check_password("Str@ngnd") is False

    def test_check_password_check_with_all_requirement(self) -> None:
        assert check_password("Pass@word1") is True

    def test_check_password_without_special_symbols(self) -> None:
        assert check_password("Passrword1") is False
