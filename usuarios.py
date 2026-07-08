# Importa las funciones para leer y guardar datos en archivos JSON.
from data_manager import leer_json, guardar_json

# Importa la función para registrar acciones importantes en el historial de auditoría.
from auditoria import registrar_auditoria


# Define la ruta del archivo donde se almacenan los usuarios del sistema.
RUTA_USUARIOS = "data/usuarios.json"


# Permite iniciar sesión validando usuario y contraseña.
def iniciar_sesion():

    # Lee la lista de usuarios desde el archivo JSON.
    usuarios = leer_json(RUTA_USUARIOS)

    # Muestra el título de la sección de inicio de sesión.
    print("\n===== INICIO DE SESIÓN =====")

    # Inicializa el contador de intentos.
    intentos = 1

    # Define la cantidad máxima de intentos permitidos.
    max_intentos = 3

    # Repite el proceso mientras no se superen los intentos permitidos.
    while intentos <= max_intentos:

        # Solicita el nombre de usuario.
        usuario = input("Usuario: ")

        # Solicita la contraseña.
        password = input("Contraseña: ")

        # Recorre cada cuenta registrada en el sistema.
        for cuenta in usuarios:

            # Verifica si el usuario y la contraseña coinciden con una cuenta existente.
            if cuenta["usuario"] == usuario and cuenta["password"] == password:

                # Muestra un mensaje confirmando el inicio de sesión.
                print("\nInicio de sesión exitoso.")

                # Registra en auditoría que el usuario ingresó al sistema.
                registrar_auditoria(cuenta, "Inicio de sesión", "El usuario ingresó al sistema.")

                # Devuelve la cuenta del usuario autenticado.
                return cuenta

        # Muestra un mensaje si las credenciales son incorrectas.
        print("Usuario o contraseña incorrectos.")

        # Muestra el número de intento actual.
        print("Intento", intentos, "de", max_intentos)

        # Aumenta el contador de intentos.
        intentos = intentos + 1

    # Muestra un mensaje si se agotaron todos los intentos.
    print("\nSe agotaron los intentos.")

    # Devuelve None porque no se pudo iniciar sesión.
    return None


# Muestra la información básica del usuario actual.
def mostrar_usuario(usuario_actual):

    # Muestra el título de la sección del usuario actual.
    print("\n===== USUARIO ACTUAL =====")

    # Muestra el nombre del usuario.
    print("Usuario:", usuario_actual["usuario"])

    # Muestra el rol del usuario.
    print("Rol:", usuario_actual["rol"])


# Verifica si un usuario tiene permiso para acceder a un módulo.
def tiene_permiso(usuario_actual, modulo):
    permisos = {
        "admin": [
            "usuarios",
            "ingresos",
            "gastos",
            "reportes",
            "reportes_mensuales",
            "ia",
            "empresas",
            "clientes",
            "proveedores",
            "presupuestos",
            "metas",
            "alertas",
            "sesiones",
            "configuracion_empresa"
        ],
        "administrador": [
            "usuarios",
            "ingresos",
            "gastos",
            "reportes",
            "reportes_mensuales",
            "ia",
            "empresas",
            "clientes",
            "proveedores",
            "presupuestos",
            "metas",
            "alertas",
            "sesiones",
            "configuracion_empresa"
        ],
        "gerente": [
            "ingresos",
            "gastos",
            "reportes",
            "reportes_mensuales",
            "ia",
            "clientes",
            "proveedores",
            "presupuestos",
            "metas",
            "alertas"
        ],
        "contador": [
            "ingresos",
            "gastos",
            "reportes",
            "reportes_mensuales",
            "presupuestos",
            "metas"
        ],
        "empleado": [
            "ingresos",
            "gastos"
        ]
    }

    rol = usuario_actual["rol"]

    if rol in permisos:
        return modulo in permisos[rol]

    return False

    if rol not in permisos:  # Si el rol no existe en el diccionario.
        return False  # No se concede permiso.

    return modulo in permisos[rol]  # Devuelve True si el módulo está permitido para ese rol.

# Verifica si un nombre de usuario ya existe en el sistema.
def usuario_existe(nombre_usuario):

    # Lee la lista de usuarios desde el archivo JSON.
    usuarios = leer_json(RUTA_USUARIOS)

    # Recorre cada usuario registrado.
    for usuario in usuarios:

        # Compara el nombre recibido con los usuarios existentes.
        if usuario["usuario"] == nombre_usuario:

            # Devuelve True si el usuario ya existe.
            return True

    # Devuelve False si no se encontró el usuario.
    return False


# Valida que el rol ingresado sea uno de los roles permitidos.
def validar_rol(rol):

    # Define los roles válidos dentro del sistema.
    roles_validos = ["administrador", "gerente", "contador", "empleado"]

    # Devuelve True si el rol recibido está dentro de la lista de roles válidos.
    return rol in roles_validos


