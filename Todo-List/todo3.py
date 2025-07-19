# Task class to manage a to-do list
class Task:
    def __init__(self):
        self.task_list = []

    def add(self, name):
        print(f"task {name} added.")
        self.task_list.append(name)

    def remove(self, name):
        if name not in self.task_list:
            print("task not found.")
        else:
            print(f"task {name} removed.")
            self.task_list.remove(name)

    def show(self):
        if not self.task_list:
            print("task list is empty")
        else:
            print("\nall tasks:")
            for task in self.task_list:
                print(" -", task)

    def save(self):
        print("tasks saved on Desktop.")
        with open("/home/amyr/Desktop/tasks.txt", "w") as f:
            for task in self.task_list:
                f.write(task + "\n")  # Write each task on a new line

    def load(self, path):
        try:
            count = 0
            with open(path, "r") as f:
                self.task_list.clear()  # Clear existing tasks
                for line in f:
                    self.task_list.append(line.strip())
                    count += 1
            print(f"\n{count} tasks loaded.")
        except FileNotFoundError:
            print("\nFile not found!")


# Main loop for command input
task = Task()
while True:
    command = input("\nadd-remove-show-save-load-quit\nWhat to do? ").lower().strip()

    if command == "add":
        t = input("task: ")
        task.add(t)

    elif command == "remove":
        t = input("task: ")
        task.remove(t)

    elif command == "show":
        task.show()

    elif command == "save":
        task.save()

    elif command == "load":
        path = input("path: ")
        task.load(path)

    elif command == "quit":
        exit()

    else:
        print("\nenter valid command!")
