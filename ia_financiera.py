# Importa la función para leer datos desde archivos JSON.
from data_manager import leer_json

# Importa la función para calcular el total de una lista de ingresos o gastos.
from finanzas import calcular_total

# Importa la función que agrupa y suma movimientos por categoría.
from reportes import total_por_categoria

# Importa la función que calcula cuánto se ha gastado realmente en una categoría.
from presupuestos import gasto_real_por_categoria

# Importa la función que calcula el avance actual de una meta financiera.
from metas import calcular_valor_actual_meta


# Define la ruta del archivo donde se guardan los ingresos.
RUTA_INGRESOS = "data/ingresos.json"

# Define la ruta del archivo donde se guardan los gastos.
RUTA_GASTOS = "data/gastos.json"

# Define la ruta del archivo donde se guardan los presupuestos.
RUTA_PRESUPUESTOS = "data/presupuestos.json"

# Define la ruta del archivo donde se guardan las metas financieras.
RUTA_METAS = "data/metas.json"


# Obtiene la categoría con el monto total más alto dentro de una lista de movimientos.
def obtener_categoria_mayor(movimientos):

    # Agrupa los movimientos por categoría y calcula el total de cada una.
    categorias = total_por_categoria(movimientos)

    # Verifica si no hay categorías disponibles para analizar.
    if len(categorias) == 0:

        # Devuelve None si no existen datos suficientes.
        return None

    # Inicializa la variable donde se guardará la categoría con mayor monto.
    mayor_categoria = ""

    # Inicializa el monto mayor en cero.
    mayor_monto = 0

    # Recorre cada categoría con su monto total.
    for categoria, monto in categorias.items():

        # Verifica si el monto actual es mayor al monto más alto encontrado.
        if monto > mayor_monto:

            # Guarda la categoría con el monto más alto.
            mayor_categoria = categoria

            # Guarda el nuevo monto mayor.
            mayor_monto = monto

    # Devuelve la categoría con mayor movimiento y su monto total.
    return mayor_categoria, mayor_monto


# Obtiene la categoría con el monto total más bajo dentro de una lista de movimientos.
def obtener_categoria_menor(movimientos):

    # Agrupa los movimientos por categoría y calcula el total de cada una.
    categorias = total_por_categoria(movimientos)

    # Verifica si no hay categorías disponibles para analizar.
    if len(categorias) == 0:

        # Devuelve None si no existen datos suficientes.
        return None

    # Inicializa la variable donde se guardará la categoría con menor monto.
    menor_categoria = ""

    # Inicializa el monto menor en cero.
    menor_monto = 0

    # Variable de control para identificar la primera categoría recorrida.
    primera = True

    # Recorre cada categoría con su monto total.
    for categoria, monto in categorias.items():

        # Si es la primera categoría, se toma como referencia inicial.
        if primera:

            # Guarda la primera categoría como menor categoría inicial.
            menor_categoria = categoria

            # Guarda el primer monto como menor monto inicial.
            menor_monto = monto

            # Cambia la variable para indicar que ya se tomó la primera referencia.
            primera = False

        # Compara si el monto actual es menor al menor monto encontrado.
        elif monto < menor_monto:

            # Actualiza la categoría menor.
            menor_categoria = categoria

            # Actualiza el monto menor.
            menor_monto = monto

    # Devuelve la categoría con menor movimiento y su monto total.
    return menor_categoria, menor_monto


