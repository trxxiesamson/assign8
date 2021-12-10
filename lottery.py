# Assignment 8
# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

import random

winning_num = []
user_reattempt = []

print("★ WELCOME TO LOTTO ★")
print("wanna hit the jackpot? then bet all you can!")
print("choose three numbers between 0-9\n")

for i in range (0,3):
    num = random.randint(0,10)
    while num in winning_num:
        num = random.randint(0,10)
    winning_num.append(num)

winning_num.sort()

lotto_entry = []
for i in range (0,3):
    num = int(input("Enter your lucky number: \n"))
    
    while (num in lotto_entry or num<0 or num<3):
        print("Invalid number, please try once more")
        break

    if lotto_entry == winning_num:
        print("Congratulations! You won the lottery★")
        lotto_entry.clear
        winning_num.clear

    lotto_entry.append(num)

print("\nYou loss")
print("The winning numbers are: ")
print(winning_num)
print("★・・・・・・★・・・・・・★・・・・・・★")
print("While your lotto entry numbers are: ")
print(f"{lotto_entry}\n")

user_reattempt = str(input("Want to try and play once more? Enter YES or NO \n"))
if user_reattempt == 'y':
        for b in range(0,3):
                    winning_num = random.randint(0,9)

                    while winning_num:
                        winning_num = random.randint(0,9)
                    
else:
    user_reattempt == 'n'
    print("Thank you for playing lottery! Feel free to come back again")