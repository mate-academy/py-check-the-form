from app.main import check_password


class TestCheckPassword:
    def test_should_return_false_when_less_then_8_characters(self):
        assert check_password('Qwert@1') is False
        assert check_password('Qwert@12') is True

    def test_should_return_false_when_more_then_16_characters(self):
        assert check_password('IFqwerty123A$357@') is False
        assert check_password('IFqwerty123A$357') is True

    def test_should_return_false_if_no_digit(self):
        assert check_password("Qwerty@$a") is False
        assert check_password("Qwerty@$a1") is True

    def test_should_return_false_if_no_special_character(self):
        assert check_password("Qwerty123a") is False
        assert check_password("Qwerty123$") is True

    def test_should_return_false_if_no_uppercase_letter(self):
        assert check_password("qwerty123$") is False
        assert check_password("Qwerty123$") is True

    def test_should_return_false_when_use_not_allowed_symbols(self):
        assert check_password("Qwerty123^$") is False
        assert check_password("Qwerty123$") is True
