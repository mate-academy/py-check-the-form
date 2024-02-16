import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("Qwerty", False),
        ("123456", False),
        ("fiuuuu#", False),
        ("#wsxer6RDT43", False),
        ("frD#dserdtututu2sdasdaf", False),
        (";8h7g6frc", False)
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
