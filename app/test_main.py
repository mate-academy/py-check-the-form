import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param(
            "Pass@word1",
            True,
            id="Test valid password"
        ),
        pytest.param(
            "qwerty",
            False,
            id="Test invalid password"
        ),
        pytest.param(
            "Str@ng",
            False,
            id="Test invalid password"
        ),
    ]
)
def test_check_password(
        password: str,
        result: bool
) -> None:
    assert check_password(password) == result
