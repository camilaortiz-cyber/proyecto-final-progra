from data_manager import leer_json
from finanzas import calcular_total
from reportes import total_por_categoria
from presupuestos import gasto_real_por_categoria
from metas import calcular_valor_actual_meta


RUTA_INGRESOS = "data/ingresos.json"
RUTA_GASTOS = "data/gastos.json"
RUTA_PRESUPUESTOS = "data/presupuestos.json"
RUTA_METAS = "data/metas.json"


def obtener_categoria_mayor(movimientos):
    categorias = total_por_categoria(movimientos)

    if len(categorias) == 0:
        return None

    mayor_categoria = ""
    mayor_monto = 0

    for categoria, monto in categorias.items():
        if monto > mayor_monto:
            mayor_categoria = categoria
            mayor_monto = monto

    return mayor_categoria, mayor_monto


def obtener_categoria_menor(movimientos):
    categorias = total_por_categoria(movimientos)

    if len(categorias) == 0:
        return None

    menor_categoria = ""
    menor_monto = 0
    primera = True

    for categoria, monto in categorias.items():
        if primera:
            menor_categoria = categoria
            menor_monto = monto
            primera = False
        elif monto < menor_monto:
            menor_categoria = categoria
            menor_monto = monto

    return menor_categoria, menor_monto


def usuario_con_mas_movimientos():
    ingresos = leer_json(RUTA_INGRESOS)
    gastos = leer_json(RUTA_GASTOS)

    conteo = {}

    for ingreso in ingresos:
        usuario = ingreso["creado_por"]

        if usuario in conteo:
            conteo[usuario] = conteo[usuario] + 1
        else:
            conteo[usuario] = 1

    for gasto in gastos:
        usuario = gasto["creado_por"]

        if usuario in conteo:
            conteo[usuario] = conteo[usuario] + 1
        else:
            conteo[usuario] = 1

    if len(conteo) == 0:
        return None

    usuario_mayor = ""
    cantidad_mayor = 0

    for usuario, cantidad in conteo.items():
        if cantidad > cantidad_mayor:
            usuario_mayor = usuario
            cantidad_mayor = cantidad

    return usuario_mayor, cantidad_mayor


def presupuesto_mas_riesgoso():
    presupuestos = leer_json(RUTA_PRESUPUESTOS)

    if len(presupuestos) == 0:
        return None

    presupuesto_riesgoso = None
    porcentaje_mayor = 0

    for presupuesto in presupuestos:
        gasto_real = gasto_real_por_categoria(presupuesto["categoria"])

        if presupuesto["monto"] > 0:
            porcentaje = (gasto_real / presupuesto["monto"]) * 100
        else:
            porcentaje = 0

        if presupuesto_riesgoso is None or porcentaje > porcentaje_mayor:
            presupuesto_riesgoso = presupuesto
            porcentaje_mayor = porcentaje

    return presupuesto_riesgoso, porcentaje_mayor


def meta_con_mejor_progreso():
    metas = leer_json(RUTA_METAS)

    if len(metas) == 0:
        return None

    mejor_meta = None
    mejor_porcentaje = 0

    for meta in metas:
        actual = calcular_valor_actual_meta(meta["tipo"])

        if meta["monto"] > 0:
            porcentaje = (actual / meta["monto"]) * 100
        else:
            porcentaje = 0

        if porcentaje > 100:
            porcentaje = 100

        if mejor_meta is None or porcentaje > mejor_porcentaje:
            mejor_meta = meta
            mejor_porcentaje = porcentaje

    return mejor_meta, mejor_porcentaje


def diagnostico_negocio():
    ingresos = leer_json(RUTA_INGRESOS)
    gastos = leer_json(RUTA_GASTOS)

    total_ingresos = calcular_total(ingresos)
    total_gastos = calcular_total(gastos)
    utilidad = total_ingresos - total_gastos

    print("\n===== DIAGNÓSTICO FINANCIERO =====")
    print("Ingresos totales: Q", total_ingresos)
    print("Gastos totales: Q", total_gastos)
    print("Utilidad actual: Q", utilidad)

    if total_ingresos == 0 and total_gastos == 0:
        print("Diagnóstico: todavía no hay suficiente información financiera para analizar.")
        print("Recomendación: registre ingresos y gastos para activar reportes más útiles.")
        return

    if utilidad > 0:
        print("Diagnóstico: la empresa tiene utilidad positiva.")
    elif utilidad == 0:
        print("Diagnóstico: la empresa está en punto de equilibrio.")
    else:
        print("Diagnóstico: la empresa está gastando más de lo que ingresa.")

    gasto_mayor = obtener_categoria_mayor(gastos)

    if gasto_mayor is not None:
        categoria, monto = gasto_mayor
        print("Categoría de gasto más alta:", categoria, "- Q", monto)

    ingreso_mayor = obtener_categoria_mayor(ingresos)

    if ingreso_mayor is not None:
        categoria, monto = ingreso_mayor
        print("Categoría de ingreso más fuerte:", categoria, "- Q", monto)

    riesgo = presupuesto_mas_riesgoso()

    if riesgo is not None:
        presupuesto, porcentaje = riesgo
        print("Presupuesto con más presión:", presupuesto["categoria"], "-", round(porcentaje, 2), "% utilizado")

    mejor_meta = meta_con_mejor_progreso()

    if mejor_meta is not None:
        meta, porcentaje = mejor_meta
        print("Meta con mejor progreso:", meta["descripcion"], "-", round(porcentaje, 2), "%")

    print("\nRecomendación general:")

    if utilidad < 0:
        print("Reducir gastos críticos y revisar categorías con mayor salida de dinero.")
    elif utilidad == 0:
        print("Aumentar ingresos o reducir costos para generar utilidad.")
    else:
        print("Mantener el control de gastos y usar la utilidad para fortalecer metas o reinversión.")


