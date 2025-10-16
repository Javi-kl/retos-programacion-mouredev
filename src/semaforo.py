from enum import Enum, auto


class EstadoSemaforo:
    ROJO = auto()
    VERDE = auto()
    AMARILLO = auto()


class Semaforo:
    def __init__(self) -> None:
        self.estado = EstadoSemaforo.ROJO

    def siguiente_estado(self):
        if self.estado == EstadoSemaforo.ROJO:
            self.estado = EstadoSemaforo.VERDE

        elif self.estado == EstadoSemaforo.VERDE:
            self.estado = EstadoSemaforo.AMARILLO

        elif self.estado == EstadoSemaforo.AMARILLO:
            self.estado = EstadoSemaforo.ROJO
