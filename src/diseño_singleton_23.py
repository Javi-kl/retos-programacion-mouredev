class Singleton:
    _instancia = None
    _inicializado = False  # Bandera para controlar que el init no se ejecute varias veces y reescriba datos

    def __new__(cls):  # cls es la clase ConfiguracionApp
        # Comprobamos si la instancia no ha sido creada todavía.
        if cls._instancia is None:
            print("Creando la única instancia de configuración...")
            # Si no existe, creamos una nueva instancia llamando al __new__
            # de la clase padre (object) y la guardamos en nuestra variable de clase _instancia
            cls._instancia = super(Singleton, cls).__new__(cls)
        else:
            print("La instancia de configuración ya existe. Devolviendo la existente.")
        return cls._instancia

    def __init__(self):
        # Usamos la bandera para asegurar que "init" solo se ejecute una vez
        # Esto evita que se reinicien los datos de configuración cada vez que se accede a la instancia.
        if self._inicializado:
            return  # Si inicializado == true no hacemos nada más.
        print("Inicializando la configuración por primera vez...")
        # incializamos algunos datos en la instancia recién creada
        self.datos_singleton = {"tema": "oscuro", "idioma": "es"}
        self.__class__._inicializado = True  # Cambiar bandera a Inicializada


# Probando funcionamiento
# 1. Se llama a __new__, crea la instancia.
# 2. Se llama a __init__, inicializa los datos y pone la bandera a True.
singleton1 = Singleton()
print(f"Configuración 1: {singleton1.datos_singleton}")

# Cambiamos el valor de la configuración a través del objeto config1
singleton1.datos_singleton["idioma"] = "en"
print(f"Idioma cambiado a: {singleton1.datos_singleton['idioma']}")

# 1. Se llama a __new__, devuelve la instancia existente.
# 2. Se llama a __init__, pero como la bandera _inicializado es True, sale inmediatamente.
singleton2 = Singleton()
print(f"Configuración 2: {singleton2.datos_singleton}")  # El idioma se mantiene en "en"

# comprobar si ambas configs apunta al mismo objetos en memoria
print(singleton1 is singleton2)


"""
Extra
"""


class SingletonSesionUsuario:
    _instancia = None

    # Datos usuario como None
    id = None
    usuario = None
    nombre = None
    email = None

    def __new__(cls):
        if not cls._instancia:  # Si el objeto no es true entonces lo creamos
            cls._instancia = super(SingletonSesionUsuario, cls).__new__(cls)
        else:
            print("La sesion ya está iniciada.")
        return cls._instancia

    def iniciar_sesion(self, id, usuario, nombre, email):
        if self.usuario is not None:
            print(f"Ya hay una sesion iniciada para {self.usuario}")
            return
        print(f"Iniciando sesion para {self.usuario}")
        self.id = id
        self.usuario = usuario
        self.nombre = nombre
        self.email = email

    def obtener_datos(self):
        """Devuelve los datos del usuario actual o un mensaje si no hay sesión."""
        if self.usuario is None:
            return "No hay ninguna sesión activa en este momento"
        return {
            "id": self.id,
            "usuario": self.usuario,
            "nombre": self.nombre,
            "email": self.email,
        }

    def cerrar_sesion(self):
        if self.usuario is None:
            return "No hay ninguna sesion activa para cerrar"
        print(f"Cerrando la sesion para {self.usuario}")
        self.id = None
        self.usuario = None
        self.nombre = None
        self.email = None


# Crear sesiones
sesion1 = SingletonSesionUsuario()
sesion2 = SingletonSesionUsuario()
# Recuperar datos
print(f"Datos actuales: {sesion1.obtener_datos()}")

# iniciar sesion
sesion1.iniciar_sesion(123, "javikl", "javi", "email@com")

# Visualizar datos desde sesion2
print(f"Datos actuales: {sesion2.obtener_datos()}")

# Intentamos iniciar otra sesión sin cerrar la actual.
sesion2.iniciar_sesion("002", "ana", "Ana", "ana@test.com")

# Cerra sesion
sesion1.cerrar_sesion()

# Comprobar que se borraron los datos
print(f"Datos después de cerrar sesión: {sesion1.obtener_datos}")

# iniciar nueva sesion
sesion2.iniciar_sesion("002", "ana", "Ana", "ana@test.com")
print(f"Nuevos datos de sesión: {sesion2.obtener_datos()}")
