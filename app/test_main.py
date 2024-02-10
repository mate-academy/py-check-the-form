import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("LongerPassword123!", False),
        ("Short1!", False),
        ("NoSpecialChar123", False),
        ("NoDigit&Special", False),
        ("OnlyLowercaseletters", False),
        ("OnlyUppercaseletters", False),
        ("OnlySpecialCharacters@", False),
        ("OnlyDigits123456", False),
        ("Valid@Passw0rd", True),
        ("AnotherValidPassw0rd", False),
        ("AValidPasswordWith$ymbols!", False),
        ("Sh0rt!", False),
        ("Toolongpasswordwithmorethan16characters", False),
        ("приветпароль", True),
        ("qwertyuiop", False),

    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result
