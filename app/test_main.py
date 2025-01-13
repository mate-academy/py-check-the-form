from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password, result", [
        ("Pass@word1", True),
        ("Qwerty#", False),
        ("s1r@ng", False),
        ("F_1dffgghhjjkkklllllllllllll#", False),
        ("ff", False),
        ("Password123", False),
        ("P@ssw0rd", True),
        ("P@ssword_okkkkkkkkkkkk_#1", False),
        ("1", False)

    ],
    ids=[
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9"
            ]


)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result, f"{password} is {result}"


