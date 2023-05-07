import pytest

from app.main import check_password

test_data = [
    ("Pass@word1", True,),  # correct
    ("P@1", False,),  # too short
    ("Pass@word1Pass@word1", False,),  # too long
    ("Pass@word", False,),  # no digits
    ("pass@word1", False,),  # no uppercase letter
    ("Password12", False,),  # no special symbol
]


@pytest.mark.parametrize(
    "password,is_valid",
    test_data,
    ids=[
        "True when password is valid",
        "False when password is too short",
        "False when password is too long",
        "False when no digits",
        "False when no uppercase",
        "False when no special symbol '$@#&!-_'"
    ]
)
def test_check_password(password: str, is_valid: bool) -> None:
    result = check_password(password)
    assert result == is_valid
