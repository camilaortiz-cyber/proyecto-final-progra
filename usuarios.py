from data_manager import leer_json


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
            "configuracion"
        ],
        "gerente": [
            "dashboard",
            "flujo_caja",
            "reportes",
            "ia_financiera"
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