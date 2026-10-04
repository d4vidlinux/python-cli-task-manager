global tasks
tasks = {}


def add_task(task, done="❌"):
    if task in tasks:
        print(f"The task '{task}' already exists!")
        return

    tasks[task] = done
    print(f"Task '{task}' added!")

def done_task(task):
    if task not in tasks:
        print("Please, enter a existing task")
        return
    
    tasks[task] = "✅"
    print(f"Task '{task}' done")


def remove_task(task):
    if task not in tasks:
        print("Please, enter a existing task")
        return
    
    tasks.pop(task)
    print(f"Task '{task}' removed")


def show_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    for task, status in tasks.items():
        print(task, status)


def save_tasks(file="tasks.txt"):
    with open(file, "w") as f:
        for i, t in tasks.items():
            f.write(f"{i} {t}\n")


def open_file(file="tasks.txt"):
    tasks.clear()
    try:
        with open(file, "r") as f:
            for line in f:
                i, t = line.strip().split(" ", 1)
                tasks[i] = t
    except FileNotFoundError:
        print("File not found...")