import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "psw, expected_result",
    [
        pytest.param(
            "Aa12345+",
            False,
            id="value should equal mask. Should return False"
        ),
        pytest.param(
            "Aa12345",
            False,
            id="value should be greater or equal than 8. Should return False"
        ),
        pytest.param(
            "1" * 17,
            False,
            id="value should be less than 16. Should return False"
        ),
        pytest.param(
            "$@#&!-_1Aa",
            True,
            id="Should return True"
        ),
        pytest.param(
            "123456aA",
            False,
            id="Psw not contain special symbols. Should return False"
        )
    ]
)
def test_check_password(psw, expected_result):
    assert check_password(psw) == expected_result


def test_should_check_digit(psw):
    for el in psw:
        if el in "1234567890":
            return True
    return False
