import pytest

from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "password, check",
        [
            pytest.param(
                "",
                False,
                id="password is empty string"
            ),
            pytest.param(
                "ABCD123$",
                True,
                id="password is valid"
            ),
            pytest.param(
                "abcd123$",
                False,
                id="password without upper letter"
            ),
            pytest.param(
                "12345678",
                False,
                id="password contains only digits"
            ),
            pytest.param(
                "Abcdef0123456789$",
                False,
                id="password length more than 16 characters"
            ),
            pytest.param(
                "Abc012$",
                False,
                id="password length less than 8 characters"
            ),
            pytest.param(
                "Abcdefgh$",
                False,
                id="password without digits"
            ),
            pytest.param(
                "Abcd0123",
                False,
                id="password without special character"
            ),
        ]
    )
    def test_check_password(self, password, check):
        assert check_password(password) == check