# Identifica qué usuario ha registrado más movimientos financieros.
def usuario_con_mas_movimientos():

    # Lee los ingresos registrados desde el archivo JSON.
    ingresos = leer_json(RUTA_INGRESOS)

    # Lee los gastos registrados desde el archivo JSON.
    gastos = leer_json(RUTA_GASTOS)

    # Crea un diccionario para contar movimientos por usuario.
    conteo = {}

    # Recorre todos los ingresos registrados.
    for ingreso in ingresos:

        # Obtiene el usuario que creó el ingreso.
        usuario = ingreso["creado_por"]

        # Si el usuario ya existe en el conteo, aumenta su cantidad.
        if usuario in conteo:
            conteo[usuario] = conteo[usuario] + 1

        # Si el usuario no existe, lo agrega con valor inicial de uno.
        else:
            conteo[usuario] = 1

    # Recorre todos los gastos registrados.
    for gasto in gastos:

        # Obtiene el usuario que creó el gasto.
        usuario = gasto["creado_por"]

        # Si el usuario ya existe en el conteo, aumenta su cantidad.
        if usuario in conteo:
            conteo[usuario] = conteo[usuario] + 1

        # Si el usuario no existe, lo agrega con valor inicial de uno.
        else:
            conteo[usuario] = 1

    # Verifica si no existe ningún movimiento registrado por usuarios.
    if len(conteo) == 0:

        # Devuelve None cuando no hay movimientos para analizar.
        return None

    # Inicializa la variable del usuario con más movimientos.
    usuario_mayor = ""

    # Inicializa la cantidad mayor en cero.
    cantidad_mayor = 0

    # Recorre cada usuario con su cantidad de movimientos.
    for usuario, cantidad in conteo.items():

        # Verifica si la cantidad actual supera la mayor cantidad encontrada.
        if cantidad > cantidad_mayor:

            # Guarda el usuario con más movimientos.
            usuario_mayor = usuario

            # Guarda la nueva cantidad mayor.
            cantidad_mayor = cantidad

    # Devuelve el usuario con más movimientos y la cantidad registrada.
    return usuario_mayor, cantidad_mayor


# Detecta cuál presupuesto tiene mayor porcentaje de uso.
def presupuesto_mas_riesgoso():

    # Lee los presupuestos guardados desde el archivo JSON.
    presupuestos = leer_json(RUTA_PRESUPUESTOS)

    # Verifica si no hay presupuestos registrados.
    if len(presupuestos) == 0:

        # Devuelve None si no hay presupuestos para evaluar.
        return None

    # Inicializa la variable donde se guardará el presupuesto con más riesgo.
    presupuesto_riesgoso = None

    # Inicializa el mayor porcentaje utilizado.
    porcentaje_mayor = 0

    # Recorre cada presupuesto registrado.
    for presupuesto in presupuestos:

        # Calcula el gasto real acumulado para la categoría del presupuesto.
        gasto_real = gasto_real_por_categoria(presupuesto["categoria"])

        # Verifica que el presupuesto tenga un monto mayor a cero.
        if presupuesto["monto"] > 0:

            # Calcula el porcentaje utilizado del presupuesto.
            porcentaje = (gasto_real / presupuesto["monto"]) * 100

        # Si el monto es cero o inválido, asigna porcentaje cero.
        else:
            porcentaje = 0

        # Verifica si es el primer presupuesto o si tiene un porcentaje mayor al anterior.
        if presupuesto_riesgoso is None or porcentaje > porcentaje_mayor:

            # Guarda el presupuesto más riesgoso encontrado.
            presupuesto_riesgoso = presupuesto

            # Guarda el porcentaje más alto encontrado.
            porcentaje_mayor = porcentaje

    # Devuelve el presupuesto con mayor uso y su porcentaje.
    return presupuesto_riesgoso, porcentaje_mayor


