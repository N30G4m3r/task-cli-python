import datetime
from .storage import load_tasks, save_tasks
from .models import Task
from .constants import DB_FILE, ID, STATUS, DESCRIPTION, UPDATE_AT


# Lógica de negocio (CRUD de tareas)
class TaskManager:
    # Constructor para inicializar el TaskManager con la ruta del archivo de tareas y cargar las tareas existentes
    def __init__(self, file_path=DB_FILE):
        # Guardamos la ruta del archivo de tareas para usarla en las operaciones de carga y guardado
        self.file_path = file_path
        # Cargamos las tareas existentes en una lista
        self.tasks = load_tasks(file_path)

    # Método para agregar una nueva tarea con una descripción dada
    def add_task(self, description):
        # Validación: Si no hay descripción o son solo espacios, lanzamos un error o devolvemos None
        if not description or description.strip() == "":
            return None  # Devolvemos None para indicar que no se creó nada
        
        # Generamos un nuevo ID para la tarea basado en la cantidad de tareas existentes (simple pero efectivo para este caso)
        new_id = max([t[ID] for t in self.tasks], default=0) + 1

        # Creamos una nueva instancia de Task con el nuevo ID y la descripción proporcionada
        task = Task(new_id, description)

        # Agregamos la tarea a la lista de tareas
        self.tasks.append(task.to_dict())

        # Guardamos la lista actualizada de tareas en el archivo JSON para persistencia
        save_tasks(self.tasks, self.file_path)
        
        # Retornamos el ID para confirmación
        return task.id

    def list_tasks(self, status=None):
        # Si no hay tareas, retornamos una lista vacía
        if not self.tasks:
            return []

        # Si se especifica un estado, filtramos las tareas por ese estado, de lo contrario retornamos todas las tareas
        if not status:
            # Retornamos todas las tareas sin filtrar
            return self.tasks

        # Retornamos solo las tareas que coinciden con el estado especificado
        return [task for task in self.tasks if task[STATUS] == status]

    # Método para actualizar una tarea existente dado su ID, con una nueva descripción y/o un nuevo estado
    def update_task(self, task_id, description=None, status=None):
        tasks_length = len(self.tasks)
        if tasks_length == 0:
            return False  # No hay tareas para actualizar
        if (not description or description.strip() == "") and (not status or status.strip() == ""):
            return False  # No se proporcionó nada para actualizar

        # Buscamos la tarea por su ID y actualizamos los campos proporcionados
        for task in self.tasks:
            # Si encontramos la tarea con el ID especificado, actualizamos su descripción y/o estado según lo proporcionado
            if task[ID] == task_id:
                # Si se proporciona una nueva descripción, la actualizamos en la tarea
                if description:
                    task[DESCRIPTION] = description
                # Si se proporciona un nuevo estado, lo actualizamos en la tarea
                if status:
                    task[STATUS] = status
                # Actualizamos el timestamp de última actualización de la tarea
                task[UPDATE_AT] = datetime.datetime.now().isoformat()
                # Guardamos la lista actualizada de tareas en el archivo JSON para persistencia
                save_tasks(self.tasks, self.file_path)
                # Retornamos True para indicar que la tarea fue actualizada exitosamente
                return True

        # Si no encontramos la tarea con el ID especificado, retornamos False para indicar que no se pudo actualizar
        return False

    def delete_task(self, task_id):
        original_length = len(self.tasks)
        if original_length == 0:
            return False  # No hay tareas para eliminar

        # Filtramos la lista de tareas para eliminar la tarea con el ID especificado
        self.tasks = [task for task in self.tasks if task[ID] != task_id]

        # Si la longitud de la lista de tareas después del filtrado es menor que la longitud original, significa que se eliminó una tarea
        if len(self.tasks) < original_length:
            # Guardamos la lista actualizada de tareas en el archivo JSON para persistencia
            save_tasks(self.tasks, self.file_path)
            # Retornamos True para indicar que la tarea fue eliminada exitosamente
            return True

        # Si no se eliminó ninguna tarea (es decir, no se encontró la tarea con el ID especificado), retornamos False
        return False
