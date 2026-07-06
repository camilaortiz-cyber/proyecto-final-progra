# Importa las funciones para leer y guardar datos en archivos JSON.
from data_manager import leer_json, guardar_json

# Importa la función para registrar acciones importantes en el historial de auditoría.
from auditoria import registrar_auditoria


# Define la ruta del archivo donde se almacenan los presupuestos.
RUTA_PRESUPUESTOS = "data/presupuestos.json"

# Define la ruta del archivo donde se almacenan los gastos.
RUTA_GASTOS = "data/gastos.json"


# Permite crear un nuevo presupuesto dentro del sistema.
def crear_presupuesto(usuario_actual):

    # Muestra el título de la sección para crear presupuestos.
    print("\n===== CREAR PRESUPUESTO =====")

    # Solicita la categoría a la que pertenece el presupuesto.
    categoria = input("Categoria del presupuesto: ")

    # Solicita el mes al que corresponde el presupuesto.
    mes = input("Mes del presupuesto: ")

    # Intenta convertir el monto ingresado a número decimal.
    try:
        monto = float(input("Monto presupuestado: Q"))

    # Captura el error si el usuario ingresa un valor no numérico.
    except ValueError:

        # Muestra un mensaje indicando que el monto debe ser numérico.
        print("El monto debe ser numerico.")

        # Devuelve False porque no se pudo crear el presupuesto.
        return False

    # Valida que la categoría, el mes y el monto sean correctos.
    if categoria == "" or mes == "" or monto <= 0:

        # Muestra un mensaje si faltan datos obligatorios.
        print("Categoria, mes y monto valido son obligatorios.")

        # Devuelve False porque los datos ingresados no son válidos.
        return False

    # Lee la lista actual de presupuestos desde el archivo JSON.
    presupuestos = leer_json(RUTA_PRESUPUESTOS)

    # Crea un diccionario con la información del nuevo presupuesto.
    presupuesto = {
        # Guarda la categoría del presupuesto.
        "categoria": categoria,

        # Guarda el mes del presupuesto.
        "mes": mes,

        # Guarda el monto asignado al presupuesto.
        "monto": monto,

        # Guarda el usuario que creó el presupuesto.
        "creado_por": usuario_actual["usuario"]
    }

    # Agrega el nuevo presupuesto a la lista de presupuestos.
    presupuestos.append(presupuesto)

    # Guarda la lista actualizada de presupuestos en el archivo JSON.
    guardar_json(RUTA_PRESUPUESTOS, presupuestos)

    # Registra en auditoría la creación del presupuesto.
    registrar_auditoria(
        usuario_actual,
        "Creacion de presupuesto",
        "Se creo presupuesto de Q" + str(monto) + " para " + categoria + "."
    )

    # Muestra un mensaje confirmando que el presupuesto fue creado correctamente.
    print("Presupuesto creado correctamente.")

    # Devuelve True para indicar que el presupuesto fue registrado exitosamente.
    return True


# Muestra todos los presupuestos registrados en el sistema.
def listar_presupuestos():

    # Lee la lista de presupuestos desde el archivo JSON.
    presupuestos = leer_json(RUTA_PRESUPUESTOS)

    # Muestra el título de la sección de presupuestos.
    print("\n===== PRESUPUESTOS =====")

    # Verifica si no existen presupuestos registrados.
    if len(presupuestos) == 0:

        # Muestra un mensaje cuando la lista de presupuestos está vacía.
        print("No hay presupuestos registrados.")

        # Termina la función para evitar recorrer una lista vacía.
        return

    # Inicializa un contador para numerar los presupuestos mostrados.
    contador = 1

    # Recorre cada presupuesto registrado.
    for presupuesto in presupuestos:

        # Imprime una línea separadora para ordenar la información visualmente.
        print("--------------------------------")

        # Muestra el número de presupuesto y su categoría.
        print(contador, ".", presupuesto["categoria"])

        # Muestra el mes del presupuesto.
        print("Mes:", presupuesto["mes"])

        # Muestra el monto del presupuesto.
        print("Monto: Q", presupuesto["monto"])

        # Muestra el usuario que creó el presupuesto.
        print("Creado por:", presupuesto["creado_por"])

        # Aumenta el contador para el siguiente presupuesto.
        contador = contador + 1


