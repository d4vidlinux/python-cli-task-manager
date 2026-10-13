import json

tasks = {}


def add_task(task, category, done="❌"):
    if not category:
        if task in tasks:
            print(f"The task '{task}' already exists!")
            return

        tasks[task] = done
        print("No category was entered")
        return

    if category in tasks and not isinstance(tasks[category], dict):
        print(f"'{category}' already exists as a task!")
        return

    if category not in tasks:
        tasks[category] = {}

    if task in tasks[category]:
        print(f"The task '{task}' in '{category}' already exists!")
        return

    tasks[category][task] = done
    print(f"Task '{task}' added!")


def done_task(task, category):
    if not category:
        if task not in tasks or isinstance(tasks[task], dict):
            print("Please, enter an existing task")
            return

        tasks[task] = "✅"
        print(f"Task '{task}' done")
        return

    if category not in tasks:
        print(f"Error: Category '{category}' does not exist")
        return

    if not isinstance(tasks[category], dict) or task not in tasks[category]:
        print("Please, enter an existing task")
        return

    tasks[category][task] = "✅"
    print(f"Task '{task}' done")


def remove_task(task, category):
    if not category:
        if task not in tasks or isinstance(tasks[task], dict):
            print("Please, enter an existing task")
            return

        tasks.pop(task)
        print(f"Task '{task}' removed")
        return

    if category not in tasks:
        print(f"Error: Category '{category}' does not exist")
        return

    if not isinstance(tasks[category], dict) or task not in tasks[category]:
        print("Please, enter an existing task")
        return

    tasks[category].pop(task)
    print(f"Task '{task}' removed")

    if not tasks[category]:
        tasks.pop(category)


def show_tasks():
    if not tasks:
        print("No tasks yet.")
        return

    for item, value in tasks.items():
        if isinstance(value, dict):
            print(f"\n{item}:")
            for task, status in value.items():
                print(f"  {task} - {status}")
        else:
            print(f"{item} - {value}")


def save_tasks_to_json_file(file="tasks.json"):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)

    print(f"Tasks saved to '{file}'!")


def open_json_file(file="tasks.json"):
    global tasks

    try:
        with open(file, "r", encoding="utf-8") as f:
            loaded_tasks = json.load(f)

        if not isinstance(loaded_tasks, dict):
            print("Error: Invalid tasks file format")
            return

        tasks = loaded_tasks
        print(f"File '{file}' opened!")

    except FileNotFoundError:
        print(f"Error: File '{file}' not found")
    except json.JSONDecodeError:
        print(f"Error: File '{file}' contains invalid JSON")


def mark_as_priority(task, category):
    if not category:
        if task not in tasks or isinstance(tasks[task], dict):
            print("Please, enter an existing task")
            return

        if "🥇" not in tasks[task]:
            tasks[task] += " 🥇"

        print(f"Task '{task}' marked as priority")
        return

    if category not in tasks:
        print(f"Error: Category '{category}' does not exist")
        return

    if not isinstance(tasks[category], dict) or task not in tasks[category]:
        print("Please, enter an existing task")
        return

    if "🥇" not in tasks[category][task]:
        tasks[category][task] += " 🥇"

    print(f"Task '{task}' marked as priority")
