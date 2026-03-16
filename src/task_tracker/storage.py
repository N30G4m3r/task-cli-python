import json
import os

# Persistencia (Lectura/Escritura JSON)
def load_tasks(file_path="tasks.json"):
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as file:
        return json.load(file)

def save_tasks(tasks, file_path):
    with open(file_path, "w") as file:
        json.dump(tasks, file)