from datetime import datetime
from data_manager import leer_json
from finanzas import calcular_total


RUTA_INGRESOS = "data/ingresos.json"
RUTA_GASTOS = "data/gastos.json"
RUTA_USUARIOS = "data/usuarios.json"
RUTA_CLIENTES = "data/clientes.json"
RUTA_PROVEEDORES = "data/proveedores.json"
RUTA_PRESUPUESTOS = "data/presupuestos.json"
RUTA_METAS = "data/metas.json"
RUTA_AUDITORIA = "data/auditoria.json"


def obtener_mes_actual():
    fecha_actual = datetime.now()
    return fecha_actual.month, fecha_actual.year


def movimiento_es_del_mes(movimiento, mes, anio):
    if "fecha" not in movimiento:
        return False

    try:
        fecha = datetime.strptime(movimiento["fecha"], "%Y-%m-%d %H:%M:%S")
        return fecha.month == mes and fecha.year == anio
    except ValueError:
        return False


def filtrar_movimientos_por_mes(movimientos, mes, anio):
    movimientos_filtrados = []

    for movimiento in movimientos:
        if movimiento_es_del_mes(movimiento, mes, anio):
            movimientos_filtrados.append(movimiento)

    return movimientos_filtrados


def filtrar_movimientos_por_usuario(movimientos, nombre_usuario):
    movimientos_usuario = []

    for movimiento in movimientos:
        if movimiento.get("creado_por") == nombre_usuario:
            movimientos_usuario.append(movimiento)

    return movimientos_usuario


def contar_movimientos_por_usuario(ingresos, gastos):
    actividad = {}

    for ingreso in ingresos:
        usuario = ingreso.get("creado_por", "desconocido")

        if usuario not in actividad:
            actividad[usuario] = {
                "ingresos": 0,
                "gastos": 0,
                "total_movimientos": 0
            }

        actividad[usuario]["ingresos"] = actividad[usuario]["ingresos"] + 1
        actividad[usuario]["total_movimientos"] = actividad[usuario]["total_movimientos"] + 1

    for gasto in gastos:
        usuario = gasto.get("creado_por", "desconocido")

        if usuario not in actividad:
            actividad[usuario] = {
                "ingresos": 0,
                "gastos": 0,
                "total_movimientos": 0
            }

        actividad[usuario]["gastos"] = actividad[usuario]["gastos"] + 1
        actividad[usuario]["total_movimientos"] = actividad[usuario]["total_movimientos"] + 1

    return actividad


def mostrar_resumen_financiero(ingresos, gastos):
    total_ingresos = calcular_total(ingresos)
    total_gastos = calcular_total(gastos)
    utilidad = total_ingresos - total_gastos

    print("Total de ingresos: Q", total_ingresos)
    print("Total de gastos: Q", total_gastos)
    print("Utilidad del mes: Q", utilidad)
    print("Cantidad de ingresos:", len(ingresos))
    print("Cantidad de gastos:", len(gastos))

    if utilidad > 0:
        print("Estado: el mes tuvo utilidad positiva.")
    elif utilidad == 0:
        print("Estado: el mes quedó en punto de equilibrio.")
    else:
        print("Estado: el mes tuvo pérdida.")


def reporte_admin(usuario, ingresos_mes, gastos_mes):
    usuarios = leer_json(RUTA_USUARIOS)
    auditoria = leer_json(RUTA_AUDITORIA)

    print("\n===== RESUMEN MENSUAL PARA ADMINISTRADOR =====")
    print("Usuario:", usuario["usuario"])
    print("--------------------------------")

    mostrar_resumen_financiero(ingresos_mes, gastos_mes)

    print("--------------------------------")
    print("Usuarios registrados:", len(usuarios))
    print("Registros de auditoría:", len(auditoria))

    print("--------------------------------")
    print("Actividad por usuario:")

    actividad = contar_movimientos_por_usuario(ingresos_mes, gastos_mes)

    if len(actividad) == 0:
        print("No hay actividad financiera registrada este mes.")
    else:
        for nombre_usuario in actividad:
            print("--------------------------------")
            print("Usuario:", nombre_usuario)
            print("Ingresos registrados:", actividad[nombre_usuario]["ingresos"])
            print("Gastos registrados:", actividad[nombre_usuario]["gastos"])
            print("Total de movimientos:", actividad[nombre_usuario]["total_movimientos"])


