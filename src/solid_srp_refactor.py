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
    def prestamos(usuario: Usuario, libro: Libro):
        print(f"Se ha prestado {libro.titulo} al usuario: {usuario.nombre} ")
        libro.copias -= 1
        print(f"Copias actuales del libro {libro.titulo}: {libro.copias}")


class ProcesamientoDevoluciones:
    @staticmethod
    def devoluciones(usuario: Usuario, libro: Libro):
        print(f"El usuario {usuario.nombre} ha devuelto: {libro.titulo}")
        libro.copias += 1
        print(f"Copias actuales del libro {libro.titulo}: {libro.copias}")


libro1 = Libro("mobidick", "frank darlin", 3)
libro2 = Libro("harry potter", "teresa arlin", 1)

usuario1 = Usuario("sara", 3, "sdaf@gmail.com")
usuario2 = Usuario("javier", 1, "dfsdaf@gmail.com")

ProcesamientoPrestamos.prestamos(usuario1, libro1)
ProcesamientoDevoluciones.devoluciones(usuario1, libro1)
