import pytest
from src.ej2_08 import obtenerNivel

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (0.0, "Inaceptable"),
        (0.2, "ERROR"),
        (0.4, "Aceptable"),
        (0.9, "Meritorio"),
        (0.6, "Meritorio"),
        (0.5, "ERROR"),
        (0.1, "ERROR"),
    ]
)
def test_calculaMeritos_params(input_n, expected):
    assert obtenerNivel(input_n) == expected