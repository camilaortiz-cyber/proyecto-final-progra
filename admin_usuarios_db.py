# Importa datetime para guardar la fecha y hora exacta de creación del usuario.
from datetime import datetime

# Importa la función que abre la conexión con la base de datos Neon.
from db import obtener_conexion


# Normaliza el rol recibido para manejar nombres equivalentes.
# Por ejemplo, si alguien escribe "admin", el sistema lo convierte a "administrador".
def normalizar_rol(rol):

    # Convierte el texto del rol a minúsculas y elimina espacios al inicio o final.
    rol = rol.lower().strip()

    # Si el rol viene como "admin", se transforma a "administrador"
    # para mantener un solo nombre estándar dentro del sistema.
    if rol == "admin":
        return "administrador"

    # Si el rol no necesita cambios, se devuelve tal como quedó normalizado.
    return rol


# Obtiene el prefijo que se usará para generar el carnet del usuario.
# Cada rol tiene un prefijo distinto para identificarlo fácilmente.
def obtener_prefijo_carnet(rol):

    # Normaliza el rol antes de comparar.
    rol = normalizar_rol(rol)

    # Prefijo para usuarios administradores.
    if rol == "administrador":
        return "ADM"

    # Prefijo para usuarios gerentes.
    if rol == "gerente":
        return "GER"

    # Prefijo para usuarios contadores.
    if rol == "contador":
        return "CON"

    # Prefijo para usuarios empleados.
    if rol == "empleado":
        return "EMP"

    # Prefijo genérico por si en el futuro se agrega otro tipo de usuario.
    return "USR"


# Genera automáticamente un carnet para el nuevo usuario.
# El carnet se compone de un prefijo según el rol y un número correlativo.
# Ejemplo: EMP-0001, CON-0002, GER-0001, ADM-0001.
def generar_carnet(rol):

    # Obtiene el prefijo correspondiente al rol.
    prefijo = obtener_prefijo_carnet(rol)

    # Abre una conexión con Neon.
    with obtener_conexion() as conexion:

        # Crea un cursor para ejecutar consultas SQL.
        with conexion.cursor() as cursor:

            # Cuenta cuántos carnets existen con el mismo prefijo.
            # Por ejemplo, si el rol es empleado, busca todos los carnets EMP-%.
            cursor.execute(
                """
                SELECT COUNT(*)
                FROM usuarios_db
                WHERE carnet LIKE %s;
                """,
                (prefijo + "-%",)
            )

            # Obtiene la cantidad actual y le suma 1 para crear el siguiente número.
            cantidad = cursor.fetchone()[0] + 1

    # Construye el carnet final usando el prefijo y un número de 4 dígitos.
    # zfill(4) rellena con ceros a la izquierda.
    # Ejemplo: 1 se vuelve 0001.
    return prefijo + "-" + str(cantidad).zfill(4)


# Verifica si un nombre de usuario ya existe en la base de datos Neon.
# Esto evita duplicar usuarios con el mismo username.
def usuario_existe_neon(usuario):

    # Abre una conexión con Neon.
    with obtener_conexion() as conexion:

        # Crea un cursor para ejecutar la consulta.
        with conexion.cursor() as cursor:

            # Busca un usuario con el mismo nombre de usuario.
            cursor.execute(
                """
                SELECT id
                FROM usuarios_db
                WHERE usuario = %s;
                """,
                (usuario,)
            )

            # fetchone devuelve un registro si lo encuentra, o None si no existe.
            resultado = cursor.fetchone()

    # Si resultado no es None, significa que el usuario ya existe.
    return resultado is not None


