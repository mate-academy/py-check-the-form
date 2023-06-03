import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param("Abcqwqq_q", False,
                     id="Should returns False for passwords without digits"),
        pytest.param("Abcqwqq_qqweqweqwewqeweqwe1weqwe", False,
                     id="Should returns False for  too long passwords"),
        pytest.param("Abcqwqqmq1", False,
                     id="Should return False for"
                        " passwords without special symbols"),
        pytest.param("abcqwqq_q1", False,
                     id="Should return False for"
                        " passwords without uppercase letter"),
        pytest.param("Ab_1", False,
                     id="Should return False for short passwords"),
    ]
)
def test_check_password(
        password: str,
        result: bool
) -> None:
    assert check_password(password) == result
