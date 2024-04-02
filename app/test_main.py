import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "new_input,expected_output",
    [
        (
            "Pass@word1", True
        ),
        (
            "qwertynice", False
        ),
        (
            "Str@ng", False
        ),
        (
            "hellotoolongpassword@1", False
        ),
        (
            "Hellospecial", False
        ),
        (
            "he11o@234", False
        ),
        (
            "Aaaaa@1", False
        ),
        (
            "Hello@one", False
        )
    ]
)
def test_valid_password(new_input: str, expected_output: bool) -> None:
    assert check_password(new_input) is expected_output
