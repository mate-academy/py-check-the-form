from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Pass@word1") is True


def test_invalid_short_password() -> None:
    assert check_password("qwerty") is False


def test_invalid_no_digit_password() -> None:
    assert check_password("Str@ng") is False


def test_invalid_no_special_char_password() -> None:
    assert check_password("Password123") is False


def test_invalid_no_uppercase_password() -> None:
    assert check_password("pass@word1") is False


def test_invalid_long_password() -> None:
    assert check_password("TooLongPassword123456") is False


def test_valid_maximum_length_password() -> None:
    assert check_password("MaxLenPass@word1") is True


def test_invalid_exceed_maximum_length_password() -> None:
    assert check_password("ExceedMaxLenPass@word1") is False


def test_invalid_restricted_special_char_password() -> None:
    assert check_password("RestrictedChar$1") is True


def test_valid_custom_special_char_password() -> None:
    assert check_password("Custom@SpecialChar1") is False
