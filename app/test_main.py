import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param(
            "Pass@word1", True,
            id="all right parts in password"
        ),
        pytest.param(
            "Ps@wd1", False,
            id="incorrect password if len of element less eight"
        ),
        pytest.param(
            "Pass@word1_Pass@word1", False,
            id="incorrect password if len of element more sixteen"
        ),
        pytest.param(
            "pass@word1", False,
            id="incorrect password if without upper letter condition"
        ),
        pytest.param(
            "Pass@worda", False,
            id="incorrect password if without digit condition"
        ),
        pytest.param(
            "Password1", False,
            id="incorrect password if without special symbols"
        ),
    ]
)
def test_logic_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
