import os
import json
from datetime import datetime

# File to store tasks
TASKS_FILE = "tasks.json"

# Function to load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    else:
        return []

# Function to save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Function to add a task
def add_task(tasks):
    task_number = input("Enter task number: ")
    task_name = input("Enter task name: ")
    priority = input("Enter priority (high, medium, low): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    tasks.append({
        "number": task_number,
        "name": task_name,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    })
    print("Task added successfully!")

# Function to remove a task
def remove_task(tasks):
    task_index = int(input("Enter task number to remove: ")) - 1
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        print("Task removed successfully!")
    else:
        print("Invalid task number!")

# Function to mark a task as completed
def complete_task(tasks):
    task_index = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number!")

# Function to display tasks
def display_tasks(tasks):
    print("\nTasks:")
    for i, task in enumerate(tasks, 1):
        status = " [X]" if task["completed"] else " [ ]"
        print(f"{i}. {task['name']} - Priority: {task['priority']} - Due Date: {task['due_date']}{status}")

# Main function
def main():
    tasks = load_tasks()
    while True:
        print("\n=== To-Do List Application ===")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            display_tasks(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
import os
import json
from datetime import datetime

# File to store tasks
TASKS_FILE = "tasks.json"

# Function to load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    else:
        return []

# Function to save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Function to add a task
def add_task(tasks):
    task_name = input("Enter task name: ")
    priority = input("Enter priority (high, medium, low): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    tasks.append({
        "name": task_name,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    })
    print("Task added successfully!")

# Function to remove a task
def remove_task(tasks):
    task_index = int(input("Enter task number to remove: ")) - 1
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        print("Task removed successfully!")
    else:
        print("Invalid task number!")

# Function to mark a task as completed
def complete_task(tasks):
    task_index = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number!")

# Function to display tasks
def display_tasks(tasks):
    print("\nTasks:")
    for i, task in enumerate(tasks, 1):
        status = " [X]" if task["completed"] else " [ ]"
        print(f"{i}. {task['name']} - Priority: {task['priority']} - Due Date: {task['due_date']}{status}")

# Main function
def main():
    tasks = load_tasks()
    while True:
        print("\n=== To-Do List Application ===")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            display_tasks(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
