from app.main import check_password
import pytest


class TestPasswordValidation:
    @pytest.mark.parametrize(
        "password,result",
        [
            pytest.param("Qwer1_", False,
                         id="lenght < 8"),
            pytest.param("@we2tyqwerty", False,
                         id="hasn't uppercase letter"),
            pytest.param("$wertRqwerty", False,
                         id="hasn't digit"),
            pytest.param("qwertrEwert1", False,
                         id="hasn't special character"),
            pytest.param("1wertRqwert_", True,
                         id="all correct"),
            pytest.param("1wertRqwert_klfsjahda", False,
                         id="too long password > 16")
        ]
    )
    def test_password_validation(self, password, result):
        assert check_password(password) is result
