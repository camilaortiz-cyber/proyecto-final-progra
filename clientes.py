# Importa las funciones para leer y guardar información en archivos JSON.
from data_manager import leer_json, guardar_json

# Importa la función para registrar acciones importantes en el historial de auditoría.
from auditoria import registrar_auditoria


# Define la ruta del archivo donde se almacenan los clientes.
RUTA_CLIENTES = "data/clientes.json"


# Permite registrar un nuevo cliente en el sistema.
def registrar_cliente(usuario_actual):

    # Muestra el título de la sección de registro de clientes.
    print("\n===== REGISTRAR CLIENTE =====")

    # Solicita el nombre del cliente.
    nombre = input("Nombre del cliente: ")

    # Solicita el número de teléfono del cliente.
    telefono = input("Telefono: ")

    # Solicita el correo electrónico del cliente.
    correo = input("Correo: ")

    # Solicita la empresa relacionada con el cliente.
    empresa = input("Empresa relacionada: ")

    # Valida que el nombre del cliente no esté vacío.
    if nombre == "":

        # Muestra un mensaje de error si el nombre no fue ingresado.
        print("El nombre del cliente es obligatorio.")

        # Detiene el registro y devuelve False porque no se guardó el cliente.
        return False

    # Lee la lista actual de clientes desde el archivo JSON.
    clientes = leer_json(RUTA_CLIENTES)

    # Crea un diccionario con la información del cliente nuevo.
    cliente = {
        # Guarda el nombre del cliente.
        "nombre": nombre,

        # Guarda el teléfono del cliente.
        "telefono": telefono,

        # Guarda el correo del cliente.
        "correo": correo,

        # Guarda la empresa relacionada con el cliente.
        "empresa": empresa,

        # Guarda el usuario que registró al cliente.
        "creado_por": usuario_actual["usuario"]
    }

    # Agrega el nuevo cliente a la lista de clientes.
    clientes.append(cliente)

    # Guarda la lista actualizada de clientes en el archivo JSON.
    guardar_json(RUTA_CLIENTES, clientes)

    # Registra la acción en el historial de auditoría del sistema.
    registrar_auditoria(
        usuario_actual,
        "Registro de cliente",
        "Se registro el cliente " + nombre + "."
    )

    # Muestra un mensaje confirmando que el cliente fue registrado correctamente.
    print("Cliente registrado correctamente.")

    # Devuelve True para indicar que el registro fue exitoso.
    return True


# Muestra todos los clientes registrados en el sistema.
def listar_clientes():

    # Lee la lista de clientes desde el archivo JSON.
    clientes = leer_json(RUTA_CLIENTES)

    # Muestra el título de la sección de clientes.
    print("\n===== CLIENTES =====")

    # Verifica si no hay clientes registrados.
    if len(clientes) == 0:

        # Muestra un mensaje cuando la lista de clientes está vacía.
        print("No hay clientes registrados.")

        # Termina la función para no recorrer una lista vacía.
        return

    # Inicializa un contador para numerar los clientes en pantalla.
    contador = 1

    # Recorre cada cliente registrado.
    for cliente in clientes:

        # Imprime una línea separadora para ordenar la información visualmente.
        print("--------------------------------")

        # Muestra el número del cliente y su nombre.
        print(contador, ".", cliente["nombre"])

        # Muestra el teléfono del cliente.
        print("Telefono:", cliente["telefono"])

        # Muestra el correo del cliente.
        print("Correo:", cliente["correo"])

        # Muestra la empresa relacionada con el cliente.
        print("Empresa:", cliente["empresa"])

        # Muestra qué usuario registró al cliente.
        print("Creado por:", cliente["creado_por"])

        # Aumenta el contador para el siguiente cliente.
        contador = contador + 1


# Permite buscar clientes por coincidencia en el nombre.
def buscar_cliente():

    # Lee la lista de clientes desde el archivo JSON.
    clientes = leer_json(RUTA_CLIENTES)

    # Muestra el título de la sección de búsqueda de clientes.
    print("\n===== BUSCAR CLIENTE =====")

    # Solicita el nombre o parte del nombre a buscar y lo convierte a minúsculas.
    busqueda = input("Ingrese nombre del cliente: ").lower()

    # Crea una variable de control para saber si se encontró algún cliente.
    encontrado = False

    # Recorre cada cliente registrado.
    for cliente in clientes:

        # Compara la búsqueda con el nombre del cliente, sin importar mayúsculas o minúsculas.
        if busqueda in cliente["nombre"].lower():

            # Imprime una línea separadora para mostrar el resultado encontrado.
            print("--------------------------------")

            # Muestra el nombre del cliente encontrado.
            print("Cliente:", cliente["nombre"])

            # Muestra el teléfono del cliente encontrado.
            print("Telefono:", cliente["telefono"])

            # Muestra el correo del cliente encontrado.
            print("Correo:", cliente["correo"])

            # Muestra la empresa relacionada con el cliente encontrado.
            print("Empresa:", cliente["empresa"])

            # Cambia la variable a True para indicar que sí hubo coincidencias.
            encontrado = True

    # Verifica si no se encontró ningún cliente.
    if not encontrado:

        # Muestra un mensaje indicando que no hubo resultados.
        print("No se encontro ningun cliente.")


# Muestra el menú principal del módulo de clientes.
def menu_clientes(usuario_actual):

    # Mantiene el menú activo hasta que el usuario decida volver.
    while True:

        # Muestra el título del módulo de clientes.
        print("\n===== MODULO DE CLIENTES =====")

        # Muestra la opción para registrar un cliente.
        print("1. Registrar cliente")

        # Muestra la opción para listar todos los clientes.
        print("2. Listar clientes")

        # Muestra la opción para buscar un cliente.
        print("3. Buscar cliente")

        # Muestra la opción para regresar al menú anterior.
        print("0. Volver")

        # Solicita al usuario que seleccione una opción del menú.
        opcion = input("Seleccione una opcion: ")

        # Ejecuta el registro de cliente si el usuario selecciona la opción 1.
        if opcion == "1":
            registrar_cliente(usuario_actual)

        # Ejecuta el listado de clientes si el usuario selecciona la opción 2.
        elif opcion == "2":
            listar_clientes()

        # Ejecuta la búsqueda de cliente si el usuario selecciona la opción 3.
        elif opcion == "3":
            buscar_cliente()

        # Sale del menú si el usuario selecciona la opción 0.
        elif opcion == "0":
            break

        # Muestra un mensaje si el usuario ingresa una opción no válida.
        else:
            print("Opcion invalida.")