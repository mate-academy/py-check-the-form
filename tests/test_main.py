import pytest

from app.main import check_password

@pytest.mark.parametrize(
    "password, is_valid",
    [
        ("Pass@word1", True),
        ("Str@ng", False),
        ("pasword213wfds322", False),
        ("password", False)
    ]
)
def test_check_password(password, is_valid):
    assert check_password(password) == is_valid
