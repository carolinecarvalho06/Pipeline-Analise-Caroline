from src.calculadora import Calculadora


def test_somar():
    calculadora = Calculadora()
    resultado = calculadora.somar(2, 3)
    assert resultado == 5