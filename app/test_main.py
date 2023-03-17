import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param("Qwer1!", False, id="password is too short"),
        pytest.param("Qwertytuiopasgdjfk1!", False, id="password is too long"),
        pytest.param("Qwertyui!@", False, id="no digits"),
        pytest.param("Qwertyu123", False, id="no special character"),
        pytest.param("q12345678!@", False, id="no upper letter"),
    ]
)
def test_password_validity(
    password: str,
    result: bool
) -> None:
    assert (check_password(password) == result)
