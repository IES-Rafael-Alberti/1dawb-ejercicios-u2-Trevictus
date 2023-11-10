import pytest
from src.ej2_02 import coincideContrasenia

@pytest.mark.parametrize(
    "input_s1, input_s2, expected",
    [
        ("contraseña", "contraSEÑA", True),
        ("contraseña", "CONtreÑA", False),
        ("contraseña", "CONtraceÑA", False),
        ("contraseña", "CONtraseÑA", True),
        ("contraseña", "cONtraSEÑa", True)
    ]
)
def test_coincideContrasenia_params(input_s1, input_s2, expected):
    assert coincideContrasenia(input_s1, input_s2) == expected