import pytest

from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "password, is_valid",
        [
            pytest.param(
                "Pass@word1",
                True,
                id="Password is valid"
            ),
            pytest.param(
                "Pass@word",
                False,
                id="Without digit"
            ),
            pytest.param(
                "Password1",
                False,
                id="Without special symbol"
            ),
            pytest.param(
                "Pas s@word1",
                False,
                id="With space"
            ),
            pytest.param(
                "passw@ord1",
                False,
                id="Without uppercase letter"
            )
        ]
    )
    def test_check_password(self, password, is_valid):
        assert check_password(password) == is_valid, f"Should return {is_valid}" \
                                                     f"if password is {password}"
