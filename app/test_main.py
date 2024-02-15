import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    (
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Pass@word1Pass@word1", False),
        ("11111111", False),
        ("a1a1a1a1a", False),
        ("x-x-x-x-x-x", False),
    )
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) is result
