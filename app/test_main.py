import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,is_secure",
    [
        (
            "Aa1!",
            False
        ),
        (
            "Aa1!afsdladssafkaasdfadadsfdafsfasdfdasfadsffadsfadsfaddfadsfa",
            False
        ),
        (
            "Aafadfa!!!!",
            False
        ),
        (
            "asfda123!",
            False
        ),
        (
            "asdASdad123",
            False
        )
    ]
)
def test_password_checker(
        password: str,
        is_secure: bool
) -> None:
    assert check_password(password) == is_secure