# Permite crear un nuevo usuario desde el módulo de administración.
def crear_usuario(usuario_actual):

    # Muestra el título de la sección de creación de usuario.
    print("\n===== CREAR NUEVO USUARIO =====")

    # Solicita el nombre del nuevo usuario.
    nuevo_usuario = input("Nombre de usuario: ")

    # Valida que el nombre de usuario no esté vacío.
    if nuevo_usuario == "":

        # Muestra un mensaje si el usuario no ingresó nombre.
        print("El nombre de usuario no puede estar vacío.")

        # Devuelve False porque no se creó el usuario.
        return False

    # Verifica si el usuario ya existe.
    if usuario_existe(nuevo_usuario):

        # Muestra un mensaje indicando que el usuario ya está registrado.
        print("Ese usuario ya existe.")

        # Devuelve False porque no se puede duplicar el usuario.
        return False

    # Solicita la contraseña del nuevo usuario.
    password = input("Contraseña: ")

    # Valida que la contraseña no esté vacía.
    if password == "":

        # Muestra un mensaje si no se ingresó contraseña.
        print("La contraseña no puede estar vacía.")

        # Devuelve False porque no se creó el usuario.
        return False

    # Muestra los roles disponibles.
    print("\nRoles disponibles:")
    print("1. administrador")
    print("2. gerente")
    print("3. contador")
    print("4. empleado")

    # Solicita el rol del nuevo usuario y lo convierte a minúsculas.
    rol = input("Rol del nuevo usuario: ").lower()

    # Valida que el rol ingresado sea permitido.
    if not validar_rol(rol):

        # Muestra un mensaje si el rol no pertenece a la lista válida.
        print("Rol inválido. Debe escribir administrador, gerente, contador o empleado.")

        # Devuelve False porque el rol no fue aceptado.
        return False

    # Lee la lista actual de usuarios desde el archivo JSON.
    usuarios = leer_json(RUTA_USUARIOS)

    # Crea un diccionario con los datos del nuevo usuario.
    nuevo = {
        # Guarda el nombre de usuario.
        "usuario": nuevo_usuario,

        # Guarda la contraseña del usuario.
        "password": password,

        # Guarda el rol asignado al usuario.
        "rol": rol
    }

    # Agrega el nuevo usuario a la lista.
    usuarios.append(nuevo)

    # Guarda la lista actualizada de usuarios en el archivo JSON.
    guardar_json(RUTA_USUARIOS, usuarios)

    # Crea el detalle que se guardará en auditoría.
    detalle = "Se creó el usuario " + nuevo_usuario + " con rol " + rol + "."

    # Registra en auditoría la creación del nuevo usuario.
    registrar_auditoria(usuario_actual, "Creación de usuario", detalle)

    # Muestra un mensaje confirmando que el usuario fue creado correctamente.
    print("Usuario creado correctamente.")

    # Devuelve True para indicar que el registro fue exitoso.
    return True


# Muestra todos los usuarios registrados en el sistema.
def listar_usuarios():

    # Lee la lista de usuarios desde el archivo JSON.
    usuarios = leer_json(RUTA_USUARIOS)

    # Muestra el título de la lista de usuarios.
    print("\n===== LISTA DE USUARIOS =====")

    # Verifica si no hay usuarios registrados.
    if len(usuarios) == 0:

        # Muestra un mensaje cuando la lista está vacía.
        print("No hay usuarios registrados.")

        # Termina la función para evitar recorrer una lista vacía.
        return

    # Inicializa un contador para numerar los usuarios.
    contador = 1

    # Recorre cada usuario registrado.
    for usuario in usuarios:

        # Muestra el número, nombre y rol del usuario.
        print(contador, ".", usuario["usuario"], "-", usuario["rol"])

        # Aumenta el contador para el siguiente usuario.
        contador = contador + 1


# Busca un usuario específico por su nombre de usuario.
def buscar_usuario():

    # Lee la lista de usuarios desde el archivo JSON.
    usuarios = leer_json(RUTA_USUARIOS)

    # Muestra el título de búsqueda de usuario.
    print("\n===== BUSCAR USUARIO =====")

    # Solicita el nombre del usuario a buscar.
    busqueda = input("Ingrese el usuario que desea buscar: ")

    # Variable para saber si se encontró el usuario.
    encontrado = False

    # Recorre cada usuario registrado.
    for usuario in usuarios:

        # Verifica si el nombre coincide exactamente con la búsqueda.
        if usuario["usuario"] == busqueda:

            # Muestra un mensaje confirmando que se encontró el usuario.
            print("Usuario encontrado.")

            # Muestra el nombre del usuario.
            print("Usuario:", usuario["usuario"])

            # Muestra el rol del usuario.
            print("Rol:", usuario["rol"])

            # Cambia la variable a True porque sí se encontró el usuario.
            encontrado = True

    # Verifica si no se encontró ningún usuario.
    if not encontrado:

        # Muestra un mensaje indicando que no existe ese usuario.
        print("No se encontró ese usuario.")


# Muestra el menú principal de administración de usuarios.
def menu_administracion_usuarios(usuario_actual):

    # Mantiene el menú activo hasta que el usuario decida volver.
    while True:

        # Muestra el título del módulo de administración de usuarios.
        print("\n===== ADMINISTRACIÓN DE USUARIOS =====")

        # Muestra la opción para crear un nuevo usuario.
        print("1. Crear nuevo usuario")

        # Muestra la opción para listar usuarios.
        print("2. Listar usuarios")

        # Muestra la opción para buscar usuario.
        print("3. Buscar usuario")

        # Muestra la opción para regresar al menú anterior.
        print("0. Volver")

        # Solicita al usuario seleccionar una opción.
        opcion = input("Seleccione una opción: ")

        # Ejecuta la creación de usuario si elige la opción 1.
        if opcion == "1":
            crear_usuario(usuario_actual)

        # Ejecuta el listado de usuarios si elige la opción 2.
        elif opcion == "2":
            listar_usuarios()

        # Ejecuta la búsqueda de usuario si elige la opción 3.
        elif opcion == "3":
            buscar_usuario()

        # Sale del menú si elige la opción 0.
        elif opcion == "0":
            break

        # Muestra un mensaje cuando la opción no es válida.
        else:
            print("Opción inválida.")