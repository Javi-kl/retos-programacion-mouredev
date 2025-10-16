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


def obtener_info_pokemon(nombre_o_id):
    url_pokemon = f"https://pokeapi.co/api/v2/pokemon/{nombre_o_id}/"

    print(f"Buscando información de: {nombre_o_id}")
    respuesta_pokemon = peticion_http(url_pokemon)
    if respuesta_pokemon:
        return respuesta_pokemon.json()
    else:
        return None


# Muostrar nombre, id, peso, altura y tipo(s) del Pokémon
def mostrar_datos_pokemon(datos_pokemon):
    """
    Recibe los datos de un Pokémon y los muestra de forma formateada.
    """
    if not datos_pokemon:
        print("No se pudo mostrar la información.")
        return

    # >> MEJORA: Extraemos los datos que nos interesan en variables.
    #    Esto hace el código más legible y fácil de depurar.
    nombre = datos_pokemon["name"]
    id_pokemon = datos_pokemon["id"]
    peso = datos_pokemon["weight"] / 10  # El peso está en hectogramos, lo pasamos a kg.
    altura = (
        datos_pokemon["height"] * 10
    )  # La altura está en decímetros, la pasamos a cm.

    # >> MEJORA: El tipo es una lista, la procesamos para mostrarla bien.
    #    Usamos una "list comprehension" para extraer los nombres de los tipos.
    tipos = [tipo["type"]["name"] for tipo in datos_pokemon["types"]]

    print("\n--- Información del Pokémon ---")
    print(
        f"Nombre: {nombre.capitalize()}"
    )  # .capitalize() pone la primera letra en mayúscula.
    print(f"ID: {id_pokemon}")
    print(f"Peso: {peso} kg")
    print(f"Altura: {altura} cm")
    print(
        f"Tipo(s): {', '.join(tipos)}"
    )  # .join une los elementos de la lista en un string.


# --- Ejecución de la dificultad extra ---
print("--- Realizando ejercicio extra (PokeAPI) ---")
pokemon_buscado = "squirtle"  # Puedes cambiarlo por un nombre o un número (ej: 7)
datos = obtener_info_pokemon(pokemon_buscado)

# Solo si obtuvimos datos, los mostramos.
if datos:
    mostrar_datos_pokemon(datos)


# Mostrar nombre de su cadena de evoluciones
def mostrar_cadena_evoluciones(url):
    endpoint = "evolution-chain/"
    id = "7/"
    url_evoluciones = url + endpoint + id
    try:
        respuesta_evoluciones = requests.get(url_evoluciones)
        respuesta_evoluciones.raise_for_status()
        print(f"Petición {url} exitosa")
        return respuesta_evoluciones

    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la petición {e}")


# Mostrar los juegos en los que aparece
def mostrar_juegos_donde_aparece(url):
    endpoint = "generation/"
    id = "7/"
    url_generacion = url + endpoint + id
    try:
        respuesta_generacion = requests.get(url_generacion)
        respuesta_generacion.raise_for_status()
        print(f"Petición {url} exitosa")
        return respuesta_generacion

    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la petición {e}")


url = "https://pokeapi.co/api/v2/"


"""respuesta_evoluciones = mostrar_cadena_evoluciones(url)
if respuesta_evoluciones:
    datos = respuesta_evoluciones.json()
    print(f" {datos}")


respuesta_generacion = mostrar_juegos_donde_aparece(url)
if respuesta_generacion:
    datos = respuesta_generacion.json()
    print(f" {datos}")
"""
