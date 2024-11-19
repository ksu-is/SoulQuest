task_manager.py
# Commit message: Added initial structure for task_rewards and task_manager modules.

tasks = []

def add_task(name, difficulty):
   #Adds a new task to the list of tasks
    tasks.append(Task(name, difficulty))
    print(f"Task '{name}' added!")

def list_tasks():
    #Shows all the tasks along with their status
    for idx, task in enumerate(tasks, start=1):
        status = "Completed" if task.completed else "Pending"
        print(f"{idx}. {task.name} ({task.difficulty}) - {status}")

def delete_task(index):
    #removes a task from the list
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Task '{removed.name}' deleted!")
    else:
        print("Invalid task number.")

# Example usage
add_task("Walk 10 minutes", "easy")
list_tasks()
delete_task(0)