# Identifica la meta financiera con mejor porcentaje de avance.
def meta_con_mejor_progreso():

    # Lee las metas registradas desde el archivo JSON.
    metas = leer_json(RUTA_METAS)

    # Verifica si no hay metas registradas.
    if len(metas) == 0:

        # Devuelve None si no hay metas para analizar.
        return None

    # Inicializa la variable donde se guardará la meta con mejor progreso.
    mejor_meta = None

    # Inicializa el mejor porcentaje encontrado.
    mejor_porcentaje = 0

    # Recorre cada meta registrada.
    for meta in metas:

        # Calcula el valor actual acumulado de la meta según su tipo.
        actual = calcular_valor_actual_meta(meta["tipo"])

        # Verifica que la meta tenga un monto objetivo mayor a cero.
        if meta["monto"] > 0:

            # Calcula el porcentaje de avance de la meta.
            porcentaje = (actual / meta["monto"]) * 100

        # Si el monto objetivo no es válido, asigna porcentaje cero.
        else:
            porcentaje = 0

        # Limita el porcentaje máximo a 100 para no mostrar avances mayores al total.
        if porcentaje > 100:
            porcentaje = 100

        # Verifica si es la primera meta o si tiene mejor progreso que las anteriores.
        if mejor_meta is None or porcentaje > mejor_porcentaje:

            # Guarda la meta con mejor progreso.
            mejor_meta = meta

            # Guarda el mejor porcentaje encontrado.
            mejor_porcentaje = porcentaje

    # Devuelve la meta con mejor avance y su porcentaje.
    return mejor_meta, mejor_porcentaje


# Genera un diagnóstico financiero general del negocio.
def diagnostico_negocio():

    # Lee los ingresos registrados desde el archivo JSON.
    ingresos = leer_json(RUTA_INGRESOS)

    # Lee los gastos registrados desde el archivo JSON.
    gastos = leer_json(RUTA_GASTOS)

    # Calcula el total de ingresos.
    total_ingresos = calcular_total(ingresos)

    # Calcula el total de gastos.
    total_gastos = calcular_total(gastos)

    # Calcula la utilidad restando gastos a ingresos.
    utilidad = total_ingresos - total_gastos

    # Muestra el título del diagnóstico financiero.
    print("\n===== DIAGNÓSTICO FINANCIERO =====")

    # Muestra los ingresos totales del negocio.
    print("Ingresos totales: Q", total_ingresos)

    # Muestra los gastos totales del negocio.
    print("Gastos totales: Q", total_gastos)

    # Muestra la utilidad actual del negocio.
    print("Utilidad actual: Q", utilidad)

    # Verifica si no hay ingresos ni gastos registrados.
    if total_ingresos == 0 and total_gastos == 0:

        # Indica que no hay suficiente información financiera.
        print("Diagnóstico: todavía no hay suficiente información financiera para analizar.")

        # Recomienda registrar movimientos para generar mejores reportes.
        print("Recomendación: registre ingresos y gastos para activar reportes más útiles.")

        # Termina la función porque no hay más datos que analizar.
        return

    # Evalúa si la utilidad es positiva.
    if utilidad > 0:

        # Muestra que la empresa está generando ganancia.
        print("Diagnóstico: la empresa tiene utilidad positiva.")

    # Evalúa si la utilidad es igual a cero.
    elif utilidad == 0:

        # Muestra que la empresa está en punto de equilibrio.
        print("Diagnóstico: la empresa está en punto de equilibrio.")

    # Si la utilidad es negativa, indica que los gastos superan ingresos.
    else:

        # Muestra que la empresa está gastando más de lo que ingresa.
        print("Diagnóstico: la empresa está gastando más de lo que ingresa.")

    # Obtiene la categoría de gasto con monto más alto.
    gasto_mayor = obtener_categoria_mayor(gastos)

    # Verifica si existe una categoría de gasto para mostrar.
    if gasto_mayor is not None:

        # Separa la categoría y el monto devueltos por la función.
        categoria, monto = gasto_mayor

        # Muestra la categoría de gasto más alta.
        print("Categoría de gasto más alta:", categoria, "- Q", monto)

    # Obtiene la categoría de ingreso con monto más alto.
    ingreso_mayor = obtener_categoria_mayor(ingresos)

    # Verifica si existe una categoría de ingreso para mostrar.
    if ingreso_mayor is not None:

        # Separa la categoría y el monto devueltos por la función.
        categoria, monto = ingreso_mayor

        # Muestra la categoría de ingreso más fuerte.
        print("Categoría de ingreso más fuerte:", categoria, "- Q", monto)

    # Obtiene el presupuesto con mayor porcentaje de uso.
    riesgo = presupuesto_mas_riesgoso()

    # Verifica si existe un presupuesto para analizar.
    if riesgo is not None:

        # Separa el presupuesto y el porcentaje devueltos por la función.
        presupuesto, porcentaje = riesgo

        # Muestra el presupuesto con mayor presión financiera.
        print("Presupuesto con más presión:", presupuesto["categoria"], "-", round(porcentaje, 2), "% utilizado")

    # Obtiene la meta financiera con mejor progreso.
    mejor_meta = meta_con_mejor_progreso()

    # Verifica si existe una meta para mostrar.
    if mejor_meta is not None:

        # Separa la meta y el porcentaje devueltos por la función.
        meta, porcentaje = mejor_meta

        # Muestra la meta con mejor avance.
        print("Meta con mejor progreso:", meta["descripcion"], "-", round(porcentaje, 2), "%")

    # Muestra el título de la recomendación general.
    print("\nRecomendación general:")

    # Si hay pérdida, recomienda reducir gastos.
    if utilidad < 0:
        print("Reducir gastos críticos y revisar categorías con mayor salida de dinero.")

    # Si está en equilibrio, recomienda aumentar ingresos o reducir costos.
    elif utilidad == 0:
        print("Aumentar ingresos o reducir costos para generar utilidad.")

    # Si hay utilidad positiva, recomienda controlar gastos y reinvertir.
    else:
        print("Mantener el control de gastos y usar la utilidad para fortalecer metas o reinversión.")


