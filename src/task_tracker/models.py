import datetime


# Definición de la estructura de la Tarea
class Task:
    # Constructor para inicializar una tarea con ID, descripción, estado y timestamps
    def __init__(self, id, description, status="todo"):
        self.id = id  # ID único de la tarea
        self.description = description  # Descripción de la tarea
        self.status = status  # todo, in-progress, done
        self.created_at = datetime.datetime.now().isoformat()  # Timestamp de creación
        self.updated_at = (
            self.created_at
        )  # Timestamp de última actualización (inicialmente igual a created_at)

    # Método para convertir la tarea a un diccionario (útil para JSON)
    def to_dict(self):
        return self.__dict__
