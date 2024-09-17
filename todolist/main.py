
import os.path

def load_tasks():
    """
    Loads tasks from tasks.txt if it exists.
    Returns a list of tasks.
    """
    tasks = []
    if os.path.exists('tasks.txt'):
        with open('tasks.txt', 'r') as file:
            for line in file:
                task_data = line.strip().split('||')
                if len(task_data) == 2:
                    tasks.append({'task': task_data[0], 'completed': task_data[1] == 'True'})
    return tasks

def save_tasks(tasks):
    """
    Saves tasks to tasks.txt.
    """
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(f"{task['task']}||{task['completed']}\n")

def display_tasks(tasks):
    """
    Displays all the tasks with their status.
    """
    if not tasks:
        print("\nYour task list is empty!\n")
        return

    print("\nYour Tasks:")
    for idx, task in enumerate(tasks, 1):
        status = '[x]' if task['completed'] else '[ ]'
        print(f"{idx}. {status} {task['task']}")
    print()

def add_task(tasks):
    """
    Adds a new task to the list.
    """
    task_input = input("\nEnter the task to add: ").strip()
    if task_input:
        tasks.append({'task': task_input, 'completed': False})
        print("Task added successfully!\n")
    else:
        print("No task entered. Returning to the menu.\n")

def remove_task(tasks):
    """
    Removes a task by its number.
    """
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Removed task: {removed_task['task']}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def mark_task_completed(tasks):
    """
    Marks a task as completed.
    """
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['completed'] = True
            print("Task marked as completed!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    """
    Main function to run the To-Do List application.
    """
    tasks = load_tasks()

    while True:
        print("==== To-Do List ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Exit")
        choice = input("Select an option (1-5): ").strip()

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            mark_task_completed(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("\nSaving tasks and exiting the application. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select a valid option.\n")

if __name__ == "__main__":
    main()
