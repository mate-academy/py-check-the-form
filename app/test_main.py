import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("Pass@word1%", False),
    ],
)
def test_password_has_forbidden_symbols(
    test_input: str, expected: bool
) -> None:
    assert check_password(test_input) == all(
        ch.isalpha() or ch.isalnum() or ch in "$@#&!-_" for ch in test_input
    )


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("s123@12", False),
        ("Ds23@12", False),
        ("2", False),
    ],
)
def test_password_shoud_be_min_8_len(test_input: str, expected: bool) -> None:
    assert check_password(test_input) is expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("123454Pass@word18", False),
        ("123454Pass@word133222ff", False),
    ],
)
def test_password_max_16_len(test_input: str, expected: bool) -> None:
    assert check_password(test_input) is expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("Pass@wordfjj", False),
    ],
)
def test_password_contain_digit(test_input: str, expected: bool) -> None:
    assert check_password(test_input) is expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("passs@word1kk", False),
    ],
)
def test_password_contain_special(test_input: str, expected: bool) -> None:
    assert check_password(test_input) is expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("Pass33word1fs", False),
    ],
)
def test_password_contain_upper(test_input: str, expected: bool) -> None:
    assert check_password(test_input) is expected
