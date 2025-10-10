from src.iteraciones_17 import recursive_func, elementos, frutas, lista_pares


def test_value_type():
    assert (type(recursive_func(n=1))) == int


def test_elementos_type():
    assert isinstance(elementos, list)


def test_frutas_lenght():
    assert len(frutas) > 0


def test_lista_pares_not_inpar_num():
    for num in lista_pares:
        assert num % 2 == 0


def test_lista_pares_has_not_zero():
    assert 0 not in lista_pares
