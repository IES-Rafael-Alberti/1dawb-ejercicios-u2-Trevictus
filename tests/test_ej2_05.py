import pytest
from src.ej2_05 import tributacion

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        (1, 50, False),
        (18, 1000, True),
        (100, 4000, True),
        (5,3000, False),
        (17, 980, False),
        (125,1001, True)
    ]
)
def test_mayoriaDeTributacion_params(input_n1, input_n2, expected):
    assert tributacion(input_n1, input_n2) == expected

