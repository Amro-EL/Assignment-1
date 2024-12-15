class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_as_complete(self):
        self.completed = True

    def __str__(self):
        status = '[x]' if self.completed else '[ ]'
        return f'{status} {self.description}'

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def mark_task_as_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_complete()
        else:
            print('Invalid task index')

    def view_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f'{i}. {task}')

def main():
    task_manager = TaskManager()

    while True:
        print('\nTask Manager')
        print('1. Add new task')
        print('2. Mark task as complete')
        print('3. View task list')
        print('4. Quit')

        choice = input('Enter your choice: ')

        if choice == '1':
            description = input('Enter task description: ')
            task_manager.add_task(description)
        elif choice == '2':
            index = int(input('Enter task index: '))
            task_manager.mark_task_as_complete(index)
        elif choice == '3':
            task_manager.view_tasks()
        elif choice == '4':
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()