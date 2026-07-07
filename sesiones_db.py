from db import obtener_conexion  # Importa la función que abre conexión con Neon.


def registrar_sesion(usuario_actual, accion):  # Guarda una acción de sesión en Neon.
    with obtener_conexion() as conexion:  # Abre conexión con Neon y la cierra automáticamente.
        with conexion.cursor() as cursor:  # Crea un cursor para ejecutar SQL.
            cursor.execute(  # Inserta un registro en la tabla sesiones_db.
                """
                INSERT INTO sesiones_db (usuario, accion)
                VALUES (%s, %s)
                """,
                (
                    usuario_actual["usuario"],  # Guarda el nombre del usuario actual.
                    accion  # Guarda la acción realizada, por ejemplo inicio_sesion o cierre_sesion.
                )
            )

        conexion.commit()  # Confirma los cambios en la base de datos.


def mostrar_sesiones():  # Muestra las últimas sesiones registradas.
    with obtener_conexion() as conexion:  # Abre conexión con Neon.
        with conexion.cursor() as cursor:  # Crea cursor para consultar datos.
            cursor.execute(  # Consulta las últimas 20 sesiones.
                """
                SELECT usuario, accion, fecha
                FROM sesiones_db
                ORDER BY fecha DESC
                LIMIT 20
                """
            )

            sesiones = cursor.fetchall()  # Guarda todos los resultados de la consulta.

    print("\n===== HISTORIAL DE SESIONES EN NEON =====")  # Imprime título.

    if len(sesiones) == 0:  # Revisa si no hay registros.
        print("No hay sesiones registradas.")  # Muestra mensaje vacío.
        return  # Sale de la función.

    for sesion in sesiones:  # Recorre cada sesión encontrada.
        usuario, accion, fecha = sesion  # Separa los datos de la fila.
        print("--------------------------------")  # Separador visual.
        print("Usuario:", usuario)  # Muestra usuario.
        print("Acción:", accion)  # Muestra acción.
        print("Fecha:", fecha)  # Muestra fecha.
        