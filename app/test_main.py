import pytest
from typing import Any
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("МійПароль1234", False),
        ("s12_P", False),
        ("ThisPswdIs_Ok123", True),
        ("pASSwordStrong123asHell!!!", False),
        ("pa55word_oknotok", False),
        ("Password_OK!", False),
        ("Password12OK", False),
        ("", False),
        (["Pass", "Word"], False),
    ],
    ids=[
        "Non-latin.",
        "Password < 6 letters.",
        "Password OK, matching all requirements.",
        "Password > 16 letters.",
        "Password without uppercase.",
        "Password without digit.",
        "Password without special character",
        "Empty password",
        "Password is not string"

    ]
)
def test_check_password(
        password: Any,
        expected_result: bool
) -> None:
    assert check_password(password) == expected_result
