from datetime import datetime
from data_manager import leer_json, guardar_json


RUTA_INGRESOS = "data/ingresos.json"
RUTA_GASTOS = "data/gastos.json"


def pedir_monto():
    try:
        monto = float(input("Monto: Q"))
        if monto <= 0:
            print("El monto debe ser mayor a cero.")
            return None
        return monto
    except ValueError:
        print("El monto debe ser un número válido.")
        return None


def registrar_ingreso(usuario):
    print("\n===== REGISTRAR INGRESO =====")

    descripcion = input("Descripción del ingreso: ")
    categoria = input("Categoría: ")
    monto = pedir_monto()

    if monto is None:
        return False

    ingreso = {
        "descripcion": descripcion,
        "categoria": categoria,
        "monto": monto,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "creado_por": usuario["usuario"]
    }

    ingresos = leer_json(RUTA_INGRESOS)
    ingresos.append(ingreso)
    guardar_json(RUTA_INGRESOS, ingresos)

    print("Ingreso registrado correctamente.")
    return True


def registrar_gasto(usuario):
    print("\n===== REGISTRAR GASTO =====")

    descripcion = input("Descripción del gasto: ")
    categoria = input("Categoría: ")
    monto = pedir_monto()

    if monto is None:
        return False

    gasto = {
        "descripcion": descripcion,
        "categoria": categoria,
        "monto": monto,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "creado_por": usuario["usuario"]
    }

    gastos = leer_json(RUTA_GASTOS)
    gastos.append(gasto)
    guardar_json(RUTA_GASTOS, gastos)

    print("Gasto registrado correctamente.")
    return True


def calcular_total(lista_movimientos):
    total = 0

    for movimiento in lista_movimientos:
        total = total + movimiento["monto"]

    return total


def mostrar_flujo_caja():
    ingresos = leer_json(RUTA_INGRESOS)
    gastos = leer_json(RUTA_GASTOS)

    total_ingresos = calcular_total(ingresos)
    total_gastos = calcular_total(gastos)
    saldo = total_ingresos - total_gastos

    print("\n===== FLUJO DE CAJA =====")
    print("Total de ingresos: Q", total_ingresos)
    print("Total de gastos: Q", total_gastos)
    print("Saldo disponible: Q", saldo)

    if saldo > 0:
        print("Estado: flujo positivo")
    elif saldo == 0:
        print("Estado: punto de equilibrio")
    else:
        print("Estado: flujo negativo")

    return saldo