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

    return WeekDay(num).name


print(day_today(6))


"""
Extra
"""
print("\n--- Ejercicio Extra ---")


class StatusOrder(Enum):

    PENDING = 1
    SEND = 2
    DELIVERED = 3
    CANCELED = 4


class Order:
    def __init__(self, id) -> None:
        self.id_order = id
        self.status_order = StatusOrder.PENDING

    def send_order(self):
        if self.status_order == StatusOrder.PENDING:
            self.status_order = StatusOrder.SEND
        else:
            print(f"El pedido {self.id_order} no puede enviarse.")

    def cancel_order(self):
        if self.status_order == StatusOrder.DELIVERED:
            print(f"El pedido {self.id_order} ya esta entregado \nNo puede cancelarse")
        else:
            self.status_order = StatusOrder.CANCELED

    def delivered_order(self):
        if self.status_order != StatusOrder.SEND:
            print(f"No se puede entregar pedido {self.id_order}, aún no esta enviado.")
        else:
            self.status_order = StatusOrder.DELIVERED

    def __str__(self) -> str:
        return f"Estado del pedido {self.id_order} es: {self.status_order.name}"


pedido1 = Order(43123)
# Esta parte de comprobaciones debes hacerla con pytest
pedido1.delivered_order()
print(pedido1)
