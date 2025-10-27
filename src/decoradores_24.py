from functools import wraps


def decorator(funcion):
    def wrapper(*args, **kwargs):
        print("Antes de la función")
        resultado = funcion(*args, **kwargs)
        print("Después de la función")
        return resultado

    return wrapper


@decorator
def suma_basica(a, b):
    return a + b


suma_basica(3, 4)


"""
extra
"""


def conteo_llamadas(func):
    """contabiliza cuántas veces
    se ha llamado a una función"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.contador += 1
        print(f"Llamada número {wrapper.contador} para {func.__name__}")
        return func(*args, **kwargs)

    wrapper.contador = 0
    return wrapper


@conteo_llamadas
def probar_conteo():
    return "Hola mundo"


for i in range(3):
    probar_conteo()


@conteo_llamadas
def probar_conteo2():
    return "Hola habi"


print(f"La función 'probar_conteo' ha sido llamada {probar_conteo.contador} veces")
