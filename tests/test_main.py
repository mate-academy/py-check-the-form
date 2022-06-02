import pytest

from app.main import check_password


class TestMain:

    @pytest.mark.parametrize(
        "password_for_check, func_returns",
        [
            pytest.param("Pass1@", False,
                         id="len of password must be 8-16 symbols"),
            pytest.param("Pass1@svvhrtxweqcgcrwtgwceg", False,
                         id="len of password must be 8-16 symbols"),
            pytest.param("пароль1@", False,
                         id="password must consist only Latin alphabet"),
            pytest.param("password1@", False,
                         id="password should have uppercase letter"),
            pytest.param("Password1", False,
                         id="password should have at"
                            " least 1 special character"),
            pytest.param("Password@", False,
                         id="password should have at least 1 digit"),
            pytest.param("Pass@word1", True,
                         id="password should have uppercase letter")
        ]
    )
    def test_check_password(self, password_for_check, func_returns):

        assert check_password(password_for_check) == func_returns
