from task import Task

class TaskManager:
    """
    Manages a list of tasks.
    """
    def __init__(self):
        """
        Initializes the task manager with an empty task list.
        """
        self.tasks = []

    def add_task(self, name, priority):
        """
        Adds a new task to the task list.
        """
        new_task = Task(name, priority)
        self.tasks.append(new_task)

    def mark_task_complete(self, task_index):
        """
        Marks a task as complete based on its index in the task list.
        """
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_complete()

    def get_tasks(self):
        """
        Returns the list of tasks.
        :return: A list of task objects.
        """
        return self.tasks

def display_tasks(tasks):
    """
    Displays the list of tasks with their details.
    """
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")

def main():
    """
    Main function to run the task management system.
    """
    task_manager = TaskManager()
    print("Welcome to your Task Management System!")
    print("You can add your tasks, mark them as complete and view your task list.")

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Tasks")
        print("4. Exit Program")
        
        choice = input("Select an option (1-4): ")

        if choice == '1':
            name = input("Enter the task name: ")
            priority = input("Enter the priority (High, Medium, Low): ")
            task_manager.add_task(name, priority)
            print("Task added successfully.")
        
        elif choice == '2':
            display_tasks(task_manager.get_tasks())
            try:
                task_index = int(input("Enter the task number to mark as complete: ")) - 1
                task_manager.mark_task_complete(task_index)
                print("Task marked as complete.")
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == '3':
            display_tasks(task_manager.get_tasks())
        
        elif choice == '4':
            print("Signing out of program. Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()