import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        pytest.param(
            "Pass@word1", True,
            id="Strong password 'Pass@word1'"
        ),
        pytest.param(
            "qwerty", False,
            id="Weak password 'qwerty'"
        ),
        pytest.param(
            "Str@ng", False,
            id="Weak password 'Str@ng'"
        ),
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
