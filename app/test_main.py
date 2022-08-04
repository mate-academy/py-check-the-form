from app.check_password import check_password


def test_required_length_of_password():
    password_ = check_password("Victory1!")
    assert password_ is True


def test_uppercase_letter_in_password():
    password_ = check_password("korsica1!")
    assert password_ is False


def test_special_character_in_password():
    password_ = check_password("World1245@")
    assert password_ is True


def test_digits_in_password():
    password_ = check_password("World@@@@")
    assert password_ is False
