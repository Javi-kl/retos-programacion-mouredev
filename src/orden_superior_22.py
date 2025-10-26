from statistics import mean
from datetime import datetime


class OpcionNoValida(Exception):
    """Excepción lanzada cuando las opciones no están dentro de su rango"""

    def __init__(self, opcion_introducida, opcion_valida):
        # Crear el constructor nos ayuda a pasar información Util para mostrar el error.
        self.opcion_introducida = opcion_introducida
        self.opcion_valida = opcion_valida
        # Creamos un mensaje claro y directo.
        mensaje = f"{opcion_introducida} no valido. Utiliza -> {opcion_valida}"
        # Llamamos al constructor de la clase padre Exception
        super().__init__(mensaje)


"""def agregar_datos(lista_prueba):
    return lista_prueba.append(4)


def eliminar_ultimo_dato(lista_prueba):
    return lista_prueba.pop()


def actualizar_ultimo_dato(lista_prueba, dato):
    lista_prueba[-1] = dato
    return lista_prueba


# Función de orden superior
def selector_opciones(
    agregar_datos, eliminar_ultimo_dato, actualizar_ultimo_dato, lista_prueba
):
    opcion = input(
        f"Opciones:\n1.Agregar un 4\n2.Eliminar el último dato\n3.Actualizar el último dato\nElige una opción...\n-> "
    )
    try:
        if opcion == "1":
            agregar_datos(lista_prueba)
        elif opcion == "2":
            eliminar_ultimo_dato(lista_prueba)
        elif opcion == "3":
            dato = input("Introduce el dato ")
            actualizar_ultimo_dato(lista_prueba, dato)
        else:
            raise OpcionNoValida(opcion, "1-3")
    except Exception as e:  
        print(f"Ha ocurrido un error {e}")


lista_prueba = [1, 2, 3]
selector_opciones(
    agregar_datos, eliminar_ultimo_dato, actualizar_ultimo_dato, lista_prueba
)"""


"""
extra, esta estructura parece útil para mantener "Unica responsabilidad"
"""


def promediar_notas(
    estudiantes,
):
    """Obtiene una lista de estudiantes por nombre y promedio de sus calificaciones."""

    return [
        {"nombre": est["nombre"], "promedio": mean(est["notas"])} for est in estudiantes
    ]


def mejores_estudiantes(estudiantes, promediar_notas):
    """Obtiene una lista con el nombre de los estudiantes
    *   que tienen calificaciones con un 9 o más de promedio."""
    promedio_notas = promediar_notas(estudiantes)
    estudiantes_sobresalientes = []
    for estudiante in promedio_notas:
        if estudiante["promedio"] >= 9:
            estudiantes_sobresalientes.append(estudiante["nombre"])
    if len(estudiantes_sobresalientes) == 0:
        return "No hay estudiantes con mas de un 9 de nota media"
    else:
        return estudiantes_sobresalientes


def orden_nacimiento(estudiantes):
    """Obtiene una lista de estudiantes ordenada desde el más joven."""
    return sorted(
        estudiantes,
        key=lambda est: datetime.fromisoformat(est["fecha nacimiento"]),
        reverse=True,
    )


def mayor_nota(estudiantes):
    """Obtiene la calificación más alta de entre todas las
    de los alumnos."""

    todas_las_notas = (nota for est in estudiantes for nota in est["notas"])
    return max(todas_las_notas)


# Función de orden superior
def menu_principal(estudiantes):

    while True:
        try:
            opcion = input(
                f"Opciones:\n1.Promediar notas\n2.Mejores estudiantes\n3.Por fecha de nacimiento\n4.Mayor calificación\n5.Salir\nElige una opción...\n-> "
            )
            if opcion == "1":
                print(promediar_notas(estudiantes))

            elif opcion == "2":
                print(
                    f"Estudiantes con sobresaliente: {mejores_estudiantes(estudiantes, promediar_notas)}"
                )
            elif opcion == "3":
                print(orden_nacimiento(estudiantes))
            elif opcion == "4":
                print(
                    f"La calificación mas alta encontrada es: {mayor_nota(estudiantes)}"
                )
            elif opcion == "5":
                break
            else:
                raise OpcionNoValida(opcion, "1-5")

        except Exception as e:
            print(f"Ha ocurrido un error {e}")


estudiantes = [
    {
        "nombre": "javier",
        "fecha nacimiento": "1990-11-11",
        "notas": [3.4, 4.5, 8.9, 9.8],
    },
    {
        "nombre": "andres",
        "fecha nacimiento": "1996-11-1",
        "notas": [1.4, 7.5, 9.9, 9.8],
    },
    {
        "nombre": "Sara",
        "fecha nacimiento": "1999-1-1",
        "notas": [9.4, 7.9, 8.9, 9.9],
    },
]
menu_principal(estudiantes)
