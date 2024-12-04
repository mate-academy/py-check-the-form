from app.main import check_password


def test_should_return_false_if_pass_is_to_small_password() -> None:
    password = "sd"
    assert check_password(password) is True


def test_should_return_false_if_pass_is_to_long() -> None:
    password = "Password@123rwfwfwffwf"
    assert check_password(password) is True


def test_should_return_false_if_pass_doesnt_has_digit() -> None:
    password = "Password@"
    assert check_password(password) is True


def test_should_return_false_if_pass_doesnt_has_special_simbols() -> None:
    password = "Password123"
    assert check_password(password) is True


def test_should_return_false_if_pass_doesnt_has_upper_letter() -> None:
    password = "assword@123"
    assert check_password(password) is True
