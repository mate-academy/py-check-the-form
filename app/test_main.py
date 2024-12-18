import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word", True),
        ("qwerty", False),
        ("Str@ng", False)
    ]
)
def test_should_check_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result