def reporte_gerente(usuario, ingresos_mes, gastos_mes):
    clientes = leer_json(RUTA_CLIENTES)
    proveedores = leer_json(RUTA_PROVEEDORES)
    presupuestos = leer_json(RUTA_PRESUPUESTOS)
    metas = leer_json(RUTA_METAS)

    print("\n===== RESUMEN MENSUAL PARA GERENTE =====")
    print("Usuario:", usuario["usuario"])
    print("--------------------------------")

    mostrar_resumen_financiero(ingresos_mes, gastos_mes)

    print("--------------------------------")
    print("Clientes registrados:", len(clientes))
    print("Proveedores registrados:", len(proveedores))
    print("Presupuestos registrados:", len(presupuestos))
    print("Metas registradas:", len(metas))

    print("--------------------------------")
    print("Actividad del equipo:")

    actividad = contar_movimientos_por_usuario(ingresos_mes, gastos_mes)

    if len(actividad) == 0:
        print("No hay actividad del equipo este mes.")
    else:
        for nombre_usuario in actividad:
            print(
                nombre_usuario,
                "- movimientos:",
                actividad[nombre_usuario]["total_movimientos"]
            )


def reporte_contador(usuario, ingresos_mes, gastos_mes):
    print("\n===== RESUMEN MENSUAL PARA CONTADOR =====")
    print("Usuario:", usuario["usuario"])
    print("--------------------------------")

    mostrar_resumen_financiero(ingresos_mes, gastos_mes)

    print("--------------------------------")
    print("Detalle de ingresos del mes:")

    if len(ingresos_mes) == 0:
        print("No hay ingresos registrados este mes.")
    else:
        for ingreso in ingresos_mes:
            print("-", ingreso["descripcion"], "|", ingreso["categoria"], "| Q", ingreso["monto"])

    print("--------------------------------")
    print("Detalle de gastos del mes:")

    if len(gastos_mes) == 0:
        print("No hay gastos registrados este mes.")
    else:
        for gasto in gastos_mes:
            print("-", gasto["descripcion"], "|", gasto["categoria"], "| Q", gasto["monto"])


def reporte_empleado(usuario, ingresos_mes, gastos_mes):
    ingresos_usuario = filtrar_movimientos_por_usuario(ingresos_mes, usuario["usuario"])
    gastos_usuario = filtrar_movimientos_por_usuario(gastos_mes, usuario["usuario"])

    print("\n===== RESUMEN MENSUAL PARA EMPLEADO =====")
    print("Usuario:", usuario["usuario"])
    print("--------------------------------")

    print("Tus ingresos registrados este mes:", len(ingresos_usuario))
    print("Tus gastos registrados este mes:", len(gastos_usuario))

    total_ingresos = calcular_total(ingresos_usuario)
    total_gastos = calcular_total(gastos_usuario)

    print("Total de ingresos registrados por ti: Q", total_ingresos)
    print("Total de gastos registrados por ti: Q", total_gastos)

    print("--------------------------------")
    print("Tus movimientos del mes:")

    if len(ingresos_usuario) == 0 and len(gastos_usuario) == 0:
        print("No registraste movimientos este mes.")
    else:
        for ingreso in ingresos_usuario:
            print("- Ingreso:", ingreso["descripcion"], "| Q", ingreso["monto"])

        for gasto in gastos_usuario:
            print("- Gasto:", gasto["descripcion"], "| Q", gasto["monto"])


def mostrar_reporte_mensual(usuario, mes, anio):
    ingresos = leer_json(RUTA_INGRESOS)
    gastos = leer_json(RUTA_GASTOS)

    ingresos_mes = filtrar_movimientos_por_mes(ingresos, mes, anio)
    gastos_mes = filtrar_movimientos_por_mes(gastos, mes, anio)

    print("\n================================")
    print("REPORTE MENSUAL")
    print("Mes:", mes)
    print("Año:", anio)
    print("Rol:", usuario["rol"])
    print("================================")

    rol = usuario["rol"]

    if rol == "admin" or rol == "administrador":
        reporte_admin(usuario, ingresos_mes, gastos_mes)

    elif rol == "gerente":
        reporte_gerente(usuario, ingresos_mes, gastos_mes)

    elif rol == "contador":
        reporte_contador(usuario, ingresos_mes, gastos_mes)

    elif rol == "empleado":
        reporte_empleado(usuario, ingresos_mes, gastos_mes)

    else:
        print("Rol no reconocido. No se puede generar reporte mensual.")

def menu_reportes_mensuales(usuario):
    while True:
        print("\n===== REPORTES MENSUALES =====")
        print("1. Ver resumen del mes actual")
        print("2. Ver resumen por mes y año")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mes, anio = obtener_mes_actual()
            mostrar_reporte_mensual(usuario, mes, anio)

        elif opcion == "2":
            try:
                mes = int(input("Ingrese el mes, por ejemplo 7: "))
                anio = int(input("Ingrese el año, por ejemplo 2026: "))
            except ValueError:
                print("Mes y año deben ser números.")
                continue

            if mes < 1 or mes > 12:
                print("El mes debe estar entre 1 y 12.")
                continue

            mostrar_reporte_mensual(usuario, mes, anio)

        elif opcion == "0":
            break

        else:
            print("Opción inválida.")