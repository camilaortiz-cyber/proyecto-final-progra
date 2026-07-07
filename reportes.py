# Importa la función para leer datos desde archivos JSON.
from data_manager import leer_json

# Importa la función para calcular el total de ingresos o gastos.
from finanzas import calcular_total


# Define la ruta del archivo donde se almacenan los ingresos.
RUTA_INGRESOS = "data/ingresos.json"

# Define la ruta del archivo donde se almacenan los gastos.
RUTA_GASTOS = "data/gastos.json"


# Muestra un resumen general de ingresos, gastos y utilidad.
def mostrar_reporte_general():

    # Lee la lista de ingresos desde el archivo JSON.
    ingresos = leer_json(RUTA_INGRESOS)

    # Lee la lista de gastos desde el archivo JSON.
    gastos = leer_json(RUTA_GASTOS)

    # Calcula el total de ingresos registrados.
    total_ingresos = calcular_total(ingresos)

    # Calcula el total de gastos registrados.
    total_gastos = calcular_total(gastos)

    # Calcula la utilidad restando los gastos a los ingresos.
    utilidad = total_ingresos - total_gastos

    # Muestra el título del reporte general.
    print("\n===== REPORTE GENERAL =====")

    # Muestra la cantidad de ingresos registrados.
    print("Cantidad de ingresos registrados:", len(ingresos))

    # Muestra la cantidad de gastos registrados.
    print("Cantidad de gastos registrados:", len(gastos))

    # Muestra el total de ingresos.
    print("Total ingresos: Q", total_ingresos)

    # Muestra el total de gastos.
    print("Total gastos: Q", total_gastos)

    # Muestra la utilidad actual.
    print("Utilidad actual: Q", utilidad)

    # Evalúa si existe ganancia.
    if utilidad > 0:
        print("Estado financiero: Ganancia")

    # Evalúa si la empresa está en punto de equilibrio.
    elif utilidad == 0:
        print("Estado financiero: Punto de equilibrio")

    # Si la utilidad es negativa, indica pérdida.
    else:
        print("Estado financiero: Pérdida")


# Muestra todos los ingresos y gastos registrados.
def mostrar_movimientos():

    # Lee la lista de ingresos desde el archivo JSON.
    ingresos = leer_json(RUTA_INGRESOS)

    # Lee la lista de gastos desde el archivo JSON.
    gastos = leer_json(RUTA_GASTOS)

    # Muestra el título de la sección de ingresos.
    print("\n===== INGRESOS =====")

    # Verifica si no hay ingresos registrados.
    if len(ingresos) == 0:

        # Muestra un mensaje si no existen ingresos.
        print("No hay ingresos registrados.")

    # Si existen ingresos, los recorre y los muestra.
    else:
        for ingreso in ingresos:

            # Muestra los datos principales de cada ingreso.
            print(ingreso["fecha"], "-", ingreso["descripcion"], "-", ingreso["categoria"], "- Q", ingreso["monto"], "- creado por:", ingreso["creado_por"])

    # Muestra el título de la sección de gastos.
    print("\n===== GASTOS =====")

    # Verifica si no hay gastos registrados.
    if len(gastos) == 0:

        # Muestra un mensaje si no existen gastos.
        print("No hay gastos registrados.")

    # Si existen gastos, los recorre y los muestra.
    else:
        for gasto in gastos:

            # Muestra los datos principales de cada gasto.
            print(gasto["fecha"], "-", gasto["descripcion"], "-", gasto["categoria"], "- Q", gasto["monto"], "- creado por:", gasto["creado_por"])


# Agrupa movimientos por categoría y suma el total de cada una.
def total_por_categoria(movimientos):

    # Crea un diccionario vacío para almacenar las categorías y sus totales.
    categorias = {}

    # Recorre cada movimiento recibido.
    for movimiento in movimientos:

        # Obtiene la categoría del movimiento actual.
        categoria = movimiento["categoria"]

        # Verifica si la categoría ya existe en el diccionario.
        if categoria in categorias:

            # Si existe, suma el monto actual al total de esa categoría.
            categorias[categoria] = categorias[categoria] + movimiento["monto"]

        # Si la categoría no existe, la crea con el monto actual.
        else:
            categorias[categoria] = movimiento["monto"]

    # Devuelve el diccionario con los totales por categoría.
    return categorias


# Muestra los gastos agrupados por categoría.
def mostrar_gastos_por_categoria():

    # Lee la lista de gastos desde el archivo JSON.
    gastos = leer_json(RUTA_GASTOS)

    # Agrupa los gastos por categoría.
    categorias = total_por_categoria(gastos)

    # Muestra el título de la sección.
    print("\n===== GASTOS POR CATEGORÍA =====")

    # Verifica si no hay datos para mostrar.
    if len(categorias) == 0:

        # Muestra un mensaje si no existen gastos agrupados.
        print("No hay datos para mostrar.")

    # Si hay categorías, muestra cada una con su total.
    else:
        for categoria, total in categorias.items():

            # Muestra la categoría y el total gastado.
            print(categoria, ": Q", total)


