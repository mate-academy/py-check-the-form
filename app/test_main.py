from unittest import mock

import pytest

from app.main import check_password


@pytest.mark.parametrize("password, result", [
    ("Pass@word1", False),
    ("qwerty", False),
    ("", False),
    ("Str@ng", False),
    ("P@word1", False)
])
@mock.patch("app.main.ascii_lowercase")
def test_check_password(
        mock_ascii_lowercase: mock.MagicMock,
        password: str,
        result: bool
):
    mock_ascii_lowercase = "abcdefghijklmnopqrstuvwxyz"
    assert check_password(password) == result