# Verifica si un correo ya existe en la base de datos Neon.
# Esto evita que dos usuarios tengan el mismo correo.
def correo_existe_neon(correo):

    # Abre una conexión con Neon.
    with obtener_conexion() as conexion:

        # Crea un cursor para ejecutar la consulta.
        with conexion.cursor() as cursor:

            # Busca un registro con el correo recibido.
            cursor.execute(
                """
                SELECT id
                FROM usuarios_db
                WHERE correo = %s;
                """,
                (correo,)
            )

            # Guarda el resultado de la búsqueda.
            resultado = cursor.fetchone()

    # Devuelve True si el correo ya existe, False si está disponible.
    return resultado is not None


# Crea un nuevo usuario en Neon.
# Recibe los datos ingresados desde el menú de administrador.
def crear_usuario_neon(nombre, correo, usuario, password, rol, empresa_id):

    # Normaliza el rol para evitar inconsistencias entre "admin" y "administrador".
    rol = normalizar_rol(rol)

    # Valida que el rol sea uno de los permitidos por la plataforma.
    if rol not in ["administrador", "gerente", "contador", "empleado"]:
        return False, "Rol inválido."

    # Valida que los campos principales no estén vacíos.
    if nombre == "" or correo == "" or usuario == "" or password == "":
        return False, "Nombre, correo, usuario y contraseña son obligatorios."

    # Valida que no exista otro usuario con el mismo username.
    if usuario_existe_neon(usuario):
        return False, "Ese nombre de usuario ya existe."

    # Valida que no exista otro usuario con el mismo correo.
    if correo_existe_neon(correo):
        return False, "Ese correo ya está registrado."

    # Genera automáticamente el carnet según el rol del usuario.
    carnet = generar_carnet(rol)

    # Abre una conexión con Neon.
    with obtener_conexion() as conexion:

        # Crea un cursor para insertar el nuevo usuario.
        with conexion.cursor() as cursor:

            # Inserta el usuario en la tabla usuarios_db.
            # activo se guarda como TRUE.
            # estado se guarda como 'activo'.
            # fecha_creacion se guarda con la fecha y hora actual.
            cursor.execute(
                """
                INSERT INTO usuarios_db
                (
                    nombre,
                    correo,
                    usuario,
                    password,
                    rol,
                    carnet,
                    empresa_id,
                    activo,
                    estado,
                    fecha_creacion
                )
                VALUES
                (
                    %s, %s, %s, %s, %s, %s, %s, TRUE, 'activo', %s
                );
                """,
                (
                    nombre,
                    correo,
                    usuario,
                    password,
                    rol,
                    carnet,
                    empresa_id,
                    datetime.now()
                )
            )

        # Confirma oficialmente los cambios en la base de datos.
        conexion.commit()

    # Devuelve True y un mensaje de éxito con el carnet generado.
    return True, "Usuario creado correctamente con carnet " + carnet + "."


# Lista todos los usuarios guardados en Neon.
# Muestra información importante, pero no muestra la contraseña por seguridad.
def listar_usuarios_neon():

    # Abre una conexión con Neon.
    with obtener_conexion() as conexion:

        # Crea un cursor para consultar usuarios.
        with conexion.cursor() as cursor:

            # Obtiene todos los usuarios ordenados por ID.
            cursor.execute(
                """
                SELECT
                    id,
                    nombre,
                    correo,
                    usuario,
                    rol,
                    carnet,
                    empresa_id,
                    estado,
                    fecha_creacion
                FROM usuarios_db
                ORDER BY id ASC;
                """
            )

            # fetchall obtiene todos los registros encontrados.
            usuarios = cursor.fetchall()

    # Título visual del listado.
    print("\n===== USUARIOS REGISTRADOS EN NEON =====")

    # Si no hay usuarios registrados, muestra un mensaje y termina la función.
    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
        return

    # Recorre cada usuario y muestra sus datos principales.
    for usuario in usuarios:
        print("--------------------------------")
        print("ID:", usuario[0])
        print("Nombre:", usuario[1])
        print("Correo:", usuario[2])
        print("Usuario:", usuario[3])
        print("Rol:", usuario[4])
        print("Carnet:", usuario[5])
        print("Empresa ID:", usuario[6])
        print("Estado:", usuario[7])
        print("Fecha creación:", usuario[8])


