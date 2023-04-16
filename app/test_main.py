import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "string,result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Pass@word1Pass@word1", False),
        ("Pass%wrd1", False),
        ("Pass*word1", False),
        ("Pass(@)word1", False),
        ("Pass+word1", False)
    ]
)
def test_check_password_is_valid(string: str, result: bool) -> None:
    assert check_password(string) == result
