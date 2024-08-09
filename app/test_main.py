from app.main import check_password


def test_check_password() -> None:
    assert check_password("Pass@word1") is True
    assert check_password("Pass@word1&word2") is True
    assert check_password("Pa@word1") is True
    assert check_password("P@word1") is False
    assert check_password("Pass@word1&word21") is False
    assert check_password("p@word1") is False
    assert check_password("Password1") is False
    assert check_password("Pass@word") is False
    assert check_password("password") is False
