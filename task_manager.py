import json
import os
import tkinter as tk

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

def menu():
    while True:
        tasks = load_tasks()
        choice = input("This is the Homepage. \nWhat would you like to do now?\n Enter:\n\t1 to add a task to the to do list.\n\t2 to delete a task from the to do list.\n\t3 to show the tasks. \n\t4 to delete done tasks.\n\t5 to show undone tasks. \n\t6 to exit.\n")

        if choice == "1":
            task = input("Enter the name of the task to add: ")
            while True:
                done_input = input("Is this task done? (yes/no): ").lower()
                if done_input == "yes":
                    done = True
                    break
                elif done_input == "no":
                    done = False
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
            new_task = {"task": task, "done": done}
            tasks.append(new_task)
            save_tasks(tasks)
            print("Task added successfully.")

        elif choice == "2":
            task_to_delete = input("Enter the task to delete: ")
            tasks = [task for task in tasks if task["task"] != task_to_delete]
            save_tasks(tasks)
            print("Task deleted successfully")
        elif choice == "3":
            tasks = load_tasks()
            print("Current tasks:", tasks)
            break
        elif choice == "4":
            done_tasks = [task for task in tasks if task["done"] == False]
            save_tasks(done_tasks)
            tasks = load_tasks()
            print("Current tasks:", tasks)
        elif choice =="5":
            undone_tasks = [task for task in tasks if task["done"] == False]
            print("Undone tasks:", undone_tasks)

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")

new_tasks = [
    {"task": "Buy groceries", "done": False},
    {"task": "Study Python", "done": True}
]

extra_tasks = [
    {"task": "Bewerbungen schicken", "done": True},
    {"task": "Arbeit anfengen", "done": False},
]



menu()
"""
save_tasks(new_tasks)
tasks = load_tasks()
print("Current tasks:", tasks)

go = input()

append_tasks(extra_tasks)
tasks = load_tasks()
print("Current tasks:", tasks)
"""