import pytest
from typing import Any

from app.main import check_password


class TestCheckEdgeCases:
    @pytest.mark.parametrize(
        "pass_input",
        [
            pytest.param(
                "W1arr!o",
                id="checking too short password 7 symbol"
            ),
            pytest.param(
                "W1arr!or_of_the_L",
                id="checking too long password 17 symbol"
            ),
            pytest.param(
                "Waarr!or",
                id="checking password without number"
            ),
            pytest.param(
                "W1arrior",
                id="checking password without allowed special symbol"
            ),
            pytest.param(
                "w1arr!or",
                id="checking password without uppercase letter"
            ),
            pytest.param(
                "Воин_Св!ета1",
                id="checking password with cyrillic symbol"
            ),
            pytest.param(
                "Warr?i1or",
                id="checking password with forbidden special symbol"
            ),
        ]
    )
    def test_checking_edge_cases(self,
                                 pass_input: Any
                                 ) -> None:
        assert check_password(pass_input) is False

    def test_check_for_correct_password(self) -> None:
        assert check_password("Warr!i1or")
