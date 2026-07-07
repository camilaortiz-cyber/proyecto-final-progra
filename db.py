import os  # Importa funciones del sistema operativo, aquí sirve para leer variables de entorno.
import psycopg  # Importa psycopg, la librería que conecta Python con PostgreSQL/Neon.
from dotenv import load_dotenv  # Importa load_dotenv para cargar las variables guardadas en el archivo .env.


load_dotenv()  # Lee el archivo .env y carga sus variables para que Python pueda usarlas.


def obtener_conexion():  # Define una función para abrir conexión con la base de datos Neon.
    database_url = os.getenv("DATABASE_URL")  # Busca la variable DATABASE_URL dentro del archivo .env.

    if not database_url:  # Valida si DATABASE_URL no existe o está vacía.
        raise ValueError("No se encontró DATABASE_URL en el archivo .env")  # Detiene el programa con un error claro.

    return psycopg.connect(database_url)  # Abre y devuelve una conexión activa hacia Neon PostgreSQL.


def inicializar_base_datos():  # Define una función para crear las tablas necesarias si no existen.
    with obtener_conexion() as conexion:  # Abre conexión con Neon y la cierra automáticamente al terminar.
        with conexion.cursor() as cursor:  # Crea un cursor para ejecutar instrucciones SQL en la base de datos.

            cursor.execute("""  
                CREATE TABLE IF NOT EXISTS usuarios_db (
                    id SERIAL PRIMARY KEY,
                    usuario TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    rol TEXT NOT NULL,
                    activo BOOLEAN DEFAULT TRUE,
                    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)  # Crea la tabla usuarios_db para guardar usuarios, contraseñas, roles y estado activo.

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS sesiones_db (
                    id SERIAL PRIMARY KEY,
                    usuario TEXT NOT NULL,
                    accion TEXT NOT NULL,
                    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)  # Crea la tabla sesiones_db para guardar inicios y cierres de sesión.

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS auditoria_db (
                    id SERIAL PRIMARY KEY,
                    usuario TEXT NOT NULL,
                    accion TEXT NOT NULL,
                    detalle TEXT,
                    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)  # Crea la tabla auditoria_db para registrar acciones importantes de cada usuario.

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS movimientos_db (
                    id SERIAL PRIMARY KEY,
                    tipo TEXT NOT NULL,
                    descripcion TEXT NOT NULL,
                    categoria TEXT NOT NULL,
                    monto NUMERIC(12, 2) NOT NULL,
                    usuario TEXT NOT NULL,
                    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)  # Crea la tabla movimientos_db para guardar ingresos y gastos.

            cursor.execute("""
                INSERT INTO usuarios_db (usuario, password, rol)
                VALUES
                    ('admin', '1234', 'admin'),
                    ('gerente', '1234', 'gerente'),
                    ('contador', '1234', 'contador'),
                    ('empleado', '1234', 'empleado')
                ON CONFLICT (usuario) DO NOTHING;
            """)  # Inserta usuarios de prueba, pero no duplica si ya existen.

        conexion.commit()  # Guarda oficialmente todos los cambios hechos en la base de datos.

    print("Base de datos Neon inicializada correctamente.")  # Muestra mensaje cuando todo salió bien.

    