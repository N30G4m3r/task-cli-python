import json
import os
from .constants import RED, BOLD, RESET, DB_FILE, READING, WRITING

# Persistencia (Lectura/Escritura JSON)
# Funciones para cargar y guardar tareas en un archivo JSON


# Función para cargar tareas desde un archivo JSON
def load_tasks(file_path=DB_FILE):
    # Si el archivo no existe, retornamos una lista vacía
    if not os.path.exists(file_path):
        # Si el archivo existe, intentamos cargar las tareas desde él
        return []

    # Abrimos el archivo en modo lectura yF cargamos las tareas usando json.load
    try:
        # Abrimos el archivo en modo lectura
        with open(file_path, READING) as file:
            # Cargamos las tareas desde el archivo y las retornamos como una lista de diccionarios
            return json.load(file)

    # Si ocurre un error al cargar, lo mostramos y salimos con un código de error
    except Exception as e:
        # Mostramos el error en rojo y negrita
        print(f"{RED}✗{RESET} {BOLD}Error loading tasks: {e}{RESET}")
        # Salimos con un código de error para indicar que algo salió mal
        exit(1)


# Función para guardar tareas en un archivo JSON
def save_tasks(tasks, file_path=DB_FILE):
    # Guardamos la lista de tareas en formato JSON en el archivo especificado
    try:
        # Abrimos el archivo en modo escritura
        with open(file_path, WRITING) as file:
            # Escribimos la lista de tareas en el archivo como JSON
            json.dump(tasks, file)

    # Si ocurre un error al guardar, lo mostramos y salimos con un código de error
    except Exception as e:
        # Mostramos el error en rojo y negrita
        print(f"{RED}✗{RESET} {BOLD}Error saving tasks: {e}{RESET}")
        # Salimos con un código de error para indicar que algo salió mal
        exit(1)
