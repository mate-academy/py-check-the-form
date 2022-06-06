import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        pytest.param("12345", False, id="password is too short"),
        pytest.param("Itis@very1ongpassword", False, id="password is too long"),
        pytest.param("noupperc@se1", False, id="password do not contain uppercase letter"),
        pytest.param("NoNumInP@ssword", False, id="password do not contain digits"),
        pytest.param("NoSpecia1InPassword", False, id="password do not contain special characters"),
        pytest.param("NoNumInP@ssword", False, id="password do not contain digits"),
        pytest.param("P@ssword123", True, id="valid password")
    ]
)
def test_check_password(password, result):
    assert check_password(password) == result
