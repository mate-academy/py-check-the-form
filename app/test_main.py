from app.main import check_password
import pytest


class TestCheckPassValidClass:
    @pytest.mark.parametrize(
        "password,result",
        [
            ("Pass@word1", True),
            ("qwerty", False),
            ("Str@ng", False),
            ("symbolisation", False),
            ("ewqwjkenqwjenqnwekjqnwkejnqwekjqwnej", False),
            ("Pass@", False),
        ],
    )
    def test_check_password_is_valid(self, password: str, result: bool) -> None:
        assert check_password(password) == result
