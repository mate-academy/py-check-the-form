from app.main import check_password


def test_check_max_len() -> None:
    assert check_password("adbdhdjskdjadjadjjcaas") is False


def test_check_min_len() -> None:
    assert check_password("adbdh") is False


def test_upper_case() -> None:
    assert check_password("Adbdh") is False


def test_right() -> None:
    assert check_password("Pass@word1") is True


def test_not_digits() -> None:
    assert check_password("Pass@word") is False


def test_not_special_symbols() -> None:
    assert check_password("Password1") is False
