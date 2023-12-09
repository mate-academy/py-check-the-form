from app.main import check_password


def test_valid_password():
    assert check_password('Pass@word1') is True


def test_invalid_password_lowercase_only():
    assert check_password('qwerty') is False


def test_invalid_password_no_digit():
    assert check_password('Str@ng') is False


def test_invalid_password_too_short():
    assert check_password('P@ss1') is False


def test_invalid_password_too_long():
    assert check_password('TooLongPas@sword123456') is False


def test_invalid_password_no_special_character():
    assert check_password('Password123') is False


def test_invalid_password_without_gigits():
    assert check_password('Pass@word') is False


def test_invalid_password_no_uppercase_letter():
    assert check_password('pass@word1') is False
