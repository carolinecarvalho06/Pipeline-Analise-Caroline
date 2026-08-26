from src.calculadora import Calculadora


def test_multiplicar():
    # Arrange
    calculadora = Calculadora()

    # Act
    resultado = calculadora.multiplicar(4, 5)

    # Assert
    assert resultado == 20
    