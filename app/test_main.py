import pytest


from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [("Pass@word1", True),
        ("qwerty@1", False),
        ("Str@ng", False),
        ("Pass@word1Pass@word1", False),
        ("Pas@1", False),
        ("Qwerty-qwerty@", False),
        ("Qwerty_qwerty1", False), ]
)
def test_password(password: str, result: bool) -> None:
    assert check_password(password) == result
