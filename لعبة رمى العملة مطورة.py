import random

def get_user_choice():
    while True:
        choice = input("Enter your choice (1 or 2):")
        if choice in ["1", "2"]:
            return choice
        else:
            print("Choose a valid number (1 or 2)")

def get_user_guess():
    while True:
        choice = input("Enter your guess (heads or tails):").lower()
        if choice in ["heads", "tails"]:
            return choice
        else:
            print("Please enter 'heads' or 'tails'.")

def main():
    while True:
        print("Welcome to the coin guessing!")
        print("Choose a method to toss the coin:")
        print("1. using random.random()")
        print("2. using random.randint()")

        choice = get_user_choice()

        random_guess = random.random() if choice == "1" else random.randint(0, 1)
        user_guess = get_user_guess()

        if (random_guess >= 0.5 and user_guess == "heads") or (random_guess < 0.5 and user_guess == "tails"):
            print("Congratulations! You won!")
        else:
            print("Sorry, you lost!")

        print(f"The computer's coin toss result was: { 'heads' if random_guess >= 0.5 else 'tails' }")

        play_again = input("Do you want to play again? (y or n): ")
        if play_again.lower() != "y":
            break

if __name__ == "__main__":
    main()