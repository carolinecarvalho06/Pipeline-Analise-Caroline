from src.calculadora import Calculadora


def test_subtrair():
    # Arrange
    calculadora = Calculadora()

    # Act
    resultado = calculadora.subtrair(5, 2)

    # Assert
    assert resultado == 3
    