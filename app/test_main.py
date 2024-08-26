# write your code here
import pytest
from app.main import check_password  # Replace 'your_module' with the actual module name


def test_valid_passwords():
    assert check_password('Pass@word1') is True
    assert check_password('A1b@Cdef') is True
    assert check_password('A1@verylongpassword') is True  # 16 characters, valid
    assert check_password('12345678$@') is True
    assert check_password('1A!b2C#d3E4') is True


def test_invalid_passwords():
    assert check_password('qwerty') is False  # No uppercase, no digit, no special char
    assert check_password('Str@ng') is False  # Too short, no digit
    assert check_password('LongPassword1234567890!') is False  # Too long
    assert check_password('short1@') is False  # Too short
    assert check_password('NoDigitsOrSpecialChar') is False  # No digit, no special char
    assert check_password('12345678') is False  # No uppercase, no special char
    assert check_password('!@#$%^&') is False  # No letters, no digits
    assert check_password('A1b@') is False  # Too short


def test_edge_cases():
    assert check_password('A1@aaaaaaa') is True  # Exactly 8 characters, valid
    assert check_password('A1@aaaaaaaaaaaaaaa') is True  # Exactly 16 characters, valid
    assert check_password('A1@aaaaaaaaaaaaaaaa') is False  # 17 characters, invalid
    assert check_password('A1@') is False  # Exactly 4 characters, too short
    assert check_password('A1') is False  # Exactly 2 characters, too short


@pytest.mark.parametrize(
    "password, expected",
    [
        ('Pass@word1', True),
        ('qwerty', False),
        ('Str@ng', False),
        ('A1b@Cdef', True),
        ('A1@verylongpassword', True),
        ('12345678$@', True),
        ('1A!b2C#d3E4', True),
        ('LongPassword1234567890!', False),
        ('short1@', False),
        ('NoDigitsOrSpecialChar', False),
        ('12345678', False),
        ('!@#$%^&', False),
        ('A1b@', False),
        ('A1@aaaaaaa', True),
        ('A1@aaaaaaaaaaaaaaa', True),
        ('A1@aaaaaaaaaaaaaaaa', False),
        ('A1@', False),
        ('A1', False),
    ]
)
def test_password_parametrized(password, expected):
    assert check_password(password) == expected
