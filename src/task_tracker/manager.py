import datetime
from .storage import load_tasks, save_tasks
from .models import Task

# Lógica de negocio (CRUD de tareas)
class TaskManager:
    def __init__(self, file_path="tasks.json"):
        self.file_path = file_path
        self.tasks = load_tasks(file_path)

    def add_task(self, description):
        new_id = len(self.tasks) + 1
        task = Task(new_id, description)
        self.tasks.append(task.to_dict())
        save_tasks(self.tasks, self.file_path)
        # Retornamos el ID para confirmación
        return task.id

    def list_tasks(self, status=None):
        if not self.tasks:
            return []
        if status:
            return [task for task in self.tasks if task["status"] == status]
        return self.tasks

    def update_task(self, task_id, description=None, status=None):
        for task in self.tasks:
            if task["id"] == task_id:
                if description:
                    task["description"] = description
                if status:
                    task["status"] = status
                task["updated_at"] = datetime.datetime.now().isoformat()
                save_tasks(self.tasks, self.file_path)
                return True
        return False

    def delete_task(self, task_id):
        original_length = len(self.tasks)
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        if len(self.tasks) < original_length:
            save_tasks(self.tasks, self.file_path)
            return True
        return False