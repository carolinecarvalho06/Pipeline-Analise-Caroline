from src.calculadora import Calculadora


def test_somar():
    # Arrange
    calculadora = Calculadora()

    # Act
    resultado = calculadora.somar(2, 3)

    # Assert
    assert resultado == 5