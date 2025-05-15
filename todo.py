class Task:
    def __init__(self, title, status="ToDo"):
        self.title = title
        self.completed = False
        self.status = status

    def mark_completed(self):
        self.completed = True
        self.status = "Done"

    def __str__(self):
        return f"Task: {self.title}, Status: {self.status}"

class TaskPool:
    def __init__(self):
        self.tasks = []

    def populate(self):
        for i in range(6):
            task = Task(f"Task {i+1}")
            if i < 3:
                task.mark_completed()
            self.tasks.append(task)

    def add_task(self, task):
        self.tasks.append(task)

    def get_open_tasks(self):
        return [t for t in self.tasks if t.status == "ToDo"]

    def get_done_tasks(self):
        return [t for t in self.tasks if t.status == "Done"]

if __name__ == "__main__":
    pool = TaskPool()
    pool.populate()
    print("ToDo Tasks:")
    for task in pool.get_open_tasks():
        print(task)
    print("Done Tasks:")
    for task in pool.get_done_tasks():
        print(task)
