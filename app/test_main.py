from app.main import check_password


def test_for_true_password():
    assert check_password("Password_1")


def test_without_a_capital_letter():
    assert not check_password("password_1")


def test_without_a_number():
    assert not check_password("Password_")


def test_without_a_special_character():
    assert not check_password("Password1")


def test_less_than_8_characters():
    assert not check_password("Pass_1")


def test_more_than_16_characters():
    assert not check_password("ItismyPassword_11")


def test_misfits_characters():
    assert not check_password("Password_1++")


def test_when_only_numbers():
    assert not check_password("357348573")


def test_password_with_spaces():
    assert not check_password("Pass word_1")
