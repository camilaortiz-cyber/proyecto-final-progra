from data_manager import leer_json, guardar_json
from auditoria import registrar_auditoria
from finanzas import calcular_total


RUTA_METAS = "data/metas.json"
RUTA_INGRESOS = "data/ingresos.json"
RUTA_GASTOS = "data/gastos.json"


def crear_meta(usuario_actual):
    print("\n===== CREAR META FINANCIERA =====")
    print("Tipos de meta:")
    print("1. ventas")
    print("2. ahorro")
    print("3. utilidad")

    tipo = input("Tipo de meta: ").lower()
    descripcion = input("Descripcion de la meta: ")

    try:
        monto = float(input("Monto objetivo: Q"))
    except ValueError:
        print("El monto debe ser numerico.")
        return False

    if tipo not in ["ventas", "ahorro", "utilidad"]:
        print("Tipo de meta invalido.")
        return False

    if descripcion == "" or monto <= 0:
        print("Descripcion y monto valido son obligatorios.")
        return False

    metas = leer_json(RUTA_METAS)

    meta = {
        "tipo": tipo,
        "descripcion": descripcion,
        "monto": monto,
        "creado_por": usuario_actual["usuario"]
    }

    metas.append(meta)
    guardar_json(RUTA_METAS, metas)

    registrar_auditoria(
        usuario_actual,
        "Creacion de meta",
        "Se creo meta de " + tipo + " por Q" + str(monto) + "."
    )

    print("Meta creada correctamente.")
    return True


def calcular_valor_actual_meta(tipo):
    ingresos = leer_json(RUTA_INGRESOS)
    gastos = leer_json(RUTA_GASTOS)

    total_ingresos = calcular_total(ingresos)
    total_gastos = calcular_total(gastos)

    if tipo == "ventas":
        return total_ingresos

    if tipo == "ahorro":
        return total_ingresos - total_gastos

    if tipo == "utilidad":
        return total_ingresos - total_gastos

    return 0


def ver_progreso_metas():
    metas = leer_json(RUTA_METAS)

    print("\n===== PROGRESO DE METAS =====")

    if len(metas) == 0:
        print("No hay metas registradas.")
        return

    for meta in metas:
        actual = calcular_valor_actual_meta(meta["tipo"])
        porcentaje = (actual / meta["monto"]) * 100

        if porcentaje > 100:
            porcentaje = 100

        print("--------------------------------")
        print("Tipo:", meta["tipo"])
        print("Descripcion:", meta["descripcion"])
        print("Objetivo: Q", meta["monto"])
        print("Actual: Q", actual)
        print("Progreso:", round(porcentaje, 2), "%")

        if porcentaje >= 100:
            print("Estado: meta alcanzada.")
        elif porcentaje >= 70:
            print("Estado: muy cerca de alcanzar la meta.")
        elif porcentaje >= 40:
            print("Estado: progreso medio.")
        else:
            print("Estado: falta avanzar.")


def menu_metas(usuario_actual):
    while True:
        print("\n===== MODULO DE METAS =====")
        print("1. Crear meta")
        print("2. Ver progreso de metas")
        print("0. Volver")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            crear_meta(usuario_actual)
        elif opcion == "2":
            ver_progreso_metas()
        elif opcion == "0":
            break
        else:
            print("Opcion invalida.")