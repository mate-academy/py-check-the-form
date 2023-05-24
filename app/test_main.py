import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("12Az!", False),
        ("22254687alghabgaAb!@", False),
        ("фпвнBё1235$", False),
        ("dnlayd8!", False),
        ("dnflndyRs@", False),
        ("fakjfD374", False),
        ("Pass@word1", True)
    ],
    ids=[
        "test should return False if password to short",
        "test should return False if password to long",
        "test should return False if password has letter not from Aa-Zz",
        "test should return False if password has no letter in uppercase",
        "test should return False if password has no digits",
        "test should return False if password has no special character",
        ("test should return True if password has "
         "at least 1 digit, 1 special character, 1 uppercase letter")
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
