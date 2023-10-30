import pytest
from src.ej2_04 import parImpar

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (1, "impar"),
        (18, "par"),
        (100, "par"),
        (5, "impar"),
        (17, "impar"),
        (125, "impar")
    ]
)
def test_parImpar_params(input_n, expected):
    assert parImpar(input_n) == expected