# Busca usuarios en Neon por nombre de usuario, correo o carnet.
def buscar_usuario_neon():

    # Solicita al administrador el dato a buscar.
    busqueda = input("Ingrese usuario, correo o carnet: ").strip()

    # Abre una conexión con Neon.
    with obtener_conexion() as conexion:

        # Crea un cursor para ejecutar la búsqueda.
        with conexion.cursor() as cursor:

            # Busca coincidencias parciales usando ILIKE.
            # ILIKE permite buscar sin importar mayúsculas o minúsculas.
            # Los signos % permiten encontrar coincidencias aunque el texto esté incompleto.
            cursor.execute(
                """
                SELECT
                    id,
                    nombre,
                    correo,
                    usuario,
                    rol,
                    carnet,
                    empresa_id,
                    estado,
                    fecha_creacion
                FROM usuarios_db
                WHERE usuario ILIKE %s
                   OR correo ILIKE %s
                   OR carnet ILIKE %s
                ORDER BY id ASC;
                """,
                (
                    "%" + busqueda + "%",
                    "%" + busqueda + "%",
                    "%" + busqueda + "%"
                )
            )

            # Guarda todos los usuarios que coinciden con la búsqueda.
            usuarios = cursor.fetchall()

    # Título visual de resultados.
    print("\n===== RESULTADOS DE BÚSQUEDA =====")

    # Si no se encontró ningún usuario, muestra mensaje y termina.
    if len(usuarios) == 0:
        print("No se encontró ningún usuario.")
        return

    # Muestra los datos de cada usuario encontrado.
    for usuario in usuarios:
        print("--------------------------------")
        print("ID:", usuario[0])
        print("Nombre:", usuario[1])
        print("Correo:", usuario[2])
        print("Usuario:", usuario[3])
        print("Rol:", usuario[4])
        print("Carnet:", usuario[5])
        print("Empresa ID:", usuario[6])
        print("Estado:", usuario[7])
        print("Fecha creación:", usuario[8])


# Desactiva un usuario en Neon.
# No elimina el registro, solo cambia su estado a inactivo.
def desactivar_usuario_neon():

    # Solicita el username del usuario que se quiere desactivar.
    usuario = input("Ingrese el usuario que desea desactivar: ").strip()

    # Abre una conexión con Neon.
    with obtener_conexion() as conexion:

        # Crea un cursor para actualizar el usuario.
        with conexion.cursor() as cursor:

            # Cambia activo a FALSE y estado a 'inactivo'.
            cursor.execute(
                """
                UPDATE usuarios_db
                SET activo = FALSE,
                    estado = 'inactivo'
                WHERE usuario = %s;
                """,
                (usuario,)
            )

            # rowcount indica cuántas filas fueron modificadas.
            filas_afectadas = cursor.rowcount

        # Guarda los cambios en Neon.
        conexion.commit()

    # Si no se modificó ninguna fila, significa que el usuario no existe.
    if filas_afectadas == 0:
        print("No se encontró ese usuario.")
    else:
        print("Usuario desactivado correctamente.")


# Activa nuevamente un usuario desactivado.
# Cambia su estado a activo para que pueda seguir siendo usado.
def activar_usuario_neon():

    # Solicita el username del usuario que se quiere activar.
    usuario = input("Ingrese el usuario que desea activar: ").strip()

    # Abre una conexión con Neon.
    with obtener_conexion() as conexion:

        # Crea un cursor para actualizar el usuario.
        with conexion.cursor() as cursor:

            # Cambia activo a TRUE y estado a 'activo'.
            cursor.execute(
                """
                UPDATE usuarios_db
                SET activo = TRUE,
                    estado = 'activo'
                WHERE usuario = %s;
                """,
                (usuario,)
            )

            # Guarda cuántas filas fueron modificadas.
            filas_afectadas = cursor.rowcount

        # Confirma el cambio en la base de datos.
        conexion.commit()

    # Si no encontró el usuario, informa al administrador.
    if filas_afectadas == 0:
        print("No se encontró ese usuario.")
    else:
        print("Usuario activado correctamente.")


