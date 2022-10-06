from app.main import check_password


def test_strong_password() -> None:
    assert check_password("p_ASS#wrd4") is True


def test_short_password() -> None:
    assert check_password("01@ss") is False


def test_long_password() -> None:
    assert check_password("23456987655493457395395739485") is False


def test_password_without_numbers() -> None:
    assert check_password("Edikedik") is False


def test_password_without_upper() -> None:
    assert check_password("pss#word1108") is False


def test_password_without_symbols() -> None:
    assert check_password("Password1999") is False
