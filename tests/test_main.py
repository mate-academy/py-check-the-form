import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,valid",
    [
        ("", False),
        ("Pass@word1", True),
        ("Qwerty@12345679$#", False)
    ]
)
def test_check_password(password: str, valid: bool):
    answer = check_password(password)

    assert answer == valid
