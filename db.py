import os  # Importa funciones del sistema operativo para leer variables de entorno.
import psycopg  # Librería para conectar Python con PostgreSQL/Neon.
from dotenv import load_dotenv  # Permite cargar variables desde el archivo .env.


load_dotenv()  # Carga las variables del archivo .env.


def obtener_conexion():
    # Lee la URL de conexión a Neon desde el archivo .env.
    database_url = os.getenv("DATABASE_URL")

    # Si no existe DATABASE_URL, se detiene el programa con un mensaje claro.
    if not database_url:
        raise ValueError("No se encontró DATABASE_URL en el archivo .env")

    # Devuelve una conexión activa a Neon PostgreSQL.
    return psycopg.connect(database_url)


def inicializar_base_datos():
    # Abre la conexión con Neon.
    with obtener_conexion() as conexion:

        # Crea un cursor para ejecutar SQL.
        with conexion.cursor() as cursor:

            # Crea la tabla principal de usuarios si no existe.
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios_db (
                    id SERIAL PRIMARY KEY,
                    usuario TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    rol TEXT NOT NULL,
                    activo BOOLEAN DEFAULT TRUE,
                    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

            # Agrega columnas nuevas a usuarios_db sin borrar datos existentes.
            cursor.execute("""
                ALTER TABLE usuarios_db
                ADD COLUMN IF NOT EXISTS nombre TEXT;
            """)

            cursor.execute("""
                ALTER TABLE usuarios_db
                ADD COLUMN IF NOT EXISTS correo TEXT UNIQUE;
            """)

            cursor.execute("""
                ALTER TABLE usuarios_db
                ADD COLUMN IF NOT EXISTS carnet TEXT UNIQUE;
            """)

            cursor.execute("""
                ALTER TABLE usuarios_db
                ADD COLUMN IF NOT EXISTS empresa_id INTEGER;
            """)

            cursor.execute("""
                ALTER TABLE usuarios_db
                ADD COLUMN IF NOT EXISTS estado TEXT DEFAULT 'activo';
            """)

            cursor.execute("""
                ALTER TABLE usuarios_db
                ADD COLUMN IF NOT EXISTS fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP;
            """)

            # Crea tabla para registrar sesiones.
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS sesiones_db (
                    id SERIAL PRIMARY KEY,
                    usuario TEXT NOT NULL,
                    accion TEXT NOT NULL,
                    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

            # Crea tabla para auditoría.
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS auditoria_db (
                    id SERIAL PRIMARY KEY,
                    usuario TEXT NOT NULL,
                    accion TEXT NOT NULL,
                    detalle TEXT,
                    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

            # Crea tabla para ingresos y gastos.
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
            """)

            # Inserta usuarios de prueba si no existen.
            cursor.execute("""
                INSERT INTO usuarios_db (usuario, password, rol, nombre, correo, carnet, estado)
                VALUES
                    ('admin', '1234', 'administrador', 'Administrador General', 'admin@finflow.com', 'ADM-0001', 'activo'),
                    ('gerente', '1234', 'gerente', 'Gerente Demo', 'gerente@finflow.com', 'GER-0001', 'activo'),
                    ('contador', '1234', 'contador', 'Contador Demo', 'contador@finflow.com', 'CON-0001', 'activo'),
                    ('empleado', '1234', 'empleado', 'Empleado Demo', 'empleado@finflow.com', 'EMP-0001', 'activo')
                ON CONFLICT (usuario) DO NOTHING;
            """)

        # Guarda los cambios en Neon.
        conexion.commit()

    print("Base de datos Neon inicializada correctamente.")