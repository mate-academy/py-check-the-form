import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        pytest.param("", False,
                     id="Should return False for empty password"),
        pytest.param("Mate_m1", False,
                     id="Should return False for password len == 7"),
        pytest.param("Mate_ma1", True,
                     id="Should return True for password len == 8"),
        pytest.param("Mate_mate_1", True,
                     id="Should return True for normal password"),
        pytest.param("Mate_mate_mate_1", True,
                     id="Should return True for password len == 16"),
        pytest.param("Mate_mate_mate_m1", False,
                     id="Should return False for password len == 17"),
        pytest.param("Mate_mate_mate_mate_mate_mate1", False,
                     id="Should return False for long password"),
    ]
)
def test_password_length_must_be_upper_7_and_less_17(
    password,
    expected
):
    assert check_password(password) == expected


@pytest.mark.parametrize(
    "password,expected",
    [
        pytest.param("Mate_mat1*", False,
                     id="Should return False when non expected symbol '*'"),
        pytest.param("Mate_мейт1", True,
                     id="Should return False when non latin symbol"),
        # must be False
        pytest.param("Mate,ma1e", False,
                     id="Should return False when non expected symbol ','"),
        pytest.param("M$@#&!-_1", True,
                     id="Should return True when expected symbol"),
    ]
)
def test_special_symbol_in_password(
    password,
    expected,
):
    assert check_password(password) == expected


@pytest.mark.parametrize(
    "password,expected",
    [
        pytest.param("mate_mat1", False,
                     id="Password must contains uppercase"),
        pytest.param("Mate123456", False,
                     id="Password must contains symbol "),
        pytest.param("1234_5678", False,
                     id="Password must contains letter"),
        pytest.param("Mate_mate_1", True,
                     id="Normal password should return True")
    ]
)
def test_password_should_have_1_digit_special_uppercase(
    password,
    expected,
):
    assert check_password(password) == expected
