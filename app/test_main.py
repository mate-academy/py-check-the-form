import pytest
from .main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("passqweword", False),
        ("qwerty", False),
        ("Str@ng", False),
        ("Pass@!word2", False),
        ("Pass@word1Pass@word1", False),
        ("", False),
    ]
)
def test_should_check_password(
        password: str,
        result: bool
) -> None:
    assert check_password(password) is result
