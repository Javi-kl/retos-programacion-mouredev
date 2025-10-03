import json
import os
import xml.etree.ElementTree as xml

# JSON
# definir datos como dict

datos = {
    "nombre": "javier",
    "edad": 25,
    "fecha": "17/11/1990",
    "lenguages": ["python", "java", "rust"],
}
datos_json = "datos.json"
# guardar datos en JSON
with open(datos_json, "w") as json_file:
    json.dump(datos, json_file)

# mostrar contenido del fichero
"""with open(datos_json, "r") as json_file:
    contenido = json.load(json_file)
    print(contenido)"""

# borrar archivo
# os.remove(datos_json)

xml_file = "javier.xml"
# XML
# crear elemento raiz
# print("\n --- XML ---")


def save_xml():
    root = xml.Element("data")
    for key, value in datos.items():
        child = xml.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                xml.SubElement(child, "item").text = item
        else:
            child.text = str(value)

    tree = xml.ElementTree(root)
    tree.write(xml_file)


save_xml()
# with open(xml_file) as xml_data:
#    print(xml_data.read())
# borrar arbol
# os.remove(xml_file)


"""
extra
"""


class Persona:
    def __init__(self, name, age, birth_date, stacks):
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.stacks = stacks

    def __str__(self) -> str:
        return f"{self.name} tiene {self.age} años, nacido el {self.birth_date} y conoce: {self.stacks}"


with open(datos_json, "r") as j_file:
    contenido = json.load(j_file)
    programmer1 = Persona(
        contenido["nombre"],
        contenido["edad"],
        contenido["fecha"],
        contenido["lenguages"],
    )

    print(f"Desde json: {programmer1}")


with open(xml_file) as xml_data:

    root1 = xml.fromstring(xml_data.read())  # Obtner el nodo raiz

    nodo_name = root1.find("nombre")
    if nodo_name is not None:
        valor_name = nodo_name.text
    else:
        valor_name = "Sin nombre"

    nodo_age = root1.find("edad")
    if nodo_age is not None:
        valor_age = nodo_age.text
    else:
        valor_age = "Sin edad"

    nodo_date = root1.find("fecha")
    if nodo_date is not None:
        valor_birth_date = nodo_date.text
    else:
        valor_birth_date = "Sin año de nacimiento"

    subnodo_stacks = root1.find("lenguages")
    if subnodo_stacks is not None:
        lista_stacks = []
        for lenguaje in subnodo_stacks.findall("item"):
            lista_stacks.append(lenguaje.text)

    else:
        lista_stacks = []

    programmer2 = Persona(valor_name, valor_age, valor_birth_date, lista_stacks)
    print(f"Desde xml: {programmer2}")


os.remove(datos_json)
os.remove(xml_file)
