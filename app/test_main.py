import pytest
from .main import check_password


@pytest.mark.parametrize(
    "has_upper, has_digit, has_special,pass_len, password",
    [
        (True, True, True, True, "Pass@word1"),
        (False, True, True, True, "q@1rtyfg"),
        (True, False, True, False, "Str@ng"),
        (True, False, True, False, "Str@ngsdcjsc"),
        (False, True, False, True, "123456df"),
        (False, True, False, False, "12345df"),
        (False, True, True, False, "12345df1234rfwf@"),
        (True, True, True, False, "A2@e"),
        (True, True, True, False, "A2@487979ghjgkjg"),
    ]
)
def test_check_password(
    has_upper: bool,
    has_digit: bool,
    has_special: bool,
    pass_len: bool,
    password: str
) -> None:
    password_check = check_password("Pass@word1")
    passw = bool
    if len(password) is True:
        if passw == all([has_upper, has_digit, has_special]):
            assert password_check == passw
        elif passw == any([has_upper, has_digit, has_special, pass_len]):
            assert password_check == passw
