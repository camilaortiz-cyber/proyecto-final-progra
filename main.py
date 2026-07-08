
# Importa funciones relacionadas con usuarios, inicio de sesión, permisos y administración.
from usuarios import iniciar_sesion, mostrar_usuario, tiene_permiso, menu_administracion_usuarios

from reportes_mensuales import menu_reportes_mensuales

from configuracion_empresa import menu_configuracion_empresa

# Importa funciones para obtener, configurar y mostrar los módulos activos del sistema.
from modulos import obtener_modulos, configurar_modulos, mostrar_modulos_activos

# Importa funciones principales del módulo financiero.
from finanzas import registrar_ingreso, registrar_gasto, mostrar_flujo_caja

# Importa funciones para registrar inicio y cierre de sesión, además del menú de sesiones.
from sesiones import registrar_inicio_sesion, registrar_cierre_sesion, menu_sesiones

 # Importa la función que guarda inicio y cierre de sesión en Neon.
from sesiones_db import registrar_sesion   

# Importa diferentes funciones del módulo de reportes.
from reportes import (
    mostrar_reporte_general,
    mostrar_movimientos,
    mostrar_gastos_por_categoria,
    mostrar_ingresos_por_categoria,
    reporte_por_usuario,
    buscar_movimiento
)

# Importa el asistente financiero simulado.
from ia_financiera import asistente_financiero

# Importa la función para mostrar el historial de auditoría.
from auditoria import mostrar_auditoria

# Importa los menús de los módulos administrativos del sistema.
from empresas import menu_empresas
from clientes import menu_clientes
from proveedores import menu_proveedores
from presupuestos import menu_presupuestos
from metas import menu_metas

# Importa la función para mostrar alertas inteligentes.
from alertas import mostrar_alertas


# Muestra el encabezado de bienvenida del sistema.
def mostrar_bienvenida():
    print("===================================")
    print("              FINFLOW")
    print(" Plataforma Financiera Modular PYME")
    print("===================================")


# Agrega una opción al menú dinámico y la relaciona con una acción interna.
def agregar_opcion(opciones, numero, nombre_visible, accion):
    print(numero, ".", nombre_visible)
    opciones[str(numero)] = accion
    return numero + 1


# Muestra el dashboard principal del usuario actual.
def mostrar_dashboard(usuario):
    print("\n===== DASHBOARD =====")

    # Muestra información del usuario que inició sesión.
    mostrar_usuario(usuario)

    # Muestra los módulos que están activos actualmente.
    mostrar_modulos_activos()

    # Muestra el estado del flujo de caja.
    mostrar_flujo_caja()


# Muestra el submenú de reportes financieros.
def mostrar_menu_reportes():
    while True:
        print("\n===== REPORTES =====")
        print("1. Reporte general")
        print("2. Ver movimientos")
        print("3. Gastos por categoría")
        print("4. Ingresos por categoría")
        print("5. Reporte por usuario")
        print("6. Buscar movimiento")
        print("0. Volver")

        # Solicita al usuario seleccionar una opción del menú de reportes.
        opcion = input("Seleccione una opción: ")

        # Ejecuta el reporte general.
        if opcion == "1":
            mostrar_reporte_general()

        # Muestra todos los movimientos financieros.
        elif opcion == "2":
            mostrar_movimientos()

        # Muestra los gastos agrupados por categoría.
        elif opcion == "3":
            mostrar_gastos_por_categoria()

        # Muestra los ingresos agrupados por categoría.
        elif opcion == "4":
            mostrar_ingresos_por_categoria()

        # Muestra movimientos filtrados por usuario.
        elif opcion == "5":
            reporte_por_usuario()

        # Permite buscar un movimiento específico.
        elif opcion == "6":
            buscar_movimiento()

        # Regresa al menú principal.
        elif opcion == "0":
            break

        # Valida opciones incorrectas.
        else:
            print("Opción inválida.")


