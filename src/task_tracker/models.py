import datetime

# Definición de la estructura de la Tarea
class Task:
    def __init__(self, id, description, status="todo"):
        self.id = id
        self.description = description
        self.status = status # todo, in-progress, done
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = self.created_at

    def to_dict(self):
        return self.__dict__