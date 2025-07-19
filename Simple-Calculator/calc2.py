# Define a function to perform the calculation based on the operation
def calc(n, m, o):
    if o == "+":
        return n + m
    elif o == "-":
        return n - m
    elif o == "*":
        return n * m
    elif o == "/":
        if m != 0:
            return n / m
        else:
            return "Error: Division by zero."
    elif o == "**":
        return n**m  # Exponentiation
    else:
        return "Invalid operation."


# Loop until the user decides to quit
exit_countinue = "a"
while exit_countinue != "q":
    # Get user input
    first_number = float(input("Enter the first number: "))
    operation = input("Enter the operation (+ - * / **): ")
    second_number = float(input("Enter the second number: "))

    # Display the result
    print(
        f"{first_number} {operation} {second_number} = {calc(first_number, second_number, operation)}"
    )

    # Prompt to continue or quit
    exit_countinue = input("\nq for exit and any key to continue!\n")
