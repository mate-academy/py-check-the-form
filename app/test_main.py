from app.main import check_password


def test_check_password_valid() -> None:
    assert check_password("Pass@word1") is True


def test_check_password_lowercase() -> None:
    assert check_password("qwerty") is False


def test_check_password_no_digits() -> None:
    assert check_password("Str@ng") is False


def test_check_password_uppercase() -> None:
    assert check_password("STDDDB") is False


def test_check_password_empty() -> None:
    assert check_password("") is False


def test_check_password_all_digits() -> None:
    assert check_password("114555") is False


def test_check_password_no_special_character() -> None:
    assert check_password("Str1ng") is False


def test_check_password_no_uppercase() -> None:
    assert check_password("t5r1n!g") is False
