import requests


def peticion_http(url):
    try:
        respuesta = requests.get(
            url, timeout=5
        )  # TImeout permite que acabe la petición si tarda demasiado
        respuesta.raise_for_status()  # lanza excepción si status_code da error
        print(f"Petición {url} exitosa")
        return respuesta

    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la petición {e}")


print("--- Realizando ejercicio base ---")
respuesta_base = peticion_http(url="https://jsonplaceholder.typicode.com/users")
if respuesta_base:
    datos = respuesta_base.json()
    print(f"Nombre del primer usuario: {datos[0]['name']}")

print("\n" + "=" * 40 + "\n")  # Separador visual
"""
extra
"""

print("--- Realizando ejercicio extra ---")


def obtener_info_pokemon(nombre_o_id, endpoint):
    url_pokemon = f"https://pokeapi.co/api/v2/{endpoint}/{nombre_o_id}/"

    print(f"Buscando información de: {nombre_o_id}")
    respuesta_pokemon = peticion_http(url_pokemon)
    if respuesta_pokemon:
        return respuesta_pokemon.json()
    else:
        return None


# Mostrar nombre, id, peso, altura y tipo(s) del Pokémon
def mostrar_datos_pokemon(datos_pokemon):
    """
    Recibe los datos de un Pokémon y los muestra de forma formateada.
    """

    nombre = datos_pokemon["name"]
    id_pokemon = datos_pokemon["id"]
    peso = datos_pokemon["weight"]
    altura = datos_pokemon["height"]

    tipos = [tipo["type"]["name"] for tipo in datos_pokemon["types"]]

    print("\n--- Información del Pokémon ---")
    print(
        f"Nombre: {nombre.capitalize()}"
    )  # .capitalize() pone la primera letra en mayúscula.
    print(f"ID: {id_pokemon}")
    print(f"Peso: {peso}")
    print(f"Altura: {altura}")
    print(
        f"Tipo(s): {', '.join(tipos)}"
    )  # .join une los elementos de la lista en un string.


# Mostrar nombre de su cadena de evoluciones
def mostrar_cadena_evoluciones(datos_evoluciones):
    """
    Recibe los datos de la cadena de evoluciones y los muestra de forma formateada.
    """
    nombre_cadena = datos_evoluciones["chain"]["species"]["name"]
    print(f"\n--- Información de la cadena de evoluciones ---")
    print(f"{nombre_cadena}")


# Mostrar los juegos en los que aparece
def mostrar_juegos_donde_aparece(datos_generacion):
    """Recibe los juegos donde aparece y los muestra de forma formateada."""

    lista_juegos = datos_generacion["name"]
    print(f"\n--- Información de juegos donde aparece ---")
    print(f"{lista_juegos}")


print("--- Realizando ejercicio extra ---")
datos = obtener_info_pokemon("7", endpoint="pokemon")

if datos:
    mostrar_datos_pokemon(datos)

datos_evoluciones = obtener_info_pokemon("7", endpoint="evolution-chain")
if datos_evoluciones:
    mostrar_cadena_evoluciones(datos_evoluciones)

datos_generacion = obtener_info_pokemon("7", endpoint="generation")
if datos_generacion:
    mostrar_juegos_donde_aparece(datos_generacion)
