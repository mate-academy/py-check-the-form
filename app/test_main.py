import pytest
from app.main import check_password


@pytest.mark.parametrize("password, expected_result", [
    pytest.param(
        "12345567",
        False,
        id="contains at least 1 capital letter"
    ),
    pytest.param(
        "12Qazzzz",
        False,
        id="contains at least 1 special character"
    ),
    pytest.param(
        "asdlOKWDA",
        False,
        id="contains at least 1 digit"
    ),
    pytest.param(
        "12345jpeg",
        False,
        id="contains at 1 special character"
    ),
    pytest.param(
        "12eh",
        False,
        id="contains at 1 special character"
    ),
    pytest.param(
        "",
        False,
        id="password is empty string"
    ),
    pytest.param(
        "08041982Plm$",
        True
    ),
    pytest.param(
        "34564848Plm&",
        True
    ),
    pytest.param(
        "6698546As#d",
        True
    ),
    pytest.param(
        "Tuy374837$ghirt11",
        False,
        id="too-long password"
    )
])
def test_should_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result
