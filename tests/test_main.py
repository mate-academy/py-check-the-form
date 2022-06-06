import pytest

from app.main import check_password


@pytest.mark.parametrize("password, result",
                         [
                             pytest.param(
                                 "",
                                 False,
                                 id="Have to be some password"
                             ),
                             pytest.param(
                                 "qwerty1",
                                 False,
                                 id="Have to be 8 symbols at least"
                             ),
                             pytest.param(
                                 "qwerty1_qwerty2_qwerty3",
                                 False,
                                 id="Have to be less than 16 symbols"
                             ),
                             pytest.param(
                                 "qwertyqwerty",
                                 False,
                                 id="Have to contain special symbols"
                             ),
                             pytest.param(
                                 "qwerty qwerty",
                                 False,
                                 id="Spaces are not allowed"
                             ),
                             pytest.param(
                                 "Qwerty_123",
                                 True,
                                 id="The strongest password ever!"
                             )
                         ]
                         )
def test_check_password(password, result):
    assert check_password(password) == result
