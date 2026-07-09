# Importa la función leer_json para poder leer información desde archivos JSON.
from data_manager import leer_json

# Importa la función calcular_total para sumar montos de ingresos o gastos.
from finanzas import calcular_total

# Importa la función que calcula el gasto real de una categoría específica.
from presupuestos import gasto_real_por_categoria

# Importa la función que calcula el avance actual de una meta financiera.
from metas import calcular_valor_actual_meta


# Define la ruta donde se almacenan los ingresos registrados.
RUTA_INGRESOS = "data/ingresos.json"

# Define la ruta donde se almacenan los gastos registrados.
RUTA_GASTOS = "data/gastos.json"

# Define la ruta donde se almacenan los presupuestos registrados.
RUTA_PRESUPUESTOS = "data/presupuestos.json"

# Define la ruta donde se almacenan las metas financieras registradas.
RUTA_METAS = "data/metas.json"


# Evalúa el estado del flujo de caja con base en ingresos, gastos y saldo disponible.
def alerta_flujo_caja():

    # Lee la lista de ingresos desde el archivo JSON correspondiente.
    ingresos = leer_json(RUTA_INGRESOS)

    # Lee la lista de gastos desde el archivo JSON correspondiente.
    gastos = leer_json(RUTA_GASTOS)

    # Calcula el total de ingresos registrados.
    total_ingresos = calcular_total(ingresos)

    # Calcula el total de gastos registrados.
    total_gastos = calcular_total(gastos)

    # Calcula el saldo disponible restando gastos a ingresos.
    saldo = total_ingresos - total_gastos

    # Verifica si el saldo es negativo, lo cual indica una situación financiera crítica.
    if saldo < 0:

        # Devuelve una alerta crítica cuando los gastos superan a los ingresos.
        return "Alerta crítica: el flujo de caja está negativo. Revise gastos inmediatamente."

    # Verifica si el saldo es exactamente cero, indicando punto de equilibrio.
    if saldo == 0:

        # Devuelve una alerta cuando no hay pérdida, pero tampoco ganancia.
        return "Alerta: la empresa está en punto de equilibrio. No hay margen de ganancia."

    # Verifica si el saldo disponible es bajo.
    if saldo < 1000:

        # Devuelve una alerta preventiva para indicar que el saldo requiere atención.
        return "Alerta preventiva: el saldo disponible es bajo."

    # Devuelve un mensaje positivo cuando el flujo de caja se considera estable.
    return "Flujo de caja saludable."


# Analiza los gastos registrados para detectar si existe algún gasto individual muy alto.
def alerta_gastos_altos():

    # Lee la lista de gastos desde el archivo JSON correspondiente.
    gastos = leer_json(RUTA_GASTOS)

    # Verifica si no hay gastos registrados.
    if len(gastos) == 0:

        # Devuelve un mensaje indicando que no hay datos suficientes para analizar.
        return "No hay gastos registrados para analizar."

    # Toma el primer gasto como referencia inicial para encontrar el gasto más alto.
    gasto_mayor = gastos[0]

    # Recorre todos los gastos registrados.
    for gasto in gastos:

        # Compara el monto del gasto actual con el monto del gasto mayor encontrado.
        if gasto["monto"] > gasto_mayor["monto"]:

            # Actualiza el gasto mayor si encuentra uno con un monto más alto.
            gasto_mayor = gasto

    # Verifica si el gasto más alto es igual o mayor a Q5000.
    if gasto_mayor["monto"] >= 5000:

        # Devuelve una alerta porque se detectó un gasto individual alto.
        return "Alerta: existe un gasto alto de Q" + str(gasto_mayor["monto"]) + " en " + gasto_mayor["categoria"] + "."

    # Verifica si el gasto más alto es igual o mayor a Q1000.
    if gasto_mayor["monto"] >= 1000:

        # Devuelve un aviso informativo sobre el gasto más alto registrado.
        return "Aviso: el gasto más alto registrado es de Q" + str(gasto_mayor["monto"]) + " en " + gasto_mayor["categoria"] + "."

    # Devuelve un mensaje positivo si no se detectan gastos individuales elevados.
    return "No se detectan gastos individuales demasiado altos."


# Evalúa los presupuestos registrados para detectar categorías en riesgo o excedidas.
def alerta_presupuestos():

    # Lee la lista de presupuestos desde el archivo JSON correspondiente.
    presupuestos = leer_json(RUTA_PRESUPUESTOS)

    # Verifica si no hay presupuestos registrados.
    if len(presupuestos) == 0:

        # Devuelve una lista con un mensaje indicando que no hay presupuestos.
        return ["No hay presupuestos registrados."]

    # Crea una lista vacía para almacenar los mensajes de alerta.
    mensajes = []

    # Recorre cada presupuesto registrado.
    for presupuesto in presupuestos:

        # Calcula el gasto real de la categoría del presupuesto actual.
        gasto_real = gasto_real_por_categoria(presupuesto["categoria"])

        # Verifica que el monto del presupuesto sea mayor que cero para evitar divisiones inválidas.
        if presupuesto["monto"] > 0:

            # Calcula el porcentaje utilizado del presupuesto.
            porcentaje = (gasto_real / presupuesto["monto"]) * 100

        # Si el presupuesto es cero o inválido, se asigna porcentaje cero.
        else:
            porcentaje = 0

        # Verifica si el gasto real superó el presupuesto asignado.
        if porcentaje > 100:

            # Agrega un mensaje indicando que el presupuesto fue superado.
            mensajes.append(
                "Presupuesto superado en " + presupuesto["categoria"] +
                ": " + str(round(porcentaje, 2)) + "% utilizado."
            )

        # Verifica si el presupuesto ya alcanzó al menos el 80% de uso.
        elif porcentaje >= 80:

            # Agrega un mensaje indicando que el presupuesto está en riesgo.
            mensajes.append(
                "Presupuesto en riesgo en " + presupuesto["categoria"] +
                ": " + str(round(porcentaje, 2)) + "% utilizado."
            )

    # Verifica si no se generó ninguna alerta de presupuesto.
    if len(mensajes) == 0:

        # Agrega un mensaje positivo indicando que los presupuestos están bajo control.
        mensajes.append("Todos los presupuestos están dentro del límite.")

    # Devuelve la lista de mensajes generados.
    return mensajes


