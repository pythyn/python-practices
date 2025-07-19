# Define a function to perform arithmetic operations
def calc(n, m, o):
    if o == "+":
        return n + m
    elif o == "-":
        return n - m
    elif o == "*":
        return n * m
    elif o == "/":
        return n / m if m != 0 else "Error: Division by zero."
    elif o == "**":
        return n**m
    else:
        return "Invalid operation."


# List of supported operators, ordered to catch multi-character ones first
operators = ["**", "+", "-", "*", "/"]

# Continue running until user chooses to quit
exit_continue = "a"
while exit_continue != "q":
    non = input("Enter numbers and operation in one line:\n")

    for o in operators:
        if o in non:
            parts = non.split(o)
            try:
                first_number = float(parts[0])
                second_number = float(parts[1])
                result = calc(first_number, second_number, o)
                print(f"{first_number}{o}{second_number} = {result}")
            except ValueError:
                print(f"{non} = Error: Invalid number format.")
            break
    else:
        print(f"{non} = Error: Unknown operator.")

    # Prompt to continue or quit
    exit_continue = input(
        "\npress [q] for exit and any other key to continue!\n"
    ).lower()
