# Importa datetime para guardar la fecha y hora exacta de cada movimiento financiero.
from datetime import datetime

# Importa las funciones para leer y guardar información en archivos JSON.
from data_manager import leer_json, guardar_json

# Importa la función para registrar acciones importantes en el historial de auditoría.
from auditoria import registrar_auditoria


# Define la ruta del archivo donde se almacenan los ingresos.
RUTA_INGRESOS = "data/ingresos.json"

# Define la ruta del archivo donde se almacenan los gastos.
RUTA_GASTOS = "data/gastos.json"


# Solicita y valida el monto ingresado por el usuario.
def pedir_monto():

    # Intenta convertir el valor ingresado a número decimal.
    try:

        # Solicita el monto al usuario.
        monto = float(input("Monto: Q"))

        # Verifica que el monto sea mayor a cero.
        if monto <= 0:

            # Muestra un mensaje si el monto no es válido.
            print("El monto debe ser mayor a cero.")

            # Devuelve None para indicar que el monto no fue aceptado.
            return None

        # Devuelve el monto cuando es válido.
        return monto

    # Captura el error si el usuario ingresa texto o un valor no numérico.
    except ValueError:

        # Muestra un mensaje indicando que el monto debe ser numérico.
        print("El monto debe ser un número válido.")

        # Devuelve None para indicar que hubo un error en el ingreso del monto.
        return None


# Solicita los datos generales de un ingreso o gasto.
def pedir_datos_movimiento(tipo):

    # Solicita la descripción del movimiento financiero.
    descripcion = input("Descripción del " + tipo + ": ")

    # Solicita la categoría del movimiento financiero.
    categoria = input("Categoría: ")

    # Solicita y valida el monto del movimiento.
    monto = pedir_monto()

    # Verifica que la descripción no esté vacía.
    if descripcion == "":

        # Muestra un mensaje si la descripción está vacía.
        print("La descripción no puede estar vacía.")

        # Devuelve None para cancelar el registro del movimiento.
        return None

    # Verifica que la categoría no esté vacía.
    if categoria == "":

        # Muestra un mensaje si la categoría está vacía.
        print("La categoría no puede estar vacía.")

        # Devuelve None para cancelar el registro del movimiento.
        return None

    # Verifica si el monto no fue válido.
    if monto is None:

        # Devuelve None para cancelar el registro del movimiento.
        return None

    # Crea un diccionario con los datos principales del movimiento.
    movimiento = {
        # Guarda la descripción del ingreso o gasto.
        "descripcion": descripcion,

        # Guarda la categoría del ingreso o gasto.
        "categoria": categoria,

        # Guarda el monto validado del movimiento.
        "monto": monto,

        # Guarda la fecha y hora actual del registro.
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Devuelve el movimiento creado para que sea guardado como ingreso o gasto.
    return movimiento


# Registra un nuevo ingreso en el sistema.
def registrar_ingreso(usuario):

    # Muestra el título de la sección de registro de ingresos.
    print("\n===== REGISTRAR INGRESO =====")

    # Solicita los datos del ingreso usando la función reutilizable.
    ingreso = pedir_datos_movimiento("ingreso")

    # Verifica si los datos del ingreso no fueron válidos.
    if ingreso is None:

        # Devuelve False porque no se registró el ingreso.
        return False

    # Agrega al ingreso el usuario que realizó el registro.
    ingreso["creado_por"] = usuario["usuario"]

    # Lee la lista actual de ingresos desde el archivo JSON.
    ingresos = leer_json(RUTA_INGRESOS)

    # Agrega el nuevo ingreso a la lista.
    ingresos.append(ingreso)

    # Guarda la lista actualizada de ingresos en el archivo JSON.
    guardar_json(RUTA_INGRESOS, ingresos)

    # Crea el detalle que se guardará en el historial de auditoría.
    detalle = "Registró ingreso de Q" + str(ingreso["monto"]) + " en categoría " + ingreso["categoria"] + "."

    # Registra en auditoría la acción de ingreso realizada por el usuario.
    registrar_auditoria(usuario, "Registro de ingreso", detalle)

    # Muestra un mensaje confirmando que el ingreso fue registrado correctamente.
    print("Ingreso registrado correctamente.")

    # Devuelve True para indicar que el registro fue exitoso.
    return True


# Registra un nuevo gasto en el sistema.
def registrar_gasto(usuario):

    # Muestra el título de la sección de registro de gastos.
    print("\n===== REGISTRAR GASTO =====")

    # Solicita los datos del gasto usando la función reutilizable.
    gasto = pedir_datos_movimiento("gasto")

    # Verifica si los datos del gasto no fueron válidos.
    if gasto is None:

        # Devuelve False porque no se registró el gasto.
        return False

    # Agrega al gasto el usuario que realizó el registro.
    gasto["creado_por"] = usuario["usuario"]

    # Lee la lista actual de gastos desde el archivo JSON.
    gastos = leer_json(RUTA_GASTOS)

    # Agrega el nuevo gasto a la lista.
    gastos.append(gasto)

    # Guarda la lista actualizada de gastos en el archivo JSON.
    guardar_json(RUTA_GASTOS, gastos)

    # Crea el detalle que se guardará en el historial de auditoría.
    detalle = "Registró gasto de Q" + str(gasto["monto"]) + " en categoría " + gasto["categoria"] + "."

    # Registra en auditoría la acción de gasto realizada por el usuario.
    registrar_auditoria(usuario, "Registro de gasto", detalle)

    # Muestra un mensaje confirmando que el gasto fue registrado correctamente.
    print("Gasto registrado correctamente.")

    # Devuelve True para indicar que el registro fue exitoso.
    return True


# Calcula la suma total de una lista de movimientos financieros.
def calcular_total(lista_movimientos):

    # Inicializa el acumulador del total en cero.
    total = 0

    # Recorre cada movimiento dentro de la lista.
    for movimiento in lista_movimientos:

        # Suma el monto del movimiento al total acumulado.
        total = total + movimiento["monto"]

    # Devuelve el total calculado.
    return total


# Muestra el flujo de caja con ingresos, gastos y saldo disponible.
def mostrar_flujo_caja():

    # Lee la lista de ingresos desde el archivo JSON.
    ingresos = leer_json(RUTA_INGRESOS)

    # Lee la lista de gastos desde el archivo JSON.
    gastos = leer_json(RUTA_GASTOS)

    # Calcula el total de ingresos registrados.
    total_ingresos = calcular_total(ingresos)

    # Calcula el total de gastos registrados.
    total_gastos = calcular_total(gastos)

    # Calcula el saldo disponible restando los gastos a los ingresos.
    saldo = total_ingresos - total_gastos

    # Muestra el título de la sección de flujo de caja.
    print("\n===== FLUJO DE CAJA =====")

    # Muestra el total de ingresos.
    print("Total de ingresos: Q", total_ingresos)

    # Muestra el total de gastos.
    print("Total de gastos: Q", total_gastos)

    # Muestra el saldo disponible.
    print("Saldo disponible: Q", saldo)

    # Verifica si el saldo es positivo.
    if saldo > 0:

        # Muestra que el flujo de caja es positivo.
        print("Estado: flujo positivo")

    # Verifica si el saldo está en cero.
    elif saldo == 0:

        # Muestra que la empresa está en punto de equilibrio.
        print("Estado: punto de equilibrio")

    # Si el saldo es menor que cero, indica flujo negativo.
    else:

        # Muestra que el flujo de caja es negativo.
        print("Estado: flujo negativo")

    # Devuelve el saldo calculado para poder reutilizarlo en otros módulos.
    return saldo