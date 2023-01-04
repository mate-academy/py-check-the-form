from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param(
            "qwewqeewqewq",
            False,
            id="test_should_check_upper_letter"
        ),
        pytest.param(
            "qweqweqwe",
            False,
            id="test_should_check_digit"
        ),
        pytest.param(
            "qweqweqwe",
            False,
            id="test_should_check_special_symbols"
        ),
        pytest.param(
            "qweqwe",
            False,
            id="test_should_check_min_length"
        ),
        pytest.param(
            "qweqweqweqweqweqwe",
            False,
            id="test_should_check_max_length"
        ),
        pytest.param(
            "Pass@word1",
            True,
            id="1 digit, 1 special character, 1 uppercase letter."
        )
    ]
)
def test_password(password: str, result: bool) -> None:
    assert check_password(password) is result
