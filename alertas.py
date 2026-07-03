from data_manager import leer_json
from finanzas import calcular_total
from presupuestos import gasto_real_por_categoria
from metas import calcular_valor_actual_meta


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
        return "Alerta crítica: el flujo de caja está negativo. Revise gastos inmediatamente."

    if saldo == 0:
        return "Alerta: la empresa está en punto de equilibrio. No hay margen de ganancia."

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

    if gasto_mayor["monto"] >= 1000:
        return "Aviso: el gasto más alto registrado es de Q" + str(gasto_mayor["monto"]) + " en " + gasto_mayor["categoria"] + "."

    return "No se detectan gastos individuales demasiado altos."


def alerta_presupuestos():
    presupuestos = leer_json(RUTA_PRESUPUESTOS)

    if len(presupuestos) == 0:
        return ["No hay presupuestos registrados."]

    mensajes = []

    for presupuesto in presupuestos:
        gasto_real = gasto_real_por_categoria(presupuesto["categoria"])

        if presupuesto["monto"] > 0:
            porcentaje = (gasto_real / presupuesto["monto"]) * 100
        else:
            porcentaje = 0

        if porcentaje > 100:
            mensajes.append(
                "Presupuesto superado en " + presupuesto["categoria"] +
                ": " + str(round(porcentaje, 2)) + "% utilizado."
            )
        elif porcentaje >= 80:
            mensajes.append(
                "Presupuesto en riesgo en " + presupuesto["categoria"] +
                ": " + str(round(porcentaje, 2)) + "% utilizado."
            )

    if len(mensajes) == 0:
        mensajes.append("Todos los presupuestos están dentro del límite.")

    return mensajes


def alerta_metas():
    metas = leer_json(RUTA_METAS)

    if len(metas) == 0:
        return ["No hay metas registradas."]

    mensajes = []

    for meta in metas:
        actual = calcular_valor_actual_meta(meta["tipo"])

        if meta["monto"] > 0:
            porcentaje = (actual / meta["monto"]) * 100
        else:
            porcentaje = 0

        if porcentaje >= 100:
            mensajes.append("Meta alcanzada: " + meta["descripcion"] + ".")
        elif porcentaje < 25:
            mensajes.append(
                "Meta con bajo progreso: " + meta["descripcion"] +
                " lleva solo " + str(round(porcentaje, 2)) + "%."
            )
        elif porcentaje >= 75:
            mensajes.append(
                "Meta cerca de cumplirse: " + meta["descripcion"] +
                " lleva " + str(round(porcentaje, 2)) + "%."
            )

    if len(mensajes) == 0:
        mensajes.append("Las metas avanzan de forma estable.")

    return mensajes


def alerta_actividad_financiera():
    ingresos = leer_json(RUTA_INGRESOS)
    gastos = leer_json(RUTA_GASTOS)

    total_movimientos = len(ingresos) + len(gastos)

    if total_movimientos == 0:
        return "No hay actividad financiera registrada. Agregue ingresos y gastos para generar análisis."

    if total_movimientos < 3:
        return "Hay poca actividad registrada. Los reportes serán más útiles con más movimientos."

    return "La actividad financiera registrada es suficiente para análisis básicos."


def mostrar_alertas():
    print("\n===== ALERTAS INTELIGENTES =====")

    print("--------------------------------")
    print(alerta_actividad_financiera())

    print("--------------------------------")
    print(alerta_flujo_caja())

    print("--------------------------------")
    print(alerta_gastos_altos())

    print("--------------------------------")
    print("Presupuestos:")
    mensajes_presupuestos = alerta_presupuestos()

    for mensaje in mensajes_presupuestos:
        print("-", mensaje)

    print("--------------------------------")
    print("Metas:")
    mensajes_metas = alerta_metas()

    for mensaje in mensajes_metas:
        print("-", mensaje)