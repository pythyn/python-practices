# Define a function to perform operations on the to-do list
def oper(op, tdl, task=""):
    if op == "add":
        tdl.append(task)  # Add a task
    elif op == "remove":
        if task in tdl:
            tdl.remove(task)  # Remove the task if it exists
        else:
            print("Task not found.")
    elif op == "show":
        if not tdl:
            print("Your to-do list is empty!")
        else:
            for i, task in enumerate(tdl):  # Display all tasks
                print(f"{i+1}. {task}")
    return


# Ask the user whether to load tasks from a file
while True:
    readfile = input("Load tasks from file? (y,n): ").lower().strip()
    if readfile == "y":
        filepath = input("Enter the file path: ")
        try:
            with open(filepath, "r") as f:
                todo_list = [x.strip() for x in f.readlines()]  # Load tasks
            print("File loaded successfully")
            break
        except FileNotFoundError:
            print("File not found, enter a valid path.")

    elif readfile == "n":
        todo_list = []  # Start with an empty list
        break

    else:
        print("Invalid.")  # Handle invalid input


# Main loop for user operations
while True:
    user_op = (
        input("What you want to do?\n(add,remove,show,save,quit): ").lower().strip()
    )

    if user_op == "show":
        oper(user_op, todo_list)

    elif user_op == "add" or user_op == "remove":
        user_task = input(f"Enter your task to {user_op}: ")
        oper(user_op, todo_list, user_task)

    elif user_op == "save":
        with open("./todolist.txt", "w") as f:
            for task in todo_list:
                f.write(f"{task}\n")  # Save tasks to file

    elif user_op == "quit":
        break  # Exit the program

    else:
        print("Not Valid")  # Handle unknown commands
