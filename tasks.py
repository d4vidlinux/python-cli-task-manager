#!/usr/bin/env python3

# Python CLI Task Manager

from task_functions import add_task, done_task, remove_task, show_tasks
from task_functions import mark_as_priority, save_tasks_to_json_file, open_json_file, tasks

print("="*6," Tasks in CLI ","="*6)

# Loop
def main():
    
    while True:
        show_options = """
        1 - Add task
        2 - Remove task
        3 - Mark task as done
        4 - View tasks
        5 - Open file (default: tasks.json)
        6 - Save tasks (default: tasks.json)
        7 - Mark task as priority [!]
        0 - Exit
        """

        # Menu
        print(show_options)
        try:
            ask = int(input("What you want? \n> "))
        except ValueError:
            print("Error: Use a valid option!")
            continue

        match ask:
            # Add task
            case 1:
                category = input("Enter the category [Press enter to no select one]\n> ")
                task = input("Task to add [Press enter to cancel]\n> ")
                if not task:
                    print("Canceled")
                    continue

                add_task(task, category)


            # Remove task
            case 2:
                print("\n")
                show_tasks()
                print("\n")

                category = input("Enter the category [Press enter to no select one]\n> ")
                task = input("Task to remove [Press enter to cancel]\n> ")
                if not task:
                    print("Canceled")
                    continue

                remove_task(task, category)


            # Done task
            case 3:
                print("\n")
                show_tasks()
                print("\n")

                category = input("Enter the category [Press enter to no select one]\n> ")
                task = input("Task to mark as done [Press enter to cancel]\n> ")
                if not task:
                    print("Canceled")
                    continue

                done_task(task, category)


            # View tasks
            case 4:
                show_tasks()

                
            # Open File
            case 5:
                open_json_file()

            # Save 
            case 6:
                if not tasks:
                    print("No tasks to save.")
                    continue
                show_tasks()
                
                sure = input("Sure? [y/n]")
                if sure.lower() == "y" or sure.lower() == "yes":
                    save_tasks_to_json_file()
                    print("+Saved!")


            # Mark as priority
            case 7:
                task = input("Enter the task [Press enter to cancel]\n> ")
                if not task:
                    print("Canceled")
                    continue

                category = input("Enter the category [Press enter if none]\n> ")

                mark_as_priority(task, category)


                
            # Exit
            case 0:
                print("Leaving...")
                break
            
            case _:
                print("Invalid option!")    

            
                

if __name__ == "__main__":
    main()
     
