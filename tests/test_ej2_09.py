import pytest
from src.ej2_09 import preguntarEdad

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (1, "Gratis"),
        (18, "10$"),
        (100, "10$"),
        (5, "5$"),
        (17, "5$"),
        (125, "10$")
    ]
)
def test_precioEntradas_params(input_n, expected):
    assert preguntarEdad(input_n) == expected
