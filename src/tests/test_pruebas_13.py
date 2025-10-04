from src.pruebas_13 import sum, datos
from datetime import datetime
import pytest


def test_sum():
    assert sum(4, 5) == 9


"""
Extra
"""

# testear diccionario(datos)
# Existen todos los campos: name, age, bith_date, lenguages


@pytest.mark.parametrize("key", ["name", "age", "birth_date", "lenguages"])
def test_dict_keys(key):
    assert key in datos


# Determina que la longitud de nombre es mayor que 0
def test_name_lenght():
    name_value = datos["name"]
    assert len(name_value) > 0


# Para testear que pase nombres compuesto, comprobamos que el nombre no tenga espacios
def test_name_no_spaces():
    name_value = datos["name"]
    assert " " not in name_value


# Determina que nombre solo tiene caracteres del alfabeto
def test_name_isalpha():
    name_value = datos["name"]
    assert name_value.isalpha()


# determina si age tiene un valor entre 0 y 100
def test_age_type_and_range():
    age_value = datos["age"]
    assert isinstance(age_value, int)
    assert 0 < age_value < 100  # Si no da error es un digito
    # assert age_value.isdigit() #Comprobar si una cadena de texto contiene digitos


# QUEDATE CON ESTO!!!
def test_check_birth_date():
    formats = ["%d/%m/%Y", "%d-%m-%Y"]
    birth_date_value = datos["birth_date"]
    assert any(datetime.strptime(birth_date_value, fmt) for fmt in formats)


# Determinar la longitud de cada lenguage para que sea mayor a 0
def test_lenguages_nonempty():
    lenguages_list = datos["lenguages"]
    for lenguage in lenguages_list:
        assert len(lenguage) > 0


# determinar que lenguages este compuesto por letras
def test_lenguages_isalpha():
    lenguages_list = datos["lenguages"]
    for lenguage in lenguages_list:
        assert lenguage.isalpha()
