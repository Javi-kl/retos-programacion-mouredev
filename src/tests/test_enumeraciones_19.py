from src.enumeraciones_19 import Order, StatusOrder, day_today
import pytest


@pytest.fixture
def order():
    return Order(1)


def test_estado_inicial_pendiente(order):
    assert order.status_order is StatusOrder.PENDING


def test_enviar_desde_pendiente_cambia_a_sent(order):
    # Act?
    ok = order.send_order()
    assert ok is True
    assert order.status_order is StatusOrder.SENT


def test_no_se_puede_entregar_si_no_esta_enviado(order):
    # Act
    ok = order.delivered_order()
    # Assert
    assert ok is False
    assert order.status_order is StatusOrder.PENDING


def test_entregar_despues_de_enviar(order):
    # Arrange
    order.send_order()
    # Act
    ok = order.delivered_order()
    # Assert
    assert ok is True
    assert order.status_order is StatusOrder.DELIVERED


def test_no_se_puede_cancelar_si_esta_entregado(order):
    # Arrange = Preparación
    order.send_order()
    order.delivered_order()
    # Act = Acción
    ok = order.cancel_order()
    # Assert = Verificación
    assert ok is False
    assert order.status_order is StatusOrder.DELIVERED


def test_cancelar_desde_pendiente(order):
    # Act
    ok = order.cancel_order()
    # Assert
    assert ok is True
    assert order.status_order is StatusOrder.CANCELED


def test_day_today_valido():
    assert day_today(6) == "SATURDAY"


@pytest.mark.parametrize("valor_invalido", [0, 8, -1])
def test_day_today_fuera_de_rango(valor_invalido):
    with pytest.raises(ValueError):
        day_today(valor_invalido)
