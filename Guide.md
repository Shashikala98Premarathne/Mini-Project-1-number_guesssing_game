Goal
The computer secretly chooses a number from 1 to 100.
The player keeps guessing until they find it.
Example interaction:
Welcome to the Number Guessing Game!

I'm thinking of a number between 1 and 100.

Enter your guess: 50
Too high!

Enter your guess: 25
Too low!

Enter your guess: 37
Correct!

You guessed the number in 3 attempts.
Requirements
Your program should:
Generate a random number between 1 and 100.
Ask the user for a guess.
Convert their input into an integer.
Compare the guess with the secret number.
Print:
"Too high!"
"Too low!"
or "Correct!"
Keep asking until the answer is correct.
Count how many guesses the player made.
Display the number of attempts at the end.
Think about the program structure
Before writing code, break the program into these pieces:
START

import what I need

generate secret number

create attempts counter

repeat:
    ask user for guess
    increase attempts

    if guess is greater than secret:
        tell user "Too high"

    elif guess is less than secret:
        tell user "Too low"

    else:
        tell user they are correct
        stop the loop

display number of attempts

END