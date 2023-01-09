import pytest

from app.main import check_password


@pytest.mark.parametrize("password, result",
                         [
                             ("Pkfjenufhrevhsurkzlwjgrd", False),
                             ("kdj", False),
                             ("Passw@ord", False),
                             ("jdurn&j1uf", False),
                             ("Hks22vjdkw", False),
                             ("Rmcjd&jf12i", True)
                         ])
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
