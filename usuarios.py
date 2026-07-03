from data_manager import leer_json, guardar_json
from auditoria import registrar_auditoria


RUTA_USUARIOS = "data/usuarios.json"


def iniciar_sesion():
    usuarios = leer_json(RUTA_USUARIOS)

    print("\n===== INICIO DE SESIÓN =====")

    intentos = 1
    max_intentos = 3

    while intentos <= max_intentos:
        usuario = input("Usuario: ")
        password = input("Contraseña: ")

        for cuenta in usuarios:
            if cuenta["usuario"] == usuario and cuenta["password"] == password:
                print("\nInicio de sesión exitoso.")
                registrar_auditoria(cuenta, "Inicio de sesión", "El usuario ingresó al sistema.")
                return cuenta

        print("Usuario o contraseña incorrectos.")
        print("Intento", intentos, "de", max_intentos)
        intentos = intentos + 1

    print("\nSe agotaron los intentos.")
    return None


def mostrar_usuario(usuario_actual):
    print("\n===== USUARIO ACTUAL =====")
    print("Usuario:", usuario_actual["usuario"])
    print("Rol:", usuario_actual["rol"])


def tiene_permiso(usuario, modulo):
    rol = usuario["rol"]

    permisos = {
        "administrador": [
            "dashboard",
            "ingresos",
            "gastos",
            "flujo_caja",
            "reportes",
            "ia_financiera",
            "configuracion",
            "usuarios",
            "auditoria",
            "sesiones",
            "empresas",
            "clientes",
            "proveedores",
            "presupuestos",
            "metas",
            "alertas"
        ],
        "gerente": [
            "dashboard",
            "flujo_caja",
            "reportes",
            "ia_financiera"
            "clientes",
            "proveedores",
            "presupuestos",
            "metas",
            "alertas"
        ],
        "contador": [
            "dashboard",
            "ingresos",
            "gastos",
            "flujo_caja",
            "reportes"
        ],
        "empleado": [
            "dashboard",
            "ingresos"
        ]
    }

    if rol in permisos:
        return modulo in permisos[rol]

    return False


def usuario_existe(nombre_usuario):
    usuarios = leer_json(RUTA_USUARIOS)

    for usuario in usuarios:
        if usuario["usuario"] == nombre_usuario:
            return True

    return False


def validar_rol(rol):
    roles_validos = ["administrador", "gerente", "contador", "empleado"]

    return rol in roles_validos


def crear_usuario(usuario_actual):
    print("\n===== CREAR NUEVO USUARIO =====")

    nuevo_usuario = input("Nombre de usuario: ")

    if nuevo_usuario == "":
        print("El nombre de usuario no puede estar vacío.")
        return False

    if usuario_existe(nuevo_usuario):
        print("Ese usuario ya existe.")
        return False

    password = input("Contraseña: ")

    if password == "":
        print("La contraseña no puede estar vacía.")
        return False

    print("\nRoles disponibles:")
    print("1. administrador")
    print("2. gerente")
    print("3. contador")
    print("4. empleado")

    rol = input("Rol del nuevo usuario: ").lower()

    if not validar_rol(rol):
        print("Rol inválido. Debe escribir administrador, gerente, contador o empleado.")
        return False

    usuarios = leer_json(RUTA_USUARIOS)

    nuevo = {
        "usuario": nuevo_usuario,
        "password": password,
        "rol": rol
    }

    usuarios.append(nuevo)
    guardar_json(RUTA_USUARIOS, usuarios)

    detalle = "Se creó el usuario " + nuevo_usuario + " con rol " + rol + "."
    registrar_auditoria(usuario_actual, "Creación de usuario", detalle)

    print("Usuario creado correctamente.")
    return True


def listar_usuarios():
    usuarios = leer_json(RUTA_USUARIOS)

    print("\n===== LISTA DE USUARIOS =====")

    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
        return

    contador = 1

    for usuario in usuarios:
        print(contador, ".", usuario["usuario"], "-", usuario["rol"])
        contador = contador + 1


def buscar_usuario():
    usuarios = leer_json(RUTA_USUARIOS)

    print("\n===== BUSCAR USUARIO =====")
    busqueda = input("Ingrese el usuario que desea buscar: ")

    encontrado = False

    for usuario in usuarios:
        if usuario["usuario"] == busqueda:
            print("Usuario encontrado.")
            print("Usuario:", usuario["usuario"])
            print("Rol:", usuario["rol"])
            encontrado = True

    if not encontrado:
        print("No se encontró ese usuario.")


def menu_administracion_usuarios(usuario_actual):
    while True:
        print("\n===== ADMINISTRACIÓN DE USUARIOS =====")
        print("1. Crear nuevo usuario")
        print("2. Listar usuarios")
        print("3. Buscar usuario")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_usuario(usuario_actual)

        elif opcion == "2":
            listar_usuarios()

        elif opcion == "3":
            buscar_usuario()

        elif opcion == "0":
            break

        else:
            print("Opción inválida.")