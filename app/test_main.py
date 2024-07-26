import pytest

from app.main import check_password


def test_should_return_false_if_len_of_password_is_incorrect(
        password: str,
) -> None:
    assert check_password("") == False
    assert check_password("1234567") == False
    assert check_password("12345678901234567") == False


@pytest.mark.parametrize(
    "password",
    [
        "asdfghjkl",
        "abcdEFG1",
        "$@#&!-_$@#&!-_",
        "1234567890",
        "12345$@#&!-_",
        "asdfg$@#&!-_",
        "asdfg1234567",
        "чомуНеДержавною",
    ],
    ids=[
        "only upper letters",
        "only lower letters",
        "only symbols",
        "only not correct symbols"
        "only numbers",
        "numbers with symbols",
        "letters with symbols",
        "letters with numbers",
        "not Latin alphabet"
    ]
)
def test_should_return_false_if_password_is_incorrect(
        password: str,
) -> None:
    assert check_password(password) == False, (
        "Check password for upper letter, digit and special letter"
    )
