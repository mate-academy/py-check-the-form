import pytest


from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@rodk1", True),
        ("password", False),
        ("Str@ng", False),
        ("Str@dng2", True),
        ("qwerty", False),
        ("onlylette!rs@oftheLati!n@alphabet", False),
        ("onetrue42!@GDfd4", True),
        ("PassWithoutDigit", False),
        ("ACB1@avs", True),
        ("NoSpecialChar", False),
        ("@42PaGecG!2", True),
        ("Valid1Pas sword@", False),
        ("Pass@word1$", True),
        ("hasnolow@1er", False),
    ],
)
def test_check_password(password: str, expected: bool) -> bool:
    assert check_password(password) == expected
