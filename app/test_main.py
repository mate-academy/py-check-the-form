import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "input_password,audit_password",
    [
        ("Abcd123$", True),
        ("Test@Pass1", True),
        ("SecurePwd!7", True),
        ("password123$", False),
        ("AbcdEfgh@!", False),
        ("Invalid@Pass!", True),
        ("Ab12@C", False),
        ("TooLongPassword123$#", False)
    ]
)
def test_check_password(input_password: str, audit_password: bool) -> None:
    assert check_password(input_password) == audit_password
