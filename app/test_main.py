import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, approved", [
        ("Pass@word1", True),
        ("Pass@word1Pass@word1", False),
        ("Pass@word", False),
        ("Pass@word1", True),
        ("1Pass@w", False),
        ("1Passw5qwer", False),
        ("1passw5qwer@", False)
    ]
)
def test_check_password(password: str, approved: bool) -> None:
    assert check_password(password) is approved
