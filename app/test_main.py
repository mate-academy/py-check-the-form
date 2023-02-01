import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("short", False),
        ("too_loooooooooong", False),
        ("nosymbols", False),
        ("no_uppercase", False),
        ("no_digits", False),
    ]
)
def test_check_password_result(
        password: str,
        result: bool
) -> None:
    assert check_password(password) == result
