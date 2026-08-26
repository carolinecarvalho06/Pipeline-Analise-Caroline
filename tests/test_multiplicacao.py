from src.calculadora import Calculadora


def test_multiplicar():
    calculadora = Calculadora()
    resultado = calculadora.multiplicar(4, 5)
    assert resultado == 20