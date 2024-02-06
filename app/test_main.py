import pytest

from app.main import check_password


@pytest.mark.parametrize(
    ("password", "validation"),
    [
        ("Pass@word1", True),
        ("P1@erty", False),
        ("Qwerty@long", False),
        ("12@password", False),
        ("Str@ng", False),
        ("@12Verylongpasswordtome", False)
    ]
)
def test_check_password(
        password: str,
        validation: bool
) -> None:
    assert check_password(password) == validation
