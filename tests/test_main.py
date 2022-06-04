import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("", False),
        ("Hello_1", False),
        ("Hello_w1", True),
        ("Hello_world_1", True),
        ("Hello_world_1234", True),
        ("Hello_world_12345", False),
        ("Hello_world_world_12345", False),
    ]
)
def test_length_of_password(password, expected):
    assert check_password(password) == expected, \
        f"function should return {expected} if length of password is {len(password)}"


@pytest.mark.parametrize(
    "password, symbol, expected",
    [
        #  ("Hello_world_1", "а", False),
        ("Hello_world_1", "*", False),
        ("Hello_world_1", ".", False),
        ("Hello_world_1", ",", False)
    ]
)
def test_for_allowed_symbols(password, symbol, expected):
    assert check_password(password + symbol) == expected, \
        f'function should return False when password has "{symbol}"'


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param(
            "hello_world_1",
            False,
            id="Func should check for upper case including"
        ),
        pytest.param(
            "Hello_world_",
            False,
            id="Func should check for digit including"
        ),
        pytest.param(
            "Helloworld123",
            False,
            id="Func should check for special symbol including"
        ),
    ]
)
def test_for_including_all_necessary_symbols(password, expected):
    assert check_password(password) == expected
