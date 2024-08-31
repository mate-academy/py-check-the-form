import pytest


from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        pytest.param("Pa$$word1ы", False, id="invalid character"),
        pytest.param("Pa$1", False, id="less than eight characters"),
        pytest.param("Pa$$wordPa$$word1",
                     False,
                     id="more than eighteen characters"),
        pytest.param("Pa$$wordP", False, id="missing digit"),
        pytest.param("Password1", False, id="missing a special symbol"),
        pytest.param("pa$$word1", False, id="missing a capital letter"),
        pytest.param("Pa$$word1", True, id="valid password")
    ]
)
def test_validity_of_different_passwords(password: str,
                                         result: bool) -> None:
    assert check_password(password) == result
