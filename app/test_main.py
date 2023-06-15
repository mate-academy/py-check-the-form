import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("PASSWORD", False),
        ("12345678", False),
        ("$@#&!-_", False),
        ("a" * 150, False),
        ("aaa", False),

    ],
    ids=[
        "Result should equal True if password is Pass@word1",
        "Result should equal False if password is lowercase only",
        "Result should equal False if password not contain digits",
        "Result should equal False if password is uppercase only",
        "Result should equal False if password is digits only",
        "Result should equal False if password is special characters only",
        "Result should equal False if password is too long (>16 chars)",
        "Result should equal False if password is too short (<8 chars)",
    ]
)
def test_should_correctly_convert_years(password: str,
                                        result: bool) -> None:
    assert check_password(password) == result
