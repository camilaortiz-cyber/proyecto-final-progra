from data_manager import leer_json, guardar_json
from auditoria import registrar_auditoria


RUTA_CLIENTES = "data/clientes.json"


def registrar_cliente(usuario_actual):
    print("\n===== REGISTRAR CLIENTE =====")

    nombre = input("Nombre del cliente: ")
    telefono = input("Telefono: ")
    correo = input("Correo: ")
    empresa = input("Empresa relacionada: ")

    if nombre == "":
        print("El nombre del cliente es obligatorio.")
        return False

    clientes = leer_json(RUTA_CLIENTES)

    cliente = {
        "nombre": nombre,
        "telefono": telefono,
        "correo": correo,
        "empresa": empresa,
        "creado_por": usuario_actual["usuario"]
    }

    clientes.append(cliente)
    guardar_json(RUTA_CLIENTES, clientes)

    registrar_auditoria(
        usuario_actual,
        "Registro de cliente",
        "Se registro el cliente " + nombre + "."
    )

    print("Cliente registrado correctamente.")
    return True


def listar_clientes():
    clientes = leer_json(RUTA_CLIENTES)

    print("\n===== CLIENTES =====")

    if len(clientes) == 0:
        print("No hay clientes registrados.")
        return

    contador = 1

    for cliente in clientes:
        print("--------------------------------")
        print(contador, ".", cliente["nombre"])
        print("Telefono:", cliente["telefono"])
        print("Correo:", cliente["correo"])
        print("Empresa:", cliente["empresa"])
        print("Creado por:", cliente["creado_por"])
        contador = contador + 1


def buscar_cliente():
    clientes = leer_json(RUTA_CLIENTES)

    print("\n===== BUSCAR CLIENTE =====")
    busqueda = input("Ingrese nombre del cliente: ").lower()

    encontrado = False

    for cliente in clientes:
        if busqueda in cliente["nombre"].lower():
            print("--------------------------------")
            print("Cliente:", cliente["nombre"])
            print("Telefono:", cliente["telefono"])
            print("Correo:", cliente["correo"])
            print("Empresa:", cliente["empresa"])
            encontrado = True

    if not encontrado:
        print("No se encontro ningun cliente.")


def menu_clientes(usuario_actual):
    while True:
        print("\n===== MODULO DE CLIENTES =====")
        print("1. Registrar cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente")
        print("0. Volver")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            registrar_cliente(usuario_actual)
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            buscar_cliente()
        elif opcion == "0":
            break
        else:
            print("Opcion invalida.")