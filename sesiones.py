# Importa datetime para guardar la fecha y hora de inicio y cierre de sesión.
from datetime import datetime

# Importa las funciones para leer y guardar datos en archivos JSON.
from data_manager import leer_json, guardar_json

# Importa la función para registrar acciones importantes en el historial de auditoría.
from auditoria import registrar_auditoria


# Define la ruta del archivo donde se almacenan las sesiones.
RUTA_SESIONES = "data/sesiones.json"


# Registra el inicio de sesión de un usuario.
def registrar_inicio_sesion(usuario):

    # Lee la lista actual de sesiones desde el archivo JSON.
    sesiones = leer_json(RUTA_SESIONES)

    # Verifica que el contenido leído sea una lista válida.
    if not isinstance(sesiones, list):

        # Si el archivo no contiene una lista, reinicia las sesiones como lista vacía.
        sesiones = []

    # Genera un ID para la nueva sesión usando la cantidad actual de registros.
    id_sesion = len(sesiones) + 1

    # Crea un diccionario con la información de la sesión iniciada.
    sesion = {
        # Guarda el ID único de la sesión.
        "id": id_sesion,

        # Guarda el nombre del usuario que inició sesión.
        "usuario": usuario["usuario"],

        # Guarda el rol del usuario.
        "rol": usuario["rol"],

        # Guarda la fecha y hora de inicio de sesión.
        "inicio": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

        # Indica que la sesión aún no ha sido cerrada.
        "cierre": "Sesion activa",

        # Marca el estado actual de la sesión como activa.
        "estado": "activa"
    }

    # Agrega la nueva sesión a la lista de sesiones.
    sesiones.append(sesion)

    # Guarda la lista actualizada de sesiones en el archivo JSON.
    guardar_json(RUTA_SESIONES, sesiones)

    # Registra en auditoría el inicio de sesión del usuario.
    registrar_auditoria(
        usuario,
        "Inicio de sesion",
        "El usuario inicio la sesion #" + str(id_sesion) + "."
    )

    # Devuelve el ID de la sesión para poder cerrarla después.
    return id_sesion


# Registra el cierre de una sesión activa.
def registrar_cierre_sesion(usuario, id_sesion):

    # Lee la lista actual de sesiones desde el archivo JSON.
    sesiones = leer_json(RUTA_SESIONES)

    # Verifica que el contenido leído sea una lista válida.
    if not isinstance(sesiones, list):

        # Si el archivo no contiene una lista, reinicia las sesiones como lista vacía.
        sesiones = []

    # Recorre cada sesión registrada.
    for sesion in sesiones:

        # Busca la sesión que coincida con el ID recibido y que todavía esté activa.
        if sesion["id"] == id_sesion and sesion["estado"] == "activa":

            # Guarda la fecha y hora exacta del cierre de sesión.
            sesion["cierre"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Cambia el estado de la sesión a cerrada.
            sesion["estado"] = "cerrada"

            # Guarda los cambios en el archivo JSON.
            guardar_json(RUTA_SESIONES, sesiones)

            # Registra en auditoría el cierre de sesión del usuario.
            registrar_auditoria(
                usuario,
                "Cierre de sesion",
                "El usuario cerro la sesion #" + str(id_sesion) + "."
            )

            # Devuelve True para indicar que la sesión fue cerrada correctamente.
            return True

    # Devuelve False si no se encontró una sesión activa con ese ID.
    return False


# Muestra el historial completo de sesiones registradas.
def mostrar_historial_sesiones():

    # Lee la lista de sesiones desde el archivo JSON.
    sesiones = leer_json(RUTA_SESIONES)

    # Muestra el título de la sección de historial.
    print("\n===== HISTORIAL DE SESIONES =====")

    # Verifica que el contenido del archivo tenga formato de lista.
    if not isinstance(sesiones, list):

        # Muestra un mensaje si el archivo tiene un formato incorrecto.
        print("El archivo de sesiones no tiene formato valido.")

        # Termina la función para evitar errores al recorrer los datos.
        return

    # Verifica si no hay sesiones registradas.
    if len(sesiones) == 0:

        # Muestra un mensaje cuando no hay sesiones guardadas.
        print("No hay sesiones registradas.")

        # Termina la función porque no hay datos para mostrar.
        return

    # Recorre cada sesión registrada.
    for sesion in sesiones:

        # Imprime una línea separadora para ordenar visualmente cada sesión.
        print("--------------------------------")

        # Muestra el ID de la sesión.
        print("ID:", sesion["id"])

        # Muestra el usuario asociado a la sesión.
        print("Usuario:", sesion["usuario"])

        # Muestra el rol del usuario.
        print("Rol:", sesion["rol"])

        # Muestra la fecha y hora de inicio.
        print("Inicio:", sesion["inicio"])

        # Muestra la fecha y hora de cierre o el texto de sesión activa.
        print("Cierre:", sesion["cierre"])

        # Muestra el estado de la sesión.
        print("Estado:", sesion["estado"])


# Muestra solamente las sesiones que están activas.
def mostrar_sesiones_activas():

    # Lee la lista de sesiones desde el archivo JSON.
    sesiones = leer_json(RUTA_SESIONES)

    # Muestra el título de la sección de sesiones activas.
    print("\n===== SESIONES ACTIVAS =====")

    # Verifica que el contenido del archivo tenga formato de lista.
    if not isinstance(sesiones, list):

        # Muestra un mensaje si el archivo tiene un formato incorrecto.
        print("El archivo de sesiones no tiene formato valido.")

        # Termina la función para evitar errores.
        return

    # Variable para saber si se encontró al menos una sesión activa.
    hay_activas = False

    # Recorre cada sesión registrada.
    for sesion in sesiones:

        # Verifica si la sesión tiene estado activo.
        if sesion["estado"] == "activa":

            # Imprime una línea separadora para ordenar la información.
            print("--------------------------------")

            # Muestra el ID de la sesión activa.
            print("ID:", sesion["id"])

            # Muestra el usuario que tiene la sesión activa.
            print("Usuario:", sesion["usuario"])

            # Muestra el rol del usuario.
            print("Rol:", sesion["rol"])

            # Muestra la fecha y hora en que inició la sesión.
            print("Inicio:", sesion["inicio"])

            # Cambia la variable para indicar que sí existe al menos una sesión activa.
            hay_activas = True

    # Verifica si no se encontró ninguna sesión activa.
    if not hay_activas:

        # Muestra un mensaje indicando que no hay sesiones abiertas.
        print("No hay sesiones activas.")


# Muestra el menú principal del módulo de sesiones.
def menu_sesiones():

    # Mantiene el menú activo hasta que el usuario decida volver.
    while True:

        # Muestra el título del módulo de sesiones.
        print("\n===== MODULO DE SESIONES =====")

        # Muestra la opción para ver el historial completo de sesiones.
        print("1. Ver historial de sesiones")

        # Muestra la opción para ver únicamente sesiones activas.
        print("2. Ver sesiones activas")

        # Muestra la opción para regresar al menú anterior.
        print("0. Volver")

        # Solicita al usuario seleccionar una opción.
        opcion = input("Seleccione una opcion: ")

        # Muestra el historial completo si el usuario elige la opción 1.
        if opcion == "1":
            mostrar_historial_sesiones()

        # Muestra las sesiones activas si el usuario elige la opción 2.
        elif opcion == "2":
            mostrar_sesiones_activas()

        # Sale del menú si el usuario elige la opción 0.
        elif opcion == "0":
            break

        # Muestra un mensaje cuando el usuario ingresa una opción inválida.
        else:
            print("Opcion invalida.")