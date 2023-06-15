import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("Pass@word1", True),
        ("VeryStr0ngP@ss", True),
        ("Str0ng$gg", True),
        ("PASSWORD!11", True),
        ("VeryStr0ngP@ss" * 3, False),
        ("Sa1$", False),
        ("q1@aaaaa", False),
        ("Str@ngqqqq", False),
        ("PASSWiRD11", False),

    ],
    ids=[
        "Result should equal True if password meets all requirements",
        "Result should equal True if password meets all requirements",
        "Result should equal True if password meets all requirements",
        "Result should equal True if password meets all requirements",
        "Result should equal False if password is too long (>16 chars)",
        "Result should equal False if password is too short (<8 chars)",
        "Result should equal False if password no uppercase in it",
        "Result should equal False if password no digits in it",
        "Result should equal False if password no special characters in it",
    ]
)
def test_valid_password(password: str, result: bool) -> None:
    assert check_password(password) == result
