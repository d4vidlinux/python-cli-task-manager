#!/usr/bin/env python3

# Python CLI Task Manager

print("="*6," Tasks in CLI ","="*6)

tasks = {}

def add_task(task, done="❌"):
    if task in tasks:
        print("The task '{}' already exists!".format(task))
        return

    tasks[task] = done
    print("Task '{}' added!".format(task))

def done_task(task):
    if task not in tasks:
        print("Please, enter a existing task")
        return
    
    tasks[task] = "✅"
    print("Task '{}' done".format(task))


def remove_task(task):
    if task not in tasks:
        print("Please, enter a existing task")
        return
    
    tasks.pop(task)
    print("Task '{}' removed".format(task))


def show_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    for task, status in tasks.items():
        print(task, status)


def save_tasks(file="tasks.txt"):
    with open(file, "w") as f:
        for i, t in tasks.items():
            f.write("{} {}\n".format(i, t))


def open_file(file="tasks.txt"):
    tasks.clear()
    try:
        with open(file, "r") as f:
            for line in f:
                i, t = line.strip().split(" ", 1)
                tasks[i] = t
    except FileNotFoundError:
        print("File not found...")


# Loop
def main():
    while True:
        show_options = """
        1 - Add task
        2 - Remove task
        3 - Mark task as done
        4 - View tasks
        5 - Open file (default: tasks.txt)
        6 - Save tasks (default: tasks.txt)
        0 - Exit
        """

        # Menu
        print(show_options)
        ask = int(input("What you want? \n> "))

        match ask:
        # Add task
            case 1:
                task = input("Task to add [Press enter to cancel]\n> ")
                if not task:
                    print("Canceled")
                    continue

                add_task(task)


            # Remove task
            case 2:
                show_tasks()
                task = input("Task to remove [Press enter to cancel]\n> ")
                if not task:
                    print("Canceled")
                    continue

                remove_task(task)


            # Done task
            case 3:
                show_tasks()
                task = input("Task to mark as done [Press enter to cancel]\n> ")
                if not task:
                    print("Canceled")
                    continue

                done_task(task)


            # View tasks
            case 4:
                show_tasks()

                
            # Open File
            case 5:
                open_file()
                print("File opened!")

            # Save 
            case 6:
                if not tasks:
                    print("No tasks to save.")
                    continue
                for i,t in tasks.items():
                    print(i, t)
                
                sure = input("Make sure your decision [y/n]")
                if sure.lower() == "y":
                    save_tasks()
                    print("+Saved!")

            # Exit
            case 0:
                print("Leaving...")
                break
            
            case _:
                print("Invalid option!")    

if __name__ == "__main__":
    main()
     
