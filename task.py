class Task:
    """
    Represents a task with a name, priority level, and status.
    """
    def __init__(self, name, priority):
        """
        Creates a new task with a name, priority, and status set to 'Pending'.
        """
        self.name = name
        self.priority = priority
        self.status = 'Pending'

    def mark_complete(self):
        """
        Marks the task as complete.
        """
        self.status = 'Completed'

    def __str__(self):
        """
        Returns a string representing the task.
        """
        return f"Task: {self.name} | Priority: {self.priority} | Status: {self.status}"