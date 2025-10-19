import time
import random


# Esto sería proceso principal
def procesar_datos(datos, funcion_callback):
    """Procesa lista de datos y ejecuta función callback sobre ella"""
    # Aqui podríamos tener mas logica, sobre todo procesos que tardan tiempo.
    print(f"Procesando datos...")
    time.sleep(2)

    return funcion_callback(datos)


# Cuando el proceso principal acabe, entonces llama a callback
def funcion_max_callback(lista_datos):
    return max(lista_datos)


lista_datos = [13213, 13213, 13213, 141, 41412]
print(procesar_datos(lista_datos, funcion_max_callback))


"""
extra
"""


# funcion principal, debe llamar a los callbacks en cada etapa
def procesar_pedidos(
    nombre_pedido,
    callback_confirmacion,
    callback_listo,
    callback_entrega,
    callback_pago,
):
    tiempo_preparación = random.randint(1, 6)

    print(f"Ha pedido {nombre_pedido}")
    callback_confirmacion(nombre_pedido)
    time.sleep(tiempo_preparación)

    callback_listo(nombre_pedido)
    time.sleep(tiempo_preparación)

    callback_entrega(nombre_pedido)

    callback_pago(nombre_pedido)
    time.sleep(tiempo_preparación)
    print(f"Pedido finalizado. Que tenga un buen dia")


def callback_confirmacion(nombre_pedido):

    print(f"CB -> Espere los { nombre_pedido} durante su elaboración")


def callback_listo(nombre_pedido):
    print(f"CB -> Pedido {nombre_pedido} listo, espere su entrega")


def callback_entrega(nombre_pedido):
    print(f"CB -> Pedido {nombre_pedido} entregado")


def callback_pago(nombre_pedido):
    print(f"Aún tiene que pagar el pedido {nombre_pedido}")


procesar_pedidos(
    "macarrones", callback_confirmacion, callback_listo, callback_entrega, callback_pago
)
