from data_manager import leer_json, guardar_json
from auditoria import registrar_auditoria


RUTA_PROVEEDORES = "data/proveedores.json"


def registrar_proveedor(usuario_actual):
    print("\n===== REGISTRAR PROVEEDOR =====")

    nombre = input("Nombre del proveedor: ")
    producto = input("Producto o servicio principal: ")
    telefono = input("Telefono: ")
    correo = input("Correo: ")

    if nombre == "" or producto == "":
        print("Nombre y producto/servicio son obligatorios.")
        return False

    proveedores = leer_json(RUTA_PROVEEDORES)

    proveedor = {
        "nombre": nombre,
        "producto": producto,
        "telefono": telefono,
        "correo": correo,
        "creado_por": usuario_actual["usuario"]
    }

    proveedores.append(proveedor)
    guardar_json(RUTA_PROVEEDORES, proveedores)

    registrar_auditoria(
        usuario_actual,
        "Registro de proveedor",
        "Se registro el proveedor " + nombre + "."
    )

    print("Proveedor registrado correctamente.")
    return True


def listar_proveedores():
    proveedores = leer_json(RUTA_PROVEEDORES)

    print("\n===== PROVEEDORES =====")

    if len(proveedores) == 0:
        print("No hay proveedores registrados.")
        return

    contador = 1

    for proveedor in proveedores:
        print("--------------------------------")
        print(contador, ".", proveedor["nombre"])
        print("Producto/Servicio:", proveedor["producto"])
        print("Telefono:", proveedor["telefono"])
        print("Correo:", proveedor["correo"])
        print("Creado por:", proveedor["creado_por"])
        contador = contador + 1


def buscar_proveedor():
    proveedores = leer_json(RUTA_PROVEEDORES)

    print("\n===== BUSCAR PROVEEDOR =====")
    busqueda = input("Ingrese nombre o producto/servicio: ").lower()

    encontrado = False

    for proveedor in proveedores:
        if busqueda in proveedor["nombre"].lower() or busqueda in proveedor["producto"].lower():
            print("--------------------------------")
            print("Proveedor:", proveedor["nombre"])
            print("Producto/Servicio:", proveedor["producto"])
            print("Telefono:", proveedor["telefono"])
            print("Correo:", proveedor["correo"])
            encontrado = True

    if not encontrado:
        print("No se encontro ningun proveedor.")


def menu_proveedores(usuario_actual):
    while True:
        print("\n===== MODULO DE PROVEEDORES =====")
        print("1. Registrar proveedor")
        print("2. Listar proveedores")
        print("3. Buscar proveedor")
        print("0. Volver")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            registrar_proveedor(usuario_actual)
        elif opcion == "2":
            listar_proveedores()
        elif opcion == "3":
            buscar_proveedor()
        elif opcion == "0":
            break
        else:
            print("Opcion invalida.")