import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("Pass@word1", True),
        ("pass@word1", False),
        ("Password1", False),
        ("Password!", False),
        ("To_Long@Password1234567890", False),
        ("@Pass12", False)


    ],
    ids=[
        "correct password",
        "without uppercase letter",
        "without special chars",
        "without digits",
        "to long password",
        "for short password"
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    result = check_password(password)
    assert result == expected_result, f"Test failed for password: {password}"
