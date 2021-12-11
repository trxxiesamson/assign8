# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

import random

random_num = random.randint(0,100)

print("Number Guessing Game")
Player_Username = input("Hello! Enter your player name: \n")
Take_Guess = 0

print(f"Hello {Player_Username}! Think of a certain number between 0 up to 100: ")

while Take_Guess < 100:
    assumption = int(input())
    Take_Guess += 1
    if assumption < random_num:
        print("Your number is LESS than the one I'm thinking of. Try once more!")
    if assumption > random_num:
        print("Your number is GREATER than the number that I have in mind. Attempt again!")
    if assumption == random_num:
        break
if assumption == random_num:
    print("The number that you guessed is", assumption)
    print("The correct number is", random_num)
    print("Great★彡! You guessed the correct number in " + str(Take_Guess) + " tries")
else:
    print("You did not guess the correct number. The number was " + str(random_num))