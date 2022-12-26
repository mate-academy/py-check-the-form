import pytest

from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize("password, expected_result", [
        pytest.param("Pass@word1", True,
                     id="Correct password must have 1 digit, "
                        "1 special character, 1 uppercase letter"),
        pytest.param("Pass@w1", False,
                     id="Correct password must have at least 8 characters"),
        pytest.param("Pass@word11234572", False,
                     id="Correct password must have max 16 characters"),
        pytest.param("Password1", False,
                     id="Correct password must have at least 1 "
                        "special character"),
        pytest.param("pass@word1", False,
                     id="Correct password must have at least 1 "
                        "uppercase letter"),
        pytest.param("Pass@word", False,
                     id="Correct password must have at least 1 digit")
    ])
    def test_check_password_function(self,
                                     password: str,
                                     expected_result: bool) -> None:

        assert check_password(password) == expected_result
