import pytest

from src.calculadora import Calculadora


def test_dividir():
    # Arrange
    calculadora = Calculadora()

    # Act
    resultado = calculadora.dividir(10, 2)

    # Assert
    assert resultado == 5


def test_dividir_por_zero():
    calculadora = Calculadora()

    with pytest.raises(ValueError):
        calculadora.dividir(10, 0)
        