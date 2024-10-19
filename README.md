# To-Do List Application (CLI)

This is a simple command-line interface (CLI) To-Do List application written in Python. It allows users to add, view, complete, delete, and save tasks persistently to a JSON file.

## Table of Contents

1. Step-by-Step Guide
2. Functions Explained
3. Making the File Executable
4. How to Run the Program

## Step-by-Step Guide

1. Clone or Download the Project
   First, you need to have Python installed on your system. If you don’t have it installed, you can download it from here.

Once Python is installed, follow these steps:

- Clone the repository (or download the code) to your local machine:

```bash

git clone https://github.com/your-username/python-todo-app.git

```

2. Set Up the Project

- Ensure you're in the project folder:

```bash
cd todo_list_project
```

- If the tasks.json file exists and is empty, either delete the file or open it and add [] (an empty list). The program will handle missing or non-empty files correctly, **_but it cannot handle an empty file without valid JSON._**

3. Run the Program
   To run the program, execute the Python script:

```bash
python todo.py
```

Now, the program will be running, and you can start using the following commands:

- add: Add a new task.
- view: View all tasks.
- complete: Mark a task as completed.
- delete: Delete a task.
- exit: Save tasks and exit the program.

## Functions Explained

Here is an explanation of what each function in the code does:

1. load_tasks()
   - Purpose: Loads tasks from the tasks.json file. If the file doesn’t exist or contains invalid JSON, it returns an empty list.
   - Details: It uses the json.load() method to convert the JSON data from the file into a Python list.
2. save_tasks(tasks)
   - Purpose: Saves the current tasks to the tasks.json file. It overwrites the file with the new list of tasks in JSON format.
   - Details: It uses the json.dump() method to write the Python list back to a JSON file.
3. add_tasks(tasks)
   - Purpose: Adds a new task to the task list.
   - Details: It prompts the user for a task title, appends it to the list, and marks it as incomplete by default (completed: False).
4. view_tasks(tasks)
   - Purpose: Displays all tasks with their current status (completed or not).
   - Details: It loops over the task list and prints each task along with a status indicator (✔ for completed, ❌ for incomplete).
5. complete_task(tasks)
   - Purpose: Marks a task as completed.
   - Details: It shows the list of tasks, prompts the user for the task number, and marks it as completed (completed: True).
6. delete_task(tasks)
   - Purpose: Deletes a task from the task list.
   - Details: It displays the task list, prompts the user for the task number, and removes the corresponding task from the list.
7. main()
   - Purpose: The main loop that drives the program.
   - Details: It repeatedly prompts the user for commands (add, view, complete, delete, exit) and calls the corresponding functions based on the input.

## How to Run the Program

Running the Program on Any System:
Once you're in the project folder, you can run the program in one of two ways:
Using Python directly:

On Windows:

```bash
python todo.py
```

On macOS/Linux:

```bash

python3 todo.py
```

### Example Usage

```bash
Commands: add, view, complete, delete, exit
Enter a command: add
Enter the task title: Buy groceries
Task "Buy groceries" added!

Commands: add, view, complete, delete, exit
Enter a command: view

1. Buy groceries [❌]

Commands: add, view, complete, delete, exit
Enter a command: complete
Enter the task number to mark completed: 1
Task 1 marked as completed.

Commands: add, view, complete, delete, exit
Enter a command: exit
Tasks saved. Goodbye!

```

> Thank you for checking out this project! Your interest and contributions are highly appreciated. If you have any questions or feedback, don't hesitate to reach out or open an issue on GitHub. Happy coding!
