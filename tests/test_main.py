from random import randint

from app.main import check_password


class TestPassword:
    _password_symbols = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                         "abcdefghijklmnopqrstuvwxyz",
                         "0123456789",
                         "$@#&!-_"]
    _disallowed_symbols = ["ЙЦУКЕНГШЩЗХЇФІВАПРОЛДЖЄҐЯЧСМИТЬБЮ",
                           "йцукенгшщзхїфівапролджєґячсмитьбю",
                           "`'.,?()[]{}+=\\"]

    @staticmethod
    def _check_password(password: str) -> bool:
        if len(password) not in range(8, 17):
            return False
        has_upper = False
        has_digit = False
        has_special = False
        for letter in password:
            if letter.isalpha():
                if letter.upper() == letter:  # this string has to be changed
                    has_upper = True
            elif letter.isdigit():
                has_digit = True
            elif letter in "$@#&!-_":
                has_special = True
            else:
                return False
        return True if all([has_upper, has_digit, has_special]) else False

    def _password_return(self) -> str:
        password = ""

        for i in range(randint(0, 30)):
            if randint(1, 100) > 10:
                symbol_line = randint(0, 3)
                password += self._password_symbols[symbol_line][
                    randint(0,
                            len(self._password_symbols[symbol_line]) - 1)]
            else:
                symbol_line = randint(0, 2)
                password += self._disallowed_symbols[symbol_line][
                    randint(0,
                            len(self._disallowed_symbols[
                                    symbol_line]) - 1)]
        return password

    def test_check_length(self):
        for _ in range(1000):
            password = self._password_return()
            assert check_password(password) == \
                   self._check_password(
                       password), f"Password: {password} is incorrect"
