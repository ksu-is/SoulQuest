class SelfCareApp:
    def __init__(self):
        self.tasks = []
        self.points = 0
        self.level = 1

    def add_task(self, task_name, points):
        """Add a new task."""
        self.tasks.append({"name": task_name, "points": points, "completed": False})

    def view_tasks(self):
        """View all tasks."""
        print("\nTasks:")
        if not self.tasks:
            print("No tasks available. Add some tasks!")
        for i, task in enumerate(self.tasks):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{i + 1}. {task['name']} ({task['points']} points) - {status}")

    def complete_task(self, task_index):
        """Mark a task as completed."""
        if 0 <= task_index < len(self.tasks) and not self.tasks[task_index]["completed"]:
            task = self.tasks[task_index]
            task["completed"] = True
            self.points += task["points"]
            print(f"\nGreat job! You completed '{task['name']}' and earned {task['points']} points.")
            self.check_level_up()
        else:
            print("\nInvalid task or task already completed.")

    def check_level_up(self):
        """Check if the user has earned enough points to level up."""
        required_points = self.level * 10
        if self.points >= required_points:
            self.level += 1
            print(f"🎉 Congratulations! You've leveled up to Level {self.level}! 🎉")

    def view_status(self):
        """View user's current status."""
        print(f"\n--- User Status ---")
        print(f"Level: {self.level}")
        print(f"Points: {self.points}")
        print("-------------------")

def main():
    app = SelfCareApp()
    while True:
        print("\n--- Self-Care App ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. View Status")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            app.view_tasks()
        elif choice == "2":
            task_name = input("\nEnter task name: ")
            try:
                points = int(input("Enter points for this task: "))
                app.add_task(task_name, points)
                print(f"\nTask '{task_name}' added with {points} points.")
            except ValueError:
                print("Invalid input. Points should be a number.")
        elif choice == "3":
            try:
                task_index = int(input("\nEnter task number to complete: ")) - 1
                app.complete_task(task_index)
            except ValueError:
                print("Invalid input. Enter a valid task number.")
        elif choice == "4":
            app.view_status()
        elif choice == "5":
            print("Goodbye! Keep up the self-care!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
