from data_manager import leer_json, guardar_json


RUTA_CONFIGURACION_EMPRESA = "data/configuracion_empresa.json"


def obtener_configuracion_empresa():
    configuracion = leer_json(RUTA_CONFIGURACION_EMPRESA)

    if not isinstance(configuracion, dict):
        configuracion = {}

    configuracion_base = {
        "nombre_empresa": "PYME Premium",
        "moneda": "Q",
        "color_principal": "dorado",
        "tema": "premium_oscuro"
    }

    for clave in configuracion_base:
        if clave not in configuracion:
            configuracion[clave] = configuracion_base[clave]

    guardar_json(RUTA_CONFIGURACION_EMPRESA, configuracion)

    return configuracion


def mostrar_configuracion_empresa():
    configuracion = obtener_configuracion_empresa()

    print("\n===== CONFIGURACIÓN DE EMPRESA =====")
    print("Nombre de empresa:", configuracion["nombre_empresa"])
    print("Moneda:", configuracion["moneda"])
    print("Color principal:", configuracion["color_principal"])
    print("Tema visual:", configuracion["tema"])


def cambiar_nombre_empresa(configuracion):
    nuevo_nombre = input("Nuevo nombre de empresa: ").strip()

    if nuevo_nombre == "":
        print("El nombre no puede estar vacío.")
        return configuracion

    configuracion["nombre_empresa"] = nuevo_nombre
    print("Nombre de empresa actualizado correctamente.")

    return configuracion


def cambiar_moneda(configuracion):
    print("\n===== MONEDAS DISPONIBLES =====")
    print("1. Quetzales (Q)")
    print("2. Dólares ($)")
    print("3. Euros (€)")
    print("4. Colones (₡)")

    opcion = input("Seleccione una moneda: ").strip()

    if opcion == "1":
        configuracion["moneda"] = "Q"
    elif opcion == "2":
        configuracion["moneda"] = "$"
    elif opcion == "3":
        configuracion["moneda"] = "€"
    elif opcion == "4":
        configuracion["moneda"] = "₡"
    else:
        print("Opción inválida.")
        return configuracion

    print("Moneda actualizada correctamente.")
    return configuracion


def cambiar_color_principal(configuracion):
    print("\n===== COLORES DISPONIBLES =====")
    print("1. Dorado FinFlow")
    print("2. Azul ejecutivo")
    print("3. Verde financiero")
    print("4. Morado premium")
    print("5. Rojo corporativo")

    opcion = input("Seleccione un color: ").strip()

    if opcion == "1":
        configuracion["color_principal"] = "dorado"
    elif opcion == "2":
        configuracion["color_principal"] = "azul"
    elif opcion == "3":
        configuracion["color_principal"] = "verde"
    elif opcion == "4":
        configuracion["color_principal"] = "morado"
    elif opcion == "5":
        configuracion["color_principal"] = "rojo"
    else:
        print("Opción inválida.")
        return configuracion

    print("Color principal actualizado correctamente.")
    return configuracion


def cambiar_tema(configuracion):
    print("\n===== TEMAS DISPONIBLES =====")
    print("1. Premium oscuro")
    print("2. Claro ejecutivo")
    print("3. Minimalista")
    print("4. Alto contraste")

    opcion = input("Seleccione un tema: ").strip()

    if opcion == "1":
        configuracion["tema"] = "premium_oscuro"
    elif opcion == "2":
        configuracion["tema"] = "claro_ejecutivo"
    elif opcion == "3":
        configuracion["tema"] = "minimalista"
    elif opcion == "4":
        configuracion["tema"] = "alto_contraste"
    else:
        print("Opción inválida.")
        return configuracion

    print("Tema actualizado correctamente.")
    return configuracion


def restaurar_configuracion_empresa():
    configuracion = {
        "nombre_empresa": "PYME Premium",
        "moneda": "Q",
        "color_principal": "dorado",
        "tema": "premium_oscuro"
    }

    guardar_json(RUTA_CONFIGURACION_EMPRESA, configuracion)

    print("Configuración restaurada a los valores predeterminados.")


def menu_configuracion_empresa(usuario_actual):
    seguir = True

    while seguir:
        configuracion = obtener_configuracion_empresa()

        print("\n===== MENÚ CONFIGURACIÓN DE EMPRESA =====")
        print("1. Ver configuración actual")
        print("2. Cambiar nombre de empresa")
        print("3. Cambiar moneda")
        print("4. Cambiar color principal")
        print("5. Cambiar tema visual")
        print("6. Restaurar configuración predeterminada")
        print("0. Volver")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mostrar_configuracion_empresa()
        elif opcion == "2":
            configuracion = cambiar_nombre_empresa(configuracion)
            guardar_json(RUTA_CONFIGURACION_EMPRESA, configuracion)
        elif opcion == "3":
            configuracion = cambiar_moneda(configuracion)
            guardar_json(RUTA_CONFIGURACION_EMPRESA, configuracion)
        elif opcion == "4":
            configuracion = cambiar_color_principal(configuracion)
            guardar_json(RUTA_CONFIGURACION_EMPRESA, configuracion)
        elif opcion == "5":
            configuracion = cambiar_tema(configuracion)
            guardar_json(RUTA_CONFIGURACION_EMPRESA, configuracion)
        elif opcion == "6":
            restaurar_configuracion_empresa()
        elif opcion == "0":
            seguir = False
        else:
            print("Opción inválida.")