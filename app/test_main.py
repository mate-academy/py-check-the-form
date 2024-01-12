import pytest
from app.main import check_password


@pytest.mark.parametrize("password, expected_result", [
    ("Pass@word1", True),
    ("qwerty", False),
    ("Str@ng", False),
    ("Password123", False),
    ("pass@word1", False),
    ("TooLongPassword123456", False),
    ("MaxLenPass@word1", True),
    ("ExceedMaxLenPass@word1", False),
    ("RestrictedChar$1", True),
    ("Custom@SpecialChar1", False),
])
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result
