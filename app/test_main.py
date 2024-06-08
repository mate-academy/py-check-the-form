from app.main import check_password
import pytest

@pytest.mark.parametrize(
        "password,result",
        [
            ("short", False),
            ("longlonglonglonglonglong", False),
            ("Pass@word1", True),
            ("ауршщыаы", False),
            ("password1", False),
            ("12345678!", False),
            ("Aa1!bbbb", True),
            ("Aa1!bbbbcccccddd", True)
        ]
)
def test_check_password(password, result) -> None:
    assert check_password(password) == result
