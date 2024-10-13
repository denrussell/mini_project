'''
1. User Interface (UI):
Create a command-line interface (CLI) for the To-Do List Application.
Display a welcoming message and a menu with the following options:
        Welcome to the To-Do List App!

        Menu:
        1. Add a task
        2. View tasks
        3. Mark a task as complete
        4. Delete a task
        5. Quit
'''
todo_list = []
print("Welcome to your To-Do List Application!")
print(" 1. Add a task\n 2. View tasks\n 3. Mark a task as complete\n 4. Delete a task\n 5. Quit")

# create all the functions and use pass for now
def add_task():
    task_to_add = input("Enter task to add: ")
    if task_to_add:
        todo_list.append({"Title": task_to_add, "Status": "Incomplete"})
        print(f"\n\u2713\u2713\u2713\u2713\u2713\u2713\u2713\u2713\u2713 Task '{task_to_add}' has been added. \u2713\u2713\u2713\u2713\u2713\u2713\u2713\u2713\u2713\n")
    else:
        print("Task cannot be empty.")

def view_task():
    if todo_list:
        print("\nTo-Do Lists:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task["Title"]} - {task["Status"]}")
    else:
        print("\n>>>>>>>>>>>>>>>>> No tasks found. Your To-Do list is empty. <<<<<<<<<<<<<<<<<\n")

def mark_task_complete():
    try:
        view_task()
        task_number = int(input("Enter the number you want to mark as 'Complete': "))
        if 1 <= task_number <= len(todo_list):
            todo_list[task_number -1]["Status"] = "Complete"
            print(f"\n>>>>>>>>>>>>>> Task '{todo_list[task_number -1]["Title"]}' marked as complete.")
        else:
            print("Invalid.")
    except ValueError:
        print("Please enter a valid task number.")

def delete_task():
    try:
        view_task()
        task_number = int(input("Please enter the number of the task to delete: "))
        if 1 <= task_number <= len(todo_list):
            remove_task = todo_list.pop(task_number -1)
            print(f"\n>>>>>>>>>>>>> Task {remove_task["Title"]} has been deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid task number.")

# create a while loop for user input until quit.
while True:
    try:
        user_choice = int(input("Please select an option (1-5): "))

# create if statements for user choices
        if user_choice == 1:
            add_task()
        elif user_choice == 2:
            view_task()
        elif user_choice == 3:
            mark_task_complete()
        elif user_choice == 4:
            delete_task()
        elif user_choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select again.")
    except ValueError:
        print("Invalid. Please enter a number.")
    finally:
        print("\n\nReturning to the menu.")
        print("Welcome to your To-Do List Application!")
        print(" 1. Add a task\n 2. View tasks\n 3. Mark a task as complete\n 4. Delete a task\n 5. Quit")