def recomendacion_personalizada():
    ingresos = leer_json(RUTA_INGRESOS)
    gastos = leer_json(RUTA_GASTOS)

    total_ingresos = calcular_total(ingresos)
    total_gastos = calcular_total(gastos)
    utilidad = total_ingresos - total_gastos

    print("\n===== RECOMENDACIÓN INTELIGENTE =====")

    if len(ingresos) == 0 and len(gastos) == 0:
        print("Primero registre movimientos financieros para obtener una recomendación más precisa.")
        return

    gasto_mayor = obtener_categoria_mayor(gastos)

    if utilidad < 0:
        print("La empresa tiene pérdida actualmente.")

        if gasto_mayor is not None:
            categoria, monto = gasto_mayor
            print("El gasto más fuerte está en", categoria, "con Q", monto)
            print("Recomendación: revisar y reducir gastos en esa categoría antes de aumentar nuevos costos.")
        else:
            print("Recomendación: registrar gastos por categoría para detectar el problema principal.")

    elif utilidad == 0:
        print("La empresa está en equilibrio.")
        print("Recomendación: definir una meta de utilidad y revisar oportunidades para aumentar ingresos.")

    else:
        print("La empresa tiene utilidad positiva.")
        print("Recomendación: separar una parte para ahorro, otra para reinversión y otra para cubrir gastos futuros.")

        mejor_meta = meta_con_mejor_progreso()

        if mejor_meta is not None:
            meta, porcentaje = mejor_meta
            print("La meta con mejor avance es:", meta["descripcion"], "con", round(porcentaje, 2), "% de progreso.")


def asistente_financiero():
    while True:
        ingresos = leer_json(RUTA_INGRESOS)
        gastos = leer_json(RUTA_GASTOS)

        total_ingresos = calcular_total(ingresos)
        total_gastos = calcular_total(gastos)
        utilidad = total_ingresos - total_gastos

        print("\n===== IA FINANCIERA SIMULADA =====")
        print("1. ¿En qué gasté más?")
        print("2. ¿Cuál fue mi ingreso más fuerte?")
        print("3. ¿Cuánto he ganado?")
        print("4. ¿Cuál es mi utilidad?")
        print("5. ¿Qué usuario registró más movimientos?")
        print("6. ¿Estoy gastando más de lo que gano?")
        print("7. ¿Qué presupuesto está en más riesgo?")
        print("8. ¿Qué meta va mejor?")
        print("9. Dame una recomendación personalizada")
        print("10. Dame un diagnóstico completo del negocio")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            resultado = obtener_categoria_mayor(gastos)

            if resultado is None:
                print("Todavía no hay gastos registrados.")
            else:
                categoria, monto = resultado
                print("La categoría donde más ha gastado es:", categoria)
                print("Monto total: Q", monto)

        elif opcion == "2":
            resultado = obtener_categoria_mayor(ingresos)

            if resultado is None:
                print("Todavía no hay ingresos registrados.")
            else:
                categoria, monto = resultado
                print("La categoría de ingreso más fuerte es:", categoria)
                print("Monto total: Q", monto)

        elif opcion == "3":
            print("Sus ingresos totales son: Q", total_ingresos)

        elif opcion == "4":
            print("Su utilidad actual es: Q", utilidad)

        elif opcion == "5":
            resultado = usuario_con_mas_movimientos()

            if resultado is None:
                print("Todavía no hay movimientos registrados.")
            else:
                usuario, cantidad = resultado
                print("El usuario con más movimientos registrados es:", usuario)
                print("Cantidad de movimientos:", cantidad)

        elif opcion == "6":
            if total_gastos > total_ingresos:
                print("Sí. Actualmente los gastos son mayores que los ingresos.")
                print("Diferencia negativa: Q", total_gastos - total_ingresos)
            elif total_gastos == total_ingresos:
                print("No exactamente. Está en punto de equilibrio.")
            else:
                print("No. Los ingresos son mayores que los gastos.")
                print("Diferencia positiva: Q", utilidad)

        elif opcion == "7":
            resultado = presupuesto_mas_riesgoso()

            if resultado is None:
                print("No hay presupuestos registrados.")
            else:
                presupuesto, porcentaje = resultado
                print("Presupuesto con más riesgo:", presupuesto["categoria"])
                print("Mes:", presupuesto["mes"])
                print("Porcentaje utilizado:", round(porcentaje, 2), "%")

                if porcentaje > 100:
                    print("Este presupuesto ya fue superado.")
                elif porcentaje >= 80:
                    print("Este presupuesto está cerca de ser superado.")
                else:
                    print("Este presupuesto todavía está bajo control.")

        elif opcion == "8":
            resultado = meta_con_mejor_progreso()

            if resultado is None:
                print("No hay metas registradas.")
            else:
                meta, porcentaje = resultado
                print("La meta con mejor progreso es:", meta["descripcion"])
                print("Tipo:", meta["tipo"])
                print("Progreso:", round(porcentaje, 2), "%")

        elif opcion == "9":
            recomendacion_personalizada()

        elif opcion == "10":
            diagnostico_negocio()

        elif opcion == "0":
            break

        else:
            print("Opción inválida.")