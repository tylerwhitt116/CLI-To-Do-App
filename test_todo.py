import unittest
import json
import os
from todo import add_task, list_tasks, remove_task, TODO_FILE

class TestTodoApp(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_todos.json"
        global TODO_FILE
        TODO_FILE = self.test_file

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def load_tasks(self):
        if os.path.exists(self.test_file):
            with open(self.test_file, "r") as file:
                return json.load(file)
            return []

    def test_add_task(self):
        add_task("Test Task")
        tasks = list_tasks()
        self.assertIsNotNone(tasks, "tasks should not be None")
        self.assertIn("Test Task", tasks)

    def test_remove_task(self):
        add_task("Task to Remove")
        remove_task(1)
        tasks = list_tasks()
        self.assertIsNotNone(tasks, "tasks should not be None")
        self.assertNotIn("Task to Remove", tasks)

if __name__ == "__main__":
    unittest.main()