# Muestra los ingresos agrupados por categoría.
def mostrar_ingresos_por_categoria():

    # Lee la lista de ingresos desde el archivo JSON.
    ingresos = leer_json(RUTA_INGRESOS)

    # Agrupa los ingresos por categoría.
    categorias = total_por_categoria(ingresos)

    # Muestra el título de la sección.
    print("\n===== INGRESOS POR CATEGORÍA =====")

    # Verifica si no hay datos para mostrar.
    if len(categorias) == 0:

        # Muestra un mensaje si no existen ingresos agrupados.
        print("No hay datos para mostrar.")

    # Si hay categorías, muestra cada una con su total.
    else:
        for categoria, total in categorias.items():

            # Muestra la categoría y el total ingresado.
            print(categoria, ": Q", total)


# Genera un reporte financiero agrupado por usuario creador.
def reporte_por_usuario():

    # Lee la lista de ingresos desde el archivo JSON.
    ingresos = leer_json(RUTA_INGRESOS)

    # Lee la lista de gastos desde el archivo JSON.
    gastos = leer_json(RUTA_GASTOS)

    # Crea un diccionario para almacenar ingresos y gastos por usuario.
    usuarios = {}

    # Recorre cada ingreso registrado.
    for ingreso in ingresos:

        # Obtiene el usuario que creó el ingreso.
        creador = ingreso["creado_por"]

        # Si el usuario no existe en el diccionario, lo inicializa.
        if creador not in usuarios:
            usuarios[creador] = {"ingresos": 0, "gastos": 0}

        # Suma el monto del ingreso al usuario correspondiente.
        usuarios[creador]["ingresos"] = usuarios[creador]["ingresos"] + ingreso["monto"]

    # Recorre cada gasto registrado.
    for gasto in gastos:

        # Obtiene el usuario que creó el gasto.
        creador = gasto["creado_por"]

        # Si el usuario no existe en el diccionario, lo inicializa.
        if creador not in usuarios:
            usuarios[creador] = {"ingresos": 0, "gastos": 0}

        # Suma el monto del gasto al usuario correspondiente.
        usuarios[creador]["gastos"] = usuarios[creador]["gastos"] + gasto["monto"]

    # Muestra el título del reporte por usuario.
    print("\n===== REPORTE POR USUARIO =====")

    # Verifica si no hay movimientos registrados.
    if len(usuarios) == 0:

        # Muestra un mensaje cuando no hay datos.
        print("No hay movimientos registrados.")

        # Termina la función para evitar recorrer datos vacíos.
        return

    # Recorre cada usuario con sus datos financieros.
    for usuario, datos in usuarios.items():

        # Calcula la utilidad asociada al usuario.
        utilidad = datos["ingresos"] - datos["gastos"]

        # Imprime una línea separadora.
        print("--------------------------------")

        # Muestra el nombre del usuario.
        print("Usuario:", usuario)

        # Muestra los ingresos registrados por ese usuario.
        print("Ingresos registrados: Q", datos["ingresos"])

        # Muestra los gastos registrados por ese usuario.
        print("Gastos registrados: Q", datos["gastos"])

        # Muestra la utilidad asociada al usuario.
        print("Utilidad asociada: Q", utilidad)


# Permite buscar movimientos por una palabra dentro de la descripción.
def buscar_movimiento():

    # Lee la lista de ingresos desde el archivo JSON.
    ingresos = leer_json(RUTA_INGRESOS)

    # Lee la lista de gastos desde el archivo JSON.
    gastos = leer_json(RUTA_GASTOS)

    # Solicita la palabra que se desea buscar y la convierte a minúsculas.
    palabra = input("Ingrese una palabra para buscar en la descripción: ").lower()

    # Muestra el título de los resultados de búsqueda.
    print("\n===== RESULTADOS DE BÚSQUEDA =====")

    # Variable para saber si se encontró al menos un resultado.
    encontrado = False

    # Recorre cada ingreso registrado.
    for ingreso in ingresos:

        # Verifica si la palabra está dentro de la descripción del ingreso.
        if palabra in ingreso["descripcion"].lower():

            # Muestra el ingreso encontrado.
            print("[Ingreso]", ingreso["fecha"], "-", ingreso["descripcion"], "- Q", ingreso["monto"])

            # Cambia el estado para indicar que sí hubo resultados.
            encontrado = True

    # Recorre cada gasto registrado.
    for gasto in gastos:

        # Verifica si la palabra está dentro de la descripción del gasto.
        if palabra in gasto["descripcion"].lower():

            # Muestra el gasto encontrado.
            print("[Gasto]", gasto["fecha"], "-", gasto["descripcion"], "- Q", gasto["monto"])

            # Cambia el estado para indicar que sí hubo resultados.
            encontrado = True

    # Verifica si no se encontró ningún movimiento.
    if not encontrado:

        # Muestra un mensaje indicando que no hubo coincidencias.
        print("No se encontraron movimientos con esa palabra.")