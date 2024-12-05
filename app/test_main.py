import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, answer",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False)
    ]
)
def test_change_password(password: str, answer: bool) -> None:
    assert check_password(password) is answer
