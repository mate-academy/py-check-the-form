import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("kaka", False),
        ("CoolPass!@", False),
        ("1!A", False),
        ("Bibi46as", False),
        ("Cookies!2", True),
        ("CocoJambo12!HeroAhfjad", False),
        ("Password%^$", False),
        ("passwordstrong!2", False),
    ],
    ids=[
        "test 1: should return False",
        "test 2: should return False",
        "test 3: should return False",
        "test 4: should return True",
        "test 5: should return False",
        "test 6: should return False",
        "test 7: should return False",
        "test 8: should return False"
    ]
)
def test_check_password(
        password: str,
        result: bool
) -> None:
    assert (
        check_password(password) == result
    )
