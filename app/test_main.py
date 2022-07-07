from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "checked_password, expected",
    [
        pytest.param(
            "Pass@word1", True,
            id="password with letters, special symbols and numbers"
        ),
        pytest.param(
            "qwerty", False,
            id="less than 8 characters"
        ),
        pytest.param(
            "Str@ng", False,
            id="less than 8 characters"
        ),
        pytest.param(
            "passwordutg", True,
            id="without uppercase and special symbols"
        ),
        pytest.param(
            "Strongpass", True,
            id="without digits"
        ),
        pytest.param(
            "Strqwertyqwertylongqwert5432ij", False,
            id="long password"
        ),
    ]
)
def test_password(checked_password, expected):
    assert check_password(checked_password) == expected
