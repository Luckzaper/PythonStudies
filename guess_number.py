#Problem Statement: Write a program in which you allow your user to guess a secret number between 1 and 10.

import random

secret_number = random.randint(1, 50)

while True:
    try:
        user_guess = int(input("Guess a number between 1 and 50:\n"))
        if user_guess < 1 or user_guess > 50:
            print("Please enter a number within the range 1-50.\n")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a whole number.\n")

while user_guess != secret_number:
    if user_guess > secret_number:
        print("The number is too high.")
    elif user_guess < secret_number:
        print("The number is too low.")
    print("You are incorrect, try again\n")
    try:
        user_guess = int(input("Guess a number between 1 and 50:\n"))
        if user_guess < 1 or user_guess > 50:
            print("Please enter a number within the range 1-50.\n")
    except ValueError:
        print("Invalid input. Please enter a whole number.\n")

print("Congrats! You guessed the correct number!")