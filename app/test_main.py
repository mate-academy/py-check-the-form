from app.main import check_password


def test_when_everything_is_ok():
    pswrd = check_password('Pass@word1')
    assert pswrd is True


def test_when_length_is_below_eight():
    pswrd = check_password('Ps@wo1')
    assert pswrd is False


def test_when_length_is_upon_sixteen():
    pswrd = check_password('Pass@word1shouldbeOK')
    assert pswrd is False


def test_when_no_uppercase():
    pswrd = check_password('pass@word1')
    assert pswrd is False


def test_when_no_digits():
    pswrd = check_password('Pass@word')
    assert pswrd is False
