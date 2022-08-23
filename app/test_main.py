import pytest
from app.main import check_password


@pytest.fixture()
def password():
    return ""


def test_should_check_min_length(password: str) -> bool:
    if len(password) > 16:
        return False
    has_upper = False
    has_digit = False
    has_special = False
    for letter in password:
        if letter.isalpha():
            if letter.upper() == letter:
                has_upper = True
        elif letter.isdigit():
            has_digit = True
        elif letter in "$@#&!-_":
            has_special = True
        else:
            return False
    return all([has_upper, has_digit, has_special])


def test_should_check_max_length(password: str) -> bool:
    if len(password) < 8:
        return False
    has_upper = False
    has_digit = False
    has_special = False
    for letter in password:
        if letter.isalpha():
            if letter.upper() == letter:
                has_upper = True
        elif letter.isdigit():
            has_digit = True
        elif letter in "$@#&!-_":
            has_special = True
        else:
            return False
    return all([has_upper, has_digit, has_special])


def test_should_check_upper_letter(password: str) -> bool:
    if len(password) not in range(8, 17):
        return False
    has_digit = False
    has_special = False
    for letter in password:
        if letter.isdigit():
            has_digit = True
        elif letter in "$@#&!-_":
            has_special = True
        elif letter.isalpha():
            continue
        else:
            return False
    return all([has_digit, has_special])


def test_should_check_digit(password: str) -> bool:
    if len(password) not in range(8, 17):
        return False
    has_upper = False
    has_special = False
    for letter in password:
        if letter.isalpha():
            if letter.upper() == letter:
                has_upper = True
        elif letter.isdigit():
            continue
        elif letter in "$@#&!-_":
            has_special = True
        else:
            return False
    return all([has_upper, has_special])


def test_should_check_special_symbols(password: str) -> bool:
    if len(password) not in range(8, 17):
        return False
    has_upper = False
    has_digit = False
    has_special = False
    for letter in password:
        if letter.isalpha():
            if letter.upper() == letter:
                has_upper = True
        elif letter.isdigit():
            has_digit = True
        elif letter in "$@#&!-_":
            has_special = True
        else:
            return False
    return all([has_upper, has_digit])
