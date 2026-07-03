from data_manager import leer_json, guardar_json
from auditoria import registrar_auditoria


RUTA_EMPRESAS = "data/empresas.json"


def crear_empresa(usuario_actual):
    print("\n===== CREAR EMPRESA =====")

    nombre = input("Nombre de la empresa: ")
    nit = input("NIT: ")
    sector = input("Sector: ")
    telefono = input("Telefono: ")

    if nombre == "" or nit == "" or sector == "":
        print("Nombre, NIT y sector son obligatorios.")
        return False

    empresas = leer_json(RUTA_EMPRESAS)

    empresa = {
        "nombre": nombre,
        "nit": nit,
        "sector": sector,
        "telefono": telefono,
        "creado_por": usuario_actual["usuario"]
    }

    empresas.append(empresa)
    guardar_json(RUTA_EMPRESAS, empresas)

    registrar_auditoria(
        usuario_actual,
        "Creacion de empresa",
        "Se creo la empresa " + nombre + "."
    )

    print("Empresa creada correctamente.")
    return True


def listar_empresas():
    empresas = leer_json(RUTA_EMPRESAS)

    print("\n===== EMPRESAS REGISTRADAS =====")

    if len(empresas) == 0:
        print("No hay empresas registradas.")
        return

    contador = 1

    for empresa in empresas:
        print("--------------------------------")
        print(contador, ".", empresa["nombre"])
        print("NIT:", empresa["nit"])
        print("Sector:", empresa["sector"])
        print("Telefono:", empresa["telefono"])
        print("Creado por:", empresa["creado_por"])
        contador = contador + 1


def buscar_empresa():
    empresas = leer_json(RUTA_EMPRESAS)

    print("\n===== BUSCAR EMPRESA =====")
    busqueda = input("Ingrese nombre o NIT: ").lower()

    encontrado = False

    for empresa in empresas:
        if busqueda in empresa["nombre"].lower() or busqueda in empresa["nit"].lower():
            print("--------------------------------")
            print("Empresa:", empresa["nombre"])
            print("NIT:", empresa["nit"])
            print("Sector:", empresa["sector"])
            print("Telefono:", empresa["telefono"])
            encontrado = True

    if not encontrado:
        print("No se encontro ninguna empresa.")


def menu_empresas(usuario_actual):
    while True:
        print("\n===== MODULO DE EMPRESAS =====")
        print("1. Crear empresa")
        print("2. Listar empresas")
        print("3. Buscar empresa")
        print("0. Volver")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            crear_empresa(usuario_actual)
        elif opcion == "2":
            listar_empresas()
        elif opcion == "3":
            buscar_empresa()
        elif opcion == "0":
            break
        else:
            print("Opcion invalida.")