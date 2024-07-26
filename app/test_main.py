import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password",
    [
        "",
        "1234567",
        "12345678901234567"
    ],
    ids=[
        "Password can't be empty line",
        "Too short password",
        "Too long password"
    ]
)
def test_should_return_false_if_len_of_password_is_incorrect(
        password: str,
) -> None:
    assert check_password(password) is False, (
        "Check password for length"
    )


@pytest.mark.parametrize(
    "password",
    [
        "ABCSD_FGHJKL1",
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
        "incorrect password",
        "only upper letters",
        "only lower letters",
        "only symbols",
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
    assert check_password(password) is False, (
        "Check password for upper letter, digit and special letter"
    )
