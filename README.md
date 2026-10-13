# Python CLI Task Manager

A simple **Task Manager** built with Python that runs directly in the terminal. It allows users to organize tasks, manage categories, track completion status, mark priorities, and store tasks in a JSON file.

## Features

- Add tasks with or without categories
- Remove tasks
- Mark tasks as completed
- View tasks organized by category
- Mark tasks as priority using 🥇
- Save tasks to a JSON file
- Load tasks from a JSON file
- Prevent duplicate tasks within the same category
- Validate task and category existence before modifying them
- Automatically remove empty categories after deleting their last task
- Cancel operations by pressing `Enter` where supported
- Interactive terminal menu
- Task status indicators:
  - ❌ Not completed
  - ✅ Completed
  - 🥇 Priority task

## Requirements

- Python 3.10 or newer

The project uses `match/case`, which requires Python 3.10 or newer.

No external dependencies are required.

## Project Structure

```text
.
├── tasks.py
├── task_functions.py
└── tasks.json
```

- `tasks.py`: Handles the interactive CLI menu and user input.
- `task_functions.py`: Contains the functions for creating, removing, completing, displaying, and prioritizing tasks, as well as loading and saving data.
- `tasks.json`: Stores tasks persistently. The file is created when tasks are saved.

## Usage

Run the application:

```bash
python3 tasks.py
```

The menu provides the following options:

```text
1 - Add task
2 - Remove task
3 - Mark task as done
4 - View tasks
5 - Open file (default: tasks.json)
6 - Save tasks (default: tasks.json)
7 - Mark task as priority [!]
0 - Exit
```

## Adding Tasks

Select option `1` and enter a task name. You can optionally assign it to a category.

Example:

```text
Enter the category
> Programming

Task to add
> Study Python
```

The task is stored under the `Programming` category with the default status `❌`.

You can also create tasks without a category by pressing `Enter` at the category prompt.

## Task Categories

Tasks can be organized into categories to make them easier to manage.

Example:

```text
Programming:
  Study Python - ❌
  Practice C - ✅

Linux:
  Learn systemd - ❌
```

Tasks without categories are stored separately from categorized tasks.

## Marking Tasks as Completed

Select option `3`, enter the category if applicable, and provide the exact task name.

The task status changes from `❌` to `✅`.

Example:

```text
Study Python - ❌
```

After completion:

```text
Study Python - ✅
```

## Removing Tasks

Select option `2`, enter the category if applicable, and specify the task to remove.

The program checks whether the specified task exists before removing it. If a category becomes empty after its last task is removed, the category is also deleted.

## Task Priorities

Select option `7` to mark a task as a priority.

Priority tasks receive the `🥇` indicator.

Example:

```text
Study Python - ❌ 🥇
```

The program avoids adding the priority indicator repeatedly to the same task.

## Viewing Tasks

Select option `4` to display the tasks currently stored in memory.

Categorized tasks are displayed under their respective categories, while uncategorized tasks are displayed separately.

If there are no tasks, the program displays a message indicating that the task list is empty.

## Case Sensitivity

**Task names and category names are case-sensitive.**

For example:

```text
Study Python
study python
STUDY PYTHON
```

These names are treated as different strings.

When completing, removing, or prioritizing a task, enter its name and category using the same capitalization used when creating them.

## Saving Tasks

Select option `6` to save the current tasks to:

```text
tasks.json
```

The program asks for confirmation before saving. Confirm with `y` or `yes`.

The data is stored in JSON format, preserving task names, categories, and statuses.

Example:

```json
{
    "Programming": {
        "Study Python": "❌ 🥇",
        "Practice C": "✅"
    },
    "Learn Linux": "❌"
}
```

The JSON format makes the stored data easier to process with other Python programs and tools.

## Loading Tasks

Select option `5` to load tasks from `tasks.json`.

Loading a file replaces the tasks currently stored in memory with the data loaded from the file.

The program handles missing files and invalid JSON by displaying an error message instead of terminating because of those errors.

## Concepts Used

This project applies several Python concepts:

- Functions and modular code organization
- Dictionaries and nested dictionaries
- Loops and conditional statements
- `match/case`
- Function parameters and default arguments
- File handling with `open()`
- JSON serialization and deserialization
- Exception handling with `try/except`
- String formatting with f-strings
- User input and interactive CLI design
- Dictionary methods such as `.items()` and `.pop()`
- Data validation
- Basic state management
- Separation of CLI logic from task management functions

## Possible Improvements

Potential features for future versions:

- Add task descriptions
- Add due dates and reminders
- Introduce unique task IDs
- Allow users to edit existing tasks
- Add task search and filtering
- Support custom file paths
- Add command-line arguments using `argparse`
- Improve terminal output with colors
- Validate the structure of loaded JSON data more thoroughly
- Separate task data management from persistence logic
- Add configuration files and logging

## License

This project is intended for learning and experimentation with Python.

## Author 
d4vidlinux
