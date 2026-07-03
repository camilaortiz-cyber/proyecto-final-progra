from datetime import datetime
from data_manager import leer_json, guardar_json


RUTA_AUDITORIA = "data/auditoria.json"


def registrar_auditoria(usuario, accion, detalle):
    auditoria = leer_json(RUTA_AUDITORIA)

    registro = {
        "usuario": usuario["usuario"],
        "rol": usuario["rol"],
        "accion": accion,
        "detalle": detalle,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    auditoria.append(registro)
    guardar_json(RUTA_AUDITORIA, auditoria)

    return True


def mostrar_auditoria():
    auditoria = leer_json(RUTA_AUDITORIA)

    print("\n===== HISTORIAL DE AUDITORÍA =====")

    if len(auditoria) == 0:
        print("No hay acciones registradas todavía.")
        return

    for registro in auditoria:
        print("--------------------------------")
        print("Fecha:", registro["fecha"])
        print("Usuario:", registro["usuario"])
        print("Rol:", registro["rol"])
        print("Acción:", registro["accion"])
        print("Detalle:", registro["detalle"])