# Importa las funciones para leer y guardar información en archivos JSON.
from data_manager import leer_json, guardar_json


# Define la ruta del archivo donde se guarda la configuración de módulos.
RUTA_CONFIGURACION = "data/configuracion.json"


# Obtiene la configuración actual de los módulos del sistema.
def obtener_modulos():

    # Lee y devuelve el contenido del archivo de configuración.
    return leer_json(RUTA_CONFIGURACION)


# Muestra en pantalla únicamente los módulos que están activos.
def mostrar_modulos_activos():

    # Obtiene la configuración actual de módulos.
    modulos = obtener_modulos()

    # Muestra el título de la sección de módulos activos.
    print("\n===== MÓDULOS ACTIVOS =====")

    # Recorre cada módulo con su estado activo o inactivo.
    for nombre, activo in modulos.items():

        # Verifica si el módulo está activo.
        if activo:

            # Muestra el nombre del módulo activo.
            print("-", nombre)


# Permite activar o desactivar módulos del sistema desde el menú.
def configurar_modulos():

    # Obtiene la configuración actual de módulos.
    modulos = obtener_modulos()

    # Mantiene abierto el menú de configuración hasta que el usuario decida volver.
    while True:

        # Muestra el título de la sección de configuración.
        print("\n===== CONFIGURACIÓN DE MÓDULOS =====")

        # Convierte las claves del diccionario de módulos en una lista para numerarlas.
        lista_modulos = list(modulos.keys())

        # Recorre la lista de módulos usando su índice.
        for i in range(len(lista_modulos)):

            # Obtiene el nombre del módulo actual.
            modulo = lista_modulos[i]

            # Define el texto del estado según si el módulo está activo o inactivo.
            estado = "Activo" if modulos[modulo] else "Inactivo"

            # Muestra el número, nombre y estado del módulo.
            print(i + 1, ".", modulo, "-", estado)

        # Muestra la opción para regresar al menú anterior.
        print("0. Volver")

        # Solicita al usuario elegir qué módulo desea activar o desactivar.
        opcion = input("Seleccione el módulo que desea activar/desactivar: ")

        # Si el usuario elige 0, sale del menú de configuración.
        if opcion == "0":
            break

        # Verifica que la opción ingresada sea un número.
        if opcion.isdigit():

            # Convierte la opción a índice de lista restando 1.
            indice = int(opcion) - 1

            # Valida que el índice esté dentro del rango de módulos existentes.
            if indice >= 0 and indice < len(lista_modulos):

                # Obtiene el módulo seleccionado por el usuario.
                modulo_elegido = lista_modulos[indice]

                # Cambia el estado del módulo: si estaba activo lo desactiva, y viceversa.
                modulos[modulo_elegido] = not modulos[modulo_elegido]

                # Guarda la configuración actualizada en el archivo JSON.
                guardar_json(RUTA_CONFIGURACION, modulos)

                # Muestra un mensaje confirmando que el módulo fue actualizado.
                print("Módulo actualizado correctamente.")

            # Muestra error si el número está fuera del rango de módulos.
            else:
                print("Opción fuera de rango.")

        # Muestra error si el usuario no ingresa un número.
        else:
            print("Debe ingresar un número válido.")