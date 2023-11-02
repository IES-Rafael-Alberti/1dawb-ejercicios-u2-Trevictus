import pytest
from src.ej2_07 import rentaAnual

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (9999, "5%"),
        (8921, "5%"),
        (10000, "15%"),
        (19999, "15%"),
        (21345, "20%"),
        (34700, "20%"),
        (40000, "30%"),
        (40999, "30%"),
        (61000, "45%"),
    ]
)
def test_tipoImpositivo_params(input_n, expected):
    assert rentaAnual(input_n) == expected