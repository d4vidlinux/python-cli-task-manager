# Python CLI Task Manager

A simple **Task Manager** made in Python that runs directly in the terminal.

The project allows you to create, remove, complete, view, save, and load tasks using a simple CLI menu.

## Features

- Add tasks
- Remove tasks
- Mark tasks as completed
- View all tasks
- Save tasks to a file
- Load tasks from a file
- Cancel operations by pressing `Enter`
- Simple interactive CLI
- Task status using emojis:
  - ❌ Not completed
  - ✅ Completed

## Requirements

- Python 3.10+

The project uses `match/case`, so Python 3.10 or newer is required.

## Usage

Run the program:

```bash
python3 task_manager.py
```

You will see a menu similar to:

```text
====== Tasks in CLI ======

1 - Add task
2 - Remove task
3 - Mark task as done
4 - View tasks
5 - Open file (default: tasks.txt)
6 - Save tasks (default: tasks.txt)
0 - Exit
```

### Adding a task

Select option `1` and enter the task:

```text
Task to add
> Study Python
```

The task will be added with the default status:

```text
Study Python ❌
```

### Marking a task as done

Select option `3` and enter the exact task name:

```text
Task to mark as done
> Study Python
```

The status will change to:

```text
Study Python ✅
```

### Removing a task

Select option `2` and enter the task you want to remove.

### Viewing tasks

Option `4` displays all currently loaded tasks:

```text
Study Python ❌
Learn Linux ✅
Practice C ❌
```

## Case Sensitivity

**Tasks are case-sensitive.**

This means that uppercase and lowercase letters are treated as different characters.

For example:

```text
Study Python
study python
STUDY PYTHON
```

These are considered **three different tasks**.

Because of this, when removing or completing a task, you must enter its name using the same capitalization used when it was created.

## Saving Tasks

Option `6` saves the current tasks to:

```text
tasks.txt
```

Before saving, the program asks for confirmation:

```text
Make sure your decision [y/n]
```

Enter `y` to save.

The file stores the task name and its status.

Example:

```text
Study Python ❌
Learn Linux ✅
Practice C ❌
```

## Loading Tasks

Option `5` loads tasks from:

```text
tasks.txt
```

Loading the file replaces the tasks currently stored in memory.

If the file does not exist, the program displays:

```text
File not found...
```

## Project Structure

```text
.
├── task_manager.py
└── tasks.txt
```

`tasks.txt` is created when tasks are saved.

## Concepts Used

This project was built using several Python concepts:

- Functions
- Dictionaries
- Loops
- `match/case`
- `*args` / function parameters
- File handling
- Exception handling
- String formatting
- User input
- Dictionary methods such as `.items()`, `.pop()` and `.clear()`

## Possible Improvements

Some ideas for future versions:

- Add task priorities
- Add task categories
- Add task descriptions
- Add due dates
- Add task IDs
- Improve file format using JSON
- Add command-line arguments with `argparse`
- Add colored terminal output
- Add a search function
- Separate the CLI logic from the task management logic

## License

This project is for learning and experimentation with Python.
