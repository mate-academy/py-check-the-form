import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        pytest.param(
            "",
            False,
            id="Empty password area."
        ),
        pytest.param(
            "Pass@word1",
            True,
            id="Correct password."
        ),
        pytest.param(
            "qwerty",
            False,
            id="Password should contain at least 1 digit, "
               "1 special character, 1 uppercase letter and have len >= 8"
        ),
        pytest.param(
            "qwertyowe",
            False,
            id="Password should contain at least 1 digit, "
               "1 special character, 1 uppercase letter"
        ),
        pytest.param(
            "Str@ng",
            False,
            id="Password should contain at least 1 digit and have len >= 8"
        ),
    ]
)
def test_check_password(password, result):
    assert check_password(password) == result
