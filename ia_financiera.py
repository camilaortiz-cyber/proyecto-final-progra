from data_manager import leer_json
from finanzas import calcular_total
from reportes import total_por_categoria


RUTA_INGRESOS = "data/ingresos.json"
RUTA_GASTOS = "data/gastos.json"


def categoria_mayor_gasto(gastos):
    categorias = total_por_categoria(gastos)

    if len(categorias) == 0:
        return None

    mayor_categoria = ""
    mayor_monto = 0

    for categoria, monto in categorias.items():
        if monto > mayor_monto:
            mayor_categoria = categoria
            mayor_monto = monto

    return mayor_categoria, mayor_monto


def asistente_financiero():
    while True:
        ingresos = leer_json(RUTA_INGRESOS)
        gastos = leer_json(RUTA_GASTOS)

        total_ingresos = calcular_total(ingresos)
        total_gastos = calcular_total(gastos)
        utilidad = total_ingresos - total_gastos

        print("\n===== IA FINANCIERA SIMULADA =====")
        print("1. ¿En qué gasté más?")
        print("2. ¿Cuánto he ganado?")
        print("3. ¿Cuál es mi utilidad?")
        print("4. Dame una recomendación")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            resultado = categoria_mayor_gasto(gastos)

            if resultado is None:
                print("Todavía no hay gastos registrados.")
            else:
                categoria, monto = resultado
                print("La categoría donde más ha gastado es:", categoria)
                print("Monto total: Q", monto)

        elif opcion == "2":
            print("Sus ingresos totales son: Q", total_ingresos)

        elif opcion == "3":
            print("Su utilidad actual es: Q", utilidad)

        elif opcion == "4":
            if utilidad > 0:
                print("Recomendación: Mantenga el control de gastos y reinvierta parte de sus ganancias.")
            elif utilidad == 0:
                print("Recomendación: Busque aumentar ingresos o reducir gastos para generar utilidad.")
            else:
                print("Recomendación: Revise sus gastos más altos y reduzca costos innecesarios.")

        elif opcion == "0":
            break

        else:
            print("Opción inválida.")