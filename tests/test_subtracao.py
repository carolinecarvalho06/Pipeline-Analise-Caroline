from src.calculadora import Calculadora


def test_subtrair():
    calculadora = Calculadora()
    resultado = calculadora.subtrair(5, 2)
    assert resultado == 3