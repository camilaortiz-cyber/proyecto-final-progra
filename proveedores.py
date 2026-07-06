# Importa las funciones para leer y guardar datos en archivos JSON.
from data_manager import leer_json, guardar_json

# Importa la función para registrar acciones importantes en el historial de auditoría.
from auditoria import registrar_auditoria


# Define la ruta del archivo donde se almacenan los proveedores.
RUTA_PROVEEDORES = "data/proveedores.json"


# Permite registrar un nuevo proveedor dentro del sistema.
def registrar_proveedor(usuario_actual):

    # Muestra el título de la sección para registrar proveedores.
    print("\n===== REGISTRAR PROVEEDOR =====")

    # Solicita el nombre del proveedor.
    nombre = input("Nombre del proveedor: ")

    # Solicita el producto o servicio principal que ofrece el proveedor.
    producto = input("Producto o servicio principal: ")

    # Solicita el número de teléfono del proveedor.
    telefono = input("Telefono: ")

    # Solicita el correo electrónico del proveedor.
    correo = input("Correo: ")

    # Valida que el nombre y el producto o servicio no estén vacíos.
    if nombre == "" or producto == "":

        # Muestra un mensaje si faltan datos obligatorios.
        print("Nombre y producto/servicio son obligatorios.")

        # Devuelve False porque no se registró el proveedor.
        return False

    # Lee la lista actual de proveedores desde el archivo JSON.
    proveedores = leer_json(RUTA_PROVEEDORES)

    # Crea un diccionario con la información del nuevo proveedor.
    proveedor = {
        # Guarda el nombre del proveedor.
        "nombre": nombre,

        # Guarda el producto o servicio principal del proveedor.
        "producto": producto,

        # Guarda el teléfono del proveedor.
        "telefono": telefono,

        # Guarda el correo del proveedor.
        "correo": correo,

        # Guarda el usuario que registró al proveedor.
        "creado_por": usuario_actual["usuario"]
    }

    # Agrega el nuevo proveedor a la lista de proveedores.
    proveedores.append(proveedor)

    # Guarda la lista actualizada de proveedores en el archivo JSON.
    guardar_json(RUTA_PROVEEDORES, proveedores)

    # Registra en auditoría la creación del proveedor.
    registrar_auditoria(
        usuario_actual,
        "Registro de proveedor",
        "Se registro el proveedor " + nombre + "."
    )

    # Muestra un mensaje confirmando que el proveedor fue registrado correctamente.
    print("Proveedor registrado correctamente.")

    # Devuelve True para indicar que el registro fue exitoso.
    return True


# Muestra todos los proveedores registrados en el sistema.
def listar_proveedores():

    # Lee la lista de proveedores desde el archivo JSON.
    proveedores = leer_json(RUTA_PROVEEDORES)

    # Muestra el título de la sección de proveedores.
    print("\n===== PROVEEDORES =====")

    # Verifica si no hay proveedores registrados.
    if len(proveedores) == 0:

        # Muestra un mensaje cuando la lista de proveedores está vacía.
        print("No hay proveedores registrados.")

        # Termina la función para evitar recorrer una lista vacía.
        return

    # Inicializa un contador para numerar los proveedores mostrados.
    contador = 1

    # Recorre cada proveedor registrado.
    for proveedor in proveedores:

        # Imprime una línea separadora para ordenar la información visualmente.
        print("--------------------------------")

        # Muestra el número de proveedor y su nombre.
        print(contador, ".", proveedor["nombre"])

        # Muestra el producto o servicio que ofrece el proveedor.
        print("Producto/Servicio:", proveedor["producto"])

        # Muestra el teléfono del proveedor.
        print("Telefono:", proveedor["telefono"])

        # Muestra el correo del proveedor.
        print("Correo:", proveedor["correo"])

        # Muestra qué usuario registró al proveedor.
        print("Creado por:", proveedor["creado_por"])

        # Aumenta el contador para el siguiente proveedor.
        contador = contador + 1


# Permite buscar proveedores por nombre o por producto/servicio.
def buscar_proveedor():

    # Lee la lista de proveedores desde el archivo JSON.
    proveedores = leer_json(RUTA_PROVEEDORES)

    # Muestra el título de la sección de búsqueda de proveedores.
    print("\n===== BUSCAR PROVEEDOR =====")

    # Solicita el texto de búsqueda y lo convierte a minúsculas.
    busqueda = input("Ingrese nombre o producto/servicio: ").lower()

    # Crea una variable para saber si se encontró al menos una coincidencia.
    encontrado = False

    # Recorre cada proveedor registrado.
    for proveedor in proveedores:

        # Verifica si la búsqueda coincide con el nombre o producto del proveedor.
        if busqueda in proveedor["nombre"].lower() or busqueda in proveedor["producto"].lower():

            # Imprime una línea separadora para mostrar el resultado encontrado.
            print("--------------------------------")

            # Muestra el nombre del proveedor encontrado.
            print("Proveedor:", proveedor["nombre"])

            # Muestra el producto o servicio del proveedor encontrado.
            print("Producto/Servicio:", proveedor["producto"])

            # Muestra el teléfono del proveedor encontrado.
            print("Telefono:", proveedor["telefono"])

            # Muestra el correo del proveedor encontrado.
            print("Correo:", proveedor["correo"])

            # Cambia la variable a True porque se encontró una coincidencia.
            encontrado = True

    # Verifica si no se encontró ningún proveedor.
    if not encontrado:

        # Muestra un mensaje indicando que no hubo resultados.
        print("No se encontro ningun proveedor.")


# Muestra el menú principal del módulo de proveedores.
def menu_proveedores(usuario_actual):

    # Mantiene el menú activo hasta que el usuario decida volver.
    while True:

        # Muestra el título del módulo de proveedores.
        print("\n===== MODULO DE PROVEEDORES =====")

        # Muestra la opción para registrar un proveedor.
        print("1. Registrar proveedor")

        # Muestra la opción para listar proveedores.
        print("2. Listar proveedores")

        # Muestra la opción para buscar proveedor.
        print("3. Buscar proveedor")

        # Muestra la opción para regresar al menú anterior.
        print("0. Volver")

        # Solicita al usuario seleccionar una opción.
        opcion = input("Seleccione una opcion: ")

        # Ejecuta el registro de proveedor si el usuario selecciona la opción 1.
        if opcion == "1":
            registrar_proveedor(usuario_actual)

        # Ejecuta el listado de proveedores si el usuario selecciona la opción 2.
        elif opcion == "2":
            listar_proveedores()

        # Ejecuta la búsqueda de proveedor si el usuario selecciona la opción 3.
        elif opcion == "3":
            buscar_proveedor()

        # Sale del menú si el usuario selecciona la opción 0.
        elif opcion == "0":
            break

        # Muestra un mensaje si el usuario ingresa una opción inválida.
        else:
            print("Opcion invalida.")