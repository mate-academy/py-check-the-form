from app.main import check_password


def test_valid_password():
    # Test a valid password that meets all the criteria
    assert check_password('Pass@word1'), "Valid password should return True"


def test_valid_password_8_char():
    # Test a valid password that meets all the criteria
    assert check_password('Pas@wor1') == True


def test_short_password():
    # Test a password shorter than 8 characters
    assert not check_password('P@ss1'), "Password shorter than 8 characters should return False"


def test_long_password():
    # Test a password longer than 16 characters
    assert not check_password('VeryLongPass@word1'), "Password longer than 16 characters should return False"


def test_password_without_digit():
    # Test a password without any digits
    assert not check_password('Password@'), "Password without a digit should return False"


def test_password_without_special_character():
    # Test a password without any special characters
    assert not check_password('Password1'), "Password without a special character should return False"

def test_password_without_uppercase():
    # Test a password without any uppercase letters
    assert not check_password('pass@word1'), "Password without an uppercase letter should return False"


def test_password_with_invalid_characters():
    # Test a password with characters not allowed (e.g., spaces, other special characters not listed)
    assert not check_password('Pass@word1*'), "Password with invalid characters should return False"


def test_password_just_right_length():
    # Test a password that is exactly 8 characters long
    assert check_password('Pass@8d1'), "Password that is exactly 8 characters should return True"


def test_password_maximum_length():
    # Test a password that is exactly 16 characters long
    assert check_password('Pass@word1234Aa'), "Password that is exactly 16 characters should return True"
