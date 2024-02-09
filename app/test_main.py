from app.main import check_password
import pytest


class TestsMain:
    @pytest.mark.parametrize(
        "password,result",
        [
            pytest.param(
                "qqqqQ1$∞",
                False,
                id="Not acceptable characters"
            ),
            pytest.param(
                "Qq1#",
                False,
                id="Less than 8 characters"
            ),
            pytest.param(
                "Qq1#rfdsjJdf345lsfkjfieiei5kdsa88-",
                False,
                id="More than 16 characters"
            ),
            pytest.param(
                "-Ddddddddd",
                False,
                id="Check for digit"
            ),
            pytest.param(
                "1Ddddddddd",
                False,
                id="Check for special character"
            ),
            pytest.param(
                "-1dddddddd",
                False,
                id="Check for uppercase letter"
            ),
        ]
    )
    def test_check_password(
            self,
            password: str,
            result: bool,
    ) -> None:
        assert check_password(password) == result
