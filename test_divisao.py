from calculadora import divisao

def test_divisao():

    a = 10
    b = 2

    resultado = soma(a, b)

    assert resultado == 5

def test_divisao_por_zero():
    with pytest.raises(ValueError):
        divisao(10, 0)