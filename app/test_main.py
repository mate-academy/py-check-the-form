from app.main import check_password


def test_required_bool():
    assert isinstance(check_password("Victory"), bool)


def test_required_min_length_of_password():
    assert check_password("") is False


def test_required_max_length_of_password():
    assert check_password("victory!123starmamory") is False


def test_required_letter_in_password():
    assert check_password("12345!!!") is False


def test_uppercase_letter_in_password():
    assert check_password("Corsica1!") is True


def test_check_special_simbols_in_password():
    assert check_password("World1245") is False


def test_check_digits_in_password():
    assert check_password("World@@@@7") is True


def test_check_excessive_in_password():
    assert check_password("World@@@^") is False
