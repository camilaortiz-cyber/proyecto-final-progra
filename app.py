import os
# Importa Flask, que permite crear una aplicación web en Python.
# Flask será el servidor que conectará la página web con la base de datos Neon.
from flask import Flask, request, jsonify, send_from_directory

# Importa CORS para permitir que el frontend pueda comunicarse con la API.
# Esto ayuda cuando la página web hace peticiones HTTP al backend.
from flask_cors import CORS

# Importa las funciones de db.py:
# obtener_conexion abre una conexión con Neon.
# inicializar_base_datos crea o actualiza las tablas necesarias.
from db import obtener_conexion, inicializar_base_datos
from admin_usuarios_db import crear_usuario_neon


# Crea la aplicación principal de Flask.
# static_folder="web" indica que los archivos HTML, CSS y JS están dentro de la carpeta web.
# static_url_path="" permite servir esos archivos desde la raíz del sitio.
app = Flask(__name__, static_folder="web", static_url_path="")

# Activa CORS en la aplicación.
# Esto permite que el navegador pueda hacer peticiones a la API sin bloqueos de origen.
CORS(app)


# Ruta principal de la aplicación web.
# Cuando el usuario entra a http://127.0.0.1:5000/,
# Flask devuelve el archivo index.html de la carpeta web.
@app.route("/")
def inicio():

    # Envía el archivo index.html como página inicial.
    return send_from_directory("web", "index.html")


# Ruta de API para iniciar sesión desde la página web.
# Esta ruta recibe datos por POST desde el formulario de login del frontend.
@app.route("/api/login", methods=["POST"])
def login_web():

    # Obtiene los datos enviados desde JavaScript en formato JSON.
    datos = request.get_json()

    # Extrae el usuario del JSON.
    # Si no viene, usa una cadena vacía.
    # strip() elimina espacios al inicio y al final.
    usuario = datos.get("usuario", "").strip()

    # Extrae la contraseña del JSON.
    # Si no viene, usa una cadena vacía.
    password = datos.get("password", "").strip()

    # Valida que el usuario y la contraseña no estén vacíos.
    if usuario == "" or password == "":

        # Devuelve una respuesta JSON indicando error.
        # El código 400 significa solicitud incorrecta.
        return jsonify({
            "success": False,
            "message": "Usuario y contraseña son obligatorios."
        }), 400

    # Abre una conexión con la base de datos Neon.
    with obtener_conexion() as conexion:

        # Crea un cursor para ejecutar consultas SQL.
        with conexion.cursor() as cursor:

            # Busca en usuarios_db una cuenta que coincida con el usuario y la contraseña.
            # Se seleccionan los datos necesarios para devolverlos al frontend.
            cursor.execute(
                """
                SELECT
                    id,
                    usuario,
                    rol,
                    activo,
                    estado,
                    nombre,
                    correo,
                    carnet,
                    empresa_id
                FROM usuarios_db
                WHERE usuario = %s
                  AND password = %s;
                """,
                (usuario, password)
            )

            # Obtiene el primer resultado encontrado.
            # Si no existe una coincidencia, devuelve None.
            cuenta = cursor.fetchone()

    # Si no se encontró ninguna cuenta, las credenciales son incorrectas.
    if cuenta is None:

        # Devuelve error de autenticación.
        # El código 401 significa no autorizado.
        return jsonify({
            "success": False,
            "message": "Usuario o contraseña incorrectos."
        }), 401

    # Extrae el estado activo desde la posición 3 del resultado.
    activo = cuenta[3]

    # Extrae el estado textual desde la posición 4 del resultado.
    estado = cuenta[4]

    # Verifica si el usuario está desactivado.
    # Si activo es False o estado es "inactivo", no se permite el acceso.
    if activo is False or estado == "inactivo":

        # Devuelve error indicando que el usuario no puede ingresar.
        # El código 403 significa acceso prohibido.
        return jsonify({
            "success": False,
            "message": "Este usuario está inactivo."
        }), 403

    # Si todo está correcto, devuelve una respuesta exitosa.
    # También envía al frontend los datos principales del usuario autenticado.
    return jsonify({
        "success": True,
        "message": "Inicio de sesión exitoso.",
        "user": {
            "id": cuenta[0],
            "usuario": cuenta[1],
            "rol": cuenta[2],
            "activo": cuenta[3],
            "estado": cuenta[4],
            "nombre": cuenta[5],
            "correo": cuenta[6],
            "carnet": cuenta[7],
            "empresa_id": cuenta[8]
        }
    })


