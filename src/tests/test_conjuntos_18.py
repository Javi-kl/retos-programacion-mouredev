from src.conjuntos_18 import my_list, s_1, s_2, s_3
import pytest


def test_list_type():
    assert isinstance(my_list, list)


def test_list_clear():
    assert len(my_list) == 0


@pytest.mark.parametrize("sets", (s_1, s_2, s_3))
def test_sets_has_items(sets):
    assert len(sets) > 0


@pytest.mark.parametrize("sets", (s_1, s_2, s_3))
def test_sets_type(sets):
    assert isinstance(sets, set)
