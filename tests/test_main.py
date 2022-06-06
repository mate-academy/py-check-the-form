import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        pytest.param("1aA!567", False,
                     id="password has at least 8 characters"),
        pytest.param("1aA!5678901234567", False,
                     id="password has maximum 16 characters"),
        pytest.param("abcdefJ!", False,
                     id="password must contain digits"),
        pytest.param("abcdef!7", False,
                     id="password must contain uppercase letters"),
        pytest.param("abcdefJ7", False,
                     id="password must contain special characters"),
        pytest.param("ab cdef!J7/%", False,
                     id="only $@#&!-_ allowed in password"),
        pytest.param("abcdef!J7", True,
                     id="password is correct")
    ]
)
def test_check_password(password, result):
    assert check_password(password) == result
