import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result", [
        ("Small@1", False),
        ("Very_nice@123!", True),
        ("To_Big_Password_123@!", False)
    ]
)
def test_should_check_length_of_password(password, result):
    assert check_password(password) is result


@pytest.mark.parametrize(
    "password,result", [
        ("p@ssword_123", False),
        ("PassWord123", False),
        ("Pass@Word_", False),
        ("Pass@Word_123!", True)
    ]
)
def test_should_check_at_least_1_digit_1_special_char_1_uppercase_letter(
        password, result):
    assert check_password(password) is result


@pytest.mark.parametrize(
    "password,result", [
        ("P@ssword_123/{}*+-", False),
        ("Pass123$@#&!-_", True)
    ]
)
def test_should_check_special_character(password, result):
    assert check_password(password) is result
