from random import randint

eoc = "p"  # Game loop control
while eoc == "p":

    user_guess = -1
    print("\nNew round started!")

    level = int(input("Enter the difficulty level from 1 to 10: "))
    if 1 <= level <= 10:
        difficulty = level * 50  # Set range based on level
        chance = (11 - level) * 3  # Set chances based on level
        pc_number = randint(1, difficulty)  # Random target number
    else:
        print("\nyou are an idiot")  # Input outside valid range
        continue

    while user_guess != pc_number and chance >= 0:

        if chance == 0:
            print(
                f"\nYou Lose, Next Time Better Luck!\t My number was {pc_number}"
            )
            break

        try:
            user_guess = int(
                input(
                    f"\nYou have {chance} chance\nGuess a number between 1 to {difficulty}: "
                )
            )
            if user_guess > pc_number:
                print("\nNope! My number is smaller.")
                chance -= 1
            elif user_guess < pc_number:
                print("\nNope! My number is bigger.")
                chance -= 1
            else:
                print(
                    f"\n🎉 Congrats! You guessed the number in {((11 - level) * 5) - chance} attempts."
                )
        except ValueError:
            print("Please enter a valid integer.")  # Input validation

    eoc = input(
        "\nPress [p] to play again or any key to exit: "
    ).lower()  # Continue or exit
