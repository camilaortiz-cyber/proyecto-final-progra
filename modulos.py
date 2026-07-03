from data_manager import leer_json, guardar_json


RUTA_CONFIGURACION = "data/configuracion.json"


def obtener_modulos():
    return leer_json(RUTA_CONFIGURACION)


def mostrar_modulos_activos():
    modulos = obtener_modulos()

    print("\n===== MÓDULOS ACTIVOS =====")

    for nombre, activo in modulos.items():
        if activo:
            print("-", nombre)


def configurar_modulos():
    modulos = obtener_modulos()

    while True:
        print("\n===== CONFIGURACIÓN DE MÓDULOS =====")

        lista_modulos = list(modulos.keys())

        for i in range(len(lista_modulos)):
            modulo = lista_modulos[i]
            estado = "Activo" if modulos[modulo] else "Inactivo"
            print(i + 1, ".", modulo, "-", estado)

        print("0. Volver")

        opcion = input("Seleccione el módulo que desea activar/desactivar: ")

        if opcion == "0":
            break

        if opcion.isdigit():
            indice = int(opcion) - 1

            if indice >= 0 and indice < len(lista_modulos):
                modulo_elegido = lista_modulos[indice]
                modulos[modulo_elegido] = not modulos[modulo_elegido]
                guardar_json(RUTA_CONFIGURACION, modulos)
                print("Módulo actualizado correctamente.")
            else:
                print("Opción fuera de rango.")
        else:
            print("Debe ingresar un número válido.")