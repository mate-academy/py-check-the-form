from app.main import check_password


def test_if_the_password_is_correct() -> None:
    assert check_password("Pass@word1") is True


def test_if_the_password_isnt_correct() -> None:
    assert check_password("qwerty") is False
