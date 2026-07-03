from data_manager import leer_json
from finanzas import calcular_total
from presupuestos import gasto_real_por_categoria


RUTA_INGRESOS = "data/ingresos.json"
RUTA_GASTOS = "data/gastos.json"
RUTA_PRESUPUESTOS = "data/presupuestos.json"
RUTA_METAS = "data/metas.json"


def alerta_flujo_caja():
    ingresos = leer_json(RUTA_INGRESOS)
    gastos = leer_json(RUTA_GASTOS)

    total_ingresos = calcular_total(ingresos)
    total_gastos = calcular_total(gastos)
    saldo = total_ingresos - total_gastos

    if saldo < 0:
        return "Alerta critica: el flujo de caja esta negativo."

    if saldo == 0:
        return "Alerta: la empresa esta en punto de equilibrio."

    if saldo < 1000:
        return "Alerta preventiva: el saldo disponible es bajo."

    return "Flujo de caja saludable."


def alerta_gastos_altos():
    gastos = leer_json(RUTA_GASTOS)

    if len(gastos) == 0:
        return "No hay gastos registrados para analizar."

    gasto_mayor = gastos[0]

    for gasto in gastos:
        if gasto["monto"] > gasto_mayor["monto"]:
            gasto_mayor = gasto

    if gasto_mayor["monto"] >= 5000:
        return "Alerta: existe un gasto alto de Q" + str(gasto_mayor["monto"]) + " en " + gasto_mayor["categoria"] + "."

    return "No se detectan gastos individuales demasiado altos."


def alerta_presupuestos():
    presupuestos = leer_json(RUTA_PRESUPUESTOS)

    if len(presupuestos) == 0:
        return "No hay presupuestos registrados."

    mensajes = []

    for presupuesto in presupuestos:
        gasto_real = gasto_real_por_categoria(presupuesto["categoria"])

        if gasto_real > presupuesto["monto"]:
            mensajes.append(
                "Presupuesto superado en " + presupuesto["categoria"] +
                ": presupuesto Q" + str(presupuesto["monto"]) +
                ", gasto real Q" + str(gasto_real) + "."
            )

    if len(mensajes) == 0:
        return "Todos los presupuestos estan dentro del limite."

    return mensajes


def mostrar_alertas():
    print("\n===== ALERTAS INTELIGENTES =====")

    print("--------------------------------")
    print(alerta_flujo_caja())

    print("--------------------------------")
    print(alerta_gastos_altos())

    print("--------------------------------")
    resultado_presupuestos = alerta_presupuestos()

    if isinstance(resultado_presupuestos, list):
        for mensaje in resultado_presupuestos:
            print(mensaje)
    else:
        print(resultado_presupuestos)