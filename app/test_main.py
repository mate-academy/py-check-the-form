import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    (
        ("qr", False),
        ("qretqrtqetq@", False),
        ("qretqrtqetqrqwerqwerqwerqwerqerq", False),
        ("qretqrtqetq123@", False),
        ("Qretqrtqetq123@", True),
    )
)
def test_pasword(password: str, result: bool) -> None:
    assert check_password(password) is result