# Evalúa el avance de las metas financieras registradas.
def alerta_metas():

    # Lee la lista de metas desde el archivo JSON correspondiente.
    metas = leer_json(RUTA_METAS)

    # Verifica si no hay metas registradas.
    if len(metas) == 0:

        # Devuelve una lista con un mensaje indicando que no hay metas.
        return ["No hay metas registradas."]

    # Crea una lista vacía para almacenar los mensajes de alerta sobre metas.
    mensajes = []

    # Recorre cada meta registrada.
    for meta in metas:

        # Calcula el valor actual acumulado según el tipo de meta.
        actual = calcular_valor_actual_meta(meta["tipo"])

        # Verifica que el monto objetivo de la meta sea mayor que cero.
        if meta["monto"] > 0:

            # Calcula el porcentaje de avance de la meta.
            porcentaje = (actual / meta["monto"]) * 100

        # Si el monto de la meta no es válido, se asigna porcentaje cero.
        else:
            porcentaje = 0

        # Verifica si la meta ya fue alcanzada o superada.
        if porcentaje >= 100:

            # Agrega un mensaje indicando que la meta fue completada.
            mensajes.append("Meta alcanzada: " + meta["descripcion"] + ".")

        # Verifica si la meta tiene un progreso muy bajo.
        elif porcentaje < 25:

            # Agrega un mensaje indicando que la meta necesita más atención.
            mensajes.append(
                "Meta con bajo progreso: " + meta["descripcion"] +
                " lleva solo " + str(round(porcentaje, 2)) + "%."
            )

        # Verifica si la meta está cerca de cumplirse.
        elif porcentaje >= 75:

            # Agrega un mensaje positivo indicando que la meta está avanzada.
            mensajes.append(
                "Meta cerca de cumplirse: " + meta["descripcion"] +
                " lleva " + str(round(porcentaje, 2)) + "%."
            )

    # Verifica si no se generó ningún mensaje especial sobre las metas.
    if len(mensajes) == 0:

        # Agrega un mensaje general indicando que las metas avanzan correctamente.
        mensajes.append("Las metas avanzan de forma estable.")

    # Devuelve la lista de mensajes generados.
    return mensajes


# Evalúa si existe suficiente actividad financiera para generar análisis útiles.
def alerta_actividad_financiera():

    # Lee la lista de ingresos desde el archivo JSON correspondiente.
    ingresos = leer_json(RUTA_INGRESOS)

    # Lee la lista de gastos desde el archivo JSON correspondiente.
    gastos = leer_json(RUTA_GASTOS)

    # Calcula la cantidad total de movimientos financieros registrados.
    total_movimientos = len(ingresos) + len(gastos)

    # Verifica si no existe ningún movimiento financiero registrado.
    if total_movimientos == 0:

        # Devuelve un mensaje indicando que se necesitan ingresos y gastos para analizar.
        return "No hay actividad financiera registrada. Agregue ingresos y gastos para generar análisis."

    # Verifica si hay pocos movimientos registrados.
    if total_movimientos < 3:

        # Devuelve un aviso indicando que los reportes mejorarán con más información.
        return "Hay poca actividad registrada. Los reportes serán más útiles con más movimientos."

    # Devuelve un mensaje positivo cuando existe suficiente información para análisis básicos.
    return "La actividad financiera registrada es suficiente para análisis básicos."


# Muestra en pantalla todas las alertas inteligentes del sistema.
def mostrar_alertas():

    # Imprime el título principal de la sección de alertas.
    print("\n===== ALERTAS INTELIGENTES =====")

    # Imprime una línea separadora para ordenar visualmente la salida.
    print("--------------------------------")

    # Muestra la alerta relacionada con la cantidad de actividad financiera registrada.
    print(alerta_actividad_financiera())

    # Imprime una línea separadora.
    print("--------------------------------")

    # Muestra la alerta relacionada con el flujo de caja.
    print(alerta_flujo_caja())

    # Imprime una línea separadora.
    print("--------------------------------")

    # Muestra la alerta relacionada con gastos individuales altos.
    print(alerta_gastos_altos())

    # Imprime una línea separadora.
    print("--------------------------------")

    # Imprime el subtítulo de la sección de presupuestos.
    print("Presupuestos:")

    # Obtiene la lista de mensajes generados por el análisis de presupuestos.
    mensajes_presupuestos = alerta_presupuestos()

    # Recorre cada mensaje de presupuesto.
    for mensaje in mensajes_presupuestos:

        # Imprime cada mensaje de presupuesto con formato de lista.
        print("-", mensaje)

    # Imprime una línea separadora.
    print("--------------------------------")

    # Imprime el subtítulo de la sección de metas.
    print("Metas:")

    # Obtiene la lista de mensajes generados por el análisis de metas.
    mensajes_metas = alerta_metas()

    # Recorre cada mensaje de metas.
    for mensaje in mensajes_metas:

        # Imprime cada mensaje de meta con formato de lista.
        print("-", mensaje)