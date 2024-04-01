import pytest
from app.main import check_password


class TestCheckPasswerd:

    @pytest.mark.parametrize(
        "password, result",
        [
            pytest.param(
                "Pass1@q",
                False,
                id="should return false when lenght < 8"
            ),
            pytest.param(
                "Pass1@Pass1@Pass3",
                False,
                id="should return false when lenght > 16"
            ),
            pytest.param(
                "12345678@",
                False,
                id="should return false when no letter"
            ),
            pytest.param(
                "password1@",
                False,
                id="should return false when no uppercase letter"
            ),
            pytest.param(
                "Password@",
                False,
                id="should return false when no digit in password"
            ),
            pytest.param(
                "Password123",
                False,
                id="should return false when no special symbol",
            ),
            pytest.param(
                "Password1$)",
                False,
                id="should return false when contains forbidden symbol",
            ),
            pytest.param(
                "PASSWORD1@",
                True,
                id="should return True when all letters are uppercase",
            ),
        ],
    )
    def test_should_return_correct_result(
        self,
        password: str,
        result: bool
    ) -> None:
        assert check_password(password) == result
