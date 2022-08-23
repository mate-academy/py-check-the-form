from app.main import check_password


def test_length_7():
    assert check_password("1D2d3e!") is False


def test_length_8():
    assert check_password("1D2d3e!8")


def test_length_16():
    assert check_password("1D2d3e!81D2d3e!8")


def test_length_17():
    assert check_password("1D2d3e!81D2d3e!8l") is False


def test_all_lower():
    assert check_password("1d2d3e!8") is False


def test_no_number():
    assert check_password("dDdDeE!t") is False


def test_no_special_symbol():
    assert check_password("dDdDeE1t") is False
