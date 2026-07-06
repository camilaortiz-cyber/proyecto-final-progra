# Importa datetime para registrar la fecha y hora exacta de cada acción.
from datetime import datetime

# Importa las funciones necesarias para leer y guardar datos en archivos JSON.
from data_manager import leer_json, guardar_json


# Define la ruta del archivo donde se guardará el historial de auditoría.
RUTA_AUDITORIA = "data/auditoria.json"


# Registra una acción realizada por un usuario dentro del sistema.
def registrar_auditoria(usuario, accion, detalle):

    # Lee el historial actual de auditoría desde el archivo JSON.
    auditoria = leer_json(RUTA_AUDITORIA)

    # Crea un diccionario con la información de la acción realizada.
    registro = {
        # Guarda el nombre del usuario que realizó la acción.
        "usuario": usuario["usuario"],

        # Guarda el rol del usuario dentro del sistema.
        "rol": usuario["rol"],

        # Guarda el nombre o tipo de acción realizada.
        "accion": accion,

        # Guarda una descripción más específica de la acción.
        "detalle": detalle,

        # Guarda la fecha y hora actual en formato año-mes-día hora:minuto:segundo.
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Agrega el nuevo registro al historial de auditoría.
    auditoria.append(registro)

    # Guarda nuevamente el historial actualizado en el archivo JSON.
    guardar_json(RUTA_AUDITORIA, auditoria)

    # Devuelve True para indicar que el registro fue guardado correctamente.
    return True


# Muestra en pantalla todo el historial de auditoría registrado.
def mostrar_auditoria():

    # Lee todos los registros de auditoría guardados en el archivo JSON.
    auditoria = leer_json(RUTA_AUDITORIA)

    # Imprime el título de la sección de historial de auditoría.
    print("\n===== HISTORIAL DE AUDITORÍA =====")

    # Verifica si todavía no existen acciones registradas.
    if len(auditoria) == 0:

        # Muestra un mensaje cuando el historial está vacío.
        print("No hay acciones registradas todavía.")

        # Termina la función para evitar recorrer una lista vacía.
        return

    # Recorre cada registro guardado en el historial de auditoría.
    for registro in auditoria:

        # Imprime una línea separadora para mejorar la presentación visual.
        print("--------------------------------")

        # Muestra la fecha en que se realizó la acción.
        print("Fecha:", registro["fecha"])

        # Muestra el usuario que realizó la acción.
        print("Usuario:", registro["usuario"])

        # Muestra el rol del usuario que realizó la acción.
        print("Rol:", registro["rol"])

        # Muestra el tipo de acción registrada.
        print("Acción:", registro["accion"])

        # Muestra el detalle o descripción de la acción realizada.
        print("Detalle:", registro["detalle"])