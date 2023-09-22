import pytest

from app.main import check_password

@pytest.fixture()
def password():
    return "Pass@word1"


def test_check_password_with_valid_password(password):
    assert check_password(password) == True


def test_check_password_with_special_symbols(password):
    password = "Password1"
    assert check_password(password) == False


def test_check_password_with_min_length(password):
    password = "Pass@1"
    assert check_password(password) == False

def test_check_password_with_max_length(password):
    password = "Pass@word1Pass@word1"
    assert check_password(password) == False


def test_check_password_with_out_digits(password):
    password = "Pass@word"
    assert check_password(password) == False

def test_check_password_with_out_uppercase(password):
    password = "pass@word1"
    assert check_password(password) == False