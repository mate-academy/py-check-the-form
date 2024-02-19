import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        (" ", False),
        ("Asdsdfdf", False),
        ("ъуъ", False),
        ("8h7g6frc", False)
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
