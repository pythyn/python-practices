# Prompt the user for the first number and convert it to float
first_number = float(input("Enter the first number: "))

# Ask the user for the desired operation
operation = input("Enter operation (+ - * /): ")

# Prompt the user for the second number
second_number = float(input("Enter the second number: "))

# Perform the chosen arithmetic operation
if operation == "+":
    print(first_number + second_number)
elif operation == "-":
    print(first_number - second_number)
elif operation == "*":
    print(first_number * second_number)
elif operation == "/":
    print(first_number / second_number)
else:
    # Handle invalid operation input
    print("Invalid operation.")
