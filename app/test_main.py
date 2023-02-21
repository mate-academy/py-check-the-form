from app.main import check_password


def test_length_lower() -> None:
    assert check_password("J56&") is False


def test_length_upper() -> None:
    assert check_password("J56&hdajhasdhgjahsgdjh") is False


def test_has_upper() -> None:
    assert check_password("t40@rere") is False


def test_has_digit() -> None:
    assert check_password("Yt$UiUiU") is False


def test_has_special() -> None:
    assert check_password("567YtuYu") is False


def test_has_all_requirements() -> None:
    assert check_password("$HeyYou56") is True
