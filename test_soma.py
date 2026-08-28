from calculadora import multiplicacao


def test_multiplicacao():
    a = 4
    b = 3

    resultado = multiplicacao(a, b)

    assert resultado == 12