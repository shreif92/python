import random

while True:
    print("Welcome to the coin guessing!")
    print("Choose a method to toss the coin:")
    print("1. using random.random()")
    print("2. using random.randint()")

    choice = input("Enter your choice (1 or 2):")

    random_guess = random.random()
    random_guess_2 = random.randint(0, 1)

    if choice == "1":
        while True:
            choice_2 = input("Enter your guess (heads or tails):").lower()
            if choice_2 == "heads" or choice_2 == "tails":
                break
            else:
                print("Please enter 'heads' or 'tails'.")

        if random_guess >= 0.5 and choice_2 == "heads" or random_guess < 0.5 and choice_2 == "tails":
            print("Congratulations! You won!")
            print("The computer's coin toss result was: heads")
        else:
            print("Sorry, you lost!")
            print("The computer's coin toss result was: " + ("heads" if random_guess >= 0.5 else "tails"))
    elif choice == "2":
        while True:
            choice_3 = input("Enter your guess (heads or tails):").lower()
            if choice_3 == "heads" or choice_3 == "tails":
                break
            else:
                print("Please enter 'heads' or 'tails'.")

        if random_guess_2 == 1 and choice_3 == "heads" or random_guess_2 == 0 and choice_3 == "tails":
            print("Congratulations! You won!")
            print("The computer's coin toss result was: heads")
        else:
            print("Sorry, you lost!")
            print("The computer's coin toss result was: " + ("heads" if random_guess_2 == 1 else "tails"))
    else:
        print("Choose a valid number (1 or 2)")

    play_again = input("Do you want to play again? (y or n): ")
    if play_again.lower() != "y":
        break