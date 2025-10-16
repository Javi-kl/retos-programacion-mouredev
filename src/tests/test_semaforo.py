from src.semaforo import Semaforo, EstadoSemaforo
import pytest

# Objetivo TDD
# 1.ROJO(hacer que falle), 2.VERDE(hacer que pase), 3.REFACTOR(mejorar el codigo)


# Aun no hemos escrito nada en el principal semaforo
def test_semaforo_debe_estar_rojo():
    # Preparación: crear un semaforo
    semaforo = Semaforo()
    # Acción

    # Verificación
    assert semaforo.estado == EstadoSemaforo.ROJO


def test_debe_cambiar_rojo_verde():
    # Preparación: crear otro semaforo, debería usar fixture.
    semaforo = Semaforo()

    # Acción: llamar a metodo de semaforo inexistente.
    semaforo.siguiente_estado()

    # verificación: El nuevo estado debe ser verde
    assert semaforo.estado == EstadoSemaforo.VERDE


def test_debe_cambiar_verde_amarillo():
    # Preparación: crear otro semaforo nuevo.
    semaforo = Semaforo()

    semaforo.siguiente_estado()
    # Acción: llamar a metodo siguiente estado, sin la logica adecuada
    # para que falle
    semaforo.siguiente_estado()

    # Verificación El nuevo estado debe ser amarillo
    assert semaforo.estado == EstadoSemaforo.AMARILLO


def test_debe_cambiar_amarillo_rojo():
    # Preparación: crear otro semaforo nuevo.
    semaforo = Semaforo()

    # Avanzamos hasta que amarillo
    semaforo.siguiente_estado()
    semaforo.siguiente_estado()
    semaforo.siguiente_estado()

    assert semaforo.estado == EstadoSemaforo.ROJO
