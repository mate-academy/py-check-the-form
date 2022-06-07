import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param("Pass@word1", True, id="valid password"),
        pytest.param("qwerty", False, id="incorrect password"),
        pytest.param("Pafffffffffffffffffss", False, id="incorrect password"),
        pytest.param("Str@ng", False, id="incorrect password"),
    ]
)

def test_check_paswsord(
        password,
        result
):
    assert check_password(password) == result