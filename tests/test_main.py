from app.main import check_password


def test_too_short_password():
    assert check_password("qwerty") is False


def test_too_long_password():
    assert check_password("ExtraLongPassword") is False


def test_deprecated_symbols():
    assert check_password("*password") is False


def test_is_necessary_symbols_included():
    assert check_password("1@Password") is True


def test_without_capital_letters():
    assert check_password("qwertyqwerty") is False


def test_without_special_symbols():
    assert check_password("password") is False