import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("Pass@word1", True),
        ("VeryStr0ngP@ss", True),
        ("Str0ng$gg", True),
        ("a" * 20, False),
        ("Sa1$", False),
        ("qwerty", False),
        ("Str@ng", False),
        ("PASSWORD", False),
        ("12345678", False),
        ("$@#&!-_", False),

    ],
    ids=[
        "Result should equal True if password meets all requirements",
        "Result should equal True if password meets all requirements",
        "Result should equal True if password meets all requirements",
        "Result should equal False if password is too long (>16 chars)",
        "Result should equal False if password is too short (<8 chars)",
        "Result should equal False if password is lowercase only",
        "Result should equal False if password not contain digits",
        "Result should equal False if password is uppercase only",
        "Result should equal False if password is digits only",
        "Result should equal False if password is special characters only",
    ]
)
def test_valid_password(password: str, result: bool) -> None:
    assert check_password(password) == result
