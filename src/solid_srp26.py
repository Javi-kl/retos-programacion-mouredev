# --- Forma correcta ---
class Order:
    def __init__(self, precio, id, email):
        self.precio = precio
        self.id = id
        self.email = email

    def coste_pedido(self):
        return self.precio


class ImprimirFactura:
    @staticmethod
    def imprimir(order: Order):
        coste_total = order.coste_pedido()
        print(f"Aqui tiene su factura : {coste_total} €")


class MandarEmail:
    @staticmethod
    def enviar_email(order: Order):
        coste_total = order.coste_pedido()
        print(f"Enviando email a: {order.email}")
        print(f"Asunto: Pedido: {order.id} confirmado")
        print(f"Cuerpo: Factura: {coste_total}")


pedido1 = Order(423.2, 1, "hola@gmail.com")
ImprimirFactura.imprimir(pedido1)
MandarEmail.enviar_email(pedido1)


# ---  Forma Incorrecta ---
class Order1:
    def __init__(self, precio, id, email):
        self.precio = precio
        self.id = id
        self.email = email

    def imprimir(self):

        print(f"Aqui tiene su factura : {self.precio} €")

    def enviar_email(self):
        print(f"Enviando email a: {self.email}")
        print(f"Asunto: Pedido {self.id} confirmado")
        print(f"Cuerpo: Factura: {self.precio}")


pedido2 = Order1(424, 2, "fal@gmail.com")
pedido2.imprimir()
pedido2.enviar_email()


"""
extra
"""

print("\n--- Extra ---\n")


# crear clase biblioteca con los 3 metodos registro de libros, gestión de usuarios
# y el procesamiento de préstamos.
class Biblioteca:
    def __init__(self) -> None:
        self.lista_libros = []
        self.lista_usuarios = []
        self.libros_disponibles = []

    # Registrar libros: recibe título, autor y número de copias disponibles.
    def registrar_libros(self, titulo, autor, copias):
        datos_libro = {}
        datos_libro["titulo"] = titulo.lower()
        datos_libro["autor"] = autor.lower()
        datos_libro["copias"] = copias
        self.lista_libros.append(datos_libro)

    # Gestionar usuarios: recibe nombre, número de identificación y correo electrónico.
    def gestionar_usuarios(self, nombre, num_id, email):
        datos_usuario = {}
        datos_usuario["nombre"] = nombre.lower()
        datos_usuario["identificación"] = num_id
        datos_usuario["email"] = email.lower()
        self.lista_usuarios.append(datos_usuario)

    # Procesar préstamos: recibe, libro a prestar(elimina 1 copia) o libro devuelto(devuelve 1 copia) a datos_libro["copias"]
    def procesar_prestamos(self, nombre_usuario, l_prestar, l_devolver):

        # Comprobar si el usuario existe en la base de datos
        usuario_registrado = any(
            u["nombre"] == nombre_usuario for u in self.lista_usuarios
        )
        if not usuario_registrado:
            print(f"Usuario {nombre_usuario} no registrado")

        elif l_prestar != None:
            libro_disponible = any(
                l["titulo"] == l_prestar and l["copias"] > 0 for l in self.lista_libros
            )

            if libro_disponible:
                print(f"Libro {l_prestar} prestado a {nombre_usuario}")
                for l in self.lista_libros:
                    if l["titulo"] == l_prestar:
                        l["copias"] -= 1
                        print(f"Copias restantes de {l_prestar}: {l['copias']}")
            else:
                print("No se ha podido procesar su solicitud.\nLibro no encontrados")
        elif l_devolver != None:
            for l in self.lista_libros:
                if l["titulo"] == l_devolver:
                    l["copias"] += 1
                    print(f"Libro {l_devolver} devuelto correctamente.")

    # Función para mostrar las listas de clase
    def __str__(self) -> str:
        return f"Lista libros: {[self.lista_libros]}\nLista usuarios: {self.lista_usuarios}"


biblioteca1 = Biblioteca()
biblioteca1.registrar_libros("mobidick", "frank darlin", 3)
biblioteca1.registrar_libros("harry potter", "teresa arlin", 1)

biblioteca1.gestionar_usuarios("javier", 2, "afsdaf@gmail.com")
biblioteca1.gestionar_usuarios("sara", 3, "sdaf@gmail.com")
print(biblioteca1)

biblioteca1.procesar_prestamos("sara", l_prestar="mobidick", l_devolver=None)
biblioteca1.procesar_prestamos("sara", l_prestar=None, l_devolver="mobidick")
