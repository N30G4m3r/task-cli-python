import unittest
import os
import json
from src.task_tracker.storage import save_tasks, load_tasks
from src.task_tracker.constants import ID, DESCRIPTION

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_storage.json"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_load_non_existent_file(self):
        """Si el archivo no existe, debe retornar una lista vacía."""
        tasks = load_tasks(self.test_file)
        self.assertEqual(tasks, [])

    def test_save_and_load_valid_data(self):
        """Prueba el flujo normal de guardado y lectura."""
        data = [{ID: 1, DESCRIPTION: "Test"}]
        save_tasks(data, self.test_file)
        
        loaded_data = load_tasks(self.test_file)
        self.assertEqual(len(loaded_data), 1)
        self.assertEqual(loaded_data[0][DESCRIPTION], "Test")

    def test_load_corrupt_json(self):
        """Si el archivo tiene basura, debe retornar [] y no romperse."""
        with open(self.test_file, 'w') as f:
            f.write("esto no es un json { {{")
        
        tasks = load_tasks(self.test_file)
        self.assertEqual(tasks, [])

    def test_load_empty_file(self):
        """Si el archivo existe pero está vacío, debe retornar []."""
        with open(self.test_file, 'w') as f:
            f.write("")
            
        tasks = load_tasks(self.test_file)
        self.assertEqual(tasks, [])