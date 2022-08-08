from app.main import check_password


def test_required_small_length_of_password():
    password_ = check_password("Vico1@!")
    assert password_ is False


def test_required_big_length_of_password():
    password_ = check_password("victoriystarmamory")
    assert password_ is False


def test_uppercase_letter_in_password():
    password_ = check_password("corsica1!")
    assert password_ is False


def test_special_character_in_password():
    password_ = check_password("World1245")
    assert password_ is False


def test_digits_in_password():
    password_ = check_password("World@@@@")
    assert password_ is False


def test_excessive_in_password():
    password_ = check_password("World@@@^")
    assert password_ is False