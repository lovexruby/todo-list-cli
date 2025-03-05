import json
import os

if os.path.exists("tasks.json"):
    print("File exists!")
else:
    print("File not found.")


TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file if it exists."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []  # Return empty list if file doesn't exist

def save_tasks(new_tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(new_tasks, file, indent=4)

def append_tasks(extra_tasks):
    """Appends tasks to JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r+") as file:
            tasks = json.load(file)
            for extras in extra_tasks:
                tasks.append(extras)
            file.seek(0)
            json.dump(tasks, file, indent=4)
    else:
        with open(TASKS_FILE, "w") as file:
            json.dump(extra_tasks, file, indent=4)



# Test: Load tasks at startup

new_tasks = [
    {"task": "Buy groceries", "done": False},
    {"task": "Study Python", "done": True}
]

extra_tasks = [
    {"task": "Bewerbungen schicken", "done": True},
    {"task": "Arbeit anfengen", "done": False},
]

save_tasks(new_tasks)
tasks = load_tasks()
print("Current tasks:", tasks)

go = input()

append_tasks(extra_tasks)
tasks = load_tasks()
print("Current tasks:", tasks)