# Muestra el menú principal según los módulos activos y los permisos del usuario.
def mostrar_menu(usuario, id_sesion):

    # Variable de control para mantener activo el menú.
    seguir = True

    while seguir:

        # Obtiene la configuración actual de módulos activos.
        modulos = obtener_modulos()

        print("\n===== MENÚ PRINCIPAL =====")
        print("Bienvenido:", usuario["usuario"])
        print("Rol:", usuario["rol"])

        # Diccionario donde se guardan las opciones disponibles del usuario.
        opciones = {}

        # Número inicial para crear el menú dinámicamente.
        numero = 1

        # Agrega Dashboard si el módulo está activo y el usuario tiene permiso.
        if modulos["dashboard"] and tiene_permiso(usuario, "dashboard"):
            numero = agregar_opcion(opciones, numero, "Dashboard", "dashboard")

        # Agrega Registrar ingreso si el módulo está activo y el usuario tiene permiso.
        if modulos["ingresos"] and tiene_permiso(usuario, "ingresos"):
            numero = agregar_opcion(opciones, numero, "Registrar ingreso", "ingresos")

        # Agrega Registrar gasto si el módulo está activo y el usuario tiene permiso.
        if modulos["gastos"] and tiene_permiso(usuario, "gastos"):
            numero = agregar_opcion(opciones, numero, "Registrar gasto", "gastos")

        # Agrega Flujo de caja si el módulo está activo y el usuario tiene permiso.
        if modulos["flujo_caja"] and tiene_permiso(usuario, "flujo_caja"):
            numero = agregar_opcion(opciones, numero, "Flujo de caja", "flujo_caja")

        # Agrega Reportes si el módulo está activo y el usuario tiene permiso.
        if modulos["reportes"] and tiene_permiso(usuario, "reportes"):
            numero = agregar_opcion(opciones, numero, "Reportes", "reportes")

        if tiene_permiso(usuario, "reportes_mensuales"):
            numero = agregar_opcion(opciones, numero, "Reportes mensuales", "reportes_mensuales")

        # Agrega IA financiera si el módulo está activo y el usuario tiene permiso.
        if modulos["ia_financiera"] and tiene_permiso(usuario, "ia_financiera"):
            numero = agregar_opcion(opciones, numero, "IA financiera", "ia_financiera")

        # Agrega Empresas si el módulo está activo y el usuario tiene permiso.
        if modulos["empresas"] and tiene_permiso(usuario, "empresas"):
            numero = agregar_opcion(opciones, numero, "Empresas", "empresas")

        # Agrega Clientes si el módulo está activo y el usuario tiene permiso.
        if modulos["clientes"] and tiene_permiso(usuario, "clientes"):
            numero = agregar_opcion(opciones, numero, "Clientes", "clientes")

        # Agrega Proveedores si el módulo está activo y el usuario tiene permiso.
        if modulos["proveedores"] and tiene_permiso(usuario, "proveedores"):
            numero = agregar_opcion(opciones, numero, "Proveedores", "proveedores")

        # Agrega Presupuestos si el módulo está activo y el usuario tiene permiso.
        if modulos["presupuestos"] and tiene_permiso(usuario, "presupuestos"):
            numero = agregar_opcion(opciones, numero, "Presupuestos", "presupuestos")

        # Agrega Metas financieras si el módulo está activo y el usuario tiene permiso.
        if modulos["metas"] and tiene_permiso(usuario, "metas"):
            numero = agregar_opcion(opciones, numero, "Metas financieras", "metas")

        # Agrega Alertas inteligentes si el módulo está activo y el usuario tiene permiso.
        if modulos["alertas"] and tiene_permiso(usuario, "alertas"):
            numero = agregar_opcion(opciones, numero, "Alertas inteligentes", "alertas")

        # Agrega administración de usuarios si el usuario tiene permiso.
        if tiene_permiso(usuario, "usuarios"):
            numero = agregar_opcion(opciones, numero, "Administrar usuarios", "usuarios")

        # Agrega auditoría si el usuario tiene permiso.
        if tiene_permiso(usuario, "auditoria"):
            numero = agregar_opcion(opciones, numero, "Ver auditoría", "auditoria")

        # Agrega configuración de módulos si el usuario tiene permiso.
        if tiene_permiso(usuario, "configuracion"):
            numero = agregar_opcion(opciones, numero, "Configuración de módulos", "configuracion")

        if tiene_permiso(usuario, "configuracion_empresa"):
            numero = agregar_opcion(opciones, numero, "Configuración de empresa", "configuracion_empresa")

        print("0. Cerrar sesión")

        # Solicita al usuario seleccionar una opción del menú principal.
        opcion = input("Seleccione una opción: ")

        # Cierra la sesión actual si el usuario selecciona 0.
        if opcion == "0":

            # Registra el cierre de sesión en el sistema.
            registrar_cierre_sesion(usuario, id_sesion)

            # Cambia la variable para salir del menú.
            seguir = False

            print("Sesión cerrada.")

        # Verifica si la opción seleccionada existe en el menú dinámico.
        elif opcion in opciones:

            # Obtiene la acción relacionada con la opción seleccionada.
            accion = opciones[opcion]

            # Ejecuta el dashboard.
            if accion == "dashboard":
                mostrar_dashboard(usuario)

            # Ejecuta el registro de ingresos.
            elif accion == "ingresos":
                registrar_ingreso(usuario)

            # Ejecuta el registro de gastos.
            elif accion == "gastos":
                registrar_gasto(usuario)

            # Muestra el flujo de caja.
            elif accion == "flujo_caja":
                mostrar_flujo_caja()

            # Abre el submenú de reportes.
            elif accion == "reportes":
                mostrar_menu_reportes()

            elif accion == "reportes_mensuales":
                menu_reportes_mensuales(usuario)

            # Abre el asistente financiero.
            elif accion == "ia_financiera":
                asistente_financiero(usuario)  # Envía el usuario actual para que la IA adapte sus respuestas según el rol.

            # Abre el módulo de empresas.
            elif accion == "empresas":
                menu_empresas(usuario)

            # Abre el módulo de clientes.
            elif accion == "clientes":
                menu_clientes(usuario)

            # Abre el módulo de proveedores.
            elif accion == "proveedores":
                menu_proveedores(usuario)

            # Abre el módulo de presupuestos.
            elif accion == "presupuestos":
                menu_presupuestos(usuario)

            # Abre el módulo de metas financieras.
            elif accion == "metas":
                menu_metas(usuario)

            # Muestra las alertas inteligentes.
            elif accion == "alertas":
                mostrar_alertas()

            # Abre el módulo de administración de usuarios.
            elif accion == "usuarios":
                menu_administracion_usuarios(usuario)

            # Muestra el historial de auditoría.
            elif accion == "auditoria":
                mostrar_auditoria()

            # Abre la configuración de módulos.
            elif accion == "configuracion":
                configurar_modulos()

            elif accion == "configuracion_empresa":
                menu_configuracion_empresa(usuario)

        # Muestra error si el usuario ingresa una opción que no existe.
        else:
            print("Opción inválida.")


# Función principal que inicia el sistema.
def main():

    # Muestra la bienvenida del sistema.
    mostrar_bienvenida()

    # Solicita al usuario iniciar sesión.
    usuario = iniciar_sesion()

    # Verifica si el inicio de sesión fue exitoso.
    if usuario is not None:

        # Guarda en Neon que el usuario inició sesión.
        registrar_sesion(usuario, "inicio_sesion")

        # Registra el inicio de sesión en el sistema local y obtiene el ID de la sesión.
        id_sesion = registrar_inicio_sesion(usuario)

        # Muestra el menú principal del sistema usando el ID de sesión local.
        mostrar_menu(usuario, id_sesion)

        # Guarda en Neon que el usuario cerró sesión.
        registrar_sesion(usuario, "cierre_sesion")

    # Si el inicio de sesión falla, muestra un mensaje.
    else:
        print("No se pudo iniciar sesión.")

# Ejecuta el programa solamente si este archivo se corre directamente.
if __name__ == "__main__":
    main()