# Genera una recomendación financiera personalizada según la situación actual.
def recomendacion_personalizada():

    # Lee los ingresos registrados desde el archivo JSON.
    ingresos = leer_json(RUTA_INGRESOS)

    # Lee los gastos registrados desde el archivo JSON.
    gastos = leer_json(RUTA_GASTOS)

    # Calcula el total de ingresos.
    total_ingresos = calcular_total(ingresos)

    # Calcula el total de gastos.
    total_gastos = calcular_total(gastos)

    # Calcula la utilidad actual.
    utilidad = total_ingresos - total_gastos

    # Muestra el título de la recomendación inteligente.
    print("\n===== RECOMENDACIÓN INTELIGENTE =====")

    # Verifica si no hay movimientos financieros registrados.
    if len(ingresos) == 0 and len(gastos) == 0:

        # Solicita registrar movimientos antes de generar una recomendación.
        print("Primero registre movimientos financieros para obtener una recomendación más precisa.")

        # Termina la función porque no hay datos suficientes.
        return

    # Obtiene la categoría de gasto con mayor monto.
    gasto_mayor = obtener_categoria_mayor(gastos)

    # Verifica si la empresa tiene pérdida.
    if utilidad < 0:

        # Muestra que actualmente la empresa tiene pérdida.
        print("La empresa tiene pérdida actualmente.")

        # Verifica si hay una categoría de gasto principal.
        if gasto_mayor is not None:

            # Separa la categoría y el monto del gasto mayor.
            categoria, monto = gasto_mayor

            # Muestra dónde se concentra el gasto más fuerte.
            print("El gasto más fuerte está en", categoria, "con Q", monto)

            # Da una recomendación enfocada en reducir esa categoría de gasto.
            print("Recomendación: revisar y reducir gastos en esa categoría antes de aumentar nuevos costos.")

        # Si no hay gastos categorizados, recomienda registrar más datos.
        else:
            print("Recomendación: registrar gastos por categoría para detectar el problema principal.")

    # Verifica si la empresa está en punto de equilibrio.
    elif utilidad == 0:

        # Muestra que la empresa no tiene pérdida ni ganancia.
        print("La empresa está en equilibrio.")

        # Recomienda definir meta de utilidad y aumentar ingresos.
        print("Recomendación: definir una meta de utilidad y revisar oportunidades para aumentar ingresos.")

    # Si la utilidad es positiva, genera recomendación de distribución.
    else:

        # Muestra que la empresa tiene utilidad positiva.
        print("La empresa tiene utilidad positiva.")

        # Recomienda dividir la utilidad entre ahorro, reinversión y gastos futuros.
        print("Recomendación: separar una parte para ahorro, otra para reinversión y otra para cubrir gastos futuros.")

        # Obtiene la meta con mejor progreso.
        mejor_meta = meta_con_mejor_progreso()

        # Verifica si existe una meta con progreso.
        if mejor_meta is not None:

            # Separa la meta y el porcentaje.
            meta, porcentaje = mejor_meta

            # Muestra cuál meta tiene mejor avance.
            print("La meta con mejor avance es:", meta["descripcion"], "con", round(porcentaje, 2), "% de progreso.")


