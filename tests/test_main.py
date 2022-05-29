from app.main import check_password


class TestCheckPassword:
    def test_should_return_false_when_less_then_8_characters(self):
        assert not check_password('Qwert@1')
        assert check_password('Qwert@12')

    def test_should_return_false_when_more_then_16_characters(self):
        assert not check_password('IFqwerty123A$357@')
        assert check_password('IFqwerty123A$357')

    def test_should_return_false_if_no_digit(self):
        assert not check_password("Qwerty@$a")
        assert check_password("Qwerty@$a1")

    def test_should_return_false_if_no_special_character(self):
        assert not check_password("Qwerty123a")
        assert check_password("Qwerty123$")

    def test_should_return_false_if_no_uppercase_letter(self):
        assert not check_password("qwerty123$")
        assert check_password("Qwerty123$")

    def test_should_return_false_when_use_not_allowed_symbols(self):
        assert not check_password("Qwerty123^$")
        assert check_password("Qwerty123$")

