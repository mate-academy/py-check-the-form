import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("fT34hgeemw", False),
        ("werqwet8#tr", False),
        ("Tuyjf#jfwen", False),
        ("Tiegj7iensw#nfwoeng", False),
        ("T4#f", False)
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
