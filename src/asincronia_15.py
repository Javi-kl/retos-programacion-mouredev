import asyncio  # importa el módulo para programación asíncrona
import datetime
import time


async def funcion_asincrona(
    time: int, name: str
):  # Define una corutina con 'async def;
    print(f"Iniciando función ...{datetime.datetime.now().strftime('%H:%M:%S')}")
    print(f"Nombre: {name} ")
    print(f"La función durara {time} segundos")
    await asyncio.sleep(time)  # Pausa no bloqueante por 3 seg(Await para esperar)
    print(f"Terminando función ...{datetime.datetime.now().strftime('%H:%M:%S')}")


# Ejecuta el event loop con la corutina principal
asyncio.run(funcion_asincrona(5, "Javier"))


"""
Extra
"""


async def a_function():
    print(f"Iniciando 'A'...")
    await asyncio.sleep(1)  # Pausa no bloqueante por 3 seg(Await para esperar)
    print(f"Función 'A' terminada")


async def b_function():
    print(f"Iniciando 'B'...")
    await asyncio.sleep(2)
    print(f"Función 'B' terminada")


async def c_function():
    print(f"Iniciando 'C'...")
    await asyncio.sleep(3)
    print(f"Función 'C' terminada")


async def d_function():
    print(f"Iniciando 'D'...")
    await asyncio.sleep(1)
    print(f"Función 'D' terminada")


async def principal_extra():  # corutina principal
    inicio = time.perf_counter()  # Medir tiempo de ejecución / inicio
    await asyncio.gather(
        a_function(),
        b_function(),
        c_function(),
        return_exceptions=True,  # No cancela si una falla
    )
    await d_function()
    print(
        f"Tiempo total: {time.perf_counter() - inicio:.3f}s"
    )  # Medir tiempo de ejecución y restar inicio


asyncio.run(principal_extra())
