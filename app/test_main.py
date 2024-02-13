import pytest

from app.main import check_password


@pytest.mark.parametrize(
    ("passwd", "confirmation"),
    [
        ("P4$$w0rD", True),
        ("Password123!", True),
        ("Qw3rt!", False),
        ("4w3S0m3P4$$w0rD", True),
        ("4w3S0m3P4$$w0rD%^&", False),
        ("P4$$w0rd%^*", False),
        ("Пароль!23", False),
    ]
)
def test_check_password(
        passwd: str,
        confirmation: bool
) -> None:
    assert check_password(passwd) == confirmation
