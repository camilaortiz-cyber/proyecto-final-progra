from usuarios import iniciar_sesion, mostrar_usuario, tiene_permiso
from modulos import obtener_modulos, configurar_modulos, mostrar_modulos_activos
from finanzas import registrar_ingreso, registrar_gasto, mostrar_flujo_caja
from reportes import mostrar_reporte_general, mostrar_movimientos, mostrar_gastos_por_categoria
from ia_financiera import asistente_financiero


def mostrar_bienvenida():
    print("===================================")
    print("              FINFLOW")
    print(" Plataforma Financiera Modular PYME")
    print("===================================")


def agregar_opcion(opciones, numero, nombre_visible, accion):
    print(numero, ".", nombre_visible)
    opciones[str(numero)] = accion
    return numero + 1


def mostrar_dashboard(usuario):
    print("\n===== DASHBOARD =====")
    mostrar_usuario(usuario)
    mostrar_modulos_activos()
    mostrar_flujo_caja()


def mostrar_menu_reportes():
    while True:
        print("\n===== REPORTES =====")
        print("1. Reporte general")
        print("2. Ver movimientos")
        print("3. Gastos por categoría")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_reporte_general()
        elif opcion == "2":
            mostrar_movimientos()
        elif opcion == "3":
            mostrar_gastos_por_categoria()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")


def mostrar_menu(usuario):
    seguir = True

    while seguir:
        modulos = obtener_modulos()

        print("\n===== MENÚ PRINCIPAL =====")
        print("Bienvenido:", usuario["usuario"])
        print("Rol:", usuario["rol"])

        opciones = {}
        numero = 1

        if modulos["dashboard"] and tiene_permiso(usuario, "dashboard"):
            numero = agregar_opcion(opciones, numero, "Dashboard", "dashboard")

        if modulos["ingresos"] and tiene_permiso(usuario, "ingresos"):
            numero = agregar_opcion(opciones, numero, "Registrar ingreso", "ingresos")

        if modulos["gastos"] and tiene_permiso(usuario, "gastos"):
            numero = agregar_opcion(opciones, numero, "Registrar gasto", "gastos")

        if modulos["flujo_caja"] and tiene_permiso(usuario, "flujo_caja"):
            numero = agregar_opcion(opciones, numero, "Flujo de caja", "flujo_caja")

        if modulos["reportes"] and tiene_permiso(usuario, "reportes"):
            numero = agregar_opcion(opciones, numero, "Reportes", "reportes")

        if modulos["ia_financiera"] and tiene_permiso(usuario, "ia_financiera"):
            numero = agregar_opcion(opciones, numero, "IA financiera", "ia_financiera")

        if tiene_permiso(usuario, "configuracion"):
            numero = agregar_opcion(opciones, numero, "Configuración de módulos", "configuracion")

        print("0. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "0":
            seguir = False
            print("Sesión cerrada.")

        elif opcion in opciones:
            accion = opciones[opcion]

            if accion == "dashboard":
                mostrar_dashboard(usuario)

            elif accion == "ingresos":
                registrar_ingreso(usuario)

            elif accion == "gastos":
                registrar_gasto(usuario)

            elif accion == "flujo_caja":
                mostrar_flujo_caja()

            elif accion == "reportes":
                mostrar_menu_reportes()

            elif accion == "ia_financiera":
                asistente_financiero()

            elif accion == "configuracion":
                configurar_modulos()

        else:
            print("Opción inválida.")


def main():
    mostrar_bienvenida()

    usuario = iniciar_sesion()

    if usuario is not None:
        mostrar_menu(usuario)
    else:
        print("No se pudo iniciar sesión.")


if __name__ == "__main__":
    main()