import pytest


from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@rodk1", True),
        ("password", False),
        ("Str@ng", False),
        ("qwerty", False),
        ("onlylette!rs@oftheLati!n@alphabet", False),
        ("PassWithoutDigit", False),
        ("NoSpecialChar", False),
        ("@42PaGecG!2", True),
    ],
)
def test_check_password(password: str, expected: bool) -> bool:
    assert check_password(password) == expected
