import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "new_input,expected_output",
    [
        pytest.param("Pass@word1", True),
        pytest.param("qwerty", False),
        pytest.param("Str@ng", False),
        pytest.param("Pass@word", False),
        pytest.param("Pass@1", False),
        pytest.param("Password1", False),
        pytest.param("pass@word1", False),
        pytest.param("Pass@word1dfjsldfjlaskjdflsasdl", False)
    ]
)
def test_valid_password(new_input: str, expected_output: bool) -> None:
    assert check_password(new_input) is expected_output
