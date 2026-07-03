from data_manager import leer_json
from finanzas import calcular_total


RUTA_INGRESOS = "data/ingresos.json"
RUTA_GASTOS = "data/gastos.json"


def mostrar_reporte_general():
    ingresos = leer_json(RUTA_INGRESOS)
    gastos = leer_json(RUTA_GASTOS)

    total_ingresos = calcular_total(ingresos)
    total_gastos = calcular_total(gastos)
    utilidad = total_ingresos - total_gastos

    print("\n===== REPORTE GENERAL =====")
    print("Cantidad de ingresos registrados:", len(ingresos))
    print("Cantidad de gastos registrados:", len(gastos))
    print("Total ingresos: Q", total_ingresos)
    print("Total gastos: Q", total_gastos)
    print("Utilidad actual: Q", utilidad)

    if utilidad > 0:
        print("Estado financiero: Ganancia")
    elif utilidad == 0:
        print("Estado financiero: Punto de equilibrio")
    else:
        print("Estado financiero: Pérdida")


def mostrar_movimientos():
    ingresos = leer_json(RUTA_INGRESOS)
    gastos = leer_json(RUTA_GASTOS)

    print("\n===== INGRESOS =====")

    if len(ingresos) == 0:
        print("No hay ingresos registrados.")
    else:
        for ingreso in ingresos:
            print(ingreso["fecha"], "-", ingreso["descripcion"], "-", ingreso["categoria"], "- Q", ingreso["monto"], "- creado por:", ingreso["creado_por"])

    print("\n===== GASTOS =====")

    if len(gastos) == 0:
        print("No hay gastos registrados.")
    else:
        for gasto in gastos:
            print(gasto["fecha"], "-", gasto["descripcion"], "-", gasto["categoria"], "- Q", gasto["monto"], "- creado por:", gasto["creado_por"])


def total_por_categoria(movimientos):
    categorias = {}

    for movimiento in movimientos:
        categoria = movimiento["categoria"]

        if categoria in categorias:
            categorias[categoria] = categorias[categoria] + movimiento["monto"]
        else:
            categorias[categoria] = movimiento["monto"]

    return categorias


def mostrar_gastos_por_categoria():
    gastos = leer_json(RUTA_GASTOS)
    categorias = total_por_categoria(gastos)

    print("\n===== GASTOS POR CATEGORÍA =====")

    if len(categorias) == 0:
        print("No hay datos para mostrar.")
    else:
        for categoria, total in categorias.items():
            print(categoria, ": Q", total)


def mostrar_ingresos_por_categoria():
    ingresos = leer_json(RUTA_INGRESOS)
    categorias = total_por_categoria(ingresos)

    print("\n===== INGRESOS POR CATEGORÍA =====")

    if len(categorias) == 0:
        print("No hay datos para mostrar.")
    else:
        for categoria, total in categorias.items():
            print(categoria, ": Q", total)


def reporte_por_usuario():
    ingresos = leer_json(RUTA_INGRESOS)
    gastos = leer_json(RUTA_GASTOS)

    usuarios = {}

    for ingreso in ingresos:
        creador = ingreso["creado_por"]

        if creador not in usuarios:
            usuarios[creador] = {"ingresos": 0, "gastos": 0}

        usuarios[creador]["ingresos"] = usuarios[creador]["ingresos"] + ingreso["monto"]

    for gasto in gastos:
        creador = gasto["creado_por"]

        if creador not in usuarios:
            usuarios[creador] = {"ingresos": 0, "gastos": 0}

        usuarios[creador]["gastos"] = usuarios[creador]["gastos"] + gasto["monto"]

    print("\n===== REPORTE POR USUARIO =====")

    if len(usuarios) == 0:
        print("No hay movimientos registrados.")
        return

    for usuario, datos in usuarios.items():
        utilidad = datos["ingresos"] - datos["gastos"]

        print("--------------------------------")
        print("Usuario:", usuario)
        print("Ingresos registrados: Q", datos["ingresos"])
        print("Gastos registrados: Q", datos["gastos"])
        print("Utilidad asociada: Q", utilidad)


def buscar_movimiento():
    ingresos = leer_json(RUTA_INGRESOS)
    gastos = leer_json(RUTA_GASTOS)

    palabra = input("Ingrese una palabra para buscar en la descripción: ").lower()

    print("\n===== RESULTADOS DE BÚSQUEDA =====")

    encontrado = False

    for ingreso in ingresos:
        if palabra in ingreso["descripcion"].lower():
            print("[Ingreso]", ingreso["fecha"], "-", ingreso["descripcion"], "- Q", ingreso["monto"])
            encontrado = True

    for gasto in gastos:
        if palabra in gasto["descripcion"].lower():
            print("[Gasto]", gasto["fecha"], "-", gasto["descripcion"], "- Q", gasto["monto"])
            encontrado = True

    if not encontrado:
        print("No se encontraron movimientos con esa palabra.")