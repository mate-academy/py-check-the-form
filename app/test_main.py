import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "expected_password,expected_result",
    [
        ("1234567", False),
        ("paasswordPassw@r1", False),
        ("Pass@word1", True),
        ("Str0nggg", False),
        ("aaaaaaa1&", False)
    ]
)
def test_check_password(expected_password, expected_result) -> None:
    assert check_password(expected_password) == expected_result
