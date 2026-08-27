from calculadora import subtracao

def test_subtracao():

    a = 5
    b = 3

    resultado = subtracao(a, b)

    assert resultado == 2