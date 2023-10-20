import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Mypassword_12356", True),
        ("My@pas09", True),
        ("Mypassword#345678", False),
        ("My-pas2", False),
        ("Pas!ы1sword", False),
        ("my_password23", False),
        ("my%password67", False),
        ("my_password", False),
        ("my1password", False)
    ],
    ids=[
        "valid password with max length",
        "valid password with min length",
        "password with more than 16 characters",
        "password with less than 8 characters",
        "password with invalid letters",
        "password should contains uppercase letters",
        "password contains invalid special character",
        "password should contain digits",
        "password should contain special character"
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
