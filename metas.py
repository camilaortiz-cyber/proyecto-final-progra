# Importa las funciones para leer y guardar datos en archivos JSON.
from data_manager import leer_json, guardar_json

# Importa la función para registrar acciones importantes en el historial de auditoría.
from auditoria import registrar_auditoria

# Importa la función para calcular el total de ingresos o gastos.
from finanzas import calcular_total


# Define la ruta del archivo donde se almacenan las metas financieras.
RUTA_METAS = "data/metas.json"

# Define la ruta del archivo donde se almacenan los ingresos.
RUTA_INGRESOS = "data/ingresos.json"

# Define la ruta del archivo donde se almacenan los gastos.
RUTA_GASTOS = "data/gastos.json"


# Permite crear una nueva meta financiera en el sistema.
def crear_meta(usuario_actual):

    # Muestra el título de la sección de creación de metas.
    print("\n===== CREAR META FINANCIERA =====")

    # Muestra los tipos de meta disponibles.
    print("Tipos de meta:")
    print("1. ventas")
    print("2. ahorro")
    print("3. utilidad")

    # Solicita el tipo de meta y lo convierte a minúsculas.
    tipo = input("Tipo de meta: ").lower()

    # Solicita una descripción para identificar la meta.
    descripcion = input("Descripcion de la meta: ")

    # Intenta convertir el monto ingresado a número decimal.
    try:
        monto = float(input("Monto objetivo: Q"))

    # Captura el error si el usuario ingresa un valor no numérico.
    except ValueError:

        # Muestra un mensaje indicando que el monto debe ser numérico.
        print("El monto debe ser numerico.")

        # Devuelve False porque no se pudo crear la meta.
        return False

    # Verifica que el tipo de meta ingresado sea uno de los permitidos.
    if tipo not in ["ventas", "ahorro", "utilidad"]:

        # Muestra un mensaje si el tipo de meta no es válido.
        print("Tipo de meta invalido.")

        # Devuelve False porque el tipo de meta no fue aceptado.
        return False

    # Valida que la descripción no esté vacía y que el monto sea mayor a cero.
    if descripcion == "" or monto <= 0:

        # Muestra un mensaje si faltan datos obligatorios.
        print("Descripcion y monto valido son obligatorios.")

        # Devuelve False porque los datos no cumplen las validaciones.
        return False

    # Lee la lista actual de metas desde el archivo JSON.
    metas = leer_json(RUTA_METAS)

    # Crea un diccionario con la información de la nueva meta.
    meta = {
        # Guarda el tipo de meta.
        "tipo": tipo,

        # Guarda la descripción de la meta.
        "descripcion": descripcion,

        # Guarda el monto objetivo de la meta.
        "monto": monto,

        # Guarda el usuario que creó la meta.
        "creado_por": usuario_actual["usuario"]
    }

    # Agrega la nueva meta a la lista de metas.
    metas.append(meta)

    # Guarda la lista actualizada de metas en el archivo JSON.
    guardar_json(RUTA_METAS, metas)

    # Registra en auditoría la creación de la meta.
    registrar_auditoria(
        usuario_actual,
        "Creacion de meta",
        "Se creo meta de " + tipo + " por Q" + str(monto) + "."
    )

    # Muestra un mensaje confirmando que la meta fue creada correctamente.
    print("Meta creada correctamente.")

    # Devuelve True para indicar que la meta fue registrada exitosamente.
    return True


# Calcula el valor actual de una meta según su tipo.
def calcular_valor_actual_meta(tipo):

    # Lee la lista de ingresos desde el archivo JSON.
    ingresos = leer_json(RUTA_INGRESOS)

    # Lee la lista de gastos desde el archivo JSON.
    gastos = leer_json(RUTA_GASTOS)

    # Calcula el total de ingresos registrados.
    total_ingresos = calcular_total(ingresos)

    # Calcula el total de gastos registrados.
    total_gastos = calcular_total(gastos)

    # Si la meta es de ventas, el avance se basa en el total de ingresos.
    if tipo == "ventas":
        return total_ingresos

    # Si la meta es de ahorro, el avance se basa en ingresos menos gastos.
    if tipo == "ahorro":
        return total_ingresos - total_gastos

    # Si la meta es de utilidad, el avance también se basa en ingresos menos gastos.
    if tipo == "utilidad":
        return total_ingresos - total_gastos

    # Devuelve cero si el tipo de meta no coincide con ninguno válido.
    return 0


# Muestra el progreso actual de todas las metas registradas.
def ver_progreso_metas():

    # Lee la lista de metas desde el archivo JSON.
    metas = leer_json(RUTA_METAS)

    # Muestra el título de la sección de progreso de metas.
    print("\n===== PROGRESO DE METAS =====")

    # Verifica si no hay metas registradas.
    if len(metas) == 0:

        # Muestra un mensaje cuando no hay metas para revisar.
        print("No hay metas registradas.")

        # Termina la función para evitar recorrer una lista vacía.
        return

    # Recorre cada meta registrada.
    for meta in metas:

        # Calcula el avance actual de la meta según su tipo.
        actual = calcular_valor_actual_meta(meta["tipo"])

        # Calcula el porcentaje de avance comparando el valor actual con el objetivo.
        porcentaje = (actual / meta["monto"]) * 100

        # Limita el porcentaje máximo a 100 para no mostrar más del total de la meta.
        if porcentaje > 100:
            porcentaje = 100

        # Imprime una línea separadora para ordenar visualmente cada meta.
        print("--------------------------------")

        # Muestra el tipo de meta.
        print("Tipo:", meta["tipo"])

        # Muestra la descripción de la meta.
        print("Descripcion:", meta["descripcion"])

        # Muestra el monto objetivo de la meta.
        print("Objetivo: Q", meta["monto"])

        # Muestra el valor actual alcanzado.
        print("Actual: Q", actual)

        # Muestra el porcentaje de progreso.
        print("Progreso:", round(porcentaje, 2), "%")

        # Evalúa si la meta ya fue alcanzada.
        if porcentaje >= 100:
            print("Estado: meta alcanzada.")

        # Evalúa si la meta está cerca de cumplirse.
        elif porcentaje >= 70:
            print("Estado: muy cerca de alcanzar la meta.")

        # Evalúa si la meta tiene un avance intermedio.
        elif porcentaje >= 40:
            print("Estado: progreso medio.")

        # Indica que la meta todavía necesita más avance.
        else:
            print("Estado: falta avanzar.")


# Muestra el menú principal del módulo de metas.
def menu_metas(usuario_actual):

    # Mantiene el menú activo hasta que el usuario decida volver.
    while True:

        # Muestra el título del módulo de metas.
        print("\n===== MODULO DE METAS =====")

        # Muestra la opción para crear una meta.
        print("1. Crear meta")

        # Muestra la opción para revisar el progreso de metas.
        print("2. Ver progreso de metas")

        # Muestra la opción para regresar al menú anterior.
        print("0. Volver")

        # Solicita al usuario seleccionar una opción.
        opcion = input("Seleccione una opcion: ")

        # Ejecuta la creación de meta si el usuario elige la opción 1.
        if opcion == "1":
            crear_meta(usuario_actual)

        # Ejecuta la visualización del progreso si el usuario elige la opción 2.
        elif opcion == "2":
            ver_progreso_metas()

        # Sale del menú de metas si el usuario elige la opción 0.
        elif opcion == "0":
            break

        # Muestra un mensaje si el usuario ingresa una opción inválida.
        else:
            print("Opcion invalida.")