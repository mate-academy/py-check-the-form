import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,is_valid_password",
    [
        pytest.param(
            "on3love-Python", True,
            id="test should return True when password is valid"
        ),
        pytest.param(
            "1@2$3#4&5!-", False,
            id="test should return False when password doesn't"
               "contains Latin letters"
        ),
        pytest.param(
            "#xcvBnm#", False,
            id="test should return False when password doesn't"
               "contains at least 1 digit"
        ),
        pytest.param(
            "1q2w3E4r5t", False,
            id="test should return False when password doesn't"
               "contains at least 1 special character ($@#&!-_)"
        ),
        pytest.param(
            "qw3rTy!", False,
            id="test should return False when len(password) < 8"
        ),
        pytest.param(
            "pD_1oaUvKW1C!pf77y9&", False,
            id="test should return False when len(password) > 16"
        )
    ]
)
def test_check_password(password: str, is_valid_password: bool) -> None:
    assert check_password(password) == is_valid_password
