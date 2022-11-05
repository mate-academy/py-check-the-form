from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password,result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("123456789", False),
        ("Ilove@mylittle12", True),
        ("Wan@3", False),
        ("Hfyrwwwdd12@fjgnsdh", False),
        ("opo1", False),
        ("orto@23part", False),
        ("Wartono@par", False),
        ("Wor9pukalol", False)
    ]
)
def test_check_password(password: str,
                        result: bool) -> None:

    assert check_password(password) == result
