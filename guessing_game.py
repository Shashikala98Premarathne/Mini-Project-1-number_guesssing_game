#Importing the required libraries
import numpy as np
import pandas as pd
import random

#User input for name
name = input("Enter your name: ")
print(f"Hello {name}! Welcome to the Number Guessing Game. You have 10 attempts. Good luck!")

#Generating a random number between 1 and 100
secret_number = random.randint(1, 100)
quit_game = False

#Getting and validating user input to guess the number
for no_of_guesses in range(1, 11):
    while True:
        try:
            guess = input("I have a number in my mind. Hint: It's between 1 and 100. 😉 (or 'q' to quit) "
                              f"Please give me your guess: ")
            if guess.lower() == "q":
                quit_game = True
                break

            guess = int(guess)
            if guess < 1 or guess > 100:
                raise ValueError("Please enter a number between 1 and 100.")
            break

        except ValueError as e:
            print(e)
            continue

    #If the user chooses to quit the game    
    if quit_game:
        print(f"Thanks for playing, {name}! 👋")
        break

#Calculating the number of attempts left and checking if the guess is correct
    attempts_left = 10 - no_of_guesses
    if guess == secret_number:
        if no_of_guesses == 1:
            print(f"Congratulations {name}! You nailed it on the first try! 🔥🎯 " 
                  f"The number was {secret_number}.")
        else:
            print(f"Congratulations {name}! "
                  f"You guessed the number {secret_number} in {no_of_guesses} attempts. 🥳")
        break

#Checking how close the guess is to the secret number
    difference = abs(guess - secret_number)
    if difference <= 5:
        print(f"Fire! You're very close!🔥 {attempts_left} attempts left.")
    elif difference <= 10:
        print(f"Wow! You're close! 😮‍💨🫣 {attempts_left} attempts left.")
    elif difference <= 20:
        print(f"You're getting warmer! 😮 {attempts_left} attempts left.")
    elif difference <= 30:
        print(f"You're getting cold! 😑❄️ {attempts_left} attempts left.")
    else:
        print(f"Wrong direction! You're very cold! 😩🥶 {attempts_left} attempts left.")

else:
    # If the user runs out of attempts, reveal the secret number
    print(
        f"Sorry {name}, you've used all your attempts.☹️ "
        f"The secret number was {secret_number}. Better luck next time! ✨🧚"
    )
