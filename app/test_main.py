import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("Pass@word1", True),
        ("qwerty1", False),
        ("Str@ng", False),
        ("Strong@pass", False),
        ("str0ng@pass", False),
        ("TooLongPasswordWithMoreThan16s", False),
        ("Str#ng@pass", False),
        ("", False)
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result