# Muestra el menú interactivo de la IA financiera simulada.
def asistente_financiero():

    # Mantiene el menú activo hasta que el usuario decida volver.
    while True:

        # Lee los ingresos registrados.
        ingresos = leer_json(RUTA_INGRESOS)

        # Lee los gastos registrados.
        gastos = leer_json(RUTA_GASTOS)

        # Calcula el total de ingresos.
        total_ingresos = calcular_total(ingresos)

        # Calcula el total de gastos.
        total_gastos = calcular_total(gastos)

        # Calcula la utilidad actual.
        utilidad = total_ingresos - total_gastos

        # Muestra el título del asistente financiero.
        print("\n===== IA FINANCIERA SIMULADA =====")

        # Opción para consultar la categoría con más gastos.
        print("1. ¿En qué gasté más?")

        # Opción para consultar la categoría con mayor ingreso.
        print("2. ¿Cuál fue mi ingreso más fuerte?")

        # Opción para consultar ingresos totales.
        print("3. ¿Cuánto he ganado?")

        # Opción para consultar la utilidad actual.
        print("4. ¿Cuál es mi utilidad?")

        # Opción para consultar qué usuario registró más movimientos.
        print("5. ¿Qué usuario registró más movimientos?")

        # Opción para comparar ingresos contra gastos.
        print("6. ¿Estoy gastando más de lo que gano?")

        # Opción para revisar el presupuesto con más riesgo.
        print("7. ¿Qué presupuesto está en más riesgo?")

        # Opción para revisar la meta con mejor progreso.
        print("8. ¿Qué meta va mejor?")

        # Opción para obtener una recomendación personalizada.
        print("9. Dame una recomendación personalizada")

        # Opción para generar un diagnóstico completo del negocio.
        print("10. Dame un diagnóstico completo del negocio")

        # Opción para volver al menú anterior.
        print("0. Volver")

        # Solicita al usuario una opción del menú.
        opcion = input("Seleccione una opción: ")

        # Opción 1: analiza la categoría donde más se ha gastado.
        if opcion == "1":

            # Obtiene la categoría de gasto con mayor monto.
            resultado = obtener_categoria_mayor(gastos)

            # Verifica si todavía no hay gastos registrados.
            if resultado is None:
                print("Todavía no hay gastos registrados.")

            # Si hay datos, muestra la categoría y el monto.
            else:
                categoria, monto = resultado
                print("La categoría donde más ha gastado es:", categoria)
                print("Monto total: Q", monto)

        # Opción 2: analiza la categoría de ingreso más fuerte.
        elif opcion == "2":

            # Obtiene la categoría de ingreso con mayor monto.
            resultado = obtener_categoria_mayor(ingresos)

            # Verifica si todavía no hay ingresos registrados.
            if resultado is None:
                print("Todavía no hay ingresos registrados.")

            # Si hay datos, muestra la categoría y el monto.
            else:
                categoria, monto = resultado
                print("La categoría de ingreso más fuerte es:", categoria)
                print("Monto total: Q", monto)

        # Opción 3: muestra los ingresos totales.
        elif opcion == "3":

            # Imprime el total de ingresos calculado.
            print("Sus ingresos totales son: Q", total_ingresos)

        # Opción 4: muestra la utilidad actual.
        elif opcion == "4":

            # Imprime la utilidad actual del negocio.
            print("Su utilidad actual es: Q", utilidad)

        # Opción 5: muestra qué usuario ha registrado más movimientos.
        elif opcion == "5":

            # Calcula el usuario con más movimientos registrados.
            resultado = usuario_con_mas_movimientos()

            # Verifica si no hay movimientos registrados.
            if resultado is None:
                print("Todavía no hay movimientos registrados.")

            # Si hay datos, muestra el usuario y su cantidad de registros.
            else:
                usuario, cantidad = resultado
                print("El usuario con más movimientos registrados es:", usuario)
                print("Cantidad de movimientos:", cantidad)

        # Opción 6: compara si los gastos son mayores, iguales o menores que los ingresos.
        elif opcion == "6":

            # Verifica si los gastos superan a los ingresos.
            if total_gastos > total_ingresos:
                print("Sí. Actualmente los gastos son mayores que los ingresos.")
                print("Diferencia negativa: Q", total_gastos - total_ingresos)

            # Verifica si la empresa está en punto de equilibrio.
            elif total_gastos == total_ingresos:
                print("No exactamente. Está en punto de equilibrio.")

            # Si los ingresos son mayores, muestra la diferencia positiva.
            else:
                print("No. Los ingresos son mayores que los gastos.")
                print("Diferencia positiva: Q", utilidad)

        # Opción 7: muestra el presupuesto con mayor riesgo.
        elif opcion == "7":

            # Obtiene el presupuesto más riesgoso según porcentaje utilizado.
            resultado = presupuesto_mas_riesgoso()

            # Verifica si no hay presupuestos registrados.
            if resultado is None:
                print("No hay presupuestos registrados.")

            # Si existe presupuesto, muestra información detallada.
            else:
                presupuesto, porcentaje = resultado
                print("Presupuesto con más riesgo:", presupuesto["categoria"])
                print("Mes:", presupuesto["mes"])
                print("Porcentaje utilizado:", round(porcentaje, 2), "%")

                # Indica si el presupuesto ya fue superado.
                if porcentaje > 100:
                    print("Este presupuesto ya fue superado.")

                # Indica si el presupuesto está cerca del límite.
                elif porcentaje >= 80:
                    print("Este presupuesto está cerca de ser superado.")

                # Indica que el presupuesto sigue bajo control.
                else:
                    print("Este presupuesto todavía está bajo control.")

        # Opción 8: muestra la meta financiera con mejor progreso.
        elif opcion == "8":

            # Obtiene la meta con mejor porcentaje de avance.
            resultado = meta_con_mejor_progreso()

            # Verifica si no hay metas registradas.
            if resultado is None:
                print("No hay metas registradas.")

            # Si existe una meta, muestra información detallada.
            else:
                meta, porcentaje = resultado
                print("La meta con mejor progreso es:", meta["descripcion"])
                print("Tipo:", meta["tipo"])
                print("Progreso:", round(porcentaje, 2), "%")

        # Opción 9: genera una recomendación personalizada.
        elif opcion == "9":

            # Ejecuta la función de recomendación inteligente.
            recomendacion_personalizada()

        # Opción 10: genera un diagnóstico financiero completo del negocio.
        elif opcion == "10":

            # Ejecuta la función de diagnóstico completo.
            diagnostico_negocio()

        # Opción 0: sale del asistente financiero.
        elif opcion == "0":
            break

        # Muestra error cuando la opción no existe.
        else:
            print("Opción inválida.")