import pytest

from app.main import check_password


class TestLength:
    @pytest.mark.parametrize(
        "password,expected",
        [
            pytest.param("", False,id="empty password"),
            pytest.param("1Q@dach", False, id="shorter than allowed"),
            pytest.param("1Q@dachk", True, id="shortest characters allowed"),
            pytest.param("1Q@dachk1Q@dachk", True, id="longest characters allowed"),
            pytest.param("1Q@dachk-1Q@dachk", False, id="longer than allowed"),
        ]
    )
    def test_password_length(self, password, expected):
        assert check_password(password) == expected


class TestValidCharacters:
    @pytest.mark.parametrize(
        "password,expected",
        [
            pytest.param("af41$@#&!-_", False, id="no uppercase"),
            pytest.param("aBs$@#&!-_", False, id="no digit"),
            pytest.param("sdF43nD777", False, id="no special symbols"),
            pytest.param("Филин2$@#&!-_", True, id="cyrillic alphabet"),
        ]
    )
    def test_valid_password(self, password, expected):
        assert check_password(password) == expected
