import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "given_password,result", [
        ("PASSWORD", False),
        ("TOOOOOLONGPASSWOOOORD", False),
        ("pass", False),
        ("qwerty", False),
        ("digitsdigits", False),
        ("Str@ng", False),
        ("Pass@word1", True),
        ("GoodPassword!1", True)
    ]
)
def test_check_password_correct_result(given_password,
                                       result):
    assert check_password(given_password) is result
