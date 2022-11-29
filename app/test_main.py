from app.main import check_password


def test_if_password_has_not_supported_special_characters() -> None:
    assert check_password("MZAFHb*5FmI") is False


def test_if_password_has_zero_characters() -> None:
    assert check_password("") is False


def test_if_password_has_less_than_eight_characters() -> None:
    assert check_password("v!UEaQ4") is False


def test_if_password_has_more_than_sixteen_characters() -> None:
    assert check_password("CoqyYw72W3O@q9qliXif") is False


def test_if_password_does_not_contain_at_least_one_digit() -> None:
    assert check_password("Z!FH&clqON") is False


def test_if_password_does_not_contain_at_least_one_special_character() -> None:
    assert check_password("mec1LkYtOCHfN") is False


def test_if_password_does_not_contain_at_least_one_uppercase_letter() -> None:
    assert check_password("wyxqx8hui3zo@") is False


def test_if_password_meets_all_requirements() -> None:
    assert check_password("ULdcGy2zpL!#Xjk") is True