# Ruta de API para listar usuarios desde la página web.
# Esta ruta sirve para que un administrador pueda ver usuarios registrados en Neon.
@app.route("/api/usuarios", methods=["GET"])
def listar_usuarios_web():

    # Abre una conexión con Neon.
    with obtener_conexion() as conexion:

        # Crea un cursor para ejecutar la consulta.
        with conexion.cursor() as cursor:

            # Consulta todos los usuarios registrados en la tabla usuarios_db.
            # No se selecciona password para no mostrar contraseñas en el frontend.
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

            # Obtiene todos los usuarios encontrados.
            usuarios = cursor.fetchall()

    # Crea una lista vacía para convertir los resultados SQL a diccionarios.
    lista = []

    # Recorre cada usuario obtenido desde Neon.
    for usuario in usuarios:

        # Agrega cada usuario como diccionario.
        # Esto facilita convertirlo a JSON para JavaScript.
        lista.append({
            "id": usuario[0],
            "nombre": usuario[1],
            "correo": usuario[2],
            "usuario": usuario[3],
            "rol": usuario[4],
            "carnet": usuario[5],
            "empresa_id": usuario[6],
            "estado": usuario[7],

            # Convierte fecha_creacion a texto porque JSON no maneja datetime directamente.
            "fecha_creacion": str(usuario[8])
        })

    # Devuelve la lista completa de usuarios en formato JSON.
    return jsonify(lista)


# Este bloque se ejecuta solamente cuando se corre directamente:
# python3 app.py

# Ruta de API para crear usuarios desde la página web.
# Esta ruta recibe una petición POST desde el formulario visual de administración de usuarios.
# Solo permite crear usuarios si quien realiza la acción tiene rol de administrador.
@app.route("/api/usuarios", methods=["POST"])
def crear_usuario_web():

    # Obtiene los datos enviados desde JavaScript en formato JSON.
    datos = request.get_json()

    # Obtiene la información del usuario administrador que inició sesión.
    # Este dato viene desde el frontend para validar permisos.
    admin_actual = datos.get("admin_actual", {})

    # Extrae el rol del administrador actual.
    # Se convierte a minúsculas y se eliminan espacios para evitar errores de formato.
    rol_admin = admin_actual.get("rol", "").lower().strip()

    # Valida que solo usuarios con rol admin o administrador puedan crear usuarios.
    if rol_admin not in ["admin", "administrador"]:
        return jsonify({
            "success": False,
            "message": "Solo un administrador puede crear usuarios."
        }), 403

    # Extrae el nombre completo del nuevo usuario.
    nombre = datos.get("nombre", "").strip()

    # Extrae el correo del nuevo usuario.
    correo = datos.get("correo", "").strip()

    # Extrae el nombre de usuario que se usará para iniciar sesión.
    usuario = datos.get("usuario", "").strip()

    # Extrae la contraseña del nuevo usuario.
    password = datos.get("password", "").strip()

    # Extrae el rol del nuevo usuario.
    # Puede ser administrador, gerente, contador o empleado.
    rol = datos.get("rol", "").strip().lower()

    # Extrae el ID de empresa.
    # Este campo es opcional, por eso puede venir vacío o como None.
    empresa_id = datos.get("empresa_id", None)

    # Si empresa_id viene vacío, se guarda como None.
    # En PostgreSQL esto equivale a NULL.
    if empresa_id == "":
        empresa_id = None

    # Si empresa_id trae algo, se intenta convertir a número entero.
    # Esto evita guardar texto en una columna que espera números.
    elif empresa_id is not None:
        try:
            empresa_id = int(empresa_id)

        # Si no se puede convertir a entero, se devuelve un mensaje claro al frontend.
        except ValueError:
            return jsonify({
                "success": False,
                "message": "Empresa ID debe ser un número o dejarse vacío."
            }), 400

    # Intenta crear el usuario en Neon usando la función central de admin_usuarios_db.py.
    try:
        exito, mensaje = crear_usuario_neon(
            nombre,
            correo,
            usuario,
            password,
            rol,
            empresa_id
        )

    # Si ocurre un error inesperado, se devuelve al frontend para poder verlo.
    except Exception as error:
        return jsonify({
            "success": False,
            "message": "No se pudo crear el usuario: " + str(error)
        }), 500

    # Si la función crear_usuario_neon devuelve False,
    # significa que hubo una validación fallida:
    # usuario duplicado, correo duplicado, rol inválido, campos vacíos, etc.
    if not exito:
        return jsonify({
            "success": False,
            "message": mensaje
        }), 400

    # Si todo salió bien, devuelve success True y el mensaje de confirmación.
    # Ejemplo: Usuario creado correctamente con carnet ADM-0002.
    return jsonify({
        "success": True,
        "message": mensaje
    })

if __name__ == "__main__":
    inicializar_base_datos()

    port = int(os.environ.get("PORT", 5050))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
