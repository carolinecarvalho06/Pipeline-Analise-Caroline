from calculadora import soma


def test_soma():
    
    a = 2
    b = 3

    resultado = soma(a, b)

    assert resultado == 5