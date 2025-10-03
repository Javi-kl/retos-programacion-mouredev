from src.pruebas_13 import sum, datos
import pytest
from datetime import datetime


def test_sum():
    assert sum(4, 5) == 9


"""
Extra
"""

# testear diccionario(datos)
# Existen todos los campos: name, age, bith_date, lenguages


def test_check_has_keys():
    for key in datos.keys():

        assert key in ["name", "age", "birth_date", "lenguages"]


# Determinar que los datos introducidos son correctos
def test_check_name():
    name_value = datos["name"]
    assert len(name_value) > 0
    assert name_value.isascii()


def test_check_age():
    age_value = datos["age"]
    assert 100 > age_value > 0  # Si no da error es un digito
    # assert age_value.isdigit() #Comprobar si una cadena de texto contiene digitos


# QUEDATE CON ESTO!!!
def test_check_birth_date():
    birth_date_value = datos["birth_date"]
    assert datetime.strptime(birth_date_value, "%d/%m/%Y")


# comprobar si existen nombres en la lista lenguages
def test_lenght_lenguages():
    for lenguage in datos["lenguages"]:
        assert len(lenguage) > 0
