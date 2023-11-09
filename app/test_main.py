import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("Pass@word", False),
        ("pass@word1", False),
        ("Password1", False),
        ("Pass$word1", True),
        ("Pa@w1", False),
        ("Pass#word1", True),
        ("Pass&word1", True),
        ("Pass@word1", True),
        ("Pass!word1", True),
        ("Pass!wortfrthhrhrd1", False),
        ("Pass-word1", True),
        ("Pass_word1", True)
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
