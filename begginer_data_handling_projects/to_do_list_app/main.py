# To-Do List App (with File Storage)

class ToDoList:
    def __init__(self):
        self.file_path = r"begginer_data_handling_projects\to_do_list_app\tasks.txt"

    def add_task(self):
        task = input("Enter you task : ")
        if task:
            with open(self.file_path, 'a') as file:
                file.write(task + "\n")
            print("Task Successfully Added !!")

        else:
            print("Task can not be empty.")

    def view_tasks(self):
        with open(self.file_path, "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("No tasks found.\n")
            return

        print("\n--- Your Tasks ---")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")
        print()

    def delete_task(self):
        with open(self.file_path, "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("No tasks to delete!\n")
            return

        print("\n--- Tasks ---")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")

        try:
            num = int(input("\nEnter task number to delete: "))
            if num < 1 or num > len(tasks):
                print("Invalid task number!\n")
                return
        except ValueError:
            print("Invalid input! Please enter a number.\n")
            return

        tasks.pop(num - 1)

        with open(self.file_path, "w") as file:
            for task in tasks:
                file.write(task)

        print("Task deleted!\n")



if __name__ == "__main__":
    print("="*120)
    print("="*120)
    print("="*51, " To Do List App ", "="*51)
    print("="*120)
    print("="*120)

    while True:
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("0. Exit")

        try:
            choice = int(input("Enter a number : "))
        except Exception as message:
            print("Error : ", message)
            continue

        if choice == 0:
            print("Thank you for using To Do List App")
            break

        if choice not in [1,2,3]:
            print("Invalid choice! Please choose 1, 2, 3, or 0.")
            continue

        todo = ToDoList()
        if choice == 1:
            todo.add_task()
        elif choice == 2:
            todo.view_tasks()
        elif choice == 3:
            todo.delete_task()