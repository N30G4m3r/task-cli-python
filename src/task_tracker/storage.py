import json
import os

# Códigos de color ANSI
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Persistencia (Lectura/Escritura JSON)
def load_tasks(file_path="tasks.json"):
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"{RED}✗{RESET} {BOLD}Error loading tasks: {e}{RESET}")
        exit(1)

def save_tasks(tasks, file_path):
    try:
        with open(file_path, "w") as file:
            json.dump(tasks, file)
    except Exception as e:
        print(f"{RED}✗{RESET} {BOLD}Error saving tasks: {e}{RESET}")
        exit(1)