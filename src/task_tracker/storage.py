import json
import os

# Códigos de color ANSI
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Persistencia (Lectura/Escritura JSON)
# Funciones para cargar y guardar tareas en un archivo JSON


# Función para cargar tareas desde un archivo JSON
def load_tasks(file_path="tasks.json"):
    # Si el archivo no existe, retornamos una lista vacía
    if not os.path.exists(file_path):
        # Si el archivo existe, intentamos cargar las tareas desde él
        return []

    # Abrimos el archivo en modo lectura yF cargamos las tareas usando json.load
    try:
        # Abrimos el archivo en modo lectura
        with open(file_path, "r") as file:
            # Cargamos las tareas desde el archivo y las retornamos como una lista de diccionarios
            return json.load(file)

    # Si ocurre un error al cargar, lo mostramos y salimos con un código de error
    except Exception as e:
        # Mostramos el error en rojo y negrita
        print(f"{RED}✗{RESET} {BOLD}Error loading tasks: {e}{RESET}")
        # Salimos con un código de error para indicar que algo salió mal
        exit(1)


# Función para guardar tareas en un archivo JSON
def save_tasks(tasks, file_path="tasks.json"):
    # Guardamos la lista de tareas en formato JSON en el archivo especificado
    try:
        # Abrimos el archivo en modo escritura
        with open(file_path, "w") as file:
            # Escribimos la lista de tareas en el archivo como JSON
            json.dump(tasks, file)

    # Si ocurre un error al guardar, lo mostramos y salimos con un código de error
    except Exception as e:
        # Mostramos el error en rojo y negrita
        print(f"{RED}✗{RESET} {BOLD}Error saving tasks: {e}{RESET}")
        # Salimos con un código de error para indicar que algo salió mal
        exit(1)
