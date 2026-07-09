# Importa las funciones para leer y guardar datos en archivos JSON.
from data_manager import leer_json, guardar_json

# Importa la función para registrar acciones importantes en el historial de auditoría.
from auditoria import registrar_auditoria


# Define la ruta del archivo donde se almacenan las empresas registradas.
RUTA_EMPRESAS = "data/empresas.json"


# Permite crear una nueva empresa dentro del sistema.
def crear_empresa(usuario_actual):

    # Muestra el título de la sección para crear empresas.
    print("\n===== CREAR EMPRESA =====")

    # Solicita el nombre de la empresa.
    nombre = input("Nombre de la empresa: ")

    # Solicita el NIT de la empresa.
    nit = input("NIT: ")

    # Solicita el sector al que pertenece la empresa.
    sector = input("Sector: ")

    # Solicita el número de teléfono de la empresa.
    telefono = input("Telefono: ")

    # Valida que los campos obligatorios no estén vacíos.
    if nombre == "" or nit == "" or sector == "":

        # Muestra un mensaje indicando cuáles datos son obligatorios.
        print("Nombre, NIT y sector son obligatorios.")

        # Detiene el proceso y devuelve False porque no se creó la empresa.
        return False

    # Lee la lista actual de empresas desde el archivo JSON.
    empresas = leer_json(RUTA_EMPRESAS)

    # Crea un diccionario con la información de la nueva empresa.
    empresa = {
        # Guarda el nombre de la empresa.
        "nombre": nombre,

        # Guarda el NIT de la empresa.
        "nit": nit,

        # Guarda el sector de la empresa.
        "sector": sector,

        # Guarda el teléfono de la empresa.
        "telefono": telefono,

        # Guarda el usuario que creó el registro de la empresa.
        "creado_por": usuario_actual["usuario"]
    }

    # Agrega la nueva empresa a la lista de empresas.
    empresas.append(empresa)

    # Guarda la lista actualizada de empresas en el archivo JSON.
    guardar_json(RUTA_EMPRESAS, empresas)

    # Registra en auditoría la creación de la empresa.
    registrar_auditoria(
        usuario_actual,
        "Creacion de empresa",
        "Se creo la empresa " + nombre + "."
    )

    # Muestra un mensaje confirmando que la empresa fue creada correctamente.
    print("Empresa creada correctamente.")

    # Devuelve True para indicar que la empresa fue registrada exitosamente.
    return True


# Muestra todas las empresas registradas en el sistema.
def listar_empresas():

    # Lee la lista de empresas desde el archivo JSON.
    empresas = leer_json(RUTA_EMPRESAS)

    # Muestra el título de la sección de empresas registradas.
    print("\n===== EMPRESAS REGISTRADAS =====")

    # Verifica si no hay empresas registradas.
    if len(empresas) == 0:

        # Muestra un mensaje cuando la lista de empresas está vacía.
        print("No hay empresas registradas.")

        # Termina la función para evitar recorrer una lista vacía.
        return

    # Inicializa un contador para numerar las empresas mostradas.
    contador = 1

    # Recorre cada empresa registrada.
    for empresa in empresas:

        # Imprime una línea separadora para ordenar la información visualmente.
        print("--------------------------------")

        # Muestra el número de registro y el nombre de la empresa.
        print(contador, ".", empresa["nombre"])

        # Muestra el NIT de la empresa.
        print("NIT:", empresa["nit"])

        # Muestra el sector de la empresa.
        print("Sector:", empresa["sector"])

        # Muestra el teléfono de la empresa.
        print("Telefono:", empresa["telefono"])

        # Muestra el usuario que creó el registro.
        print("Creado por:", empresa["creado_por"])

        # Aumenta el contador para la siguiente empresa.
        contador = contador + 1


# Permite buscar una empresa por nombre o por NIT.
def buscar_empresa():

    # Lee la lista de empresas desde el archivo JSON.
    empresas = leer_json(RUTA_EMPRESAS)

    # Muestra el título de la sección de búsqueda de empresas.
    print("\n===== BUSCAR EMPRESA =====")

    # Solicita el nombre o NIT a buscar y lo convierte a minúsculas.
    busqueda = input("Ingrese nombre o NIT: ").lower()

    # Crea una variable para controlar si se encontró alguna coincidencia.
    encontrado = False

    # Recorre cada empresa registrada.
    for empresa in empresas:

        # Verifica si la búsqueda coincide con el nombre o el NIT de la empresa.
        if busqueda in empresa["nombre"].lower() or busqueda in empresa["nit"].lower():

            # Imprime una línea separadora para mostrar el resultado encontrado.
            print("--------------------------------")

            # Muestra el nombre de la empresa encontrada.
            print("Empresa:", empresa["nombre"])

            # Muestra el NIT de la empresa encontrada.
            print("NIT:", empresa["nit"])

            # Muestra el sector de la empresa encontrada.
            print("Sector:", empresa["sector"])

            # Muestra el teléfono de la empresa encontrada.
            print("Telefono:", empresa["telefono"])

            # Cambia la variable a True porque sí se encontró una empresa.
            encontrado = True

    # Verifica si no se encontró ninguna coincidencia.
    if not encontrado:

        # Muestra un mensaje indicando que no se encontró ninguna empresa.
        print("No se encontro ninguna empresa.")


# Muestra el menú principal del módulo de empresas.
def menu_empresas(usuario_actual):

    # Mantiene activo el menú hasta que el usuario decida volver.
    while True:

        # Muestra el título del módulo de empresas.
        print("\n===== MODULO DE EMPRESAS =====")

        # Muestra la opción para crear una empresa.
        print("1. Crear empresa")

        # Muestra la opción para listar empresas.
        print("2. Listar empresas")

        # Muestra la opción para buscar empresas.
        print("3. Buscar empresa")

        # Muestra la opción para regresar al menú anterior.
        print("0. Volver")

        # Solicita al usuario que seleccione una opción.
        opcion = input("Seleccione una opcion: ")

        # Ejecuta la función para crear empresa si el usuario selecciona la opción 1.
        if opcion == "1":
            crear_empresa(usuario_actual)

        # Ejecuta la función para listar empresas si el usuario selecciona la opción 2.
        elif opcion == "2":
            listar_empresas()

        # Ejecuta la función para buscar empresa si el usuario selecciona la opción 3.
        elif opcion == "3":
            buscar_empresa()

        # Sale del menú si el usuario selecciona la opción 0.
        elif opcion == "0":
            break

        # Muestra un mensaje si el usuario ingresa una opción inválida.
        else:
            print("Opcion invalida.")