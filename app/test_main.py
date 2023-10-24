from app.main import check_password


def test_short_password():
    assert check_password("Pa@rd1") is False


def test_too_long_password():
    assert check_password("Pass@word11111111") is False


def test_without_upper_case():
    assert check_password("pass@word1") is False


def test_check_digits():
    assert check_password("Pass@wordd") is False


def test_check_special_symbol():
    assert check_password("Passsword1") is False
