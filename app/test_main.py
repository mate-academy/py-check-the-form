import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Pass@word134547", True)
    ]
)
def test_valid_password(password: str, result: bool) -> None:
    assert check_password(password) == result
