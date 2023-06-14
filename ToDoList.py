import datetime

class Task:
    def __init__(self, description, deadline=None, completed=False):
        self.description = description
        self.deadline = deadline
        self.completed = completed

    def mark_as_completed(self):
        self.completed = True

    def mark_as_incomplete(self):
        self.completed = False

    def set_deadline(self, deadline):
        self.deadline = deadline

    def is_completed(self):
        return self.completed

    def is_deadline_approaching(self):
        if self.deadline is None:
            return False
        now = datetime.datetime.now()
        return now < self.deadline <= now + datetime.timedelta(hours=1)

    def __str__(self):
        status = "[Completed]" if self.completed else "[Not Completed]"
        if self.is_deadline_approaching() and not self.completed:
            return f"!!! {status} {self.description} - Deadline Approaching !!!"
        elif self.deadline is not None and not self.completed:
            return f"{status} {self.description} - Deadline: {self.deadline}"
        else:
            return f"{status} {self.description}"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def modify_task(self, task, new_description):
        task.description = new_description

    def mark_task_as_completed(self, task):
        task.mark_as_completed()

    def mark_task_as_incomplete(self, task):
        task.mark_as_incomplete()

    def set_task_deadline(self, task, deadline):
        task.set_deadline(deadline)

    def get_completed_tasks(self):
        return [task for task in self.tasks if task.is_completed()]

    def get_incomplete_tasks(self):
        return [task for task in self.tasks if not task.is_completed()]

    def show_task_statuses(self):
        completed_count = len(self.get_completed_tasks())
        incomplete_count = len(self.get_incomplete_tasks())

        print("Task Statuses:")
        print(f"Completed Tasks: {completed_count}")
        print(f"Incomplete Tasks: {incomplete_count}\n")

        print("Completed Tasks:")
        for task in self.get_completed_tasks():
            print(task)

        print("\nIncomplete Tasks:")
        for task in self.get_incomplete_tasks():
            print(task)
        print()


todo_list = TodoList()

task1 = Task("Buy sometig")
task2 = Task("Do homewrok")
task3 = Task("Finish the task")
todo_list.add_task(task1)
todo_list.add_task(task2)
todo_list.add_task(task3)

task1.set_deadline(datetime.datetime(2023, 6, 20))
task3.set_deadline(datetime.datetime(2023, 6, 15, 12, 0, 0))
print(task1.is_deadline_approaching()
)
todo_list.mark_task_as_completed(task1)

todo_list.modify_task(task2, "Clean the garage")

todo_list.remove_task(task3)

todo_list.show_task_statuses()
