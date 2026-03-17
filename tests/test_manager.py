import unittest
import os
from src.task_tracker.manager import TaskManager
from src.task_tracker.constants import ID, DESCRIPTION, STATUS, STATUS_TODO, STATUS_IN_PROGRESS, STATUS_DONE


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        """Se ejecuta antes de cada test. Prepara un entorno limpio."""
        self.test_db = "test_tasks.json"
        # Forzamos al manager (o storage) a usar el archivo de test
        # Nota: Aquí podrías necesitar ajustar tu storage para aceptar un path
        self.manager = TaskManager(self.test_db)
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def tearDown(self):
        """Se ejecuta después de cada test. Limpia los archivos temporales."""
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_add_task(self):
        """Prueba que se pueda agregar una tarea correctamente."""
        new_id = self.manager.add_task("Prueba de test")
        self.assertEqual(new_id, 1)

        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0][DESCRIPTION], "Prueba de test")

    def test_create_task_without_description(self):
        """Prueba que no se cree una tarea si la descripción es nula o vacía."""
        # Intento con None
        res_none = self.manager.add_task(None)
        self.assertIsNone(res_none)
        
        # Intento con string vacío
        res_empty = self.manager.add_task("")
        self.assertIsNone(res_empty)
        
        # Intento con solo espacios
        res_spaces = self.manager.add_task("    ")
        self.assertIsNone(res_spaces)
        
        # Verificamos que realmente no se guardó nada en el archivo
        self.assertEqual(len(self.manager.list_tasks()), 0)

    def test_delete_task(self):
        """Prueba que la eliminación funcione."""
        self.manager.add_task("Borrarme")
        success = self.manager.delete_task(1)
        self.assertTrue(success)
        self.assertEqual(len(self.manager.list_tasks()), 0)
    
    def test_delete_non_existent_task(self):
        """Prueba que elimina un ID que no existe devuelva False."""
        success = self.manager.delete_task(999)
        self.assertFalse(success)

    def test_update_task_description(self):
        """Prueba que se pueda cambiar la descripción de una tarea."""
        self.manager.add_task("Descripción vieja")
        success = self.manager.update_task(1, description="Descripción nueva")

        self.assertTrue(success)
        task = self.manager.list_tasks()[0]
        self.assertEqual(task[DESCRIPTION], "Descripción nueva")

    def test_update_task_status(self):
        """Prueba el cambio de estado de todo a in-progress."""
        self.manager.add_task("Hacer ejercicio")
        self.manager.update_task(1, status=STATUS_IN_PROGRESS)

        task = self.manager.list_tasks()[0]
        self.assertEqual(task[STATUS], STATUS_IN_PROGRESS)

    def test_update_task_with_empty_description_and_status(self):
        """Prueba que no se actualice si la descripción y el status está vacía."""
        self.manager.add_task("Tarea original")
        
        # Caso 1: String vacío
        success = self.manager.update_task(1, description="", status="")
        self.assertFalse(success)
        
        # Caso 2: Solo espacios en blanco
        success = self.manager.update_task(1, description="   ", status="  ")
        self.assertFalse(success)

    def test_update_non_existent_task(self):
        """Prueba que actualizar un ID que no existe devuelva False."""
        success = self.manager.update_task(999, "No existo")
        self.assertFalse(success)

    def test_list_filtering(self):
        """Prueba que el filtrado por estado funcione correctamente."""
        self.manager.add_task("Tarea 1") # todo
        self.manager.add_task("Tarea 2") # todo
        self.manager.add_task("Tarea 3") # todo
        self.manager.update_task(2, status=STATUS_DONE)
        self.manager.update_task(3, status=STATUS_IN_PROGRESS)
        
        all_tasks = self.manager.list_tasks()
        done_tasks = self.manager.list_tasks(STATUS_DONE)
        todo_tasks = self.manager.list_tasks(STATUS_TODO)
        in_progress_tasks = self.manager.list_tasks(STATUS_IN_PROGRESS)
        
        self.assertEqual(len(all_tasks), 3)
        self.assertEqual(len(done_tasks), 1)
        self.assertEqual(done_tasks[0][ID], 2)
        self.assertEqual(len(todo_tasks), 1)
        self.assertEqual(todo_tasks[0][ID], 1)
        self.assertEqual(len(in_progress_tasks), 1)
        self.assertEqual(in_progress_tasks[0][ID], 3)


if __name__ == "__main__":
    unittest.main()
