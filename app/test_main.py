import pytest

from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "password, expected",
        [
            pytest.param(
                "Pass@word1", True,
                id="Should return 'True' "
            ),
            pytest.param(
                "qwerty", False,
                id="Should return 'False'"
            ),
            pytest.param(
                "Str@ng", False,
                id="Should return 'False'"
            ),
            pytest.param(
                "12345", False,
                id="Should return 'False'"
            ),
            pytest.param(
                "H33l0 w0rld", False,
                id="Should return 'False'"
            ),
            pytest.param(
                "Pass@word1Pass@word1Pass@word1", False,
                id="Should return 'False'"
            )
        ]
    )
    def test_check_password(self,
                            password: str,
                            expected: bool) -> None:
        assert check_password(password) == expected
