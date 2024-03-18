import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Mate_academy19908", False),

    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
