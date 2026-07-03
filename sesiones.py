from datetime import datetime
from data_manager import leer_json, guardar_json
from auditoria import registrar_auditoria


RUTA_SESIONES = "data/sesiones.json"


def registrar_inicio_sesion(usuario):
    sesiones = leer_json(RUTA_SESIONES)

    if not isinstance(sesiones, list):
        sesiones = []

    id_sesion = len(sesiones) + 1

    sesion = {
        "id": id_sesion,
        "usuario": usuario["usuario"],
        "rol": usuario["rol"],
        "inicio": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cierre": "Sesion activa",
        "estado": "activa"
    }

    sesiones.append(sesion)
    guardar_json(RUTA_SESIONES, sesiones)

    registrar_auditoria(
        usuario,
        "Inicio de sesion",
        "El usuario inicio la sesion #" + str(id_sesion) + "."
    )

    return id_sesion


def registrar_cierre_sesion(usuario, id_sesion):
    sesiones = leer_json(RUTA_SESIONES)

    if not isinstance(sesiones, list):
        sesiones = []

    for sesion in sesiones:
        if sesion["id"] == id_sesion and sesion["estado"] == "activa":
            sesion["cierre"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sesion["estado"] = "cerrada"

            guardar_json(RUTA_SESIONES, sesiones)

            registrar_auditoria(
                usuario,
                "Cierre de sesion",
                "El usuario cerro la sesion #" + str(id_sesion) + "."
            )

            return True

    return False


def mostrar_historial_sesiones():
    sesiones = leer_json(RUTA_SESIONES)

    print("\n===== HISTORIAL DE SESIONES =====")

    if not isinstance(sesiones, list):
        print("El archivo de sesiones no tiene formato valido.")
        return

    if len(sesiones) == 0:
        print("No hay sesiones registradas.")
        return

    for sesion in sesiones:
        print("--------------------------------")
        print("ID:", sesion["id"])
        print("Usuario:", sesion["usuario"])
        print("Rol:", sesion["rol"])
        print("Inicio:", sesion["inicio"])
        print("Cierre:", sesion["cierre"])
        print("Estado:", sesion["estado"])


def mostrar_sesiones_activas():
    sesiones = leer_json(RUTA_SESIONES)

    print("\n===== SESIONES ACTIVAS =====")

    if not isinstance(sesiones, list):
        print("El archivo de sesiones no tiene formato valido.")
        return

    hay_activas = False

    for sesion in sesiones:
        if sesion["estado"] == "activa":
            print("--------------------------------")
            print("ID:", sesion["id"])
            print("Usuario:", sesion["usuario"])
            print("Rol:", sesion["rol"])
            print("Inicio:", sesion["inicio"])
            hay_activas = True

    if not hay_activas:
        print("No hay sesiones activas.")


def menu_sesiones():
    while True:
        print("\n===== MODULO DE SESIONES =====")
        print("1. Ver historial de sesiones")
        print("2. Ver sesiones activas")
        print("0. Volver")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            mostrar_historial_sesiones()

        elif opcion == "2":
            mostrar_sesiones_activas()

        elif opcion == "0":
            break

        else:
            print("Opcion invalida.")