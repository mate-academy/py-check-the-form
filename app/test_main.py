import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,answer",
    [
        ("Pass@word1", True),
        ("pass@word1", False),
        ("P@w1", False),
        ("Pass@word", False),
        ("Pass@word1wordwordword", False),
        ("Password1", False),

    ]
)
def test_check_password(password: str, answer: bool) -> None:
    assert check_password(password) == answer
