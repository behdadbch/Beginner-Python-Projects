# To-Do List Application

## 📝 Description

This is a simple command-line **To-Do List Application** that allows you to:

- Add new tasks
- View all tasks
- Remove tasks by their number
- Mark tasks as completed

Your tasks are saved in a text file (`tasks.txt`), so they persist even after you close the program.

## 🧰 Key Concepts Covered

- File Handling (`open`, `read`, `write`, `close`)
- Lists and Data Structures
- Functions and Modular Code
- String Manipulation
- Exception Handling
- User Input and Output

## 🚀 How to Run the Application

### Prerequisites

- Python 3.x installed on your machine.
- Access to a command-line interface (CLI) or terminal.

### Steps

1. **Navigate to the project directory**:

   ```bash
   cd todo_list
Run the application:
bash
Copy code
python main.py
Follow the on-screen instructions to interact with your to-do list.
📖 Usage Instructions

Upon running the application, you'll be presented with a menu:

mathematica
Copy code
==== To-Do List ====
1. View Tasks
2. Add Task
3. Remove Task
4. Mark Task as Completed
5. Exit
Select an option (1-5):
Options:
View Tasks: Displays all current tasks with their status (Pending/Completed).
Add Task: Prompts you to enter a new task to add to your list.
Remove Task: Allows you to remove a task by entering its number from the list.
Mark Task as Completed: Lets you mark a task as completed by its number.
Exit: Saves your tasks and exits the application.
📄 Sample Output

mathematica
Copy code
==== To-Do List ====
1. View Tasks
2. Add Task
3. Remove Task
4. Mark Task as Completed
5. Exit
Select an option (1-5): 2

Enter the task to add: Buy groceries
Task added successfully!

==== To-Do List ====
1. View Tasks
2. Add Task
3. Remove Task
4. Mark Task as Completed
5. Exit
Select an option (1-5): 1

Your Tasks:
1. [ ] Buy groceries

==== To-Do List ====
1. View Tasks
2. Add Task
3. Remove Task
4. Mark Task as Completed
5. Exit
Select an option (1-5): 4

Enter the number of the task to mark as completed: 1
Task marked as completed!

==== To-Do List ====
1. View Tasks
2. Add Task
3. Remove Task
4. Mark Task as Completed
5. Exit
Select an option (1-5): 1

Your Tasks:
1. [x] Buy groceries

==== To-Do List ====
1. View Tasks
2. Add Task
3. Remove Task
4. Mark Task as Completed
5. Exit
Select an option (1-5): 5

Saving tasks and exiting the application. Goodbye!
🛠️ Code Overview

The application is structured with functions for each main feature:

load_tasks(): Loads tasks from the tasks.txt file.
save_tasks(tasks): Saves tasks to the tasks.txt file.
display_tasks(tasks): Displays the current list of tasks.
add_task(tasks): Adds a new task to the list.
remove_task(tasks): Removes a task by its number.
mark_task_completed(tasks): Marks a task as completed.
main(): The main loop that displays the menu and handles user choices.
Modules Used
os.path: To check if the tasks.txt file exists before loading.
sys: For system-specific parameters and functions.
🤝 Contributing

Contributions are welcome! If you have ideas to enhance this application, feel free to fork the repository and submit a pull request.

📧 Contact

If you have any questions or suggestions, feel free to reach out by creating an issue in the repository.