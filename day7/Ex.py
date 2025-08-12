class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_done(self):
        self.completed = True

    def __str__(self):
        status = "✅" if self.completed else ""
        return f"{status} {self.description}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f" Task added: {description}")

    def show_tasks(self):
        if not self.tasks:
            print(" No tasks yet.")
        else:
            print("\n Your Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def mark_task_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()
            print(f" Task marked as done: {self.tasks[index].description}")
        else:
            print(" Invalid task number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"🗑️ Task deleted: {removed.description}")
        else:
            print(" Invalid task number.")


def main():
    todo = ToDoList()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            desc = input("Enter task description: ")
            todo.add_task(desc)
        elif choice == "2":
            todo.show_tasks()
        elif choice == "3":
            todo.show_tasks()
            try:
                index = int(input("Enter task number to mark as done: ")) - 1
                todo.mark_task_done(index)
            except ValueError:
                print(" Please enter a valid number.")
        elif choice == "4":
            todo.show_tasks()
            try:
                index = int(input("Enter task number to delete: ")) - 1
                todo.delete_task(index)
            except ValueError:
                print(" Please enter a valid number.")
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print(" Invalid choice. Try again.")


if __name__ == "__main__":
    main()
