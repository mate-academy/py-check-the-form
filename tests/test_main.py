import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param(
            "Pass@word1",
            True
        ),
        pytest.param(
            "qwerty",
            False
        ),
        pytest.param(
            "Str@ng",
            False
        ),
        pytest.param(
            "qwerty#",
            False
        ),
        pytest.param(
            "Pass@word12131234",
            False
        ),
        pytest.param(
            "Pass@wordqweryhgf",
            False
        ),
        pytest.param(
            "Pass@word1213123",
            True
        ),
    ]
)
def test_check_password(password, result):
    assert check_password(password) == result

