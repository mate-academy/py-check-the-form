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
                "Pass@word1Pass@word1Pass@word1", False,
                id="Should return returns False for"
                   " too long passwords"
            ),
            pytest.param(
                "Str@ng", False,
                id="Should return 'False'"
            ),
            pytest.param(
                "Password1", False,
                id="Should returns False for passwords"
                   " without special symbols"
            ),
            pytest.param(
                "Password", False,
                id="Should returns False for passwords"
                   " without digits"
            ),
            pytest.param(
                "abrakadabra", False,
                id="Should  returns False for passwords"
                   " without uppercase letter"
            ),
            pytest.param(
                "Pass", False,
                id="Should returns False for short passwords"
            )
        ]
    )
    def test_check_password(self,
                            password: str,
                            expected: bool) -> None:
        assert check_password(password) == expected
