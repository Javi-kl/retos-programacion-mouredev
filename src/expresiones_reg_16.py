import re

texto = "hola qu3 tal m3 llamo 13gnacio"
patron = r"\d+"

resultado = re.findall(patron, texto)

if resultado:
    print(f"Encontrado: {resultado}")
else:
    print("No se encontró el patrón")


"""
Extra
"""


def buscar_email(texto):
    # Patrón: letras/números + @ + letras/números + . + letras
    patron = r"\w+@\w+\.[a-z]{2,}"  # \W+ = una o mas letras/numeros, @ = arroba literal, \. = punto literal [a-z]{2,} al menos 2 letras minusculas
    resultado = re.search(
        patron, texto
    )  # re.search busca la primera coincidencia del patron
    return (
        resultado.group() if resultado else None
    )  # group = obtener el texto que coincide


direccion_email = buscar_email("Mi email es email123@gmail.com")
if direccion_email:
    print(f"La dirección de correo es: {direccion_email}")
else:
    print("Dirección de email no encontrada")


def buscar_telefono(numero):
    # \+? = simbolo'+' opcional, \d{2} = 2 digitos, [\s-]? = " " o - opcionales, | = "o logico", \d{9} = 9 digitos
    patron = r"\+?\d{2}[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}[\s-]?\d{2}|\d{9}"
    resultado = re.search(patron, numero)
    return resultado.group() if resultado else None


numero_telefono = buscar_telefono(numero="Mi telefono es: +34 622322123")
if numero_telefono:  # Si número distinto de None entonces imprime.
    print(f"El número de telefono es: {numero_telefono}")
else:
    print("Número de telefono no encontrado")


def buscar_url(texto):
    patron = r"(https://)?(www\.)?[a-zA-Z0-9-)+\.[a-z]{2,}([\w/._-]*)?"
    resultado = re.search(patron, texto)

    return resultado.group() if resultado else None


url = buscar_url(texto="jaga.com/repo")
if url:
    print(f"Url encontrada: {url}")
else:
    print("Url no encontrada")
