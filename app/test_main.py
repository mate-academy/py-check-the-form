from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("MateAc@damy1", True),
        ("Python", False),
        ((5, 2), ValueError),
        ([], ValueError)

    ]
)
def test_check_password(
        password: str, 
        expected: bool
) -> None:
    if isinstance(expected, bool):
        assert check_password(password) == expected
    else:
        with pytest.raises(expected):
            check_password(password)


if __name__ == "__main__":
    pytest.main()
