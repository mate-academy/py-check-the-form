import pytest

from app.main import check_password


@pytest.mark.parametrize("password, valid",
                         [("Pass@word1", True),
                          ("Pass@word", False),
                          ("qwerty@1", False),
                          ("Password2", False),
                          ("123123", False),
                          ("", False),
                          ("Qsdfghjklzxcvbnm@1", False),
                          ("Qsdfghjklzxcmm@1", True),
                          ("Df@2", False)],
                         ids=[
                             "correct pass",
                             "no digit",
                             "no uppercase",
                             "no special symbol",
                             "only digits",
                             "len 0",
                             "len > 16",
                             "len == 16",
                             "len < 9"
                         ])
def test_check_pass(password: str, valid: bool) -> None:
    assert check_password(password) == valid
