import pytest
from app.main import check_password


@pytest.mark.parametrize(
    'password, answer',
    [
        pytest.param(
            'notapasswordatallhonestly',
            False,
            id="Too long password"
        ),
        pytest.param(
            'pwd',
            False,
            id="Too short password"
        ),
        pytest.param(
            'NoSpecSymb',
            False,
            id="No special symbol"
        ),
        pytest.param(
            "8Symbol!",
            True,
            id="Exactly 8 symbols"
        ),
        pytest.param(
            "16Symbols!!!!!!",
            True,
            id="Exactly 16 symbols"
        )
    ]
)
def test_check_password(password, answer):
    assert check_password(password) == answer
