import unittest
import os
from src.task_tracker.manager import TaskManager
from src.task_tracker.constants import DESCRIPTION, STATUS, STATUS_TODO, STATUS_IN_PROGRESS, STATUS_DONE


class TestTaskTrackerIntegration(unittest.TestCase):

    def setUp(self):
        # Usamos un archivo separado para no tocar tus datos reales
        self.test_db = "integration_tasks.json"
        # Importante: Asegúrate de que tu TaskManager acepte el path del archivo
        self.manager = TaskManager(self.test_db)

        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def tearDown(self):
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_full_workflow(self):
        """Prueba el ciclo de vida completo de una tarea."""

        # 1. Crear la tarea
        task_id = self.manager.add_task("Aprender Integration Testing")
        self.assertEqual(task_id, 1)

        # 2. Verificar que aparezca en la lista general
        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0][STATUS], STATUS_TODO)

        # 3. Cambiar descripción y estado
        self.manager.update_task(task_id, description="Dominar Integration Testing", status=STATUS_IN_PROGRESS)

        # 4. Verificar filtrado de lista
        in_progress_tasks = self.manager.list_tasks(STATUS_IN_PROGRESS)
        self.assertEqual(len(in_progress_tasks), 1)
        self.assertEqual(
            in_progress_tasks[0][DESCRIPTION], "Dominar Integration Testing"
        )

        # 5. Marcar como completada
        self.manager.update_task(task_id, status=STATUS_DONE)
        done_tasks = self.manager.list_tasks(STATUS_DONE)
        self.assertEqual(len(done_tasks), 1)

        # 6. Eliminar la tarea y verificar que el archivo esté vacío
        self.manager.delete_task(task_id)
        final_tasks = self.manager.list_tasks()
        self.assertEqual(len(final_tasks), 0)
