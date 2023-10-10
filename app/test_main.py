import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "input_pass, expected_result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("1Qwer@tyui", True),
        ("1Qwertyui$9023g", True),
        ("1wertyui$9023g", False),
        ("1Qwertyui$9023gwq1", False),
        ("Qwer@tyui$g", False),
        ("1Qwe$", False),
        ("1Qwertyui923g", False)
    ]
)
def test_check_password(input_pass: str, expected_result: bool) -> None:
    assert check_password(input_pass) == expected_result
