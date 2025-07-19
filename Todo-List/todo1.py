# Define a function to operate on the to-do list
def oper(op, tdl, task=""):
    if op == "add":
        tdl.append(task)  # Add task to the list
    elif op == "remove":
        if task in tdl:
            tdl.remove(task)  # Remove task if it exists
        else:
            print("Task not found.")
    elif op == "show":
        if not tdl:
            print("Your to-do list is empty!")  # List is empty
        else:
            for i, task in enumerate(tdl):  # Show tasks with numbers
                print(f"{i+1}.{task}")
    return


todo_list = []  # Initialize empty to-do list

# Main loop
while True:
    user_op = input("What you want to do?\n(add,remove,show,quit): ").lower().strip()

    if user_op == "show":
        oper(user_op, todo_list)

    elif user_op == "add" or user_op == "remove":
        user_task = input(f"Enter your task to {user_op}: ")
        oper(user_op, todo_list, user_task)

    elif user_op == "quit":
        break  # Exit the loop and program

    else:
        print("Not Valid")  # Handle invalid input
