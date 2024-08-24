import random
import string

while True:
    print("Welcome to the password generator!")

    length = int(input("Enter the length of your password: "))
    num_letters = int(input("Enter the number of letters in the password: "))
    num_numbers = int(input("Enter the number of numbers in the password: "))
    num_symbols = int(input("Enter the number of symbols in the password: "))

    if length != (num_letters + num_numbers + num_symbols):
        print("Invalid input! The sum of letters, numbers, and symbols should equal the password length.")
    else:
        letters = string.ascii_letters
        numbers = string.digits
        symbols = string.punctuation

        # Generate a list with the required number of each character type
        password_list = (
            random.choices(letters, k=num_letters) +
            random.choices(numbers, k=num_numbers) +
            random.choices(symbols, k=num_symbols)
        )

        # Shuffle the list to randomize the order
        random.shuffle(password_list)

        # Join the list elements to create the final password
        password = "".join(password_list)

        print("Generated password:", password)

    # Ask the user if they want to generate another password
    again = input("Do you want to generate another password? (yes/no): ").lower()
    if again != 'yes':
        break  # Exit the loop if the user does not want to generate another password
