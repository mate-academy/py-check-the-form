import pytest
from app.main import check_password

@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param("qwerty", False),
        pytest.param("qwertyuiopasdfghj", False),
        pytest.param("слава Україні", False),
        pytest.param("Geroyamslava@", False),
        pytest.param("S1mpleIsGO@T", True),
        pytest.param("Pass@word1", True)
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
