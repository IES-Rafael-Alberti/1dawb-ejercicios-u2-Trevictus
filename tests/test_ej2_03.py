import pytest
from src.ej2_03 import divisionNumeros

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        (1, 0, "ERROR"),
        (18, 9, str(18.0/9.0)),
        (100, 2, "50.0"),
        (5, 0, "ERROR"),
        (17, 0, "ERROR"),
        (125, 5, str(25.0))
    ]
)
def test_divisionNumeros_params(input_n1, input_n2, expected):
    assert divisionNumeros(input_n1, input_n2) == expected
