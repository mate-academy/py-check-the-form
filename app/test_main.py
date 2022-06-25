import pytest
from app.main import check_password


@pytest.mark.parametrize("is_valid, result", [
                         pytest.param("Pass@word1", True,
                                      id="all requirements complete"),
                         pytest.param("qwerty", False,
                                      id="has no digit, special, short pass"),
                         pytest.param("Str@ng", False,
                                      id="has no digit, short password"),
                         pytest.param("qqqqqqqqqqqqqqqqqqqqqqqqqqqqq", False,
                                      id="too long password"),
                         pytest.param("вамик", False,
                                      id="non_latin_letter")]
                         )
def test_is_valid_password(is_valid, result):
    assert check_password(is_valid) == result
