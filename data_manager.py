# Importa la librería json para poder leer y escribir datos en formato JSON.
import json

# Importa la librería os para verificar si existen archivos o rutas en el sistema.
import os


# Lee información desde un archivo JSON.
def leer_json(ruta):

    # Verifica si el archivo no existe en la ruta indicada.
    if not os.path.exists(ruta):

        # Si el archivo no existe, devuelve una lista vacía para evitar errores.
        return []

    # Abre el archivo JSON en modo lectura usando codificación UTF-8.
    with open(ruta, "r", encoding="utf-8") as archivo:

        # Intenta convertir el contenido del archivo JSON a una estructura de Python.
        try:
            return json.load(archivo)

        # Captura el error si el archivo está vacío o tiene formato JSON inválido.
        except json.JSONDecodeError:

            # Devuelve una lista vacía si no se pudo leer correctamente el JSON.
            return []


# Guarda información dentro de un archivo JSON.
def guardar_json(ruta, datos):

    # Abre el archivo JSON en modo escritura usando codificación UTF-8.
    with open(ruta, "w", encoding="utf-8") as archivo:

        # Convierte los datos de Python a JSON y los guarda con formato ordenado.
        json.dump(datos, archivo, indent=4, ensure_ascii=False)