import json
import sys
import os

TODO_FILE = 'todos.json'

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
        return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=2)


def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {task}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("NO tasks here")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def remove_task(i):
    tasks = load_tasks()

    if 0 < i <= len(tasks):
        removed = tasks.pop(i - save_tasks(tasks))
        print(f"Removed task: {removed}")
    else:
        print("Invalid task number.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python todo.py [add/list/remove] [task/number]")
        return

    command = sys.argv[1]

    if command == "add" and len(sys.argv) > 2:
        add_task("".join(sys.argv[2:]))
    elif command == "list":
        list_tasks()
    elif command == "remove" and len(sys.argv) > 2:
        try:
            remove_task(int(sys.argv[2]))
        except ValueError:
            print("Is that a real number?")
    else:
        print("Invalid command, pick one of these three")

if __name == "__main__":
    main()