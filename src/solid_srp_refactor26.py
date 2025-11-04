class Biblioteca:
    def __init__(self):
        self.lista_libros = []
        self.lista_usuarios = []
        self.prestamos = []

    def agregar_libro(self, *libros):
        for libro in libros:
            self.lista_libros.append(libro)

    def agregar_usuario(self, *usuarios):
        for usuario in usuarios:
            self.lista_usuarios.append(usuario)

    def gestionar_prestamos(self, usuarioid, libro):
        datos_prestamo = {"id": usuarioid, "libro": libro}
        self.prestamos.append(datos_prestamo)

    def gestionar_devoluciones(self, usuarioid):
        self.prestamos = [p for p in self.prestamos if p["id"] != usuarioid]


class Libro:
    def __init__(self, titulo, autor, copias):
        self.titulo = titulo
        self.autor = autor
        self.copias = copias


class Usuario:
    def __init__(self, nombre, num_id, email):
        self.nombre = nombre
        self.num_id = num_id
        self.email = email


class ProcesamientoPrestamos:
    @staticmethod
    def prestamos(biblioteca: Biblioteca, usuario: Usuario, libro: Libro):
        if libro.copias > 0:
            print(f"Se ha prestado {libro.titulo} al usuario: {usuario.nombre} ")
            libro.copias -= 1
            biblioteca.gestionar_prestamos(usuario.num_id, libro.titulo)
            print(f"Copias actuales del libro {libro.titulo}: {libro.copias}")
        else:
            print(f"No hay suficientes copias")


class ProcesamientoDevoluciones:
    @staticmethod
    def devoluciones(biblioteca: Biblioteca, usuario: Usuario, libro: Libro):
        print(f"El usuario {usuario.nombre} ha devuelto: {libro.titulo}")

        libro.copias += 1
        biblioteca.gestionar_devoluciones(usuario.num_id)

        print(f"Copias actuales del libro {libro.titulo}: {libro.copias}")


libro1 = Libro("mobidick", "frank darlin", 3)
libro2 = Libro("harry potter", "teresa arlin", 1)

usuario1 = Usuario("sara", 3, "sdaf@gmail.com")
usuario2 = Usuario("javier", 1, "dfsdaf@gmail.com")

biblioteca_publica = Biblioteca()
biblioteca_publica.agregar_libro(libro1, libro2)
biblioteca_publica.agregar_usuario(usuario1, usuario2)

ProcesamientoPrestamos.prestamos(biblioteca_publica, usuario1, libro1)
ProcesamientoDevoluciones.devoluciones(biblioteca_publica, usuario1, libro1)
