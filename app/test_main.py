import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    (
        ("qqqqQ1$∞", False),
        ("Qq1#", False),
        ("Qq1#rfdsjJdf345lsfkjfieiei5kdsa88-", False),
        ("-Ddddddddd", False),
        ("1Ddddddddd", False),
        ("-1dddddddd", False),
        ("dddddddddd", False),
    )
)
def test_pasword(password: str, result: bool) -> None:
    assert check_password(password) is result
