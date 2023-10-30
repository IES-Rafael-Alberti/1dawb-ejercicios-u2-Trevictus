import pytest
from src.ej2_06 import pedirNombre

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        ("A", "M", "A"),
        ("M", "M","B"),
        ("V", "H", "A"),
        ("D", "H", "B"),
        ("S", "M", "B"),
        ("P", "H", "A")
    ]
)
def test_asignaGrupo_params(input_n1, input_n2, expected):
    assert pedirNombre(input_n1, input_n2) == expected