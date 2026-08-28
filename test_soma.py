from calculadora import soma


def test_soma():
    a = 4
    b = 3

    resultado = soma(a, b)

    assert resultado == 10
