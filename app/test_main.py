import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "checked_password,expected_result",
    [
        ("Valid123$", True),
        ("Test@Password9", True),
        ("Secure1@Password", True),
        ("MyPass_2024", True),
        ("Hello_World1", True)
    ]
)
def test_for_true_passwords(
        checked_password: str,
        expected_result: bool
) -> None:
    assert check_password(checked_password) == expected_result


@pytest.mark.parametrize(
    "checked_password,expected_result",
    [
        ("short", False),
        ("longpasswordwithnospecialcharacter1", False),
        ("12345678", False),
        ("validpassword$buttoolong123", False),
        ("noUppercase1$", False)
    ]
)
def test_for_false_passwords(
        checked_password: str,
        expected_result: bool
) -> None:
    assert check_password(checked_password) == expected_result