# Calcula el total de gastos reales registrados para una categoría específica.
def gasto_real_por_categoria(categoria):

    # Lee la lista de gastos desde el archivo JSON.
    gastos = leer_json(RUTA_GASTOS)

    # Inicializa el acumulador del gasto real en cero.
    total = 0

    # Recorre cada gasto registrado.
    for gasto in gastos:

        # Compara la categoría del gasto con la categoría recibida, sin importar mayúsculas.
        if gasto["categoria"].lower() == categoria.lower():

            # Suma el monto del gasto si pertenece a la categoría indicada.
            total = total + gasto["monto"]

    # Devuelve el total de gastos reales de la categoría.
    return total


# Compara cada presupuesto contra el gasto real registrado en su categoría.
def comparar_presupuestos():

    # Lee la lista de presupuestos desde el archivo JSON.
    presupuestos = leer_json(RUTA_PRESUPUESTOS)

    # Muestra el título de la sección de comparación.
    print("\n===== PRESUPUESTO VS REALIDAD =====")

    # Verifica si no hay presupuestos registrados.
    if len(presupuestos) == 0:

        # Muestra un mensaje cuando no hay presupuestos para comparar.
        print("No hay presupuestos registrados.")

        # Termina la función porque no hay datos para analizar.
        return

    # Recorre cada presupuesto registrado.
    for presupuesto in presupuestos:

        # Calcula el gasto real de la categoría del presupuesto.
        gasto_real = gasto_real_por_categoria(presupuesto["categoria"])

        # Calcula la diferencia entre el presupuesto asignado y el gasto real.
        diferencia = presupuesto["monto"] - gasto_real

        # Imprime una línea separadora para ordenar cada comparación.
        print("--------------------------------")

        # Muestra la categoría del presupuesto.
        print("Categoria:", presupuesto["categoria"])

        # Muestra el mes del presupuesto.
        print("Mes:", presupuesto["mes"])

        # Muestra el monto presupuestado.
        print("Presupuesto: Q", presupuesto["monto"])

        # Muestra el gasto real registrado.
        print("Gasto real: Q", gasto_real)

        # Muestra la diferencia entre presupuesto y gasto real.
        print("Diferencia: Q", diferencia)

        # Evalúa si el gasto real superó el presupuesto.
        if diferencia < 0:
            print("Alerta: se supero el presupuesto.")

        # Evalúa si el presupuesto fue utilizado exactamente.
        elif diferencia == 0:
            print("Estado: presupuesto utilizado exactamente.")

        # Indica que el gasto está por debajo del presupuesto.
        else:
            print("Estado: dentro del presupuesto.")


# Muestra el menú principal del módulo de presupuestos.
def menu_presupuestos(usuario_actual):

    # Mantiene el menú activo hasta que el usuario decida volver.
    while True:

        # Muestra el título del módulo de presupuestos.
        print("\n===== MODULO DE PRESUPUESTOS =====")

        # Muestra la opción para crear un presupuesto.
        print("1. Crear presupuesto")

        # Muestra la opción para listar presupuestos.
        print("2. Listar presupuestos")

        # Muestra la opción para comparar presupuesto contra gasto real.
        print("3. Comparar presupuesto vs realidad")

        # Muestra la opción para regresar al menú anterior.
        print("0. Volver")

        # Solicita al usuario seleccionar una opción.
        opcion = input("Seleccione una opcion: ")

        # Ejecuta la creación de presupuesto si el usuario selecciona la opción 1.
        if opcion == "1":
            crear_presupuesto(usuario_actual)

        # Ejecuta el listado de presupuestos si el usuario selecciona la opción 2.
        elif opcion == "2":
            listar_presupuestos()

        # Ejecuta la comparación de presupuestos si el usuario selecciona la opción 3.
        elif opcion == "3":
            comparar_presupuestos()

        # Sale del menú si el usuario selecciona la opción 0.
        elif opcion == "0":
            break

        # Muestra error si el usuario ingresa una opción no válida.
        else:
            print("Opcion invalida.")