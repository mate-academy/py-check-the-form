from app.main import check_password


def test_length_min_8_char():
    assert check_password("Povs@2h") is False


def test_length_max_16_char():
    assert check_password("Povs@2hcwDfkey7ck") is False


def test_str_with_uppercase_letter():
    assert check_password("v7n!fegl") is False


def test_str_with_digits():
    assert check_password("Von!fegl") is False


def test_str_has_special_char():
    assert check_password("Von6fegl") is False
