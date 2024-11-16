import pytest
from app.main import check_password

def test_check_password():
    assert check_password("Pass@word1") is True
    assert check_password("Hello@123") is True
    assert check_password("Secure@99") is True

def test_short_password():
    assert check_password("Short@1") is False

def test_long_password():
    assert check_password("IsLong@password123") is False

def test_no_digit():
    assert check_password("Nodigit@") is False

def test_no_special_character():
    assert check_password("NoSpec1al") is False

def test_no_uppercase():
    assert check_password("n0uppercase@") is False

def test_only_specials():
    assert check_password("@@@@@111") is False