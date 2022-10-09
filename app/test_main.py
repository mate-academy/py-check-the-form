import pytest
from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "test_password, expected_result",
        [
            ("Very_long_password$@#", False),
            ("Short_(", False),
            ("with0utChar", False),
            ("with0ut_upper!", False),
            ("without_numbEr!@", False),
            ("Pass@word1", True)
        ]
    )
    def test_check_password(
            self,
            test_password: str,
            expected_result: bool
    ) -> None:
        assert check_password(test_password) == expected_result
