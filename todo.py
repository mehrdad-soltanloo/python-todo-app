import json
import os

def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return [] 

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)


def add_tasks(tasks):
    title= input("Enter the task title: ")
    task = {'title': title, 'completed':False}
    tasks.append(task)
    print(f'Task "{title}" added!')


def view_tasks(tasks):
    if len(tasks) ==0:
        print("No tasks found!")
    else:
        for i,task in enumerate(tasks,1):
            status = "✅" if task['completed'] else "❌"
            print(f"{i}. {task['title']} [{status}]")

def complete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark completed: "))    
        tasks[task_num - 1]['completed'] = True
        print(f"Task {task_num} mark as completed")
    except (IndexError,ValueError):
        print("Invalid task number")    

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        tasks.pop(task_num-1)
        print(f"Task {task_num} deleted.")
    except(IndexError,ValueError):
        print("Invalid task number")   

def main():
    tasks = load_tasks()

    while True:
        print("\nCommands: add, view, complete, delete, exit") 
        command = input("Enter a command: ").lower()

        if command == 'add':
            add_tasks(tasks)
        elif command == 'view':
            view_tasks(tasks)
        elif command == 'complete':
            complete_task(tasks)
        elif command == 'delete':
            delete_task(tasks)
        elif command == 'exit':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break 
        else:
            print("Invalid command. please try again")           
print("I am okay")

if __name__ == "__main__":
    main()  # This is necessary to run the main loop
