from enum import Enum


class WeekDay(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


def day_today(num):
    if not isinstance(num, int):
        raise TypeError("num debe ser int")
    try:
        return WeekDay(num).name
    except ValueError as e:
        raise ValueError("Número de día inválido usa 1-7") from e


print(day_today(6))


"""
Extra
"""
print("\n--- Ejercicio Extra ---")


class StatusOrder(Enum):

    PENDING = 1
    SENT = 2
    DELIVERED = 3
    CANCELED = 4


class Order:
    def __init__(self, id) -> None:
        self.id_order = id
        self.status_order = StatusOrder.PENDING

    def send_order(self) -> bool:
        if self.status_order == StatusOrder.PENDING:
            self.status_order = StatusOrder.SENT
            return True

        return False

    def cancel_order(self) -> bool:
        if self.status_order == StatusOrder.DELIVERED:
            return False

        self.status_order = StatusOrder.CANCELED
        return True

    def delivered_order(self) -> bool:
        if self.status_order == StatusOrder.SENT:
            self.status_order = StatusOrder.DELIVERED
            return True
        return False

    def __str__(self) -> str:
        return f"Estado del pedido {self.id_order} es: {self.status_order.name}"


pedido1 = Order(1)
# Esta parte de comprobaciones debes hacerla con pytest
pedido1.send_order()
print(pedido1)
