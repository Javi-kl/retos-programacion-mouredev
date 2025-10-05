from src.fecha_14 import months_list, format_born_date
import pytest


@pytest.mark.parametrize(
    "key",
    [
        "enero",
        "febrero",
        "marzo",
        "abril",
        "mayo",
        "junio",
        "julio",
        "agosto",
        "septiembre",
        "octubre",
        "noviembre",
        "diciembre",
    ],
)
def test_name_months(key):
    assert key in months_list


def test_num_of_months():
    assert len(months_list) == 12
