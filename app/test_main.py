import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("Vlad@Pass12", True),
        ("VeryVery@LongPass123", False),
        ("123Ds_", False),
        ("╜Letters1", False),
        ("withou@tup12", False),
        ("without@Num", False),
        ("WithoutSp1", False),

    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
