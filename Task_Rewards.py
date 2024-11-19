# task_rewards.py
# Commit message: Added initial structure for task_rewards and task_manager modules.

class Task:
    def __init__(self, name, difficulty):
        #Initialize a task with a name and difficulty.
        self.name = name
        self.difficulty = difficulty
        self.completed = False

    def complete_task(self):
        # Marks the task as completed and calculates the reward points.
        self.completed = True
        return self.calculate_points()

    def calculate_points(self):
        # Determines the number of points to reward based on task difficulty.
        difficulty_points = {"easy": 5, "medium": 10, "hard": 20}
        return difficulty_points.get(self.difficulty, 0)
