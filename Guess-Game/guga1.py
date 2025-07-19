from random import randint


def guga(g):  # Check guess and give feedback
    if user_guess > pc_number:
        print("Nope! My number is smaller.")
    elif user_guess < pc_number:
        print("Nope! My number is bigger.")
    else:
        print("🎉 Congrats! You guessed it.")


eoc = "p"  # Play control
while eoc == "p":
    pc_number = randint(1, 100)
    user_guess = -1
    print("\nNew round started!")

    while user_guess != pc_number:
        try:
            user_guess = int(input("Guess a number between 1 to 100: "))
            guga(user_guess)
        except ValueError:
            print("Please enter a valid integer.")

    eoc = input(
        "\nPress [p] to play again or any key to exit: "
    ).lower()
