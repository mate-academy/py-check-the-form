from app.main import check_password


def test_symbols():
    assert check_password('фешсэзмо') == False


def test_length():
    assert check_password('abc') == False


def test_max_length():
    assert check_password('abc1234567891234567') == False


def test_not_symbols():
    assert check_password('asdfgh1@') == False
