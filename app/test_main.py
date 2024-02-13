from app.main import check_password


def test_check_password() -> None:
    assert check_password('qwerty') is False
    assert check_password('Pass@word1') is True
    assert check_password('pass@word1') is False
    assert check_password('pass@word1111111') is True
    assert check_password('pass@word11111111') is False
    assert check_password('Str@ng') is False