# Muestra el menú principal para administrar usuarios guardados en Neon.
# Solo permite acceso si el usuario actual es administrador.
def menu_admin_usuarios_neon(usuario_actual):

    # Normaliza el rol del usuario que inició sesión.
    rol_actual = normalizar_rol(usuario_actual["rol"])

    # Valida que solo un administrador pueda entrar a este menú.
    if rol_actual != "administrador":
        print("No tiene permiso para administrar usuarios.")
        return

    # Mantiene el menú activo hasta que el administrador seleccione volver.
    while True:

        # Muestra las opciones disponibles.
        print("\n===== ADMINISTRACIÓN DE USUARIOS NEON =====")
        print("1. Crear nuevo usuario")
        print("2. Listar usuarios")
        print("3. Buscar usuario")
        print("4. Desactivar usuario")
        print("5. Activar usuario")
        print("0. Volver")

        # Solicita una opción al administrador.
        opcion = input("Seleccione una opción: ")

        # Opción 1: crear usuario nuevo.
        if opcion == "1":
            print("\n===== CREAR USUARIO =====")

            # Solicita los datos principales del nuevo usuario.
            nombre = input("Nombre completo: ").strip()
            correo = input("Correo: ").strip()
            usuario = input("Usuario: ").strip()
            password = input("Contraseña: ").strip()

            # Muestra roles disponibles para evitar errores de escritura.
            print("\nRoles disponibles:")
            print("1. administrador")
            print("2. gerente")
            print("3. contador")
            print("4. empleado")

            # Permite elegir el rol por número o escribiendo el nombre.
            rol_opcion = input("Rol: ").strip().lower()

            # Convierte la opción numérica en el texto del rol.
            if rol_opcion == "1":
                rol = "administrador"
            elif rol_opcion == "2":
                rol = "gerente"
            elif rol_opcion == "3":
                rol = "contador"
            elif rol_opcion == "4":
                rol = "empleado"
            else:
                # Si no escribió un número, usa el texto ingresado.
                rol = rol_opcion

            # Solicita el ID de la empresa.
            # Puede dejarse vacío si todavía no se está asociando a una empresa.
            empresa_texto = input("Empresa ID, dejar vacío si no aplica: ").strip()

            # Si no escribió nada, empresa_id se guarda como None.
            # En PostgreSQL esto se guarda como NULL.
            if empresa_texto == "":
                empresa_id = None
            else:
                try:
                    # Convierte el texto ingresado a número entero.
                    empresa_id = int(empresa_texto)
                except ValueError:
                    # Si no se puede convertir, muestra error y vuelve al menú.
                    print("Empresa ID debe ser numérico.")
                    continue

            # Llama a la función que guarda el usuario en Neon.
            exito, mensaje = crear_usuario_neon(
                nombre,
                correo,
                usuario,
                password,
                rol,
                empresa_id
            )

            # Muestra el mensaje devuelto por la función.
            print(mensaje)

        # Opción 2: listar todos los usuarios.
        elif opcion == "2":
            listar_usuarios_neon()

        # Opción 3: buscar un usuario.
        elif opcion == "3":
            buscar_usuario_neon()

        # Opción 4: desactivar un usuario.
        elif opcion == "4":
            desactivar_usuario_neon()

        # Opción 5: activar un usuario.
        elif opcion == "5":
            activar_usuario_neon()

        # Opción 0: volver al menú principal.
        elif opcion == "0":
            break

        # Cualquier otra opción se considera inválida.
        else:
            print("Opción inválida.") 
            