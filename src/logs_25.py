import logging
import re
from datetime import date
import time
from functools import wraps

logging.basicConfig(
    level=logging.DEBUG,
    filename="proyecto.log",
    filemode="w",  # usar 'a' si no se quiere sobreescribir datos
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def validar_contraseña(contraseña=""):
    """Función para validar una contraseña y guardar un log"""

    logging.info(
        f"Iniciando la función 'validar_contraseña' con parametro: {contraseña} "
    )
    patron = r"^(?=.{8,64}$)(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s]).+$"
    logging.info(f"Validando con: {patron} ")
    if not contraseña:
        logging.error("No se ha introducido ninguna contraseña que validar")
        return "No hay nada que validar"
    elif " " in contraseña:
        logging.error("Contraseña rechazada por contener espacios en blanco")
        logging.debug("Debe arreglarse el patrón para que no permita espacios")
        return "Contraseña no valida"

    elif re.match(patron, contraseña):
        logging.info("Se ha validado correctamente")
        return "Contraseña valida"

    else:
        logging.warning("Se ha introducido contraseña no valida")
        return "Contraseña no valida"


print(validar_contraseña(""))


"""
extra
"""
print("\n--- Extra ---")
logging.info("\nIniciando parte Extra")


def logger(func):
    """Decorador para medir el tiempo de ejecución de las funciones"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Llamando a función: {func.__name__}")
        logging.info(f"Parametros de función: {args}")
        contador_inicio = time.time()
        resultado = func(*args, **kwargs)  #
        logging.info(f"Fin función: {func.__name__}.")
        contador_fin = time.time()
        duracion = contador_fin - contador_inicio
        logging.info(
            f"La función: {func.__name__}  tardo {duracion:.5f} en ejecutarse."
        )
        return resultado  # si devuelves la funcion directamente, no será legible por terminal

    return wrapper


@logger
def añadir(tarea, descripcion, tareas_list):
    """Añadir tarea"""
    fecha = date.today()

    if len(tareas_list) >= 20:  # Primero la condición mas restrictiva !!
        logging.error(f"La lista de tareas está llena {len(tareas_list)}.")
        logging.debug("Si esto ocurre a menudo, ampliar limite de tareas")
        print(
            f"La lista de tareas está llena {len(tareas_list)}, elimine algunas tareas."
        )
        return

    elif len(descripcion) > 58:
        logging.error(f"Descripción de {tarea} demasiado larga {len(descripcion)}.")
        logging.debug("Si esto ocurre a menudo, ampliar limite de carácteres")
        print(f"Descripción de: {tarea} demasiado larga. Maximo 58 caracteres.")
        return

    elif len(tareas_list) >= 17:
        logging.warning(f"El limite de tareas esta cerca {len(tareas_list)} de 20.")
        logging.debug("Si esto ocurre a menudo, ampliar limite de carácteres")

    dict_tarea = {
        "tarea": tarea.lower(),
        "descripcion": descripcion,
        "fecha": fecha.isoformat(),
    }
    tareas_list.append(dict_tarea)
    return tareas_list


@logger
def eliminar(tareas_creadas, tarea_a_eliminar):
    """Eliminar una tarea"""
    tarea_a_eliminar = tarea_a_eliminar.lower()
    longitud_inicial = len(tareas_creadas)
    # crear nueva lista que no contiene la tarea a eliminar
    nuevas_tareas = [t for t in tareas_creadas if t["tarea"] != tarea_a_eliminar]
    if len(nuevas_tareas) < longitud_inicial:
        logging.info(f"Tarea: {tarea_a_eliminar} borrada con exito")
    else:
        logging.warning(
            f"El usuario no ha conseguido borrar la tarea: {tarea_a_eliminar}"
        )

    return nuevas_tareas


@logger
def listar(tareas_creadas):
    """Listar todas las tareas"""
    tareas_formateadas = "\n".join(
        ", ".join(f"{value}" for value in item.values()) for item in tareas_creadas
    )
    logging.info(f"Solo se muestran los valores de las tareas")
    return tareas_formateadas


def gestion_tareas():
    """Función para gestionar las tareas(podría convertirse
    en menú principal para el usuario con distintas opcioens)
    """
    tareas_list = []

    añadir(
        "pagarte a ti mismo",
        "Al principio serás el primero en recibir tu parte",
        tareas_list,
    )

    añadir(
        "mantener servidor",
        "Realizar mantenimiento semanal en el servidor",
        tareas_list,
    )

    print(listar(tareas_list))
    tareas_list = eliminar(tareas_list, "mantener servidor")
    print(listar(tareas_list))

    logging.warning(
        f"La función {gestion_tareas.__name__} debe convertirse en un menú para usuario"
    )


gestion_tareas()
