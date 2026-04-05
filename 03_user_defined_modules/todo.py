tasks = []

def add_task(task):
    tasks.append(task)
    return "Task added!"

def show_tasks():
    
    if not tasks:
        print("No tasks available")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task(index):
    if 0 < index <= len(tasks):
        return f"Removed: {tasks.pop(index-1)}"
    else:
        return "Invalid task number"