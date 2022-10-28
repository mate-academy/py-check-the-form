from app.main import check_password


def test_check_password_return_false_for_short_password():
    assert check_password("@mC1") is False


def test_check_password_return_false_for_long_password():
    assert check_password("@@@HytgHukiy23tt@@@@gfgfggv") is False


def test_check_password_return_false_for_password_no_symbols():
    assert check_password("Holah0ype") is False


def test_check_password_return_false_for_password_no_big_letter():
    assert check_password("m@cb00kair") is False


def test_check_password_return_false_for_password_no_digits():
    assert check_password("Holah@ype") is False