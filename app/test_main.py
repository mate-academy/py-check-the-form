import pytest
from app.main import check_password


@pytest.mark.parametrize("password, expected", [
    ("Pass@word1", True),
    ("Abcdefg1$", True),
    ("P@ssw0rdA", True),
    ("S3cr3t-$", True),
    ("", False),
    ("1234567", False),
    ("Abcdefghijklmnopqrstuvwxyz", False),
    ("noSpecial123", False),
    ("OnlyLowerCase", False),
    ("onlyuppercase", False),
    ("12345678", False),
    ("nopassword", False),
    ("qwerty", False),
    ("Str@ng", False)
])
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected


if __name__ == "__main__":
    pytest.main()
