import unittest
from todo import Task, TaskPool

class TestTaskPool(unittest.TestCase):
    def setUp(self):
        self.pool = TaskPool()
        self.pool.populate()

    def test_add_task(self):
        task = Task("New Task")
        self.pool.add_task(task)
        self.assertIn(task, self.pool.tasks)

    def test_get_open_tasks(self):
        opens = self.pool.get_open_tasks()
        self.assertTrue(all(t.status == "ToDo" for t in opens))

    def test_get_done_tasks(self):
        dones = self.pool.get_done_tasks()
        self.assertTrue(all(t.status == "Done" for t in dones))

if __name__ == "__main__":
    unittest.main()
