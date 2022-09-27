import pytest

from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "password,expected",
        [
            ("Pass@word1", True),
            ("qwerty", False),
            ("Str@ng", False),
            ("123_123_asd_asd_asd", False),
            ("Password12", False),
            ("_123454321_", False),
            ("Good_password", False),
            ("Should_be_@_good_password_mayb3", False),
            ("Aa1_", False),
        ]
    )
    def test_get_valid_password(
            self,
            password,
            expected
    ):
        assert check_password(password) is expected
